# 抓取、提交与打包

## 命令

```bash
python3 -m sites_epub add <docs-url> [blog-url] [--name NAME] [--id ID]
python3 -m sites_epub fetch --id codex
python3 -m sites_epub pack                 # CI：按书跳过未变厂商
python3 -m sites_epub pack --force         # 全量重打
python3 -m sites_epub pack --id claude     # 只打一本
python3 -m sites_epub catalog
```

## 新建 vs 增量

1. `catalog.json` 没有该 vendor id：建 `vendors/<id>/`，爬全部路由。
2. 已存在：用 `vendors/<id>/fingerprints.json` 对照 `corpus/pages`，**未变路由不重抓**。若缓存仍是 React/MDX 运行时源码（`export const` / `useMemo`），即使哈希未变也要重抓 HTML。
3. 站点文档导航在前；**Blog 必须是最后一个 TOC parent**。
4. `fetch` 把 `updated_at`（语料时间）写进 `catalog.json`，书架用来对照线上是否过期。其他 EPUB 站点在 `catalog.json` → `sites`，封面点击跳到那些 URL。

## 提交

提交：`catalog.json`、`vendors/<id>/vendor.json`、`fingerprints.json`、`corpus/pages`、`corpus/routes.json`、`corpus/image-map.json`、压缩后的图片。

禁止：cookie、token、`.env`、`work/`。

## CI

- 环境变量 `SITESEPUB_OFFLINE=1`。http 层对任何 live fetch 直接失败。
- 先 checkout `gh-pages` 到 `prev-site`，`SITESEPUB_PREV_SITE=prev-site`。
- 一本书只在 **corpus / 封面 / 打包器源码** 变化时重打；否则复制上次 EPUB。
- 打包器改动（标题链接、CSS）会改变共享指纹，三本都重打。这是正确行为。
- workflow_dispatch 勾 `force` 或 `SITESEPUB_FORCE=1` 全量重打。
- `walk` 用 `blocking_defects`：破图或 `unlinked_page_title` 即失败。

不要在 Actions 里跑 `add`/`fetch`。

## 常见踩坑（详见 `lessons.md`）

| 症状 | 一次性原因 | 一次性动作 |
|---|---|---|
| 封面写着 "ChatGPT Codex Docs" | `grouped_html()` 硬编码 + `pack_epub` 默认值 | 修 `epub_pack.py`（`grouped_html` 接 `title`/`author`），`images.py` / `page.py` 把 `base` 默认从 `https://learn.chatgpt.com` 改为 `""` |
| `icon.png` 文件头是 `<svg ...` | `ensure_vendor_icon()` 只看字节数不看魔数 | push 前 `file vendors/<id>/icon.png` 校验，SVG-as-PNG 必须替换 |
| `add` 后 0 条路由 | 站点用 Mintlify `===/path===` 而非 `[title](url)` 列表 | 写 80 行小适配器（参考 `sites_epub/xai_nav.py`），不要去改 `parse_llms_generic` |
| `git push` 被 GH secret-scan 拦 | 文档示例里的 API key 形似真 key | `git commit --amend` 就地把真 key 替换成占位符再 push |
| 跨子域多 docs 根（如 docs.x.ai + x.ai/bot/guides） | `Vendor` 只接 1 个 docs_url | 统一用 `docs.x.ai/llms.txt` 拿索引，bot/guides 在 adapter 分支里额外 `fetch_text` + parse |
| 新 vendor 封面和 claude/codex/cursor 不对齐 | 没手画 SVG，copy icon 当 cover | `covers/<id>.svg` 用 400×560 模板手画，渲 800×1120 PNG（缺 cairo 时用 PIL fallback） |
| 「补齐到最新」但 `skipped=N` 被当无更新证据 | skip 判据=缓存完整性（命中指纹不发网络请求），页面级线上漂移不可见 | 用 `--refetch` 全量重拉；或先证明线上 llms.txt 与 `corpus/llms.txt` md5 一致（详见 `lessons.md` §10） |
| 目录标题乱码（`�`） | 源站强制 gzip，响应体被当 UTF-8 存进语料 | 修 `http.py` 解压（已修，见 `lessons.md` §12），refetch 对应页 |
| EPUB 超 100MB 在 gh-pages push 才爆 | 门禁只查破图不查体积 | 语料图重压 + CI Validate 已加 98MB 门禁（`lessons.md` §11） |

## 提交前自检

```bash
# 1. 封面标题门禁：所有 EPUB cover.xhtml 都不应包含 ChatGPT Codex Docs
for v in claude codex cursor grok gemini; do
  curl -ksSL https://epub.zenheart.site/$v.epub -o /tmp/$v.epub
  python3 .agents/skills/site2epub/scripts/check_epub.py /tmp/$v.epub >/dev/null && echo "$v: PASS" || echo "$v: FAIL"
done

# 2. icon 真为 PNG
file vendors/<id>/icon.png

# 3. 没有真 API key 被提交
git diff --cached | grep -E "xai-[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}" && echo "WARN: 真 key 漏出"

# 4. 语料维护（新增 vendor / 大批 refetch 后必跑；脚本同时报告 secret 命中与乱码页）
python3 .agents/skills/site2epub/scripts/sanitize_corpus_html.py <id>
python3 .agents/skills/site2epub/scripts/shrink_corpus_images.py <id>
# 然后对齐指纹（脚本改动过语料字节时）：
python3 - <<'PY'
import sys; sys.path.insert(0, '.')
from pathlib import Path
from sites_epub.fingerprint import content_hash, save_fingerprints
vendor = "<id>"
corpus = Path(f"vendors/{vendor}/corpus")
fp = {p.relative_to(corpus / "pages").as_posix()[:-3]: content_hash(p.read_text(encoding="utf-8", errors="replace")) for p in (corpus / "pages").glob("**/*.md")}
save_fingerprints(corpus.parent / "fingerprints.json", fp)
print("fingerprints:", len(fp))
PY

# 5. 本地离线 pack 预演 CI（需 pandoc；Windows 加 PYTHONUTF8=1），看体积 + walk 门禁
python3 -m sites_epub pack --id <id>
```
