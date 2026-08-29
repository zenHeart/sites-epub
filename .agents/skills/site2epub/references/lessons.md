# 实战踩坑（从 claude/codex/cursor → xai 这条路）

每一项都给出了**根因**、**怎么发现**、**怎么修**、**怎么防止复发**。下一次 /site2epub 时先扫一遍这里。

## 1. 封面标题串号：每本书开头都写着 "ChatGPT Codex Docs"

**症状**：claude / codex / cursor / grok 四本书的 `EPUB/text/cover.xhtml` 里 `<title>` 都是 `ChatGPT Codex Docs`，OPF 的 `<dc:title>` 才对。

**根因**：`sites_epub/epub_pack.py` 里 `grouped_html()` 把 `<title>ChatGPT Codex Docs</title>` 写死；`pack_epub()` 的 `title` 默认值也是 `"ChatGPT Codex Docs"`、`author="OpenAI"`。第一个 vendor 是 codex 时遗留的硬编码。

**怎么发现**：下载已发布 EPUB，`zipfile` 读 `EPUB/text/cover.xhtml`，看 `<title>`。`check_epub.py` 现在已经把它列为门禁。

**怎么修**：

| 文件 | 改动 |
|---|---|
| `sites_epub/epub_pack.py` | `grouped_html(..., *, title="", author="")` 接受参数；`<title>{title or "Documentation"}</title>`；`pack_epub` 默认 `title="Documentation"`、`author=""`；临时目录前缀从 `chatgpt-learn-docs-epub-` 改为 `sites-epub-` |
| `sites_epub/images.py` | `normalize_image_url / collect_markdown_image_urls / collect_image_urls / collect_source_image_urls` 的 `base` 默认值从 `"https://learn.chatgpt.com"` 改为 `""` |
| `sites_epub/page.py` | 三处 `base=url or "https://learn.chatgpt.com"` → `base=url or ""` |

**怎么防止复发**：`.agents/skills/site2epub/scripts/check_epub.py` 新增 `_check_cover_title()`：扫描 `cover.xhtml` / `.opf` / `metadata.yaml`，匹配 `ChatGPT Codex Docs` / `ChatGPT Codex` / `learn.chatgpt.com/docs`，命中即 `FAIL cover title leak`。CI 的 "Validate EPUBs" 步骤对每个 `dist/*.epub` 都跑一遍。

---

## 2. icon 自动抓取会把 SVG 字节当 PNG 存

**症状**：`vendors/<id>/icon.png` 文件头是 `<svg width=...`，但扩展名是 `.png`。打包时 pandoc 把这段 SVG 嵌进封面，某些阅读器拒绝渲染。

**根因**：`sites_epub/compile.py: ensure_vendor_icon()` 只看字节数 >200 且不以 `<!do` 开头，没校验文件魔数（PNG 应是 `\x89PNG\r\n\x1a\n`）。

**怎么发现**：`file vendors/grok/icon.png` 显示 `SVG Scalable Vector Graphics image, ASCII text`，与 `.png` 扩展名冲突。

**怎么修**：直接 `curl https://<host>/icon.png -o vendors/<id>/icon.png` 拿一个真 PNG；写完后用 `file vendors/<id>/icon.png` 验证魔数。xAI 这种 Next.js 站点的根 `/icon.png` 通常是真 PNG。

**怎么防止复发**：在 skill workflow.md 里加一条「icon 入库前 `file` 校验魔数；SV G- 字节 -as -PNG 必须替换」。

---

## 3. llms.txt 格式不止一种：Mintlify `===/path===` 切片式

**症状**：`docs.x.ai/llms.txt` 是 164 个 `===/route===` 切片，每段内部才写 `# Title` 与 `* [Link](/path)`。`parse_llms_generic()` 只识别 `- [title](url)` / `- https://...`，拿到 0 条。

**根因**：xAI 用 Mintlify，`llms.txt` 是页面合并版（每段即一篇文档正文）。Cursor / Claude 用的是另一种（仅索引列表）。

**怎么修**：写 `sites_epub/xai_nav.py`，`parse_xai_llms(text, docs_url)` 用 `SECTION_RE = re.compile(r"^===(/[^=]*)===\s*$")` 切片，第一个 `^# (.+)$` 取标题，group 由 URL 前缀映射（build / developers / grok / grok-bot / console / integrations）。同时把 `compile.py` 的 `discover_entries` 加 `xai` 分支；`fetch_vendor` 的 llms 候选列表加 `"https://docs.x.ai/llms.txt" if vendor.adapter == "xai" else ""`。

**怎么防止复发**：每个新 vendor 跑 add 前先 `curl -sSL <docs-url>/llms.txt | head -60` 看一下格式。若不是 `[title](url)` 列表式，写个 80 行小适配器，不要去改 `parse_llms_generic` 的正则——它的格式契约已被多个 vendor 依赖。

