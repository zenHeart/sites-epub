---
name: site2epub
description: Turn a product docs site (and optional blog) into one EPUB on the sites-epub catalog. Create the vendor directory if missing; incrementally refetch only changed pages if it exists. Use when the user runs /site2epub, /site-to-epub, or asks to pack cursor.com/docs, claude.com, or learn.chatgpt.com into an EPUB.
---

# site2epub

Project-local skill. Working tree: the `sites-epub` repo root.

## Command

```bash
python3 -m sites_epub add <docs-url> [blog-url] [--name NAME] [--id ID]
```

Examples:

```bash
python3 -m sites_epub add https://cursor.com/docs https://cursor.com/blog --name Cursor --id cursor
python3 -m sites_epub build --id cursor
python3 -m sites_epub catalog
```

## Create vs incremental

1. Read `catalog.json`. If the vendor id (from `--id` or host guess) is **absent**, create `vendors/<id>/`, append the catalog row, then full-compile.
2. If it **exists**, keep the vendor directory. `compile_from_sources` / `compile_vendor_live` skip routes whose content hash matches `vendors/<id>/fingerprints.json`. Unchanged pages are not rewritten.
3. Docs routes stay in live-nav order; **Blog is always the last TOC parent**.
4. Do not commit `vendors/*/work/`, cookies, tokens, or `.env`.

## After a successful local compile

If `git remote` is `origin` on GitHub, commit catalog + vendor metadata + fingerprints (hashes only) and push so **GitHub Actions** rebuilds and publishes `epub.zenheart.site`. Do not put credentials in the repo.

## Output

Print vendor id, fetched vs skipped route counts, EPUB path, and whether the catalog card was written.
