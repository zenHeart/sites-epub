#!/usr/bin/env python3
"""Fail if a packed EPUB has broken images or unlinked page titles."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub.walk import blocking_defects, format_walk_log, walk_chapters


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("epub", type=Path)
    args = parser.parse_args(argv)
    report = walk_chapters(args.epub)
    broken = [
        (c.chapter, d)
        for c in report.chapters
        for d in blocking_defects(c.defects)
    ]
    print(format_walk_log(report), end="")
    cover_leak = _check_cover_title(args.epub)
    if cover_leak:
        print(f"FAIL cover title leak: {cover_leak}", file=sys.stderr)
        return 1
    if broken:
        print("blocking:", broken[:8], file=sys.stderr)
        return 1
    return 0


def _check_cover_title(epub: Path) -> str | None:
    """Guard against hardcoded vendor strings leaking into another vendor's EPUB.

    The cover.xhtml title was hardcoded to ``ChatGPT Codex Docs`` when codex was
    first shipped, leaking the wrong vendor name into claude/codex/cursor/grok
    EPUBs. Metadata.yaml carries the canonical title; cross-check that cover.xhtml
    does not embed a stale hardcoded vendor title.
    """
    import zipfile

    try:
        with zipfile.ZipFile(epub) as zf:
            cover_text = ""
            opf_text = ""
            yaml_text = ""
            for name in zf.namelist():
                if name.endswith("cover.xhtml"):
                    cover_text = zf.read(name).decode("utf-8", errors="replace")
                elif name.endswith(".opf"):
                    opf_text = zf.read(name).decode("utf-8", errors="replace")
                elif name.endswith((".yaml", ".yml")) and "metadata" in name:
                    yaml_text = zf.read(name).decode("utf-8", errors="replace")
    except Exception as exc:
        return f"unable to scan ({exc})"
    if not cover_text and not opf_text:
        return None
    forbidden = ("ChatGPT Codex Docs", "ChatGPT Codex", "learn.chatgpt.com/docs")
    for s in forbidden:
        if s in cover_text:
            return f"cover.xhtml leaks hardcoded title: {s!r}"
        if s in opf_text and "<dc:title>" in opf_text:
            return f"OPF leaks hardcoded title: {s!r}"
    if yaml_text:
        m = re.search(r"^title:\s*(.+)$", yaml_text, flags=re.M)
        yaml_title = m.group(1).strip() if m else ""
        if any(s in yaml_title for s in forbidden):
            return f"metadata.yaml leaks hardcoded title: {yaml_title!r}"
    return None


if __name__ == "__main__":
    raise SystemExit(main())
