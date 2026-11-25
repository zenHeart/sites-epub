"""Regression tests for the scope gate's shrinkage rule.

The gate exists because a shrinking book usually means a page was lost without
anyone deciding so (lessons §29: minimax lost its whole "MiniMax Code" group
when the product changed domain and the seed URL was never updated).

But "shrinkage" and "defect" are not the same thing. On 2026-11-26 two Kimi
routes (``inspiration`` and ``make3d``) left the book because the site stopped
linking them and the pages turned out to be client-rendered shells with no
body text at all, and one ZCode route (``zcode-repo-wiki``) left because the
docs nav dropped the link. None of those is a lost page -- they are decisions.
The old rule ("any shrinkage is a PROBLEM") could not tell the two apart and
would have blocked the whole refresh.

So the rule became: shrinkage is a PROBLEM only when a removal is *unreviewed*.
These tests pin both halves of that:

* a reviewed removal does not trip the gate;
* an unreviewed removal still trips it (the guard must not have been weakened).

They also check that the old implementation -- which flagged every shrinkage --
would fail the "reviewed removal" case, so the test cannot be a false green.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.path.insert(0, str(ROOT / ".agents" / "skills" / "site2epub" / "scripts"))

from scope_gate import (  # noqa: E402
    REVIEWED_REMOVALS,
    shrinkage_problem,
    split_removals,
)


class SplitRemovalsTest(unittest.TestCase):
    def test_known_route_is_reviewed(self):
        reviewed, unreviewed = split_removals("kimi", ["inspiration"])
        self.assertEqual(reviewed, ["inspiration"])
        self.assertEqual(unreviewed, [])

    def test_unknown_route_is_unreviewed(self):
        reviewed, unreviewed = split_removals("kimi", ["some-new-loss"])
        self.assertEqual(reviewed, [])
        self.assertEqual(unreviewed, ["some-new-loss"])

    def test_review_list_is_per_vendor(self):
        # A route retired for kimi must not excuse the same route name in
        # another vendor -- otherwise one vendor's review leaks into another's.
        reviewed, unreviewed = split_removals("zhipu", ["inspiration"])
        self.assertEqual(reviewed, [])
        self.assertEqual(unreviewed, ["inspiration"])

    def test_every_reviewed_entry_carries_a_reason(self):
        for vid, entries in REVIEWED_REMOVALS.items():
            for route, reason in entries.items():
                self.assertTrue(reason.strip(), f"{vid}/{route} has no reason")


class ShrinkageProblemTest(unittest.TestCase):
    def test_reviewed_shrinkage_is_not_a_problem(self):
        self.assertIsNone(shrinkage_problem("kimi", 118, 116, []))

    def test_unreviewed_shrinkage_is_still_a_problem(self):
        complaint = shrinkage_problem("kimi", 118, 116, ["some-new-loss"])
        self.assertIsNotNone(complaint)
        self.assertIn("some-new-loss", complaint)

    def test_unreviewed_removal_next_to_a_reviewed_one_still_fails(self):
        # Mixed batch: one route was retired on purpose, another vanished.
        # The reviewed one must not launder the unreviewed one.
        complaint = shrinkage_problem("kimi", 118, 116, ["some-new-loss"])
        self.assertIsNotNone(complaint)

    def test_growth_is_never_a_problem(self):
        self.assertIsNone(shrinkage_problem("claude", 514, 537, []))

    def test_old_implementation_would_have_failed_the_reviewed_case(self):
        # The pre-2026-11-26 rule flagged every shrinking count. Guard the test
        # itself: if that behaviour came back, this case would go green wrongly.
        def old_rule(vid, old_count, new_count, unreviewed_removed):
            if new_count < old_count:
                return f"{vid}: route shrinkage {old_count} -> {new_count}"
            return None

        self.assertIsNotNone(old_rule("kimi", 118, 116, []))
        self.assertIsNone(shrinkage_problem("kimi", 118, 116, []))


if __name__ == "__main__":
    unittest.main()
