"""Kimi product adapter: sitemap-driven product pages + blog posts.

2026-10 the site reorganised under three fronts and both of the old enumeration
signals broke at once:

* **Docs** used to come from ``parse_docs_html`` over the homepage. The homepage
  now only anchors 8 links (``/``, ``/mykimi``, ``/plugins``, ``/tasks``,
  ``/inspiration``, ``/slides``, ``/deep-research``, ``/docs``) and dropped the
  whole ``/agent-swarm /sheets /design /build`` half of the product family, so a
  2026-10-09 refresh silently lost 5 product pages.
* **Blog** used to be scraped for ``/blog/<slug>`` patterns inside the SSR blob.
  ``/blog/<slug>`` now 302s to ``/en/blog/<slug>`` and the canonical listing is
  ``/en/blog``; the old regex only survived on by accident.

Enumeration is therefore explicit rather than incidental:

1. product pages — ``sitemap.xml`` (root language only; ``/en/*`` are the same
   pages mirrored under the i18n prefix), unioned with the homepage anchors,
   unioned with a link crawl of every product hub (``/products``, ``/academy``,
   ``/resources``, ``/features``, ``/help``, ``/ai-models``) — the hubs are the
   only place the tutorial and help sub-trees are linked from, and the sitemap
   lists none of them — then filtered by the scope rules below;
2. blog posts — the ``/en/blog`` listing anchors, canonicalised to
   ``https://www.kimi.com/en/blog/<slug>`` so no route points at a 302.

**Scope rule (范围铁律：产品书不是 API 书).** Kimi ships no public API docs on
this host, so the exclusion axis is *product page vs. marketing page*, not
*product vs. API*. Kept: feature pages, the help centre, product downloads, the
``/academy`` tutorials, and the agent/coding tutorials under ``/resources``.
Dropped: the SEO landing hubs (``/capabilities``, ``/use-cases``,
``/showcases``), enterprise sales pages (``/solutions``, ``/business``) and the
pricing page — they sell, they don't document usage. Every excluded prefix is
listed in ``KIMI_OUT_PREFIXES`` so the omission is auditable rather than
silent.

``/resources`` needs a second axis. It is not a hub page but a 341-child
content farm, and roughly 200 of those children answer long-tail office-suite
queries — ``how-to-use-vlookup-in-excel``, ``word-to-pdf-with-sejda``,
``best-fonts-for-powerpoint`` — with full articles about software that has
nothing to do with Kimi. Those are SEO 落地页 in the plain sense of 范围铁律,
so ``/resources`` is enumerated but gated by an explicit, reviewed allowlist
(``RESOURCES_KEEP``) rather than swept wholesale. The allowlist is the audited
agent / coding / Kimi-product / AI-creation tutorials; anything unlisted stays
out and the omission is visible in one place.
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

from .generic_nav import parse_docs_html
from .http import fetch_text
from .models import IndexEntry

BLOG_SLUG = re.compile(r"/(?:en/)?blog/([a-z0-9][a-z0-9-]{3,})")
BLOG_SKIP = {"page", "category", "tag", "author", "zh"}
BLOG_BASE = "https://www.kimi.com/en/blog"
KIMI_HOSTS = {"kimi.com", "www.kimi.com"}
SITEMAP_URL = "https://www.kimi.com/sitemap.xml"

#: Product hubs whose anchors (and embedded Next.js payload) are the only place
#: their sub-trees are linked. Each is crawled and unioned into the route set;
#: the hub page itself is an index, not a chapter.
HUB_PAGES = ("/products", "/academy", "/resources", "/features", "/help", "/ai-models")
HUB_BASE = "https://www.kimi.com"

#: hub prefix -> TOC group. ``/docs`` and the homepage product links fall back
#: to "Kimi 产品".
HUB_GROUPS = {
    "/academy": "Academy 教程",
    "/resources": "Resources 教程",
    "/features": "Features",
    "/help": "Help Center",
    "/products": "Products",
    "/ai-models": "Models",
}
DEFAULT_GROUP = "Kimi 产品"

#: Marketing / SEO hubs. Listed exhaustively so the report can name what was
#: left out and why instead of dropping pages without trace.
KIMI_OUT_PREFIXES = (
    "/capabilities/",  # per-tool SEO landing pages ("AI Python 代码生成器")
    "/use-cases/",  # per-scenario SEO landing pages ("AI MVP 生成器")
    "/showcases/",  # user-submitted output gallery
    "/solutions/",  # enterprise industry sales decks
    "/business",  # enterprise edition pitch
    "/membership/",  # pricing / subscription plans
    "/landing-ui/",  # build assets, not pages
    "/en",  # i18n mirror of the root language
    "/zh",  # i18n mirror
    "/blog",  # enumerated separately into the Blog group
    "/news",  # press-release hub
)
#: Suffixes that are never pages.
KIMI_OUT_SUFFIXES = (".md", ".xml", ".txt", ".json", ".js", ".css", ".png", ".jpg", ".jpeg", ".svg", ".ico", ".webmanifest", ".woff2")

#: ``/resources/<slug>`` children that are genuinely Kimi tutorials. Reviewed
#: against the live listing: the agent/agent-skill library, agent & agentic-AI
#: explainers, vibe-coding and coding-agent walkthroughs, AI image/slides/poster
#: creation, AI business & website building, the Kimi product pages, and the
#: sibling coding-agent setup guides. Everything else on that hub is an office
#: suite or third-party PDF utility SEO page and stays out of the book.
RESOURCES_KEEP = frozenset({
    # Agent skill library (Kimi 可安装技能说明)
    "academic-skills-for-agents", "academic-writing-skills-for-agents",
    "business-writing-skills-for-agents", "chart-skills-for-agents",
    "coding-skills-for-agents", "communication-skills-for-agents",
    "content-writing-skills-for-agents", "copywriting-skills-for-agents",
    "creative-writing-skills-for-agents", "customer-service-skills-for-agents",
    "customer-support-skills-for-agents", "data-analysis-skills-for-agents",
    "data-visualization-skills-for-agents", "design-skills-for-agents",
    "e-commerce-skills-for-agents", "financial-analysis-skills-for-agents",
    "financial-modeling-skills-for-agents", "goal-setting-skills-for-agents",
    "graphic-skills-for-agents", "html-skills-for-agents",
    "multimedia-skills-for-agents", "pdf-skills-for-agents",
    "ppt-skills-for-agents", "product-management-skills-for-agents",
    "product-manager-skills-for-agents", "productivity-skills-for-agents",
    "project-management-skills-for-agents", "public-speaking-skills-for-agents",
    "report-writing-skills-for-agents", "research-writing-skills",
    "seo-skills-for-agents", "skill-development-skills-for-agents",
    "software-skills-for-agents", "software-testing-skills",
    "spreadsheet-skills-for-agents", "translation-skills-for-agents",
    "ui-ux-design-skills-for-agents", "web-development-skills-for-agents",
    "create-skills", "agent-skills-examples", "what-are-ai-skills",
    # 智能体与 AI 概念
    "agent-ai-vs-agentic-ai", "agent-harness", "agent-orchestration",
    "agentic-ai", "agentic-ai-architectures", "agentic-coding",
    "agentic-coding-tools", "ai-agent", "ai-agent-use-cases",
    "ai-agent-vs-llm", "ai-agent-workflow", "ai-agents-examples",
    "ai-automation", "ai-computer-use", "ai-cowork", "ai-virtual-agent",
    "ai-workflow-automation", "autonomous-ai-agent", "goal-based-agent",
    "knowledge-based-agents-in-ai", "llm-agent", "local-ai-agent",
    "local-ai-assistant", "multi-agent", "multi-agent-collaboration",
    "parallel-agent", "rational-agent", "types-of-ai-agent",
    # Vibe Coding 与编程
    "what-is-vibe-coding", "how-to-vibe-code", "vibe-coding-examples",
    "what-is-ai-code", "visual-coding", "ai-coding-workflow",
    "ai-in-programming", "desktop-automation",
    # AI 创作：图片、海报、幻灯片、游戏
    "create-your-poster", "ai-poster-ideas", "how-to-create-ai-images",
    "prompts-for-ai-image-generators", "generate-slides-with-ai",
    "game-assets", "game-ideas", "how-to-create-game-assets",
    "how-to-make-a-2d-game", "how-to-make-a-3d-game",
    "how-to-make-a-game-with-ai", "how-to-create-a-3d-model-from-a-picture",
    # AI 商业与建站
    "ai-business-ideas", "ai-business-strategy", "ai-for-business",
    "ai-for-enterprise", "ai-in-business-examples", "benefits-of-ai-in-business",
    "how-to-use-ai-in-business", "one-person-company", "ai-excel-bot",
    "business-data-analysis", "business-intelligence-and-business-analytics",
    "business-proposal-vs-business-plan", "how-to-write-a-business-proposal",
    "how-to-draft-a-business-plan", "types-of-business-plan",
    "business-plan-templates",
    "create-ecommerce-websites", "create-websites-with-ai",
    "how-to-build-a-website", "how-to-build-a-website-from-scratch",
    "how-to-build-a-business-website-for-free",
    "make-a-website-for-a-small-business", "how-to-build-landing-pages",
    "how-to-create-a-portfolio-website", "how-to-create-an-online-store-website",
    # Kimi 自有产品
    "kimi-brand", "kimi-browser-extension", "kimi-claw-introduction",
    "kimi-code-introduction", "kimi-community", "kimi-for-mac",
    "kimi-for-windows", "kimi-mira-introduction", "kimi-work-dashboard",
    "kimi-work-introduction", "kimi-work-remote-control", "kimi-k2-7-code",
    # 同类编程 Agent 的安装与技能（第三方 API 接入类不在此列）
    "cursor-skills", "cursor-ai-website", "opencode-install", "opencode-skills",
    "openclaw-cloud", "openclaw-skills", "how-to-install-hermes-agent",
    # 工程写作
    "technical-design-document", "technical-design-document-templates",
    "organize-files",
})


def _path_of(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc.lower() not in KIMI_HOSTS:
        return None
    return (parsed.path or "/").rstrip("/") or "/"


def _in_scope(path: str) -> bool:
    # A prefix written with a trailing slash is a subtree ("/capabilities/" plus
    # its own index page "/capabilities"); one without is a single path that
    # also owns its subtree ("/business", "/blog").
    for prefix in KIMI_OUT_PREFIXES:
        if prefix.endswith("/"):
            if path.startswith(prefix) or path == prefix.rstrip("/"):
                return False
        elif path == prefix or path.startswith(prefix + "/"):
            return False
    if any(path.endswith(sfx) for sfx in KIMI_OUT_SUFFIXES):
        return False
    if path.startswith("/resources/"):
        # The content farm gate: only the reviewed tutorial slugs get in.
        if path[len("/resources/"):] not in RESOURCES_KEEP:
            return False
    return True


def _group_for(path: str) -> str:
    for prefix, group in HUB_GROUPS.items():
        if path == prefix or path.startswith(prefix + "/"):
            return group
    return DEFAULT_GROUP


#: TOC order for the docs section. ``grouped_html`` keys its section headings on
#: first appearance and renames any repeat, so the union of five enumeration
#: sources has to be grouped before it is emitted or one knowledge domain turns
#: into several sibling sections with route-suffixed names.
_GROUP_ORDER = {
    "Products": 0,
    "Models": 1,
    "Features": 2,
    "Academy 教程": 3,
    "Resources 教程": 4,
    "Help Center": 5,
    DEFAULT_GROUP: 6,
}


def _entries_from_paths(paths: list[str]) -> list[IndexEntry]:
    out: list[IndexEntry] = []
    for path in sorted(paths, key=lambda p: _GROUP_ORDER.get(_group_for(p), 99)):
        html_url = f"https://www.kimi.com{path}"
        out.append(
            IndexEntry(
                group=_group_for(path),
                title=path.strip("/").rsplit("/", 1)[-1].replace("-", " ") or "index",
                # Soft 404: the ``.md`` twin of a product page answers 200 with
                # the parent index (and ``/products/.md`` is a malformed URL
                # anyway), so the HTML page is the only real source.
                md_url=html_url,
                html_url=html_url,
                route=path.strip("/") or "index",
                kind="doc",
            )
        )
    return out


def parse_kimi_sitemap(sitemap_xml: str) -> list[str]:
    """Root-language product paths from ``<loc>`` entries, in sitemap order.

    The sitemap carries every page twice — once at the root language and once
    under ``/en`` — so the mirror half is dropped here rather than downstream.
    """
    out: list[str] = []
    seen: set[str] = set()
    for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", sitemap_xml, flags=re.I):
        path = _path_of(loc)
        if not path or path in seen or not _in_scope(path):
            continue
        seen.add(path)
        out.append(path)
    return out


def parse_kimi_family_links(family_html: str, hub: str = "/products") -> list[str]:
    """In-scope product paths linked from a product hub page.

    Anchors *and* the Next.js payload are swept, because part of each hub's
    card grid ships as escaped JSON rather than real anchors. The hub's own
    index path is returned by neither pass and is not added here.
    """
    out: list[str] = []
    seen: set[str] = set()
    candidates = list(re.findall(r'href="(/[A-Za-z0-9/_.\-]*)"', family_html))
    candidates += re.findall(r'"(/[A-Za-z0-9/_.\-]+)"', family_html)
    for cand in candidates:
        path = _path_of("https://www.kimi.com" + cand) or "/"
        if path in HUB_PAGES or not _in_scope(path) or path in seen:
            continue
        seen.add(path)
        out.append(path)
    return out


def parse_kimi_docs(docs_html: str) -> list[IndexEntry]:
    """Product pages from sitemap + homepage anchors + every product hub crawl."""
    paths: list[str] = []
    seen: set[str] = set()

    def _push(path: str | None) -> None:
        if path and _in_scope(path) and path not in seen:
            seen.add(path)
            paths.append(path)

    for path in parse_kimi_sitemap(_safe_fetch(SITEMAP_URL)):
        _push(path)
    # Homepage anchors keep /mykimi and /inspiration, which the sitemap omits.
    for entry in parse_docs_html(docs_html, "https://www.kimi.com"):
        _push("/" + entry.route if entry.route != "index" else "/")
    # The hub crawls are what surface /academy, /resources, /features, /help
    # and /ai-models children: none of those sub-trees appear in the sitemap,
    # and the homepage links only 8 of them.
    for hub in HUB_PAGES:
        for path in parse_kimi_family_links(_safe_fetch(HUB_BASE + hub), hub):
            _push(path)
    return _entries_from_paths(paths)


def parse_kimi_blog(html: str, blog_url: str) -> list[IndexEntry]:
    """Blog posts, canonicalised to ``https://www.kimi.com/en/blog/<slug>``.

    2026-10: ``/blog/<slug>`` 302s to ``/en/blog/<slug>``, so a route still
    pointing at the root path would be a redirect rather than a page. Both
    spellings are scanned and de-duplicated by slug.
    """
    out: list[IndexEntry] = []
    seen: set[str] = set()
    for slug in BLOG_SLUG.findall(html):
        if slug in BLOG_SKIP or slug in seen:
            continue
        seen.add(slug)
        url = f"{BLOG_BASE}/{slug}"
        out.append(
            IndexEntry(
                group="Blog",
                title=slug.replace("-", " "),
                # Soft 404: ``<url>.md`` answers 200 but redirects to the blog
                # index page, and ``fetch_source`` accepts it as readable, so
                # every post would cache the same listing. The HTML page is the
                # only source carrying the article.
                md_url=url,
                html_url=url,
                route=f"blog/{slug}",
                kind="blog",
            )
        )
    return out


def _safe_fetch(url: str) -> str:
    """The listing may go down mid-refresh; enumeration should still return
    whatever the other sources found rather than abort the whole vendor."""
    try:
        return fetch_text(url)
    except Exception:
        return ""