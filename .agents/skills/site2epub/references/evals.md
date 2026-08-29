# 触发与验收

## 应触发

- 「把 cursor.com/docs 打成 EPUB」
- 「/site2epub claude.com/blog」
- 「增量更新 Codex 文档书」
- 「站点文档转 EPUB，标题点回原文」

## 不应触发

- 「把这份 docx 转成 EPUB」→ `book` 模式 C
- 「给这个开源仓写一章源码书」→ `book` 模式 A
- 「从大纲出中文课程书」→ `book` 模式 B
- 「调研官方文档教程树，不要打包」→ `deep-research`

## 功能验收

1. `python3 -m unittest tests.test_sites_epub -v` 全部通过。
2. 打包后 `python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub` 退出码 0（含封面标题反向门禁：cover.xhtml / OPF / metadata.yaml 不再出现 `ChatGPT Codex Docs` 等残留）。
3. 每页 `h2` 含 `a.source-title[href^=http]`；正文无 `.page-meta` 印 URL；nav 无 `href="https://..."` 指向原文章节。
4. Frame 图进 `<figure>`；Card 标题链到原站；Mermaid 成 `pre.mdx-mermaid` 而非消失；交互树有原站锚点且无 `useMemo`。
5. `python3 -m unittest tests.test_sites_epub.TestSceneRestore -v` 通过。
6. 结构：`python3 ~/.agents/skills/skill-optimizer/scripts/validate_skill_structure.py .agents/skills/site2epub` 无 error（脚本路径以本机 skill-optimizer 安装位置为准）。
7. 已发布 EPUB 抽样核对：每本书 `cover.xhtml` 的 `<title>` 与 `<dc:title>` 都是该 vendor 的真实名（Claude / Codex / Cursor / Grok），不是其它 vendor 的旧默认。
