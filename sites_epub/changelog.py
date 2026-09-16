"""Per-vendor changelog derived from routes.json git history.

Every commit touching vendors/<id>/corpus/routes.json is one update event;
diffing consecutive committed versions yields added/removed pages (title +
original URL, doc vs blog via `kind`). No manual bookkeeping: git history is
the SSOT. Generated locally (`python -m sites_epub changelog`) because CI
checks out shallow; the rendered site/changelog.html is committed and
published as-is by the existing gh-pages flow.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path(__file__).with_name("changelog_tpl.html")
INITIAL_CAP = 400  # never list more than this many pages for the initial import


@dataclass
class Change:
    title: str
    url: str
    group: str
    kind: str  # doc | blog


@dataclass
class Update:
    date: str  # YYYY-MM-DD (commit date)
    subject: str
    short: str
    added: list[Change] = field(default_factory=list)
    removed: list[Change] = field(default_factory=list)


def _git(*args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True,
        encoding="utf-8", errors="replace", check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout


def _routes_at(rev: str, vid: str) -> dict[str, dict] | None:
    path = f"vendors/{vid}/corpus/routes.json"
    try:
        raw = _git("show", f"{rev}:{path}")
    except RuntimeError:
        return None
    try:
        entries = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return {e["route"]: e for e in entries}


def vendor_updates(vid: str) -> list[Update]:
    """One Update per commit touching the vendor's routes.json, newest first."""
    log = _git(
        "log", "--format=%H%x09%cs%x09%s",
        "--", f"vendors/{vid}/corpus/routes.json",
    ).strip()
    if not log:
        return []
    rows = [line.split("\t", 2) for line in log.splitlines()]  # newest -> oldest
    updates: list[Update] = []
    for i, (sha, date, subject) in enumerate(rows):
        cur = _routes_at(sha, vid)
        if cur is None:
            continue
        if i + 1 < len(rows):
            prev = _routes_at(rows[i + 1][0], vid) or {}
        else:
            prev = {}  # oldest commit = initial import
        added_routes = sorted(set(cur) - set(prev))
        removed_routes = sorted(set(prev) - set(cur))
        if not added_routes and not removed_routes and i + 1 < len(rows):
            continue  # touch-only commit, nothing to report
        upd = Update(
            date=date,
            subject=subject.strip(),
            short=sha[:7],
            added=[
                Change(cur[r].get("title") or r, cur[r].get("html_url", ""), cur[r].get("group", ""), cur[r].get("kind", "doc"))
                for r in added_routes[:INITIAL_CAP]
            ],
            removed=[
                Change(prev[r].get("title") or r, prev[r].get("html_url", ""), prev[r].get("group", ""), prev[r].get("kind", "doc"))
                for r in removed_routes[:INITIAL_CAP]
            ],
        )
        updates.append(upd)
    return updates


def changelog_payload() -> dict:
    vendors = []
    for v in load_catalog():
        updates = vendor_updates(v.id)
        if updates:
            vendors.append({
                "id": v.id,
                "name": v.name,
                "author": v.author or v.name,
                "chapters": v.chapters,
                "updates": [
                    {
                        "date": u.date,
                        "subject": u.subject,
                        "short": u.short,
                        # short keys match the template's JS (t/u/g/k)
                        "added": [{"t": c.title, "u": c.url, "g": c.group, "k": c.kind} for c in u.added],
                        "removed": [{"t": c.title, "u": c.url, "g": c.group, "k": c.kind} for c in u.removed],
                    }
                    for u in updates
                ],
            })
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "vendors": vendors,
    }


def render_changelog() -> str:
    payload = json.dumps(changelog_payload(), ensure_ascii=False)
    return TEMPLATE.read_text(encoding="utf-8").replace("__CHANGELOG_JSON__", payload)


def write_changelog(dest: Path) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / "changelog.html"
    out.write_text(render_changelog(), encoding="utf-8")
    return out
