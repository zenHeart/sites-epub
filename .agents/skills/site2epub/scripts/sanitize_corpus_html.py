"""Post-fetch corpus maintenance: strip script/style/template blocks from stored
HTML pages, report leftover secret-shaped strings and mojibake (gzip stored as text).

Usage: python sanitize_corpus_html.py <vendor_id>

Why: devsite page-template JS embeds public API-explorer keys that trip GitHub
secret-scanning; script content is dead weight at pack time (sanitize_body_html
decomposes it). Mojibake pages mean http.py failed to decompress a gzipped
response (lessons #12) — fix http layer, then refetch, never edit by hand:
refetch will revert manual corpus edits (lessons #4).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

SCRIPT_RE = re.compile(r"<script\b[^>]*>[\s\S]*?</script\s*>", re.I)
SCRIPT_OPEN_RE = re.compile(r"<script\b[^>]*>[\s\S]*\Z", re.I)  # unterminated script
STYLE_RE = re.compile(r"<style\b[^>]*>[\s\S]*?</style\s*>", re.I)
TEMPLATE_RE = re.compile(r"<template\b[^>]*>[\s\S]*?</template\s*>", re.I)

SECRET_PATTERNS = {
    "google AIza": r"AIza[0-9A-Za-z_\-]{30,}",
    "openai sk": r"sk-[A-Za-z0-9]{20,}",
    "anthropic": r"sk-ant-[A-Za-z0-9_\-]{20,}",
    "xai": r"xai-[A-Za-z0-9]{20,}",
    "aws": r"AKIA[0-9A-Z]{16}",
    "gh token": r"gh[pousr]_[A-Za-z0-9]{20,}",
}


def main(vendor: str) -> int:
    pages = ROOT / "vendors" / vendor / "corpus" / "pages"
    if not pages.is_dir():
        print(f"no corpus for {vendor}: {pages}")
        return 1
    changed = 0
    for p in pages.glob("**/*.md"):
        t = p.read_text(encoding="utf-8", errors="replace")
        if not t.lstrip().lower().startswith("<!"):
            continue
        new = TEMPLATE_RE.sub("", STYLE_RE.sub("", SCRIPT_OPEN_RE.sub("", SCRIPT_RE.sub("", t))))
        if new != t:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"pages stripped: {changed}")

    hits, moji = [], []
    for p in pages.glob("**/*.md"):
        raw = p.read_bytes()
        if raw.count(b"\xef\xbf\xbd") > 20 or raw[:3] == b"\x1f\x8b":
            moji.append(p.relative_to(pages).as_posix())
        t = raw.decode("utf-8", errors="replace")
        for name, pat in SECRET_PATTERNS.items():
            m = re.search(pat, t)
            if m:
                hits.append((name, p.name, m.group(0)[:14]))
    for h in hits:
        print("SECRET HIT:", *h)
    for mpath in moji:
        print("MOJIBAKE PAGE (fix http decompression, then refetch):", mpath)
    print(f"secret hits: {len(hits)}, mojibake pages: {len(moji)}")
    return 1 if (hits or moji) else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
