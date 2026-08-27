"""Generic docs index: llms.txt first, then in-site /docs links."""

from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from .models import IndexEntry

LLMS_LINK = re.compile(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)")
BARE_URL = re.compile(r"^\s*-\s+(https?://\S+)")
I18N_PREFIX = re.compile(r"^/(es|ja|cn|ru|pt-BR|pt|de|fr|ko|zh)(/|$)", re.I)
SKIP_H1 = {"help center"}
SKIP_H2 = {"internationalization"}


def _title_from_path(path: str) -> str:
    slug = path.rstrip("/").rsplit("/", 1)[-1] or "overview"
    if slug.endswith(".md"):
        slug = slug[:-3]
    if slug in {"docs", "index", ""}:
        return "Overview"
    return slug.replace("-", " ")


def parse_llms_generic(text: str, docs_url: str) -> list[IndexEntry]:
    """Parse Mintlify-style [title](url) and Cursor-style nested bare URLs."""
    parsed = urlparse(docs_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    section = ""
    group = "Docs"
    skip = False
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            section = re.sub(r"\s+Documentation$", "", line[2:].strip(), flags=re.I)
            group = section or "Docs"
            skip = section.lower() in SKIP_H1 or "international" in section.lower()
            continue
        if line.startswith("## "):
            sub = line[3:].strip()
            group = f"{section}: {sub}" if section else (sub or group)
            skip = sub.lower() in SKIP_H2 or "international" in sub.lower()
            continue
        if skip:
            continue
        title = ""
        href = ""
        match = LLMS_LINK.match(line)
        if match:
            title, href = match.group(1), match.group(2).strip()
        else:
            match = BARE_URL.match(line)
            if match:
                href = match.group(1).strip().rstrip(").,")
        if not href:
            continue
        if href.count("://") != 1:
            continue
        href = href.split("#", 1)[0].split("?", 1)[0]
        absolute = urljoin(origin + "/", href)
        p = urlparse(absolute)
        if p.netloc and p.netloc != parsed.netloc:
            continue
        path = p.path or "/"
        if I18N_PREFIX.match(path):
            continue
        if path == "/help" or path.startswith("/help/"):
            continue
        if path.endswith(".md"):
            md_url = f"{p.scheme}://{p.netloc}{path}"
            html_url = re.sub(r"\.md$", "", md_url)
            route = re.sub(r"\.md$", "", path.lstrip("/"))
        else:
            html_url = f"{p.scheme}://{p.netloc}{path}".rstrip("/") or f"{p.scheme}://{p.netloc}/"
            md_url = html_url + ".md"
            route = path.strip("/") or "index"
        if not route or route in seen:
            continue
        seen.add(route)
        out.append(
            IndexEntry(
                group=group,
                title=title or _title_from_path(path),
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
