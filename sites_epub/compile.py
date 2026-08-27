"""Compile a vendor (docs nav + optional blog last) into one EPUB, incrementally."""

from __future__ import annotations

import json
from pathlib import Path

from .epub_pack import pack_epub
from .fingerprint import content_hash, load_fingerprints, save_fingerprints
from .http import fetch_bytes, fetch_text
from .images import guess_ext, local_name_for_url
from .models import CompileResult, IndexEntry, Vendor
from .page import DocPage, extract_page

ROOT = Path(__file__).resolve().parents[1]


def _looks_missing(text: str) -> bool:
    stripped = (text or "").strip()
    if not stripped or len(stripped) < 20:
        return True
    if stripped.lower() in {"not found", "not found."}:
        return True
    return False


def discover_entries(
    vendor: Vendor,
    *,
    docs_html: str | None = None,
    docs_llms: str | None = None,
    blog_html: str | None = None,
) -> list[IndexEntry]:
    docs: list[IndexEntry] = []
    if vendor.adapter == "codex":
        from .codex_nav import parse_nav_html

        if not docs_html:
            raise ValueError("codex adapter needs docs HTML")
        docs = parse_nav_html(docs_html)
    elif vendor.adapter == "claude":
        from .claude_nav import parse_llms_txt

        if not docs_llms:
            raise ValueError("claude adapter needs llms.txt")
        docs = parse_llms_txt(docs_llms)
    else:
        from .generic_nav import parse_docs_html, parse_llms_generic

        if docs_llms:
            docs = parse_llms_generic(docs_llms, vendor.docs_url)
        if not docs and docs_html:
            docs = parse_docs_html(docs_html, vendor.docs_url)
    blog: list[IndexEntry] = []
    if vendor.blog_url and blog_html:
        if "claude.com/blog" in vendor.blog_url:
            from .blog_listing import extract_blog_urls

            urls = extract_blog_urls(blog_html, base="https://claude.com")
            for url in urls:
                slug = url.rstrip("/").rsplit("/", 1)[-1]
                blog.append(
                    IndexEntry(
                        group="Blog",
                        title=slug.replace("-", " "),
                        md_url=url + ".md",
                        html_url=url,
                        route=f"blog/{slug}",
                        kind="blog",
                    )
                )
        else:
            from .generic_blog import parse_blog_html

            blog = parse_blog_html(blog_html, vendor.blog_url)
    return list(docs) + list(blog)


def compile_from_sources(
    entries: list[IndexEntry],
    sources: dict[str, str],
    output: Path,
    *,
    fingerprints: dict[str, str] | None = None,
    image_files: dict[str, Path] | None = None,
    title: str = "Docs",
    author: str = "",
    cover_image: Path | None = None,
    work_dir: Path | None = None,
) -> CompileResult:
    """Shipped incremental entry: skip routes whose content hash is unchanged."""
    prev = fingerprints or {}
    fetched: list[str] = []
    skipped: list[str] = []
    new_fp: dict[str, str] = {}
    pages: list[DocPage] = []
    for entry in entries:
        text = sources.get(entry.route)
        if text is None:
            continue
        digest = content_hash(text)
        new_fp[entry.route] = digest
        if prev.get(entry.route) == digest:
            skipped.append(entry.route)
        else:
            fetched.append(entry.route)
        kind = "html" if text.lstrip().lower().startswith("<!") else "md"
        page = None
        if entry.kind == "blog" and kind == "html":
            try:
                from .blog_article import extract_article
                from .page import DocPage as DP

                art = extract_article(text, url=entry.html_url)
                if art.body_text and len(art.body_text) >= 20:
                    page = DP(
                        title=art.title or entry.title,
                        body_html=art.body_html,
                        body_text=art.body_text,
                        image_urls=art.image_urls,
                        route=entry.route,
                        group=entry.group,
                        url=entry.html_url,
                    )
            except Exception:
                page = None
        if page is None:
            page = extract_page(
                text,
                route=entry.route,
                group=entry.group,
                url=entry.html_url,
                kind=kind,
            )
        page.group = entry.group
        page.route = entry.route
        pages.append(page)
    if not pages:
        raise ValueError("no pages to pack")
    imgs = image_files or {}
    if not imgs:
        # map any local sample by url if provided as Path values later
        imgs = {}
        url_to_rel = {}
    else:
        url_to_rel = {url: f"images/{path.name}" for url, path in imgs.items()}
    pack_epub(
        pages,
        output,
        images={f"images/{p.name}": p for p in imgs.values()},
        entries=entries,
        url_to_rel=url_to_rel,
        title=title,
        author=author,
        work_dir=work_dir,
        cover_image=cover_image,
    )
    return CompileResult(
        output=str(output),
        fetched_routes=fetched,
        skipped_routes=skipped,
        fingerprints=new_fp,
        chapters=len(pages),
    )


def fetch_source(entry: IndexEntry) -> str:
    try:
        text = fetch_text(entry.md_url)
    except Exception:
        text = ""
    if _looks_missing(text):
        text = fetch_text(entry.html_url)
    return text


