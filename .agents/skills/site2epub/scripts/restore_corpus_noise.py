#!/usr/bin/env python3
"""Restore corpus files whose diff is pure build/deploy noise (lessons.md §23).

`vendor_pack_key` hashes EVERY file under `vendors/<id>/corpus/`, so byte-level
noise in files that carry no book content forces a full rebuild of that book:

  * `corpus/image-map.json`  — compile.py writes it without a trailing newline
  * `corpus/docs.html`       — raw docs-listing snapshot, Vercel `dpl=` deploy id
  * `corpus/blog.html`       — raw blog-listing snapshot, Vercel `dpl=` deploy id
  * `corpus/llms.txt`        — index text embedding Next.js build id / timestamps

None of these are read by `pack_vendor` (it packs from routes.json + pages/), so
when the only difference is noise we restore the HEAD bytes and the book is
correctly treated as unchanged.

The decision is conservative: we normalize the known noise patterns and only
restore when the normalized text is byte-identical to HEAD. A real content
change never normalizes away, so it is always kept.

Usage: restore_noise.py [vendor_id ...]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

#: (path-suffix, list of (regex, replacement)) — normalization applied to BOTH
#: the HEAD version and the working-tree version before comparing.
NOISE_PATTERNS = {
    "corpus/image-map.json": [],
    "corpus/docs.html": [
        (re.compile(r"dpl=dpl_[A-Za-z0-9]+"), "dpl=dpl_X"),
        (re.compile(r"(?<=[\./])[A-Za-z0-9_\-]{8}(?=\.(?:js|css))"), "HASH"),
    ],
    "corpus/blog.html": [
        (re.compile(r"dpl=dpl_[A-Za-z0-9]+"), "dpl=dpl_X"),
        (re.compile(r"(?<=[\./])[A-Za-z0-9_\-]{8}(?=\.(?:js|css))"), "HASH"),
    ],
    "corpus/llms.txt": [
        (re.compile(r"dataUpdatedAt\"?\s*[:=]\s*\d+"), "dataUpdatedAt:X"),
        (re.compile(r"dehydratedAt\"?\s*[:=]\s*\d+"), "dehydratedAt:X"),
        (re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z"), "TIMESTAMP"),
        (re.compile(r"\d{2}:\d{2}:\d{2}\.\d{3}Z"), "TIMESTAMP"),
        (re.compile(r"buildId[\"'\s:=]+[A-Za-z0-9_\-]+"), "buildId:X"),
        (re.compile(r"static/(js|css)/[A-Za-z0-9_\-]+/([a-zA-Z0-9_\-]+)\.[A-Za-z0-9]{8}\.(js|css)"), r"static/\1/\2.HASH.\3"),
        # release / build hashes embedded in inline scripts
        (re.compile(r"(\"rel\"\s*:\s*\")[0-9a-f]{6,10}(\")"), r"\1X\2"),
        (re.compile(r"(\"buildId\"\s*:\s*\")[^\"]*(\")"), r"\1X\2"),
        (re.compile(r"\b[0-9a-f]{40}\b"), "HASH40"),
        # Vite / bundler asset hashes: style.3zaY0nzc.css, app.BGcK8dKj.js,
        # index.md.Djfvhn-i.lean.js, assets/Cd35j_JO2.js
        (re.compile(r"(?<=[\./])[A-Za-z0-9_\-]{8,10}(?=\.(?:[A-Za-z0-9_\-]*\.)?(?:js|css|woff2|woff))"), "HASH"),
        (re.compile(r"(?<=/)[A-Za-z0-9_\-]{8,10}(?=\.(?:[A-Za-z0-9_\-]*\.)?(?:js|css|woff2|woff))"), "HASH"),
        # explicit build stamps:
        #   <!-- pre,cn,c63ec83,2026-10-23 16:15:43 -->
        #   <meta name="build-info" content="prod / main@aafbbf51beed / build 2026/10/19 11:15:33 / commit ...">
        (re.compile(r"(?<=pre,[a-z]{2},)[0-9a-f]{6,10}"), "HASH"),
        (re.compile(r"main@[0-9a-f]{8,}"), "main@HASH"),
        (re.compile(r"(?<=gitCommit:`)[0-9a-f]{8,}"), "HASH"),
        (re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"), "TIMESTAMP"),
        (re.compile(r"\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{2}:\d{2}"), "TIMESTAMP"),
    ],
}


def git_show(rel: str) -> bytes | None:
    res = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True)
    return res.stdout if res.returncode == 0 else None


def normalize(raw: bytes, patterns) -> bytes:
    text = raw.decode("utf-8", errors="replace")
    for rx, repl in patterns:
        text = rx.sub(repl, text)
    return text.encode("utf-8")


def main(vids: list[str]) -> int:
    if not vids:
        vids = sorted(p.name for p in (ROOT / "vendors").iterdir() if p.is_dir())
    restored, kept = [], []
    for vid in vids:
        for suffix, patterns in NOISE_PATTERNS.items():
            rel = f"vendors/{vid}/{suffix}"
            path = ROOT / rel
            if not path.exists():
                continue
            cur = path.read_bytes()
            old = git_show(rel)
            if old is None or cur == old:
                continue
            # trailing-newline-only difference
            if old.rstrip(b"\n") == cur.rstrip(b"\n"):
                path.write_bytes(old)
                restored.append(rel)
                continue
            if normalize(old, patterns) == normalize(cur, patterns):
                path.write_bytes(old)
                restored.append(rel)
            else:
                kept.append(rel)
    print(json.dumps({"restored": restored, "kept_changed": kept}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main([a for a in sys.argv[1:] if not a.startswith("-")]))
