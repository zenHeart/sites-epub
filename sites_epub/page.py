"""Extract title, body, and image URLs from a Claude Code docs page (Markdown preferred)."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag

from .images import collect_image_urls, collect_markdown_image_urls
from .mdx import strip_leaked_jsx_text, transform_mdx

INDEX_BANNER_RE = re.compile(
    r"^>\s*## Documentation Index\s*\n(?:>.*\n)*",
    re.M,
)
LEARN_BANNER_RE = re.compile(
    r"^>\s*For the complete documentation index, see .*(?:\n>\s.*)*\n?",
    re.M,
)


@dataclass
class DocPage:
    title: str
    body_html: str
    body_text: str
    image_urls: list[str] = field(default_factory=list)
    route: str = ""
    group: str = ""
    url: str | None = None


def strip_index_banner(md: str) -> str:
    text = INDEX_BANNER_RE.sub("", md, count=1)
    text = LEARN_BANNER_RE.sub("", text, count=1)
    return text.lstrip()


def title_from_markdown(md: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    for line in md.splitlines():
        text = line.strip()
        if not text or text.startswith((">", "```", "<", "[", "-", "*", "#")):
            continue
        sentence = text.split(". ")[0].strip().rstrip(".")
        if len(sentence) >= 8:
            return sentence[:120]
    return ""


def markdown_to_html(md: str) -> str:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required to convert docs markdown")
    proc = subprocess.run(
        [pandoc, "-f", "markdown-tex_math_dollars-tex_math_single_backslash", "-t", "html"],
        input=md,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc md→html failed: {(proc.stderr or proc.stdout).strip()}")
    return proc.stdout


def _plain(el: Tag) -> str:
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()


def extract_from_markdown(
    md: str,
    *,
    route: str = "",
    group: str = "",
    url: str | None = None,
) -> DocPage:
    cleaned = strip_index_banner(md)
    title = title_from_markdown(cleaned) or "Untitled"
    # Drop the first ATX h1 so the packer can own heading levels.
    body_md = re.sub(r"^# .+\n+", "", cleaned, count=1)
    body_md = transform_mdx(body_md, page_url=url)
    html = markdown_to_html(body_md)
    soup = BeautifulSoup(html, "lxml")
    root = soup.body if soup.body else soup
    text = _plain(root) if isinstance(root, Tag) else re.sub(r"\s+", " ", str(root))
    image_urls = collect_markdown_image_urls(body_md, base=url or "https://learn.chatgpt.com")
    html_imgs = collect_image_urls(
        root.decode_contents() if hasattr(root, "decode_contents") else html,
        base=url or "https://learn.chatgpt.com",
    )
    seen: set[str] = set()
    merged: list[str] = []
    for u in image_urls + html_imgs:
        if u not in seen:
            seen.add(u)
            merged.append(u)
    if not text and not merged:
        raise ValueError("doc body is empty")
    body_html = root.decode_contents() if hasattr(root, "decode_contents") else html
    body_html = sanitize_body_html(body_html, page_url=url)
    text_soup = BeautifulSoup(body_html, "lxml")
    text_root = text_soup.body if text_soup.body else text_soup
    text = _plain(text_root) if isinstance(text_root, Tag) else re.sub(r"\s+", " ", str(text_root))
    return DocPage(
        title=title,
        body_html=body_html,
        body_text=text,
        image_urls=merged,
        route=route,
        group=group,
        url=url,
    )


def rewrite_absolute_links(html: str, page_url: str | None) -> str:
    """Turn site-root links into https URLs so EPUB readers can open the original page."""
    if not page_url:
        return html
    parsed = urlparse(page_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    soup = BeautifulSoup(html, "lxml")
    root = soup.body if soup.body else soup
    for anchor in root.find_all("a", href=True):
        href = (anchor.get("href") or "").strip()
        if not href or href.startswith(("#", "mailto:", "http://", "https://")):
            continue
        if href.startswith("//"):
            abs_href = "https:" + href
        elif href.startswith("/"):
            abs_href = origin + href
        else:
            abs_href = urljoin(page_url, href)
        anchor["href"] = abs_href
        anchor["rel"] = "external"
    serialized = root.decode_contents() if hasattr(root, "decode_contents") else str(root)
    return serialized


def sanitize_body_html(html: str, page_url: str | None = None) -> str:
    """Drop chrome that would hijack pandoc's HTML reader (nested <main>/<section>)."""
    soup = BeautifulSoup(html, "lxml")
    root = soup.body if soup.body else soup
    for iframe in list(root.find_all("iframe")):
        src = (iframe.get("src") or "").strip()
        if src.startswith("//"):
            src = "https:" + src
        if src:
            note = soup.new_tag("p")
            note["class"] = "mdx-live-widget"
            link = soup.new_tag("a", href=src, rel="external")
            link.string = src
            note.append("Embedded media on the original page: ")
            note.append(link)
            iframe.replace_with(note)
        else:
            iframe.decompose()
    for sel in (
        "script",
        "style",
        "astro-island",
        "noscript",
        "[data-markdown-export='illustration']",
    ):
        for el in root.select(sel):
            el.decompose()
    # Page-local <section>/<main> would close packer wrappers. Keep figure/aside.
    for el in root.find_all(["main", "article", "section"]):
        el.name = "div"
        if el.has_attr("role"):
            del el["role"]
    pascal = re.compile(r"<[A-Z][A-Za-z0-9]*\b")
    for node in list(root.find_all(string=True)):
        raw = str(node)
        if pascal.search(raw) or "&lt;" in raw:
            node.replace_with(strip_leaked_jsx_text(raw))
    serialized = root.decode_contents() if hasattr(root, "decode_contents") else str(root)
    cleaned = strip_leaked_jsx_text(serialized)
    return rewrite_absolute_links(cleaned, page_url)


