---
name: site2epub
description: Turn a product docs site (and optional blog) into one navigable EPUB3. Crawl locally and incrementally; GitHub Actions only packs offline. Use when the user runs /site2epub, /site-to-epub, or asks to pack cursor.com/docs, claude.com, learn.chatgpt.com, or similar docs+blog sites into an EPUB. 触发：站点转 EPUB、文档站打包、site to epub. Not for local Word/HTML files (book mode C) or writing original book chapters (book A/B).
compatibility: python3 + pandoc + beautifulsoup4 + lxml. Crawl needs network on the local machine; pack is offline (`SITESEPUB_OFFLINE=1`).
---

# site2epub

把产品文档站（及可选博客）打成一部可导航 EPUB3。工作树是 **sites-epub 仓库根**。

**抓取只在本地。EPUB 打包只走 GitHub Actions（或本机离线 `pack`）。**

## 何时用 / 何时不用

- 用：把官方文档树 + 博客编成一书；`/site2epub`；增量更新已有厂商。
- 不用：本地 Word/HTML 成品 → `book` 模式 C；源码级写书/课程书 → `book` A/B；只调研文档树不打包 → `deep-research`。

## 快流程

1. 在仓库根执行。新站：`python3 -m sites_epub add <docs-url> [blog-url] --name NAME`。已有厂商：`python3 -m sites_epub fetch --id ID`。
2. 未变路由跳过；缺失图片仍要补。Docs 导航在前，**Blog 是最后一个 TOC parent**。
3. 提交 `catalog.json`、`vendors/<id>/` 的 corpus 与 `fingerprints.json`。禁止 cookie、token、`.env`、`work/`。
4. 推 `main`。Actions 设 `SITESEPUB_OFFLINE=1` 只 `pack`（语料/封面/打包器未变的书跳过）。本机强制重打：`python3 -m sites_epub pack --force` 或 `--id ID`。
5. 验收：`python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub`（破图或标题未链原文即失败）。

## 按需读取

| 何时 | 文件 |
|---|---|
| 新建/增量/提交/CI | `references/workflow.md` |
| 图片缺失、破图、远程 src | `references/images.md` |
| 标题点击原文、TOC、walk 门禁 | `references/epub-rendering.md` |
| 文本/图/表/组件/画图怎么还原 | `references/scenes.md` |
| 判断该不该触发本技能 | `references/evals.md` |
| 标题 HTML 合同 | `assets/page-title.html` |

不要把上述正文再抄进本文件。

## 产出

打印 vendor id、fetched/skipped、corpus 路径。推送后 Actions 的 EPUB 才是书。
