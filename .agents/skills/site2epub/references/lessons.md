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
