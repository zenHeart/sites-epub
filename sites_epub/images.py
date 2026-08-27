"""Collect and rewrite doc-body images for EPUB packaging."""

from __future__ import annotations

import hashlib
import mimetypes
import re
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

import warnings

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

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


def collect_source_image_urls(text: str, base: str) -> list[str]:
    """Markdown + HTML (including site-relative /images/...) from raw page source."""
    seen: set[str] = set()
    out: list[str] = []
    for url in collect_markdown_image_urls(text, base=base) + collect_image_urls(text, base=base):
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def rewrite_body_images(
    body_html: str,
    url_to_rel: dict[str, str],
    base: str = "https://learn.chatgpt.com",
    *,
    available: set[str] | None = None,
) -> str:
    """Keep <img> only when the local pack file exists. Never leave a dangling src."""
    available = available if available is not None else set(url_to_rel.values())
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
        elif (raw or "").split("?")[0].startswith("images/"):
            rel = raw.split("?")[0]
        if not rel or rel not in available:
            img.decompose()
            continue
        img["src"] = rel
        for attr in ("srcset", "data-src", "data-srcset", "sizes"):
            if img.has_attr(attr):
                del img[attr]
    root = soup.body if soup.body else soup
    if hasattr(root, "decode_contents"):
        return root.decode_contents()
    return str(root)


def resolve_epub_img_src(chapter: str, src: str, zip_names: set[str]) -> str | None:
    """Return the zip member for a chapter-relative img src, or None if missing."""
    src = (src or "").strip()
    if not src or src.startswith("data:"):
        return None
    if src.startswith(("http://", "https://", "//")):
        return None
    from posixpath import dirname, normpath, join

    candidates = [src.lstrip("/"), normpath(join(dirname(chapter), src))]
    for cand in candidates:
        if cand in zip_names:
            return cand
        if cand.startswith("../"):
            trimmed = cand
            while trimmed.startswith("../"):
                trimmed = trimmed[3:]
            if trimmed in zip_names:
                return trimmed
    base = src.rsplit("/", 1)[-1]
    if base:
        hits = [n for n in zip_names if n.endswith("/" + base)]
        if len(hits) == 1:
            return hits[0]
    return None


def repair_epub_images(epub_path: Path) -> int:
    """Strip <img> whose src is not a zip member. Returns how many tags were removed."""
    import zipfile

    epub_path = Path(epub_path)
    with zipfile.ZipFile(epub_path, "r") as zf:
        names = zf.namelist()
        name_set = set(names)
        contents = {name: zf.read(name) for name in names}
        infos = {info.filename: info for info in zf.infolist()}

    removed = 0
    for name in names:
        lower = name.lower()
        if not lower.endswith((".xhtml", ".html")):
            continue
        html = contents[name].decode("utf-8", errors="replace")
        soup = BeautifulSoup(html, "lxml")
        changed = False
        for img in list(soup.find_all("img")):
            src = (img.get("src") or "").strip()
            if resolve_epub_img_src(name, src, name_set):
                continue
            img.decompose()
            removed += 1
            changed = True
        if changed:
            root = soup
            contents[name] = str(root).encode("utf-8")

    if removed == 0:
        return 0

    tmp = epub_path.with_suffix(".epub.tmp")
    with zipfile.ZipFile(tmp, "w") as out:
        for name in names:
            info = infos[name]
            if name == "mimetype":
                out.writestr(info, contents[name], compress_type=zipfile.ZIP_STORED)
            else:
                out.writestr(info, contents[name])
    tmp.replace(epub_path)
    return removed
