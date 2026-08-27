"""Pack docs pages into an EPUB3 whose TOC parents follow index groups / nested routes."""

from __future__ import annotations

import html as html_lib
import os
import re
import shutil
import subprocess
import tempfile
import warnings
import zipfile
from collections import OrderedDict
from pathlib import Path, PurePosixPath

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

from .images import repair_epub_images, rewrite_body_images
from .models import IndexEntry, unique_group_label
from .page import DocPage, sanitize_body_html

HTTP_URL_RE = re.compile(r"^https?://", re.I)
NAV_NAME_HINTS = ("nav.xhtml", "toc.xhtml")
SKIP_SOURCE_REPAIR = ("title_page.xhtml",)

CSS = """
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.55; color: #1a1a1a; }
h1, h2, h3, h4 { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.3; }
img { max-width: 100%; height: auto; }
h2.page-title { margin: 1.15em 0 0.45em; }
h2.page-title a.source-title {
  color: #0f4c81;
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.16em;
}
h2.page-title a.source-title:visited { color: #0f4c81; }
.source-mark { font-size: 0.62em; margin-left: 0.28em; font-weight: 400; vertical-align: super; }
pre, pre code { font-family: Menlo, Consolas, "SF Mono", monospace; font-size: 0.85em; }
pre { background: #f5f5f5; padding: 0.8em 1em; overflow-x: auto; white-space: pre-wrap; word-break: break-word; border-radius: 4px; }
code { font-family: Menlo, Consolas, monospace; font-size: 0.9em; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; table-layout: auto; }
th, td { border: 1px solid #ccc; padding: 0.45em 0.65em; word-wrap: break-word; overflow-wrap: anywhere; vertical-align: top; }
th { background: #f0f0f0; font-weight: 600; }
.mdx-tabs { margin: 1em 0; }
.mdx-tab { border: 1px solid #ddd; border-radius: 6px; padding: 0.75em 1em; margin: 0.6em 0; background: #fafafa; }
.mdx-tab-title { font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0 0 0.4em; }
.mdx-callout { border-left: 4px solid #888; padding: 0.6em 1em; margin: 1em 0; background: #f7f7f7; }
.mdx-info { border-left-color: #3b82f6; background: #eff6ff; }
.mdx-tip { border-left-color: #16a34a; background: #f0fdf4; }
.mdx-warning { border-left-color: #d97706; background: #fffbeb; }
.mdx-note { border-left-color: #6b7280; background: #f9fafb; }
.mdx-callout-label { font-weight: 600; margin: 0 0 0.35em; font-size: 0.9em; }
.mdx-accordion { border: 1px solid #ddd; border-radius: 6px; padding: 0.75em 1em; margin: 0.8em 0; }
.mdx-accordion-title { font-weight: 600; margin: 0 0 0.4em; }
.mdx-steps { margin: 1em 0 1em 1.2em; }
.mdx-step-title { font-weight: 600; }
.mdx-codegroup { margin: 1em 0; }
.mdx-codepanel { border: 1px solid #ddd; border-radius: 6px; padding: 0.75em 1em; margin: 0.6em 0; background: #fafafa; }
.mdx-codepanel-title { font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0 0 0.4em; }
.mdx-live-widget { border: 1px solid #c5d0dc; border-left: 4px solid #0f4c81; padding: 0.75em 1em; margin: 1em 0; background: #f4f7fb; }
.mdx-live-widget-label { font-weight: 600; margin: 0 0 0.35em; font-size: 0.9em; }
.mdx-file-card { border: 1px solid #ddd; border-radius: 6px; padding: 0.75em 1em; margin: 0.8em 0; background: #fafafa; }
.mdx-file-card h3 { margin: 0 0 0.35em; font-size: 1.05em; }
.mdx-when { font-size: 0.92em; color: #444; }
blockquote { border-left: 3px solid #ccc; margin: 1em 0; padding: 0.15em 0.9em; color: #444; }
kbd { font-family: Menlo, Consolas, monospace; font-size: 0.85em; border: 1px solid #ccc; border-radius: 3px; padding: 0.05em 0.35em; background: #f6f6f6; }
a { color: #0f4c81; }
figure.mdx-frame, figure.mdx-diagram { margin: 1.2em 0; }
figcaption { font-size: 0.9em; color: #555; margin-top: 0.4em; }
.mdx-card { border: 1px solid #ddd; border-radius: 10px; padding: 0.9em 1.1em; margin: 0.8em 0; background: #fafafa; }
.mdx-card > :first-child { margin-top: 0; }
.mdx-card > :last-child { margin-bottom: 0; }
.mdx-card-title { font-weight: 600; margin: 0 0 0.35em; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
.mdx-card-group { margin: 1em 0; }
.mdx-mermaid { background: #f4f4f4; }
.mdx-danger, .mdx-callout.mdx-danger { border-left-color: #dc2626; background: #fef2f2; }
"""


