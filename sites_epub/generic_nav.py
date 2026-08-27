"""Generic docs index: llms.txt first, then in-site /docs links."""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .models import IndexEntry

LLMS_LINK = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)")


def parse_llms_generic(text: str, docs_url: str) -> list[IndexEntry]:
    parsed = urlparse(docs_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    group = "Docs"
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for line in text.splitlines():
        if line.startswith("## "):
            group = line[3:].strip() or group
            continue
        match = LLMS_LINK.match(line.strip())
        if not match:
            continue
        title, href = match.group(1), match.group(2).strip()
        absolute = urljoin(origin + "/", href)
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        path = p.path or "/"
        if path.endswith(".md"):
            md_url = absolute
            html_url = re.sub(r"\.md$", "", absolute)
            route = path[1:] if path.startswith("/") else path
            route = re.sub(r"\.md$", "", route)
        else:
            html_url = absolute.split("#", 1)[0]
            md_url = html_url.rstrip("/") + ".md"
            route = path.strip("/") or "index"
        if not route or route in seen:
            continue
        seen.add(route)
        out.append(
            IndexEntry(
                group=group,
                title=title,
                md_url=md_url,
                html_url=html_url,
                route=route,
                kind="doc",
            )
        )
    return out


def parse_docs_html(html: str, docs_url: str) -> list[IndexEntry]:
    parsed = urlparse(docs_url)
    prefix = parsed.path.rstrip("/") or "/docs"
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    group = "Docs"
    for a in soup.find_all("a", href=True):
        href = a["href"]
        absolute = urljoin(docs_url, href)
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        path = (p.path or "/").rstrip("/") or "/"
        if prefix != "/" and not (path == prefix or path.startswith(prefix + "/")):
            continue
        if path.endswith(".md"):
            continue
        route = path.strip("/") or "index"
        if route in seen:
            continue
        title = " ".join(a.get_text(" ", strip=True).split()) or route.rsplit("/", 1)[-1]
        if not title or len(title) > 80:
            continue
        seen.add(route)
        html_url = f"{parsed.scheme}://{parsed.netloc}{path}"
        out.append(
            IndexEntry(
                group=group,
                title=title,
                md_url=html_url + ".md",
                html_url=html_url,
                route=route,
                kind="doc",
            )
        )
    return out
