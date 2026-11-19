#!/usr/bin/env python3
"""Mechanical lint for hand-written route allowlists (issue #2, root cause 2).

A curated allowlist is a human decision, and human decisions drift.  kimi's
``RESOURCES_KEEP`` once held 136 entries; 27 of them had the shape of a
programmatic SEO landing page (``how-to-*``, ``*-ideas``, ``game-*``,
``ai-for-*``, ``*-examples``, ``3d-model``).  The filter itself worked
perfectly -- every route in the book was on the allowlist -- so the allowlist
was the thing that let them in, and no amount of re-reviewing the corpus
would have caught it.

So the lint checks the *allowlist*, not the corpus: an entry whose slug
matches a deny pattern must be listed in a companion ``<NAME>_EXEMPT`` set and
carry a written reason next to it.  A new SEO slug can no longer be added by
accident, and an exemption that nobody justified is itself a finding.

Usage::

    python3 .agents/skills/site2epub/scripts/seo_lint.py [file.py ...]

With no arguments every ``sites_epub/*.py`` module is scanned.  Exit code is
1 when a violation is found.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_GLOBS = ("sites_epub/*.py",)

#: Slug shapes that mark a programmatic SEO landing page rather than a tutorial
#: a reader of the book would follow (issue #2, root cause 2).
DENY_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"^how-to-", "how-to-*"),
    (r"-ideas$", "*-ideas"),
    (r"^game-", "game-*"),
    (r"^ai-for-", "ai-for-*"),
    (r"-examples$", "*-examples"),
    (r"3d-model", "3d-model"),
)

#: Names of the form ``<SOMETHING>_KEEP`` / ``_ALLOW`` / ``_WHITELIST`` are
#: treated as hand-written allowlists.
ALLOWLIST_NAME_RE = re.compile(r"^[A-Z][A-Z0-9_]*(?:KEEP|ALLOW|ALLOWLIST|WHITELIST)[A-Z0-9_]*$")
EXEMPT_SUFFIX = "_EXEMPT"
REASON_RE = re.compile(r"#\s*(?:allow|允许|豁免|理由)\b", re.I)


def _string_entries(node: ast.AST) -> list[tuple[str, int]]:
    """The string literals of a set/frozenset literal, with their line numbers."""
    if isinstance(node, ast.Call):  # frozenset({...})
        if not node.args:
            return []
        node = node.args[0]
    if isinstance(node, (ast.Set, ast.Tuple, ast.List)):
        return [
            (e.value, e.lineno)
            for e in node.elts
            if isinstance(e, ast.Constant) and isinstance(e.value, str)
        ]
    return []


def collect_allowlists(source: str) -> dict[str, dict[str, object]]:
    """Map every allowlist assignment in ``source`` to its entries and exemptions."""
    tree = ast.parse(source)
    found: dict[str, dict[str, object]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        for name in names:
            if name.endswith(EXEMPT_SUFFIX):
                continue  # the exemption set itself is not an allowlist
            if not ALLOWLIST_NAME_RE.match(name):
                continue
            entries = _string_entries(node.value)
            if not entries:
                continue
            found[name] = {
                "entries": entries,
                "exempt_name": name + EXEMPT_SUFFIX,
            }
    # second pass: attach the companion exemption sets
    exempts: dict[str, list[tuple[str, int]]] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id.endswith(EXEMPT_SUFFIX):
                exempts[target.id] = _string_entries(node.value)
    for name, data in found.items():
        data["exempt"] = dict(exempts.get(str(data["exempt_name"]), []))
    return found


def _matched_patterns(value: str) -> list[str]:
    return [label for pat, label in DENY_PATTERNS if re.search(pat, value)]


def lint_source(source: str, label: str = "<source>") -> list[str]:
    """Return the violations found in ``source``; empty list means clean."""
    lines = source.splitlines()
    problems: list[str] = []
    for name, data in collect_allowlists(source).items():
        entries: list[tuple[str, int]] = data["entries"]  # type: ignore[assignment]
        exempt: dict[str, int] = data["exempt"]  # type: ignore[assignment]
        values = {v for v, _ in entries}
        for value, _lineno in entries:
            hits = _matched_patterns(value)
            if hits and value not in exempt:
                problems.append(
                    f"{label}: {name} entry '{value}' has an SEO landing-page shape "
                    f"({', '.join(hits)}) and is not exempted"
                )
        for value, lineno in exempt.items():
            if value not in values:
                problems.append(f"{label}: {name} exemption '{value}' is not in the allowlist")
                continue
            if not _matched_patterns(value):
                problems.append(
                    f"{label}: {name} exemption '{value}' matches no deny pattern; remove it"
                )
                continue
            comment = lines[lineno - 1] if 0 < lineno <= len(lines) else ""
            if not REASON_RE.search(comment):
                problems.append(
                    f"{label}: {name} exemption '{value}' must carry a reason "
                    f"comment ('# allow: ...') on its own line"
                )
    return problems


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv if not a.startswith("-")]
    if not paths:
        paths = [p for pattern in DEFAULT_GLOBS for p in sorted(ROOT.glob(pattern))]
    problems: list[str] = []
    for path in paths:
        source = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT) if path.is_absolute() else path
        problems.extend(lint_source(source, str(rel)))
    if problems:
        print(f"SEO allowlist lint: {len(problems)} problem(s)")
        for problem in problems:
            print(f"FAIL {problem}")
        return 1
    print(f"SEO allowlist lint: clean ({len(paths)} file(s) scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
