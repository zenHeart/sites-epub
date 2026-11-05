#!/usr/bin/env python3
"""Locate the page that makes a book lose its structure.

A book can lose its whole structure to a single page: pandoc's HTML reader
treats an element carrying ``role="main"`` as the *document body* and drops
everything around it, so one such page inside a volume leaves the EPUB with
one chapter instead of hundreds. The page converts perfectly well on its own,
which is why the defect only shows up once the page is embedded.

The first version of this diagnostic (issue #5) bisected by *bytes* and then
looped forever on its last step: with one candidate page left, ``half`` became
0, the empty half was skipped and the other half was the same page again, so
the script re-tested the same single page 357,666 times without ever
concluding.

Two rules keep it finite and truthful here:

* **Cut by page, not by byte.** Every candidate is a complete document built
  by the packer's own :func:`grouped_html`, so a truncated fragment can never
  be mistaken for a broken book.
* **A one-element candidate is the answer.** When only one page is left it is
  tested directly and reported; it is never re-split into itself.

The bisect narrows over *prefixes* of the page list. The predicate "does this
prefix collapse the book" is monotone in the number of pages (a prefix
collapses exactly when it contains a trigger), so a binary search finds the
first collapsing prefix in O(log n) pandoc runs. The page that entered the
book at that step is the trigger.

Usage::

    python3 .agents/skills/site2epub/scripts/bisect_pages.py --id gemini
    python3 .agents/skills/site2epub/scripts/bisect_pages.py --id gemini --scan

``--scan`` tests every page on its own instead of bisecting. It is slower but
finds *all* single-page triggers, not just the first one.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub.compile import corpus_dir  # noqa: E402
from sites_epub.epub_pack import grouped_html  # noqa: E402
from sites_epub.models import IndexEntry, Vendor  # noqa: E402
from sites_epub.page import extract_page  # noqa: E402


def load_catalog(root: Path) -> dict[str, Vendor]:
    data = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    out: dict[str, Vendor] = {}
    for entry in data.get("vendors", []):
        vendor = Vendor(
            id=entry["id"],
            name=entry.get("name", entry["id"]),
            docs_url=entry.get("docs_url", ""),
            blog_url=entry.get("blog_url"),
            icon=entry.get("icon", f"vendors/{entry['id']}/icon.png"),
            author=entry.get("author", ""),
            adapter=entry.get("adapter", "generic"),
            summary=entry.get("summary", ""),
            cover=entry.get("cover", ""),
        )
        out[vendor.id] = vendor
    return out


def load_entries(corpus: Path) -> list[IndexEntry]:
    raw = json.loads((corpus / "routes.json").read_text(encoding="utf-8"))
    return [
        IndexEntry(
            group=d.get("group", ""),
            title=d.get("title", ""),
            md_url=d.get("md_url", ""),
            html_url=d.get("html_url", ""),
            route=d.get("route", ""),
            kind=d.get("kind", "doc"),
        )
        for d in raw
    ]


def load_pages(corpus: Path, entries: list[IndexEntry]) -> list:
    """Extract the corpus through the packer's own page extractor."""
    pages = []
    for entry in entries:
        path = corpus / "pages" / f"{entry.route}.md"
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        kind = "html" if text.lstrip().lower().startswith("<!") else "md"
        try:
            page = extract_page(
                text, route=entry.route, group=entry.group, url=entry.html_url, kind=kind
            )
        except Exception:  # noqa: BLE001
            continue
        page.group = entry.group
        page.route = entry.route
        pages.append(page)
    return pages


