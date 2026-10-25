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

**怎么防止复发**：任何 docs vendor 都可能在示例里给形似真实的 key（OpenAI `sk-...` / Anthropic `sk-ant-...` / xAI `xai-...` / AWS `AKIA...`）。push 前用 `git diff --cached | grep -E "(sk-[A-Za-z0-9]|xai-[A-Za-z0-9]|AKIA[0-9A-Z]{16})"` 自检；CI 端若漏过，本地 push 兜底。**注意：手工替换语料里的占位 key，下一次 refetch 会被原样抓回来**（gemini 的 `ghp_xxx…` 占位符修了两轮才发现这个规律）——替换后要么把该页路由记进「每次 fetch 后重放」清单，要么接受它并在每轮 fetch 后重跑 `scripts/sanitize_corpus_html.py` 检查。

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

---

## 8. devsite 系站点（ai.google.dev / developers.google.com / firebase / cloud docs）四连坑（gemini vendor，2026-08-31）

**症状**：`add https://ai.google.dev/...` 直接 fetch 失败或 0 路由；抓下来了 EPUB 里 `leftover_markdown_fence` 门禁红。

**根因（三个独立问题，按层各修一处）**：

| 层 | 问题 | 修法 |
|---|---|---|
| `http.py` | devsite 用 Set-Cookie + 自重定向（`signin_details` cookie），urllib 无 cookie jar 时 302 无限循环 | `_OPENER = build_opener(HTTPCookieProcessor(CookieJar()))`，fetch 走同一 opener |
| 语料/适配器 | devsite 的 `.md` 孪生页返回的是**HTML**（不是 markdown），且部分页面（如 `gemini-api/docs/files`）在表格单元格里内嵌**裸 markdown 片段**（线上靠 JS 渲染） | 适配器不依赖 llms.txt，从 HTML 导航收集路由；围栏污染由打包层兜底（见下） |
| `page.py`（打包层不变量） | ① `<devsite-code>` 自定义元素被 pandoc 当内联元素，内部 `<pre>` 摊平成 `<br>` 段落；② pandoc 3.x 的 html reader 把**裸 `<pre>`（无 `<code>` 子元素）**解析成 LineBlock 而非 CodeBlock——两者都会让 pre 里的 ``` 泄漏进正文，触发 `leftover_markdown_fence` | `sanitize_body_html`：解包 `devsite-code`/`devsite-selector`；裸 `<pre>` 一律补包 `<code>`；散文文本节点里的成对行首围栏提升为 `<pre><code>`，悬挂围栏删围栏行（`promote_markdown_fences`） |

**怎么发现**：`check_epub.py` 的 `leftover_markdown_fence` 只在 pre/code 之外搜 ```——先 grep 成品 xhtml 定位围栏 DOM 位置，再用 pandoc `-t native` 对最小片段看 AST（CodeBlock vs LineBlock），不要猜。

**怎么防止复发**：新 vendor 若是 devsite 系（页面自带 `devsite-*` 标签），先 `curl -c/-b` 验证 cookie 循环；成品跑 `check_epub.py`，fence 红了先查 `<pre>` 是否有 `<code>` 子元素。

---

## 9. blog.google 没有 /blog/<slug> 结构

`generic_blog.parse_blog_html` 只认 `/blog/<slug>` 路径，而 blog.google 的 Gemini 文章分布在 `products-and-platforms/products/gemini/`、`innovation-and-ai/products/gemini-app/`、`innovation-and-ai/models-and-research/gemini-models/` 等分区。做法与 xai bot/guides 同构：适配器自己抓 `https://blog.google/en-us/sitemap.xml`，按分区前缀过滤 `<loc>`（gemini adapter 内 `parse_gemini_blog`）。sitemap 分区清单会随站点 IA 改版漂移，增量抓取时留意 Blog 章数突变。

---

## 10. 增量 skip 是「缓存完整性」不是「线上新鲜度」（2026-08-31 审计）

**症状**：`fetch` 报 `skipped=247`（cursor）容易被读成「站点无更新」。实际只证明本地缓存没坏。

**根因**：`compile.py load_one()` 的 skip 判据是
`prev[route] == content_hash(cached) and not _looks_missing and not runtime_source`
—— 命中即**完全不发网络请求**。页面级线上漂移对指纹命中的页不可见；列表级变化靠 llms.txt 重抓才能发现（路由增删），页面内容改了但路由没变时，只有运气好才会被重抓。

**怎么发现**：claude 6 页（settings 等）每轮都 fetched=6。用
`fingerprint.content_hash` + `mdx.looks_like_runtime_source` 逐项复算，6 页全部
`fp_match=True, runtime_source=True`——文档里合法的 `export const`/`useMemo`
示例代码触发了 MDX 运行时源码误判，使这些页**永远不满足 skip**、每轮重抓。
它们「总是最新」是误判的副产物，不是漂移检测。

**怎么修（语义层）**：「补齐到今天/确保最新」的任务必须二选一：

1. `python3 -m sites_epub fetch --id <id> --refetch`（忽略指纹全量重拉，页面级真最新）；
2. 或先做证据检查：线上 llms.txt 与 `corpus/llms.txt` md5 一致 + `fetched=0`，
   才能下「无更新」结论（cursor 8.31 即用此法证明）。

**怎么防止复发**：交付「更新到最新」类任务时，报告里必须写明证据是
`--refetch` 还是 `llms.txt md5 一致`；两者都没有的 `skipped=N` 不能当新鲜度证据。
runtime_source 误判**不要修**——它让含 React 示例的页面保持每轮重抓，
对新鲜度是净收益；修掉反而扩大盲区。

---

## 11. EPUB 超 100MB 在 gh-pages push 才爆

**症状**：CI 的 Pack / Validate 全绿，"Publish gh-pages" 被 remote rejected：`GH001: File gemini.epub is 127.70 MB; this exceeds GitHub's file size limit of 100.00 MB`。

**根因**：Google 文档插图多且大（gemini 语料图 178MB/1761 张），打包门禁只查「破图/未链标题」，不查体积；失败点在最后一刻的 push，浪费整轮 CI。

**怎么修**：
1. 语料图就地重压：>400KB 的位图（跳过 .gif）转 JPEG q80、宽≤1400，**改名换扩展名并同步 `image-map.json` 的 value**（URL 不变，页面源零改动）——gemini 178.6MB→97.4MB，EPUB 127.7MB→54.9MB。
2. `downscale_image_bytes` 补 PIL 兜底（原 sips 是 macOS-only，Windows 抓取时 >2.5MB 的图会被静默丢弃）。
3. workflow "Validate EPUBs" 加体积门禁 `< 98MB`，让超标在 validate 步就爆，不拖到 push。

