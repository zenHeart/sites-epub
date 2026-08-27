# 图片

**总原则:EPUB 必须完全自包含。所有正文图在抓取阶段落入 `corpus/images`,打包时全部本地嵌入;不做任何远程引用(阅读器离线与兼容性无法保证)。**

- 抓取把正文图写入 `vendors/<id>/corpus/images` 与 `image-map.json`。Markdown `![]()` **和** HTML `<img src>` 都要收(Mintlify 文档图几乎全是 `<img>`,不是 ATX 图片语法);`/_next/image?url=` 包装图解包出内层地址再对齐。
- 增量 `fetch`:页面文本未变也要补 **缺失** 图片(`one_img` 对全部 routes 的图片列表重跑,map 外的重新下载)。
- **超大图不弃书**:下载超过 2.5MB 的位图先用 sips 等比降采样(1600→1100→800)压缩到阈值内再入包;压缩不可用或无效才放弃。
- `.md` 导出端点整体丢图时(Codex docs 常见):`fetch_source` 检测到 md 无任何图片标记,自动改抓渲染后的 HTML 版本作为语料源,保住正文插图。
- 打包只嵌入 corpus 里真实存在的文件;无本地副本时**去掉 `<img>`**,禁止留下远程 URL 或章节相对断链。
- `src` 带 `?fit=max` 查询串时按去掉 `?` 后的路径对齐 image-map,避免同一张图因参数不同被丢掉。
- 站点 chrome(`/logo/`、favicon、og 图、placeholder.svg)不入书。
- pandoc 之后打包器再剥掉 zip 中没有对应成员的 `<img>`。
- `walk` / `pack` / Actions 对 `empty_img_src`、`remote_img_src`、`broken_img_src` 一律失败(自包含硬约束)。
- 不要引入第三方图床(Google Drive 直链有配额封禁风险且阅读器兼容性差);体积控制走抓取端压缩,不走外链。
- 本机检查:`python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub`。
