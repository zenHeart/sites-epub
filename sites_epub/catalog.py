"""Vendor catalog: JSON on disk, no secrets."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import LinkedSite, Vendor

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def vendor_to_dict(v: Vendor) -> dict:
    return {
        "id": v.id,
        "name": v.name,
        "docs_url": v.docs_url,
        "blog_url": v.blog_url,
        "icon": v.icon,
        "author": v.author,
        "adapter": v.adapter,
        "updated_at": v.updated_at,
        "packed_at": v.packed_at,
        "summary": v.summary,
        "category": v.category,
        "chapters": v.chapters,
        "cover": v.cover,
    }


def _vendor_from_dict(item: dict) -> Vendor:
    return Vendor(
        id=item["id"],
        name=item["name"],
        docs_url=item["docs_url"],
        blog_url=item.get("blog_url"),
        icon=item.get("icon") or f"vendors/{item['id']}/icon.png",
        author=item.get("author") or "",
        adapter=item.get("adapter") or "generic",
        updated_at=item.get("updated_at") or "",
        packed_at=item.get("packed_at") or "",
        summary=item.get("summary") or "",
        category=item.get("category") or "docs",
        chapters=int(item.get("chapters") or 0),
        cover=item.get("cover") or "",
    )


def load_raw(path: Path | None = None) -> dict:
    p = Path(path) if path else CATALOG_PATH
    if not p.is_file():
        return {"vendors": [], "sites": []}
    raw = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(raw, list):
        return {"vendors": raw, "sites": []}
    return {
        "vendors": raw.get("vendors", []),
        "sites": raw.get("sites", []),
    }


def load_catalog(path: Path | None = None) -> list[Vendor]:
    return [_vendor_from_dict(item) for item in load_raw(path)["vendors"]]


def load_sites(path: Path | None = None) -> list[LinkedSite]:
    out: list[LinkedSite] = []
    for item in load_raw(path)["sites"]:
        out.append(
            LinkedSite(
                id=item["id"],
                name=item["name"],
                url=item["url"],
                author=item.get("author") or "",
                summary=item.get("summary") or "",
                cover=item.get("cover") or "",
                category=item.get("category") or "handbook",
                updated_at=item.get("updated_at") or "",
            )
        )
    return out


def save_catalog(vendors: list[Vendor], path: Path | None = None) -> None:
    p = Path(path) if path else CATALOG_PATH
    raw = load_raw(p) if p.is_file() else {"vendors": [], "sites": []}
    payload = {
        "vendors": [vendor_to_dict(v) for v in vendors],
        "sites": raw.get("sites") or [],
    }
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def stamp_vendor(vendor_id: str, path: Path | None = None, **fields: object) -> Vendor | None:
    """Merge timestamp/meta fields onto one catalog vendor. Returns the vendor or None."""
    p = Path(path) if path else CATALOG_PATH
    vendors = load_catalog(p)
    found: Vendor | None = None
    out: list[Vendor] = []
    for v in vendors:
        if v.id == vendor_id:
            data = vendor_to_dict(v)
            for key, value in fields.items():
                if key in data and value is not None:
                    data[key] = value
            v = _vendor_from_dict(data)
            found = v
        out.append(v)
    if found is None:
        return None
    save_catalog(out, p)
    return found


def vendor_dir(vendor_id: str, root: Path | None = None) -> Path:
    base = Path(root) if root else ROOT
    return base / "vendors" / vendor_id


def upsert_vendor(vendor: Vendor, path: Path | None = None) -> list[Vendor]:
    vendors = load_catalog(path)
    by_id = {v.id: v for v in vendors}
    if vendor.id in by_id:
        old = by_id[vendor.id]
        if not vendor.updated_at:
            vendor.updated_at = old.updated_at
        if not vendor.packed_at:
            vendor.packed_at = old.packed_at
        if not vendor.summary:
            vendor.summary = old.summary
        if not vendor.chapters:
            vendor.chapters = old.chapters
        if not vendor.cover:
            vendor.cover = old.cover
        if vendor.category == "docs" and old.category:
            vendor.category = old.category
    by_id[vendor.id] = vendor
    ordered = list(by_id.values())
    save_catalog(ordered, path)
    return ordered


def guess_vendor_id(docs_url: str, name: str | None = None) -> str:
    if name:
        slug = re_slug(name)
        if slug:
            return slug
    from urllib.parse import urlparse

    host = urlparse(docs_url).netloc.lower()
    host = host.removeprefix("www.").removeprefix("docs.")
    part = host.split(".")[0]
    if "claude" in host or "anthropic" in host:
        return "claude"
    if "chatgpt" in host or "openai" in host or "codex" in host:
        return "codex"
    if "cursor" in host:
        return "cursor"
    return re_slug(part) or "site"


def re_slug(text: str) -> str:
    import re

    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:40]


def guess_adapter(docs_url: str) -> str:
    host = docs_url.lower()
    if "learn.chatgpt.com" in host:
        return "codex"
    if "code.claude.com" in host or "claude.com" in host:
        return "claude"
    if "docs.x.ai" in host or "x.ai" in host:
        return "xai"
    return "generic"