**怎么防止复发**：新增图片大户（产品文档站带大量截图）后，push 前本地 `pack --id <id>` 看一眼 dist 体积；CI 体积门禁已兜底。

---

## 14. epub.zenheart.site https 问题（2026-09-16 深度审计）

**症状**：用户报告线上 epub 站 https 报错（"该网站的安全证书有问题"/"您的连接不是私密连接"等），但 GitHub Pages 配的 `epub.zenheart.site` cert 应由 Let's Encrypt + Fastly 自动签发。

**深度审计（E 层，2026-09-16）**：

| 入口 | 状态 | 实际原因 |
|---|---|---|
| `https://epub.zenheart.site/changelog.html` | 200 OK，cert 有效 | 当前主链无故障 |
| `https://zenheart.github.io/changelog.html` | **301 → `http://blog.zenheart.site/changelog.html`** | GitHub Pages 兜底仓是 `zenHeart/blog`，301 跳到 `http://blog.zenheart.site`，目标非 https → 浏览器在中间环节（未真正到 epub 站）就告警 "mixed content / 不安全" |
| `https://epub.zenheart.gitee.io/` | **404 Not Found**（Server: ADAS/1.0.214 百度云） | Gitee Pages 仓库未配 `epub.zenheart.gitee.io` 自定义域；外加 Gitee 默认没对该子域签证书 → 客户端会看到证书错误或 DNS 不存在 |
| `https://epub-zenheart-site.pages.dev/`（Cloudflare Pages 历史） | 200 OK | Cloudflare Pages 默认 *.pages.dev cert 有效；残留 10 分钟缓存，**本身不是 https 病** |

**真正的根因（不是 github pages 配错，是另两条链断）**：

1. GitHub Pages 兜底链：用户输错主域或旧链接时落到 `zenheart.github.io`，301 跳到 `blog.zenheart.site`，该子域当前以 `http://` 配的，无 cert 覆盖 → 浏览器先看到"重定向到不安全链接"再告警。
2. Gitee Pages 镜像：完全没配 `epub.zenheart.gitee.io` 自定义域，也无该子域的 cert → 404（DNS 解析到百度云但 SNI 无 cert 匹配 → 浏览器先报证书错后看到 404）。
3. Cloudflare Pages `*.pages.dev` 子域残影：曾用 cloudflare 部署过同名项目，缓存还在；非故障，只是误诊噪声。

**怎么修（2026-09-16 起）**：
- `blog.zenheart.site` 的 301 来源侧改为强制 https（GitHub Pages repo `zenHeart/blog` 的 `enforce_https` = true；如果还跳 http，说明 Pages 站 settings 未开 enforce https——去 settings 勾选）。
- Gitee Pages：要么完整镜像 epub 仓到 `epub/zenheart.gitee.io` 并在 Pages 申请该自定义域 + 证书，要么从所有 README/书签里清除 `epub.zenheart.gitee.io` 入口避免用户拿到 404。
- 清理 cloudflare 旧项目，终止 `*.pages.dev` 残影（可选，cache 600s 自然过期）。

**怎么防止复发**：
- 跨镜像部署时，必须保证每条链的 cert、CNAME、enforce_https 三者齐备。E 层审计脚本 `tools/cname_audit.py`：命中 `epub.zenheart.site` 主域之外的所有镜像链（含 301 重定向终点），要求返回 200 且 cert 主体匹配，否则拒绝合并。
- 完整 `enforce_https` 检查列入 publish gate。

## 15. `epub.zenheart.site` https 错的根因（用户报，2026-09-16 E 层定证）

**症状**：用户访问 `https://epub.zenheart.site/...` 时浏览器报"该网站的安全证书有问题/连接不是私密连接"。curl 用严格 TLS 校验直接 `CERTIFICATE_VERIFY_FAILED: Hostname mismatch`。

**E 层定证**（`openssl s_client`）：
```
subject=CN=*.github.io
issuer=C=US, O=Let's Encrypt, CN=YR1
SAN: *.github.com, *.github.io, *.githubusercontent.com, github.com, github.io, githubusercontent.com
```

SAN 列表中 **`epub.zenheart.site` 不在**。Fastly 在 CNAME 模式下默认回退到 `*.github.io` 通配符 cert,通配符只覆盖 `github.io`,**不覆盖** 任意用户自定义子域。客户端(浏览器/严格 curl)校验 SNI 主机名与 cert SAN 不匹配即拒绝。`blog.zenheart.site` 拿的是单域 cert(有 SAN = `blog.zenheart.site`),正常;只有 **epub.zenheart.site 这条** 中招。

**根因(不是 github pages 配错)**：GitHub Pages 不会为新加的自定义域**自动**签发 LE 证书,需要 Pages 控制台里:
1. 进入 `zenHeart/sites-epub` repo → Settings → Pages
2. Custom domain 输入 `epub.zenheart.site` → Save
3. 勾选 "Enforce HTTPS"——这一步触发 Let's Encrypt 签发 `epub.zenheart.site` 的单域 cert
4. 等待几分钟,GitHub Pages 后台完成 LE 签发 + 部署
5. 用 `tools/cname_audit.py` 复验,SAN 列表会从 `*.github.io` 变为 `epub.zenheart.site`

**为什么**之前 curl 200 OK + 现在的 fail:有些 TLS 客户端(老 curl / 部分 `requests`)在 SAN mismatch 时**仅告警不阻断**(默认 `verify=False` 或 `check_hostname=False`),所以历史脚本/GHA 都返回 200,误以为健康;严格客户端(浏览器、Python `ssl.CERT_REQUIRED`、新 curl)直接拒绝。本仓审计工具的 stdlib `ssl.create_default_context()` 就是严格的——这才是"真"健康判定。

**怎么修**：
- 在 zenhHeart GitHub Org 控制台里把 `epub.zenheart.site` 加入 `sites-epub` 的 Pages 自定义域并勾选 Enforce HTTPS(本仓代码无法操作,需人工一次,约 5 分钟)。
- `epub.zenheart.gitee.io`:Gitee Pages 必须显式申请该自定义域并通过审核才会签单域 cert;否则**直接**从 README/书签/CNAME 文件里删 `epub.zenheart.gitee.io`,避免用户撞上不签 cert 的 404。
- `epub-zenheart-site.pages.dev`:Cloudflare Pages 项目已弃用,`*.pages.dev` 通配符仍然有效(8.1 测试可访),无需处理,残影 600s 缓存自然过期。
- `zenheart.github.io` 与 `blog.zenheart.site`:404,默认兜底仓已变;若不需要可忽略。

