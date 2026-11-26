#!/usr/bin/env python3
"""Regression tests for the gemini help-centre enumeration.

Regression (2026-11-27): support.google.com renders a global promo banner on
every help-centre page ("Learn how to manage your Gemini App").  The banner
links to a real article, but its anchor text is a generic call-to-action.  The
landing page's anchors are scanned before the topic pages and the enumeration
used `setdefault`, so the banner text won and the chapter shipped titled
"Learn how" instead of "Use Gemini Apps" — while `fetch` still reported ok.

The fix puts promo anchors in a lower-priority tier: they may still contribute
a route the nav never links, but they never override a real article title.

The fixture below reproduces the live shape verbatim (see the A/B against the
real site on 2026-11-27: 105 + 27 routes, exactly one title changed).
"""

from __future__ import annotations

import sys
import unittest
import unittest.mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub import gemini_nav  # noqa: E402
from sites_epub.gemini_nav import help_center_entries  # noqa: E402

LANDING = "https://support.google.com/gemini/"

# The real page shape: a promo banner link and the article link both point at
# /gemini/answer/13275745, and the banner comes FIRST in document order.
FIXTURE = """
<html><body>
  <header><div class="info-bar-container">
    <div class="notification" data-name="always_on_global" tabindex="0">
      <p><a href="https://support.google.com/gemini/answer/13275745" rel="noopener">Learn how</a> to manage your Gemini App</p>
    </div>
  </div></header>
  <div class="child" role="listitem"><a class="article-link" href="/gemini/answer/13275745?hl=en&amp;ref_topic=15280100">Use Gemini Apps</a></div>
  <div class="child" role="listitem"><a class="article-link" href="/gemini/answer/13595584?hl=en&amp;ref_topic=13194540">Set up your account</a></div>
  <div class="child" role="listitem"><a class="article-link" href="/gemini/answer/99999999?hl=en">Promo only article</a></div>
</body></html>
"""


def _fake_fetch(url: str) -> str:
    if url == LANDING:
        return FIXTURE
    raise AssertionError(f"unexpected fetch: {url}")


class HelpCenterTitlePriorityTest(unittest.TestCase):
    def _entries(self):
        """Drive the enumeration with the landing fixture.

        The module-level fetch_text is patched rather than an argument passed,
        so this exact call shape also works against the pre-fix implementation.
        That matters: the test then fails on the real assertion (title text)
        rather than on a signature mismatch.
        """
        with unittest.mock.patch.object(gemini_nav, "fetch_text", _fake_fetch):
            return help_center_entries(
                LANDING, "gemini", "Gemini App Help", "gemini-app/"
            )

    def test_promo_banner_text_does_not_win_over_article_title(self):
        """The banner's "Learn how" must not become the chapter title."""
        titles = {e.route: e.title for e in self._entries()}
        self.assertEqual(titles["gemini-app/13275745"], "Use Gemini Apps")

    def test_old_first_wins_logic_would_have_failed(self):
        """Prove the fixture actually exercises the old bug.

        The pre-fix implementation kept the first anchor text it saw for a
        path.  Reproduce that rule here so the test cannot pass by accident
        if the fixture ever stops matching the live page shape.
        """
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin
        import re

        soup = BeautifulSoup(FIXTURE, "lxml")
        first_seen: dict[str, str] = {}
        for a in soup.find_all("a", href=True):
            absu = urljoin(LANDING, a["href"]).split("#")[0].split("?")[0]
            m = re.search(r"/gemini/(topic|answer)/[A-Za-z0-9]+", absu)
            if not m or m.group(1) != "answer":
                continue
            first_seen.setdefault(m.group(0), " ".join(a.get_text(" ", strip=True).split()))
        self.assertEqual(
            first_seen["/gemini/answer/13275745"],
            "Learn how",
            "fixture no longer reproduces the old first-wins bug",
        )

    def test_promo_only_route_is_still_collected(self):
        """Downgrading promo text must not drop the route it points at."""
        routes = {e.route for e in self._entries()}
        self.assertIn("gemini-app/99999999", routes)

    def test_regular_article_titles_unchanged(self):
        titles = {e.route: e.title for e in self._entries()}
        self.assertEqual(titles["gemini-app/13595584"], "Set up your account")

    def test_entries_link_to_the_original_url(self):
        by_route = {e.route: e for e in self._entries()}
        for route, entry in by_route.items():
            self.assertTrue(
                entry.html_url.startswith("https://support.google.com/gemini/answer/"),
                f"{route} does not link to the original",
            )


if __name__ == "__main__":
    unittest.main()
