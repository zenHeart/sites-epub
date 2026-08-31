"""HTTP fetch used by the local crawl entry point. Disabled when SITESEPUB_OFFLINE=1."""

from __future__ import annotations

import gzip
import http.cookiejar
import os
import time
import urllib.error
import urllib.request
import zlib

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# Cookie-aware opener: devsite sites (e.g. ai.google.dev) answer plain requests
# with a Set-Cookie + self-redirect loop that deadlocks urllib's redirect handler.
_OPENER = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
)


def _decode_body(data: bytes, encoding: str | None) -> bytes:
    """Undo Content-Encoding. urllib does not decompress; some hosts (antigravity
    .google) gzip responses regardless, and storing the raw bytes is what produced
    mojibake titles in the packed TOC."""
    enc = (encoding or "").lower().strip()
    if enc == "gzip" or (not enc and data[:2] == b"\x1f\x8b"):
        return gzip.decompress(data)
    if enc == "deflate":
        try:
            return zlib.decompress(data)
        except zlib.error:
            return zlib.decompress(data, -zlib.MAX_WBITS)
    return data


def fetch_bytes(url: str, timeout: int = 60, retries: int = 3) -> tuple[bytes, str | None]:
    if os.environ.get("SITESEPUB_OFFLINE"):
        raise RuntimeError(f"offline: live fetch disabled ({url})")
    last_err: Exception | None = None
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            # Explicit gzip only (never brotli, which stdlib cannot decode);
            # antigravity.google gzipped even identity-less requests.
            "Accept-Encoding": "gzip",
        },
    )
    for attempt in range(retries):
        try:
            with _OPENER.open(req, timeout=timeout) as resp:
                body = _decode_body(resp.read(), resp.headers.get("Content-Encoding"))
                return body, resp.headers.get("Content-Type")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_err = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"fetch failed after {retries} tries: {url}: {last_err}")


def fetch_text(url: str, timeout: int = 60) -> str:
    data, _ = fetch_bytes(url, timeout=timeout)
    return data.decode("utf-8", errors="replace")
