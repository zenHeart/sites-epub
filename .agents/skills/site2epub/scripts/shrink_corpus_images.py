"""Recompress oversized corpus images to JPEG in place; keep image-map.json consistent.

Usage: python shrink_corpus_images.py <vendor_id> [--threshold 400000] [--max-width 1400]

Why: GitHub rejects gh-pages pushes containing files over 100MB (lessons #11).
Readers-scale JPEG q80 keeps the book readable while fitting the gate. Files that
do not shrink (or animated .gif) are kept as-is; image-map.json values are renamed
with the extension so page sources stay untouched (they reference URLs, not files).
"""
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]


def main(vendor: str, threshold: int, max_width: int) -> int:
    img_dir = ROOT / "vendors" / vendor / "corpus" / "images"
    map_path = ROOT / "vendors" / vendor / "corpus" / "image-map.json"
    if not img_dir.is_dir():
        print(f"no images for {vendor}: {img_dir}")
        return 1
    mapping = json.loads(map_path.read_text(encoding="utf-8"))
    reverse = {v: k for k, v in mapping.items()}

    saved = changed = 0
    for p in sorted(img_dir.iterdir()):
        if p.suffix.lower() == ".gif" or p.stat().st_size <= threshold:
            continue
        try:
            im = Image.open(p)
            im.load()
        except Exception:  # noqa: BLE001
            continue
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            base = Image.new("RGB", im.size, (255, 255, 255))
            base.paste(im, mask=im.split()[-1])
            im = base
        elif im.mode != "RGB":
            im = im.convert("RGB")
        if im.width > max_width:
            im = im.resize((max_width, round(im.height * max_width / im.width)), Image.LANCZOS)
        out = img_dir / (p.stem + ".jpg")
        im.save(out, "JPEG", quality=80, optimize=True)
        if out.stat().st_size >= p.stat().st_size:
            out.unlink()
            continue
        saved += p.stat().st_size - out.stat().st_size
        p.unlink()
        url = reverse.get(p.name)
        if url:
            mapping[url] = out.name
        changed += 1
    map_path.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
    total = sum(q.stat().st_size for q in img_dir.iterdir())
    print(f"{vendor}: recompressed {changed}, saved {saved/1e6:.1f}MB, images now {total/1e6:.1f}MB")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        raise SystemExit(2)
    vid = args[0]
    thr = int(args[args.index("--threshold") + 1]) if "--threshold" in args else 400_000
    width = int(args[args.index("--max-width") + 1]) if "--max-width" in args else 1400
    raise SystemExit(main(vid, thr, width))
