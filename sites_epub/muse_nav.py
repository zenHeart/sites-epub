"""Enumerate the Muse Code product tree from its server-rendered side nav.

The Muse site hosts Model API, open-weight model, cookbook, and agent-guide
documentation beside Muse Code. This adapter deliberately keeps only links
under ``/docs/muse-code`` so a product EPUB cannot absorb the platform tree.
"""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

from .models import IndexEntry


PREFIX = "/docs/muse-code"


def _clean_route(path: str) -> str | None:
    """Return a corpus route for a Muse Code path, or ``None`` out of scope."""
    clean = path.split("#", 1)[0].split("?", 1)[0].rstrip("/") or PREFIX
    if clean != PREFIX and not clean.startswith(PREFIX + "/"):
        return None
    suffix = clean[len(PREFIX) :].strip("/")
    return suffix or "index"


def _title(anchor, route: str) -> str:
    text = " ".join(anchor.get_text(" ", strip=True).split()) if anchor is not None else ""
    fallback = "Overview" if route == "index" else route.rsplit("/", 1)[-1]
    return text or fallback.replace("-", " ").title()


def parse_muse_docs(html: str, docs_url: str) -> list[IndexEntry]:
    """Parse the SSR side navigation and keep only Muse Code product pages."""
    parsed = urlparse(docs_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    base = origin + PREFIX
    seen: set[str] = set()
    entries: list[IndexEntry] = []
    try:
        from bs4 import BeautifulSoup

        anchors = BeautifulSoup(html, "lxml").find_all("a", href=True)
        links = [
            (a["href"], " ".join(a.get_text(" ", strip=True).split()))
            for a in anchors
        ]
    except ImportError:
        # Keep the adapter usable for offline route inspection when the optional
        # BeautifulSoup dependency is unavailable. Production runs use bs4.
        from lxml import html as lxml_html

        root = lxml_html.fromstring(html)
        links = [
            (a.get("href"), " ".join(a.text_content().split()))
            for a in root.xpath(".//a[@href]")
        ]
    for href, anchor_title in links:
        absolute = urljoin(base, href)
        target = urlparse(absolute)
        if target.netloc and target.netloc != parsed.netloc:
            continue
        route = _clean_route(target.path)
        if route is None or route in seen:
            continue
        seen.add(route)
        html_url = f"{origin}{PREFIX}" + ("" if route == "index" else f"/{route}")
        entries.append(
            IndexEntry(
                group="Muse Code",
                title=anchor_title or _title(None, route),
                # musemuse.dev serves no .md twin (the URL returns a Next.js
                # error shell), so point md_url at the article itself: the
                # HTML-only pattern fetch_page handles via same_url.
                md_url=html_url,
                html_url=html_url,
                route=route,
                kind="doc",
            )
        )
    return entries