---

## 4. GitHub secret-scanner 会拦下文档示例 API key

**症状**：`git push origin main` 被拒：`xAI API Key` 命中，路径 `vendors/grok/corpus/llms.txt:29091` 等。

**根因**：xAI 文档示例里给了形如 `xai-2xr2bnFV7lAbc...` 的真实模式 key，secret-scanner 误判为真 key。

**怎么修**：
1. 先把所有命中行的真实 key 替换成 `xai-YOUR_API_KEY_HERE`。
2. `git commit --amend --no-edit` 重新打包。
3. 重试 push。

**怎么防止复发**：任何 docs vendor 都可能在示例里给形似真实的 key（OpenAI `sk-...` / Anthropic `sk-ant-...` / xAI `xai-...` / AWS `AKIA...`）。push 前用 `git diff --cached | grep -E "(sk-[A-Za-z0-9]|xai-[A-Za-z0-9]|AKIA[0-9A-Z]{16})"` 自检；CI 端若漏过，本地 push 兜底。

---

## 5. covers/<id>.png 缺位或不对齐

**症状**：第一次 `add` 出来的 `covers/grok.png` 是把 `vendors/grok/icon.png` 复制的 512x512 SVG；其它 vendor 的封面是 800x1120 PNG 排版。

**根因**：现有 vendor 的封面 SVG 是手画的（`covers/claude.svg`、`covers/codex.svg`、`covers/cursor.svg`），pandoc 渲成 800x1120 PNG 后入库；新 vendor 没有手画 SVG，直接 copy icon 不对齐。

**怎么修**：

| 步骤 | 做法 |
|---|---|
| 1 | 写 `covers/<id>.svg`：viewBox 400×560，深色背景 + 边框 + eyebrow `SITE EPUB / {COMPANY}` + 衬线大字标题 + 中文副标题 + 1px accent line + 底部品牌 + URL。复制 `covers/codex.svg` 当骨架改色 |
| 2 | 渲成 `covers/<id>.png` 800×1120：缺 cairo DLL 时用 PIL 走 fallback（`from PIL import Image, ImageDraw, ImageFont`，逐元素 `rect` / `text` / `line`），文件大小 ~25 KB |
| 3 | catalog.json 的 `cover` 字段指向 `covers/<id>.png`，CI 的 catalog 步骤会同步到 gh-pages |

**怎么防止复发**：每次新 vendor 先把 SVG 手画一份，再渲 PNG；不要直接拿 icon.png 当 cover。模板见 `covers/codex.svg`。

---

## 6. 多文档根域名（docs.x.ai + x.ai/bot/guides）

**症状**：用户给的 5 个 URL 跨 `docs.x.ai/*` 与 `x.ai/bot/guides`、`x.ai/news`，但 CLI 只接受 1 个 docs_url + 1 个 blog_url。

**根因**：`Vendor` 模型只有 `docs_url`，`parse_docs_html` 用前缀匹配；docs_url = `/build/overview` 时只匹配 `/build/*`，丢了 `/grok/*` `/grok-bot/*`。

**怎么修**：
- docs_url 取 `docs.x.ai` 下某条统一入口；统一用 `https://docs.x.ai/llms.txt` 拿全量索引（163 条）。
- bot/guides 不是 docs.x.ai 的一部分，在 `discover_entries` 的 `xai` 分支里额外 `fetch_text("https://x.ai/bot/guides")` + `parse_xai_bot_guides()`，group = `Bot Guides`，route = `bot-guides/<slug>`。
- news 走正常 blog_url 分支，`parse_xai_blog()` 用 `NEWS_SLUG = re.compile(r"^/news/([A-Za-z0-9][A-Za-z0-9\-_]*)/?$")` 匹配。

**怎么防止复发**：下次遇到 docs URL 跨子域 / 多根时，先用 `curl` 摸一遍能不能拿到一份统一 llms.txt；不能就写个小适配器把跨域路由合进来，不要 hack `parse_docs_html` 的前缀。

---

## 7. CI 校验门禁顺序

**当前 `.github/workflows/build-epub.yml` "Validate EPUBs"** 步骤：

1. mimetype 检查
2. `walk_chapters()` 的 `blocking_defects`（破图 / `unlinked_page_title`）
3. **对每个 dist/*.epub 跑一遍 `check_epub.py`**（含 `_check_cover_title()` 反向标题门禁）

任何一步失败即不发布到 gh-pages。第 3 步是新加的——它是封面标题串号事件的回归门禁。`check_epub.py` 本地与 CI 用同一份脚本，不要复制一份到 workflow 内联。