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

from sites_epub.catalog import load_sites, upsert_vendor  # noqa: E402
from sites_epub.catalog_html import render_index, shelf_books  # noqa: E402
from sites_epub.compile import compile_from_sources, discover_entries, pack_vendor  # noqa: E402
from sites_epub.pack_cache import run_pack, vendor_pack_key  # noqa: E402
from sites_epub.epub_pack import grouped_html  # noqa: E402
from sites_epub.generic_blog import parse_blog_html  # noqa: E402
from sites_epub.generic_nav import parse_llms_generic  # noqa: E402
from sites_epub.images import repair_epub_images, rewrite_body_images  # noqa: E402
from sites_epub.mdx import looks_like_runtime_source, transform_mdx  # noqa: E402
from sites_epub.page import extract_from_html, extract_from_markdown  # noqa: E402
from sites_epub.models import IndexEntry, Vendor  # noqa: E402
from sites_epub.page import DocPage  # noqa: E402
from sites_epub.walk import blocking_defects, walk_chapters  # noqa: E402

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
                self.assertIn('href="https://example.test/blog/hello"', chapter)
                self.assertIn("source-title", chapter)
                self.assertNotIn("page-meta", chapter)
                self.assertNotIn("https://example.test/blog/hello", nav)
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


class TestPackFromCorpus(unittest.TestCase):
    def test_pack_vendor_reads_disk_corpus_offline(self) -> None:
        entries = _entries()
        src = _sources()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            vdir = root / "vendors" / "codex"
            corpus = vdir / "corpus" / "pages"
            corpus.mkdir(parents=True)
            for route, text in src.items():
                dest = corpus / f"{route}.md"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text, encoding="utf-8")
            import json

            (vdir / "corpus" / "routes.json").write_text(
                json.dumps(
                    [
                        {
                            "group": e.group,
                            "title": e.title,
                            "md_url": e.md_url,
                            "html_url": e.html_url,
                            "route": e.route,
                            "kind": e.kind,
                        }
                        for e in entries
                    ]
                ),
                encoding="utf-8",
            )
            vendor = Vendor(
                id="codex",
                name="Codex",
                docs_url="https://example.test/docs",
                blog_url="https://example.test/blog",
                icon="vendors/codex/icon.png",
                adapter="codex",
            )
            (vdir / "icon.png").write_bytes(SAMPLE.read_bytes())
            out = root / "dist" / "codex.epub"
            result = pack_vendor(vendor, out, root=root)
            self.assertTrue(out.is_file())
            self.assertEqual(result.chapters, 3)
            with zipfile.ZipFile(out) as zf:
                chapter = _chapter_text(zf)
                self.assertIn("Blog body phrase unique", chapter)
                self.assertIn("curl install", chapter)


