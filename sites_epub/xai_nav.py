"""Parse docs.x.ai/llms.txt (`===/path===` Mintlify format) and x.ai/news blog.

docs.x.ai/llms.txt uses a custom section-per-page format instead of Mintlify's
typical `[title](url)` index. We split on `===/route===` markers, take the
first `# Title` after each marker as the page title, and group routes by URL
prefix.

x.ai/news uses `/news/<slug>` paths and Next.js server-rendered HTML.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .models import IndexEntry

SECTION_RE = re.compile(r"^===(/[^=]*)===\s*$")
H1_RE = re.compile(r"^#\s+(.+)$")

GROUP_BY_PREFIX = {
    "build": "Build",
    "developers": "Developers",
    "grok-bot": "Grok Bot",
    "grok": "Grok",
    "console": "Console",
    "integrations": "Integrations",
}


def _title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").strip().title() or slug


def _group_from_route(route: str) -> str:
    parts = route.strip("/").split("/")
    if not parts or parts == [""]:
        return "Overview"
    return GROUP_BY_PREFIX.get(parts[0], parts[0].replace("-", " ").title())


def _route_url(origin: str, route: str) -> tuple[str, str]:
    """Return (html_url, md_url) for a /route relative to docs origin."""
    clean = route.strip("/")
    if clean:
        html_url = f"{origin}/{clean}"
    else:
        html_url = origin + "/"
    return html_url, html_url + ".md"


def parse_xai_llms(text: str, docs_url: str) -> list[IndexEntry]:
    """Parse Mintlify `===/path===` sections into one entry per page."""
    parsed = urlparse(docs_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"

    out: list[IndexEntry] = []
    seen: set[str] = set()
    route = ""
    title = ""

    def flush() -> None:
        nonlocal route, title
        if not route or route in seen:
            route, title = "", ""
            return
        seen.add(route)
        html_url, md_url = _route_url(origin, route)
        slug = route.strip("/").rsplit("/", 1)[-1] or "index"
        out.append(
            IndexEntry(
                group=_group_from_route(route),
                title=title or _title_from_slug(slug),
                md_url=md_url,
                html_url=html_url,
                route=route.strip("/") or "index",
                kind="doc",
            )
        )
        route, title = "", ""

    for line in text.splitlines():
        sm = SECTION_RE.match(line)
        if sm:
            flush()
            route = sm.group(1)
            continue
        if not route or title:
            continue
        hm = H1_RE.match(line)
        if hm:
            title = hm.group(1).strip()
    return out


NEWS_SLUG = re.compile(r"^/news/([A-Za-z0-9][A-Za-z0-9\-_]*)/?$")
NEWS_SKIP_SLUGS = {
    "", "category", "tag", "author", "page", "topic", "api",
    "grok", "imagine", "voice", "automations", "workflows", "government",
}


def parse_xai_blog(html: str, blog_url: str) -> list[IndexEntry]:
    """Extract `/news/<slug>` article URLs from the news listing HTML."""
    parsed = urlparse(blog_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute = urljoin(blog_url, href)
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        match = NEWS_SLUG.match(p.path or "")
        if not match:
            continue
        slug = match.group(1)
        if slug in NEWS_SKIP_SLUGS:
            continue
        route = f"news/{slug}"
        if route in seen:
            continue
        seen.add(route)
        link_text = " ".join(a.get_text(" ", strip=True).split())
        title = link_text or _title_from_slug(slug)
        html_url = f"{origin}/news/{slug}"
        out.append(
            IndexEntry(
                group="News",
                title=title,
                md_url=html_url + ".md",
                html_url=html_url,
                route=route,
                kind="blog",
            )
        )
    return out


BOT_GUIDE_SLUG = re.compile(r"^/bot/guides/([A-Za-z0-9][A-Za-z0-9\-_]*)/?$")


def parse_xai_bot_guides(html: str, base_url: str) -> list[IndexEntry]:
    """Extract `/bot/guides/<slug>` from the guides listing page."""
    parsed = urlparse(base_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute = urljoin(base_url, href)
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        match = BOT_GUIDE_SLUG.match(p.path or "")
        if not match:
            continue
        slug = match.group(1)
        if slug in {"", "category", "tag"}:
            continue
        route = f"bot-guides/{slug}"
        if route in seen:
            continue
        seen.add(route)
        link_text = " ".join(a.get_text(" ", strip=True).split())
        title = link_text or _title_from_slug(slug)
        html_url = f"{origin}/bot/guides/{slug}"
        out.append(
            IndexEntry(
                group="Bot Guides",
                title=title,
                md_url=html_url + ".md",
                html_url=html_url,
                route=route,
                kind="doc",
            )
        )
    return out