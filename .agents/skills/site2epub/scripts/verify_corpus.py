#!/usr/bin/env python3
"""Per-route content gate and pre-pack size estimate (issue #2).

Two pipeline gaps made both of the 2026-10-10 defects visible only hours
after the work had started:

* **no per-route acceptance.**  Nothing measured how much body text a route
  actually carried.  cursor shipped 2334 of 4850 characters on one page and
  6361 of 12908 on another -- ``fetch`` reported ``ok:true`` and the gate only
  noticed hours later, by hand.
* **the size budget was checked after packing.**  A book that was over budget
  was met with five rounds of image compression, when the real problem was
  that the enumeration had collected 135 SEO routes it should never have
  taken (issue #3: *routes out of scope -> cut routes; routes in scope ->
  compress images*).

This gate runs between ``fetch`` and ``pack`` and reports:

1. **empty and shell pages** -- a route whose body text is empty, or shorter
   than ``SHELL_CHARS``, carries nothing;
2. **shrunk routes** -- a route whose corpus file lost more than half of its
   committed size.  This is the signal that catches an abridged ``.md`` twin:
   the page still exists, it just no longer holds the article;
3. **short routes** -- routes below half of their vendor's median, reported
   for review (a legitimately short page is normal; a *shrunk* one is not);
4. **the size estimate** -- referenced image bytes plus half the text bytes,
   compared against the 98MB budget, plus the growth against the previous
   committed corpus.

``--exact`` measures the body with the packer's own ``extract_page`` instead of
the cheap estimate (slower: it runs pandoc over every markdown page).

Usage::

    python3 .agents/skills/site2epub/scripts/verify_corpus.py [vendor_id ...]
    python3 .agents/skills/site2epub/scripts/verify_corpus.py --exact
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

#: A route whose body text is shorter than this is a shell page.  The threshold
#: matches the packer's own ``empty_or_stub_body`` defect (sites_epub/walk.py),
#: so this gate and the CI gate agree on what "empty" means.
SHELL_CHARS = 40
#: Between the shell threshold and this one a page is merely thin -- reported
#: for review, not a failure.  Known SPA product pages (kimi's landing pages,
#: minimax's hailuo pages) sit in this band: the site renders them client-side,
#: so the corpus only ever holds the title.
THIN_CHARS = 120
#: A route below this fraction of its vendor's median is listed for review.
SHORT_RATIO = 0.5
#: A route that lost more than this share of its committed size has shrunk.
SHRINK_RATIO = 0.5
#: Only a committed page above this size counts as "substantial" for the
#: shrink rule, so that tiny stubs do not produce noise.
SHRINK_MIN_BYTES = 2000
#: GitHub rejects pushes over 100MB; the CI gate is at 98MB.
SIZE_BUDGET = 98 * 1000 * 1000
#: Text contributes roughly half of its byte count to the packed book.
TEXT_WEIGHT = 0.5
#: Only an estimate this far over the budget is a hard failure; between 1.0x
#: and 1.5x the book is reported as close to the limit.
SIZE_FAIL_FACTOR = 1.5
#: A corpus that grew this many times over the previous round is an
#: enumeration problem, not a compression problem (issue #3).
GROWTH_FAIL_FACTOR = 3.0

TAG_RE = re.compile(r"<[^>]+>")
MARKDOWN_NOISE_RE = re.compile(r"[#*_>`\[\]()!|]|^\s*[-=]{3,}\s*$", re.M)
IMG_URL_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)|<img[^>]+src=[\"']([^\"']+)", re.I)
#: Script/style/template *contents* are code, not prose.  The sanitizer strips
#: them from the corpus (scripts/sanitize_corpus_html.py), and a page whose
#: only loss is that payload has not lost any content -- it has been cleaned.
#: Measured on 2026-11-26: zhipu's zcode-changelog went from 109KB to 44KB
#: because ~65KB of inline JavaScript (a GTM snippet plus the hydration blob)
#: was removed.  Its prose was byte-identical before and after (3719 chars).
SCRIPT_BLOCK_RE = re.compile(
    r"<(script|style|template)\b[^>]*>.*?</\1\s*>", re.S | re.I
)


def _text_len(raw: str) -> int:
    """Cheap body-text length: markup and markdown syntax removed."""
    if not raw:
        return 0
    text = TAG_RE.sub(" ", raw)
    text = MARKDOWN_NOISE_RE.sub(" ", text)
    return len(re.sub(r"\s+", " ", text).strip())


def _prose_len(raw: str) -> int:
    """Body-text length with script/style/template contents removed.

    Used for the shrink rule, where both sides must be measured the same way:
    the committed page still carries the inline JavaScript that the sanitizer
    strips from the working tree, so comparing raw bytes would report a
    content loss that never happened.
    """
    if not raw:
        return 0
    return _text_len(SCRIPT_BLOCK_RE.sub(" ", raw))


def _exact_text_len(raw: str, url: str) -> int:
    """Body-text length as the packer measures it (runs pandoc for markdown)."""
    try:
        from sites_epub.page import extract_page

        kind = "html" if raw.lstrip().lower().startswith("<!") else "md"
        page = extract_page(raw, url=url, kind=kind)
    except Exception:
        return 0
    return len((page.body_text or "").strip())


def _committed_sizes(rel: str, root: Path | None = None) -> dict[str, int]:
    """Byte size of every committed file under ``rel`` (path -> size)."""
    root = Path(root) if root else ROOT
    res = subprocess.run(
        ["git", "ls-tree", "-r", "-l", "HEAD", "--", rel],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        return {}
    sizes: dict[str, int] = {}
    for line in res.stdout.splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) < 4 or parts[3] == "-":
            continue  # a tree, not a blob
        try:
            sizes[path] = int(parts[3])
        except ValueError:
            continue
    return sizes


def _git_show_text(rel: str, root: Path | None = None) -> str | None:
    """The committed content of one file, or None if it is not in HEAD."""
    root = Path(root) if root else ROOT
    res = subprocess.run(
        ["git", "show", f"HEAD:{rel}"],
        cwd=root,
        capture_output=True,
    )
    if res.returncode != 0:
        return None
    return res.stdout.decode("utf-8", errors="replace")


def _referenced_images(corpus: Path, pages: dict[str, str]) -> int:
    """Bytes of the images the pages actually reference."""
    map_path = corpus / "image-map.json"
    if not map_path.is_file():
        return 0
    try:
        mapping = json.loads(map_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return 0
    used: set[str] = set()
    for raw in pages.values():
        for match in IMG_URL_RE.finditer(raw):
            url = match.group(1) or match.group(2)
            name = mapping.get(url)
            if name:
                used.add(name)
    total = 0
    for name in used:
        path = corpus / "images" / name
        if path.is_file():
            total += path.stat().st_size
    return total


def check_vendor(vid: str, *, exact: bool = False, root: Path | None = None) -> dict:
    root = Path(root) if root else ROOT
    corpus = root / "vendors" / vid / "corpus"
    routes_path = corpus / "routes.json"
    result: dict[str, object] = {"vendor": vid, "routes": 0, "problems": [], "notes": []}
    if not routes_path.is_file():
        return result
    routes = json.loads(routes_path.read_text(encoding="utf-8"))
    pages: dict[str, str] = {}
    lengths: list[tuple[str, int]] = []
    page_bytes: dict[str, int] = {}
    for route in routes:
        name = route.get("route")
        if not name:
            continue
        path = corpus / "pages" / f"{name}.md"
        if not path.is_file():
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        pages[name] = raw
        page_bytes[name] = path.stat().st_size
        url = route.get("url") or route.get("html_url") or ""
        length = _exact_text_len(raw, url) if exact else _text_len(raw)
        lengths.append((name, length))
    result["routes"] = len(routes)

    problems: list[str] = result["problems"]  # type: ignore[assignment]
    notes: list[str] = result["notes"]  # type: ignore[assignment]
    if not lengths:
        return result
    measured = sorted(n for _, n in lengths)
    median = measured[len(measured) // 2]
    empty = [name for name, n in lengths if n == 0]
    shells = [name for name, n in lengths if 0 < n < SHELL_CHARS]
    thin = [name for name, n in lengths if SHELL_CHARS <= n < THIN_CHARS]
    short = [
        name
        for name, n in lengths
        if n >= THIN_CHARS and median and n < median * SHORT_RATIO
    ]
    if empty:
        problems.append(f"{len(empty)} route(s) with an empty body: {empty[:8]}")
    if shells:
        problems.append(f"{len(shells)} shell page(s) under {SHELL_CHARS} chars: {shells[:8]}")
    if thin:
        notes.append(
            f"{len(thin)} thin page(s) under {THIN_CHARS} chars (client-rendered SPA "
            f"pages land here): {thin[:8]}"
        )
    if short:
        notes.append(
            f"{len(short)} route(s) under {int(SHORT_RATIO * 100)}% of the median "
            f"({median} chars) -- review if unexpected: {short[:8]}"
        )
    result["empty_pages"] = len(empty)
    result["shell_pages"] = len(shells)
    result["thin_pages"] = len(thin)
    result["short_pages"] = len(short)
    result["median_chars"] = median

    # Shrink detection: the route still exists but no longer holds the article.
    #
    # The cheap byte comparison is only a pre-filter.  A page can lose bytes
    # without losing content -- the sanitizer strips inline <script> blocks
    # from the corpus, and on 2026-11-26 that made zhipu's zcode-changelog look
    # like it had lost 60% of itself while its prose stayed byte-identical.
    # So every candidate is re-measured as prose against the committed blob,
    # and only a real prose loss counts.
    committed = _committed_sizes(f"vendors/{vid}/corpus/pages", root)
    shrunk: list[str] = []
    cleaned: list[str] = []
    for name, size in page_bytes.items():
        rel = f"vendors/{vid}/corpus/pages/{name}.md"
        old = committed.get(rel)
        if not old or old < SHRINK_MIN_BYTES:
            continue
        if size >= old * SHRINK_RATIO:
            continue
        old_raw = _git_show_text(rel, root)
        if old_raw is None:
            shrunk.append(f"{name} ({size}B of {old}B)")
            continue
        old_prose = _prose_len(old_raw)
        new_prose = _prose_len(pages.get(name, ""))
        if old_prose and new_prose < old_prose * SHRINK_RATIO:
            shrunk.append(
                f"{name} ({new_prose} prose chars of {old_prose})"
            )
        else:
            # Bytes went down, prose did not: the payload that went away was
            # script/style boilerplate, i.e. a cleanup, not a content loss.
            cleaned.append(f"{name} ({size}B of {old}B, prose kept)")
    if shrunk:
        problems.append(
            f"{len(shrunk)} route(s) lost more than half their committed prose "
            f"(possible abridged source): {shrunk[:8]}"
        )
    result["shrunk_pages"] = len(shrunk)
    result["cleaned_pages"] = len(cleaned)

    image_bytes = _referenced_images(corpus, pages)
    text_bytes = sum(len(raw) for raw in pages.values())
    estimate = int(image_bytes + TEXT_WEIGHT * text_bytes)
    result["image_mb"] = round(image_bytes / 1e6, 1)
    result["text_mb"] = round(text_bytes / 1e6, 1)
    result["estimate_mb"] = round(estimate / 1e6, 1)
    if estimate > SIZE_BUDGET * SIZE_FAIL_FACTOR:
        problems.append(
            f"estimated {estimate / 1e6:.1f}MB is over the {SIZE_BUDGET / 1e6:.0f}MB budget: "
            "cut out-of-scope routes first, do not start an image-compression loop"
        )
    elif estimate > SIZE_BUDGET:
        notes.append(
            f"estimated {estimate / 1e6:.1f}MB is close to the {SIZE_BUDGET / 1e6:.0f}MB budget: "
            "check the out-of-scope share before packing"
        )

    prev_text = sum(committed.values())
    if prev_text and text_bytes > prev_text * GROWTH_FAIL_FACTOR:
        problems.append(
            f"corpus text grew {text_bytes / prev_text:.1f}x against the previous commit "
            f"({prev_text / 1e6:.1f}MB -> {text_bytes / 1e6:.1f}MB): check the enumeration "
            "before compressing anything"
        )
    return result


def main(argv: list[str]) -> int:
    exact = "--exact" in argv
    vids = [a for a in argv if not a.startswith("-")]
    if not vids:
        vids = sorted(
            p.name for p in (ROOT / "vendors").iterdir() if (p / "corpus" / "routes.json").is_file()
        )
    failed = 0
    for vid in vids:
        result = check_vendor(vid, exact=exact)
        problems = result["problems"]  # type: ignore[assignment]
        notes = result["notes"]  # type: ignore[assignment]
        print(json.dumps({k: v for k, v in result.items() if k not in {"problems", "notes"}}, ensure_ascii=False))
        for note in notes:
            print(f"  NOTE {note}")
        for problem in problems:
            print(f"  FAIL {problem}")
        if problems:
            failed += 1
    print("\nPROBLEMS: none" if not failed else f"\nPROBLEMS: {failed} vendor(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
