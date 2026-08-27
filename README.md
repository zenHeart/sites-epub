# sites-epub

Pack official product **docs + blog** into one EPUB per model vendor. Catalog: [epub.zenheart.site](http://epub.zenheart.site/).

## Layout

```
catalog.json          vendor list (no secrets)
vendors/<id>/         icon + fingerprints.json (content hashes only)
sites_epub/           crawl → MDX/HTML transform → pandoc EPUB3
.grok/skills/site2epub
```

TOC: live docs nav groups first, **Blog last**.

## Commands

```bash
python3 -m sites_epub add https://cursor.com/docs https://cursor.com/blog --name Cursor
python3 -m sites_epub build --all
python3 -m sites_epub catalog
```

GitHub Actions on `main` rebuilds every catalog vendor and publishes `gh-pages` (CNAME `epub.zenheart.site`).

Crawl caches (`vendors/*/work`) are gitignored. Do not commit tokens or cookies.
