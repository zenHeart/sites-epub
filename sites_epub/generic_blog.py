"""Generic blog listing: unique in-site /blog/<slug> URLs."""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .models import IndexEntry

SLUG = re.compile(r"^/blog/([A-Za-z0-9][A-Za-z0-9\-_/]*)/?$")


def parse_blog_html(html: str, blog_url: str) -> list[IndexEntry]:
    parsed = urlparse(blog_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for a in soup.find_all("a", href=True):
        absolute = urljoin(blog_url, a["href"])
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        match = SLUG.match(p.path or "")
        if not match:
            continue
        slug = match.group(1).strip("/")
        if not slug or slug in {"category", "tag", "author", "page", "topic"}:
            continue
        route = f"blog/{slug}"
        if route in seen:
            continue
        title = " ".join(a.get_text(" ", strip=True).split()) or slug
        if len(title) > 120:
            title = slug.replace("-", " ")
        seen.add(route)
        html_url = f"{origin}/blog/{slug}"
        out.append(
            IndexEntry(
                group="Blog",
                title=title,
                md_url=html_url + ".md",
                html_url=html_url,
                route=route,
                kind="blog",
            )
        )
    return out
