"""Parse Claude blog listing HTML for post URLs and pagination."""

from __future__ import annotations

import re
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

DEFAULT_LISTING = "https://claude.com/blog"
BLOG_PATH = re.compile(r"^/blog/([A-Za-z0-9][A-Za-z0-9\-]*)/?$")
PAGE_COUNT_RE = re.compile(r"(\d+)\s*/\s*(\d+)")
COLLECTION_PAGE_RE = re.compile(r"([0-9a-fA-F]+)_page=(\d+)")


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
    if host not in {"claude.com", "www.claude.com"}:
        return None
    match = BLOG_PATH.match(parsed.path)
    if not match:
        return None
    slug = match.group(1)
    if slug in {"category", "tag", "author"}:
        return None
    return f"https://claude.com/blog/{slug}"


def extract_blog_urls(html: str, base: str = "https://claude.com") -> list[str]:
    """De-duplicated https://claude.com/blog/<slug> URLs in first-seen order."""
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[str] = []
    for tag in soup.find_all("a", href=True):
        url = normalize_blog_url(tag["href"], base=base)
        if url and url not in seen:
            seen.add(url)
            out.append(url)
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
