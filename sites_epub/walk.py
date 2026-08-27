"""Walk every packed chapter for visual-structure defects."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from dataclasses import asdict, dataclass, field
from html import unescape
from pathlib import Path

import warnings

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

MDX_VISIBLE = re.compile(
    r"<(Tabs|Tab|Info|Tip|Warning|Note|Accordion|AccordionGroup|CodeGroup|"
    r"WorkflowSteps|CodexDocsOverviewLanding|CodexOverviewLanding|"
    r"ContentModeSwitch|CodexAppDownloadCta|PromptComponent|GlossaryTable|"
    r"ConfigTable|FileTree|ContentSwitcher|ModelDetails|CodexCollectionList|"
    r"CodexPlanFeatureMatrix)\b",
    re.I,
)
# Any leftover JSX island in prose; ignore `hooks.<Event>` type placeholders.
PASCAL_TAG = re.compile(r"(?<![\w.])<([A-Z][A-Za-z0-9]+)\b")
THEME_LEAK = re.compile(r"theme=\{null\}")
FENCE_LEAK = re.compile(r"```")
PRETTIER_LEAK = re.compile(r"\{/\*\s*prettier-ignore\s*\*/\}")
REMOTE_SRC = re.compile(r"^(https?:)?//", re.I)
SKIP_XHTML = ("nav.xhtml", "title_page.xhtml", "toc.xhtml")


@dataclass
class ChapterResult:
    chapter: str
    ok: bool
    chars: int
    defects: list[str] = field(default_factory=list)
    img_srcs: list[str] = field(default_factory=list)


@dataclass
class WalkReport:
    epub: str
    chapter_count: int
    fail_count: int
    ok: bool
    chapters: list[ChapterResult]


def _chapter_names(zf: zipfile.ZipFile) -> list[str]:
    names: list[str] = []
    for name in zf.namelist():
        lower = name.lower()
        if not lower.endswith(".xhtml"):
            continue
        if any(skip in lower for skip in SKIP_XHTML):
            continue
        names.append(name)
    return names


def _page_units(name: str, html: str) -> list[tuple[str, str]]:
    """One unit per .doc-page (site route); fall back to the whole file."""
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.select(".doc-page")
    if pages:
        out = []
        for i, page in enumerate(pages, start=1):
            pid = page.get("id") or f"p{i}"
            out.append((f"{name}#{pid}", str(page)))
        return out
    # Pandoc may emit leftover split files with no route page; skip them.
    return []


def inspect_fragment(
    html: str,
    *,
    chapter: str = "",
    zip_names: set[str] | None = None,
) -> tuple[list[str], int, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True)).strip()
    defects: list[str] = []
    prose = BeautifulSoup(html, "html.parser")
    for el in prose.select("pre, code"):
        el.decompose()
    prose_text = re.sub(r"\s+", " ", prose.get_text(" ", strip=True)).strip()
    markup = unescape(str(prose))
    if (
        MDX_VISIBLE.search(prose_text)
        or MDX_VISIBLE.search(markup)
        or PASCAL_TAG.search(markup)
        or PASCAL_TAG.search(prose_text)
        or prose.find(["codegroup", "tabs", "accordiongroup", "workflowsteps"])
    ):
        defects.append("leftover_mdx_tags")
    if THEME_LEAK.search(prose_text):
        defects.append("theme_null_leak")
    if FENCE_LEAK.search(prose_text):
        defects.append("leftover_markdown_fence")
    if PRETTIER_LEAK.search(prose_text):
        defects.append("leftover_mdx_tags")
    if len(text) < 40:
        defects.append("empty_or_stub_body")
    img_srcs: list[str] = []
    from .images import resolve_epub_img_src

    for img in soup.find_all("img"):
        src = (img.get("src") or "").strip()
        img_srcs.append(src)
        if not src:
            defects.append("empty_img_src")
            continue
        if REMOTE_SRC.search(src) or src.startswith("https://") or src.startswith("http://"):
            defects.append(f"remote_img_src:{src}")
            continue
        if zip_names is not None and not resolve_epub_img_src(chapter, src, zip_names):
            defects.append(f"broken_img_src:{src}")
    return defects, len(text), img_srcs


def walk_chapters(epub_path: Path, expected_routes: int | None = None) -> WalkReport:
    epub_path = Path(epub_path)
    results: list[ChapterResult] = []
    with zipfile.ZipFile(epub_path) as zf:
        zip_names = set(zf.namelist())
        for name in _chapter_names(zf):
            html = zf.read(name).decode("utf-8", errors="replace")
            for label, fragment in _page_units(name, html):
                defects, chars, img_srcs = inspect_fragment(
                    fragment, chapter=name, zip_names=zip_names
                )
                results.append(
                    ChapterResult(
                        chapter=label,
                        ok=not defects,
                        chars=chars,
                        defects=defects,
                        img_srcs=img_srcs,
                    )
                )
    if expected_routes is not None and len(results) != expected_routes:
        results.append(
            ChapterResult(
                chapter="__count__",
                ok=False,
                chars=0,
                defects=[f"chapter_count {len(results)} != expected_routes {expected_routes}"],
            )
        )
    fail = sum(1 for r in results if not r.ok)
    return WalkReport(
        epub=str(epub_path),
        chapter_count=len([r for r in results if r.chapter != "__count__"]),
        fail_count=fail,
        ok=fail == 0,
        chapters=results,
    )


def format_walk_log(report: WalkReport) -> str:
    lines = [
        f"epub {report.epub}",
        f"chapter_count {report.chapter_count}",
        f"fail_count {report.fail_count}",
        f"ok {report.ok}",
        "chapters:",
    ]
    for ch in report.chapters:
        status = "PASS" if ch.ok else "FAIL"
        extra = "" if ch.ok else " " + ",".join(ch.defects)
        lines.append(f"  {status} {ch.chapter} chars={ch.chars}{extra}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Walk every EPUB chapter for visual defects")
    parser.add_argument("--epub", required=True)
    parser.add_argument("--expected-routes", type=int, default=None)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    report = walk_chapters(Path(args.epub), expected_routes=args.expected_routes)
    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print(format_walk_log(report), end="")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
