# sites-epub

把官方文档站 + 博客打成 EPUB。执行契约在 `.agents/skills/site2epub/`（Claude 经 `.claude/skills/site2epub` 指向同一目录）。

- 抓取只在本机 `add`/`fetch`；GitHub Actions 只离线 `pack`。
- 不要走 `book` 模式 C（那是本地 Word/HTML 转换，不是站点抓取）。
- 标题必须链到原文；破图和未链标题会使 pack/CI 失败。