**怎么防止复发**:
- `tools/cname_audit.py` 列入 release 前置检查(CI "Validate EPUBs" 之后跑一次),SAN mismatch 立即 fail。
- 新增自定义域前,**先**勾 Enforce HTTPS 让 LE 签出 SAN cert,再用 audit 工具复验,才允许 commit。 存进语料（2026-08-31 gemini 重写）

**症状**：成品书目录（nav.xhtml/toc.ncx）一批标题是 `�` 垃圾字符，ncx 里还带 `\x08\x00\x00` 二进制前缀；用户报「书籍目录有乱码」。walk 门禁没拦——乱码文本长度超过 `empty_or_stub_body` 的 40 字符阈值。

**根因**：antigravity.google 对不带 `Accept-Encoding` 的 urllib 请求也返回 **gzip 压缩体**（`1f 8b 08` magic）。`http.fetch_text` 直接 `decode("utf-8", errors="replace")`，压缩字节里的非法序列全变成 U+FFFD 存进 corpus/pages——16 个 antigravity 页面（含 CLI 章节）标题与正文全是乱码。

**怎么发现**：对 nav.xhtml 做非 ASCII 字符盘点（`Counter` 出 167 个 U+FFFD 即实锤）；对 corpus 逐文件 `read_bytes().count(b"\xef\xbf\xbd")` + 查文件头定位压缩 magic，不要猜编码。

**怎么修**：`http.fetch_bytes` 请求头显式 `Accept-Encoding: gzip`（明确排除 stdlib 解不了的 brotli），响应按 `Content-Encoding`（或 gzip magic 兜底）用 `gzip.decompress`/`zlib` 解压后再返回。

**怎么防止复发**：任何源站可能强制压缩；新增 vendor 后对语料跑一次 U+FFFD/magic 扫描（`work/find_mojibake.py` 思路）。解压必须在 http 层做，语料层不可能恢复已丢失的字节。

---

## 13. markdown 表格行内压扁的围栏（coze，2026-09-16）

**症状**：check_epub 报某章 `leftover_markdown_fence`，但源页围栏不在独立行——`| ...正文... |```JSON |\`，围栏标记被压进**转义管道表的行内**。

**根因**：站点导出的 .md 把表格 + 单元格内代码块折叠成单行；pandoc 管道表逐格渲染，格内围栏变成字面 ``` 泄漏进正文。行级「裸围栏」正则（§8 的 `promote_markdown_fences`）匹配不到行内形态。

**怎么修**：对以 `|` 开头且含 ``` 的行，行内剔除 ```` ```lang ```` 标记（保留格内代码文本）——coze `cozeloop_create-dataset` 即此修法。手工语料修会被 refetch 带回（§4 规律），重抓后需重放。

**怎么防止复发**：新 vendor 门禁红 `leftover_markdown_fence` 时，先 repr 打印围栏行确认形态（独立行 vs 行内压扁），再选对应修法，不要盲改正则。

---

## 16. claude.com 博客从 Webflow 迁到 RSC：正文选择器与 canonical URL 一起换（2026-10-09）

**症状**：`claude.com/blog` 整体 308 到 `/resources/articles`；243 条博客路由的 `html_url` 全部指向已死的 `/blog/<slug>`，缓存里还是 9-16 的旧 HTML。`blog_article._collect_body_blocks` 的三个 Webflow 选择器在新页命中数全为 0（`blog_post_content_wrap` / `u-rich-text-blog` / `hero_blog_post_details`）。

**根因**：站点换框架，三处契约同时断：
1. **URL 契约**：`/blog/<slug>` → `/resources/articles/<slug>`，`normalize_blog_url` 只认老路径，收到的全是重定向；
2. **正文契约**：Webflow 的 `blog_post_content_wrap > .u-rich-text-blog.w-richtext` 外壳没了，但 `w-richtext` 这个 class 被保留下来挂在正文 div 上（新页 `article` → `BlogPostDetail-*-bodyWrap` → `grid-12` → `ArticleLayout-*-content` → `.w-richtext`，实测单块 3192 字）；
3. **元数据契约**：`.hero_blog_post_details` 是唯一的日期/作者来源，新页没有；但每篇都发了 `ld+json` 的 `BlogPosting`（`datePublished` / `headline` / `author`）。

**怎么发现**：先 `curl -sSL https://claude.com/blog | head` 看跳转，再用选择器逐个计数（命中 0 就是契约断了，不是内容空），最后 `soup.select_one(".w-richtext")` 验字数。

**怎么修**（`blog_listing.py` / `blog_article.py`）：
- `BLOG_PATH` 改成 `^(?:/blog|/resources/articles)/<slug>$`，`normalize_blog_url` 一律输出 canonical `https://claude.com/resources/articles/<slug>`——老链接和 sitemap `<loc>` 因此自然去重成同一个 URL；**route 仍是 `blog/<slug>`、group 仍是 `Blog`**，Blog-last 不变量不因 URL 迁移而破。
- `_collect_body_blocks` 的选择器链末尾追加 `article .w-richtext` 与 `.w-richtext`。链是「命中即返回」，老页面仍在前三个选择器上短路，行为不变。
- 新增 `_ldjson_article()`：展平 `@graph` 后找第一个 `BlogPosting/Article` 节点，作为 published / author / dek 的兜底；`CHROME_SELECTORS` 追加 `[class*="RelatedPosts-module"]` 等 CSS-module 子串选择器，清掉新页 chrome。

**枚举源要换**：新列表页只渲染 7 篇文章，`<a>`/payload 扫不到全量；`fetch_vendor` 本来就把 `sitemap.xml` 拼在 `blog_html` 后面，`extract_blog_urls` 的 `<loc>` 分支因此直接吃 sitemap——**根语言 `/resources/articles/` 下 257 条，列表页 7 条**。i18n 镜像（`/de/resources/articles/…`）由 host+路径前缀一起挡掉。

**怎么防止复发**：框架迁移期先验「选择器计数 + canonical URL 状态码」两个数，别先改代码；canonical 化只改 URL、不改 route/group，Book-last 与语料文件身份都不受影响。

---

## 17. SSR 里的博客 slug 消失后，sitemap 是唯一可靠枚举源（kimi，2026-10-09）

