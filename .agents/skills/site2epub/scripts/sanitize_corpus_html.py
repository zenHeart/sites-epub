"""Post-fetch corpus maintenance: strip script/style/template blocks from stored
HTML pages, replace secret-shaped strings with readable placeholders, and report
whatever is still left plus any mojibake (gzip stored as text).

Usage: python sanitize_corpus_html.py <vendor_id> [--report-only]

Why: devsite page-template JS embeds public API-explorer keys that trip GitHub
secret-scanning; script content is dead weight at pack time (sanitize_body_html
decomposes it). Mojibake pages mean http.py failed to decompress a gzipped
response (lessons #12) — fix http layer, then refetch, never edit by hand:
refetch will revert manual corpus edits (lessons #4).

Secret replacement keeps the vendor prefix so the doc example still reads as a
credential, but is short enough that it no longer matches its own pattern
(lessons #19). Because refetch re-imports the original secret, this pass has to
run after every fetch — which is why it replaces by default.
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
    "anthropic": r"sk-ant-[A-Za-z0-9_\-]{20,}",
    "openai sk": r"sk-[A-Za-z0-9]{20,}",
    "xai": r"xai-[A-Za-z0-9]{20,}",
    "aws": r"AKIA[0-9A-Z]{16}",
    "gh token": r"gh[pousr]_[A-Za-z0-9]{20,}",
}

#: name -> (regex matching the whole secret, replacement keeping the prefix).
#: Every placeholder is deliberately shorter than its own pattern's tail so
#: the rewritten page cannot re-trigger the detector.
SECRET_FIXES = {
    "google AIza": (r"(AIza)[0-9A-Za-z_\-]{30,}", r"\1YOUR_API_KEY"),
    "anthropic": (r"(sk-ant-)[A-Za-z0-9_\-]{20,}", r"\1YOUR_API_KEY"),
    "openai sk": (r"(sk-)[A-Za-z0-9]{20,}", r"\1YOUR_API_KEY"),
    "xai": (r"(xai-)[A-Za-z0-9]{20,}", r"\1YOUR_API_KEY"),
    "aws": (r"(AKIA)[0-9A-Z]{16}", r"\1YOUR_ACCESS_KEY"),
    "gh token": (r"(gh[pousr]_)[A-Za-z0-9]{20,}", r"\1YOUR_TOKEN"),
}


def _fix_secrets(text: str) -> str:
    """Replace secret-shaped runs with prefixed placeholders."""
    for fix_re, repl in SECRET_FIXES.values():
        text = re.sub(fix_re, repl, text)
    return text


def main(vendor: str, report_only: bool = False) -> int:
    pages = ROOT / "vendors" / vendor / "corpus" / "pages"
    if not pages.is_dir():
        print(f"no corpus for {vendor}: {pages}")
        return 1
    changed = 0
    for p in pages.glob("**/*.md"):
        t = p.read_text(encoding="utf-8", errors="replace")
        new = t
        if t.lstrip().lower().startswith("<!"):
            new = TEMPLATE_RE.sub("", STYLE_RE.sub("", SCRIPT_OPEN_RE.sub("", SCRIPT_RE.sub("", t))))
        if not report_only:
            new = _fix_secrets(new)
        if new != t and not report_only:
            p.write_text(new, encoding="utf-8")
            changed += 1
    print(f"pages rewritten: {changed}")

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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    report_only = "--report-only" in sys.argv[1:]
    if len(args) != 1:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(args[0], report_only=report_only))