class TestPackSkipUnchanged(unittest.TestCase):
    def _vendor_tree(self, root: Path) -> Vendor:
        entries = _entries()
        src = _sources()
        vdir = root / "vendors" / "codex"
        corpus = vdir / "corpus" / "pages"
        corpus.mkdir(parents=True)
        for route, text in src.items():
            dest = corpus / f"{route}.md"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
        import json

        (vdir / "corpus" / "routes.json").write_text(
            json.dumps(
                [
                    {
                        "group": e.group,
                        "title": e.title,
                        "md_url": e.md_url,
                        "html_url": e.html_url,
                        "route": e.route,
                        "kind": e.kind,
                    }
                    for e in entries
                ]
            ),
            encoding="utf-8",
        )
        (vdir / "icon.png").write_bytes(SAMPLE.read_bytes())
        return Vendor(
            id="codex",
            name="Codex",
            docs_url="https://example.test/docs",
            blog_url="https://example.test/blog",
            icon="vendors/codex/icon.png",
            adapter="codex",
        )

    def test_second_pack_skips_until_corpus_changes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            vendor = self._vendor_tree(root)
            dest = root / "dist"
            first = run_pack([vendor], dest, root=root, stamp=False)
            self.assertEqual(first[0]["action"], "packed")
            epub = dest / "codex.epub"
            self.assertTrue(epub.is_file())
            key = vendor_pack_key(vendor, root)
            self.assertEqual(first[0]["sha256"], key)
            mtime = epub.stat().st_mtime_ns
            second = run_pack([vendor], dest, root=root, stamp=False)
            self.assertEqual(second[0]["action"], "skipped")
            self.assertEqual(epub.stat().st_mtime_ns, mtime)
            page = root / "vendors" / "codex" / "corpus" / "pages" / "codex.md"
            page.write_text(page.read_text(encoding="utf-8") + "\nchanged body\n", encoding="utf-8")
            self.assertNotEqual(vendor_pack_key(vendor, root), key)
            third = run_pack([vendor], dest, root=root, stamp=False)
            self.assertEqual(third[0]["action"], "packed")
            self.assertGreater(epub.stat().st_mtime_ns, mtime)

    def test_reuses_epub_from_previous_site(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            vendor = self._vendor_tree(root)
            prev = root / "prev-site"
            first = run_pack([vendor], prev, root=root, stamp=False)
            self.assertEqual(first[0]["action"], "packed")
            dest = root / "dist"
            second = run_pack([vendor], dest, root=root, prev_site=prev, stamp=False)
            self.assertEqual(second[0]["action"], "skipped")
            self.assertTrue((dest / "codex.epub").is_file())


class TestGenericLlmsAndBlog(unittest.TestCase):
    def test_cursor_llms_nested_bare_urls(self) -> None:
        text = """# Cursor Documentation

## Get Started

- https://cursor.com/docs.md
- https://cursor.com/docs/get-started/quickstart.md
- https://cursor.comhttps://cursor.com/changelog.md

## Agent

- https://cursor.com/docs/agent/overview.md
  - https://cursor.com/docs/agent/tools/terminal.md

# Help Center

## Getting started

- https://cursor.com/help/getting-started/install.md

# API Documentation

## API Overview

- https://cursor.com/docs/api.md
- https://cursor.com/docs/api.md#authentication
"""
        entries = parse_llms_generic(text, "https://cursor.com/docs")
        routes = [e.route for e in entries]
        self.assertEqual(
            routes,
            [
                "docs",
                "docs/get-started/quickstart",
                "docs/agent/overview",
                "docs/agent/tools/terminal",
                "docs/api",
            ],
        )
        self.assertTrue(entries[0].group.startswith("Cursor"))
        self.assertTrue(any(e.group.endswith("Agent") for e in entries))
        self.assertTrue(all(e.kind == "doc" for e in entries))

    def test_blog_html_reads_sitemap_locs(self) -> None:
        html = (
            '<a href="/blog/hello">Hello</a>'
            "<urlset><url><loc>https://cursor.com/blog/second-post</loc></url>"
            "<url><loc>https://cursor.com/blog/topic/product</loc></url></urlset>"
        )
        entries = parse_blog_html(html, "https://cursor.com/blog")
        routes = [e.route for e in entries]
        self.assertEqual(routes, ["blog/hello", "blog/second-post"])
        self.assertTrue(all(e.kind == "blog" for e in entries))


class TestRewriteImages(unittest.TestCase):
    def test_unmapped_remote_images_are_dropped(self) -> None:
        html = (
            '<p>x</p><img src="https://cdn.example/kept.png" alt="k">'
            '<img src="https://cdn.example/skip.png" alt="s">'
            '<img src="/images/blog/side-chat.jpg" alt="broken">'
        )
        out = rewrite_body_images(
            html,
            {"https://cdn.example/kept.png": "images/kept.png"},
            base="https://learn.chatgpt.com/blog/post",
            available={"images/kept.png"},
        )
        self.assertIn("images/kept.png", out)
        self.assertNotIn("https://cdn.example/skip.png", out)
        self.assertNotIn("/images/blog/side-chat.jpg", out)
        self.assertNotIn("http://", out)

    def test_site_relative_img_is_embedded_and_unmapped_omitted(self) -> None:
        entries = [
            IndexEntry(
                group="Overview",
                title="Home",
                md_url="https://learn.chatgpt.com/docs.md",
                html_url="https://learn.chatgpt.com/docs",
                route="docs",
                kind="doc",
            )
        ]
        src = {
            "docs": (
                "# Home\n\nA paragraph before the screenshot.\n\n"
                '<img src="/images/blog/side-chat.jpg" alt="side chat">\n\n'
                '<img src="/images/blog/missing.jpg" alt="missing">\n\n'
                "A paragraph after the screenshot.\n"
            )
        }
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "book.epub"
            mapped = {
                "https://learn.chatgpt.com/images/blog/side-chat.jpg": SAMPLE,
            }
            compile_from_sources(
                entries,
                src,
                out,
                image_files=mapped,
                title="Codex",
                author="OpenAI",
                cover_image=SAMPLE,
            )
            with zipfile.ZipFile(out) as zf:
                names = set(zf.namelist())
                chapter = _chapter_text(zf)
                self.assertNotIn("/images/blog/missing.jpg", chapter)
                self.assertNotIn("broken_img", chapter)
                report = walk_chapters(out)
                broken = [
                    d
                    for c in report.chapters
                    for d in blocking_defects(c.defects)
                ]
                self.assertEqual(broken, [])
                media = [n for n in names if n.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))]
                self.assertTrue(media)

    def test_repair_strips_img_missing_from_zip(self) -> None:
        import io
        import zipfile as zfmod

        buf = io.BytesIO()
        html = (
            '<?xml version="1.0"?><html xmlns="http://www.w3.org/1999/xhtml">'
            '<body><div class="doc-page" id="p"><p>Hello there screenshot.</p>'
            '<img src="../media/nope.jpg" alt="x"/></div></body></html>'
        )
        with zfmod.ZipFile(buf, "w") as zf:
            zf.writestr("mimetype", "application/epub+zip", compress_type=zfmod.ZIP_STORED)
            zf.writestr("EPUB/text/ch001.xhtml", html)
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "book.epub"
            path.write_bytes(buf.getvalue())
            removed = repair_epub_images(path)
            self.assertGreaterEqual(removed, 1)
            with zfmod.ZipFile(path) as zf:
                text = zf.read("EPUB/text/ch001.xhtml").decode("utf-8")
            self.assertNotIn("<img", text.lower())


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
                updated_at="2026-08-27T04:00:00Z",
            )
            upsert_vendor(v, cat)
            again = upsert_vendor(
                Vendor(
                    id="cursor",
                    name="Cursor",
                    docs_url="https://cursor.com/docs",
                    blog_url="https://cursor.com/blog",
                    icon="vendors/cursor/icon.png",
                    adapter="generic",
                ),
                cat,
            )
            ids = [x.id for x in again]
            self.assertEqual(ids.count("cursor"), 1)
            self.assertEqual(again[0].updated_at, "2026-08-27T04:00:00Z")


