"""Collect and rewrite doc-body images for EPUB packaging."""

from __future__ import annotations

import hashlib
import mimetypes
import re
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup

IMG_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"}
MD_IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def normalize_image_url(src: str, base: str = "https://learn.chatgpt.com") -> str | None:
    if not src:
        return None
    src = src.strip().strip("<>")
    if src.startswith("data:"):
        return None
    if src.startswith("//"):
        src = "https:" + src
    absolute = urljoin(base if base.endswith("/") else base + "/", src)
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    return absolute


def collect_markdown_image_urls(md: str, base: str = "https://learn.chatgpt.com") -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in MD_IMG_RE.findall(md):
        url = normalize_image_url(raw, base=base)
        if url and url not in seen:
            seen.add(url)
            out.append(url)
    return out


def collect_image_urls(html: str, base: str = "https://learn.chatgpt.com") -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[str] = []
    for img in soup.find_all("img"):
        raw = img.get("src") or img.get("data-src") or ""
        url = normalize_image_url(raw, base=base)
        if url and url not in seen:
            seen.add(url)
            out.append(url)
        srcset = img.get("srcset") or img.get("data-srcset") or ""
        for part in srcset.split(","):
            token = part.strip().split(" ")[0]
            url = normalize_image_url(token, base=base)
            if url and url not in seen:
                seen.add(url)
                out.append(url)
    return out


def local_name_for_url(url: str) -> str:
    parsed = urlparse(url)
    raw_name = unquote(Path(parsed.path).name) or "image"
    raw_name = re.sub(r"[^\w.\-]+", "_", raw_name).strip("._") or "image"
    stem = Path(raw_name).stem[:60] or "image"
    ext = Path(raw_name).suffix.lower()
    if ext not in IMG_EXT:
        ext = ""
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return f"{digest}_{stem}{ext}"


def guess_ext(content_type: str | None, url: str) -> str:
    name = local_name_for_url(url)
    existing = Path(name).suffix.lower()
    if existing in IMG_EXT:
        return existing
    mapping = {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
        "image/avif": ".avif",
    }
    if content_type:
        ctype = content_type.split(";")[0].strip().lower()
        if ctype in mapping:
            return mapping[ctype]
        ext = mimetypes.guess_extension(ctype) or ""
        if ext == ".jpe":
            ext = ".jpg"
        if ext in IMG_EXT:
            return ext
    return ".img"


def rewrite_body_images(
    body_html: str,
    url_to_rel: dict[str, str],
    base: str = "https://learn.chatgpt.com",
) -> str:
    soup = BeautifulSoup(body_html, "lxml")
    for img in soup.find_all("img"):
        raw = img.get("src") or img.get("data-src") or ""
        if not raw:
            srcset = img.get("srcset") or ""
            raw = srcset.split(",")[0].strip().split(" ")[0] if srcset else ""
        url = normalize_image_url(raw, base=base)
        rel = None
        if url and url in url_to_rel:
            rel = url_to_rel[url]
        elif raw in url_to_rel:
            rel = url_to_rel[raw]
        if rel:
            img["src"] = rel
        elif (raw or "").startswith("images/"):
            img["src"] = raw.split("?")[0]
        else:
            # Drop remotes so pandoc cannot fetch during offline pack.
            img.decompose()
            continue
        for attr in ("srcset", "data-src", "data-srcset", "sizes"):
            if img.has_attr(attr):
                del img[attr]
    root = soup.body if soup.body else soup
    if hasattr(root, "decode_contents"):
        return root.decode_contents()
    return str(root)
