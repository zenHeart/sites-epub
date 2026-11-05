"""Regression test for the bisect diagnostic (issue #5).

The first bisect script re-split its last candidate page into itself, so it
re-tested one page forever instead of naming it. The tool now bisects over
page prefixes and treats a one-element candidate as the answer.

The search is exercised through an injected probe, so the properties that
matter are pinned without a pandoc run per candidate:

* a single trigger page is *named*;
* a healthy book reports no trigger;
* the search terminates, including when the trigger is the very last page
  (the exact shape that used to loop forever).

One end-to-end test then packs a real single page and confirms the reader
keeps its headings, which is the property the collapse broke.
"""

from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load_bisect():
    path = ROOT / ".agents" / "skills" / "site2epub" / "scripts" / "bisect_pages.py"
    spec = importlib.util.spec_from_file_location("bisect_pages", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestBisectSearch(unittest.TestCase):
    """The search must terminate and name the page that collapses the book."""

    def setUp(self) -> None:
        self.mod = _load_bisect()

    def _pages(self, count: int):
        from sites_epub.models import IndexEntry
        from sites_epub.page import DocPage

        entries = [
            IndexEntry(
                group="Group",
                title=f"Page {i}",
                md_url="",
                html_url=f"https://example.test/p{i}",
                route=f"p{i}",
                kind="doc",
            )
            for i in range(count)
        ]
        pages = [
            DocPage(
                title=entry.title,
                body_html="<p>Body copy.</p>",
                body_text="Body copy.",
                route=entry.route,
                group=entry.group,
                url=entry.html_url,
            )
            for entry in entries
        ]
        return entries, pages

    def _probe(self, trigger_index: int, calls: list[int] | None = None):
        """A probe that reports a collapse once the trigger page is included."""

        def probe(candidate: list) -> bool:
            if calls is not None:
                calls.append(len(candidate))
            return any(p.route == f"p{trigger_index}" for p in candidate)

        return probe

    def test_single_trigger_page_is_named(self) -> None:
        entries, pages = self._pages(9)
        with tempfile.TemporaryDirectory() as td:
            report = self.mod.bisect_trigger(
                pages, entries, "T", Path(td), probe=self._probe(4)
            )
        self.assertEqual(report["trigger"], "p4")
        self.assertEqual(report["trigger_index"], 4)
        self.assertEqual(report["reason"], "single page reproduces the collapse")

    def test_last_page_trigger_is_still_named(self) -> None:
        """The one-element candidate is the answer, never re-split.

        This is the exact shape that used to loop forever: the trigger is the
        final page, so the candidate set shrinks to a single page.
        """
        entries, pages = self._pages(5)
        with tempfile.TemporaryDirectory() as td:
            report = self.mod.bisect_trigger(
                pages, entries, "T", Path(td), probe=self._probe(4)
            )
        self.assertEqual(report["trigger"], "p4")
        self.assertEqual(report["trigger_index"], 4)

    def test_search_terminates_in_log_n_probes(self) -> None:
        """The prefix bisect must not test the same candidate twice in a row."""
        entries, pages = self._pages(64)
        calls: list[int] = []
        with tempfile.TemporaryDirectory() as td:
            report = self.mod.bisect_trigger(
                pages, entries, "T", Path(td), probe=self._probe(63, calls)
            )
        self.assertEqual(report["trigger"], "p63")
        self.assertLess(len(calls), 20, f"probe called {len(calls)} times")
        # No candidate size is probed twice in a row: that is the shape of the
        # old infinite loop.
        self.assertFalse(any(a == b for a, b in zip(calls, calls[1:])))

    def test_healthy_book_reports_no_trigger(self) -> None:
        entries, pages = self._pages(6)
        with tempfile.TemporaryDirectory() as td:
            report = self.mod.bisect_trigger(
                pages, entries, "T", Path(td), probe=lambda candidate: False
            )
        self.assertIsNone(report["trigger"])
        self.assertIn("keeps its structure", report["reason"])


class TestSinglePageKeepsItsHeadings(unittest.TestCase):
    """The end-to-end property the collapse broke (issue #5 AC#2)."""

    @unittest.skipUnless(shutil.which("pandoc"), "pandoc not installed")
    def test_pandoc_keeps_page_headings_for_a_role_main_page(self) -> None:
        from sites_epub.page import sanitize_body_html

        body = sanitize_body_html('<div role="main"><p>Body copy.</p></div>')
        html = (
            '<html><head><title>t</title></head><body>'
            '<div class="doc-group"><h1>Group</h1>'
            '<div class="doc-page"><h2 class="page-title">Page Title</h2>'
            f"{body}</div></div></body></html>"
        )
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            src = work / "b.html"
            src.write_text(html, encoding="utf-8")
            out = work / "b.epub"
            proc = subprocess.run(
                [
                    "pandoc", str(src), "-f", "html", "-t", "epub3", "-o", str(out),
                    "--toc", "--split-level=1", f"--resource-path={work}",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            with zipfile.ZipFile(out) as zf:
                blob = "".join(
                    zf.read(n).decode("utf-8", "replace")
                    for n in zf.namelist()
                    if n.startswith("EPUB/text/")
                )
        self.assertGreater(blob.count("<h2"), 0)
        self.assertGreater(blob.count("doc-page"), 0)
        self.assertIn("Page Title", blob)


class TestBisectCliExitCodes(unittest.TestCase):
    """The CLI must be usable as a gate: 0 clean, 2 trigger found, 1 error."""

    def test_cli_rejects_unknown_vendor(self) -> None:
        script = ROOT / ".agents" / "skills" / "site2epub" / "scripts" / "bisect_pages.py"
        proc = subprocess.run(
            [sys.executable, str(script), "--id", "no-such-vendor"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("unknown vendor", proc.stderr)


if __name__ == "__main__":
    unittest.main()
