"""Zencoder vendor: blog + docs from sitemap; separate groups.

Zencoder is an independent AI coding agent (zencoder.ai, SOC2/ISO 27001
certified, supports 20+ IDEs). Its product docs live under /blog and
/docs. The .md twins for blog posts are not provided; HTML is the
authoritative form, so we still fetch the HTML version.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .http import fetch_text
from .models import IndexEntry


def parse_zencoder_docs() -> list[IndexEntry]:
    """Discover blog + docs URLs from sitemap; HTML is the canonical form."""
    out: list[IndexEntry] = []
    try:
        sitemap = fetch_text("https://zencoder.ai/sitemap.xml")
    except Exception:  # noqa: BLE001
        return out
    seen: set[str] = set()
    for loc in re.findall(r"<loc>([^<]+)</loc>", sitemap):
        p = urlparse(loc)
        path = p.path.strip("/")
        if not path or loc in seen:
            continue
        if not (path.startswith("blog/") or path.startswith("docs/")):
            continue
        if path.endswith(("feed/", "category/")):
            continue
        if "?" in loc:
            continue
        seen.add(loc)
        is_blog = path.startswith("blog/")
        kind = "blog" if is_blog else "doc"
        # Use the path slug as the title seed; HTML will overwrite on fetch
        slug = path.rsplit("/", 1)[-1]
        title = slug.replace("-", " ")
        out.append(
            IndexEntry(
                group="Blog" if is_blog else "Zencoder Docs",
                title=title,
                md_url=loc,
                html_url=loc,
                route=("blog/" if is_blog else "docs/") + slug,
                kind=kind,
            )
        )
    return out
