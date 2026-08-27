"""Turn Mintlify MDX constructs into labeled, readable HTML/Markdown for EPUB."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import textwrap
from urllib.parse import urljoin

OPEN_TAG = re.compile(r"<([A-Za-z][\w.-]*)(\s[^>]*)?>")
RUNTIME_ASSIGN = re.compile(
    r"(?m)^(export\s+)?const\s+[A-Za-z_]\w*\s*=\s*(?:\(\s*\)\s*=>|useMemo\s*\(|useCallback\s*\(|useState\s*\()"
)


def looks_like_runtime_source(text: str) -> bool:
    """True when a Mintlify .md twin is React/MDX source, not readable markdown."""
    if not text:
        return False
    if re.search(r"(?m)^export\s+const\s+\w+\s*=", text):
        return True
    if "useMemo(" in text or "useCallback(" in text or "useState(" in text:
        return True
    if re.search(r"(?m)^import\s+.+\sfrom\s+['\"]react['\"]", text):
        return True
    return False


def _skip_balanced(text: str, start: int) -> int:
    """Return index after the statement that starts at start, using brace/paren depth."""
    opener = None
    i = start
    while i < len(text):
        ch = text[i]
        if ch in "{(":
            opener = ch
            break
        i += 1
    if opener is None:
        nl = text.find("\n", start)
        return len(text) if nl < 0 else nl + 1
    close = "}" if opener == "{" else ")"
    depth = 0
    in_str = None
    escape = False
    while i < len(text):
        ch = text[i]
        if in_str:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == in_str:
                in_str = None
            i += 1
            continue
        if ch in "\"'`":
            in_str = ch
            i += 1
            continue
        if ch == opener:
            depth += 1
        elif ch == close:
            depth -= 1
            if depth == 0:
                i += 1
                while i < len(text) and text[i] in " \t;":
                    i += 1
                if i < len(text) and text[i] == "\n":
                    i += 1
                return i
        i += 1
    return len(text)


def strip_runtime_source(md: str) -> str:
    """Drop export-const / useMemo islands so pandoc never prints React source."""
    text = md or ""
    guard = 0
    while guard < 80:
        guard += 1
        match = RUNTIME_ASSIGN.search(text)
        if not match:
            break
        # `useMemo(` already consumed '('; `() => {` must start at the body brace.
        cursor = match.end() - 1 if text[match.end() - 1 : match.end()] == "(" else match.end()
        end = _skip_balanced(text, cursor)
        text = text[: match.start()] + text[end:]
    return text


def _jsx_to_text(raw: str) -> str:
    text = raw or ""
    text = re.sub(
        r'<A\s+href="([^"]+)">([^<]*)</A>',
        lambda m: f"[{m.group(2)}]({m.group(1)})",
        text,
    )
    text = re.sub(r"<C>([\s\S]*?)</C>", r"`\1`", text)
    text = re.sub(r"\{['\"]([^'\"]*)['\"]\}", r"\1", text)
    text = re.sub(r"</?[A-Za-z][^>]*>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _quoted_field(chunk: str, name: str) -> str:
    match = re.search(rf"{name}:\s*'((?:\\'|[^'])*)'", chunk)
    if match:
        return match.group(1).replace("\\'", "'")
    match = re.search(rf"{name}:\s*<>", chunk)
    if not match:
        return ""
    start = match.end()
    end = chunk.find("</>", start)
    return _jsx_to_text(chunk[start:end] if end > 0 else chunk[start : start + 800])


def _example_field(chunk: str) -> str:
    match = re.search(r"example:\s*`([\s\S]*?)`", chunk)
    return match.group(1).strip() if match else ""


def _doc_href(href: str, page_url: str | None) -> str:
    if not href:
        return ""
    if href.startswith("http"):
        return href
    base = page_url or "https://code.claude.com/docs/en/"
    if href.startswith("/docs/"):
        return urljoin("https://code.claude.com", href)
    if href.startswith("/en/"):
        return urljoin("https://code.claude.com/docs", href)
    return urljoin(base if base.endswith("/") else base + "/", href.lstrip("/"))


def explorer_fragment(page_url: str | None) -> str:
    if page_url and page_url.rstrip("/").endswith("claude-directory"):
        return "explore-the-directory"
    return "explore-the-directory"


def extract_explorer_nodes(md: str) -> list[dict[str, str | list[str]]]:
    """Pull FILE_TREE file cards out of ClaudeExplorer MDX source."""
    nodes: list[dict[str, str | list[str]]] = []
    seen: set[str] = set()
    for part in re.split(r"\bid:\s*'", md or "")[1:]:
        nid, _, rest = part.partition("'")
        label = _quoted_field(rest, "label")
        if not label or label in seen:
            continue
        one = _quoted_field(rest, "oneLiner")
        desc = _quoted_field(rest, "description")
        when = _quoted_field(rest, "when")
        intro = _quoted_field(rest, "exampleIntro")
        example = _example_field(rest)
        docs = _quoted_field(rest, "docsLink")
        tips_raw = re.search(r"tips:\s*\[([\s\S]*?)\]\s*,", rest)
        tips: list[str] = []
        if tips_raw:
            inner = tips_raw.group(1)
            tips.extend(re.findall(r"'((?:\\'|[^'])*)'", inner))
            for frag in re.findall(r"<>([\s\S]*?)</>", inner):
                got = _jsx_to_text(frag)
                if got:
                    tips.append(got)
        if not (one or desc or example or tips):
            continue
        seen.add(label)
        nodes.append(
            {
                "id": nid,
                "label": label,
                "oneLiner": one,
                "when": when,
                "description": desc,
                "tips": tips,
                "exampleIntro": intro,
                "example": example,
                "docsLink": docs,
            }
        )
    return nodes


def render_explorer_fallback(md: str, page_url: str | None) -> str:
    """Static stand-in for interactive directory explorers that EPUB cannot run."""
    url = (page_url or "").split("?")[0].rstrip("/")
    if not url:
        url = "https://code.claude.com/docs/en/claude-directory"
    href = f"{url}#{explorer_fragment(url)}"
    parts = [
        '<aside class="mdx-live-widget">',
        '<p class="mdx-live-widget-label">Interactive explorer</p>',
        "<p>This directory tree is interactive on the original page and cannot run inside an EPUB. "
        f'Open it here: <a class="source-title" href="{html.escape(href, quote=True)}" rel="external">'
        f"{html.escape(href)}</a></p>",
        "</aside>",
    ]
    nodes = extract_explorer_nodes(md)
    if not nodes:
        return "\n".join(parts) + "\n"
    parts.append('<div class="mdx-file-index">')
    parts.append("<p>File-by-file notes from that explorer:</p>")
    for node in nodes:
        parts.append('<div class="mdx-file-card">')
        label = html.escape(str(node["label"]))
        docs = _doc_href(str(node.get("docsLink") or ""), page_url)
        heading = f"<code>{label}</code>"
        if docs:
            heading = (
                f'<a href="{html.escape(docs, quote=True)}" rel="external">{heading}</a>'
            )
        parts.append(f"<h3>{heading}</h3>")
        if node.get("oneLiner"):
            parts.append(f"<p>{html.escape(str(node['oneLiner']))}</p>")
        if node.get("when"):
            parts.append(
                f'<p class="mdx-when"><strong>When it loads.</strong> {html.escape(str(node["when"]))}</p>'
            )
        if node.get("description"):
            parts.append(f"<p>{html.escape(str(node['description']))}</p>")
        tips = node.get("tips") or []
        if isinstance(tips, list) and tips:
            parts.append("<p><strong>Tips</strong></p><ul>")
            for tip in tips:
                if tip:
                    parts.append(f"<li>{html.escape(str(tip))}</li>")
            parts.append("</ul>")
        if node.get("exampleIntro"):
            parts.append(f"<p>{html.escape(str(node['exampleIntro']))}</p>")
        if node.get("example"):
            parts.append(
                f"<pre><code>{html.escape(str(node['example']))}</code></pre>"
            )
        parts.append("</div>")
    parts.append("</div>")
    return "\n".join(parts) + "\n"


def merge_explorer_into_html(html_page: str, md: str, page_url: str | None) -> str:
    """Keep rendered article copy and splice in explorer notes + live link."""
    from bs4 import BeautifulSoup

    block = render_explorer_fallback(md, page_url)
    soup = BeautifulSoup(html_page, "lxml")
    article = soup.select_one("article") or soup.select_one("main") or soup.body
    if article is None:
        return html_page
    frag = BeautifulSoup(block, "lxml")
    root = frag.body if frag.body else frag
    children = [child.extract() for child in list(root.contents) if str(child).strip()]
    anchor = None
    for heading in article.find_all(["h2", "h3"]):
        if "explore" in heading.get_text(" ", strip=True).lower():
            anchor = heading
            break
    if anchor is None:
        anchor = article.find(["h1", "h2"])
    if anchor is not None:
        for child in reversed(children):
            anchor.insert_after(child)
    else:
        for child in reversed(children):
            article.insert(0, child)
    return str(soup)


def _attr(attrs: str, name: str) -> str:
    if not attrs:
        return ""
    match = re.search(
        rf'{name}\s*=\s*(?:\{{?\s*["\']([^"\']+)["\']\s*\}}?|([^\s>]+))',
        attrs,
        re.I,
    )
    if not match:
        return ""
    return (match.group(1) or match.group(2) or "").strip()


def _find_block(text: str, tag: str, start: int = 0) -> tuple[int, int, str, str] | None:
    open_re = re.compile(rf"<{re.escape(tag)}(\s[^>]*)?>", re.I)
    close_re = re.compile(rf"</{re.escape(tag)}>", re.I)
    opened = open_re.search(text, start)
    if not opened:
        return None
    depth = 1
    i = opened.end()
    while i < len(text) and depth:
        nxt_open = open_re.search(text, i)
        nxt_close = close_re.search(text, i)
        if nxt_close is None:
            return None
        if nxt_open and nxt_open.start() < nxt_close.start():
            depth += 1
            i = nxt_open.end()
            continue
        depth -= 1
        if depth == 0:
            inner = text[opened.end() : nxt_close.start()]
            return opened.start(), nxt_close.end(), opened.group(1) or "", inner
        i = nxt_close.end()
    return None


def _replace_innermost(text: str, tag: str, render) -> str:
    guard = 0
    while guard < 2000:
        guard += 1
        pos = 0
        chosen = None
        while True:
            found = _find_block(text, tag, pos)
            if not found:
                break
            start, end, attrs, inner = found
            if re.search(rf"<{re.escape(tag)}[\s>]", inner, re.I):
                pos = start + 1
                continue
            chosen = found
            break
        if chosen is None:
            break
        start, end, attrs, inner = chosen
        text = text[:start] + render(attrs, inner) + text[end:]
    return text


def _iter_children(inner: str, tag: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    pos = 0
    while True:
        found = _find_block(inner, tag, pos)
        if not found:
            break
        start, end, attrs, body = found
        out.append((attrs, body.strip("\n")))
        pos = end
    return out


FENCE_OPEN = re.compile(r"^([ \t]*)(`{3,}|~{3,})([^`\n]*)\s*$")
FENCE_CLOSE = re.compile(r"^([ \t]*)(`{3,}|~{3,})\s*$")


def _clean_info(info: str) -> str:
    info = re.sub(r"\s*theme=\{[^}]*\}", "", info or "")
    return re.sub(r"\s+", " ", info).strip()


def _scan_fences(lines: list[str]) -> list[tuple[int, int, str, str, str]]:
    """CommonMark fenced blocks: close only on a line of >= N of the same tick.

    Returns (start_idx, end_idx inclusive, ticks, info, body).
    """
    results: list[tuple[int, int, str, str, str]] = []
    i = 0
    while i < len(lines):
        opened = FENCE_OPEN.match(lines[i])
        if not opened:
            i += 1
            continue
        ticks = opened.group(2)
        info = opened.group(3) or ""
        n = len(ticks)
        mark = ticks[0]
        j = i + 1
        while j < len(lines):
            closed = FENCE_CLOSE.match(lines[j])
            if (
                closed
                and closed.group(2)[0] == mark
                and len(closed.group(2)) >= n
            ):
                body = "\n".join(lines[i + 1 : j])
                results.append((i, j, ticks, info, body))
                i = j + 1
                break
            j += 1
        else:
            body = "\n".join(lines[i + 1 :])
            results.append((i, len(lines) - 1, ticks, info, body))
            break
    return results


def clean_fence_headers(md: str) -> str:
    """Strip leaking fence attrs such as repeated theme={null}; keep tick count."""
    out: list[str] = []
    for ln in md.splitlines():
        opened = FENCE_OPEN.match(ln)
        if not opened:
            out.append(ln)
            continue
        indent, ticks, info = opened.group(1), opened.group(2), opened.group(3) or ""
        info = _clean_info(info)
        if info:
            out.append(f"{indent}{ticks} {info}")
        else:
            # Preserve closing fences and bare openers (``` / ````).
            out.append(f"{indent}{ticks}")
    text = "\n".join(out)
    if md.endswith("\n"):
        text += "\n"
    return re.sub(r"(?:\s*theme=\{null\})+", "", text)


def _is_html_line(ln: str) -> bool:
    s = ln.lstrip()
    return s.startswith("<") or s.startswith("&lt;")


def _fully_unindent(md: str) -> str:
    """Flush markdown lines to column 0 so nested <Tab> bodies are not code.

    Mintlify indents tab/callout bodies 4–8 spaces; a leftover 4-space indent
    makes pandoc wrap the whole body in <pre>. HTML already injected is left
    as-is (it is already a fragment).
    """
    out: list[str] = []
    for ln in (md or "").splitlines():
        if not ln.strip():
            out.append("")
            continue
        if _is_html_line(ln):
            out.append(ln.lstrip())
            continue
        out.append(ln.lstrip(" \t"))
    return "\n".join(out)


def _md_to_html(md: str) -> str:
    text = _fully_unindent(textwrap.dedent(md or "")).strip("\n")
    if not text.strip():
        return ""
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return text
    proc = subprocess.run(
        [
            pandoc,
            "-f",
            "markdown-tex_math_dollars-tex_math_single_backslash",
            "-t",
            "html",
        ],
        input=text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return text
    return proc.stdout.strip()


def _iter_fences(text: str) -> list[tuple[str, str, str]]:
    """Split a CodeGroup body into (lang, title, code) fences."""
    out: list[tuple[str, str, str]] = []
    for _start, _end, _ticks, info, body in _scan_fences(text.splitlines()):
        info = _clean_info(info)
        parts = info.split()
        lang = parts[0] if parts else ""
        title = " ".join(parts[1:]) if len(parts) > 1 else (lang or "Code")
        code = textwrap.dedent(body).rstrip("\n")
        out.append((lang, title, code))
    return out


def _render_codegroup(_attrs: str, inner: str) -> str:
    fences = _iter_fences(inner)
    if not fences:
        return _md_to_html(inner)
    parts = ['\n<div class="mdx-codegroup">']
    for lang, title, code in fences:
        cls = f' class="language-{html.escape(lang, quote=True)}"' if lang else ""
        parts.append('<div class="mdx-codepanel">')
        parts.append(f'<p class="mdx-codepanel-title">{html.escape("Code: " + title)}</p>')
        parts.append(f"<pre><code{cls}>{html.escape(code)}</code></pre>")
        parts.append("</div>")
    parts.append("</div>\n")
    return "\n".join(parts)


def _tab_labels(attrs: str) -> list[str]:
    return re.findall(r'label:\s*"([^"]+)"', attrs or "")


def _find_all_blocks(text: str, tag: str) -> list[tuple[int, int, str, str]]:
    out: list[tuple[int, int, str, str]] = []
    pos = 0
    while True:
        found = _find_block(text, tag, pos)
        if not found:
            break
        out.append(found)
        pos = found[1]
    return out


def _partition_around_spans(text: str, spans: list[tuple[int, int]]) -> list[str]:
    chunks: list[str] = []
    prev = 0
    for i, (start, end) in enumerate(spans):
        if i == 0:
            chunks.append(text[:end])
        else:
            chunks.append(text[prev:end])
        prev = end
    if chunks and prev < len(text) and text[prev:].strip():
        chunks[-1] += text[prev:]
    return chunks


def _split_tab_bodies(inner: str, n: int) -> list[str]:
    if n <= 1:
        return [inner]
    steps = _find_all_blocks(inner, "WorkflowSteps")
    if len(steps) == n:
        return _partition_around_spans(inner, [(s[0], s[1]) for s in steps])
    fences = _scan_fences(inner.splitlines())
    if len(fences) == n:
        lines = inner.splitlines(keepends=True)
        # Map line indexes to string offsets.
        offsets = [0]
        for ln in lines:
            offsets.append(offsets[-1] + len(ln))
        spans = [(offsets[s], offsets[e + 1] if e + 1 < len(offsets) else len(inner)) for s, e, *_ in fences]
        return _partition_around_spans(inner, spans)
    chunks = [c.strip("\n") for c in re.split(r"\n[ \t]*\n[ \t]*\n+", inner) if c.strip()]
    if len(chunks) == n:
        return chunks
    if len(chunks) > n:
        return chunks[: n - 1] + ["\n\n".join(chunks[n - 1 :])]
    if chunks:
        return chunks + [""] * (n - len(chunks))
    return [inner] + [""] * (n - 1)


def _render_tabs(attrs: str, inner: str) -> str:
    tabs = _iter_children(inner, "Tab")
    parts = ['\n<div class="mdx-tabs">']
    if tabs:
        for child_attrs, body in tabs:
            title = _attr(child_attrs, "title") or "Tab"
            parts.append('<div class="mdx-tab">')
            parts.append(f'<p class="mdx-tab-title">{html.escape("Tab: " + title)}</p>')
            parts.append(_tab_body_html(body))
            parts.append("</div>")
        parts.append("</div>\n")
        return "\n".join(parts)
    labels = _tab_labels(attrs)
    if labels:
        bodies = _split_tab_bodies(inner, len(labels))
        for title, body in zip(labels, bodies):
            parts.append('<div class="mdx-tab">')
            parts.append(f'<p class="mdx-tab-title">{html.escape("Tab: " + title)}</p>')
            parts.append(_tab_body_html(body))
            parts.append("</div>")
        parts.append("</div>\n")
        return "\n".join(parts)
    return inner.strip()


def _tab_body_html(body: str) -> str:
    text = _replace_innermost(body, "WorkflowSteps", _render_workflow_steps)
    text = convert_remaining_fences(text)
    return _md_to_html(text)


def _render_callout(kind: str, _attrs: str, inner: str) -> str:
    label = kind.capitalize()
    body = _md_to_html(inner)
    return (
        f'\n<aside class="mdx-callout mdx-{kind.lower()}">'
        f'<p class="mdx-callout-label">{html.escape(label)}</p>\n'
        f"{body}\n</aside>\n"
    )


def _render_accordion(_attrs: str, inner: str) -> str:
    items = _iter_children(inner, "Accordion")
    if not items:
        title = _attr(_attrs, "title") or "Details"
        return (
            f'\n<div class="mdx-accordion">'
            f'<p class="mdx-accordion-title">{html.escape(title)}</p>\n'
            f"{_md_to_html(inner)}\n</div>\n"
        )
    parts = ['\n<div class="mdx-accordion-group">']
    for attrs, body in items:
        title = _attr(attrs, "title") or "Details"
        parts.append('<div class="mdx-accordion">')
        parts.append(f'<p class="mdx-accordion-title">{html.escape(title)}</p>')
        parts.append(_md_to_html(body))
        parts.append("</div>")
    parts.append("</div>\n")
    return "\n".join(parts)


def _render_steps(_attrs: str, inner: str) -> str:
    steps = _iter_children(inner, "Step")
    if not steps:
        return inner.strip()
    parts = ['\n<ol class="mdx-steps">']
    for i, (attrs, body) in enumerate(steps, start=1):
        title = _attr(attrs, "title")
        parts.append("<li class=\"mdx-step\">")
        if title:
            parts.append(f'<p class="mdx-step-title">{html.escape(f"{i}. {title}")}</p>')
        parts.append(_md_to_html(body))
        parts.append("</li>")
    parts.append("</ol>\n")
    return "\n".join(parts)


def _render_workflow_steps(_attrs: str, inner: str) -> str:
    """Numbered setup steps with heading+body stay as a readable ordered list."""
    return f'\n<div class="mdx-steps">\n{_md_to_html(inner)}\n</div>\n'


def _find_jsx(text: str, tag: str, start: int = 0) -> tuple[int, int, str, str] | None:
    """Find <Tag ... /> or <Tag ...>inner</Tag>, allowing nested `{...}` in attrs."""
    open_re = re.compile(rf"<{re.escape(tag)}(?=[\s>/])", re.I)
    opened = open_re.search(text, start)
    if not opened:
        return None
    i = opened.end()
    in_str: str | None = None
    brace = 0
    attr_start = i
    while i < len(text):
        c = text[i]
        if in_str:
            if c == "\\" and i + 1 < len(text):
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in {'"', "'"}:
            in_str = c
            i += 1
            continue
        if c == "{":
            brace += 1
            i += 1
            continue
        if c == "}":
            brace = max(0, brace - 1)
            i += 1
            continue
        if brace:
            i += 1
            continue
        if text.startswith("/>", i):
            attrs = text[attr_start:i]
            return opened.start(), i + 2, attrs, ""
        if c == ">":
            attrs = text[attr_start:i]
            inner_start = i + 1
            close = re.search(rf"</{re.escape(tag)}>", text[inner_start:], re.I)
            if not close:
                return None
            inner = text[inner_start : inner_start + close.start()]
            return opened.start(), inner_start + close.end(), attrs, inner
        i += 1
    return None


def _replace_jsx(text: str, tag: str, render) -> str:
    guard = 0
    pos = 0
    while guard < 4000:
        guard += 1
        found = _find_jsx(text, tag, pos)
        if not found:
            break
        start, end, attrs, inner = found
        text = text[:start] + render(attrs, inner) + text[end:]
        pos = start
    return text


def _skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i] in " \t\n\r":
        i += 1
    return i


def _parse_js_string(s: str, i: int) -> tuple[str, int]:
    quote = s[i]
    i += 1
    out: list[str] = []
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            out.append(s[i + 1])
            i += 2
            continue
        if c == quote:
            return "".join(out), i + 1
        out.append(c)
        i += 1
    return "".join(out), i


def _parse_js(s: str, i: int = 0):
    i = _skip_ws(s, i)
    if i >= len(s):
        return None, i
    c = s[i]
    if c in {'"', "'", "`"}:
        return _parse_js_string(s, i)
    if s.startswith("true", i) and (i + 4 == len(s) or not s[i + 4].isalnum()):
        return True, i + 4
    if s.startswith("false", i) and (i + 5 == len(s) or not s[i + 5].isalnum()):
        return False, i + 5
    if s.startswith("null", i) and (i + 4 == len(s) or not s[i + 4].isalnum()):
        return None, i + 4
    if c == "-" or c.isdigit():
        m = re.match(r"-?\d+(?:\.\d+)?", s[i:])
        if m:
            raw = m.group(0)
            num: int | float = float(raw) if "." in raw else int(raw)
            return num, i + len(raw)
    if c == "[":
        i += 1
        items = []
        while True:
            i = _skip_ws(s, i)
            if i < len(s) and s[i] == "]":
                return items, i + 1
            val, i = _parse_js(s, i)
            items.append(val)
            i = _skip_ws(s, i)
            if i < len(s) and s[i] == ",":
                i += 1
                continue
            if i < len(s) and s[i] == "]":
                return items, i + 1
            return items, i
    if c == "{":
        i += 1
        obj: dict = {}
        while True:
            i = _skip_ws(s, i)
            if i < len(s) and s[i] == "}":
                return obj, i + 1
            if i < len(s) and s[i] in {'"', "'", "`"}:
                key, i = _parse_js_string(s, i)
            else:
                m = re.match(r"[A-Za-z_$][\w$]*", s[i:])
                if not m:
                    return obj, i
                key = m.group(0)
                i += len(key)
            i = _skip_ws(s, i)
            if i < len(s) and s[i] == ":":
                i += 1
            val, i = _parse_js(s, i)
            obj[key] = val
            i = _skip_ws(s, i)
            if i < len(s) and s[i] == ",":
                i += 1
                continue
            if i < len(s) and s[i] == "}":
                return obj, i + 1
            return obj, i
    m = re.match(r"[A-Za-z_$][\w$]*", s[i:])
    if m:
        return m.group(0), i + len(m.group(0))
    return None, i


def _jsx_expr(attrs: str, name: str):
    if not attrs:
        return None
    match = re.search(rf"{re.escape(name)}\s*=\s*\{{", attrs)
    if not match:
        return None
    val, _ = _parse_js(attrs, match.end())
    return val


def _table(headers: list[str], rows: list[list[str]]) -> str:
    parts = ['\n<table class="mdx-table"><thead><tr>']
    for h in headers:
        parts.append(f"<th>{html.escape(h)}</th>")
    parts.append("</tr></thead><tbody>")
    for row in rows:
        parts.append("<tr>")
        for cell in row:
            parts.append(f"<td>{html.escape(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>\n")
    return "".join(parts)


def _render_glossary(_attrs: str, _inner: str) -> str:
    options = _jsx_expr(_attrs, "options") or []
    rows = []
    for item in options:
        if not isinstance(item, dict):
            continue
        rows.append(
            [
                str(item.get("key") or ""),
                str(item.get("appliesTo") or ""),
                str(item.get("description") or ""),
            ]
        )
    if not rows:
        return ""
    return _table(["Term", "Applies to", "Definition"], rows)


def _render_config_table(_attrs: str, _inner: str) -> str:
    options = _jsx_expr(_attrs, "options") or []
    rows = []
    for item in options:
        if not isinstance(item, dict):
            continue
        rows.append(
            [
                str(item.get("key") or ""),
                str(item.get("type") or ""),
                str(item.get("description") or ""),
            ]
        )
    if not rows:
        return ""
    return _table(["Key", "Type", "Description"], rows)


def _render_tree_items(items) -> str:
    if not isinstance(items, list) or not items:
        return ""
    parts = ["<ul>"]
    for item in items:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "")
        comment = str(item.get("comment") or "")
        label = html.escape(name)
        if comment:
            label += f" — {html.escape(comment)}"
        parts.append(f"<li>{label}")
        children = item.get("children") or []
        nested = _render_tree_items(children)
        if nested:
            parts.append(nested)
        parts.append("</li>")
    parts.append("</ul>")
    return "\n".join(parts)


def _render_file_tree(_attrs: str, _inner: str) -> str:
    tree = _jsx_expr(_attrs, "tree") or []
    body = _render_tree_items(tree)
    if not body:
        return ""
    return f'\n<div class="mdx-filetree">{body}</div>\n'


def _render_model_details(_attrs: str, _inner: str) -> str:
    name = _attr(_attrs, "name") or _attr(_attrs, "imageLabel") or "Model"
    desc = _attr(_attrs, "description")
    data = _jsx_expr(_attrs, "data") or {}
    features = data.get("features") if isinstance(data, dict) else []
    parts = ['\n<div class="mdx-model">', f"<p><strong>{html.escape(name)}</strong></p>"]
    if desc:
        parts.append(f"<p>{html.escape(desc)}</p>")
    if isinstance(features, list) and features:
        parts.append("<ul>")
        for feat in features:
            if not isinstance(feat, dict):
                continue
            title = str(feat.get("title") or "")
            value = feat.get("value")
            extra = ""
            if value is True:
                extra = " — yes"
            elif value is False:
                extra = " — no"
            elif value:
                extra = f" — {html.escape(str(value))}"
            parts.append(f"<li>{html.escape(title)}{extra}</li>")
        parts.append("</ul>")
    parts.append("</div>\n")
    return "\n".join(parts)


def _render_pricing_card(attrs: str, inner: str) -> str:
    name = _attr(attrs, "name") or "Plan"
    price = _attr(attrs, "price")
    interval = _attr(attrs, "interval")
    subtitle = _attr(attrs, "subtitle")
    bits = [html.escape(name)]
    if price:
        bits.append(html.escape(price + (interval or "")))
    parts = ['\n<div class="mdx-price-card">', f"<p><strong>{' '.join(bits)}</strong></p>"]
    if subtitle:
        parts.append(f"<p>{html.escape(subtitle)}</p>")
    if inner and inner.strip():
        parts.append(_md_to_html(inner))
    parts.append("</div>\n")
    return "\n".join(parts)


def _render_table_wrapper(_attrs: str, inner: str) -> str:
    body = (inner or "").strip()
    if not body:
        return ""
    if re.search(r"<table\b", body, re.I):
        return f"\n{body}\n"
    return f'\n<table class="mdx-table">\n{body}\n</table>\n'


def _render_feature_matrix(_attrs: str, _inner: str) -> str:
    data = _jsx_expr(_attrs, "data") or {}
    if not isinstance(data, dict):
        return ""
    plans = data.get("plans") or []
    sections = data.get("sections") or []
    headers = ["Feature"] + [
        str(p.get("shortLabel") or p.get("label") or "")
        for p in plans
        if isinstance(p, dict)
    ]
    plan_ids = [str(p.get("id") or "") for p in plans if isinstance(p, dict)]
    rows = []
    for section in sections:
        if not isinstance(section, dict):
            continue
        for feat in section.get("features") or []:
            if not isinstance(feat, dict):
                continue
            avail = feat.get("availability") or {}
            row = [str(feat.get("name") or "")]
            for pid in plan_ids:
                row.append(str(avail.get(pid) or "") if isinstance(avail, dict) else "")
            rows.append(row)
    if not rows:
        return ""
    return _table(headers, rows)


def _render_collection_list(_attrs: str, _inner: str) -> str:
    slugs = _jsx_expr(_attrs, "slugs") or []
    if not isinstance(slugs, list) or not slugs:
        return ""
    items = "".join(f"<li>{html.escape(str(s))}</li>" for s in slugs)
    return f"\n<ul class=\"mdx-collection\">{items}</ul>\n"


def _render_toggle(attrs: str, inner: str) -> str:
    title = _attr(attrs, "title") or "Details"
    return (
        f'\n<div class="mdx-accordion">'
        f'<p class="mdx-accordion-title">{html.escape(title)}</p>\n'
        f"{_md_to_html(inner)}\n</div>\n"
    )


def _render_content_switcher(attrs: str, inner: str) -> str:
    options = _jsx_expr(attrs, "options") or []
    labels = []
    if isinstance(options, list):
        for item in options:
            if isinstance(item, dict):
                labels.append(str(item.get("label") or item.get("value") or "Tab"))
    if not labels:
        return inner.strip()
    bodies = _split_tab_bodies(inner, len(labels))
    parts = ['\n<div class="mdx-tabs">']
    for title, body in zip(labels, bodies):
        parts.append('<div class="mdx-tab">')
        parts.append(f'<p class="mdx-tab-title">{html.escape("Tab: " + title)}</p>')
        parts.append(_tab_body_html(body))
        parts.append("</div>")
    parts.append("</div>\n")
    return "\n".join(parts)


PASCAL_OPEN = re.compile(r"<([A-Z][A-Za-z0-9]*)(?=[\s/>])")
LEAKED_JSX_TEXT = re.compile(
    r"&lt;[A-Z][A-Za-z0-9]*\b[^<]*|<[A-Z][A-Za-z0-9]*\b[^<]*",
)


def _slurp_broken_jsx(text: str, start: int) -> int:
    i = start + 1
    while i < len(text) and text[i] not in "<\n":
        i += 1
    if i < len(text) and text.startswith("</", i):
        return i
    return i


def _close_raw_html_divs(text: str) -> str:
    """Balance leftover raw <div> islands from source pages (e.g. pricing footnotes)."""
    opens = len(re.findall(r"<div\b", text, flags=re.I))
    closes = len(re.findall(r"</div>", text, flags=re.I))
    if opens > closes:
        text = text + ("</div>" * (opens - closes))
    return text


def strip_remaining_jsx(text: str) -> str:
    """Drop leftover PascalCase islands; keep inner markdown when present."""
    guard = 0
    while guard < 4000:
        guard += 1
        match = PASCAL_OPEN.search(text)
        if not match:
            break
        tag = match.group(1)
        found = _find_jsx(text, tag, match.start())
        if not found:
            end = _slurp_broken_jsx(text, match.start())
            text = text[: match.start()] + text[end:]
            continue
        start, end, attrs, inner = found
        replacement = inner.strip("\n") if inner and inner.strip() else ""
        if not replacement:
            title = _attr(attrs, "title") or _attr(attrs, "name") or _attr(attrs, "label")
            if title:
                replacement = html.escape(title)
        text = text[:start] + replacement + text[end:]
    return text


def strip_leaked_jsx_text(text: str) -> str:
    """Remove escaped/unclosed PascalCase tags left in HTML text nodes."""
    return LEAKED_JSX_TEXT.sub("", text)


def _render_landing(attrs: str, _inner: str) -> str:
    title = _attr(attrs, "title") or "Overview"
    desc = _attr(attrs, "description")
    intro = _attr(attrs, "intro")
    pages = re.findall(
        r'title:\s*"([^"]+)"\s*,\s*description:\s*"([^"]*)"\s*,\s*href:\s*"([^"]+)"',
        attrs or "",
        re.S,
    )
    parts = ['\n<div class="mdx-landing">']
    parts.append(f"<h3>{html.escape(title)}</h3>")
    if desc:
        parts.append(f"<p>{html.escape(desc)}</p>")
    if intro:
        parts.append(f"<p>{html.escape(intro)}</p>")
    if pages:
        parts.append("<ul>")
        for page_title, page_desc, href in pages:
            parts.append(
                f"<li><strong>{html.escape(page_title)}</strong>"
                f" — {html.escape(page_desc)} ({html.escape(href)})</li>"
            )
        parts.append("</ul>")
    parts.append("</div>\n")
    return "\n".join(parts)


def _unwrap(_attrs: str, inner: str) -> str:
    return inner


ISLAND_TAGS = (
    "CodexAppDownloadCta",
    "ChatGPTModeDropdown",
    "ChatWorkSegmentPicker",
    "OpenBook",
    "CompareArrows",
    "PermissionModeSelectorDemo",
    "PromptComponent",
    "CodexOverviewLanding",
    "VideoPlayer",
    "CodexScreenshot",
    "CodexPetsDemo",
    "CodexModelSwitcher",
    "CodexReasoningLevelTerminal",
    "ComputerHistoryThreadDemo",
    "ServiceAccountsDemo",
    "PermissionModeSelectorDemo",
    "ElevatedRiskBadge",
    "CodexMicroTableKeycap",
    "CtaPillLink",
    "ButtonLink",
)


def strip_islands(text: str) -> str:
    for tag in ISLAND_TAGS:
        text = _replace_jsx(text, tag, lambda _a, inner: inner.strip("\n") if inner else "")
    return text


def strip_mdx_comments(text: str) -> str:
    return re.sub(r"\{/\*.*?\*/\}", "", text, flags=re.S)


def convert_remaining_fences(text: str) -> str:
    """Turn leftover fenced blocks into HTML. Close only on >= N matching ticks."""
    lines = text.splitlines()
    fences = _scan_fences(lines)
    if not fences:
        return text
    out: list[str] = []
    last = 0
    for start, end, _ticks, info, body in fences:
        out.extend(lines[last:start])
        info = _clean_info(info)
        lang = info.split()[0] if info else ""
        code = textwrap.dedent(body).rstrip("\n")
        cls = f' class="language-{html.escape(lang, quote=True)}"' if lang else ""
        out.append(f"<pre><code{cls}>{html.escape(code)}</code></pre>")
        last = end + 1
    out.extend(lines[last:])
    result = "\n".join(out)
    if text.endswith("\n"):
        result += "\n"
    return result


def transform_mdx(md: str, page_url: str | None = None) -> str:
    """Convert Mintlify/Starlight MDX in a docs page to readable Markdown/HTML."""
    extra = ""
    if looks_like_runtime_source(md) and ("FILE_TREE" in md or "ClaudeExplorer" in md):
        extra = render_explorer_fallback(md, page_url)
    text = strip_runtime_source(md)
    text = strip_mdx_comments(text)
    text = clean_fence_headers(text)
    text = _replace_jsx(text, "CodexDocsOverviewLanding", _render_landing)
    text = _replace_innermost(text, "ContentModeSwitch", _unwrap)
    text = _replace_jsx(text, "GlossaryTable", _render_glossary)
    text = _replace_jsx(text, "ConfigTable", _render_config_table)
    text = _replace_jsx(text, "FileTree", _render_file_tree)
    text = _replace_jsx(text, "ModelDetails", _render_model_details)
    text = _replace_jsx(text, "PricingCard", _render_pricing_card)
    text = _replace_jsx(text, "CodexPlanFeatureMatrix", _render_feature_matrix)
    text = _replace_jsx(text, "CodexCollectionList", _render_collection_list)
    text = _replace_jsx(text, "TableWrapper", _render_table_wrapper)
    text = _replace_innermost(text, "ToggleSection", _render_toggle)
    text = _replace_jsx(text, "ContentSwitcher", _render_content_switcher)
    text = strip_islands(text)
    for kind in ("Info", "Tip", "Warning", "Note", "Check", "WarningTip", "Alert", "CodexCallout"):
        text = _replace_innermost(
            text, kind, lambda attrs, inner, k=kind: _render_callout(k, attrs, inner)
        )
    text = _replace_innermost(text, "AccordionGroup", _render_accordion)
    text = _replace_innermost(text, "Accordion", _render_accordion)
    # CodeGroup before Tabs/Steps so nested fences become <pre><code>, not
    # leftover ``` paragraphs (pandoc would also treat bash $() as TeX).
    text = _replace_innermost(text, "CodeGroup", _render_codegroup)
    # Tabs before Steps: many Step bodies nest Tabs; converting Steps first
    # would pandoc-escape leftover <Tabs> into visible prose.
    text = _replace_innermost(text, "Tabs", _render_tabs)
    text = _replace_innermost(text, "WorkflowSteps", _render_workflow_steps)
    text = _replace_innermost(text, "Steps", _render_steps)
    text = strip_remaining_jsx(text)
    text = convert_remaining_fences(text)
    text = _close_raw_html_divs(text)
    if extra:
        return extra + "\n" + text
    return text
