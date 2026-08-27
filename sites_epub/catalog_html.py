"""Static ZenShelf catalog for gh-pages."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .catalog import load_catalog, load_sites
from .models import LinkedSite, Vendor

ROOT = Path(__file__).resolve().parents[1]
SHELF = Path(__file__).with_name("shelf.html")
TONES = {"codex": "codex", "claude": "claude", "cursor": "cursor"}


def _iso_from_mtime(path: Path) -> str:
    if not path.is_file():
        return ""
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _vendor_book(v: Vendor, *, dist: Path | None) -> dict:
    epub = (dist or ROOT / "dist") / f"{v.id}.epub"
    packed = v.packed_at or _iso_from_mtime(epub)
    updated = v.updated_at or packed
    declared = (v.cover or "").strip()
    jacket = ROOT / declared if declared else ROOT / "covers" / f"{v.id}.png"
    if not jacket.is_file() and declared:
        jacket = ROOT / "covers" / Path(declared).name
    if jacket.is_file() or declared:
        cover_kind = "image"
        cover = declared if declared.startswith("covers/") else f"covers/{jacket.name if jacket.is_file() else v.id + '.png'}"
        tone = ""
    else:
        cover_kind, cover, tone = "plate", f"icons/{v.id}.png", TONES.get(v.id, "codex")
    return {
        "id": v.id,
        "title": v.name,
        "author": v.author or v.name,
        "summary": v.summary
        or f"{v.name} 官方文档与博客，按站点导航打包为一部 EPUB。",
        "category": v.category or "docs",
        "categoryLabel": "厂商文档",
        "kind": "vendor",
        "coverKind": cover_kind,
        "cover": cover,
        "tone": tone,
        "updatedAt": updated,
        "packedAt": packed,
        "chapters": v.chapters,
        "href": f"{v.id}.epub",
        "docsUrl": v.docs_url,
        "blogUrl": v.blog_url or "",
    }


def _site_book(s: LinkedSite) -> dict:
    cover = s.cover
    if cover and not cover.startswith(("http://", "https://", "covers/")):
        cover = f"covers/{Path(cover).name}"
    return {
        "id": s.id,
        "title": s.name,
        "author": s.author,
        "summary": s.summary,
        "category": s.category or "handbook",
        "categoryLabel": "源码书",
        "kind": "site",
        "coverKind": "image",
        "cover": cover,
        "tone": "",
        "updatedAt": s.updated_at,
        "packedAt": s.updated_at,
        "chapters": 0,
        "href": s.url,
        "docsUrl": s.url,
        "blogUrl": "",
    }


def shelf_books(
    vendors: list[Vendor] | None = None,
    sites: list[LinkedSite] | None = None,
    *,
    dist: Path | None = None,
) -> list[dict]:
    vendors = vendors if vendors is not None else load_catalog()
    sites = sites if sites is not None else load_sites()
    return [_vendor_book(v, dist=dist) for v in vendors] + [_site_book(s) for s in sites]


def render_index(
    vendors: list[Vendor] | None = None,
    *,
    dist_dir: Path | None = None,
    sites: list[LinkedSite] | None = None,
) -> str:
    books = shelf_books(vendors, sites, dist=dist_dir)
    payload = json.dumps(books, ensure_ascii=False)
    template = SHELF.read_text(encoding="utf-8")
    return template.replace("__BOOKS_JSON__", payload)


def write_site(dest: Path, vendors: list[Vendor] | None = None, dist: Path | None = None) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    vendors = vendors if vendors is not None else load_catalog()
    sites = load_sites()
    (dest / "index.html").write_text(
        render_index(vendors, dist_dir=dist, sites=sites), encoding="utf-8"
    )
    (dest / "CNAME").write_text("epub.zenheart.site\n", encoding="utf-8")
    icons = dest / "icons"
    icons.mkdir(exist_ok=True)
    covers = dest / "covers"
    covers.mkdir(exist_ok=True)
    for v in vendors:
        src = ROOT / v.icon
        if src.is_file():
            data = src.read_bytes()
            (icons / f"{v.id}{src.suffix}").write_bytes(data)
            # Never publish SVG (or other XML) as .png — browsers show a broken icon.
            if data[:8] == b"\x89PNG\r\n\x1a\n" or data[:3] == b"\xff\xd8\xff":
                (icons / f"{v.id}.png").write_bytes(data)
        epub_src = (dist or ROOT / "dist") / f"{v.id}.epub"
        if epub_src.is_file():
            (dest / f"{v.id}.epub").write_bytes(epub_src.read_bytes())
    hashes = (dist or ROOT / "dist") / "pack-hashes.json"
    if hashes.is_file():
        shutil.copy2(hashes, dest / "pack-hashes.json")
    src_covers = ROOT / "covers"
    if src_covers.is_dir():
        for path in src_covers.iterdir():
            if path.is_file():
                shutil.copy2(path, covers / path.name)
    for s in sites:
        if s.cover:
            src = ROOT / s.cover if not Path(s.cover).is_absolute() else Path(s.cover)
            if not src.is_file():
                src = src_covers / Path(s.cover).name
            if src.is_file():
                shutil.copy2(src, covers / src.name)
