"""Gemini vendor: multi-root docs (five origins) + blog.google, merged into one book.

Sources, discovered by probing each official host (2026-08-31):
- ai.google.dev      Gemini API / AI Studio guides  (/gemini-api/*, devsite HTML nav)
- ai.google.dev      Gemini API reference           (/api/*,       devsite HTML nav)
- geminicli.com      Gemini CLI docs                (/docs/*,      Astro sidebar, real .md twins)
- docs.cloud.google.com  Gemini Code Assist         (/gemini/docs/codeassist|code-review/*)
- antigravity.google Antigravity docs               (llms.txt [title](/docs/*) rows)
- jules.google       Jules docs + changelog         (llms.txt listing real .md files)
- firebase.google.com Firebase Studio               (/docs/studio*, devsite HTML nav)
- blog.google        Gemini product blog            (en-us sitemap, gemini sections)

Routes are namespaced per source so same-named paths from different origins
cannot overwrite each other in corpus/pages.
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
    ".zip", ".pdf", ".json", ".xml", ".yaml", ".yml", ".txt", ".css", ".js",
)

BLOG_SECTIONS = (
    "products-and-platforms/products/gemini/",
    "innovation-and-ai/products/gemini-app/",
    "innovation-and-ai/models-and-research/gemini-models/",
)

BLOG_SITEMAP = "https://blog.google/en-us/sitemap.xml"


def _clean_href(href: str, base: str) -> str | None:
    href = href.split("#", 1)[0].split("?", 1)[0].strip()
    if not href or href.startswith(("mailto:", "javascript:", "tel:")):
        return None
    absolute = urljoin(base, href)
    p = urlparse(absolute)
    if p.scheme not in {"http", "https"}:
        return None
    path = p.path
    if not path or path == "/":
        return None
    if path.lower().endswith(SKIP_SUFFIX):
        return None
    return p.scheme + "://" + p.netloc + path.rstrip("/")


def nav_entries(
    html: str,
    base_url: str,
    keep,
    group: str,
    prefix: str,
    root_title: str,
    strip: str = "",
) -> list[IndexEntry]:
    """Collect in-site links matching `keep`, namespaced under `prefix`.

    `strip` is the site-path prefix removed before namespacing, so
    /gemini-api/docs/quickstart under prefix "gemini-api/" becomes route
    "gemini-api/docs/quickstart" instead of "gemini-api/gemini-api/docs/quickstart".
    """
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[IndexEntry] = []
    for a in soup.find_all("a", href=True):
        clean = _clean_href(a["href"], base_url)
        if not clean:
            continue
        p = urlparse(clean)
        if not keep(p.path):
            continue
        tail = p.path[len(strip) :] if strip and p.path.startswith(strip) else p.path
        route = prefix + tail.strip("/")
        if route in seen:
            continue
        seen.add(route)
        title = " ".join(a.get_text(" ", strip=True).split())
        out.append(
            IndexEntry(
                group=group,
                title=title or route.rsplit("/", 1)[-1].replace("-", " "),
                md_url=clean + ".md",
                html_url=clean,
                route=route,
                kind="doc",
            )
        )
    # The landing page itself is the book's section opener; skip if the
    # sidebar already links it (duplicate URL must not become two chapters).
    root_url = base_url.split("#")[0].split("?")[0]
    if not any(e.html_url.rstrip("/") == root_url.rstrip("/") for e in out):
        out.insert(
            0,
            IndexEntry(
                group=group,
                title=root_title,
                md_url=root_url + ".md",
                html_url=root_url,
                route=prefix.rstrip("/"),
                kind="doc",
            ),
        )
    return out


def parse_gemini_docs() -> list[IndexEntry]:
    docs: list[IndexEntry] = []

    def fetch(url: str) -> str:
        return fetch_text(url)

    # 1. Gemini API guides (ai.google.dev)
    html = fetch("https://ai.google.dev/gemini-api/docs")
    docs += nav_entries(
        html,
        "https://ai.google.dev/gemini-api/docs",
        lambda p: p.startswith("/gemini-api/"),
        "Gemini API · AI Studio",
        "gemini-api/",
        "Gemini API overview",
        strip="/gemini-api",
    )
    # 2. Gemini API reference
    html = fetch("https://ai.google.dev/api")
    docs += nav_entries(
        html,
        "https://ai.google.dev/api",
        lambda p: p.startswith("/api/"),
        "Gemini API Reference",
        "api-ref/",
        "API reference",
        strip="/api",
    )
    # 3. Gemini CLI (geminicli.com — official site of google-gemini/gemini-cli)
    html = fetch("https://geminicli.com/docs")
    docs += nav_entries(
        html,
        "https://geminicli.com/docs",
        lambda p: p.startswith("/docs"),
        "Gemini CLI",
        "gemini-cli/",
        "Gemini CLI",
        strip="/docs",
    )
    # 4. Gemini Code Assist (cloud docs platform; developers.google.com redirects here)
    html = fetch("https://docs.cloud.google.com/gemini/docs/codeassist/overview")
    docs += nav_entries(
        html,
        "https://docs.cloud.google.com/gemini/docs/codeassist/overview",
        lambda p: p.startswith(("/gemini/docs/codeassist/", "/gemini/docs/code-review/")),
        "Gemini Code Assist",
        "code-assist/",
        "Gemini Code Assist",
        strip="/gemini/docs",
    )
    # 5. Antigravity (llms.txt; keep only the /docs/ section)
    text = fetch("https://antigravity.google/llms.txt")
    seen: set[str] = set()
    for title, href in LLMS_LINK.findall(text):
        clean = _clean_href(href, "https://antigravity.google/llms.txt")
        if not clean:
            continue
        p = urlparse(clean)
        if not p.netloc.endswith("antigravity.google") or not p.path.startswith("/docs/"):
            continue
        route = "antigravity/" + p.path[len("/docs/") :].strip("/")
        if route in seen:
            continue
        seen.add(route)
        docs.append(
            IndexEntry(
                group="Antigravity",
                title=title.strip(),
                md_url=clean + ".md",
                html_url=clean,
                route=route,
                kind="doc",
            )
        )
    # 6. Jules (llms.txt lists real .md files)
    text = fetch("https://jules.google/docs/llms.txt")
    seen = set()
    for title, href in LLMS_LINK.findall(text):
        clean = _clean_href(href, "https://jules.google/docs/llms.txt")
        if not clean:
            continue
        p = urlparse(clean)
        if not p.netloc.endswith("jules.google"):
            continue
        tail = re.sub(r"\.md$", "", p.path.strip("/"))
        if tail.startswith("docs/"):
            tail = tail[len("docs/") :]
        route = "jules/" + tail
        if route in seen:
            continue
        seen.add(route)
        docs.append(
            IndexEntry(
                group="Jules",
                title=title.strip(),
                md_url=clean,
                html_url=re.sub(r"\.md$", "", clean),
                route=route,
                kind="doc",
            )
        )
    # 7. Firebase Studio
    html = fetch("https://firebase.google.com/docs/studio")
    docs += nav_entries(
        html,
        "https://firebase.google.com/docs/studio",
        lambda p: p == "/docs/studio" or p.startswith("/docs/studio/"),
        "Firebase Studio",
        "firebase-studio/",
        "Firebase Studio",
        strip="/docs/studio",
    )
    return docs


def parse_gemini_blog() -> list[IndexEntry]:
    """blog.google Gemini sections from the en-us sitemap; Blog is the last TOC parent."""
    sitemap = fetch_text(BLOG_SITEMAP)
    out: list[IndexEntry] = []
    seen: set[str] = set()
    for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sitemap, flags=re.I):
        p = urlparse(loc)
        path = p.path.rstrip("/")
        if not any(f"/{section}" in path + "/" for section in BLOG_SECTIONS):
            continue
        route = "blog/" + path.strip("/")
        if route in seen:
            continue
        seen.add(route)
        title = path.rsplit("/", 1)[-1].replace("-", " ")
        out.append(
            IndexEntry(
                group="Blog",
                title=title,
                md_url=loc.rstrip("/"),
                html_url=loc.rstrip("/"),
                route=route,
                kind="blog",
            )
        )
    return out
