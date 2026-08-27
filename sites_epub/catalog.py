"""Vendor catalog: JSON on disk, no secrets."""

from __future__ import annotations

import json
from pathlib import Path

from .models import Vendor

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"


def load_catalog(path: Path | None = None) -> list[Vendor]:
    p = Path(path) if path else CATALOG_PATH
    if not p.is_file():
        return []
    raw = json.loads(p.read_text(encoding="utf-8"))
    items = raw.get("vendors", raw) if isinstance(raw, dict) else raw
    out: list[Vendor] = []
    for item in items:
        out.append(
            Vendor(
                id=item["id"],
                name=item["name"],
                docs_url=item["docs_url"],
                blog_url=item.get("blog_url"),
                icon=item.get("icon") or f"vendors/{item['id']}/icon.png",
                author=item.get("author") or "",
                adapter=item.get("adapter") or "generic",
            )
        )
    return out


def save_catalog(vendors: list[Vendor], path: Path | None = None) -> None:
    p = Path(path) if path else CATALOG_PATH
    payload = {
        "vendors": [
            {
                "id": v.id,
                "name": v.name,
                "docs_url": v.docs_url,
                "blog_url": v.blog_url,
                "icon": v.icon,
                "author": v.author,
                "adapter": v.adapter,
            }
            for v in vendors
        ]
    }
    p.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def vendor_dir(vendor_id: str, root: Path | None = None) -> Path:
    base = Path(root) if root else ROOT
    return base / "vendors" / vendor_id


def upsert_vendor(vendor: Vendor, path: Path | None = None) -> list[Vendor]:
    vendors = load_catalog(path)
    by_id = {v.id: v for v in vendors}
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
    return "generic"
