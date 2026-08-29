"""Regenerate sitemap.xml with a per-language entry and reciprocal hreflang alternates.

Every language version gets its **own** `<url>` entry, and each entry lists every language
including itself plus `x-default`. Listing the English URL once with alternates hanging off it is
the common shortcut and it under-reports the site: engines index what they find a `<loc>` for.

    python3 tools/sitemap.py 2026-08-27
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import LOCALES, PAGES, _canonical

ROOT = Path(__file__).resolve().parent.parent

#: Pages that exist only in English, with why. Kept in the sitemap so they are still indexed.
#: Empty again: Harmony Palette's two pages moved into `PAGES` once their copy was signed off and
#: translated, so they carry eleven entries each like everything else.
ENGLISH_ONLY = {}

WEIGHT = {"": ("weekly", "1.0"), "frmt/": ("monthly", "0.9"), "modul8/": ("monthly", "0.9"),
          "cyano/": ("monthly", "0.9"), "harmony/": ("monthly", "0.9"),
          "dollop/": ("monthly", "0.9")}


def main(lastmod):
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    count = 0
    for page_url in list(PAGES.values()):
        freq, priority = WEIGHT.get(page_url, ("yearly", "0.2"))
        alternates = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{h}" href="{_canonical(loc, page_url)}"/>'
            for loc, (_, h, _, _) in LOCALES.items())
        alternates += ('\n    <xhtml:link rel="alternate" hreflang="x-default" '
                       f'href="{_canonical("en", page_url)}"/>')
        for locale in LOCALES:
            out.append(f'  <url>\n    <loc>{_canonical(locale, page_url)}</loc>{alternates}'
                       f'\n    <lastmod>{lastmod}</lastmod>'
                       f'\n    <changefreq>{freq}</changefreq>'
                       f'\n    <priority>{priority}</priority>\n  </url>')
            count += 1
    for page_url, why in ENGLISH_ONLY.items():
        out.append(f'  <!-- English only: {why} -->\n  <url>'
                   f'\n    <loc>{_canonical("en", page_url)}</loc>'
                   f'\n    <lastmod>{lastmod}</lastmod>'
                   f'\n    <changefreq>yearly</changefreq>\n    <priority>0.2</priority>\n  </url>')
        count += 1
    out.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(out) + "\n")
    print(f"sitemap.xml: {count} urls, {len(LOCALES)} languages")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "2026-08-27")
