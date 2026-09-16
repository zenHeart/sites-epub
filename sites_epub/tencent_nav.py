"""Tencent vendor book: WorkBuddy (Tencent Cloud CodeBuddy team) product docs.

workbuddy.cn/docs is SSR with a clean product-domain split — one top-level
chapter per product domain (workbuddy / cli / ide / plugin / enterprise),
per the one-book-per-vendor + product-per-chapter rule.
"""

from __future__ import annotations

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .http import fetch_text
from .models import IndexEntry

DOCS_ROOT = "https://www.workbuddy.cn/docs/workbuddy/Overview"
GROUPS = {
    "workbuddy": "WorkBuddy 工作台",
    "cli": "WorkBuddy CLI",
    "ide": "WorkBuddy IDE 插件",
    "plugin": "WorkBuddy 插件",
    "enterprise": "企业版",
}
SKIP_SUFFIX = (".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf")


def parse_tencent_docs() -> list[IndexEntry]:
    html = fetch_text(DOCS_ROOT)
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for a in soup.find_all("a", href=True):
        href = a["href"].split("#", 1)[0].split("?", 1)[0]
        absolute = urljoin(DOCS_ROOT, href)
        p = urlparse(absolute)
        if p.netloc != "www.workbuddy.cn":
            continue
        path = p.path.rstrip("/")
        if not path.startswith("/docs/") or path.lower().endswith(SKIP_SUFFIX):
            continue
        parts = path[len("/docs/"):].strip("/").split("/")
        if not parts or not parts[0]:
            continue
        group = GROUPS.get(parts[0], "WorkBuddy 工作台")
        route = "wb-" + "-".join(parts).lower()
        if route in seen:
            continue
        title = " ".join(a.get_text(" ", strip=True).split()) or parts[-1]
        if not title:
            continue
        seen.add(route)
        out.append(
            IndexEntry(
                group=group,
                title=title,
                md_url=absolute,
                html_url=absolute,
                route=route,
                kind="doc",
            )
        )
    return out
