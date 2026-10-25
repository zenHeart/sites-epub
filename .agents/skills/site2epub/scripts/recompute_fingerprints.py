#!/usr/bin/env python3
"""Recompute fingerprints.json for one vendor using ACTIVE routes only.

lessons.md §24: the workflow.md snippet globs every `corpus/pages/**/*.md`,
which re-adds orphan pages (routes already dropped from routes.json but whose
.md file is still on disk). `fetch_vendor` writes fingerprints for active
routes only, so the two semantics fight and the diff is all noise.

Usage: recompute_fingerprints.py <vendor_id> [<vendor_id> ...]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from sites_epub.fingerprint import content_hash, save_fingerprints  # noqa: E402


def recompute(vid: str) -> dict:
    corpus = ROOT / "vendors" / vid / "corpus"
    routes_path = corpus / "routes.json"
    routes = json.loads(routes_path.read_text(encoding="utf-8"))
    active = {r["route"] for r in routes}
    fp = {}
    for r in sorted(active):
        page = corpus / "pages" / f"{r}.md"
        if page.is_file():
            fp[r] = content_hash(page.read_text(encoding="utf-8", errors="replace"))
    fp_path = ROOT / "vendors" / vid / "fingerprints.json"
    save_fingerprints(fp_path, fp)
    orphans = len(list((corpus / "pages").glob("**/*.md"))) - len(fp)
    return {"vendor": vid, "active_routes": len(active), "fingerprints": len(fp), "orphan_pages": orphans}


def main(vids: list[str]) -> int:
    out = [recompute(v) for v in vids]
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        print(__doc__)
        raise SystemExit(2)
    raise SystemExit(main(args))
