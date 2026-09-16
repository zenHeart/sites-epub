> ## Documentation Index
> Fetch the complete documentation index at: https://platform.kimi.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI 可读文档

> 通过 llms.txt、llms-full.txt、OpenAPI Schema 和单页 Markdown，将 Kimi 开放平台文档提供给 AI 编程助手、企业机器人或 RAG 系统。

Kimi 开放平台文档站提供多种机器可读入口。你可以把整站文档直接交给 AI 编程助手、企业机器人或 RAG 系统使用，无需逐页抓取网页。

## 全站入口

| 入口             | 地址                                                                                           | 说明                                                 |
| :------------- | :------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| llms.txt       | [https://platform.kimi.com/docs/llms.txt](https://platform.kimi.com/docs/llms.txt)           | 全站页面索引，目录式结构，体积约 9 KB。适合先让模型了解站点结构，再按需读取具体页面       |
| llms-full.txt  | [https://platform.kimi.com/docs/llms-full.txt](https://platform.kimi.com/docs/llms-full.txt) | 全站文档的完整 Markdown，体积约 700 KB。适合作为完整上下文或 RAG 语料一次性读入 |
| OpenAPI Schema | [https://platform.kimi.com/docs/openapi.json](https://platform.kimi.com/docs/openapi.json)   | API 接口规范原文（OpenAPI 3.1）。适合对接 API、生成调用代码            |

## 单页 Markdown

任意文档页面在 URL 后加 `.md` 后缀，即可获得该页的 Markdown 版本，例如 [https://platform.kimi.com/docs/get-api-key.md](https://platform.kimi.com/docs/get-api-key.md)。页面右上角菜单也提供 Copy Page（复制本页 Markdown）和「在 Kimi 中打开」入口，适合只关心个别页面的场景。

<img src="https://mintcdn.com/moonshotcn/0pXCc2kBtCe8FRPk/assets/pics/ai-readable-docs/copy-page-menu.png?fit=max&auto=format&n=0pXCc2kBtCe8FRPk&q=85&s=5282d1e89ae80fa163be78c3a3f63b22" alt="复制页面菜单：复制页面、以 Markdown 格式查看、在 Kimi 中打开" width="2232" height="984" data-path="assets/pics/ai-readable-docs/copy-page-menu.png" />

## 推荐使用方式

* **AI 编程助手**（Claude Code、Cursor 等）：把 llms.txt 的地址加入规则或上下文文件，模型会先了解站点结构，再按需读取具体页面；
* **RAG 全量索引、企业机器人知识源**：抓取 llms-full.txt，一次获得全站内容，按页面切分后建立索引；
* **对接 API、生成调用代码**：直接使用 openapi.json，无需从文档页面提取接口信息。

英文文档站同样提供以上入口。
