"""Pack docs pages into an EPUB3 whose TOC parents follow index groups / nested routes."""

from __future__ import annotations

import html as html_lib
import shutil
import subprocess
import tempfile
from collections import OrderedDict
from pathlib import Path

from .images import rewrite_body_images
from .models import IndexEntry, unique_group_label
from .page import DocPage, sanitize_body_html

CSS = """
body { font-family: Georgia, "Times New Roman", serif; line-height: 1.55; color: #1a1a1a; }
h1, h2, h3, h4 { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.3; }
img { max-width: 100%; height: auto; }
.page-meta { color: #555; font-size: 0.85em; }
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
"""


def _esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def _yaml_str(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


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
            )
            rewritten = sanitize_body_html(rewritten)
            rewritten = demote_headings(rewritten)
            parts.append(f"<div class=\"doc-page\" id=\"{_esc(page.route or page.title)}\">")
            parts.append(f"<h2>{_esc(page.title)}</h2>")
            if page.url:
                parts.append(f'<p class="page-meta">{_esc(page.url)}</p>')
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
        return output
    finally:
        if own_tmp is not None:
            own_tmp.cleanup()
