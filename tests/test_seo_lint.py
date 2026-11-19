"""Regression tests for the allowlist SEO lint (issue #2, root cause 2).

kimi's ``RESOURCES_KEEP`` once held 136 entries, and 27 of them had the shape
of a programmatic SEO landing page.  The filter worked exactly as written --
every route in the book was on the allowlist -- so the allowlist was what let
them in.  The lint therefore has to catch them *in the allowlist*.

The fixture below is the historical offender set, verbatim from the 136-entry
allowlist that shipped before the prune (commit 914a7a2c^).
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.path.insert(0, str(ROOT / ".agents" / "skills" / "site2epub" / "scripts"))

from seo_lint import lint_source  # noqa: E402

#: The 27 slugs of the 136-entry allowlist that match a deny pattern.
HISTORICAL_SEO_SLUGS = (
    "agent-skills-examples",
    "ai-agents-examples",
    "ai-business-ideas",
    "ai-for-business",
    "ai-for-enterprise",
    "ai-in-business-examples",
    "ai-poster-ideas",
    "game-assets",
    "game-ideas",
    "how-to-build-a-business-website-for-free",
    "how-to-build-a-website",
    "how-to-build-a-website-from-scratch",
    "how-to-build-landing-pages",
    "how-to-create-a-3d-model-from-a-picture",
    "how-to-create-a-portfolio-website",
    "how-to-create-ai-images",
    "how-to-create-an-online-store-website",
    "how-to-create-game-assets",
    "how-to-draft-a-business-plan",
    "how-to-install-hermes-agent",
    "how-to-make-a-2d-game",
    "how-to-make-a-3d-game",
    "how-to-make-a-game-with-ai",
    "how-to-use-ai-in-business",
    "how-to-vibe-code",
    "how-to-write-a-business-proposal",
    "vibe-coding-examples",
)


def _allowlist_source(entries: str, exempt: str = "") -> str:
    return f"RESOURCES_KEEP = frozenset({{\n{entries}\n}})\n{exempt}"


class SeoLintTest(unittest.TestCase):
    def test_historical_allowlist_is_flagged(self):
        entries = "\n".join(f'    "{slug}",' for slug in HISTORICAL_SEO_SLUGS)
        problems = lint_source(_allowlist_source(entries), "fixture")
        self.assertGreaterEqual(
            len(problems), 24, "the lint must report at least the 24 known offenders"
        )
        for slug in HISTORICAL_SEO_SLUGS:
            self.assertTrue(
                any(slug in p for p in problems), f"{slug} was not reported"
            )

    def test_clean_allowlist_passes(self):
        entries = '\n    "kimi-brand",\n    "cursor-skills",\n    "create-skills",'
        self.assertEqual(lint_source(_allowlist_source(entries), "fixture"), [])

    def test_exemption_must_carry_a_reason(self):
        entries = '\n    "how-to-build-landing-pages",'
        exempt = (
            "\nRESOURCES_KEEP_EXEMPT = frozenset({\n"
            '    "how-to-build-landing-pages",\n'
            "})\n"
        )
        problems = lint_source(_allowlist_source(entries, exempt), "fixture")
        self.assertTrue(any("reason" in p for p in problems), problems)

    def test_exemption_with_reason_passes(self):
        entries = '\n    "how-to-build-landing-pages",'
        exempt = (
            "\nRESOURCES_KEEP_EXEMPT = frozenset({\n"
            '    "how-to-build-landing-pages",  # allow: 合同必需路由\n'
            "})\n"
        )
        self.assertEqual(lint_source(_allowlist_source(entries, exempt), "fixture"), [])

    def test_dead_exemption_is_reported(self):
        entries = '\n    "kimi-brand",'
        exempt = (
            "\nRESOURCES_KEEP_EXEMPT = frozenset({\n"
            '    "how-to-build-landing-pages",  # allow: 合同必需路由\n'
            "})\n"
        )
        problems = lint_source(_allowlist_source(entries, exempt), "fixture")
        self.assertTrue(any("not in the allowlist" in p for p in problems), problems)

    def test_repository_allowlists_are_clean(self):
        problems: list[str] = []
        for path in sorted(ROOT.glob("sites_epub/*.py")):
            problems.extend(lint_source(path.read_text(encoding="utf-8"), str(path.name)))
        self.assertEqual(problems, [], problems)


if __name__ == "__main__":
    unittest.main()