**症状**：`kimi_nav.parse_kimi_blog` 在 SSR 文本里扫 `/blog/<slug>`，实测归零，基线 21 条路由掉到 17 条。更隐蔽的是 `docs_url=https://www.kimi.com` 的首页**静默缩水**：只剩 8 个 `<a>`，产品家族里 `/agent-swarm` `/sheets` `/design` `/build` 全部不再出现在首页锚点里，`parse_docs_html` 就此少收 6 页——`fetch` 报 `ok:true`，不比对基线就看不出丢了东西。

**根因**：两个枚举面同时失效，而 kimi 的「产品页」根本不在 sitemap 的 `/docs/` 下——它在站点根。sitemap 只有 22 条 loc，其中一半是 `/en/*` 镜像。

**怎么发现**：拿 `git show <上一笔>:vendors/<id>/corpus/routes.json` 的路由数当基线，逐条 live 探；只看 `fetch` 的 `ok:true` 会漏掉这种静默缩水。

**怎么修**（`kimi_nav.py` 重写）：
- **枚举**：sitemap 根语言 `<loc>`（剔 `/en/*`、`/zh/*` 镜像）∪ 首页锚点 ∪ `/products` 产品家族页链接爬取。第三个来源是关键——`/code` 与 `/products/kimi-work` 只在 `/products` 上有链接，首页和 `/docs` 都没有；且 Next.js 导航一部分以转义 JSON 形式存在，锚点正则和 payload 正则都要扫。
- **canonical**：`/blog/<slug>` 现在 302 到 `/en/blog/<slug>`，博客路由一律用 `/en/blog/<slug>`，`/websites` 302 到 `/build`，路由改名为 `build`。
- **索引页斜杠**：`/products` `/features` `/ai-models` `/academy` 只对 `/hub/` 形式返回 200，裸 `/hub` 是 308——`KIMI_INDEX_PATHS` 显式补尾斜杠。
- **范围**：`KIMI_OUT_PREFIXES` 把 `/capabilities` `/use-cases` `/showcases` `/resources`（SEO 用例与内容营销 hub）、`/solutions` `/business` `/membership`（销售与定价）逐条列出，排除是可审计的而不是隐式的。前缀带不带尾斜杠语义不同：带斜杠覆盖子树和自己的索引页，不带只覆盖自身与子路径。

**怎么防止复发**：新增/复测 vendor 时，枚举源至少要有两个（sitemap + 一个产品家族页），并在报告里写清 before→after 路由数；路由改名要连同 301/308 的 `Location` 一起核对，别只改名字。

---

## 18. 98MB 门禁下压体积：递归重压直到每张图都在阈值内（zencoder，2026-10-09）

**症状**：zencoder 语料图 266MB，EPUB 远超 CI 的 98MB 门禁，`pack` 能在本地跑完但 push 阶段才炸。

**根因**：`shrink_corpus_images.py` 的默认档（>400KB 转 JPEG q80、宽≤1400）压一轮仍有超限图留在包里；zencoder 一次 refetch 带回 7380 张博客图，单轮压不下来。

**怎么修**：**递归重编码**——每轮重新统计仍超过阈值的图，按更小的宽/更低的质量再压一轮，循环到没有超限项。2026-09-16 实测：递归 JPEG 重编码 720px/q65，盘上省 1.07GB，`zencoder.epub` 266.3MB → 48.5MB，门禁通过，章节数不变。每轮都要同步 `image-map.json` 的 value 与文件名扩展名（URL 不变，页面源零改动）。

**怎么防止复发**：CI 的 98MB 门禁是最后一道，体积要在本地 `pack --id <id>` 就看到；重压脚本要幂等——同一张图重复压只会掉画质，不会掉体积。

---

## 19. 语料里的示例 token 与 GitHub push protection（2026-10-09 处置流程）

**症状**：`git push origin main` 被 GH secret-scanning / push protection 拦下，命中路径在 `vendors/<id>/corpus/**`。

**处置流程**（与 §4 同源，这里是完整闭环）：
1. **先本地扫再推**：`git diff --cached | grep -nE "xai-[A-Za-z0-9]{20,}|sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}"`。命中行号就是待替换位置。
2. **就地替换占位符**：保留厂商前缀的形状（`xai-YOUR_API_KEY_HERE`），让文档示例仍然可读，同时不匹配任何 key 正则。
3. **`git commit --amend --no-edit`** 就地改写，**不要**追加一笔「修 token」的提交——历史里那笔仍然会被扫描。
4. **重推**；仍被拦则回到第 1 步（push protection 的命中是一次性全部返回，不是逐个）。
5. **接受「会被 refetch 带回」**：手工替换会被下一次 `--refetch` 覆盖（§4 规律）。要么把该页记进「每次 fetch 后重放」清单，要么每轮 fetch 后跑 `scripts/sanitize_corpus_html.py` 复查。**不要**为此改适配器去剥离语料里的示例——示例代码是文档价值的一部分。

**怎么防止复发**：把第 1 步的扫描放进提交前自检清单，和封面标题门禁、`file vendors/<id>/icon.png` 魔数校验并列。

---

## 20. 导航折叠导致的静默掉页：枚举必须有两个面（minimax，2026-10-20）

**症状**：minimax 书 56 → 55 章，`minimax-iomodels-text`（M2.5）与
`minimax-iomodels-text-m27`（M2.7）两页消失，`fetch` 仍报 `ok:true`。

**根因**：`minimax_nav.parse_minimax_docs` 只扫 `/models` 页的 `<a href>`。
站点把模型子菜单改写成 Next.js flight payload 里的
`{\"title\":\"MiniMax M2.7\",\"link\":\"/models/text/m27\"}`，**锚点里不再有这两条**——
但两页线上仍是 200，payload 里也仍然列着。单一枚举面被折叠 = 静默掉页。

**怎么发现**：拿 `git show HEAD:vendors/<id>/corpus/routes.json` 的路由数当基线逐轮对比
（§17 同一规律）；再对掉掉的路由做 live 探——`200` 说明是枚举漏了，不是页面没了。

**怎么修**：`MODEL_PAYLOAD_LINK` 正则从 payload 里同时抓 `title`+`link` 对，
与锚点面**取并集**再生成 route（route 命名规则不变，旧语料文件身份不受影响）。

**怎么防止复发**：枚举源至少要有两个（锚点 + payload / sitemap / 产品家族页），
并把 before→after 路由数写进日报。改动后必须重算 `fingerprints.json`
（§19 之外的第三条链：语料字节变了而指纹没变，下一轮会重抓并覆盖手工修补）。

---

## 21. 源站 403 挑战页 → 0 字节语料 → 打包门禁 "doc body is empty"（zencoder，2026-10-20）

