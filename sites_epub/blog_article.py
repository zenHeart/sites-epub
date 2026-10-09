"""Extract title, article body, and image URLs from a Claude blog post."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from bs4 import BeautifulSoup, Tag

from .images import collect_image_urls

CHROME_SELECTORS = (
    "nav",
    "header",
    "footer",
    ".blog_related_section_wrap",
    ".is_related_posts",
    ".nav_desktop_layout",
    ".footer_wrap",
    # 2026-10 RSC rewrite: the Webflow class names are gone, but the related
    # posts rail / site nav carry stable CSS-module substrings.
    '[class*="RelatedPosts-module"]',
    '[class*="Navigation-module"]',
    '[class*="Footer-module"]',
)
TITLE_SUFFIX = re.compile(r"\s*\|\s*Claude by Anthropic\s*$", re.I)


@dataclass
class Article:
    title: str
    body_html: str
    body_text: str
    image_urls: list[str] = field(default_factory=list)
    url: str | None = None
    published: str | None = None
    author: str | None = None
    dek: str | None = None


def _plain(el: Tag) -> str:
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()


def _meta_content(soup: BeautifulSoup, *keys: str) -> str | None:
    for key in keys:
        tag = soup.find("meta", attrs={"property": key}) or soup.find("meta", attrs={"name": key})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None


def _is_visible_richtext(el: Tag) -> bool:
    classes = el.get("class") or []
    if "w-condition-invisible" in classes or "w-dyn-bind-empty" in classes:
        return False
    return bool(_plain(el))


def _collect_body_blocks(soup: BeautifulSoup) -> list[Tag]:
    """Every non-empty article richtext, in document order.

    Claude posts often split a short lede and the rest of the article across
    two ``blog_post_content_wrap`` columns. Returning only the first block
    drops the body (e.g. “Turn-based loops”).
    """
    seen: set[int] = set()
    blocks: list[Tag] = []
    selectors = (
        "div.blog_post_content_wrap div.u-rich-text-blog.w-richtext",
        "div.blog_post_content_wrap .w-richtext",
        "div.u-rich-text-blog.w-richtext",
        # 2026-10: the RSC rewrite dropped every blog_post_content_wrap wrapper
        # but kept the Webflow ``w-richtext`` class on the single article body
        # div (verified 3192 chars on /resources/articles/1m-context). It sits
        # inside the article element, siblings of the related-posts rail, so
        # picking it directly keeps that rail out of the body.
        "article .w-richtext",
        ".w-richtext",
    )
    for sel in selectors:
        found = False
        for el in soup.select(sel):
            if id(el) in seen or not _is_visible_richtext(el):
                continue
            seen.add(id(el))
            blocks.append(el)
            found = True
        if found:
            return blocks
    return blocks


def _pick_body(soup: BeautifulSoup) -> Tag | None:
    blocks = _collect_body_blocks(soup)
    if len(blocks) == 1:
        return blocks[0]
    if len(blocks) > 1:
        # 新版 Claude 博客把客户引述卡等正文组件放在 richtext 块之间的夹层,
        # 只拼接 richtext 会整段丢内容;改取所有块的最近公共祖先,
        # 由既有的 chrome/related 清理链兜底去除噪声。
        for candidate in blocks[0].parents:
            if all(candidate in el.parents for el in blocks):
                if candidate.name not in {"html", "body"} and candidate.parent is not None:
                    return candidate
                break
        container = soup.new_tag("div")
        container["class"] = ["article-body-merged"]
        for el in blocks:
            container.append(el)
        return container
    main = soup.find("main")
    if main:
        for related in main.select(".blog_related_section_wrap, .is_related_posts"):
            related.decompose()
        return main
    return soup.body


def _details_value(soup: BeautifulSoup, label: str) -> str | None:
    details = soup.select_one(".hero_blog_post_details")
    if not details:
        return None
    text = details.get_text(" ", strip=True)
    match = re.search(rf"{re.escape(label)}\s+(.+?)(?=\s+(?:Category|Product|Date|Reading time|Share|Author)|$)", text)
    if match:
        return match.group(1).strip(" |")
    return None


def _ldjson_nodes(soup: BeautifulSoup) -> list[object]:
    """Every object in every ld+json block, flattened out of @graph wrappers."""
    import json

    nodes: list[object] = []
    for tag in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = tag.string or tag.get_text() or ""
        raw = raw.strip()
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except ValueError:
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, list):
                stack.extend(node)
            elif isinstance(node, dict):
                if "@graph" in node:
                    graph = node["@graph"]
                    stack.extend(graph if isinstance(graph, list) else [graph])
                nodes.append(node)
    return nodes


def _ldjson_article(soup: BeautifulSoup) -> dict:
    """The first schema.org BlogPosting/Article node, if the page ships one.

    2026-10: the RSC pages dropped ``.hero_blog_post_details`` entirely, so the
    old Webflow byline scraping has nothing left to read. Every article page
    still emits a BlogPosting ld+json with datePublished / headline / author.
    """
    for node in _ldjson_nodes(soup):
        types = node.get("@type")
        types = types if isinstance(types, list) else [types]
        if any(t in {"BlogPosting", "Article", "NewsArticle"} for t in types):
            return node
    return {}


def extract_article(html: str, url: str | None = None) -> Article:
    soup = BeautifulSoup(html, "lxml")
    for sel in CHROME_SELECTORS:
        for el in soup.select(sel):
            el.decompose()

    h1 = soup.find("h1")
    title = _plain(h1) if h1 else ""
    ld = _ldjson_article(soup)
    if not title:
        og = _meta_content(soup, "og:title", "twitter:title")
        if og:
            title = TITLE_SUFFIX.sub("", og).strip()
        elif soup.title:
            title = TITLE_SUFFIX.sub("", soup.title.get_text(" ", strip=True)).strip()
    if not title:
        title = TITLE_SUFFIX.sub("", str(ld.get("headline") or "")).strip()
    if not title:
        title = "Untitled"

    dek_el = soup.select_one(".hero_blog_description_wrap")
    dek = _plain(dek_el) if dek_el else None
    if not dek:
        dek = (str(ld.get("description") or "").strip() or None)

    published = _details_value(soup, "Date")
    author = _details_value(soup, "Author(s)") or _details_value(soup, "Author")
    if not published:
        published = _meta_content(soup, "article:published_time")
    if not published:
        published = (str(ld.get("datePublished") or "").strip() or None)
    if not author:
        ld_author = ld.get("author")
        if isinstance(ld_author, dict):
            author = (str(ld_author.get("name") or "").strip() or None)
        elif isinstance(ld_author, list):
            names = [
                str(a.get("name") or "").strip()
                for a in ld_author
                if isinstance(a, dict) and a.get("name")
            ]
            author = ", ".join(names) or None
        elif ld_author:
            author = str(ld_author).strip()

    body_el = _pick_body(soup)
    if body_el is None:
        raise ValueError("article body not found")

    # Drop leftover related-post cards if they nested into the body container.
    for el in body_el.select(".card_blog_wrap, .blog_cms_item, .is_related_posts"):
        el.decompose()
    for el in list(body_el.select(".w-condition-invisible, .w-dyn-bind-empty")):
        if not _plain(el):
            el.decompose()
    # Video iframe fallbacks ("An error occurred.") and form chrome are not article body.
    for el in body_el.select(".player-unavailable, .w-form-fail, .w-form-done"):
        el.decompose()
    # Body subheads sometimes use h1; keep a single chapter-title h1 in the packer.
    for h1 in body_el.find_all("h1"):
        h1.name = "h2"

    body_html = body_el.decode_contents()
    body_text = re.sub(r"\s+", " ", body_el.get_text(" ", strip=True)).strip()
    if not body_text:
        raise ValueError("article body is empty")

    image_urls = collect_image_urls(body_html, base=url or "https://claude.com")
    return Article(
        title=title,
        body_html=body_html,
        body_text=body_text,
        image_urls=image_urls,
        url=url or _meta_content(soup, "og:url"),
        published=published,
        author=author,
        dek=dek,
    )


def chapter_html(article: Article, rewritten_body: str | None = None) -> str:
    """Wrap one article as an HTML fragment whose h1 becomes an EPUB chapter."""
    body = rewritten_body if rewritten_body is not None else article.body_html
    bits = [f"<h1>{_escape(article.title)}</h1>"]
    meta_parts = [p for p in (article.published, article.author, article.url) if p]
    if meta_parts:
        bits.append(f'<p class="chapter-meta">{_escape(" · ".join(meta_parts))}</p>')
    if article.dek:
        bits.append(f'<p class="chapter-dek"><em>{_escape(article.dek)}</em></p>')
    bits.append(body)
    return "\n".join(bits)


def _escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
