"""Static catalog page for gh-pages: one card per vendor, icon = cover."""

from __future__ import annotations

from pathlib import Path

from .catalog import load_catalog
from .models import Vendor

ROOT = Path(__file__).resolve().parents[1]


def render_index(vendors: list[Vendor] | None = None, *, dist_dir: Path | None = None) -> str:
    vendors = vendors if vendors is not None else load_catalog()
    cards = []
    for v in vendors:
        epub_name = f"{v.id}.epub"
        icon_href = f"icons/{v.id}.png"
        cards.append(
            f"""
            <a class="card" href="{epub_name}">
              <img class="cover" src="{icon_href}" alt="{v.name} icon">
              <h2>{v.name}</h2>
              <p>Download EPUB</p>
            </a>"""
        )
    cards_html = "\n".join(cards) if cards else "<p>No books yet.</p>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>site EPUB · zenheart</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
           margin: 0; background: #0c1115; color: #f4f0ea; }}
    main {{ max-width: 960px; margin: 0 auto; padding: 3rem 1.5rem; }}
    h1 {{ font-weight: 600; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
             gap: 1.5rem; margin-top: 2rem; }}
    .card {{ display: block; background: #171d24; border-radius: 16px; padding: 1.25rem;
             text-decoration: none; color: inherit; border: 1px solid #2a333d; }}
    .card:hover {{ border-color: #e07755; }}
    .cover {{ width: 96px; height: 96px; object-fit: contain; display: block; margin: 0 auto 1rem; }}
    h2 {{ text-align: center; margin: 0 0 .4rem; font-size: 1.15rem; }}
    p {{ text-align: center; margin: 0; color: #a4abb7; font-size: .9rem; }}
  </style>
</head>
<body>
  <main>
    <h1>site EPUB</h1>
    <p>Official product docs + blog, packed as EPUB.</p>
    <div class="grid">
      {cards_html}
    </div>
  </main>
</body>
</html>
"""


def write_site(dest: Path, vendors: list[Vendor] | None = None, dist: Path | None = None) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    vendors = vendors if vendors is not None else load_catalog()
    (dest / "index.html").write_text(render_index(vendors), encoding="utf-8")
    (dest / "CNAME").write_text("epub.zenheart.site\n", encoding="utf-8")
    icons = dest / "icons"
    icons.mkdir(exist_ok=True)
    root = ROOT
    for v in vendors:
        src = root / v.icon
        if src.is_file():
            (icons / f"{v.id}{src.suffix}").write_bytes(src.read_bytes())
            if src.suffix.lower() != ".png":
                # catalog always references .png; copy as-is too
                (icons / f"{v.id}.png").write_bytes(src.read_bytes())
        epub_src = (dist or root / "dist") / f"{v.id}.epub"
        if epub_src.is_file():
            (dest / f"{v.id}.epub").write_bytes(epub_src.read_bytes())
