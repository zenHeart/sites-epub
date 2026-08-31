"""Parse learn.chatgpt.com Codex product nav into grouped route entries."""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag

from .models import IndexEntry

SITE = "https://learn.chatgpt.com"
SIX_SECTIONS = (
    "Overview",
    "Features",
    "Configuration",
    "Developers",
    "Security",
    "Administration",
)
SKIP_SECTION = {"Use Cases", "Resources"}


def _plain(el: Tag) -> str:
    return " ".join(el.get_text(" ", strip=True).split())


def _norm_href(href: str) -> str | None:
    if not href:
        return None
    href = href.strip()
    if href.startswith("#"):
        return None
    if href.startswith("http://") or href.startswith("https://"):
        parsed = urlparse(href)
        if parsed.netloc not in {"learn.chatgpt.com", "www.learn.chatgpt.com"}:
            return None
        path = parsed.path or "/"
    else:
        path = urlparse(href).path or href.split("#", 1)[0].split("?", 1)[0]
    path = path.rstrip("/") or path
    if not path.startswith("/codex"):
        return None
    if path.startswith("/codex/use-cases") or path.startswith("/codex/resources"):
        return None
    return path


def route_from_path(path: str) -> str:
    return path.lstrip("/")


def html_url_for(path: str) -> str:
    return urljoin(SITE + "/", path.lstrip("/"))


def md_url_for(path: str) -> str:
    """Advertised twin: append .md to the page URL (often 302s to /docs/<slug>.md)."""
    return html_url_for(path) + ".md"


def _section_select(soup: BeautifulSoup) -> Tag | None:
    # 2026-08: site renamed aria-label "Docs section" → "Docs"; several selects
    # share that label. Locate by option-set instead of the brittle label text.
    for sel in soup.find_all("select"):
        labels = {_plain(opt) for opt in sel.find_all("option")}
        if {"Overview", "Features", "Administration"} <= labels:
            return sel
    return None


def parse_nav_html(html: str) -> list[IndexEntry]:
    """De-duplicated in-site Codex routes under the six horizontal sections."""
    soup = BeautifulSoup(html, "lxml")
    select = _section_select(soup)
    if select is None:
        raise ValueError("Codex six-section nav select not found")

    variant_to_group: dict[str, str] = {}
    for opt in select.find_all("option"):
        label = _plain(opt)
        vid = (opt.get("value") or "").strip()
        if not vid or label in SKIP_SECTION:
            continue
        if label not in SIX_SECTIONS:
            continue
        variant_to_group[vid] = label

    seen: set[str] = set()
    out: list[IndexEntry] = []
    for vid, group in variant_to_group.items():
        panel = soup.select_one(
            f'[data-mobile-nav-variant-content][data-variant-id="{vid}"]'
        )
        if panel is None:
            continue
        for a in panel.find_all("a"):
            path = _norm_href(a.get("href") or "")
            if not path:
                continue
            title = _plain(a) or path.rsplit("/", 1)[-1]
            route = route_from_path(path)
            if not route or route in seen:
                continue
            seen.add(route)
            out.append(
                IndexEntry(
                    group=group,
                    title=title,
                    md_url=md_url_for(path),
                    html_url=html_url_for(path),
                    route=route,
                )
            )
    return out


def format_nav_routes(entries: list[IndexEntry]) -> str:
    lines = [
        f"{e.group}\t{e.title}\t{e.html_url}\t{e.md_url}" for e in entries
    ]
    return "\n".join(lines) + ("\n" if lines else "")
