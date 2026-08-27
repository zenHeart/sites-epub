# sites-epub

按厂商把官方文档和博客打成一部 EPUB。目录站：[epub.zenheart.site](http://epub.zenheart.site/)（ZenShelf）。

- **厂商文档**（Codex / Claude / Cursor）：点封面下载 EPUB。
- **源码书**（Pi、Claude Code 架构分析、DeepSeek Harness）：点封面进入各自落地站，不在本仓库重复托管文件。
- 卡片上的「语料」对应 `catalog.json` 的 `updated_at`，即最近一次本地增量抓取的时间，用来对照线上是否过期。

抓取只在本地执行（`add` / `fetch`，未变更的页面会跳过）。GitHub Actions 只从已提交的 `vendors/<id>/corpus` 离线打包 EPUB，不访问产品站点。书中每篇教程和文章的标题是指向原文的链接，点击标题即可打开对应页面。

## 目录

```
catalog.json          厂商与源码书清单（不含密钥）
vendors/<id>/         图标与 fingerprints.json（仅内容哈希）
  corpus/             页面、图片、routes.json（CI 打包的输入）
sites_epub/           抓取 → MDX/HTML 转换 → pandoc EPUB3
.grok/skills/site2epub
```

目录顺序：站点文档导航在前，**Blog 放在最后**。

## 命令

```bash
# 本地新建或增量抓取（本机 / agent）
python3 -m sites_epub add https://cursor.com/docs https://cursor.com/blog --name Cursor
python3 -m sites_epub fetch --id cursor

# 离线打包（GitHub Actions 跑这一步；未变化的书会跳过）
python3 -m sites_epub pack
python3 -m sites_epub pack --force
python3 -m sites_epub catalog
```

提交 `corpus` 与 `fingerprints.json` 后推送 `main`。Actions 设置 `SITESEPUB_OFFLINE=1`，只跑 `pack`，再发布 `gh-pages`（CNAME 为 `epub.zenheart.site`）。打包按厂商增量：语料、封面和打包器都没变的书直接复用上次发布的 EPUB，不会每次全量重打。

不要提交令牌、cookie、`.env` 或 `work/`。
