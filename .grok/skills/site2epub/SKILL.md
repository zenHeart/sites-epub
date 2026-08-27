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
python3 -m sites_epub pack --force          # rebuild every vendor
python3 -m sites_epub pack --id claude      # rebuild one book
```

## Create vs incremental

1. If vendor id is missing from `catalog.json`, create `vendors/<id>/` and crawl every route.
2. If it exists, compare `vendors/<id>/fingerprints.json` to cached `corpus/pages`; **do not refetch unchanged routes**.
3. Docs nav order first; **Blog is the last TOC parent**.
4. Commit `catalog.json`, `vendors/<id>/vendor.json`, `fingerprints.json`, `corpus/pages`, `corpus/routes.json`, `corpus/image-map.json`, and compressed images. Never commit cookies, tokens, `.env`, or `work/`.
5. Push `main`. Actions sets `SITESEPUB_OFFLINE=1` and runs `python3 -m sites_epub pack` only (no live crawl) and publishes `epub.zenheart.site`. **Pack is per-vendor:** a book is rebuilt only when its corpus, cover, or packer source changes. Unchanged books are copied from the previous `gh-pages` publish (`SITESEPUB_PREV_SITE`). `--force` / workflow_dispatch `force` rebuilds every vendor. A packer change (for example title-link CSS) changes the shared fingerprint and rebuilds all books.
6. `fetch` writes `updated_at` (语料时间) onto `catalog.json` so the shelf shows how stale the book is versus the live docs/blog. Other EPUB sites live in `catalog.json` → `sites` and the shelf jumps to those URLs.

## Images

- Crawl writes every content image into `vendors/<id>/corpus/images` and `image-map.json`.
- Incremental `fetch` still downloads **missing** images even when page text is unchanged.
- Pack embeds only files that exist in the corpus. If an image cannot be fetched, **omit the `<img>`** — never leave a remote or chapter-relative `src` that the reader will show as a broken placeholder.
- After pandoc, the packer strips any leftover `<img>` whose `src` is not a zip member. Walk/`pack` fail on `broken_img_src` / `remote_img_src` / `empty_img_src`.

## EPUB 标题即原文

打包器必须把每一篇教程/文章的页面标题做成 EPUB3 外部链接，读者在阅读器里**点击标题**即打开 `html_url`（Apple Books / Kindle 通常用系统浏览器）。

- 页面容器：`<div class="doc-page" id="{route}" data-source="{html_url}">`。
- 标题：`<h2 class="page-title"><a class="source-title" href="{html_url}" rel="external">标题</a></h2>`。用链接色 + 下划线，不要把标题做成不可点的纯文本。
- **不要**再把原文 URL 印成 `.page-meta` 段落。那是未链接标题的代偿，不是 EPUB 的跳转形态。
- 目录 `nav`/`toc` 仍指向书内章节。标题外链只存在于正文，禁止把 TOC 改成打开网页。
- 只改打包即可，**不要重新抓取**。`SITESEPUB_OFFLINE=1 python3 -m sites_epub pack` 从已有 corpus 重建。
- `walk` / `pack` / Actions 对 `unlinked_page_title` 失败，与破图同等拦截。

## Output

Print vendor id, fetched vs skipped counts, corpus path. After push, the Actions EPUB artifact is the book.
