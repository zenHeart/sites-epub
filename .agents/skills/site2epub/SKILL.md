---
name: site2epub
description: Turn a product docs site (and optional blog) into one navigable EPUB3. Crawl locally and incrementally; GitHub Actions only packs offline. Use when the user runs /site2epub, /site-to-epub, or asks to pack cursor.com/docs, claude.com, learn.chatgpt.com, or similar docs+blog sites into an EPUB. 触发：站点转 EPUB、文档站打包、site to epub. Not for local Word/HTML files (book mode C) or writing original book chapters (book A/B).
compatibility: python3 + pandoc + beautifulsoup4 + lxml. Crawl needs network on the local machine; pack is offline (`SITESEPUB_OFFLINE=1`).
---

# site2epub

把产品文档站（及可选博客）打成一部可导航 EPUB3。工作树是 **sites-epub 仓库根**。

**抓取只在本地。EPUB 打包只走 GitHub Actions（或本机离线 `pack`）。**

## 何时用 / 何时不用

- 用：把**厂商产品**文档树 + 高质量博客 + 使用经验编成一书；`/site2epub`；增量更新已有厂商。
- 不用：本地 Word/HTML 成品 → `book` 模式 C；源码级写书/课程书 → `book` A/B；只调研文档树不打包 → `deep-research`。

## 范围铁律:产品书,不是 API 书(用户 2026-09-16 定调)

对标 codex / claude code / cursor / gemini / manus 五本:收的都是**模型厂商面向用户的产品**——产品文档、官方 blog、教程与使用经验沉淀。**开放平台 API 使用文档(API key / 鉴权 / 端点参考 / SDK 接入)不属于本书系范畴**,发现即剔出路由。判断法:这页内容是「用这个产品」还是「调这个厂商的 API」——后者出局。

**章节组织**:每个独立产品、知识域(如厂商经验/教程)或 blog 各占一个顶层大章节(group),按产品逐个组织,绝不按 API 域混排;Blog 恒为最后一个大章节。每章标题必须链回原文(打包器既有不变量)。

## 穷尽主流门禁(用户 2026-09-16 增:避免漏抓热门产品)

**每本书开工前必须跑 `tools/mainstream_list.py` 域级探测**,对照当前领域「Top N 主流 AI 工具榜单」(至少 3 个独立来源,如 Pinggy / skills-hub / automationswitch / capitalandcompute 等 2026 横评),把可能遗漏的产品先走一遍 E 层探测(`llms.txt` / `sitemap.xml` / 关键产品域名),再决定建书/并入/放弃。**禁止** 仅凭用户提到或上一会话探到的站点就开工——2026-09-16 zcode.z.ai 漏抓就是这一缺陷的直接结果。

判定规则:
- **独立公司产品**(如 Zencoder、Manus): 独立成书。
- **厂商自有产品**且同公司已有书(如 ZCode 属智谱): 并入该厂商书,新增一个「产品」大章节。
- **API 平台、跨厂商 orchestration 工具**(openapi/RPC/sdk 接入类): 不建书,出报告进注册表。

## 快流程

1. 在仓库根执行。新站：`python3 -m sites_epub add <docs-url> [blog-url] --name NAME`。已有厂商：`python3 -m sites_epub fetch --id ID`。
2. 未变路由跳过；缺失图片仍要补。Docs 导航在前，**Blog 是最后一个 TOC parent**。
3. 提交 `catalog.json`、`vendors/<id>/` 的 corpus 与 `fingerprints.json`。禁止 cookie、token、`.env`、`work/`。
4. 推 `main`。Actions 设 `SITESEPUB_OFFLINE=1` 只 `pack`（语料/封面/打包器未变的书跳过）。本机强制重打：`python3 -m sites_epub pack --force` 或 `--id ID`。
5. 验收：`python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub`（破图、标题未链原文、封面标题反向串号即失败）。

## 按需读取

| 何时 | 文件 |
|---|---|
| 新建/增量/提交/CI | `references/workflow.md` |
| 图片缺失、破图、远程 src | `references/images.md` |
| 标题点击原文、TOC、walk 门禁 | `references/epub-rendering.md` |
| 文本/图/表/组件/画图怎么还原 | `references/scenes.md` |
| 判断该不该触发本技能 | `references/evals.md` |
| 实战踩坑（封面标题串号、icon SVG-as-PNG、Mintlify llms.txt、secret-scan、跨子域多根） | `references/lessons.md` |
| 标题 HTML 合同 | `assets/page-title.html` |

不要把上述正文再抄进本文件。

## 产出

打印 vendor id、fetched/skipped、corpus 路径。推送后 Actions 的 EPUB 才是书。
