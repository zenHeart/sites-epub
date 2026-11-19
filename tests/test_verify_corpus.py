"""Regression tests for the corpus content gate (issue #2, root cause 3).

The gate has to *fail* on the two shapes that cost a full day in 2026-10-10:

* a route that carries no article at all (a shell page), and
* a route that exists but no longer holds the article (an abridged source).

The first is measured against the packer's own ``empty_or_stub_body`` threshold
so the two gates agree; the second is measured against the previous commit.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.path.insert(0, str(ROOT / ".agents" / "skills" / "site2epub" / "scripts"))

from verify_corpus import check_vendor  # noqa: E402


def _write_corpus(root: Path, vid: str, pages: dict[str, str]) -> None:
    corpus = root / "vendors" / vid / "corpus"
    (corpus / "pages").mkdir(parents=True, exist_ok=True)
    (corpus / "images").mkdir(parents=True, exist_ok=True)
    routes = [{"route": name, "url": f"https://x.test/{name}"} for name in pages]
    (corpus / "routes.json").write_text(json.dumps(routes), encoding="utf-8")
    (corpus / "image-map.json").write_text("{}", encoding="utf-8")
    for name, body in pages.items():
        (corpus / "pages" / f"{name}.md").write_text(body, encoding="utf-8")


LONG = "<!DOCTYPE html><html><body><article><p>" + ("content " * 40000) + "</p></article></body></html>"


class VerifyCorpusTest(unittest.TestCase):
    def test_shell_page_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"good": LONG, "shell": "<html><body>ok</body></html>"})
            result = check_vendor("acme", root=root)
        problems = result["problems"]
        self.assertTrue(any("shell page" in p for p in problems), problems)

    def test_thin_page_is_a_note_not_a_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"good": LONG, "thin": "<html><body>x" + "y" * 90 + "</body></html>"})
            result = check_vendor("acme", root=root)
        self.assertEqual(result["problems"], [], result["problems"])
        self.assertTrue(any("thin page" in n for n in result["notes"]), result["notes"])

    def test_healthy_corpus_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"a": LONG, "b": LONG})
            result = check_vendor("acme", root=root)
        self.assertEqual(result["problems"], [], result["problems"])

    def test_size_estimate_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"a": LONG})
            result = check_vendor("acme", root=root)
        self.assertIn("estimate_mb", result)
        self.assertGreater(result["text_mb"], 0)
        self.assertGreaterEqual(result["estimate_mb"], result["text_mb"] * 0.5)


if __name__ == "__main__":
    unittest.main()