def compile_vendor_live(
    vendor: Vendor,
    output: Path,
    *,
    root: Path | None = None,
    workers: int = 12,
) -> CompileResult:
    from concurrent.futures import ThreadPoolExecutor, as_completed

    base = Path(root) if root else ROOT
    vdir = base / "vendors" / vendor.id
    vdir.mkdir(parents=True, exist_ok=True)
    work = vdir / "work"
    work.mkdir(exist_ok=True)
    fp_path = vdir / "fingerprints.json"
    prev = load_fingerprints(fp_path)

    docs_html = fetch_text(vendor.docs_url)
    (work / "docs.html").write_text(docs_html, encoding="utf-8")
    docs_llms = ""
    for llms in (
        vendor.docs_url.rstrip("/") + "/llms.txt",
        vendor.docs_url.rsplit("/docs", 1)[0] + "/llms.txt" if "/docs" in vendor.docs_url else "",
        "https://code.claude.com/docs/llms.txt" if vendor.adapter == "claude" else "",
        "https://learn.chatgpt.com/llms.txt" if vendor.adapter == "codex" else "",
    ):
        if not llms:
            continue
        try:
            docs_llms = fetch_text(llms)
            if docs_llms and not _looks_missing(docs_llms):
                break
        except Exception:
            continue
    blog_html = ""
    if vendor.blog_url:
        try:
            blog_html = fetch_text(vendor.blog_url)
        except Exception:
            blog_html = ""
        if blog_html:
            (work / "blog.html").write_text(blog_html, encoding="utf-8")

    entries = discover_entries(
        vendor, docs_html=docs_html, docs_llms=docs_llms, blog_html=blog_html
    )
    if not entries:
        raise RuntimeError(f"no routes discovered for {vendor.id}")

    pages_dir = work / "pages"
    pages_dir.mkdir(exist_ok=True)
    sources: dict[str, str] = {}

    def load_one(entry: IndexEntry) -> tuple[str, str, bool]:
        dest = pages_dir / f"{entry.route}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        cached = ""
        if dest.is_file():
            cached = dest.read_text(encoding="utf-8", errors="replace")
        if cached and prev.get(entry.route) == content_hash(cached) and not _looks_missing(cached):
            return entry.route, cached, False
        text = fetch_source(entry)
        dest.write_text(text, encoding="utf-8")
        return entry.route, text, True

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futs = [pool.submit(load_one, e) for e in entries]
        for fut in as_completed(futs):
            route, text, _did = fut.result()
            sources[route] = text

    # images
    pages_preview: list[DocPage] = []
    # compile_from_sources extracts again; collect image urls after extract inside it
    # download images for extracted pages in a second pass via compile_from_sources then...
    # Simpler: extract here for images, then pack through compile_from_sources with image_files.

    from concurrent.futures import ThreadPoolExecutor as Pool2

    image_dir = work / "images"
    image_dir.mkdir(exist_ok=True)
    # Pre-extract to gather image URLs only for fetched/changed routes
    tmp_pages: list[DocPage] = []
    for entry in entries:
        text = sources.get(entry.route)
        if not text:
            continue
        kind = "html" if text.lstrip().lower().startswith("<!") else "md"
        try:
            if entry.kind == "blog" and kind == "html":
                from .blog_article import extract_article

                art = extract_article(text, url=entry.html_url)
                from .page import DocPage as DP

                tmp_pages.append(
                    DP(
                        title=art.title or entry.title,
                        body_html=art.body_html,
                        body_text=art.body_text,
                        image_urls=art.image_urls,
                        route=entry.route,
                        group=entry.group,
                        url=entry.html_url,
                    )
                )
            else:
                tmp_pages.append(
                    extract_page(
                        text,
                        route=entry.route,
                        group=entry.group,
                        url=entry.html_url,
                        kind=kind,
                    )
                )
        except Exception:
            continue
    urls: list[str] = []
    seen: set[str] = set()
    for p in tmp_pages:
        for u in p.image_urls:
            if u not in seen:
                seen.add(u)
                urls.append(u)

    image_files: dict[str, Path] = {}

    def one_img(url: str) -> tuple[str, Path | None]:
        name = local_name_for_url(url)
        cached = image_dir / name
        if cached.is_file() and cached.stat().st_size > 0:
            return url, cached
        try:
            data, ctype = fetch_bytes(url)
        except Exception:
            return url, None
        if not data:
            return url, None
        if len(data) > 800_000:
            return url, None
        if not Path(name).suffix:
            name = name + guess_ext(ctype, url)
        path = image_dir / name
        path.write_bytes(data)
        return url, path

    with Pool2(max_workers=min(12, workers)) as pool:
        futs = [pool.submit(one_img, u) for u in urls]
        for fut in as_completed(futs):
            url, path = fut.result()
            if path is not None:
                image_files[url] = path

    icon = base / vendor.icon
    if not icon.is_file():
        icon = vdir / "icon.png"
    result = compile_from_sources(
        entries,
        sources,
        output,
        fingerprints=prev,
        image_files=image_files,
        title=vendor.name,
        author=vendor.author,
        cover_image=icon if icon.is_file() else None,
        work_dir=work / "epub-build",
    )
    save_fingerprints(fp_path, result.fingerprints)
    stats = {
        "vendor": vendor.id,
        "chapters": result.chapters,
        "fetched": len(result.fetched_routes),
        "skipped": len(result.skipped_routes),
        "output": result.output,
    }
    (work / "compile-stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return result
