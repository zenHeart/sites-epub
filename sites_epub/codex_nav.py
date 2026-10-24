"""Parse learn.chatgpt.com Codex product nav into grouped route entries."""

from __future__ import annotations

import json
import re
from dataclasses import replace
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag

from .models import IndexEntry

SITE = "https://learn.chatgpt.com"
SIX_SECTIONS = (
    "Overview",
    "Features",
    "Configuration",
    "Developers",
    "Security",
    "Administration",
)
SKIP_SECTION = {"Use Cases", "Resources"}

# 2026-10: learn.chatgpt.com is mid-migration from ``/codex/<slug>`` to
# ``/docs/<slug>`` and the split is partial — ``/codex/quickstart`` still answers
# 200 while ``/codex/cli`` 308s to ``/docs/codex/cli``. 174 of the book's 204
# committed routes were sitting on the redirecting half. ``llms.txt`` is the
# site's own index of what lives where, so it decides the canonical spelling
# instead of a per-route probe.
_DOCS_INDEX_RE = re.compile(r"https://learn\.chatgpt\.com/docs/([A-Za-z0-9/_.\-]*?)(?:\.md)?(?=[)\s]|$)")


def _plain(el: Tag) -> str:
    return " ".join(el.get_text(" ", strip=True).split())


def _norm_href(href: str) -> str | None:
    if not href:
        return None
    href = href.strip()
    if href.startswith("#"):
        return None
    if href.startswith("http://") or href.startswith("https://"):
        parsed = urlparse(href)
        if parsed.netloc not in {"learn.chatgpt.com", "www.learn.chatgpt.com"}:
            return None
        path = parsed.path or "/"
    else:
        path = urlparse(href).path or href.split("#", 1)[0].split("?", 1)[0]
    path = path.rstrip("/") or path
    if not path.startswith("/codex"):
        return None
    if path.startswith("/codex/use-cases") or path.startswith("/codex/resources"):
        return None
    return path


def route_from_path(path: str) -> str:
    return path.lstrip("/")


def html_url_for(path: str) -> str:
    return urljoin(SITE + "/", path.lstrip("/"))


def md_url_for(path: str) -> str:
    """Advertised twin: append .md to the page URL (often 302s to /docs/<slug>.md)."""
    return html_url_for(path) + ".md"


#: Labels that identify the Codex dropdown among the page's several nav
#: dropdowns (the API docs tab has "Models"/"Agents", the plugins tab has
#: "Plugins"/"Commerce", the blog tab has "Showcase"/"Cookbook").
_CODEX_SECTION_MARKERS = {"Overview", "Features", "Administration"}


def _section_select(soup: BeautifulSoup) -> Tag | None:
    # 2026-08: site renamed aria-label "Docs section" → "Docs"; several selects
    # share that label. Locate by option-set instead of the brittle label text.
    for sel in soup.find_all("select"):
        labels = {_plain(opt) for opt in sel.find_all("option")}
        if _CODEX_SECTION_MARKERS <= labels:
            return sel
    return None


def _astro_prop(value: object) -> str:
    """Read one Astro prop value: Astro serializes as ``[type, value]``."""
    if isinstance(value, list) and len(value) >= 2:
        value = value[1]
    return value if isinstance(value, str) else ""


def _dropdown_options(soup: BeautifulSoup) -> dict[str, str]:
    """Variant id -> section label from the MobileContextDropdown island.

    2026-10: the site dropped the native ``<select>`` and renders the section
    dropdown client-side, so the option list survives only as JSON inside the
    island's ``props`` attribute. The variant ids (``mobile-nav-tab-3-variant-N``)
    and the panel markup are unchanged, so the mapping is identical to the one
    the ``<select>`` used to carry.

    The page carries one dropdown per nav tab (API docs, plugins, Codex, blog);
    the Codex one is picked by its label set, the same discriminator the old
    ``<select>`` lookup used.
    """
    fallback: dict[str, str] = {}
    for island in soup.find_all("astro-island"):
        marker = f"{island.get('component-url') or ''}{island.get('component-export') or ''}"
        if "MobileContextDropdown" not in marker:
            continue
        props = island.get("props")
        if not props:
            continue
        try:
            data = json.loads(props)
        except (TypeError, ValueError):
            continue
        options = data.get("options")
        if not isinstance(options, list) or len(options) < 2:
            continue
        out: dict[str, str] = {}
        for entry in options[1]:
            if not isinstance(entry, list) or len(entry) < 2:
                continue
            item = entry[1]
            if not isinstance(item, dict):
                continue
            vid = _astro_prop(item.get("value")).strip()
            label = _astro_prop(item.get("label")).strip()
            if vid and label:
                out[vid] = label
        if not out:
            continue
        if _CODEX_SECTION_MARKERS <= set(out.values()):
            return out
        fallback = fallback or out
    return fallback


