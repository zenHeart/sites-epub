"""CLI: local incremental fetch; GitHub Actions packs EPUB from corpus."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .catalog import guess_adapter, guess_vendor_id, load_catalog, upsert_vendor, vendor_dir
from .catalog_html import write_site
from .compile import fetch_vendor, pack_vendor
from .models import Vendor

ROOT = Path(__file__).resolve().parents[1]


def _write_vendor_json(v: Vendor, vdir: Path) -> None:
    (vdir / "vendor.json").write_text(
        json.dumps(
            {
                "id": v.id,
                "name": v.name,
                "docs_url": v.docs_url,
                "blog_url": v.blog_url,
                "icon": v.icon,
                "author": v.author,
                "adapter": v.adapter,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def _vendor_from_args(args: argparse.Namespace) -> Vendor:
    vid = args.id or guess_vendor_id(args.docs, args.name)
    return Vendor(
        id=vid,
        name=args.name or vid.replace("-", " ").title(),
        docs_url=args.docs,
        blog_url=args.blog,
        icon=f"vendors/{vid}/icon.png",
        author=args.author or "",
        adapter=args.adapter or guess_adapter(args.docs),
    )


def cmd_add(args: argparse.Namespace) -> int:
    vendor = _vendor_from_args(args)
    vdir = vendor_dir(vendor.id, ROOT)
    vdir.mkdir(parents=True, exist_ok=True)
    upsert_vendor(vendor)
    _write_vendor_json(vendor, vdir)
    result = fetch_vendor(vendor, root=ROOT, workers=args.workers)
    print(
        json.dumps(
            {
                "ok": True,
                "vendor": vendor.id,
                "mode": "fetch",
                "fetched": result.fetched_routes,
                "skipped": result.skipped_routes,
                "entries": result.entries,
            },
            indent=2,
        )
    )
    return 0


def cmd_fetch(args: argparse.Namespace) -> int:
    vendors = load_catalog()
    if args.id:
        vendors = [v for v in vendors if v.id == args.id]
        if not vendors:
            print(f"unknown vendor {args.id}", file=sys.stderr)
            return 1
    code = 0
    for v in vendors:
        try:
            result = fetch_vendor(v, root=ROOT, workers=args.workers)
            print(
                json.dumps(
                    {
                        "ok": True,
                        "vendor": v.id,
                        "fetched": len(result.fetched_routes),
                        "skipped": len(result.skipped_routes),
                        "entries": result.entries,
                    }
                )
            )
        except Exception as exc:  # noqa: BLE001
            print(f"error {v.id}: {exc}", file=sys.stderr)
            code = 1
    return code


def cmd_pack(args: argparse.Namespace) -> int:
    vendors = load_catalog()
    if args.id:
        vendors = [v for v in vendors if v.id == args.id]
        if not vendors:
            print(f"unknown vendor {args.id}", file=sys.stderr)
            return 1
    dest = ROOT / "dist"
    dest.mkdir(exist_ok=True)
    code = 0
    for v in vendors:
        try:
            out = dest / f"{v.id}.epub"
            result = pack_vendor(v, out, root=ROOT)
            print(
                json.dumps(
                    {
                        "ok": True,
                        "vendor": v.id,
                        "output": result.output,
                        "chapters": result.chapters,
                    }
                )
            )
        except Exception as exc:  # noqa: BLE001
            print(f"error {v.id}: {exc}", file=sys.stderr)
            code = 1
    write_site(ROOT / "site", load_catalog(), dist=dest)
    return code


def cmd_catalog(args: argparse.Namespace) -> int:
    dest = Path(args.dest) if args.dest else ROOT / "site"
    write_site(dest, dist=ROOT / "dist")
    print(json.dumps({"ok": True, "dest": str(dest)}))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="site2epub")
    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="register vendor and incrementally fetch corpus (local)")
    add.add_argument("docs")
    add.add_argument("blog", nargs="?")
    add.add_argument("--id")
    add.add_argument("--name")
    add.add_argument("--adapter")
    add.add_argument("--author")
    add.add_argument("--workers", type=int, default=12)
    add.set_defaults(func=cmd_add)

    fetch = sub.add_parser("fetch", help="incremental crawl into vendors/<id>/corpus (local)")
    fetch.add_argument("--id")
    fetch.add_argument("--workers", type=int, default=12)
    fetch.set_defaults(func=cmd_fetch)

    pack = sub.add_parser("pack", help="offline EPUB pack from corpus (GitHub Actions)")
    pack.add_argument("--id")
    pack.add_argument("--all", action="store_true")
    pack.set_defaults(func=cmd_pack)

    cat = sub.add_parser("catalog", help="write static catalog HTML")
    cat.add_argument("--dest")
    cat.set_defaults(func=cmd_catalog)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
