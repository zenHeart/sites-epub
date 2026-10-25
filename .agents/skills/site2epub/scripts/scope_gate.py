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


def git_show(rel: str):
    res = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, capture_output=True)
    if res.returncode != 0:
        return None
    try:
        return json.loads(res.stdout)
    except json.JSONDecodeError:
        return None


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

        row = {
            "vendor": vid,
            "routes": len(routes),
            "routes_head": len(old),
            "added": len(added),
            "removed": len(removed),
            "groups": len(groups),
            "last_group": groups[-1] if groups else None,
            "blog_last_ok": blog_last_ok,
            "api_routes": len(api_routes),
            "empty_pages": len(empty_pages),
        }
        print(json.dumps(row, ensure_ascii=False))
        if len(routes) < len(old):
            problems.append(f"{vid}: route shrinkage {len(old)} -> {len(routes)}")
        if added:
            print(f"  + added: {added}")
        if removed:
            print(f"  - removed: {removed}")
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
