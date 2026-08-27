"""Vendor-organized site-docs + blog → EPUB."""

from .catalog import load_catalog, upsert_vendor
from .compile import compile_from_sources, discover_entries
from .models import IndexEntry, Vendor
from .walk import walk_chapters

__all__ = [
    "IndexEntry",
    "Vendor",
    "compile_from_sources",
    "discover_entries",
    "load_catalog",
    "upsert_vendor",
    "walk_chapters",
]
