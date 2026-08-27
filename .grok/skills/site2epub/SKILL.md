---
name: site2epub
description: Turn a product docs site (and optional blog) into one EPUB on the sites-epub catalog. Crawl locally (create vendor dir or incrementally update changed pages); GitHub Actions only packs EPUB. Use when the user runs /site2epub, /site-to-epub, or asks to pack cursor.com/docs, claude.com, or learn.chatgpt.com into an EPUB.
---

# site2epub

Working tree: `sites-epub` repo root.

**Crawl is local. EPUB pack is GitHub Actions.**

## Commands

```bash
# create or incremental fetch (network, local machine / agents)
python3 -m sites_epub add <docs-url> [blog-url] [--name NAME] [--id ID]

# refetch existing catalog vendors
python3 -m sites_epub fetch --id codex

# offline pack from committed corpus (what CI runs)
python3 -m sites_epub pack
```

## Create vs incremental

1. If vendor id is missing from `catalog.json`, create `vendors/<id>/` and crawl every route.
2. If it exists, compare `vendors/<id>/fingerprints.json` to cached `corpus/pages`; **do not refetch unchanged routes**.
3. Docs nav order first; **Blog is the last TOC parent**.
4. Commit `catalog.json`, `vendors/<id>/vendor.json`, `fingerprints.json`, `corpus/pages`, `corpus/routes.json`, `corpus/image-map.json`, and compressed images. Never commit cookies, tokens, `.env`, or `work/`.
5. Push `main`. Actions runs `python3 -m sites_epub pack` only (no live crawl) and publishes `epub.zenheart.site`.

## Output

Print vendor id, fetched vs skipped counts, corpus path. After push, the Actions EPUB artifact is the book.
