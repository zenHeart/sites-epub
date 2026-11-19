"""Regression tests for ``fetch_source`` (issue #2, root cause 1).

Some sites publish a markdown twin of every documentation page.  The twin is
usually faithful, but it can be an *abridgement*: cursor shipped 2334 of the
4850 characters of ``help/account-and-billing/bugbot-usage-based-billing`` and
6361 of 12908 for ``help/grok-bot/agent-email``.  The old switch condition only
asked whether the HTML page *had images* -- it never compared how much *text*
each source carried, so an abridged twin was shipped as-is.

These tests pin the rule that is now in force: the source with the fuller body
wins, and the markdown twin is kept only while it carries at least
``MD_TWIN_MIN_RATIO`` of the HTML article's text.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub import compile as compile_mod  # noqa: E402
from sites_epub.models import IndexEntry  # noqa: E402
from sites_epub.page import extract_page  # noqa: E402

FILLER = (
    "Billing for usage based plans is calculated from the metered tokens of "
    "every request that the workspace makes during the billing period. "
)


def _markdown(chars: int) -> str:
    """A markdown article whose extracted body text is roughly ``chars`` long."""
    body = (FILLER * ((chars // len(FILLER)) + 1)).strip()
    return f"# Article\n\n{body}\n"


def _html(chars: int, *, with_image: bool = False) -> str:
    """An HTML article whose extracted body text is roughly ``chars`` long."""
    body = (FILLER * ((chars // len(FILLER)) + 1)).strip()
    image = '<img src="https://x.test/diagram.png" alt="diagram">' if with_image else ""
    return (
        "<!DOCTYPE html><html><head><title>Article</title></head><body>"
        f"<nav>Home Docs Blog</nav><article><h1>Article</h1>{image}"
        f"<p>{body}</p></article><footer>copyright</footer></body></html>"
    )


def _body_len(source: str, url: str) -> int:
    kind = "html" if source.lstrip().lower().startswith("<!") else "md"
    return len(extract_page(source, url=url, kind=kind).body_text.strip())


def _entry(md_url: str = "https://x.test/page.md", html_url: str = "https://x.test/page"):
    return IndexEntry(
        group="Test",
        title="Article",
        md_url=md_url,
        html_url=html_url,
        route="page",
    )


class FetchSourceTest(unittest.TestCase):
    def _serve(self, md: str, html: str):
        def fake_fetch(url: str) -> str:
            return md if url.endswith(".md") else html

        return mock.patch.object(compile_mod, "fetch_text", side_effect=fake_fetch)

    def test_abridged_twin_loses_to_the_live_article(self):
        md = _markdown(2334)
        html = _html(4850)
        with self._serve(md, html):
            chosen = compile_mod.fetch_source(_entry(), suspect_below=6000)
        self.assertEqual(chosen, html, "the abridged twin must not be shipped")
        self.assertGreaterEqual(
            _body_len(chosen, "https://x.test/page"),
            0.9 * _body_len(html, "https://x.test/page"),
        )

    def test_second_cursor_shape_also_loses(self):
        # 6361 of 12908 characters -- the second page that shipped abridged.
        md = _markdown(6361)
        html = _html(12908)
        with self._serve(md, html):
            chosen = compile_mod.fetch_source(_entry(), suspect_below=8000)
        self.assertEqual(chosen, html)
        self.assertGreaterEqual(
            _body_len(chosen, "https://x.test/page"),
            0.9 * _body_len(html, "https://x.test/page"),
        )

    def test_a_long_twin_is_not_pulled_against_the_live_article(self):
        # The comparison costs an extra request, so it only runs on pages that
        # are already suspect (below half of the vendor's median).
        md = _markdown(6361)
        html = _html(12908)
        with self._serve(md, html):
            chosen = compile_mod.fetch_source(_entry(), suspect_below=3000)
        self.assertEqual(chosen, md)

    def test_faithful_twin_is_kept(self):
        md = _markdown(4000)
        html = _html(4100)
        with self._serve(md, html):
            chosen = compile_mod.fetch_source(_entry(), suspect_below=6000)
        self.assertEqual(chosen, md, "a twin that is not abridged must stay the source")

    def test_html_with_illustrations_wins_over_a_twin_without_any(self):
        md = _markdown(4000)
        html = _html(4000, with_image=True)
        with self._serve(md, html):
            chosen = compile_mod.fetch_source(_entry(), suspect_below=6000)
        self.assertEqual(chosen, html)

    def test_same_url_is_fetched_once(self):
        html = _html(4000)
        calls: list[str] = []

        def fake_fetch(url: str) -> str:
            calls.append(url)
            return html

        entry = _entry(md_url="https://x.test/page", html_url="https://x.test/page")
        with mock.patch.object(compile_mod, "fetch_text", side_effect=fake_fetch):
            chosen = compile_mod.fetch_source(entry)
        self.assertEqual(chosen, html)
        self.assertEqual(len(calls), 1, "one address must not be fetched twice")

    def test_missing_twin_falls_back_to_html(self):
        html = _html(4000)

        def fake_fetch(url: str) -> str:
            if url.endswith(".md"):
                raise RuntimeError("404")
            return html

        with mock.patch.object(compile_mod, "fetch_text", side_effect=fake_fetch):
            chosen = compile_mod.fetch_source(_entry())
        self.assertEqual(chosen, html)


if __name__ == "__main__":
    unittest.main()