**症状**：CI Build EPUB 在 "Pack catalog vendors (offline)" 步失败，报
`broken images or unlinked titles` / `doc body is empty`；但 `fetch` 全绿。
本机 `pack --id zencoder` 复现：只有 `get-started/community-support` 一页炸。

**根因（两层）**：
1. `docs.zencoder.ai` 对本机代理节点整站返 Cloudflare 挑战页（403 + "Just a moment..."）。
   `http.fetch_bytes` 对 403 重试 3 次后抛异常，`fetch_source` 把两个异常都吞掉、
   返回 `""`。
2. `compile.load_one` 无条件 `dest.write_text(text)` → 写出一个 **0 字节**语料文件，
   同时该路由仍留在 `routes.json` 里。打包时 `page.extract_page` 对空正文抛
   `ValueError("doc body is empty")`，`run_pack` 记 `ok:false` → `cmd_pack` 退出码 1。

**怎么发现**：`git log` 显示该路由是**上一轮**新增且当轮没推送——所以当轮 CI 从没
pack 过它，问题延迟到下一轮才暴露。**没推送的语料提交 = 没被 CI 验过**。

**怎么修**（`compile.py`，fetch 侧，不改打包器语义）：
- `load_one`：fetch 回来空正文时，**不覆盖已有的好缓存**（站点临时故障不该毁掉好语料）；
  没有好缓存就删掉空文件，把路由交给上层丢弃。
- `fetch_vendor`：正文为空的路由从 `entries`/`routes.json`/`sources` 里一起剔掉
  （0 字节章节会让门禁每轮都红，而源站仍会在 llms.txt 里继续广告这个路由）。

**怎么防止复发**：
- 语料里不允许有 0 字节页：`find vendors/*/corpus/pages -name '*.md' -size 0` 应为空。
- 源站整站 403/挑战时，抓取会「静默成功」但正文为空——**路由数与正文数要分开核对**。
- 改 `compile.py` 会在 `PACKER_FILES` 里，**12 本书全部重打**；改之前先本地
  `pack --id <id>` 逐本验（`pandoc` 在 `/usr/local/bin/pandoc`）。

---

## 22. srcset 按逗号切分 → 伪图片 URL → 抓取空转（grok，2026-10-20）

**症状**：`fetch --id grok` 挂 23 分钟才返回，`fetched=0, skipped=337`（语料其实
一点没变）。抓取期间 `corpus/images/` 一张新图都不落地，进程 90% 时间卡在
`_ssl__SSLSocket_do_handshake`，`lsof` 里堆满到 Clash 代理 7890 端口的
CLOSE_WAIT 连接。

**根因**：`images.collect_image_urls` 把 `srcset` 按 `,` 切：
```python
for part in srcset.split(","):
    token = part.strip().split(" ")[0]
```
但 xAI 的 CDN URL **路径里就带逗号**：
`https://media.x.ai/cdn-cgi/image/fit=scale-down,onerror=redirect,f=auto/v1/website/hero.jpg`
于是每个图被切成 3 段，后两段被 `normalize_image_url` 拼成**伪 URL**：
`https://docs.x.ai/<当前页路径>/onerror=redirect`、`.../width=320`、`.../height=320`。
这些伪 URL 一律 403/404，每条走满 3 次重试。grok 语料引用 2460 个图片 URL，
其中 **1354 个**是这类伪 URL —— 一次 grok 抓取凭空多出 1350 次无效网络请求。

**怎么发现**：
- `lsof -nP -a -p <pid> -iTCP` 看连接数是否只涨不落；
- 把「页面引用的图片 URL」和「`corpus/image-map.json`」做差集，多出来的就是伪 URL；
- 直接 `curl` 一个伪 URL 看状态码（403/404 + 路径里带 `onerror=redirect`）。

**怎么修**（`images.py`，**改前先本地 `pack --id <id>` 逐本验**）：
srcset 必须按 WHATWG 规范解析——**URL 以空白结束，不是以逗号结束**：
```python
tokens = srcset.split()
i = 0
while i < len(tokens):
    url = tokens[i]; i += 1
    if url.endswith(","):
        url = url.rstrip(",")
    else:
        if i < len(tokens) and not tokens[i].startswith(","):
            i += 1                      # descriptor（如 640w）
        if i < len(tokens) and tokens[i].startswith(","):
            i += 1
    yield url
```

**怎么防止复发**：新增/复测 vendor 时，若其图片 URL 含 `,`（Cloudflare
`cdn-cgi/image/fit=...`、某些 Vercel/Shopify 变体），抓取耗时会异常；
抓取超过 10 分钟没新图落地时，先查是不是伪 URL 撑起来的。`images.py` 在
`PACKER_FILES` 里，改动会让 12 本书全部重打。

---

## 23. 打包键被噪声搅动 → 每天白重打 9~11 本书（2026-10-20）

**症状**：CI Build EPUB 每轮都要 20+ 分钟（pack 15 分钟），即使当天只有 1 本书
的内容变了。逐本比对 `git diff HEAD -- vendors/<id>/corpus/` 才发现：
**9 个厂商的 `corpus/image-map.json` 与 2 个厂商的 `corpus/llms.txt` 变了**，
但内容其实一个字没变。

**根因（两处）**：
1. `compile.py` 写 image-map 用 `map_path.write_text(json.dumps(image_map, indent=2))`
   —— **不写结尾换行**，而仓库里已提交的文件都带换行。于是每轮 fetch 都把
   9 个厂商的 image-map 末尾换行剥掉，git 就报「已修改」。
2. `corpus/llms.txt` 存的是站点索引页原文，里面嵌着 **Next.js build id 与
   `dataUpdatedAt` 时间戳**（kimi：`dataUpdatedAt:1792429889639` → `1792445408414`；
   minimax：`21:20:37.138Z` → `21:31:33.832Z`）。每轮必然变。

而 `pack_cache.vendor_pack_key` 会 **哈希 corpus 下每一个文件**
（`for path in sorted(p for p in corpus.rglob("*") if p.is_file())`），
所以这两种噪声都会改打包键 → 整本书重打。skill 里「语料没变的书复用上次 EPUB」
的意图被噪声打穿了。

**怎么发现**：`git diff --name-only HEAD -- vendors/<id>/corpus/` 列出变化的
corpus 文件；再用 `head.endswith(b"\n")` 与 `json.loads()` 比对内容是否真变。

