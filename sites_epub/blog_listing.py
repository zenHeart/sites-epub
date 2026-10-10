"""Parse Claude blog listing HTML for post URLs and pagination."""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

DEFAULT_LISTING = "https://claude.com/blog"
# 2026-10: claude.com 308-redirects /blog/<slug> to /resources/articles/<slug>.
# Both spellings are accepted on input; the canonical URL is always the
# /resources/articles one, so legacy links and sitemap <loc> dedupe together.
LEGACY_BLOG_PATH = re.compile(r"^/blog/([A-Za-z0-9][A-Za-z0-9\-]*)/?$")
ARTICLE_PATH = re.compile(r"^/resources/articles/([A-Za-z0-9][A-Za-z0-9\-]*)/?$")
BLOG_PATH = re.compile(
    r"^(?:/blog|/resources/articles)/([A-Za-z0-9][A-Za-z0-9\-]*)/?$"
)
CANONICAL_BLOG = "https://claude.com/resources/articles"
PAGE_COUNT_RE = re.compile(r"(\d+)\s*/\s*(\d+)")
COLLECTION_PAGE_RE = re.compile(r"([0-9a-fA-F]+)_page=(\d+)")

# 2026-10: two signals had both gone stale at once for the engineering blog.
# claude.com/blog is now a React listing that renders ~6 posts and carries no
# Webflow pagination markers, and claude.com/sitemap.xml never listed the
# engineering posts — so /blog/a-harness-for-every-task-dynamic-workflows-in-claude-code
# (16k chars live) was enumerated by neither. Anthropic's engineering blog has
# moved to its own host and publishes its own sitemap; that is the missing
# second source, and it is what ``compile.discover_entries`` unions in.
ENGINEERING_HOST = "claude.dev"
ENGINEERING_BLOG_SITEMAP = "https://claude.dev/sitemap.xml"
ENGINEERING_BLOG_PATH = re.compile(r"^/blog/([A-Za-z0-9][A-Za-z0-9\-]*)/?$")


@dataclass(frozen=True)
class Pagination:
    collection_id: str | None
    current: int | None
    total: int | None
    next_href: str | None


def normalize_blog_url(href: str, base: str = "https://claude.com") -> str | None:
    if not href:
        return None
    href = href.strip()
    if href.startswith("#"):
        return None
    absolute = urljoin(base.rstrip("/") + "/", href)
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    host = parsed.netloc.lower()
    if host in {ENGINEERING_HOST, "www." + ENGINEERING_HOST}:
        match = ENGINEERING_BLOG_PATH.match(parsed.path)
        if not match:
            return None
        return f"https://{ENGINEERING_HOST}/blog/{match.group(1)}"
    if host not in {"claude.com", "www.claude.com"}:
        return None
    match = BLOG_PATH.match(parsed.path)
    if not match:
        return None
    slug = match.group(1)
    if slug in {"category", "tag", "author"}:
        return None
    return f"{CANONICAL_BLOG}/{slug}"


def extract_blog_urls(html: str, base: str = "https://claude.com") -> list[str]:
    """De-duplicated https://claude.com/resources/articles/<slug> URLs in first-seen order.

    2026-08: claude.com moved off Webflow; the listing is now a React app whose
    article links live in embedded JSON payloads. 2026-10: the listing page
    itself only renders ~7 posts, so sitemap.xml <loc> (appended to this html
    by fetch_vendor) is the real enumeration source — 257 root-language EN
    articles vs. 7 on the listing page. Walk <a> tags first, then sweep the raw
    text for both path spellings and <loc> so payload links are covered.
    normalize_blog_url still enforces host + EN slug, so i18n (/de/...) and
    chrome links stay excluded.
    """
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[str] = []

    def _add(href: str) -> None:
        url = normalize_blog_url(href, base=base)
        if url and url not in seen:
            seen.add(url)
            out.append(url)

    for tag in soup.find_all("a", href=True):
        _add(tag["href"])
    for href in re.findall(r'href="([^"]*/blog/[^"]*)"', html):
        _add(href)
    for href in re.findall(r'href="([^"]*/resources/articles/[^"]*)"', html):
        _add(href)
    for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", html, flags=re.I):
        _add(loc)
    return out


def extract_pagination(html: str) -> Pagination:
    soup = BeautifulSoup(html, "lxml")
    current: int | None = None
    total: int | None = None
    for el in soup.select(".w-page-count, [aria-label*='Page ']"):
        text = el.get("aria-label") or el.get_text(" ", strip=True)
        match = PAGE_COUNT_RE.search(text.replace("of", "/"))
        if match:
            current = int(match.group(1))
            total = int(match.group(2))
            break
        match = re.search(r"Page\s+(\d+)\s+of\s+(\d+)", text, re.I)
        if match:
            current = int(match.group(1))
            total = int(match.group(2))
            break

    next_href: str | None = None
    collection_id: str | None = None
    for tag in soup.select("a.w-pagination-next[href], a[aria-label='Next Page'][href]"):
        href = tag.get("href") or ""
        match = COLLECTION_PAGE_RE.search(href)
        if match:
            collection_id = match.group(1)
            next_href = href
            break
        if href and "page=" in href:
            next_href = href
            break

    if collection_id is None:
        for tag in soup.find_all("a", href=True):
            match = COLLECTION_PAGE_RE.search(tag["href"])
            if match:
                collection_id = match.group(1)
                break
    return Pagination(
        collection_id=collection_id,
        current=current,
        total=total,
        next_href=next_href,
    )


def listing_page_url(
    page: int,
    collection_id: str,
    listing: str = DEFAULT_LISTING,
) -> str:
    parsed = urlparse(listing)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{collection_id}_page={page}"


def next_listing_url(html: str, current_url: str) -> str | None:
    pag = extract_pagination(html)
    if pag.collection_id and pag.current and pag.total and pag.current < pag.total:
        return listing_page_url(pag.current + 1, pag.collection_id, listing=current_url.split("?")[0])
    if pag.next_href:
        return urljoin(current_url, pag.next_href)
    return None
