"""Kimi product adapter: web-app nav pages + blog posts embedded in SSR state.

kimi.com is a SPA-ish Next-style site: the docs-ish product pages appear as
plain <a> links on the landing page, but the blog listing renders post links
from client state — only part of them are real anchors. The full slug set is
embedded in the SSR HTML, so scan the raw text for /blog/<slug> patterns.
"""

from __future__ import annotations

import re

from .generic_nav import parse_docs_html
from .models import IndexEntry

BLOG_SLUG = re.compile(r"/blog/([a-z0-9][a-z0-9-]{3,})")
BLOG_SKIP = {"page", "category", "tag", "author", "zh", "en"}


def parse_kimi_blog(html: str, blog_url: str) -> list[IndexEntry]:
    out: list[IndexEntry] = []
    seen: set[str] = set()
    for slug in BLOG_SLUG.findall(html):
        if slug in BLOG_SKIP or slug in seen:
            continue
        seen.add(slug)
        url = f"https://www.kimi.com/blog/{slug}"
        out.append(
            IndexEntry(
                group="Blog",
                title=slug.replace("-", " "),
                md_url=url,
                html_url=url,
                route=f"blog/{slug}",
                kind="blog",
            )
        )
    return out
