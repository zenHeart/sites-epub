"""HTTP fetch used by the local crawl entry point. Disabled when SITESEPUB_OFFLINE=1."""

from __future__ import annotations

import http.cookiejar
import os
import time
import urllib.error
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

# Cookie-aware opener: devsite sites (e.g. ai.google.dev) answer plain requests
# with a Set-Cookie + self-redirect loop that deadlocks urllib's redirect handler.
_OPENER = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
)


def fetch_bytes(url: str, timeout: int = 60, retries: int = 3) -> tuple[bytes, str | None]:
    if os.environ.get("SITESEPUB_OFFLINE"):
        raise RuntimeError(f"offline: live fetch disabled ({url})")
    last_err: Exception | None = None
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    for attempt in range(retries):
        try:
            with _OPENER.open(req, timeout=timeout) as resp:
                return resp.read(), resp.headers.get("Content-Type")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_err = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"fetch failed after {retries} tries: {url}: {last_err}")


def fetch_text(url: str, timeout: int = 60) -> str:
    data, _ = fetch_bytes(url, timeout=timeout)
    return data.decode("utf-8", errors="replace")
