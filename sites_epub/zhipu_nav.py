"""Zhipu (智谱 AI) vendor: API platform docs + product docs (ZCode, Z.ai chat).

Per scope rule (SKILL.md): product docs are the main content; the
open-platform API platform is now in a separate API book that is NOT
the focus of this collection, so this adapter stays focused on Zhipu
ZCode (Z.ai's product) — a future /api book is a separate concern.
"""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .http import fetch_text
from .models import IndexEntry

CHANGELOG_URL = "https://zcode.z.ai/cn/changelog"


def parse_zhipu_docs() -> list[IndexEntry]:
    """ZCode product docs at zcode.z.ai/cn/docs/* — 智谱自有产品."""
    out: list[IndexEntry] = []
    html = fetch_text("https://zcode.z.ai/cn/docs/welcome")
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#", 1)[0].split("?", 1)[0]
        if not href.startswith("/cn/docs/") or href.endswith("/"):
            continue
        if href in seen:
            continue
        seen.add(href)
        url = urljoin("https://zcode.z.ai", href)
        slug = href[len("/cn/docs/"):].strip("/").replace("/", "-")
        route = "zcode-" + slug
        title = " ".join(a.get_text(" ", strip=True).split()) or slug
        if not title:
            continue
        out.append(
            IndexEntry(
                group="ZCode 产品",
                title=title,
                md_url=url,
                html_url=url,
                route=route,
                kind="doc",
            )
        )
    # 版本发布与更新 sits beside /cn/docs rather than inside it, so the docs nav
    # never links it. It is the product's own release history — how to tell which
    # build ships which fix — so it belongs in the ZCode chapter.
    out.append(
        IndexEntry(
            group="ZCode 产品",
            title="版本发布与更新",
            md_url=CHANGELOG_URL,
            html_url=CHANGELOG_URL,
            route="zcode-changelog",
            kind="doc",
        )
    )
    return out
