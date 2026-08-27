# EPUB 渲染

读者点教程/文章**标题**必须打开原文 `html_url`（Apple Books / Kindle 通常走系统浏览器）。HTML 合同以 `assets/page-title.html` 为准。

## 必须

- 页面容器：`<div class="doc-page" id="{route}" data-source="{html_url}">`。
- 标题：`h2.page-title > a.source-title[rel=external][href={html_url}]`。链接色 + 下划线，可加 `span.source-mark`「↗」。
- 目录 `nav`/`toc` 仍指向书内章节。标题外链只存在于正文。
- 只改打包即可，**不要为改标题链接重新抓取**。

## 禁止

- 把原文 URL 印成 `.page-meta` 段落（那是未链接标题的代偿）。
- 把 TOC 项改成打开网页。

## 门禁

`walk` / `pack` / Actions 对 `unlinked_page_title` 失败，与破图同级。本地：

```bash
python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub
python3 -m unittest tests.test_sites_epub.TestSourceTitleLinks -v
```
