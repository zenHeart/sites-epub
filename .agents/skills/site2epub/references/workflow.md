# 抓取、提交与打包

## 命令

```bash
python3 -m sites_epub add <docs-url> [blog-url] [--name NAME] [--id ID]
python3 -m sites_epub fetch --id codex
python3 -m sites_epub pack                 # CI：按书跳过未变厂商
python3 -m sites_epub pack --force         # 全量重打
python3 -m sites_epub pack --id claude     # 只打一本
python3 -m sites_epub catalog
```

## 新建 vs 增量

1. `catalog.json` 没有该 vendor id：建 `vendors/<id>/`，爬全部路由。
2. 已存在：用 `vendors/<id>/fingerprints.json` 对照 `corpus/pages`，**未变路由不重抓**。
3. 站点文档导航在前；**Blog 必须是最后一个 TOC parent**。
4. `fetch` 把 `updated_at`（语料时间）写进 `catalog.json`，书架用来对照线上是否过期。其他 EPUB 站点在 `catalog.json` → `sites`，封面点击跳到那些 URL。

## 提交

提交：`catalog.json`、`vendors/<id>/vendor.json`、`fingerprints.json`、`corpus/pages`、`corpus/routes.json`、`corpus/image-map.json`、压缩后的图片。

禁止：cookie、token、`.env`、`work/`。

## CI

- 环境变量 `SITESEPUB_OFFLINE=1`。http 层对任何 live fetch 直接失败。
- 先 checkout `gh-pages` 到 `prev-site`，`SITESEPUB_PREV_SITE=prev-site`。
- 一本书只在 **corpus / 封面 / 打包器源码** 变化时重打；否则复制上次 EPUB。
- 打包器改动（标题链接、CSS）会改变共享指纹，三本都重打。这是正确行为。
- workflow_dispatch 勾 `force` 或 `SITESEPUB_FORCE=1` 全量重打。
- `walk` 用 `blocking_defects`：破图或 `unlinked_page_title` 即失败。

不要在 Actions 里跑 `add`/`fetch`。