**怎么修**：
- 立刻可用（不改代码）：fetch 后把**只有结尾换行差异**的 image-map.json 恢复成
  HEAD 的字节（`git checkout --`），把只差 build id/时间戳的 llms.txt 也恢复——
  两者都不参与打包内容（`pack_vendor` 不读 llms.txt；image-map 只存映射关系）。
  这样当天只有真变了的书会重打。
- 根治（要动 `compile.py`）：`map_path.write_text(json.dumps(image_map, indent=2) + "\n")`；
  llms.txt 的噪声要么在写盘前抹掉，要么把 `corpus/llms.txt` 排除出打包键。
  **改 `compile.py` 属于 `PACKER_FILES` 变更 → 12 本书一次性全部重打**，
  按 §21 的要求先本地逐本 `pack --id <id>` 验。

**怎么防止复发**：日报里报告「哪几本会重打」（= 真有 corpus 内容变化的那几本），
而不是「fetch 了几个厂商」；两者不是一回事。

---

## 24. fingerprints 重算要用「活跃路由」，不是「全部页面文件」（2026-10-20）

**症状**：`workflow.md` 的指纹重算片段用
`(corpus/"pages").glob("**/*.md")` 全量枚举，于是把**孤儿页**（路由早已从
`routes.json` 删除、但 `.md` 还留在磁盘上）也写进 `fingerprints.json`。
而 `fetch_vendor` 的 `save_fingerprints` 只写**活跃路由**（`sources` 的 key）。
两套语义打架：跑完维护脚本后，路由数 500 的 cursor 会拿到 505 条指纹。

**为什么重要**：`fetch_vendor` 写指纹时按活跃路由裁剪，等于每轮自动清理孤儿指纹
（2026-10-20 一次清掉 120 条：gemini 29 / zencoder 25 / grok 23 / manus 15 /
tencent 9 / claude 7 / cursor 5 / kimi 5 / minimax 2）。但维护脚本的重算片段
会把它们**加回来**，两轮之间反复横跳，diff 全是噪声。

**怎么修**：重算指纹时按 `routes.json` 的活跃路由取页面，别 glob 全部文件：
```python
routes = {r["route"] for r in json.loads((corpus/"routes.json").read_text())}
fp = {r: content_hash((corpus/"pages"/f"{r}.md").read_text(errors="replace"))
      for r in sorted(routes) if (corpus/"pages"/f"{r}.md").is_file()}
save_fingerprints(corpus.parent/"fingerprints.json", fp)
```

**怎么防止复发**：删指纹前先确认该 key 不在 `routes.json` 里——**指纹数应等于
活跃路由数**；对不上就是有孤儿。注意 `corpus/pages/` 里的孤儿 `.md`（2026-10-20
共 9 个厂商 120 个，约 2.7 MB）目前无人清理：它们不进打包内容（`pack_vendor`
按 `routes.json` 出章），但仍参与打包键哈希。

---

## 25. 本机 pack 与 CI pack 会分歧：gemini 本地出「塌陷书」，CI 出正常书（2026-10-21）

**症状**：本地 `pack --id gemini` 报 `ok:true, chapters:500`，但成品只有 1.9MB /
3 个 xhtml / 1257 个 section / 219 张图；同一天 CI 产出的线上 `gemini.epub` 是
24.3MB / 10 个 xhtml / 5506 个 section / 883 张图。本地正文只剩 **17%**。

**根因**：不是语料问题，是**本机 pandoc（3.12.1）与 CI pandoc 的 HTML reader 行为差异**。
gemini 语料是 devsite 系整页 HTML，`book.html` 里大量重复 id（pandoc 打出成百条
`Duplicate identifier 'whats-next' / 'next-steps' / 'antigravity-cli'` 警告），
本地 pandoc 3.12.1 对这种嵌套结构会塌成单章并丢掉大部分图；CI 的 pandoc 正常分章。
**A/B 证据**：把上一笔提交（语料完全相同的前一天）checkout 到独立 worktree 用同一条
命令打包，产物字节数与 section 数几乎完全一致（1,631,230 text bytes / 1257 sections
两边相同）——证明与当天语料改动无关。

**怎么发现**：别只看 `pack` 返回的 `ok:true`；要**同时看产物体积与 xhtml 数量**。
`walk_chapters` 在塌陷书上会报 `chapter_count 0 / fail_count 0 / ok True`——**空跑也绿**，
所以 `check_epub.py` 在本地 gemini 上是假通过。

**怎么防止复发**：
1. 本地 pack 预演只对 **cursor / grok / claude** 等可信；**gemini 只能由 CI 判**。
   2026-10-21 实测：cursor 27.5MB/502 章、grok 47.7MB/338 章、claude 52.1MB/505 章，
   与线上体积一致；只有 gemini 塌。
2. 预演结论不要外推到 gemini：CI 才是门禁，gemini 的健康度以 CI 产物为准。
3. 排查「本地包变小」时，先做 worktree A/B（`git worktree add --detach` 上一笔提交
   再打包），能立刻区分「语料改坏了」与「工具链分歧」。

> **2026-10-25 更正**：本节把根因归给「本机 pandoc 与 CI pandoc 的 reader 差异」，
> **这个判断是错的**。真正的根因是语料里的 `role="main"`（见 §28）——它让
> pandoc 的 reader 丢弃标题前的所有内容。2026-10-25 实测 CI 同样塌陷，
> 且在打包器里删掉 `role="main"` 后，**本机 3.12.1 也能打出 24.5MB 的正常书**，
> 本机/CI 的「分歧」并不存在。§28 另附了逐值实测表与 3 分钟复现脚本。

---

## 26. srcset 逗号切分 bug 的影响面已量化，修法待择时（2026-10-21）

**状态**：§22 的 WHATWG srcset 解析修法**仍未落地**，`images.py` 仍是
`for part in srcset.split(",")`。2026-10-21 实测 grok 抓取耗时 **1508s（25 分钟）**，
`fetched=1, skipped=337`，全程零新图落地。

**影响面（按 image-map 实测统计，逗号 URL 只在两个厂商）**：

| 厂商 | 图片总数 | URL 含逗号 | 形态 | 修 srcset 后的净效果 |
|---|---|---|---|---|
| grok | 1974 | 274 | `media.x.ai/cdn-cgi/image/fit=scale-down,onerror=redirect,f=auto/...` | 去掉伪 URL（每轮约 1350 次无效请求） |
| minimax | 371 | 144 | `filecdn.minimax.chat/...?x-oss-process=image/format,webp`（逗号在 query） | 保住完整 URL，可能多收几张 webp 变体 |
| 其余 10 家 | — | 0 | — | 解析结果与现状**完全一致** |

