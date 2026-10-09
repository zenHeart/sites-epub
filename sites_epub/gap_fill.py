"""Second-source enumeration for vendors whose primary adapter under-collects.

Every vendor here has pages that exist online, answer 200, and are absent from
``routes.json``. They share one cause: the primary adapter enumerates a single
nav surface (an HTML nav, a section select, one llms.txt branch) and the site
grew new trees — Cursor's ``/help`` centre and ``/learn`` course, Zencoder's
``/zenflow``, xAI's ``/bot`` — without those trees reaching the surface the
adapter reads. The fix is to enumerate the second source (sitemap / llms.txt /
product-family page) and let an explicit policy decide what belongs in the book.

The policy is data, not code, so the audit that produced it stays reviewable:
``SOURCES`` says where to look, ``ALLOW``/``DENY`` say what counts as product
documentation, and everything else is recorded as an explicit exclusion.

**范围铁律 (产品书不是 API 书).** The exclusion axis differs per vendor and is
spelled out in each ``DENY`` comment:

* vendors whose second source is the **open-platform API site** (Zhipu) are
  excluded wholesale — those pages are "调这个厂商的 API", not "用这个产品";
* vendors whose gaps are **API cookbooks / console / developer account** pages
  (xAI) are excluded by prefix, keeping the product-feature pages;
* everything else is **marketing** (pricing, careers, legal, persona landing
  pages, user-generated marketplaces) and is excluded as non-documentation.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

from .http import fetch_text
from .models import IndexEntry

# ---------------------------------------------------------------- extraction

_LINK_RE = re.compile(r"\[[^\]\n]{1,140}\]\((https?://[^\s)\]]+)\)")
_HREF_RE = re.compile(r'href=["\'](https?://[^"\'\s]+)["\']')
_LOC_RE = re.compile(r"<loc>\s*([^<\s]+?)\s*</loc>")
_NON_PAGE_EXT = (
    ".dmg", ".exe", ".deb", ".rpm", ".appimage", ".png", ".jpg", ".jpeg", ".gif",
    ".svg", ".webp", ".zip", ".tar", ".gz", ".pdf", ".woff", ".woff2", ".mp4", ".ico",
)
_NON_PAGE_HOST = ("localhost", "sitemaps.org", "schema.org", "www.w3.org", "mintlify.com")


def _clean(raw: str) -> str | None:
    url = raw.split("#")[0].split("?")[0].strip().rstrip("/")
    url = re.sub(r"\\u003[cC].*$", "", url)
    if not url.startswith("http"):
        return None
    host = re.sub(r"^https?://([^/]+).*$", r"\1", url).lower()
    if any(k in host for k in _NON_PAGE_HOST):
        return None
    if url.lower().endswith(_NON_PAGE_EXT) or url.lower().endswith((".xml", ".txt", ".json")):
        return None
    return re.sub(r"\.md$", "", url)


def _links(body: str) -> set[str]:
    raw = set(_LOC_RE.findall(body)) | set(_LINK_RE.findall(body)) | set(_HREF_RE.findall(body))
    out = set()
    for item in raw:
        cleaned = _clean(item)
        if cleaned:
            out.add(cleaned)
    return out


def _safe(url: str) -> str:
    try:
        return fetch_text(url)
    except Exception:
        return ""


# ------------------------------------------------------------------- policy

#: vendor -> (source URLs, group name for allowed pages, deny prefix predicates)
SOURCES: dict[str, tuple[tuple[str, ...], str]] = {
    "codex": (("https://learn.chatgpt.com/llms.txt",), "Codex Docs"),
    "cursor": (
        (
            "https://cursor.com/docs/sitemap.xml",
            "https://cursor.com/sitemap.xml",
            "https://cursor.com/llms.txt",
        ),
        "Cursor: Docs",
    ),
    "grok": (("https://docs.x.ai/sitemap.xml", "https://x.ai/sitemap.xml", "https://docs.x.ai/llms.txt"), "Grok Product"),
    "manus": (("https://manus.im/sitemap.xml",), "Manus: Features"),
    "zencoder": (("https://docs.zencoder.ai/llms.txt", "https://docs.zencoder.ai/sitemap.xml"), "Zencoder Docs"),
}

#: Blog hosts that carry real articles; anything else under /blog is an
#: aggregation page (topic/author/category) and stays out of the book.
BLOG_HOSTS = {
    "cursor": "cursor.com",
    "manus": "manus.im",
    "zencoder": "zencoder.ai",
}

#: prefix -> group. Longest match wins, so a vendor can nest groups.
GROUPS: dict[str, tuple[tuple[str, str], ...]] = {
    # Codex: the six-section nav still owns the bulk; llms.txt contributes the
    # pages that moved out of it under /docs/.
    "codex": (
        ("/docs/codex/", "Codex: Developers"),
        ("/docs/enterprise/", "Codex: Administration"),
        ("/docs/environments/", "Codex: Developers"),
        ("/docs/whats-new/", "Codex: What's New"),
        ("/docs/", "Codex: Docs"),
    ),
    # Cursor: docs / help centre / learn course / guides / workflows.
    "cursor": (
        ("/docs/", "Cursor: Docs"),
        ("/docs/release-notes", "Cursor: Release Notes"),
        ("/help/", "Cursor: Help Center"),
        ("/learn/", "Cursor: Learn"),
        ("/guides/", "Cursor: Guides"),
        ("/workflows/", "Cursor: Workflows"),
    ),
    # xAI: Grok product features + Bot guides + release changelog. The docs
    # host's cookbook/console/developers trees and x.ai's api/stories/solutions
    # trees are excluded below.
    "grok": (
        ("/grok/", "Grok Product"),
        ("/bot/guides", "Grok Bot Guides"),
        ("/bot/use-cases", "Grok Bot Guides"),
        ("/voice/", "Grok Voice"),
        ("/news/", "xAI News"),
        ("/changelog/", "xAI Changelog"),
        ("/build", "Grok Product"),
    ),
    "manus": (("/features/", "Manus: Features"), ("/blog/", "Manus: Blog")),
    # Zencoder: Zenflow is a first-party product and belongs in the book.
    "zencoder": (
        ("/zenflow-changelog", "Zenflow"),
        ("/zenflow-work", "Zenflow"),
        ("/zenflow/", "Zenflow"),
        ("/changelog/", "Zencoder Changelog"),
        ("/learn/", "Zencoder Learn"),
        ("/features/", "Zencoder: Features"),
        ("/admin/", "Zencoder: Administration"),
        ("/clis", "Zencoder: CLI Integrations"),
        ("/faq", "Zencoder: FAQ"),
    ),
}

#: Vendor-specific exclusions, most-specific-first. Each entry is
#: ``(url prefix, reason recorded in the audit report)``.
DENY: dict[str, tuple[tuple[str, str], ...]] = {
    "codex": (
        # 2.9 MB aggregate of the sectioned docs that are already collected.
        ("/docs/codex-manual", "Codex Manual 聚合页（2.9MB），与已收录分节文档重复"),
        ("/docs/custom-prompts", "官方标注 deprecated，已由 /docs/build-skills 取代"),
        ("/docs/mcp-server", "codex mcp-server 命令移除公告，非可用文档"),
        ("/docs/environments/cloud-environment", "Codex Cloud (Legacy)，已被 cloud-environments 取代"),
        ("/docs/cloud/internet-access", "Codex Cloud (Legacy)，已被 cloud-environments 取代"),
        ("/docs/llms-full", "llms-full.txt 全站导出文件，非页面"),
        # ChatGPT Learn site-level pages, not Codex product docs.
        ("/guides/", "ChatGPT Learn 站点级指南，非 Codex 产品文档"),
        ("/resources", "ChatGPT Learn 站点资源索引页"),
        ("/videos", "ChatGPT Learn 视频索引页"),
        ("/docs/guides", "ChatGPT Learn 站点级指南，非 Codex 产品文档"),
    ),
    "cursor": (
        ("/for/", "「Cursor for <人群/语言>」获客落地页，非产品文档"),
        ("/terms/", "法务条款"),
        ("/abuse", "滥用政策，法务文本"),
        ("/acceptable-use-policy", "可接受使用政策，法务文本"),
        ("/licenses", "许可，法务文本"),
        ("/privacy", "隐私政策，法务文本"),
        ("/data-use", "数据使用政策，法务文本"),
        ("/cookie", "Cookie 政策，法务文本"),
        ("/blog/topic/", "博客分类聚合页，非文章"),
        ("/blog/author/", "博客作者聚合页，非文章"),
        ("/blog/category/", "博客分类聚合页，非文章"),
        # Top-level product/marketing pages: the book is the documentation set.
        ("/ambassadors", "社区大使营销页"),
        ("/brand", "品牌资产页"),
        ("/careers", "招聘页"),
        ("/contact-sales", "销售联系页"),
        ("/customers", "客户案例营销页"),
        ("/field-kit", "品牌物料页"),
        ("/lennyssummit", "会议活动营销页"),
        ("/community", "社区入口页"),
        ("/contact", "联系页"),
        ("/enterprise", "企业版销售页"),
        ("/pricing", "定价页"),
        ("/students", "学生计划营销页"),
        ("/workshops", "活动页"),
        ("/business/", "企业销售页"),
        ("/future", "品牌愿景页"),
        ("/", "站点首页/产品落地页，非文档"),
    ),
    "grok": (
        ("/bot/marketplace", "用户投稿的 Bot 市场目录，非官方产品文档"),
        ("/grok/business", "xAI for Business 销售页"),
        ("/grok/government", "xAI for Government 销售页"),
        ("/grok/use-cases", "Grok 用例获客落地页"),
        ("/news/api", "API 公测公告（调 API），范围铁律排除"),
        ("/news/government", "xAI for Government 销售公告"),
        ("/cookbook", "Grok API 调用示例（调 API），范围铁律排除"),
        ("/console/", "xAI Console 账号/计费控制台，非产品文档"),
        ("/developers/", "API 开发者账号与模型 API 参考，范围铁律排除"),
        ("/rest-api-reference", "REST API 端点参考，范围铁律排除"),
        ("/api/", "API 产品页/端点参考，范围铁律排除"),
        ("/stories/", "客户案例营销页"),
        ("/solutions/", "行业方案销售页"),
        ("/legal", "法务页"),
        ("/privacy-portal", "隐私请求门户"),
        ("/security", "安全合规营销页"),
        ("/safety", "安全政策页"),
        ("/contact", "联系页"),
        ("/contact-sales", "销售联系页"),
        ("/careers", "招聘页"),
        ("/pricing", "定价页"),
        ("/grokathon", "黑客松活动页"),
        ("/colossus", "算力集群介绍页"),
        ("/galaxy", "Galaxy 交易页"),
        ("/london", "站点页"),
        ("/memphis", "站点页"),
        ("/open-source", "开源项目导流页"),
        ("/company", "公司介绍页"),
        ("/.well-known/", "站点元数据，非页面"),
        ("/docs.x.ai/", "docs.x.ai 已由 xai 适配器主枚举覆盖"),
        ("/x.ai", "x.ai 站点首页/产品落地页"),
        ("/", "站点首页/产品落地页，非文档"),
    ),
    "manus": (
        ("/events/", "活动营销页"),
        ("/solutions/", "行业方案营销页"),
        ("/tools/", "「AI <X> 生成器」SEO 工具落地页"),
        ("/usecase-", "用户/官方用例聚合页"),
        ("/playbook", "营销 Playbook"),
        ("/brand", "品牌资产页"),
        ("/about", "公司介绍页"),
        ("/team", "团队介绍页"),
        ("/startups", "创业计划营销页"),
        ("/edu", "教育计划营销页"),
        ("/help.manus.im", "帮助站入口，非产品文档"),
        ("/", "站点首页/功能落地页，非文档"),
    ),
    "zencoder": (
        ("/glossary", "161 个单术语 SEO 内容页，非产品文档"),
        ("/glossary/", "单术语 SEO 内容页，非产品文档"),
        ("/compare/", "竞品对比营销页"),
        ("/blog/author/", "博客作者聚合页，非文章"),
        ("/blog/topic/", "博客分类聚合页，非文章"),
        ("/blog/category/", "博客分类聚合页，非文章"),
        ("/events", "活动营销页"),
        ("/webinars", "线上研讨会营销页"),
        ("/customers", "客户案例营销页"),
        ("/pricing", "定价页"),
        ("/enterprise", "企业版销售页"),
        ("/contact", "联系页"),
        ("/about", "公司介绍页"),
        ("/", "站点首页，非文档"),
    ),
}

BLOG_GROUP = {"cursor": "Cursor: Blog", "manus": "Manus: Blog", "zencoder": "Blog"}

#: Routes the site still advertises but no longer serves. These come from the
#: *primary* enumeration (the vendor's own llms.txt / sitemap / blog listing),
#: so the scope policy above cannot drop them — only an explicit retired list
#: can. Every entry is a 404/307-to-/404 confirmed live, not a guess.
RETIRED: dict[str, tuple[str, ...]] = {
    "manus": (
        "https://manus.im/blog/manus-is-hiring",
        "https://manus.im/blog/manus-pops-event-bts",
    ),
    "cursor": (
        # Client-rendered Next.js hub: neither the .md twin nor the HTML twin
        # yields a body (extract_page sees 76 chars, the real guides are its
        # /workflows/autonomous-agents/* children, which are all collected).
        "https://cursor.com/workflows/autonomous-agents",
    ),
    "gemini": (
        # Still listed in jules.google/docs/llms.txt, gone from the site.
        "https://jules.google/docs/index",
        # The Code Assist nav still links the pre-rename page; it 301s to
        # …/write-code-gemini, which is already collected under its own route.
        "https://docs.cloud.google.com/gemini/docs/codeassist/use-in-ide",
    ),
}


def drop_retired(vendor_id: str, entries: list[IndexEntry]) -> list[IndexEntry]:
    dead = {u.rstrip("/") for u in RETIRED.get(vendor_id, ())}
    if not dead:
        return entries
    return [e for e in entries if (e.html_url or "").rstrip("/") not in dead]


def _denied(vendor: str, path: str) -> bool:
    for prefix, _reason in DENY.get(vendor, ()):
        if prefix == "/":
            if path == "/":
                return True
            continue
        if path == prefix:
            return True
        # A trailing slash means "this subtree"; without one the prefix still
        # owns its children but not its siblings ("/business" vs "/business/").
        if path.startswith(prefix if prefix.endswith("/") else prefix + "/"):
            return True
    return False


def _group_for(vendor: str, url: str) -> str | None:
    """Longest-prefix group match, after the DENY list says no."""
    path = urlparse(url).path or "/"
    if _denied(vendor, path):
        return None
    best = None
    for prefix, group in GROUPS.get(vendor, ()):
        if path.startswith(prefix):
            if best is None or len(prefix) > len(best[0]):
                best = (prefix, group)
    if best:
        return best[1]
    # Blog articles: allow only real post URLs, never the aggregations.
    if path.startswith("/blog/") and len(path.strip("/").split("/")) >= 2:
        return BLOG_GROUP.get(vendor)
    return None


def _route_for(url: str) -> str:
    path = urlparse(url).path.strip("/")
    return path or "index"


#: learn.chatgpt.com serves the same page at ``/codex/<slug>`` and
#: ``/docs/<slug>``; the Codex adapter collects under the ``codex/`` route
#: namespace, so a ``/docs/`` discovery maps onto it instead of forking a
#: second copy of every page. The route keeps the Codex namespace; the
#: html_url keeps the URL that actually answers 200.
ROUTE_ALIAS = {
    "codex": ("/docs/", "codex/"),
}


def _route_and_url(vendor: str, url: str) -> tuple[str, str]:
    alias = ROUTE_ALIAS.get(vendor)
    path = urlparse(url).path
    if alias and (path.startswith(alias[0]) or path == alias[0].rstrip("/")):
        tail = path[len(alias[0]):] if path.startswith(alias[0]) else ""
        # /docs/codex/cli describes the same page the nav collects as
        # /codex/cli, so keep one route instead of forking "codex/codex/…".
        if tail == alias[1] or tail.startswith(alias[1]):
            return tail.strip("/"), url
        return (alias[1] + tail).strip("/"), url
    return _route_for(url), url


def _title_for(url: str) -> str:
    slug = _route_for(url).rsplit("/", 1)[-1]
    return slug.replace("-", " ").replace("_", " ") or "index"


def supplement(vendor_id: str, taken_routes: set[str]) -> list[IndexEntry]:
    """Routes for vendor ``vendor_id`` that the primary adapter missed.

    ``taken_routes`` is the route set the primary enumeration already produced;
    anything it yields is skipped so the two sources never disagree about a
    page that is already in the book.
    """
    spec = SOURCES.get(vendor_id)
    if not spec:
        return []
    sources, _ = spec
    blog_host = BLOG_HOSTS.get(vendor_id)
    seen = set(taken_routes)
    out: list[IndexEntry] = []
    for source in sources:
        for url in sorted(_links(_safe(source))):
            parsed = urlparse(url)
            if blog_host and parsed.netloc != blog_host:
                # A vendor's own docs host is fair game; the product-family
                # crawl may surface marketing pages on other hosts.
                if vendor_id in {"cursor", "zencoder"} and "docs." in parsed.netloc:
                    pass
                else:
                    continue
            group = _group_for(vendor_id, url)
            if not group:
                continue
            route, html_url = _route_and_url(vendor_id, url)
            if route in seen:
                continue
            seen.add(route)
            out.append(
                IndexEntry(
                    group=group,
                    title=_title_for(url),
                    md_url=html_url + ".md",
                    html_url=html_url,
                    route=route,
                    kind="blog" if group == BLOG_GROUP.get(vendor_id) else "doc",
                )
            )
    return out