def _variant_sections(soup: BeautifulSoup) -> dict[str, str]:
    """Variant id -> section label, from whichever markup carries it."""
    select = _section_select(soup)
    if select is not None:
        out: dict[str, str] = {}
        for opt in select.find_all("option"):
            vid = (opt.get("value") or "").strip()
            label = _plain(opt)
            if vid and label:
                out[vid] = label
        return out
    return _dropdown_options(soup)


def parse_nav_html(html: str) -> list[IndexEntry]:
    """De-duplicated in-site Codex routes under the six horizontal sections."""
    soup = BeautifulSoup(html, "lxml")
    sections = _variant_sections(soup)
    if _CODEX_SECTION_MARKERS <= set(sections.values()):
        variant_to_group: dict[str, str] = {}
        for vid, label in sections.items():
            if label in SKIP_SECTION:
                continue
            if label not in SIX_SECTIONS:
                continue
            variant_to_group[vid] = label
    else:
        raise ValueError("Codex six-section nav mapping not found")
    if not variant_to_group:
        raise ValueError("Codex six-section nav mapping empty")

    seen: set[str] = set()
    out: list[IndexEntry] = []
    for vid, group in variant_to_group.items():
        panel = soup.select_one(
            f'[data-mobile-nav-variant-content][data-variant-id="{vid}"]'
        )
        if panel is None:
            continue
        for a in panel.find_all("a"):
            path = _norm_href(a.get("href") or "")
            if not path:
                continue
            title = _plain(a) or path.rsplit("/", 1)[-1]
            route = route_from_path(path)
            if not route or route in seen:
                continue
            seen.add(route)
            out.append(
                IndexEntry(
                    group=group,
                    title=title,
                    md_url=md_url_for(path),
                    html_url=html_url_for(path),
                    route=route,
                )
            )
    return out


def format_nav_routes(entries: list[IndexEntry]) -> str:
    lines = [
        f"{e.group}\t{e.title}\t{e.html_url}\t{e.md_url}" for e in entries
    ]
    return "\n".join(lines) + ("\n" if lines else "")


def docs_index_paths(llms_text: str) -> set[str]:
    """Paths the site indexes under ``/docs/`` (``llms.txt`` is the SSOT)."""
    return {m.rstrip("/") for m in _DOCS_INDEX_RE.findall(llms_text) if m}


def canonicalize(entries: list[IndexEntry], docs_paths: set[str]) -> list[IndexEntry]:
    """Repoint ``/codex/<slug>`` routes at ``/docs/<slug>`` when the site moved them.

    The route name is left alone so chapter files keep their identity across
    the migration; only the URL the reader clicks changes. Codex's own pages
    keep the ``codex/`` segment under ``/docs`` too (``/docs/codex/cli``), so a
    nav route tries both spellings before deciding the page stayed put.

    ``llms.txt`` omits a handful of routes (``changelog``,
    ``reference/slash-commands``, ``enterprise/govcloud-configuration``,
    ``hipaa-configuration``, ``developer-commands``, ``developer-settings``) that
    also moved, so anything the index does not vouch for is resolved with one
    live probe rather than trusted by default.
    """
    out: list[IndexEntry] = []
    for entry in entries:
        if entry.route == "codex":
            # The docs root moved too: /codex -> /docs.
            out.append(replace(entry, md_url=f"{SITE}/docs.md", html_url=f"{SITE}/docs"))
            continue
        if not entry.route.startswith("codex/"):
            out.append(entry)
            continue
        tail = entry.route[len("codex/"):]
        for candidate in (tail, f"codex/{tail}"):
            if candidate in docs_paths:
                url = f"{SITE}/docs/{candidate}"
                out.append(replace(entry, md_url=url + ".md", html_url=url))
                break
        else:
            url = f"{SITE}/docs/{tail}"
            if _answers_200(url):
                out.append(replace(entry, md_url=url + ".md", html_url=url))
            else:
                out.append(entry)
    return out


def _answers_200(url: str) -> bool:
    """Direct-200 check.

    ``http.fetch_text`` follows redirects, so it cannot tell "this URL serves
    the page" from "this URL bounces to the page". The migration question is
    exactly that distinction, so this asks urllib not to follow.
    """
    import urllib.error
    import urllib.request

    class _NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args):
            return None

    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        return opener.open(req, timeout=20).status == 200
    except urllib.error.HTTPError as exc:
        return exc.code == 200
    except Exception:
        return False