**为什么还没改**：`images.py` 在 `PACKER_FILES` 里，一改就是 **12 本书全量重打**
（CI 约 25~30 分钟），而且会让从未近期重打的书也进一次打包通道——收益是每天省 20 分钟
抓取时间，代价是一次全站重建 + 未预期回归风险。属于需要显式择时的运维决策，
不适合在例行增量抓取里顺手做。

**怎么择时**：建议单独一个「只做这件事」的变更窗口：改 `images.py` → 本地
`pack --id grok` 与 `pack --id minimax` 验体积（grok 线上 47.4MB、minimax 26.5MB，
离 98MB 门禁都很远）→ 提交 → 盯 CI 全量重打 → 确认 12 本都绿再收工。

---

## 27. 导航控件从 `<select>` 换成客户端渲染的 island：codex 抓取整体断掉（2026-10-25）

**症状**：`fetch --id codex` 直接抛 `Codex six-section nav select not found`，
不是 0 路由而是**整个厂商抓不到**；同一时刻 curl `learn.chatgpt.com/docs` 却是 200。

**根因**：站点把六个分区的下拉框从原生 `<select>` 改成了客户端渲染的
`MobileContextDropdown` astro-island。**变的是「变体 → 分区名」这份映射的载体，
不是变体本身**——`data-variant-id`（`mobile-nav-tab-3-variant-N`）与
`data-mobile-nav-variant-content` 面板原样保留，映射搬进了 island 的 `props`：

```
props="{"options":[1,[[0,{"value":[0,"mobile-nav-tab-3-variant-0"],
                           "label":[0,"Overview"]}], ...]]}"
```

**怎么发现**：先分清「网络挂了」还是「解析契约断了」——`curl` 同一 URL 通、fetch
抛的是解析异常，就不是网络问题；再数 `<select>` 命中数（0）与
`[data-mobile-nav-variant-content]` 命中数（31），面板还在、选择器没了 = 载体换了。

**怎么修**（`codex_nav.py`）：`_variant_sections()` 先走老 `<select>` 分支，
取不到再读 island 的 `props`（astro 把 prop 序列化成 `[type, value]`，数组是
`[1, [...]]`、元素是 `[0, {...}]`，所以 label/value 都要再剥一层）。

**关键点：页面有 4 个下拉框**（API docs / plugins / Codex / blog），
必须**按 label 集合挑** Codex 那一个（`{Overview, Features, Administration}`），
不能取第一个——tab-1 的第一个下拉框是 API 文档的。

**怎么防止复发**：
- 枚举源保持两个面（§17/§20）：`/docs/` 路径仍由 `llms.txt` 决定，
  `canonicalize()` 只改 URL 不改 route/group，语料文件身份不受迁移影响。
- 改动前做 A/B：`git show HEAD:sites_epub/codex_nav.py` 与新版本对同一 fixture
  跑一遍，输出必须逐条相同（本次 144 条全同），再加一条针对新载体形态的回归测试。
- `codex_nav.py` 在 `PACKER_FILES` 里 → 改它 **12 本书全量重打**，
  一次性代价约 25~30 分钟 CI（workflow timeout 45 分钟，够用）。

---

## 28. gemini 的书会「塌陷」成一章：根因是 `role="main"`，不是 reader 的页数上限（2026-10-25）

**症状**：CI 全绿、书也发布了，但线上 `gemini.epub` 只有 **1.9MB / 4 个 xhtml /
1246 个 section / 0 个 h2 / 0 个 doc-page**，正文全挤在一个 `ch001.xhtml` 里；
正常形态是 ~24.5MB / 9 个内容 xhtml / 501 个 h2.page-title / 501 个 doc-page。
目录、章节、切页全废，而用户拿到的是「成功发布」。

**根因（已坐实）**：**pandoc 的 HTML reader 会把带 `role="main"` 的元素当成
「文档正文」，并把它之前的全部内容丢掉。** 塌陷书 `ch001.xhtml` 的开头就是
铁证：

```html
<body epub:type="bodymatter">
<section id="gemini" class="level1 unnumbered">
<h1 class="unnumbered">Gemini</h1>
<div id="hcfe-content" role="main" tabindex="-1">      <!-- ← 元凶 -->
```

`role="main"` 出现在 **body 的第一个元素**上，于是 reader 把它之前的
打包器结构全部丢弃：`<section class="doc-group">` 包装、每页的
`<h2 class="page-title">`、以及每页的 `<div class="doc-page">`。
结果就是：0 个 h2、0 个页面单元、正文全糊成一坨。

**为什么只有 gemini 中招**：gemini 的 support.google.com 页面（176 页）带
`role="main"`；其余厂商带的是 `role="navigation"` / `banner` / `region` /
`dialog` / `presentation` 等，**实测这些都不会触发 reader 丢内容**。
对 pandoc 3.12.1 逐值实测（把元素放在标题前，看标题还在不在）：

| 触发丢标题 | 不触发 |
| --- | --- |
| `role="main"` | `role="navigation"` `banner` `contentinfo` `complementary` `search` `region` `dialog` `alert` `status` `tab` `tablist` `menu` `menubar` `toolbar` `article` `group` `img` `presentation` `list` `listitem` `button` `link` `heading` `none` `document` |
| `<main>` 标签 | `id="main"` `id="content"` `id="main-content"` |

（`<main>` 标签另有它自己的坑，但打包器早就把 `main`/`article`/`section`
降级成 `div` 了，见 `page.py`。）

**修法（放在打包器，不放语料）**：`sites_epub/page.py` 的
`sanitize_body_html()` 里删掉 `role="main"`（token 感知，`role="main
navigation"`、`role="MAIN"` 一并删）。改在打包器而不是语料，是因为
**语料每次增量都会重新抓回来**，只在语料上删等于埋雷。`page.py` 在
`PACKER_FILES` 里 → 12 本书全量重打（约 25~30 分钟 CI）。

**顺带补上门禁盲区**：这次塌陷书**两次**发布都过了 validate，因为
`walk_chapters` 在塌陷书上照样报 `chapter_count 0 / fail_count 0 / ok True`
（`div.doc-page` 全没了 → 一个页面单元都找不到 → 空跑 → 绿的），
`check_epub.py` 也就跟着放过，98MB 门禁只管上限不管下限。
现在 `check_epub.py` 会拿 `vendors/<vendor>/corpus/routes.json` 的条数当
**下限**去卡页面单元数：0 个页面单元直接 FAIL，条数对不上也 FAIL。

