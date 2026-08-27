"""Route content fingerprints for incremental rebuilds (hashes only, never cookies)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def content_hash(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def load_fingerprints(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return {str(k): str(v) for k, v in data.items()}
    return {}


def save_fingerprints(path: Path, fingerprints: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(fingerprints, indent=2, sort_keys=True) + "\n", encoding="utf-8")
