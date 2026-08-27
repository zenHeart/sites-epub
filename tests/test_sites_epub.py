#!/usr/bin/env python3
"""Drive shipped discover/compile/incremental/pack entry points from fixtures."""

from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub.catalog import upsert_vendor  # noqa: E402
from sites_epub.compile import compile_from_sources, discover_entries  # noqa: E402
from sites_epub.models import IndexEntry, Vendor  # noqa: E402
from sites_epub.walk import walk_chapters  # noqa: E402

FIXTURES = ROOT / "fixtures"
NAV = FIXTURES / "nav.html"
SAMPLE = FIXTURES / "sample.png"


def _entries() -> list[IndexEntry]:
    return [
        IndexEntry(
            group="Overview",
            title="Home",
            md_url="https://example.test/codex.md",
            html_url="https://example.test/codex",
            route="codex",
            kind="doc",
        ),
        IndexEntry(
            group="Overview",
            title="Quickstart",
            md_url="https://example.test/codex/quickstart.md",
            html_url="https://example.test/codex/quickstart",
            route="codex/quickstart",
            kind="doc",
        ),
        IndexEntry(
            group="Blog",
            title="Hello post",
            md_url="https://example.test/blog/hello.md",
            html_url="https://example.test/blog/hello",
            route="blog/hello",
            kind="blog",
        ),
    ]


def _sources(quick: str = "Desktop tab body with curl install.") -> dict[str, str]:
    return {
        "codex": "# Home\n\nStart with a goal, idea, or task for the home page.\n",
        "codex/quickstart": f"# Quickstart\n\n{quick}\n\n```bash\necho hello-from-fence\n```\n",
        "blog/hello": (
            "<!DOCTYPE html><html><body><article>"
            "<h1>Hello post</h1>"
            "<p>Blog body phrase unique for the fixture post.</p>"
            "</article></body></html>"
        ),
    }


def _nav_text(zf: zipfile.ZipFile) -> str:
    chunks = []
    for name in zf.namelist():
        if "nav" in name.lower() or name.lower().endswith("toc.xhtml"):
            chunks.append(zf.read(name).decode("utf-8", errors="replace"))
    return "\n".join(chunks)


def _chapter_text(zf: zipfile.ZipFile) -> str:
    chunks = []
    for name in zf.namelist():
        if name.lower().endswith(".xhtml"):
            chunks.append(zf.read(name).decode("utf-8", errors="replace"))
    return "\n".join(chunks)


class TestDiscover(unittest.TestCase):
    def test_codex_nav_fixture_rejects_sibling_trees(self) -> None:
        html = NAV.read_text(encoding="utf-8")
        vendor = Vendor(
            id="codex",
            name="Codex",
            docs_url="https://learn.chatgpt.com/docs",
            blog_url=None,
            icon="vendors/codex/icon.png",
            adapter="codex",
        )
        entries = discover_entries(vendor, docs_html=html)
        self.assertTrue(entries)
        groups = {e.group for e in entries}
        for name in (
            "Overview",
            "Features",
            "Configuration",
            "Developers",
            "Security",
            "Administration",
        ):
            self.assertIn(name, groups)
        self.assertNotIn("Use Cases", groups)
        for e in entries:
            self.assertFalse(e.html_url.startswith("https://learn.chatgpt.com/api/"))
            self.assertEqual(e.kind, "doc")


class TestCompileIncremental(unittest.TestCase):
    def test_docs_then_blog_and_incremental_skip(self) -> None:
        entries = _entries()
        src = _sources()
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "book.epub"
            first = compile_from_sources(
                entries, src, out, title="Codex", author="OpenAI", cover_image=SAMPLE
            )
            self.assertEqual(set(first.fetched_routes), {e.route for e in entries})
            self.assertEqual(first.skipped_routes, [])
            self.assertTrue(out.is_file())
            with zipfile.ZipFile(out) as zf:
                self.assertEqual(zf.read("mimetype").decode().strip(), "application/epub+zip")
                nav = _nav_text(zf)
                chapter = _chapter_text(zf)
                self.assertLess(nav.find("Overview"), nav.find("Blog"))
                self.assertLess(nav.find("Quickstart"), nav.find("Hello post"))
                self.assertIn("Start with a goal", chapter)
                self.assertIn("curl install", chapter)
                self.assertIn("Blog body phrase unique", chapter)
                self.assertNotIn("<Tabs", chapter)
                report = walk_chapters(out)
                self.assertTrue(report.ok, [c.defects for c in report.chapters if not c.ok])

            changed = _sources(quick="CHANGED quickstart body phrase after incremental.")
            second = compile_from_sources(
                entries,
                changed,
                out,
                fingerprints=first.fingerprints,
                title="Codex",
                author="OpenAI",
                cover_image=SAMPLE,
            )
            self.assertEqual(second.fetched_routes, ["codex/quickstart"])
            self.assertIn("codex", second.skipped_routes)
            self.assertIn("blog/hello", second.skipped_routes)
            with zipfile.ZipFile(out) as zf:
                chapter = _chapter_text(zf)
                self.assertIn("CHANGED quickstart body phrase after incremental", chapter)
                self.assertIn("Blog body phrase unique", chapter)


class TestCatalogUpsert(unittest.TestCase):
    def test_upsert_vendor_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            cat = Path(td) / "catalog.json"
            v = Vendor(
                id="cursor",
                name="Cursor",
                docs_url="https://cursor.com/docs",
                blog_url="https://cursor.com/blog",
                icon="vendors/cursor/icon.png",
                adapter="generic",
            )
            upsert_vendor(v, cat)
            again = upsert_vendor(v, cat)
            ids = [x.id for x in again]
            self.assertEqual(ids.count("cursor"), 1)


if __name__ == "__main__":
    unittest.main()