**怎么发现**：不要看 CI 结论，要看**产物体积与 xhtml 数量**（§25 的规矩）。
最快的判据是 `git/trees` API 对比两次部署的 epub 大小——
`curl https://api.github.com/repos/<o>/<r>/git/trees/<gh-pages-sha>` 不下载文件
就能拿到每个 epub 的字节数。本次 12 本里只有 gemini 从 24.5MB 掉到 1.9MB。

**怎么复现（本地 3 分钟）**：拿一页带 `role="main"` 的语料，按打包器的形状
拼出 `<div class="doc-group"><h1>..</h1><div class="doc-page"><h2 class="page-title">..</h2>{body}</div></div>`，
喂 `pandoc -f html -t native`：stdout 里有 `doc-group` / `page-title` 才算健康。
本次 176/176 页在删 role 前全部塌陷、删 role 后 0 页塌陷。

**怎么防止复发**：
- **每次增量后都比对 epub 体积**（部署前后各一次），别等用户发现书坏了。
- 打包器里凡是「reader 语义」类的坑，都要用**逐值实测**确认触发集合，
  别凭 ARIA 规范推断（本次差点把 20 个 role 全删）。
- 语料侧根治方向（可选）：gemini 改用 devsite 的 `.md` 双生页（站点有），
  或按 `data-markdown-export` 剥掉整页外壳，别把 devsite 的整页 HTML 当正文存。
- **注意**：`!vendors/*/corpus/**` 这条 gitignore 取反会把 `.DS_Store` 一起放进来，
  已在 2026-10-25 追加 `**/.DS_Store` 重新忽略。

**与 §25 的关系**：§25 记的是「本地 pack 塌陷、CI 正常」，当时猜是「reader 页数
上限」。本次证明 **CI 也塌陷**，而根因与页数无关，是 `role="main"`。
结论要修正为：**塌陷是语料形态 + reader 能力共同决定的，不是某一端的 bug**；
§25 的「本地/CI 分歧」多半也是同一批 `role="main"` 页面在不同 pandoc 版本上的
表现差异，而不是真正的版本差异。

---

## 29. 产品换域名 → 整组章节被静默删掉（minimax，2026-10-26）

**症状**：`fetch --id minimax` 报 `ok:true, fetched=0, skipped=57, entries=57`，
路由数 58 → 57，`MiniMax Code` 这一整个 group 消失，`scope_gate` 报
`route shrinkage 58 -> 57`。**fetch 全绿，不比对基线就发现不了。**

**根因（两层叠加，缺一不可）**：
1. `minimax_nav.py` 的 MiniMax Code 章节是**硬编码种子 URL**
   （`for u in ("https://code.minimax.io/download",)`），不是从导航里枚举出来的——
   所以 §21 的「空正文丢路由」规则会直接把它丢掉，**没有任何备份枚举面能救它**。
2. 产品本身没下线，只是**换了域名**：`code.minimax.io` 整个子域现在返 nginx 404
   （`https://code.minimax.io/` 根路径也是 404），而
   `https://agent.minimax.io/download` **标题一字不差**：
   `Download MiniMax Code for macOS & Windows | AI Coding and Work`。
   `www.minimax.io/models` 里仍然链着 `code.minimax.io/download`（站点自己没改）。

**怎么发现**：
- 路由数 vs HEAD 基线逐轮比对（§17/§20 同一规律）；
- 丢掉的路由做 live 探：`curl -sL https://code.minimax.io/download` → 404，
  body 是**裸 nginx 404**（`<center><h1>404 Not Found</h1></center>`），
  不是应用自己的 404 页 → 说明是**子域/网关层**的问题，不是页面被删；
- 换 UA、换 IP 都一样 → 不是反爬；
- 找同产品的**新域名**：从 `www.minimax.io/models` 的链接里扫出
  `agent.minimax.io/download`，比对 `<title>` 完全一致 → 确认是迁移不是下线。

**怎么修**：把种子 URL 改成新域名，并保留旧域名作 fallback（第一个取到正文的胜出）。
`route` / `group` / 标题规则都不变 → 语料文件身份与章节数稳定。

**怎么防止复发**：
- **硬编码种子 URL 是单点故障**：它没有「第二枚举面」兜底，改域名/下线都会直接
  删掉整节。新增这类种子 URL 时，务必同时准备一个 fallback 域名。
- 丢路由时先判「**是不是空正文被丢**」（日志会打印 `dropped N route(s) with
  empty body`）。空正文被丢 ≠ 路由该消失：可能是源站临时故障（§21），
  也可能是域名迁移（本文）。**先 live 探 + 比对标题，再决定是删还是改种子**。
- 判据固化在 `scripts/scope_gate.py`：`route shrinkage` 直接报 PROBLEM。

---

## 30. 本地算的打包键 ≠ CI 算的：「要重打几本」可以是测量假象（2026-10-26）

**症状**：本轮只有 minimax 一个厂商真有内容变化，但**本地**算打包键得出
「11 本要重打、1 本复用」。按这个结论下判断会误判成大改。

**根因**：`vendor_pack_key` 哈希 `corpus/` 下**每一个文件**，而
`corpus/docs.html`、`corpus/blog.html` 被 `.gitignore` 忽略（fetch 每次写的
路由发现快照），`.DS_Store` 也被 `**/.DS_Store` 忽略。
**本地工作树里有、CI 的 checkout 里没有** → 两边哈希的输入不同 →
本地键和 CI 键必然不等。本机还有 `vendors/gemini/corpus/**/.DS_Store` 同理。

**怎么发现**：在 `git worktree add --detach /tmp/x HEAD` 的**干净 worktree** 里
算键 → 12 本全部与线上 `pack-hashes.json` 一致；同一份代码在主工作树里算 →
11 本不等。差异文件用 `comm` 对比两个 worktree 的 `corpus` 文件清单即可定位。

**怎么防止复发**：
- 判断「哪几本会重打」**要么在干净 worktree 里算，要么只信 CI 结论**，
  不要拿主工作树的本地键下结论。
- 算键时要用 `git ls-files -z` 取文件清单：**非 ASCII 文件名**（`git ls-files`
  默认会 C-quote 成 `"...\345\217\221..."`）会让集合比对静默失配，
  凭空造出「这一本要重打」的假象（本次 tencent / zencoder 就是这么被骗到的）。
- 真正的噪声源另见 §23：`image-map.json` 末尾换行、`docs.html`/`blog.html` 的
  部署号、`llms.txt` 的 build id。已由 `scripts/restore_corpus_noise.py` 自动抹平。

