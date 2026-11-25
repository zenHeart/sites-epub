#!/usr/bin/env python3
"""Scope + structure gate for the daily sites-epub refresh.

Checks, per vendor:
  1. route count vs HEAD (silent shrinkage detection, lessons §17/§20)
  2. Blog group must be the last TOC parent (SKILL.md scope rule)
  3. newly added routes that look like open-platform API docs (scope rule:
     "product book, not API book")
  4. zero-byte corpus pages (lessons §21)

Usage: scope_gate.py [vendor_id ...]
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

API_ROUTE_PAT = re.compile(
    r"(api[-_]?reference|api[-_]?docs|/api/|openapi|platform[-_]?api|"
    r"developer[-_]?api|api[-_]?platform|rest[-_]?api|api[-_]?quickstart)",
    re.I,
)
BLOG_WORD = re.compile(r"blog|news|resource|article|公告|博客|新闻", re.I)

#: Routes deliberately dropped from the book, each after a live check.
#:
#: The shrinkage check exists because a shrinking book usually means a page was
#: lost without anyone deciding so (lessons §29: minimax lost its whole "MiniMax
#: Code" group because the product changed domain and the seed URL was never
#: updated). But some removals ARE decisions, and a gate that cannot tell the
#: two apart blocks the whole refresh for a non-defect.
#:
#: So each reviewed removal is written down here with its evidence. An
#: unreviewed removal still fails the gate; a reviewed one is reported and
#: accepted. Nothing here is a guess — each entry was probed live first.
#:
#: Format: vendor id -> {route: why it left the book}.
REVIEWED_REMOVALS: dict[str, dict[str, str]] = {
    "kimi": {
        # Both are client-rendered shells that never carried a document body:
        # the corpus page fetched on 2026-11-25 holds 116KB/169KB of markup but
        # only 75/124 characters of text, and that text is site chrome
        # ("新建会话 / 我的 Kimi / 插件 / 定时任务 / 灵感库"). Live probe on
        # 2026-11-26 returns 200 with the same shell (text_size 35/27, under
        # the 40-char stub threshold). Kimi's own sitemap omits them, the
        # homepage no longer links them, and no product hub does either — the
        # adapter's comment says the homepage anchors used to keep them. So the
        # book loses two empty chapters, not two pages of documentation.
        "inspiration": "client-rendered shell, no body text (75 chars in HEAD corpus, 35 live); unlinked by the site",
        "make3d": "client-rendered shell, no body text (124 chars in HEAD corpus, 27 live); unlinked by the site",
    },
    "zhipu": {
        # https://zcode.z.ai/cn/docs/repo-wiki — dropped from the ZCode docs nav
        # (zhipu_nav.py enumerates the links on /cn/docs/welcome, and the link is
        # gone). Live probe on 2026-11-26 answers 404, but so does a random
        # non-existent path (zcode.z.ai is a soft-404 SPA), so the page is
        # unreachable rather than moved: no other URL in the nav points at a
        # replacement. zcode-workflow and zcode-computer-use replaced it.
        "zcode-repo-wiki": "unlinked from the ZCode docs nav; unreachable upstream (soft-404 SPA)",
    },
    "gemini": {
        # https://support.google.com/gemini/answer/16802014 — "Create & manage AI
        # mini-apps or custom workflows as Gems from Google Labs". Google retired
        # the article and REUSED the id for an unrelated product's FAQ: the URL
        # now answers 200 with the title "Frequently asked questions | Opal |
        # Google for Developers". Keeping the chapter would have left a page
        # whose "view original" link opens a completely different document.
        # The topic itself is still covered by gemini-app/15146780 ("Use Gems in
        # Gemini Apps") and gemini-app/15236321 ("Get started with Gems").
        "gemini-app/16802014": "article retired upstream; its id was reused for an unrelated Opal FAQ",
    },
}


def git_show(rel: str):
    res = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True)
    if res.returncode != 0:
        return None
    try:
        return json.loads(res.stdout)
    except json.JSONDecodeError:
        return None


def split_removals(vid: str, removed: list[str]) -> tuple[list[str], list[str]]:
    """Split removed routes into (reviewed, unreviewed) for one vendor.

    A removal is "reviewed" when it is written down in REVIEWED_REMOVALS with
    the reason it left the book. Everything else is unexplained and must still
    fail the gate -- that is the whole point of the shrinkage check.
    """
    reviewed = REVIEWED_REMOVALS.get(vid, {})
    return (
        [r for r in removed if r in reviewed],
        [r for r in removed if r not in reviewed],
    )


def shrinkage_problem(
    vid: str, old_count: int, new_count: int, unreviewed_removed: list[str]
) -> str | None:
    """The shrinkage complaint, or None when the shrinkage is fully explained.

    Shrinkage only matters when it is unexplained: a route count that dropped
    because reviewed pages were retired is a decision, not an accident. Any
    unreviewed removal alongside a shrinking count still fails.
    """
    if new_count >= old_count:
        return None
    if not unreviewed_removed:
        return None
    return (
        f"{vid}: route shrinkage {old_count} -> {new_count} "
        f"(unreviewed removals: {unreviewed_removed})"
    )


def main(vids: list[str]) -> int:
    if not vids:
        vids = sorted(p.name for p in (ROOT / "vendors").iterdir() if p.is_dir())
    problems = []
    for vid in vids:
        rp = ROOT / "vendors" / vid / "corpus" / "routes.json"
        if not rp.exists():
            continue
        routes = json.loads(rp.read_text(encoding="utf-8"))
        old = git_show(f"vendors/{vid}/corpus/routes.json") or []
        old_routes = {r["route"] for r in old}
        new_routes = {r["route"] for r in routes}
        added = sorted(new_routes - old_routes)
        removed = sorted(old_routes - new_routes)

        groups = []
        for r in routes:
            g = r.get("group")
            if g not in groups:
                groups.append(g)
        blog_groups = [g for g in groups if BLOG_WORD.search(g or "")]
        blog_last_ok = True
        if blog_groups:
            # the last group overall should be a blog-ish group
            blog_last_ok = bool(BLOG_WORD.search(groups[-1] or ""))

        api_routes = [
            r for r in routes
            if API_ROUTE_PAT.search(r.get("route", "")) or API_ROUTE_PAT.search(r.get("url", ""))
        ]

        empty_pages = []
        pages_dir = ROOT / "vendors" / vid / "corpus" / "pages"
        for p in pages_dir.glob("**/*.md"):
            if p.stat().st_size == 0:
                empty_pages.append(p.relative_to(pages_dir).as_posix())

        reviewed_removed, unreviewed_removed = split_removals(vid, removed)

        row = {
            "vendor": vid,
            "routes": len(routes),
            "routes_head": len(old),
            "added": len(added),
            "removed": len(removed),
            "reviewed_removed": len(reviewed_removed),
            "groups": len(groups),
            "last_group": groups[-1] if groups else None,
            "blog_last_ok": blog_last_ok,
            "api_routes": len(api_routes),
            "empty_pages": len(empty_pages),
        }
        print(json.dumps(row, ensure_ascii=False))
        complaint = shrinkage_problem(vid, len(old), len(routes), unreviewed_removed)
        if complaint:
            problems.append(complaint)
        if added:
            print(f"  + added: {added}")
        if removed:
            print(f"  - removed: {removed}")
        for r in reviewed_removed:
            print(f"  = reviewed removal: {r} -- {REVIEWED_REMOVALS[vid][r]}")
        if api_routes:
            print(f"  ! api-looking routes: {[r['route'] for r in api_routes][:20]}")
        if empty_pages:
            problems.append(f"{vid}: {len(empty_pages)} zero-byte pages {empty_pages[:5]}")
        if not blog_last_ok:
            problems.append(f"{vid}: Blog is not the last TOC parent (last={groups[-1]!r})")
    print("\nPROBLEMS:" if problems else "\nPROBLEMS: none")
    for p in problems:
        print(" -", p)
    return 1 if problems else 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main([a for a in sys.argv[1:] if not a.startswith("-")]))