def _esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def _yaml_str(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def http_url(url: str | None) -> str | None:
    if not url:
        return None
    text = url.strip()
    if HTTP_URL_RE.match(text):
        return text
    return None


def _norm_url(url: str | None) -> str:
    return (url or "").strip().rstrip("/")


def _source_title_html(title: str, url: str | None) -> str:
    text = _esc(title)
    src = http_url(url)
    if not src:
        return f'<h2 class="page-title">{text}</h2>'
    href = _esc(src)
    return (
        f'<h2 class="page-title">'
        f'<a class="source-title" href="{href}" rel="external">{text}'
        f'<span class="source-mark" aria-hidden="true">↗</span></a></h2>'
    )


def demote_headings(body_html: str) -> str:
    """Shift h1–h4 down two levels so packer h1=group, h2=page title."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(body_html, "lxml")
    root = soup.body if soup.body else soup
    mapping = {"h1": "h3", "h2": "h4", "h3": "h5", "h4": "h6"}
    for tag in list(root.find_all(list(mapping))):
        tag.name = mapping[tag.name]
    if hasattr(root, "decode_contents"):
        return root.decode_contents()
    return str(root)


def grouped_html(
    pages: list[DocPage],
    entries: list[IndexEntry] | None = None,
    url_to_rel: dict[str, str] | None = None,
) -> str:
    """Build one HTML book: h1 = section group, h2 = page title."""
    url_to_rel = url_to_rel or {}
    entry_by_route = {e.route: e for e in (entries or [])}
    used: dict[str, str] = {}
    groups: OrderedDict[str, list[DocPage]] = OrderedDict()
    last_name: str | None = None
    last_label: str | None = None
    for page in pages:
        entry = entry_by_route.get(page.route)
        group = page.group or (entry.group if entry else "Docs")
        if group == last_name and last_label is not None:
            label = last_label
        else:
            label = unique_group_label(group, page.route or "page", used)
            last_name = group
            last_label = label
        page.group = label
        groups.setdefault(label, []).append(page)

    parts = [
        "<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">",
        "<title>ChatGPT Codex Docs</title></head><body>",
    ]
    for label, grouped in groups.items():
        parts.append(f"<div class=\"doc-group\"><h1>{_esc(label)}</h1>")
        for page in grouped:
            rewritten = rewrite_body_images(
                page.body_html,
                url_to_rel,
                base=page.url or "https://learn.chatgpt.com",
                available=set(url_to_rel.values()),
            )
            rewritten = sanitize_body_html(rewritten, page_url=page.url)
            rewritten = demote_headings(rewritten)
            page_id = _esc(page.route or page.title)
            source = http_url(page.url)
            attrs = [f'class="doc-page"', f'id="{page_id}"']
            if source:
                attrs.append(f'data-source="{_esc(source)}"')
            parts.append(f"<div {' '.join(attrs)}>")
            parts.append(_source_title_html(page.title, page.url))
            parts.append(rewritten)
            parts.append("</div>")
        parts.append("</div>")
    parts.append("</body></html>")
    return "\n".join(parts)


def pack_epub(
    pages: list[DocPage],
    output: Path,
    *,
    images: dict[str, Path] | None = None,
    entries: list[IndexEntry] | None = None,
    url_to_rel: dict[str, str] | None = None,
    title: str = "ChatGPT Codex Docs",
    author: str = "OpenAI",
    lang: str = "en",
    work_dir: Path | None = None,
    cover_image: Path | None = None,
) -> Path:
    if not pages:
        raise ValueError("no pages to pack")
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc is required to build EPUB3")

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    own_tmp: tempfile.TemporaryDirectory[str] | None = None
    if work_dir is None:
        own_tmp = tempfile.TemporaryDirectory(prefix="chatgpt-learn-docs-epub-")
        root = Path(own_tmp.name)
    else:
        root = Path(work_dir)
        root.mkdir(parents=True, exist_ok=True)

    try:
        img_dir = root / "images"
        img_dir.mkdir(exist_ok=True)
        if images:
            for rel, src in images.items():
                dest = root / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                src = Path(src)
                if src.resolve() != dest.resolve():
                    shutil.copy2(src, dest)

        html_path = root / "book.html"
        html_path.write_text(
            grouped_html(pages, entries=entries, url_to_rel=url_to_rel or {}),
            encoding="utf-8",
        )
        css_path = root / "book.css"
        css_path.write_text(CSS, encoding="utf-8")
        meta_path = root / "metadata.yaml"
        meta_path.write_text(
            "---\n"
            f"title: {_yaml_str(title)}\n"
            f"author: {_yaml_str(author)}\n"
            f"lang: {lang}\n"
            "---\n",
            encoding="utf-8",
        )
        cmd = [
            pandoc,
            str(html_path),
            "-f",
            "html",
            "-t",
            "epub3",
            "-o",
            str(output),
            "--toc",
            "--toc-depth=2",
            "--split-level=1",
            f"--metadata-file={meta_path}",
            f"--css={css_path}",
            f"--resource-path={root}",
        ]
        if cover_image is not None and Path(cover_image).is_file():
            cmd.append(f"--epub-cover-image={Path(cover_image)}")
        proc = subprocess.run(cmd, text=True, capture_output=True, check=False)
        if proc.returncode != 0 or not output.is_file() or output.stat().st_size == 0:
            raise RuntimeError(
                f"pandoc failed ({proc.returncode}): {(proc.stderr or proc.stdout).strip()}"
            )
        repair_epub_images(output)
        repair_epub_source_links(output)
        return output
    finally:
        if own_tmp is not None:
            own_tmp.cleanup()


def _is_nav_doc(name: str) -> bool:
    lower = name.lower()
    return any(hint in lower for hint in NAV_NAME_HINTS)


def _toc_href(nav_name: str, chapter_name: str, fragment: str) -> str:
    start = str(PurePosixPath(nav_name).parent)
    rel = os.path.relpath(chapter_name, start=start).replace("\\", "/")
    if fragment:
        return f"{rel}#{fragment}"
    return rel


def _ensure_heading_source_link(soup: BeautifulSoup, page, source: str) -> bool:
    h2 = page.find("h2")
    if h2 is None:
        return False
    changed = False
    classes = list(h2.get("class") or [])
    if "page-title" not in classes:
        classes.append("page-title")
        h2["class"] = classes
        changed = True
    existing = h2.find("a", href=True)
    if existing is not None and _norm_url(existing.get("href")) == _norm_url(source):
        link_classes = list(existing.get("class") or [])
        if "source-title" not in link_classes:
            link_classes.append("source-title")
            existing["class"] = link_classes
            changed = True
        rel = existing.get("rel")
        if rel != "external" and rel != ["external"] and "external" not in (rel or []):
            existing["rel"] = "external"
            changed = True
        return changed
    title = h2.get_text(" ", strip=True).replace("↗", "").strip() or source
    h2.clear()
    anchor = soup.new_tag("a", href=source, **{"class": "source-title", "rel": "external"})
    anchor.append(title)
    mark = soup.new_tag("span", **{"class": "source-mark", "aria-hidden": "true"})
    mark.string = "↗"
    anchor.append(mark)
    h2.append(anchor)
    return True


def repair_epub_source_links(epub_path: Path) -> int:
    """Keep page titles as original-URL links; keep nav/TOC pointing inside the book."""
    epub_path = Path(epub_path)
    with zipfile.ZipFile(epub_path, "r") as zf:
        names = zf.namelist()
        contents = {name: zf.read(name) for name in names}
        infos = {info.filename: info for info in zf.infolist()}

    soups: dict[str, BeautifulSoup] = {}
    changed_names: set[str] = set()
    source_index: dict[str, tuple[str, str]] = {}
    for name in names:
        lower = name.lower()
        if not lower.endswith((".xhtml", ".html")):
            continue
        if any(skip in lower for skip in SKIP_SOURCE_REPAIR):
            continue
        soup = BeautifulSoup(contents[name].decode("utf-8", errors="replace"), "lxml")
        soups[name] = soup
        if _is_nav_doc(name):
            continue
        for page in soup.select(".doc-page"):
            source = http_url(page.get("data-source"))
            if not source:
                continue
            fragment = (page.get("id") or "").strip()
            h2 = page.find("h2")
            if h2 and (h2.get("id") or "").strip():
                fragment = (h2.get("id") or "").strip()
            source_index[_norm_url(source)] = (name, fragment)
            if _ensure_heading_source_link(soup, page, source):
                changed_names.add(name)

    for name, soup in soups.items():
        if not _is_nav_doc(name):
            continue
        nav_changed = False
        for mark in soup.select("span.source-mark"):
            mark.decompose()
            nav_changed = True
        for anchor in soup.find_all("a", href=True):
            href = (anchor.get("href") or "").strip()
            key = _norm_url(href)
            if key not in source_index:
                continue
            chapter, fragment = source_index[key]
            anchor["href"] = _toc_href(name, chapter, fragment)
            nav_changed = True
        if nav_changed:
            changed_names.add(name)

    if not changed_names:
        return 0

    for name in changed_names:
        contents[name] = str(soups[name]).encode("utf-8")
    tmp = epub_path.with_suffix(".epub.tmp")
    with zipfile.ZipFile(tmp, "w") as out:
        for name in names:
            info = infos[name]
            if name == "mimetype":
                out.writestr(info, contents[name], compress_type=zipfile.ZIP_STORED)
            else:
                out.writestr(info, contents[name])
    tmp.replace(epub_path)
    return len(changed_names)
