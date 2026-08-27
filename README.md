# sites-epub

Pack official product **docs + blog** into one EPUB per model vendor. Catalog (ZenShelf): [epub.zenheart.site](http://epub.zenheart.site/).

The shelf shows **语料更新** time (`catalog.json` `updated_at`) so an incremental `fetch` can be judged against the live site. Linked handbooks (Pi, Claude Code 架构分析) open their own sites instead of duplicating the EPUB here.

**Crawl is local** (`add` / `fetch`, including incremental skip). **GitHub Actions only packs** EPUB from the committed `vendors/<id>/corpus` (no live fetch).

## Layout

```
catalog.json          vendor list (no secrets)
vendors/<id>/         icon + fingerprints.json (content hashes only)
  corpus/             pages + images + routes.json (committed source for CI pack)
sites_epub/           crawl → MDX/HTML transform → pandoc EPUB3
.grok/skills/site2epub
```

TOC: live docs nav groups first, **Blog last**.

## Commands

```bash
# local create or incremental crawl (agents / this machine)
python3 -m sites_epub add https://cursor.com/docs https://cursor.com/blog --name Cursor
python3 -m sites_epub fetch --id cursor

# offline pack (what GitHub Actions runs)
python3 -m sites_epub pack
python3 -m sites_epub catalog
```

Push `main` after committing corpus + fingerprints. Actions sets `SITESEPUB_OFFLINE=1` and runs `pack` only, then publishes `gh-pages` (CNAME `epub.zenheart.site`).

Do not commit tokens, cookies, `.env`, or `work/`.
