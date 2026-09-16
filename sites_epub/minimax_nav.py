"""MiniMax vendor: one book aggregating the vendor's model-organized products.

Sources (user directive 2026-09-16: start at the vendor's /products-style
family entry; products are organized around models; one book per vendor):
- minimax.io/models/*  international model catalog pages (SSR nav)
- hailuoai.com         Hailuo consumer product pages (llms.txt index;
    hailuoai.video serves the identical index — not double-counted)
"""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .http import fetch_text
from .models import IndexEntry

LLMS_LINK = re.compile(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)", re.M)

SKIP_SUFFIX = (
    ".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp", ".ico",
    ".zip", ".pdf", ".json", ".xml", ".yaml", ".yml", ".css", ".js",
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

    # 2. MiniMax Code (code.minimax.io — "MiniMax Agent" coding product)
    for u in ("https://code.minimax.io/", "https://code.minimax.io/download"):
        try:
            chtml = fetch_text(u)
        except Exception:  # noqa: BLE001
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
