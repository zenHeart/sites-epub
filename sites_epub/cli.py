"""CLI: site2epub create-or-incremental compile + catalog."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .catalog import (
    CATALOG_PATH,
    guess_adapter,
    guess_vendor_id,
    load_catalog,
    upsert_vendor,
    vendor_dir,
)
from .catalog_html import write_site
from .compile import compile_from_sources, compile_vendor_live, discover_entries
from .models import Vendor

ROOT = Path(__file__).resolve().parents[1]


def cmd_add(args: argparse.Namespace) -> int:
    docs = args.docs
    blog = args.blog
    vid = args.id or guess_vendor_id(docs, args.name)
    name = args.name or vid.replace("-", " ").title()
    adapter = args.adapter or guess_adapter(docs)
    author = args.author or ""
    vdir = vendor_dir(vid, ROOT)
    vdir.mkdir(parents=True, exist_ok=True)
    icon_rel = f"vendors/{vid}/icon.png"
    vendor = Vendor(
        id=vid,
        name=name,
        docs_url=docs,
        blog_url=blog,
        icon=icon_rel,
        author=author,
        adapter=adapter,
    )
    upsert_vendor(vendor)
    (vdir / "vendor.json").write_text(
        json.dumps(
            {
                "id": vid,
                "name": name,
                "docs_url": docs,
                "blog_url": blog,
                "icon": icon_rel,
                "author": author,
                "adapter": adapter,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"ok": True, "vendor": vid, "created": True}, indent=2))
    if args.no_build:
        return 0
    return cmd_build_one(vendor, args)


def cmd_build_one(vendor: Vendor, args: argparse.Namespace) -> int:
    out = ROOT / "dist" / f"{vendor.id}.epub"
    result = compile_vendor_live(vendor, out, root=ROOT, workers=args.workers)
    print(
        json.dumps(
            {
                "ok": True,
                "vendor": vendor.id,
                "output": result.output,
                "fetched": result.fetched_routes,
                "skipped": result.skipped_routes,
                "chapters": result.chapters,
            },
            indent=2,
        )
    )
    return 0


def cmd_all(args: argparse.Namespace) -> int:
    vendors = load_catalog()
    if not vendors:
        print("no vendors in catalog.json", file=sys.stderr)
        return 1
    code = 0
    for v in vendors:
        try:
            cmd_build_one(v, args)
        except Exception as exc:  # noqa: BLE001
            print(f"error {v.id}: {exc}", file=sys.stderr)
            code = 1
    write_site(ROOT / "site", vendors, dist=ROOT / "dist")
    return code


def cmd_catalog(args: argparse.Namespace) -> int:
    write_site(Path(args.dest) if args.dest else ROOT / "site", dist=ROOT / "dist")
    print(json.dumps({"ok": True, "dest": str(args.dest or ROOT / "site")}))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="site2epub")
    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="create or update a vendor and compile")
    add.add_argument("docs")
    add.add_argument("blog", nargs="?")
    add.add_argument("--id")
    add.add_argument("--name")
    add.add_argument("--adapter")
    add.add_argument("--author")
    add.add_argument("--workers", type=int, default=12)
    add.add_argument("--no-build", action="store_true")
    add.set_defaults(func=cmd_add)

    build = sub.add_parser("build", help="rebuild one or all catalog vendors")
    build.add_argument("--id")
    build.add_argument("--all", action="store_true")
    build.add_argument("--workers", type=int, default=12)
    build.set_defaults(func=lambda a: cmd_all(a) if a.all or not a.id else cmd_build_one(
        next(v for v in load_catalog() if v.id == a.id), a
    ))

    cat = sub.add_parser("catalog", help="write static catalog HTML")
    cat.add_argument("--dest")
    cat.add_argument("--workers", type=int, default=12)
    cat.set_defaults(func=cmd_catalog)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
