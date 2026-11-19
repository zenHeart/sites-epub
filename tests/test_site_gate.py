"""Regression test for the site asset gate.

The gate exists because a missing cover shipped as a broken image on the live
site for months: `covers/deepseek.png` was deleted while the shelf entry
still pointed at it, and the site build skipped the missing file silently.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _load_check_site():
    path = ROOT / ".agents" / "skills" / "site2epub" / "scripts" / "check_site.py"
    spec = importlib.util.spec_from_file_location("check_site", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _index(books: list[dict]) -> str:
    return (
        "<html><body><script>const BOOKS = "
        + json.dumps(books)
        + ";</script></body></html>"
    )


class TestSiteGate(unittest.TestCase):
    def setUp(self) -> None:
        self.mod = _load_check_site()

    def _site(self, root: Path, books: list[dict], files: list[str]) -> Path:
        site = root / "site"
        site.mkdir(parents=True, exist_ok=True)
        (site / "index.html").write_text(_index(books), encoding="utf-8")
        (site / "CNAME").write_text("epub.zenheart.site\n", encoding="utf-8")
        for rel in files:
            target = site / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"x")
        return site

    def _run(self, site: Path) -> int:
        script = ROOT / ".agents" / "skills" / "site2epub" / "scripts" / "check_site.py"
        proc = subprocess.run(
            [sys.executable, str(script), str(site)],
            capture_output=True,
            text=True,
        )
        return proc.returncode

    def test_complete_site_passes(self) -> None:
        books = [
            {
                "id": "codex",
                "kind": "vendor",
                "href": "codex.epub",
                "cover": "covers/codex.png",
                "docsUrl": "https://example.test/docs",
                "blogUrl": "",
            }
        ]
        with tempfile.TemporaryDirectory() as td:
            site = self._site(
                Path(td),
                books,
                ["codex.epub", "covers/codex.png"],
            )
            self.assertEqual(self._run(site), 0)

    def test_missing_cover_fails(self) -> None:
        """The exact defect that shipped: a cover the index points at is gone."""
        books = [
            {
                "id": "deepseek-harness",
                "kind": "site",
                "href": "https://example.test/",
                "cover": "covers/deepseek.png",
                "docsUrl": "https://example.test/",
                "blogUrl": "",
            }
        ]
        with tempfile.TemporaryDirectory() as td:
            site = self._site(Path(td), books, [])
            self.assertEqual(self._run(site), 1)

    def test_missing_epub_fails(self) -> None:
        books = [
            {
                "id": "codex",
                "kind": "vendor",
                "href": "codex.epub",
                "cover": "covers/codex.png",
                "docsUrl": "https://example.test/docs",
                "blogUrl": "",
            }
        ]
        with tempfile.TemporaryDirectory() as td:
            site = self._site(Path(td), books, ["covers/codex.png"])
            self.assertEqual(self._run(site), 1)

    def test_linked_site_is_not_expected_to_be_an_epub(self) -> None:
        """A shelf entry links to another publication; it is not an EPUB here."""
        books = [
            {
                "id": "pi-handbook",
                "kind": "site",
                "href": "https://example.test/pi/",
                "cover": "covers/pi.png",
                "docsUrl": "https://example.test/pi/",
                "blogUrl": "",
            },
            {
                "id": "codex",
                "kind": "vendor",
                "href": "codex.epub",
                "cover": "covers/codex.png",
                "docsUrl": "https://example.test/docs",
                "blogUrl": "",
            },
        ]
        with tempfile.TemporaryDirectory() as td:
            site = self._site(
                Path(td),
                books,
                ["codex.epub", "covers/codex.png", "covers/pi.png"],
            )
            self.assertEqual(self._run(site), 0)

    def test_stray_epub_fails(self) -> None:
        books = [
            {
                "id": "codex",
                "kind": "vendor",
                "href": "codex.epub",
                "cover": "covers/codex.png",
                "docsUrl": "https://example.test/docs",
                "blogUrl": "",
            }
        ]
        with tempfile.TemporaryDirectory() as td:
            site = self._site(
                Path(td),
                books,
                ["codex.epub", "covers/codex.png", "dropped.epub"],
            )
            self.assertEqual(self._run(site), 1)


if __name__ == "__main__":
    unittest.main()