class TestShelf(unittest.TestCase):
    def test_shelf_lists_vendors_and_linked_sites(self) -> None:
        html = render_index()
        self.assertIn("ZenShelf", html)
        self.assertIn("可以离线翻的书", html)
        self.assertIn("落地站", html)
        self.assertIn("增量抓取", html)
        self.assertIn("Codex", html)
        self.assertIn("Claude", html)
        self.assertIn("Cursor", html)
        self.assertIn("Pi Agent", html)
        self.assertIn("https://blog.zenheart.site/pi/", html)
        self.assertIn("https://blog.zenheart.site/claude-code-sourcemap/", html)
        self.assertIn("https://dh.zenheart.site/", html)
        self.assertIn("DeepSeek", html)
        self.assertIn("语料", html)
        books = shelf_books()
        kinds = {b["id"]: b["kind"] for b in books}
        self.assertEqual(kinds["codex"], "vendor")
        self.assertEqual(kinds["pi-handbook"], "site")
        self.assertEqual(kinds["deepseek-harness"], "site")
        pi = next(b for b in books if b["id"] == "pi-handbook")
        self.assertTrue(pi["cover"].endswith(".png"))
        codex = next(b for b in books if b["id"] == "codex")
        self.assertEqual(codex["coverKind"], "image")
        self.assertEqual(codex["cover"], "covers/codex.png")
        self.assertIn("display: flex", html)
        self.assertIn("flex-wrap: wrap", html)
        self.assertNotIn("grid-template-columns", html)
        self.assertIn("book-cover-slot", html)
        self.assertIn("padding-bottom: 133.333%", html)
        sites = load_sites()
        self.assertTrue(any(s.id == "claude-code-sourcemap" for s in sites))


