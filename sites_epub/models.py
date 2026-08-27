"""Shared types for vendor catalog entries and packed pages."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class IndexEntry:
    group: str
    title: str
    md_url: str
    html_url: str
    route: str
    kind: str = "doc"  # doc | blog


@dataclass
class Vendor:
    id: str
    name: str
    docs_url: str
    blog_url: str | None
    icon: str
    author: str = ""
    adapter: str = "generic"
    updated_at: str = ""
    packed_at: str = ""
    summary: str = ""
    category: str = "docs"
    chapters: int = 0


@dataclass
class LinkedSite:
    id: str
    name: str
    url: str
    author: str = ""
    summary: str = ""
    cover: str = ""
    category: str = "handbook"
    updated_at: str = ""


def unique_group_label(group: str, route: str, used: dict[str, str]) -> str:
    """Keep repeated group names distinct when they belong to nested routes."""
    if group not in used:
        used[group] = route
        return group
    prefix = route.split("/", 1)[0] if "/" in route else ""
    first = used[group]
    first_prefix = first.split("/", 1)[0] if "/" in first else ""
    if prefix and prefix != first_prefix:
        label = f"{prefix} · {group}"
    else:
        label = f"{group} (cont.)"
    n = 2
    base = label
    while label in used:
        label = f"{base} {n}"
        n += 1
    used[label] = route
    return label


@dataclass
class CompileResult:
    output: str
    fetched_routes: list[str] = field(default_factory=list)
    skipped_routes: list[str] = field(default_factory=list)
    fingerprints: dict[str, str] = field(default_factory=dict)
    chapters: int = 0


@dataclass
class FetchResult:
    fetched_routes: list[str] = field(default_factory=list)
    skipped_routes: list[str] = field(default_factory=list)
    fingerprints: dict[str, str] = field(default_factory=dict)
    entries: int = 0
