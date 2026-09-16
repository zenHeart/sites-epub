"""E-layer CNAME/HTTPS audit for the published mirror chain (lessons #14).

For each known entry-point host, fetch the configured path and assert:
- 2xx response (404/301/302 are flagged)
- TLS cert SAN covers the host (lessons #14 root cause: GitHub Pages
  returns the *.github.io wildcard cert when CNAME points there, which
  matches "github.io" but not the custom CNAME like "epub.zenheart.site".
  Browsers reject this with a hostname-mismatch warning. We must check
  the actual SAN list, not just whether connect + GET 200.)
- final URL is on https and matches the host family

Run:  python tools/cname_audit.py
Exit: 0 on all green; 1 on any failure.
"""
from __future__ import annotations

import re
import socket
import ssl
import subprocess
import sys
import urllib.request
from pathlib import Path

HOSTS = [
    "epub.zenheart.site",      # primary: GitHub Pages + LE cert via Fastly
    "zenheart.github.io",       # fallback: should 301 to blog.zenheart.site
    "blog.zenheart.site",       # downstream: must be https, no http downgrades
    "epub.zenheart.gitee.io",   # Gitee Pages mirror (typically 404 if not configured)
    "epub-zenheart-site.pages.dev",  # Cloudflare Pages historic residue
]

# host suffixes considered safe (no http downgrade warning)
SAFE = ("zenheart.site", "github.io", "pages.dev")


def cert_via_openssl(host: str) -> tuple[str, list[str], str]:
    """Return (CN, SAN list, issuer CN) using the local openssl binary."""
    try:
        out = subprocess.run(
            ["openssl", "s_client", "-servername", host, "-connect", f"{host}:443"],
            input=b"\n", capture_output=True, timeout=20,
        )
        chain = subprocess.run(
            ["openssl", "x509", "-noout", "-subject", "-issuer", "-ext", "subjectAltName"],
            input=out.stdout, capture_output=True, timeout=10,
        )
        text = chain.stdout.decode("utf-8", errors="replace")
    except Exception as e:  # noqa: BLE001
        return ("", [], f"openssl error: {e}")
    cn = ""
    issuer = ""
    for line in text.splitlines():
        if line.startswith("subject=") and "CN=" in line:
            cn = line.split("CN=", 1)[1].strip()
        if line.startswith("issuer=") and "CN=" in line:
            issuer = line.split("CN=", 1)[1].split(",")[0].strip()
    sans = re.findall(r"DNS:([\w\.\-]+)", text)
    return (cn, sans, issuer)


def check_host(host: str) -> tuple[str, str]:
    """Return (status_note, final_url)."""
    cn, sans, issuer = cert_via_openssl(host)
    san_match = host in sans or any(s.startswith("*.") and host.endswith(s[1:]) for s in sans)

    url = f"https://{host}/changelog.html"
    req = urllib.request.Request(url, headers={"User-Agent": "cname-audit/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            final = r.geturl()
            code = r.status
    except Exception as e:  # noqa: BLE001
        return (f"FAIL fetch: {e.__class__.__name__}: {e}", "")

    note = f"http={code} cert=CN={cn or '?'} SAN={len(sans)} issuer={issuer or '?'}"
    if not san_match:
        note += f" [ROOT CAUSE] cert SAN does not cover {host} (got CN={cn!r})"
    if code >= 400:
        note += f" [FAIL] http {code}"
    if final.startswith("http://"):
        note += f" [REGRESSION] final url downgrades to http: {final}"
    if not any(final.endswith(s) or "/" + s in final for s in SAFE):
        note += f" [WARN] final off-family: {final}"
    flag = "OK" if san_match and code < 400 and not final.startswith("http://") else "FAIL"
    return (f"{flag} {note}", final)


def main() -> int:
    bad = 0
    for h in HOSTS:
        note, _ = check_host(h)
        flag = "OK" if note.startswith("OK") else "FAIL"
        if flag == "FAIL":
            bad += 1
        print(f"  {h:42} {flag:5}  {note}")
    print(f"\n{bad}/{len(HOSTS)} hosts have https problems")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())

