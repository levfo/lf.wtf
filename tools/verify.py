"""Check the published set the way a crawler would, rather than trusting the build.

hreflang only works if it is reciprocal and self-inclusive: every page in a set must list every
other page **and itself**, and the URLs must resolve. A one-way or incomplete annotation is not
partially effective, it is ignored, which is why this is worth checking rather than assuming.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import LOCALES, PAGES, _canonical

ROOT = Path(__file__).resolve().parent.parent
problems = []


def path_for(locale, page_url):
    prefix = LOCALES[locale][0]
    return ROOT / prefix / page_url / "index.html" if prefix else ROOT / page_url / "index.html"


english_titles, english_descs = {}, {}
for page_url in PAGES.values():
    for locale in LOCALES:
        f = path_for(locale, page_url)
        where = f"{locale}:/{LOCALES[locale][0]}/{page_url}"
        if not f.exists():
            problems.append(f"{where}: missing file"); continue
        s = f.read_text()

        lang = re.search(r'<html lang="([^"]*)"', s)
        if not lang or lang.group(1) != LOCALES[locale][1]:
            problems.append(f"{where}: html lang is {lang and lang.group(1)!r}")

        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        if not canon or canon.group(1) != _canonical(locale, page_url):
            problems.append(f"{where}: canonical is {canon and canon.group(1)!r}")

        alts = dict(re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)">', s))
        expected = {h: _canonical(l, page_url) for l, (_, h, _, _) in LOCALES.items()}
        expected["x-default"] = _canonical("en", page_url)
        if alts != expected:
            missing = set(expected) - set(alts)
            problems.append(f"{where}: hreflang set wrong, missing {sorted(missing)}")

        title = re.search(r"<title>(.*?)</title>", s, re.S)
        if not title:
            problems.append(f"{where}: no <title>")
        elif locale == "en":
            english_titles[page_url] = title.group(1)
            d = re.search(r'<meta name="description" content="([^"]*)"', s)
            english_descs[page_url] = d.group(1) if d else None
        elif title.group(1) == english_titles.get(page_url):
            # A short title can legitimately be identical: "Privacy" is the same word in Italian
            # and Dutch. Only flag it when the description matches too, which means nothing on the
            # page was translated.
            desc = re.search(r'<meta name="description" content="([^"]*)"', s)
            if desc and desc.group(1) == english_descs.get(page_url):
                problems.append(f"{where}: title and description are both still English")

        for m in re.finditer(r'(<script[^>]*ld\+json[^>]*>)(.*?)(</script>)', s, re.S):
            try:
                g = json.loads(m.group(2))
            except json.JSONDecodeError as e:
                problems.append(f"{where}: JSON-LD does not parse ({e})"); continue
            if not json.dumps(g).count(f'"inLanguage": "{LOCALES[locale][1]}"'):
                problems.append(f"{where}: JSON-LD has no inLanguage for this locale")

        if '<nav class="i18n"' not in s:
            problems.append(f"{where}: no visible language switcher")

# Every alternate URL must actually resolve to a file on disk.
for page_url in PAGES.values():
    for locale in LOCALES:
        if not path_for(locale, page_url).exists():
            problems.append(f"alternate target missing: {_canonical(locale, page_url)}")

pages = len(PAGES) * len(LOCALES)
print("\n".join(problems) if problems else "")
print(f"{pages} pages checked, {len(problems)} problem(s)")
sys.exit(1 if problems else 0)