def measure(pages: list, entries: list[IndexEntry], title: str, work: Path) -> dict:
    """Pack *pages* with pandoc and report the structure that survived."""
    html_path = work / "book.html"
    html_path.write_text(
        grouped_html(pages, entries=entries, title=title, author=""), encoding="utf-8"
    )
    out = work / "book.epub"
    if out.exists():
        out.unlink()
    proc = subprocess.run(
        [
            "pandoc",
            str(html_path),
            "-f",
            "html",
            "-t",
            "epub3",
            "-o",
            str(out),
            "--toc",
            "--split-level=1",
            f"--resource-path={work}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0 or not out.is_file():
        return {"ok": False, "h2": 0, "doc_page": 0, "error": (proc.stderr or "").strip()[:400]}
    with zipfile.ZipFile(out) as zf:
        blob = "".join(
            zf.read(name).decode("utf-8", "replace")
            for name in zf.namelist()
            if name.startswith("EPUB/text/")
        )
    return {
        "ok": True,
        "h2": blob.count("<h2"),
        # Pandoc rewrites the wrapper's class attribute (``class="doc-page"``
        # becomes ``class="level2 page-title doc-page"``), so the marker is
        # matched by name rather than by an exact attribute string.
        "doc_page": blob.count("doc-page"),
        "error": "",
    }


def is_collapsed(result: dict) -> bool:
    """True when a measured book lost its page structure."""
    if not result["ok"]:
        return True
    return result["doc_page"] == 0 or result["h2"] == 0


def collapses(pages: list, entries: list[IndexEntry], title: str, work: Path) -> bool:
    """True when the book built from *pages* lost its page structure."""
    return is_collapsed(measure(pages, entries, title, work))


def bisect_trigger(
    pages: list,
    entries: list[IndexEntry],
    title: str,
    work: Path,
    probe=None,
) -> dict:
    """Find the first page that collapses the book.

    *probe* is the predicate used to test a candidate page list; it defaults to
    packing the candidate with pandoc. Tests inject their own predicate so the
    search logic can be exercised without a pandoc run per candidate.

    Returns ``{"trigger": route, "trigger_index": i}`` when a single page is
    responsible, and ``{"trigger": None, ...}`` when the book is healthy or
    when no single page reproduces the collapse on its own.
    """
    total = len(pages)
    report: dict = {
        "pages": total,
        "trigger": None,
        "trigger_index": None,
        "collapse_at": None,
        "full_set": None,
        "reason": "",
    }
    if total == 0:
        report["reason"] = "no pages loaded"
        return report

    if probe is None:
        def probe(candidate: list) -> bool:
            return collapses(candidate, entries, title, work)

    full = measure(pages, entries, title, work)
    report["full_set"] = full
    if not is_collapsed(full) and not probe(pages):
        report["reason"] = "the full book keeps its structure; no trigger page"
        return report

    # Binary search over prefix length. The predicate is monotone: a prefix
    # collapses exactly when it contains a trigger page.
    lo, hi = 1, total
    first_bad = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if probe(pages[:mid]):
            first_bad = mid
            hi = mid - 1
        else:
            lo = mid + 1

    if first_bad is None:
        report["reason"] = "the full book collapses but no prefix does; not a single-page trigger"
        return report

    report["collapse_at"] = first_bad
    # The trigger is the page that entered the book at the collapsing prefix.
    # A one-element candidate is the answer: it is tested, never re-split.
    candidate = pages[first_bad - 1]
    report["single_page"] = measure([candidate], entries, title, work)
    if probe([candidate]):
        report["trigger"] = candidate.route
        report["trigger_index"] = first_bad - 1
        report["reason"] = "single page reproduces the collapse"
        return report

    # The prefix collapsed without any single page doing so on its own.
    # Fall back to testing every page alone so the report names a culprit.
    for index, page in enumerate(pages):
        if probe([page]):
            report["trigger"] = page.route
            report["trigger_index"] = index
            report["reason"] = "single page reproduces the collapse"
            return report
    report["reason"] = "no single page reproduces the collapse on its own"
    return report


def scan_triggers(pages: list, entries: list[IndexEntry], title: str, work: Path) -> list[str]:
    """Every page that collapses a book on its own."""
    found = []
    for page in pages:
        result = measure([page], entries, title, work)
        if result["ok"] and result["doc_page"] == 0:
            found.append(page.route)
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="vendor id to bisect")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--scan",
        action="store_true",
        help="test every page alone instead of bisecting (finds all triggers)",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    catalog = load_catalog(root)
    if args.id not in catalog:
        print(f"unknown vendor {args.id}", file=sys.stderr)
        return 1
    vendor = catalog[args.id]
    corpus = corpus_dir(vendor, root)
    if not (corpus / "routes.json").is_file():
        print(f"no corpus for {args.id}", file=sys.stderr)
        return 1
    if not shutil.which("pandoc"):
        print("pandoc is required", file=sys.stderr)
        return 1

    entries = load_entries(corpus)
    pages = load_pages(corpus, entries)
    if not pages:
        print(f"no pages loaded for {args.id}", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="sites-epub-bisect-") as tmp:
        work = Path(tmp)
        if args.scan:
            triggers = scan_triggers(pages, entries, vendor.name, work)
            print(json.dumps({"vendor": args.id, "pages": len(pages), "triggers": triggers}, indent=2))
            # A trigger is a finding, so scanning finds one: exit 2 to say
            # "defect present", 0 to say "clean". Errors stay at 1.
            return 2 if triggers else 0

        report = bisect_trigger(pages, entries, vendor.name, work)
        report["vendor"] = args.id
        print(json.dumps(report, indent=2, ensure_ascii=False))
        if report.get("trigger"):
            print(f"trigger page = {report['trigger']}")
            # 2 = "a trigger page was found", 0 = "the book is clean".
            return 2
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
