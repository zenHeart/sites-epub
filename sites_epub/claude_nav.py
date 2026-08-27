"""Parse code.claude.com/docs/llms.txt into (group, title, route) entries."""

from __future__ import annotations

import re

from .models import IndexEntry

LINK_RE = re.compile(
    r"^- \[([^\]]+)\]\((https://code\.claude\.com/docs/en/([^)\s]+))\)",
)
MD_SUFFIX = re.compile(r"\.md$", re.I)


def canonical_html_url(md_url: str) -> str:
    route = route_from_md_url(md_url)
    return f"https://code.claude.com/docs/en/{route}"


def route_from_md_url(md_url: str) -> str:
    marker = "/docs/en/"
    idx = md_url.find(marker)
    if idx < 0:
        raise ValueError(f"not an EN docs URL: {md_url}")
    path = md_url[idx + len(marker) :]
    path = path.split("#", 1)[0].split("?", 1)[0]
    return MD_SUFFIX.sub("", path).strip("/")


def parse_llms_txt(text: str) -> list[IndexEntry]:
    """De-duplicated EN doc entries in first-seen order, with section groups."""
    group = "Docs"
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for line in text.splitlines():
        if line.startswith("## "):
            group = line[3:].strip() or group
            continue
        match = LINK_RE.match(line.strip())
        if not match:
            continue
        title, md_url, _rest = match.group(1), match.group(2), match.group(3)
        if "/docs/en/" not in md_url:
            continue
        route = route_from_md_url(md_url)
        if not route or route in seen:
            continue
        seen.add(route)
        html_url = canonical_html_url(md_url)
        out.append(
            IndexEntry(
                group=group,
                title=title,
                md_url=md_url if md_url.endswith(".md") else html_url + ".md",
                html_url=html_url,
                route=route,
            )
        )
    return out
