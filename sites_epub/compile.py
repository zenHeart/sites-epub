"""Compile a vendor (docs nav + optional blog last) into one EPUB, incrementally."""

from __future__ import annotations

import json
from pathlib import Path

from urllib.parse import urljoin, urlparse

from .epub_pack import pack_epub
from .fingerprint import content_hash, load_fingerprints, save_fingerprints
from .http import fetch_bytes, fetch_text
from .images import collect_source_image_urls, guess_ext, local_name_for_url
from .models import CompileResult, FetchResult, IndexEntry, Vendor
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


def _entry_dict(e: IndexEntry) -> dict:
    return {
        "group": e.group,
        "title": e.title,
        "md_url": e.md_url,
        "html_url": e.html_url,
        "route": e.route,
        "kind": e.kind,
    }


def _entry_from_dict(d: dict) -> IndexEntry:
    return IndexEntry(
        group=d["group"],
        title=d["title"],
        md_url=d["md_url"],
        html_url=d["html_url"],
        route=d["route"],
        kind=d.get("kind") or "doc",
    )


def corpus_dir(vendor: Vendor, root: Path | None = None) -> Path:
    base = Path(root) if root else ROOT
    return base / "vendors" / vendor.id / "corpus"


def _origin(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"


def ensure_vendor_icon(vendor: Vendor, vdir: Path, docs_html: str = "") -> None:
    dest = vdir / "icon.png"
    if dest.is_file() and dest.stat().st_size > 200:
        return
    candidates: list[str] = []
    if docs_html:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(docs_html, "lxml")
        for tag in soup.find_all("link"):
            rel = " ".join(tag.get("rel") or []).lower()
            href = tag.get("href") or ""
            if href and "icon" in rel and not href.endswith(".ico"):
                candidates.append(urljoin(vendor.docs_url, href))
    origin = _origin(vendor.docs_url)
    host = urlparse(vendor.docs_url).netloc
    candidates.extend(
        [
            f"{origin}/docs-static/icon-192x192.png",
            f"{origin}/apple-touch-icon.png",
            f"https://www.google.com/s2/favicons?domain={host}&sz=128",
        ]
    )
    for url in candidates:
        try:
            data, _ctype = fetch_bytes(url)
        except Exception:
            continue
        if not data or len(data) < 200 or data[:32].lstrip().lower().startswith(b"<!do"):
            continue
        dest.write_bytes(data)
        return


def fetch_vendor(
    vendor: Vendor,
    *,
    root: Path | None = None,
    workers: int = 12,
) -> FetchResult:
    """Local incremental crawl. Writes corpus/ (pages, images, routes). No EPUB."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    base = Path(root) if root else ROOT
    vdir = base / "vendors" / vendor.id
    vdir.mkdir(parents=True, exist_ok=True)
    corpus = corpus_dir(vendor, base)
    pages_dir = corpus / "pages"
    image_dir = corpus / "images"
    pages_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(exist_ok=True)
    fp_path = vdir / "fingerprints.json"
    prev = load_fingerprints(fp_path)

    docs_html = fetch_text(vendor.docs_url)
    (corpus / "docs.html").write_text(docs_html, encoding="utf-8")
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
                (corpus / "llms.txt").write_text(docs_llms, encoding="utf-8")
                break
        except Exception:
            continue
    blog_html = ""
    if vendor.blog_url:
        try:
            blog_html = fetch_text(vendor.blog_url)
            if "claude.com/blog" in vendor.blog_url:
                from .blog_listing import extract_pagination, listing_page_url

                pag = extract_pagination(blog_html)
                parts = [blog_html]
                if pag.collection_id and pag.total and pag.total > 1:
                    for page in range(2, min(pag.total, 60) + 1):
                        page_url = listing_page_url(
                            page, pag.collection_id, listing=vendor.blog_url.split("?")[0]
                        )
                        parts.append(fetch_text(page_url))
                blog_html = "\n".join(parts)
            try:
                sitemap = fetch_text(_origin(vendor.blog_url) + "/sitemap.xml")
                if sitemap and "<loc>" in sitemap:
                    blog_html = (blog_html or "") + "\n" + sitemap
            except Exception:
                pass
        except Exception:
            blog_html = blog_html or ""
        if blog_html:
            (corpus / "blog.html").write_text(blog_html, encoding="utf-8")
    ensure_vendor_icon(vendor, vdir, docs_html)

    entries = discover_entries(
        vendor, docs_html=docs_html, docs_llms=docs_llms, blog_html=blog_html
    )
    if not entries:
        raise RuntimeError(f"no routes discovered for {vendor.id}")
    (corpus / "routes.json").write_text(
        json.dumps([_entry_dict(e) for e in entries], indent=2), encoding="utf-8"
    )

    fetched: list[str] = []
    skipped: list[str] = []
    sources: dict[str, str] = {}

    def load_one(entry: IndexEntry) -> tuple[str, str, bool]:
        dest = pages_dir / f"{entry.route}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        cached = dest.read_text(encoding="utf-8", errors="replace") if dest.is_file() else ""
        if cached and prev.get(entry.route) == content_hash(cached) and not _looks_missing(cached):
            return entry.route, cached, False
        text = fetch_source(entry)
        dest.write_text(text, encoding="utf-8")
        return entry.route, text, True

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futs = [pool.submit(load_one, e) for e in entries]
        for fut in as_completed(futs):
            route, text, did_fetch = fut.result()
            sources[route] = text
            (fetched if did_fetch else skipped).append(route)

    new_fp = {route: content_hash(text) for route, text in sources.items()}
    save_fingerprints(fp_path, new_fp)

    # Images for every route (including skipped pages) so incremental fetch
    # still backfills missing corpus/images.
    urls: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        text = sources.get(entry.route) or ""
        kind = "html" if text.lstrip().lower().startswith("<!") else "md"
        img_list: list[str] = []
        try:
            if entry.kind == "blog" and kind == "html":
                from .blog_article import extract_article

                img_list = extract_article(text, url=entry.html_url).image_urls
            else:
                img_list = extract_page(
                    text, route=entry.route, group=entry.group, url=entry.html_url, kind=kind
                ).image_urls
        except Exception:
            img_list = []
        if not img_list:
            img_list = collect_source_image_urls(text, entry.html_url)
        for u in img_list:
            if u not in seen:
                seen.add(u)
                urls.append(u)

    image_map: dict[str, str] = {}
    map_path = corpus / "image-map.json"
    if map_path.is_file():
        image_map = json.loads(map_path.read_text(encoding="utf-8"))

    def one_img(url: str) -> tuple[str, str | None]:
        name = local_name_for_url(url)
        mapped = image_map.get(url)
        cached = image_dir / mapped if mapped else image_dir / name
        if cached.is_file() and cached.stat().st_size > 0:
            return url, cached.name
        try:
            data, ctype = fetch_bytes(url)
        except Exception:
            return url, None
        if not data or len(data) > 1_500_000:
            return url, None
        if not Path(name).suffix:
            name = name + guess_ext(ctype, url)
        (image_dir / name).write_bytes(data)
        return url, name

    with ThreadPoolExecutor(max_workers=min(12, workers)) as pool:
        futs = [pool.submit(one_img, u) for u in urls]
        for fut in as_completed(futs):
            url, name = fut.result()
            if name:
                image_map[url] = name
    map_path.write_text(json.dumps(image_map, indent=2), encoding="utf-8")

    return FetchResult(
        fetched_routes=sorted(fetched),
        skipped_routes=sorted(skipped),
        fingerprints=new_fp,
        entries=len(entries),
    )


def pack_vendor(
    vendor: Vendor,
    output: Path,
    *,
    root: Path | None = None,
) -> CompileResult:
    """Offline pack from committed corpus. No network."""
    base = Path(root) if root else ROOT
    corpus = corpus_dir(vendor, base)
    routes_path = corpus / "routes.json"
    if not routes_path.is_file():
        raise FileNotFoundError(f"missing corpus for {vendor.id}: {routes_path}")
    entries = [_entry_from_dict(d) for d in json.loads(routes_path.read_text(encoding="utf-8"))]
    pages_dir = corpus / "pages"
    sources: dict[str, str] = {}
    for e in entries:
        p = pages_dir / f"{e.route}.md"
        if p.is_file():
            sources[e.route] = p.read_text(encoding="utf-8", errors="replace")
    image_files: dict[str, Path] = {}
    map_path = corpus / "image-map.json"
    image_dir = corpus / "images"
    if map_path.is_file():
        mapping = json.loads(map_path.read_text(encoding="utf-8"))
        for url, name in mapping.items():
            path = image_dir / name
            if path.is_file():
                image_files[url] = path
    icon = base / vendor.icon
    if not icon.is_file():
        icon = base / "vendors" / vendor.id / "icon.png"
    vdir = base / "vendors" / vendor.id
    prev = load_fingerprints(vdir / "fingerprints.json")
    result = compile_from_sources(
        entries,
        sources,
        output,
        fingerprints=prev,
        image_files=image_files,
        title=vendor.name,
        author=vendor.author,
        cover_image=icon if icon.is_file() else None,
        work_dir=vdir / "work" / "epub-build",
    )
    from .walk import walk_chapters

    report = walk_chapters(output)
    broken = [
        c
        for c in report.chapters
        if any(d.startswith(("broken_img", "remote_img", "empty_img")) for d in c.defects)
    ]
    if broken:
        sample = broken[0].defects[:3]
        raise RuntimeError(f"broken images in {vendor.id} epub: {sample}")
    return result


def compile_vendor_live(
    vendor: Vendor,
    output: Path,
    *,
    root: Path | None = None,
    workers: int = 12,
) -> CompileResult:
    """Fetch locally then pack. GitHub Actions should call pack_vendor only."""
    fetch_vendor(vendor, root=root, workers=workers)
    return pack_vendor(vendor, output, root=root)
