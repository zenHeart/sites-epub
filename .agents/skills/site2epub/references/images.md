# 图片

- 抓取把正文图写入 `vendors/<id>/corpus/images` 与 `image-map.json`。
- 增量 `fetch`：页面文本未变也要补 **缺失** 图片。
- 打包只嵌入 corpus 里真实存在的文件。抓不到就 **去掉 `<img>`**，禁止留下远程 URL 或章节相对断链（阅读器会显示裂图）。
- pandoc 之后打包器再剥掉 zip 中没有对应成员的 `<img>`。
- `walk` / `pack` / Actions 对 `empty_img_src`、`remote_img_src`、`broken_img_src` 失败。
- 本机检查：`python3 .agents/skills/site2epub/scripts/check_epub.py dist/<id>.epub`。