def extract_from_html(
    html: str,
    *,
    route: str = "",
    group: str = "",
    url: str | None = None,
) -> DocPage:
    soup = BeautifulSoup(html, "lxml")
    for sel in ("nav", "header", "footer", "[data-component-path]"):
        for el in soup.select(sel):
            if el.name in {"article", "main"}:
                continue
            el.decompose()
    article = soup.select_one("article") or soup.select_one("main") or soup.body
    if article is None:
        raise ValueError("doc body not found")
    h1 = article.find("h1") or soup.find("h1")
    title = _plain(h1) if h1 else (soup.title.get_text(" ", strip=True) if soup.title else "Untitled")
    if h1:
        h1.decompose()
    for logo in article.select('img[src*="mintcdn.com"][src*="logo/"]'):
        logo.decompose()
    # 站点 UI 小图标(侧栏模拟、按钮图标)不是正文插图,统一剔除。
    from .images import is_chrome_img_tag

    for img in article.find_all("img"):
        if is_chrome_img_tag(img):
            img.decompose()
    body_html = sanitize_body_html(
        article.decode_contents() if hasattr(article, "decode_contents") else str(article),
        page_url=url,
    )
    text_soup = BeautifulSoup(body_html, "lxml")
    text_root = text_soup.body if text_soup.body else text_soup
    text = _plain(text_root) if isinstance(text_root, Tag) else re.sub(r"\s+", " ", str(text_root))
    if not text:
        raise ValueError("doc body is empty")
    image_urls = collect_image_urls(body_html, base=url or "https://learn.chatgpt.com")
    return DocPage(
        title=title,
        body_html=body_html,
        body_text=text,
        image_urls=image_urls,
        route=route,
        group=group,
        url=url,
    )


def extract_page(
    source: str,
    *,
    route: str = "",
    group: str = "",
    url: str | None = None,
    kind: str | None = None,
) -> DocPage:
    hint = (kind or "").lower()
    looks_html = source.lstrip().lower().startswith("<!") or "<html" in source[:200].lower()
    if hint == "html" or (hint != "md" and looks_html):
        return extract_from_html(source, route=route, group=group, url=url)
    return extract_from_markdown(source, route=route, group=group, url=url)


def load_page(path: Path, **kwargs) -> DocPage:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    suffix = Path(path).suffix.lower()
    kind = "html" if suffix in {".html", ".htm"} else "md"
    return extract_page(text, kind=kind, **kwargs)