class TestRuntimeSourceAndImages(unittest.TestCase):
    _MDX = """# Explore the .claude directory

> Where Claude Code reads CLAUDE.md.

export const ClaudeExplorer = () => {
  const A = useMemo(() => ({href, children}) => <a href={href}>{children}</a>, []);
  const FILE_TREE = useMemo(() => ({
    project: {
      label: 'your-project/',
      children: [{
        id: 'claude-md',
        label: 'CLAUDE.md',
        type: 'file',
        oneLiner: 'Project instructions Claude reads every session',
        when: 'Loaded into context at the start of every session',
        description: 'Project-specific instructions that shape how Claude works.',
        example: `# Project conventions
- Build: npm run build`,
        docsLink: '/en/memory'
      }]
    }
  }), []);
  return <div>{FILE_TREE}</div>;
};

## What’s not shown

The explorer covers files you author and edit.
"""

    def test_transform_strips_react_islands(self) -> None:
        self.assertTrue(looks_like_runtime_source(self._MDX))
        out = transform_mdx(self._MDX)
        self.assertNotIn("useMemo", out)
        self.assertNotIn("export const", out)
        self.assertIn("What’s not shown", out)
        self.assertIn("explore-the-directory", out)
        self.assertIn("CLAUDE.md", out)

    def test_extract_markdown_does_not_leak_react(self) -> None:
        page = extract_from_markdown(
            self._MDX,
            route="claude-directory",
            url="https://code.claude.com/docs/en/claude-directory",
        )
        self.assertNotIn("useMemo", page.body_html)
        self.assertNotIn("FILE_TREE", page.body_text)
        self.assertIn("not shown", page.body_text.lower())
        self.assertIn("https://code.claude.com/docs/en/claude-directory#explore-the-directory", page.body_html)
        self.assertIn("CLAUDE.md", page.body_text)

    def test_html_article_keeps_readable_copy(self) -> None:
        html = (
            "<!DOCTYPE html><html><body><article>"
            "<h1>Explore the .claude directory</h1>"
            "<p>Claude Code reads instructions from your project directory.</p>"
            "<h2>What’s not shown</h2>"
            "<p>The explorer covers files you author and edit.</p>"
            '<img src="https://mintcdn.com/claude-code/x/images/vs-code.png" alt="VS Code">'
            "</article></body></html>"
        )
        page = extract_from_html(
            html,
            route="claude-directory",
            url="https://code.claude.com/docs/en/claude-directory",
        )
        self.assertIn("project directory", page.body_text)
        self.assertNotIn("useMemo", page.body_html)
        self.assertTrue(any("vs-code.png" in u for u in page.image_urls))

    def test_rewrite_maps_query_string_variants(self) -> None:
        html = '<p><img src="https://mintcdn.com/x/a.png?fit=max&amp;auto=format" alt="a"></p>'
        out = rewrite_body_images(
            html,
            {"https://mintcdn.com/x/a.png?q=85": "images/a.png"},
            base="https://code.claude.com/docs",
            available={"images/a.png"},
        )
        self.assertIn("images/a.png", out)
        self.assertNotIn("mintcdn.com", out)


