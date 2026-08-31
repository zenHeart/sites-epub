"""Gemini vendor: multi-root docs (six origins) + blog.google, merged into one book.

Sources, discovered by probing each official host (2026-08-31, scope 2):
- ai.google.dev      Gemini API / AI Studio guides  (/gemini-api/*, devsite HTML nav)
- ai.google.dev      Gemini API reference           (/api/*,       devsite HTML nav)
- antigravity.google Antigravity docs incl. agy CLI (llms.txt [title](/docs/*) rows)
- jules.google       Jules docs + changelog         (llms.txt listing real .md files)
- docs.cloud.google.com  Gemini Code Assist         (/gemini/docs/codeassist|code-review/*)
- support.google.com Gemini App help center         (/gemini/answer/*, 88 SSR articles;
     covers the web app, Canvas, Deep Research, Flow and Whisk usage)
- support.google.com NotebookLM help center         (/gemininotebook/answer/*, 24 articles)
- blog.google        Gemini product blog            (en-us sitemap, gemini sections)

Gemini CLI (geminicli.com) and Firebase Studio were dropped 2026-08-31: consumer
Gemini CLI stopped serving AI Pro/Ultra/free accounts on 2026-06-18 (official
transition to Antigravity CLI, binary `agy`), and Firebase Studio is outside the
membership-centered scope. Routes are namespaced per source so same-named paths
from different origins cannot overwrite each other in corpus/pages.
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


def help_center_entries(landing: str, product: str, group: str, prefix: str) -> list[IndexEntry]:
    """support.google.com help center: flat SSR landing links, expand topics once."""
    html = fetch_text(landing)
    soup = BeautifulSoup(html, "lxml")
    answers: dict[str, str] = {}
    topics: set[str] = set()
    for a in soup.find_all("a", href=True):
        absu = urljoin(landing, a["href"]).split("#")[0].split("?")[0]
        m = re.search(rf"/{product}/(topic|answer)/[A-Za-z0-9]+", absu)
        if not m:
            continue
        if m.group(1) == "topic":
            topics.add(m.group(0))
        else:
            answers.setdefault(m.group(0), " ".join(a.get_text(" ", strip=True).split()))
    for tp in sorted(topics):
        try:
            thtml = fetch_text(tp)
        except Exception:  # noqa: BLE001
            continue
        for a in BeautifulSoup(thtml, "lxml").find_all("a", href=True):
            absu = urljoin(tp, a["href"]).split("#")[0].split("?")[0]
            m = re.search(rf"/{product}/answer/[A-Za-z0-9]+", absu)
            if m:
                answers.setdefault(
                    m.group(0), " ".join(a.get_text(" ", strip=True).split())
                )
    out: list[IndexEntry] = []
    for path, title in sorted(answers.items()):
        clean = f"https://support.google.com{path}"
        out.append(
            IndexEntry(
                group=group,
                title=title or f"article {path.rsplit('/', 1)[-1]}",
                md_url=clean,
                html_url=clean,
                route=prefix + path.rsplit("/", 1)[-1],
                kind="doc",
            )
        )
    return out


def parse_gemini_docs() -> list[IndexEntry]:
    docs: list[IndexEntry] = []

    def fetch(url: str) -> str:
        return fetch_text(url)

    # 1. Gemini API guides (ai.google.dev) — includes the AI Studio quickstart tree
    html = fetch("https://ai.google.dev/gemini-api/docs")
    docs += nav_entries(
        html,
        "https://ai.google.dev/gemini-api/docs",
        lambda p: p.startswith("/gemini-api/"),
        "Gemini API and AI Studio",
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
    # 3. Antigravity incl. the agy CLI (llms.txt; keep only the /docs/ section)
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
    # 4. Jules (llms.txt lists real .md files)
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
    # 5. Gemini Code Assist (cloud docs platform; consumer IDE access stopped
    #    2026-06-18 but the Standard/Enterprise product line is still documented)
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
    # 6. Gemini App help center — web app, Canvas, Deep Research, Flow, Whisk
    docs += help_center_entries(
        "https://support.google.com/gemini/", "gemini", "Gemini App Help", "gemini-app/"
    )
    # 7. NotebookLM help center (renamed Gemini Notebook; support path gemininotebook)
    docs += help_center_entries(
        "https://support.google.com/notebooklm/",
        "gemininotebook",
        "NotebookLM Help",
        "notebooklm/",
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
