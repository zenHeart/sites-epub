"""Regression tests for the corpus content gate (issue #2, root cause 3).

The gate has to *fail* on the two shapes that cost a full day in 2026-10-10:

* a route that carries no article at all (a shell page), and
* a route that exists but no longer holds the article (an abridged source).

The first is measured against the packer's own ``empty_or_stub_body`` threshold
so the two gates agree; the second is measured against the previous commit.

The shrink rule compares *prose* on both sides, not raw bytes.  A page can lose
bytes without losing content: the sanitizer strips inline ``<script>`` blocks
from the corpus, and on 2026-11-26 that made zhipu's ``zcode-changelog`` look
like it had lost 60% of itself while its prose stayed byte-identical.  These
tests pin both halves: a real prose loss still fails, a script cleanup does not.
"""

from __future__ import annotations

import json
import subprocess
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


def _git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        env={
            "PATH": "/usr/bin:/bin:/usr/local/bin",
            "HOME": str(root),
            "GIT_CONFIG_GLOBAL": "/dev/null",
            "GIT_CONFIG_SYSTEM": "/dev/null",
        },
    )


def _commit_all(root: Path, message: str) -> None:
    _git(root, "init", "-q")
    _git(root, "add", "-A")
    _git(
        root,
        "-c", "user.email=gate@test.local",
        "-c", "user.name=gate",
        "commit", "-q", "-m", message,
    )


LONG = "<!DOCTYPE html><html><body><article><p>" + ("content " * 40000) + "</p></article></body></html>"
#: A page whose prose is real but whose payload is mostly inline JavaScript --
#: the shape the sanitizer cleans up.
SCRIPTY = (
    "<!DOCTYPE html><html><body><article><p>"
    + ("content " * 40000)
    + "</p></article><script>"
    + ("var x = 1; " * 40000)
    + "</script></body></html>"
)
CLEANED = (
    "<!DOCTYPE html><html><body><article><p>"
    + ("content " * 40000)
    + "</p></article></body></html>"
)


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


class ShrinkRuleTest(unittest.TestCase):
    """The shrink rule needs a committed baseline, so these use a real repo."""

    def test_real_prose_loss_still_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"page": LONG})
            _commit_all(root, "baseline")
            # The article is gone -- only a stub of it is left.
            _write_corpus(root, "acme", {"page": LONG[: len(LONG) // 3]})
            result = check_vendor("acme", root=root)
        problems = result["problems"]
        self.assertTrue(
            any("committed prose" in p for p in problems), problems
        )
        self.assertEqual(result["shrunk_pages"], 1, result)

    def test_script_cleanup_is_not_a_content_loss(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_corpus(root, "acme", {"page": SCRIPTY})
            _commit_all(root, "baseline")
            # The sanitizer stripped the inline script; the prose is untouched.
            _write_corpus(root, "acme", {"page": CLEANED})
            result = check_vendor("acme", root=root)
        self.assertEqual(result["problems"], [], result["problems"])
        self.assertEqual(result["shrunk_pages"], 0, result)
        self.assertEqual(result["cleaned_pages"], 1, result)

    def test_the_old_byte_rule_would_have_failed_the_cleanup_case(self):
        # Guard the test itself: the byte ratio really did halve, so the old
        # implementation would have reported a shrink here. Without this the
        # "cleanup is fine" case could pass for the wrong reason.
        self.assertLess(len(CLEANED), len(SCRIPTY) * 0.5)
        self.assertGreater(len(CLEANED), 0)


if __name__ == "__main__":
    unittest.main()