class TestSceneRestore(unittest.TestCase):
    def test_frame_becomes_figure_with_image(self) -> None:
        md = (
            "# Status line\n\n"
            "<Frame>\n"
            '<img src="https://mintcdn.com/claude-code/x/images/statusline.png" alt="status line">\n'
            "</Frame>\n"
        )
        page = extract_from_markdown(
            md, route="statusline", url="https://code.claude.com/docs/en/statusline"
        )
        self.assertIn("mdx-frame", page.body_html)
        self.assertIn("statusline.png", page.body_html)
        self.assertTrue(any("statusline.png" in u for u in page.image_urls))

    def test_card_links_to_original_docs(self) -> None:
        md = (
            "# Quickstart\n\n"
            '<Card title="Best practices" href="/docs/en/best-practices">\n'
            "Get better results.\n"
            "</Card>\n"
        )
        page = extract_from_markdown(
            md, route="quickstart", url="https://code.claude.com/docs/en/quickstart"
        )
        self.assertIn("https://code.claude.com/docs/en/best-practices", page.body_html)
        self.assertIn("mdx-card", page.body_html)
        self.assertIn("Get better results", page.body_text)

    def test_mermaid_stays_as_diagram_source(self) -> None:
        md = "# Flow\n\n```mermaid\ngraph TD\n  A-->B\n```\n"
        page = extract_from_markdown(
            md, route="flow", url="https://code.claude.com/docs/en/flow"
        )
        self.assertIn("mdx-mermaid", page.body_html)
        self.assertIn("language-mermaid", page.body_html)
        self.assertIn("A--", page.body_html)
        self.assertNotIn("useMemo", page.body_html)

    def test_root_relative_links_become_absolute(self) -> None:
        md = "# X\n\nSee [hooks](/docs/en/hooks) for details.\n"
        page = extract_from_markdown(
            md, route="x", url="https://code.claude.com/docs/en/x"
        )
        self.assertIn("https://code.claude.com/docs/en/hooks", page.body_html)


class TestSourceTitleLinks(unittest.TestCase):
    def test_grouped_html_title_is_the_original_url(self) -> None:
        pages = [
            DocPage(
                title="Zero Trust for AI agents",
                body_html="<p>Enough article body for a real chapter.</p>",
                body_text="Enough article body for a real chapter.",
                route="blog/zero-trust-for-ai-agents",
                group="Blog",
                url="https://claude.com/blog/zero-trust-for-ai-agents",
            )
        ]
        html = grouped_html(pages)
        self.assertIn(
            'href="https://claude.com/blog/zero-trust-for-ai-agents"',
            html,
        )
        self.assertIn("class=\"source-title\"", html)
        self.assertIn("Zero Trust for AI agents", html)
        self.assertIn('data-source="https://claude.com/blog/zero-trust-for-ai-agents"', html)
        self.assertNotIn("page-meta", html)
        self.assertNotRegex(
            html,
            r"<p[^>]*>https://claude.com/blog/zero-trust-for-ai-agents</p>",
        )

    def test_walk_flags_unlinked_page_title(self) -> None:
        import zipfile as zfmod

        html = (
            '<?xml version="1.0"?><html xmlns="http://www.w3.org/1999/xhtml">'
            '<body><div class="doc-page" id="p" '
            'data-source="https://claude.com/blog/zero-trust-for-ai-agents">'
            "<h2>Zero Trust for AI agents</h2>"
            "<p>https://claude.com/blog/zero-trust-for-ai-agents</p>"
            "<p>Enough body text so the stub check does not fire here.</p>"
            "</div></body></html>"
        )
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "book.epub"
            with zfmod.ZipFile(path, "w") as zf:
                zf.writestr("mimetype", "application/epub+zip", compress_type=zfmod.ZIP_STORED)
                zf.writestr("EPUB/text/ch001.xhtml", html)
            report = walk_chapters(path)
            flags = [
                d
                for c in report.chapters
                for d in c.defects
                if d.startswith("unlinked_page_title")
            ]
            self.assertTrue(flags)
            self.assertFalse(report.ok)


if __name__ == "__main__":
    unittest.main()
