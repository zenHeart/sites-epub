"""Regression tests for Muse Code navigation scope and URL normalization."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sites_epub.muse_nav import parse_muse_docs  # noqa: E402


FIXTURE = """
<html><body>
  <nav>
    <a href="/docs/muse-code">Overview</a>
    <a href="/docs/muse-code/auth">Authentication and billing</a>
    <a href="/docs/muse-code/permissions">Permissions and safety</a>
    <a href="/docs/muse-code/permissions/approval-modes">Approval modes</a>
    <a href="/docs/muse-code/changelog#latest">Changelog</a>
    <a href="/docs/overview">Model API overview</a>
    <a href="/docs/muse-code/../models">Models</a>
    <a href="https://other.example/docs/muse-code/escape">External</a>
  </nav>
</body></html>
"""


class MuseNavTest(unittest.TestCase):
    def test_enumerates_product_pages_and_nested_children(self):
        entries = parse_muse_docs(FIXTURE, "https://www.musemuse.dev/docs/muse-code")
        self.assertEqual(
            [entry.route for entry in entries],
            ["index", "auth", "permissions", "permissions/approval-modes", "changelog"],
        )
        self.assertEqual(entries[1].title, "Authentication and billing")

    def test_every_entry_is_hard_scoped_to_muse_code(self):
        entries = parse_muse_docs(FIXTURE, "https://www.musemuse.dev/docs/muse-code")
        for entry in entries:
            self.assertTrue(
                entry.html_url.startswith("https://www.musemuse.dev/docs/muse-code")
            )
            self.assertNotIn("models", entry.route)
            self.assertNotIn("other.example", entry.html_url)

    def test_same_route_is_deduplicated(self):
        html = FIXTURE.replace(
            '<a href="/docs/muse-code/auth">Authentication and billing</a>',
            '<a href="/docs/muse-code/auth">Authentication and billing</a>'
            '<a href="/docs/muse-code/auth#copy">Auth copy</a>',
        )
        entries = parse_muse_docs(html, "https://www.musemuse.dev/docs/muse-code")
        self.assertEqual([e.route for e in entries].count("auth"), 1)


if __name__ == "__main__":
    unittest.main()
