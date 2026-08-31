"""Skip EPUB pack when corpus + packer inputs are unchanged."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from pathlib import Path

from .catalog import now_iso, stamp_vendor
from .compile import pack_vendor
from .models import Vendor

HASHES_NAME = "pack-hashes.json"
PACKER_FILES = (
    "sites_epub/epub_pack.py",
    "sites_epub/compile.py",
    "sites_epub/page.py",
    "sites_epub/images.py",
    "sites_epub/codex_nav.py",
    "sites_epub/claude_nav.py",
    "sites_epub/generic_nav.py",
    "sites_epub/generic_blog.py",
    "sites_epub/blog_listing.py",
    "sites_epub/xai_nav.py",
    "sites_epub/mdx.py",
    "sites_epub/blog_article.py",
    "sites_epub/models.py",
)


def _digest_file(path: Path) -> bytes:
    return hashlib.sha256(path.read_bytes()).digest()


def vendor_pack_key(vendor: Vendor, root: Path) -> str:
    """Fingerprint of inputs that change the packed EPUB bytes."""
    h = hashlib.sha256()
    h.update(b"pack-key-v1\n")
    h.update(vendor.id.encode())
    h.update(b"\0")
    h.update((vendor.name or "").encode())
    h.update(b"\0")
    h.update((vendor.author or "").encode())
    for rel in PACKER_FILES:
        path = root / rel
        h.update(rel.encode())
        h.update(b"\0")
        if path.is_file():
            h.update(_digest_file(path))
    for extra in (
        root / vendor.icon,
        root / "vendors" / vendor.id / "icon.png",
        root / "covers" / f"{vendor.id}.png",
    ):
        if extra.is_file():
            h.update(extra.relative_to(root).as_posix().encode())
            h.update(_digest_file(extra))
    corpus = root / "vendors" / vendor.id / "corpus"
    if corpus.is_dir():
        for path in sorted(p for p in corpus.rglob("*") if p.is_file()):
            h.update(path.relative_to(corpus).as_posix().encode())
            h.update(_digest_file(path))
    return h.hexdigest()


def load_pack_hashes(path: Path) -> dict:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def save_pack_hashes(path: Path, hashes: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(hashes, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def force_from_env() -> bool:
    return os.environ.get("SITESEPUB_FORCE", "").strip().lower() in {"1", "true", "yes"}


def prev_site_from_env() -> Path | None:
    raw = os.environ.get("SITESEPUB_PREV_SITE", "").strip()
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_dir() else None


def run_pack(
    vendors: list[Vendor],
    dest: Path,
    *,
    root: Path,
    prev_site: Path | None = None,
    force: bool = False,
    force_ids: set[str] | None = None,
    stamp: bool = True,
) -> list[dict]:
    """Pack only vendors whose inputs changed. Reuse previous EPUBs for the rest."""
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    prev = Path(prev_site) if prev_site else None
    hashes = load_pack_hashes(dest / HASHES_NAME)
    if prev is not None:
        hashes = {**load_pack_hashes(prev / HASHES_NAME), **hashes}
    results: list[dict] = []
    for vendor in vendors:
        key = vendor_pack_key(vendor, root)
        out = dest / f"{vendor.id}.epub"
        prev_epub = (prev / f"{vendor.id}.epub") if prev is not None else None
        must = force or (force_ids is not None and vendor.id in force_ids)
        reused = (
            not must
            and hashes.get(vendor.id, {}).get("sha256") == key
            and (out.is_file() or (prev_epub is not None and prev_epub.is_file()))
        )
        if reused:
            if not out.is_file() and prev_epub is not None:
                shutil.copy2(prev_epub, out)
            record = hashes.get(vendor.id) or {}
            results.append(
                {
                    "ok": True,
                    "vendor": vendor.id,
                    "action": "skipped",
                    "output": str(out),
                    "chapters": record.get("chapters"),
                    "packed_at": record.get("packed_at") or "",
                    "sha256": key,
                }
            )
            continue
        try:
            result = pack_vendor(vendor, out, root=root)
        except Exception as exc:  # noqa: BLE001
            results.append(
                {
                    "ok": False,
                    "vendor": vendor.id,
                    "action": "error",
                    "error": str(exc),
                }
            )
            continue
        packed_at = now_iso()
        if stamp:
            stamp_vendor(vendor.id, packed_at=packed_at, chapters=result.chapters)
        hashes[vendor.id] = {
            "sha256": key,
            "packed_at": packed_at,
            "chapters": result.chapters,
        }
        results.append(
            {
                "ok": True,
                "vendor": vendor.id,
                "action": "packed",
                "output": result.output,
                "chapters": result.chapters,
                "packed_at": packed_at,
                "sha256": key,
            }
        )
    save_pack_hashes(dest / HASHES_NAME, hashes)
    return results
