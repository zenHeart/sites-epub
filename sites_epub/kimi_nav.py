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
   unioned with a link crawl of ``/products`` (which is the page that actually
   carries the product family and is absent from both), then filtered by the
   scope rule below;
2. blog posts — the ``/en/blog`` listing anchors, canonicalised to
   ``https://www.kimi.com/en/blog/<slug>`` so no route points at a 302.

**Scope rule (范围铁律：产品书不是 API 书).** Kimi ships no public API docs on
this host, so the exclusion axis is *product page vs. marketing page*, not
*product vs. API*. Kept: feature pages, the help centre, product downloads, the
``/academy`` tutorials. Dropped: the SEO landing hubs (``/capabilities``,
``/use-cases``, ``/showcases``, ``/resources``), enterprise sales pages
(``/solutions``, ``/business``) and the pricing page — they sell, they don't
document usage. Every excluded prefix is listed in ``KIMI_OUT_PREFIXES`` so the
omission is auditable rather than silent.
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
FAMILY_URL = "https://www.kimi.com/products"

#: Marketing / SEO hubs. Listed exhaustively so the report can name what was
#: left out and why instead of dropping pages without trace.
KIMI_OUT_PREFIXES = (
    "/capabilities/",  # per-tool SEO landing pages ("AI Python 代码生成器")
    "/use-cases/",  # per-scenario SEO landing pages ("AI MVP 生成器")
    "/showcases/",  # user-submitted output gallery
    "/resources/",  # content-marketing editorial hub
    "/solutions/",  # enterprise industry sales decks
    "/business",  # enterprise edition pitch
    "/membership/",  # pricing / subscription plans
    "/landing-ui/",  # build assets, not pages
    "/help/",  # help-centre article leaves (indexed via /help, not per-article)
    "/en",  # i18n mirror of the root language
    "/zh",  # i18n mirror
    "/blog",  # enumerated separately into the Blog group
    "/news",  # press-release hub
)
#: Hub index pages that only answer 308 ``/hub -> /hub/``. The trailing-slash
#: form is the one that returns 200, so the route has to carry it.
KIMI_INDEX_PATHS = frozenset({"/products", "/features", "/ai-models", "/academy"})
#: Suffixes that are never pages.
KIMI_OUT_SUFFIXES = (".md", ".xml", ".txt", ".json", ".js", ".css", ".png", ".jpg", ".jpeg", ".svg", ".ico", ".webmanifest", ".woff2")


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
    return True


def _entries_from_paths(paths: list[str]) -> list[IndexEntry]:
    out: list[IndexEntry] = []
    for path in paths:
        html_url = f"https://www.kimi.com{path}"
        if path in KIMI_INDEX_PATHS:
            html_url += "/"
        out.append(
            IndexEntry(
                group="Docs",
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


def parse_kimi_family_links(family_html: str) -> list[str]:
    """In-scope product paths linked from ``/products``.

    ``/products`` is the product-family hub the homepage no longer links to; it
    is also the only in-site page that links ``/code`` and
    ``/products/kimi-work``. Anchors *and* the Next.js payload are swept,
    because part of the nav ships as escaped JSON rather than real anchors.
    """
    out: list[str] = []
    seen: set[str] = set()
    candidates = list(re.findall(r'href="(/[A-Za-z0-9/_.\-]*)"', family_html))
    candidates += re.findall(r'"(/[A-Za-z0-9/_.\-]+)"', family_html)
    for cand in candidates:
        path = _path_of("https://www.kimi.com" + cand) or "/"
        if not _in_scope(path) or path in seen:
            continue
        seen.add(path)
        out.append(path)
    return out


def parse_kimi_docs(docs_html: str) -> list[IndexEntry]:
    """Product pages from sitemap + homepage anchors + ``/products`` crawl."""
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
    for path in parse_kimi_family_links(_safe_fetch(FAMILY_URL)):
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