# 场景还原合同

Markdown / MDX / HTML 进 EPUB 时，按**站点上的读者体验**映射，而不是按源码形态。交互跑不起来就给原站链接，并把能静态化的内容留下。

| 站点场景 | EPUB 形态 | 跑不了时 |
|---|---|---|
| 标题 | `h2` 外链到 `html_url` | — |
| 正文、列表、引用、行内 `code`/`kbd` | 保留，套 EPUB CSS | — |
| 表格 | 真 `<table>`，有边框表头 | — |
| 截图 / `<img>` / `<Frame>` | 嵌入 corpus 图；Frame → `<figure>` | 抓不到则删 `<img>`，不留裂图 |
| SVG 示意图 | 保留 `<svg>` 或 `<img src="*.svg">` | 同上 |
| Mermaid / 画图源码 | `<figure class="mdx-diagram">` + `pre.mdx-mermaid` | 提示去原站看渲染结果 |
| Note / Tip / Warning / Danger | 左边框 callout | — |
| Tabs / CodeGroup | 每个面板带标题，全部展开 | — |
| Accordion | 标题 + 正文展开 | — |
| Steps | 有序步骤列表 | — |
| Card / CardGroup | 卡片 + 指向原站的标题链接 | — |
| 目录浏览器等交互组件 | 静态卡片（文件说明/示例） | **必须**链到原文章节，如 `#explore-the-directory` |
| Video / iframe | 一句说明 + 原站/片源链接 | 不嵌播放器 |
| 站内 `/docs/...` 链接 | 写成 `https://` 绝对地址 | 阅读器可跳出打开 |

Mintlify「View as Markdown」若是 React/MDX 源码，改用渲染后的 HTML article，再叠上述映射。禁止把 `export const` / `useMemo` 打进书里。
