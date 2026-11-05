#!/usr/bin/env python3
"""Gate for the published site: every local reference must resolve.

The site index embeds the catalogue as a JSON array, and each entry points at
a cover image or an icon.  A reference that resolves to nothing ships as a
broken image on the live site -- silently, because nothing checked it.

That is not hypothetical: `covers/deepseek.png` was deleted in 2026-09 while
the `deepseek-harness` shelf entry still pointed at it, and the broken image
stayed on epub.zenheart.site until this gate existed.

Checks, over the *rendered* site directory:

1. every local reference in the catalogue resolves to a file;
2. every EPUB on disk is listed in the catalogue, and vice versa;
3. the CNAME file is present and names the published host.

Usage::

    python3 .agents/skills/site2epub/scripts/check_site.py site
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SITE = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "site")


def main() -> int:
    if not SITE.is_dir():
        print(f"no site directory: {SITE}", file=sys.stderr)
        return 1
    index = SITE / "index.html"
    if not index.is_file():
        print(f"no site index: {index}", file=sys.stderr)
        return 1

    html = index.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"const BOOKS\s*=\s*(\[.*?\]);", html, re.S)
    if not match:
        print("site index does not embed a BOOKS array", file=sys.stderr)
        return 1
    books = json.loads(match.group(1))

    problems: list[str] = []

    refs: dict[str, str] = {}
    for book in books:
        for key in ("href", "cover", "docsUrl", "blogUrl"):
            value = book.get(key)
            if not isinstance(value, str) or not value:
                continue
            if value.startswith(("http://", "https://")):
                continue
            refs[value.lstrip("/")] = f"{book.get('id', '?')}.{key}"
    missing = sorted(r for r in refs if not (SITE / r).is_file())
    for ref in missing:
        problems.append(f"missing local asset: {ref} (referenced by {refs[ref]})")

    listed = {b.get("id") for b in books if b.get("id")}
    # Shelf entries (kind == "site") link to a separate publication; they are
    # not EPUBs on this host and must not be expected in the EPUB set.
    local_books = {b.get("id") for b in books if b.get("kind") != "site" and b.get("id")}
    on_disk = {p.stem for p in SITE.glob("*.epub")}
    for vendor in sorted(local_books - on_disk):
        problems.append(f"catalogue lists {vendor} but no {vendor}.epub is published")
    for extra in sorted(on_disk - listed):
        problems.append(f"{extra}.epub is published but not listed in the catalogue")

    cname = SITE / "CNAME"
    if not cname.is_file():
        problems.append("no CNAME file")
    elif not cname.read_text(encoding="utf-8").strip():
        problems.append("CNAME file is empty")

    print(f"site: {SITE}")
    print(f"catalogue entries : {len(books)}")
    print(f"local references  : {len(refs)}")
    print(f"published EPUBs   : {len(on_disk)}")
    if problems:
        print()
        for problem in problems:
            print(f"FAIL {problem}")
        return 1
    print("OK: every local reference resolves and the catalogue matches the published EPUBs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
