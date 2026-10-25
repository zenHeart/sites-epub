"""MiniMax vendor: one book aggregating the vendor's model-organized products.

Sources (user directive 2026-09-16: start at the vendor's /products-style
family entry; products are organized around models; one book per vendor):
- minimax.io/models/*  international model catalog pages (SSR nav)
- hailuoai.com         Hailuo consumer product pages (llms.txt index;
    hailuoai.video serves the identical index — not double-counted)
- minimax.io/blog     model release + research posts (product-facing writing)
- minimax.io/news     model/product announcements

The blog and news listings are enumerated separately because
``www.minimax.io/sitemap.xml`` lists 0 blog/news URLs (it only covers the
static marketing shell), so the corpus had no official writing at all until
this source was added. Blog is the last TOC parent, so these entries carry
``kind="blog"``.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .http import fetch_text
from .models import IndexEntry

LLMS_LINK = re.compile(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)", re.M)

#: ``/blog/<slug>`` research + release posts and ``/news/<slug>`` announcements.
POST_PATH = re.compile(r"^/(blog|news)/([A-Za-z0-9][A-Za-z0-9._\-]*)/?$")

SKIP_SUFFIX = (
    ".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp", ".ico",
    ".zip", ".pdf", ".json", ".xml", ".yaml", ".yml", ".css", ".js",
)

#: The model submenu ships as JSON inside the Next.js flight payload rather
#: than as ``<a href>`` anchors:
#: ``{\"title\":\"MiniMax M2.7\",\"link\":\"/models/text/m27\"}``.
#: Anchors alone silently drop the older models whenever the site collapses
#: that nav, so the payload is swept as a second enumeration surface.
MODEL_PAYLOAD_LINK = re.compile(
    r'\\?"title\\?":\\?"((?:[^"\\]|\\.){1,60}?)\\?",\\?"(?:link|href)\\?":'
    r'\\?"((?:/models|/product)[^"\\]*)\\?"'
)


def _clean(href: str, base: str) -> str | None:
    href = href.split("#", 1)[0].split("?", 1)[0].strip()
    if not href or href.startswith(("mailto:", "javascript:")):
        return None
    absolute = urljoin(base, href)
    p = urlparse(absolute)
    if p.scheme not in {"http", "https"} or not p.netloc:
        return None
    path = p.path
    if not path or path == "/" or path.lower().endswith(SKIP_SUFFIX):
        return None
    return p.scheme + "://" + p.netloc + path.rstrip("/")


def parse_minimax_docs() -> list[IndexEntry]:
    docs: list[IndexEntry] = []

    # 1. minimax.io model catalog (SSR nav)
    html = fetch_text("https://www.minimax.io/models")
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        clean = _clean(a["href"], "https://www.minimax.io/models")
        if not clean or "minimax.io" not in clean:
            continue
        p = urlparse(clean)
        if not (p.path.startswith("/models") or p.path.startswith("/product")):
            continue
        route = "minimax-io" + p.path.strip("/").replace("/", "-")
        if route in seen:
            continue
        seen.add(route)
        title = " ".join(a.get_text(" ", strip=True).split()) or p.path.rsplit("/", 1)[-1]
        if not title:
            continue
        docs.append(
            IndexEntry(
                group="MiniMax Models",
                title=title,
                md_url=clean + ".md",
                html_url=clean,
                route=route,
                kind="doc",
            )
        )

    # 1b. Same catalog, second enumeration surface: the model submenu is JSON
    # in the Next.js flight payload, so the <a href> anchors alone dropped
    # M2.5 / M2.7 (both still live) and shrank the book by two chapters.
    # Union both surfaces so a nav change cannot shrink the corpus silently.
    for ptitle, href in MODEL_PAYLOAD_LINK.findall(html):
        clean = _clean(href, "https://www.minimax.io/models")
        if not clean or "minimax.io" not in clean:
            continue
        p = urlparse(clean)
        if not (p.path.startswith("/models") or p.path.startswith("/product")):
            continue
        route = "minimax-io" + p.path.strip("/").replace("/", "-")
        if route in seen:
            continue
        seen.add(route)
        title = " ".join(ptitle.replace('\\"', '"').split()) or p.path.rstrip("/").rsplit("/", 1)[-1]
        if not title:
            continue
        docs.append(
            IndexEntry(
                group="MiniMax Models",
                title=title,
                md_url=clean + ".md",
                html_url=clean,
                route=route,
                kind="doc",
            )
        )

    # 2. MiniMax Code ("MiniMax Agent" coding product).
    # The site root is a client-rendered shell that yields no body and no
    # images, so only the server-rendered download page is a chapter.
    # 2026-10-26: the product moved from code.minimax.io to agent.minimax.io.
    # The old host now answers a flat nginx 404 for the whole subdomain, which
    # made §21's empty-body rule drop the route and silently delete the whole
    # "MiniMax Code" group (58 -> 57 chapters). The new host serves the same
    # page under the same title, so the seed URL is repointed and the retired
    # host is kept as a fallback. Route id / group / title rule are unchanged,
    # so the corpus file identity and the chapter count stay stable.
    for u in ("https://agent.minimax.io/download", "https://code.minimax.io/download"):
        try:
            chtml = fetch_text(u)
        except Exception:  # noqa: BLE001
            continue
        if not chtml.strip():
            continue
        csoup = BeautifulSoup(chtml, "lxml")
        ctitle = csoup.title.get_text(" ", strip=True).split(":")[0].strip() if csoup.title else "MiniMax Code"
        docs.append(
            IndexEntry(
                group="MiniMax Code",
                title=ctitle + (" · Download" if u.endswith("/download") else ""),
                md_url=u,
                html_url=u,
                route="mm-code" + ("-download" if u.endswith("/download") else ""),
                kind="doc",
            )
        )
        break

    # 3. MiniMax Design (design.minimax.io — SSR creative tools product)
    dhtml = fetch_text("https://design.minimax.io/")
    dsoup = BeautifulSoup(dhtml, "lxml")
    dseen: set[str] = set()
    for a in dsoup.find_all("a", href=True):
        clean = _clean(a["href"], "https://design.minimax.io/")
        if not clean or "design.minimax.io" not in clean:
            continue
        p = urlparse(clean)
        if not p.path or p.path == "/":
            continue
        # /media-plan/* is the pricing and subscription funnel, not usage docs.
        if p.path.startswith("/media-plan"):
            continue
        route = "mm-design-" + re.sub(r"[^a-z0-9-]+", "-", p.path.strip("/").lower()).strip("-")
        if route in dseen:
            continue
        dseen.add(route)
        title = " ".join(a.get_text(" ", strip=True).split()) or p.path.strip("/")
        if not title:
            continue
        docs.append(
            IndexEntry(
                group="MiniMax Design",
                title=title,
                md_url=clean,
                html_url=clean,
                route=route,
                kind="doc",
            )
        )

    # 4. Hailuo consumer product pages (llms.txt; .video mirrors it)
    text = fetch_text("https://hailuoai.com/llms.txt")
    seen2: set[str] = set()
    for title, href in LLMS_LINK.findall(text):
        clean = _clean(href, "https://hailuoai.com/llms.txt")
        if not clean:
            continue
        p = urlparse(clean)
        if not (p.netloc.endswith("hailuoai.com") or p.netloc.endswith("hailuoai.video")):
            continue
        route = "hailuo-" + re.sub(r"[^a-z0-9-]+", "-", p.path.strip("/").lower()).strip("-")
        if not route or route == "hailuo" or route in seen2:
            continue
        seen2.add(route)
        docs.append(
            IndexEntry(
                group="Hailuo 产品",
                title=title.strip(),
                md_url=clean,
                html_url=clean,
                route=route,
                kind="doc",
            )
        )
    return docs


def parse_minimax_blog(html: str, blog_url: str) -> list[IndexEntry]:
    """Research / release posts from the ``/blog`` and ``/news`` listings.

    minimax.io is a Next.js site, so the listing's card grid ships as escaped
    JSON rather than only as anchors — both are swept, and the slug is the
    route. Titles are seeded from the slug and replaced by the real article
    title at extraction time.
    """
    out: list[IndexEntry] = []
    seen: set[str] = set()
    candidates = re.findall(r'href="(/[A-Za-z0-9/_.\-]*)"', html)
    candidates += re.findall(r'"(/[A-Za-z0-9/_.\-]+)"', html)
    for cand in candidates:
        match = POST_PATH.match(cand.rstrip("/") or "/")
        if not match:
            continue
        section, slug = match.group(1), match.group(2)
        route = f"{section}/{slug}"
        if route in seen:
            continue
        seen.add(route)
        url = f"https://www.minimax.io/{section}/{slug}"
        out.append(
            IndexEntry(
                group="Blog",
                title=slug.replace("-", " "),
                # No .md twin is published for these; pointing md_url at the
                # HTML page keeps the fetch to one request instead of a
                # guaranteed 404 followed by a retry.
                md_url=url,
                html_url=url,
                route=route,
                kind="blog",
            )
        )
    return out
