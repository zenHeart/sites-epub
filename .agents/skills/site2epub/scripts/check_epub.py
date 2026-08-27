#!/usr/bin/env python3
"""Fail if a packed EPUB has broken images or unlinked page titles."""

from __future__ import annotations

import argparse
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
    if broken:
        print("blocking:", broken[:8], file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
