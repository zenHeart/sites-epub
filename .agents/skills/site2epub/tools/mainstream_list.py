"""Domain-level mainstream AI tool cross-check (site2epub 穷尽主流门禁).

Purpose: prevent the recurring failure mode (2026-09-16) where new
vendors were added one at a time as the user named them, instead of
being enumerated against current 2026 mainstream AI tool rankings.
This script enumerates the AI coding-assistant domain; mirror it for
other domains (model vendors, image/video, RAG platforms, etc.) by
adding more `LISTS` below and running with a domain arg.

Usage: python tools/mainstream_list.py [coding|chatbot|video|...]
       (no args -> all known domains)

Output: prints the deduplicated union of tools across the curated
sources for each domain so a maintainer can see whether the current
catalogue is missing any of them, and cross-checks against
catalog.json's vendor list to flag mismatches.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # tools -> .agents -> skill -> site/epub repo

LISTS = {
    "coding": [
        "https://pinggy.io/blog/best_ai_tools_for_coding/",
        "https://skills-hub.ai/best-ai-coding-tools",
        "https://automationswitch.com/ai-coding-assistants/ai-coding-assistants-scorecard",
        "https://amux.io/blog/best-ai-coding-tools-2026",
        "https://capitalandcompute.net/blog/new-agentic-code-editors-2026/",
    ],
    "model": [
        "https://m.toutiao.com/article/7649683752150467126",
        "https://xjzx.hut.edu.cn/info/1402/6015.htm",
    ],
}

TOOL_PATTERNS = {
    "coding": re.compile(
        r"\b(Claude Code|Cursor|Copilot|Antigravity|Codex|Codex CLI|Cline|Roo Code|Kilo Code|Continue|Aider|Aider|Gemini CLI|Grok Build|Amp|Droid|Goose|Windsurf|Kiro|Qodo|Augment|Warp|Zed|TRAE|Codebuddy|CodeBuddy|WorkBuddy|Tabnine|Supermaven|Codeium|Sourcegraph|Devin|Blitzy|OpenHands|OpenCode|Pi|JetBrains AI|Junie|Comate|Zencoder|Zcode)\b"
    ),
    "model": re.compile(
        r"\b(豆包|Doubao|Kimi|文心一言|Wenxin|通义千问|Tongyi|智谱清言|ChatGLM|腾讯元宝|Yuanbao|DeepSeek|MiniMax|MiniMax|讯飞星火|Xinghuo|CodeGeex|TRAE|ZCode|Z.ai|JieKou|Hunyuan|混元|StepFun|阶跃)\b"
    ),
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def extract(text: str, domain: str) -> set[str]:
    pat = TOOL_PATTERNS.get(domain)
    if not pat:
        return set()
    return {m.group(0) for m in pat.finditer(text)}


def main(argv: list[str]) -> int:
    targets = argv[1:] or list(LISTS.keys())
    catalog_path = ROOT / "catalog.json"
    catalog_vendors: set[str] = set()
    if catalog_path.is_file():
        try:
            d = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog_vendors = {v["id"] for v in d.get("vendors", [])}
        except Exception:  # noqa: BLE001
            pass

VENDOR_ALIAS = {
    "claude code": "claude", "claude": "claude",
    "cursor": "cursor",
    "codex": "codex", "codex cli": "codex",
    "antigravity": "gemini",       # 隶属 Google 会员产品集
    "gemini cli": "gemini",
    "grok build": "grok",
    "kiro": "(amazon, out of scope)",
    "warp": "(terminal, not a vendor)",
    "windsurf": "(windsurf / codeium, unmaintained — out of scope)",
    "augment": "(enterprise IDE, unconfirmed crawlable docs)",
    "tabnine": "(enterprise, unconfirmed crawlable docs)",
    "supermaven": "(early 2026 status, unconfirmed)",
    "codebuddy": "tencent", "workbuddy": "tencent",
    "trae": "bytedance (unconfirmed crawlable docs)",
    "qodo": "(PR review, unconfirmed crawlable docs)",
    "cline": "open-source (no vendor book, by design)",
    "continue": "open-source (no vendor book, by design)",
    "aider": "open-source (no vendor book, by design)",
    "kilo code": "open-source (no vendor book, by design)",
    "roo code": "open-source (no vendor book, by design)",
    "opencode": "open-source (no vendor book, by design)",
    "openhands": "open-source (no vendor book, by design)",
    "pi": "open-source (no vendor book, by design)",
    "goose": "open-source (no vendor book, by design)",
    "amp": "(sourcegraph — unconfirmed crawlable docs)",
    "droid": "(factory — unconfirmed crawlable docs)",
    "devin": "(autonomous, paywall — unconfirmed crawlable docs)",
    "blitzy": "(enterprise, no public docs)",
    "sourcegraph": "open-source (no vendor book)",
    "zed": "open-source (no vendor book, by design)",
    "jetbrains ai": "(jetbrains, unconfirmed crawlable docs)",
    "junie": "(jetbrains agent, unconfirmed)",
    "comate": "baidu (unconfirmed crawlable docs)",
    "zencoder": "zencoder (independent book)",
    "zcode": "zhipu (merged into vendor book)",
}


def main(argv: list[str]) -> int:
    targets = argv[1:] or list(LISTS.keys())
    catalog_path = ROOT / "catalog.json"
    catalog_vendors: set[str] = set()
    if catalog_path.is_file():
        try:
            d = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog_vendors = {v["id"] for v in d.get("vendors", [])}
        except Exception:  # noqa: BLE001
            pass

    for domain in targets:
        if domain not in LISTS:
            print(f"!! unknown domain: {domain}; known: {list(LISTS)}")
            continue
        union: set[str] = set()
        per_source: list[tuple[str, set[str]]] = []
        for src in LISTS[domain]:
            try:
                html = fetch(src)
            except Exception as e:  # noqa: BLE001
                print(f"  {domain:8} {src[:60]:60} -> fetch fail {e}")
                continue
            found = extract(html, domain)
            per_source.append((src, found))
            union |= found
        print(f"\n== {domain} (union {len(union)} tools across {len(per_source)} sources) ==")
        for t in sorted(union):
            sources = [s for s, f in per_source if t in f]
            mapping = VENDOR_ALIAS.get(t.lower(), "")
            if mapping in catalog_vendors:
                mark = f" [in book: {mapping}]"
            elif mapping:
                mark = f" [{mapping}]"
            else:
                mark = " [NOT MAPPED — decide]"
            print(f"  {t:20} {len(sources)}/{len(per_source)} sources{mark}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
