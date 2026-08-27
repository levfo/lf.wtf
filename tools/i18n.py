"""Translate lf.wtf's hand-written pages without regenerating them.

The pages are hand-tuned HTML with inline CSS and a little JavaScript. They are **transformed**,
not rebuilt: the markup, the styles, the scripts and the asset paths stay byte for byte as they
are, and only text nodes, a named set of attributes, and named fields inside the JSON-LD are
replaced. That keeps the English pages as the single source of design truth, so a change to the
layout reaches all eleven languages by rerunning this.

Replacement is a **forward scan**, not a global string substitution. Segments are collected in
document order and each is matched at or after the previous one's end, skipping any match that
falls inside a `<script>` or `<style>` block. Global substitution would be a disaster on these
pages: short strings like "Film", "FRMT" and "iPhone" appear in class names, CSS selectors,
JavaScript and URLs as well as in the copy.

    python3 tools/i18n.py extract      # write content/<page>.json, the English segments
    python3 tools/i18n.py build        # write every localised page
    python3 tools/i18n.py check        # verify coverage and reciprocity, write nothing
"""
from __future__ import annotations

import html as htmllib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

#: Locale code -> (url path segment, hreflang value, og:locale, native name for the switcher)
LOCALES = {
    "en":      ("",         "en",     "en_US", "English"),
    "de":      ("de",       "de",     "de_DE", "Deutsch"),
    "es":      ("es",       "es",     "es_ES", "Español"),
    "es-MX":   ("es-mx",    "es-MX",  "es_MX", "Español (MX)"),
    "fr":      ("fr",       "fr",     "fr_FR", "Français"),
    "it":      ("it",       "it",     "it_IT", "Italiano"),
    "ja":      ("ja",       "ja",     "ja_JP", "日本語"),
    "ko":      ("ko",       "ko",     "ko_KR", "한국어"),
    "nl":      ("nl",       "nl",     "nl_NL", "Nederlands"),
    "pt-BR":   ("pt-br",    "pt-BR",  "pt_BR", "Português (BR)"),
    "zh-Hans": ("zh-hans",  "zh-Hans", "zh_CN", "简体中文"),
}
TRANSLATED = [k for k in LOCALES if k != "en"]

#: The pages that get translated, as source path -> url path under the locale prefix.
PAGES = {
    "index.html": "",
    "frmt/index.html": "frmt/",
    "cyano/index.html": "cyano/",
    "modul8/index.html": "modul8/",
    "frmt/privacy/index.html": "frmt/privacy/",
    "cyano/privacy/index.html": "cyano/privacy/",
    #: Back in the set. It was held out while it still described Google AdMob as current, which
    #: 1.3 removes. It now states both positions with the version boundary explicit, because 1.2 is
    #: what the App Store is serving until 1.3 clears review.
    "modul8/privacy/index.html": "modul8/privacy/",
}

ATTRS = {"content", "alt", "title", "aria-label", "placeholder"}
#: Values that are machine-read or are URLs, and must survive untouched.
SKIP_META = {"og:image", "og:url", "og:type", "og:site_name", "twitter:card", "twitter:creator",
             "viewport", "color-scheme", "author", "og:locale", "og:locale:alternate",
             "theme-color", "charset"}
SKIP_TAGS = {"script", "style"}
#: JSON-LD keys worth translating. Everything else in the graph is an identifier, a URL or a number.
LD_KEYS = {"name", "description", "alternateName", "featureList", "headline", "abstract",
           "articleBody", "text", "caption", "disambiguatingDescription"}


# ---------------------------------------------------------------- extraction

class _Walk(HTMLParser):
    """Collect translatable strings, and nothing else.

    Two exclusions earn their keep. Anything under `role="img"` or `aria-hidden="true"` is a
    picture made of characters, not language: the home page draws an ASCII portrait out of 184
    `<b>` elements holding runs of `.`, `:`, `#` and `@`. Translating those would have destroyed
    the artwork in ten languages at once. Its `aria-label` is the part that carries meaning, and
    that is captured as an attribute. A text node with no letters in it is skipped for the same
    reason, as a second line of defence.
    """

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.segments = []          # (kind, value)
        self.stack = []
        self.art = 0                # depth inside a decorative subtree

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        key = d.get("property") or d.get("name") or ""
        decorative = d.get("role") == "img" or d.get("aria-hidden") == "true"
        for name, value in attrs:
            if name not in ATTRS or not value or not value.strip():
                continue
            if key in SKIP_META or value.startswith(("http://", "https://", "/", "#")):
                continue
            if re.fullmatch(r"[\d.\s/:,-]+", value):
                continue
            self.segments.append((f"attr:{name}", value))
        self.stack.append(tag)
        if decorative:
            self.art += 1
        self._art_at = getattr(self, "_art_at", [])
        if decorative:
            self._art_at.append(len(self.stack))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if getattr(self, "_art_at", []) and self._art_at[-1] == len(self.stack):
            self._art_at.pop()
            self.art -= 1
        self.stack.pop()

    def handle_endtag(self, tag):
        if tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
            while getattr(self, "_art_at", []) and self._art_at[-1] > len(self.stack):
                self._art_at.pop()
                self.art -= 1

    def handle_data(self, data):
        if self.art or (self.stack and self.stack[-1] in SKIP_TAGS):
            return
        if data.strip() and re.search(r"[^\W\d_]", data):
            self.segments.append((f"text:{self.stack[-1] if self.stack else ''}", data))


def _ld_strings(node, out):
    """Walk a JSON-LD graph and collect the values worth translating, in a stable order."""
    if isinstance(node, dict):
        for k in sorted(node):
            v = node[k]
            if k in LD_KEYS and isinstance(v, str) and not v.startswith("http"):
                out.append(v)
            elif k in LD_KEYS and isinstance(v, list):
                out += [x for x in v if isinstance(x, str)]
            else:
                _ld_strings(v, out)
    elif isinstance(node, list):
        for v in node:
            _ld_strings(v, out)
    return out


def _ld_blocks(source):
    return list(re.finditer(
        r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)', source, re.S))


def strip_injected(source):
    """Remove everything a previous run of this script added.

    The English pages are both the input and the output, so without this the language switcher
    starts being extracted as if it were copy: "English", "Deutsch", "Language" and ten og:locale
    codes all turned up as translatable segments on the second pass.
    """
    source = re.sub(r"\n?/\* i18n:start \*/.*?/\* i18n:end \*/\n?", "", source, flags=re.S)
    source = re.sub(r'\n?<nav class="i18n".*?</nav>\n?', "", source, flags=re.S)
    source = re.sub(r'\n?<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", source)
    source = re.sub(r'\n?<meta property="og:locale:alternate" content="[^"]*">', "", source)
    return source


def extract(source):
    """Every translatable string in the page, in document order, deduplicated."""
    source = strip_injected(source)
    walk = _Walk()
    walk.feed(source)
    seen, out = set(), []
    for kind, value in walk.segments:
        v = value.strip()
        if not v or v in seen:
            continue
        seen.add(v)
        out.append({"kind": kind, "en": v})
    for m in _ld_blocks(source):
        for v in _ld_strings(json.loads(m.group(2)), []):
            if v not in seen:
                seen.add(v)
                out.append({"kind": "ld", "en": v})
    return out


# ---------------------------------------------------------------- rebuilding

def _protected_spans(source):
    spans = [(m.start(), m.end()) for m in
             re.finditer(r"<script\b.*?</script>|<style\b.*?</style>", source, re.S)]
    # JSON-LD is handled separately and on purpose, so it is not protected from that pass.
    return spans


def _inside(spans, i):
    return any(a <= i < b for a, b in spans)


def _apply_text(source, pairs):
    """Replace each English string with its translation, scanning forward and never backtracking."""
    spans = _protected_spans(source)
    out, cursor, misses = [], 0, []
    for english, translated in pairs:
        i = source.find(english, cursor)
        while i != -1 and _inside(spans, i):
            i = source.find(english, i + 1)
        if i == -1:
            misses.append(english)
            continue
        out.append(source[cursor:i])
        out.append(translated)
        cursor = i + len(english)
    out.append(source[cursor:])
    return "".join(out), misses


#: Nodes that describe something a reader consumes, and so have a language.
LD_LANGUAGE_TYPES = {"WebPage", "WebSite", "MobileApplication", "SoftwareApplication",
                     "CollectionPage", "AboutPage", "Article", "FAQPage"}


def _apply_ld(source, table, hreflang):
    """Translate the graph and stamp `inLanguage`, so an answer engine knows what it is quoting.

    Set on the node rather than by patching the serialised text. A regex over `"@type": "WebPage",`
    silently did nothing, because whether that key is followed by a comma depends on where it lands
    in the object.
    """
    def swap(node):
        if isinstance(node, dict):
            out = {k: ([table.get(x, x) if isinstance(x, str) else swap(x) for x in v]
                       if k in LD_KEYS and isinstance(v, list)
                       else table.get(v, v) if k in LD_KEYS and isinstance(v, str)
                       else swap(v))
                   for k, v in node.items()}
            t = out.get("@type")
            types = t if isinstance(t, list) else [t]
            if any(x in LD_LANGUAGE_TYPES for x in types):
                out["inLanguage"] = hreflang
            return out
        if isinstance(node, list):
            return [swap(v) for v in node]
        return node

    def repl(m):
        data = swap(json.loads(m.group(2)))
        return m.group(1) + "\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n" + m.group(3)

    return re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',
                  repl, source, flags=re.S)


def _canonical(locale, page_url):
    prefix = LOCALES[locale][0]
    return "https://lf.wtf/" + (f"{prefix}/" if prefix else "") + page_url


def _alternates(page_url):
    """Reciprocal hreflang for every language, plus x-default pointing at English.

    Every page in the set must list every other, itself included. A one-way annotation is ignored,
    which is the usual way a multilingual site ends up with none of it working.
    """
    lines = []
    for loc, (_, hreflang, _, _) in LOCALES.items():
        lines.append(f'<link rel="alternate" hreflang="{hreflang}" '
                     f'href="{_canonical(loc, page_url)}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" '
                 f'href="{_canonical("en", page_url)}">')
    return "\n".join(lines)


def _switcher(locale, page_url):
    """A visible list of the other languages. Crawlers follow links; they do not guess."""
    items = []
    for loc, (_, _, _, native) in LOCALES.items():
        href = _canonical(loc, page_url).replace("https://lf.wtf", "") or "/"
        if loc == locale:
            items.append(f'<span aria-current="true" lang="{LOCALES[loc][1]}">{native}</span>')
        else:
            items.append(f'<a href="{href}" hreflang="{LOCALES[loc][1]}" '
                         f'lang="{LOCALES[loc][1]}">{native}</a>')
    return ('\n<nav class="i18n" aria-label="Language">\n  ' + "\n  ".join(items) + "\n</nav>\n")


#: Letterspacing is a Latin display convention. The site tracks out its small labels, which looks
#: deliberate in Latin and looks broken in kana, hangul and hanzi: it pulls the characters of a word
#: apart. This was not visible in the markup and only turned up on looking at the rendered Japanese
#: page, where the subtitle read as separated characters rather than as a phrase.
#:
#: `!important` because the rule has to beat whatever specificity the hand-written CSS uses, and it
#: is scoped to the three scripts that need it so no Latin locale is affected.
CJK_CSS = """
html[lang="ja"] *, html[lang="ko"] *, html[lang="zh-Hans"] * { letter-spacing: normal !important; }
"""

SWITCHER_CSS = """
/* i18n:start */
.i18n{max-width:var(--w,initial);margin:0 auto;padding:26px 22px 40px;display:flex;flex-wrap:wrap;
gap:6px 14px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;opacity:.55;
justify-content:center}
.i18n a{color:inherit;text-decoration:none;border-bottom:1px solid transparent}
.i18n a:hover{border-bottom-color:currentColor}
.i18n span[aria-current]{opacity:.5;cursor:default}
/* i18n:end */
"""


class Face:
    """Just enough of the app-side Face to answer 'is this locale Latin'."""

    def __init__(self, locale):
        self.latin = locale not in {"ja", "ko", "zh-Hans"}


def build_page(source, locale, page_url, table):
    """One localised page: translated copy, correct language metadata, reciprocal alternates."""
    _, hreflang, og_locale, _ = LOCALES[locale]
    pairs = [(e, t) for e, t in table if e != t]
    out, misses = _apply_text(source, pairs)
    out = _apply_ld(out, dict(table), hreflang)

    out = re.sub(r'<html lang="[^"]*"', f'<html lang="{hreflang}"', out, count=1)
    out = re.sub(r'<link rel="canonical" href="[^"]*">',
                 f'<link rel="canonical" href="{_canonical(locale, page_url)}">', out, count=1)
    out = re.sub(r'<meta property="og:url" content="[^"]*">',
                 f'<meta property="og:url" content="{_canonical(locale, page_url)}">', out, count=1)
    out = re.sub(r'<meta property="og:locale" content="[^"]*">',
                 f'<meta property="og:locale" content="{og_locale}">', out, count=1)

    # Alternates go immediately before the canonical, and any previous set is stripped first so a
    # rebuild is idempotent. The privacy pages have no canonical at all, which silently gave them
    # no alternates either: the anchor simply was not there. They get one written for them.
    out = re.sub(r'\n?<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", out)
    block = _alternates(page_url)
    if '<link rel="canonical"' in out:
        out = out.replace('<link rel="canonical"', block + '\n<link rel="canonical"', 1)
    else:
        canonical = f'<link rel="canonical" href="{_canonical(locale, page_url)}">'
        out = re.sub(r"(</title>)", r"\1\n" + block.replace("\\", "\\\\") + "\n" + canonical,
                     out, count=1)
    # Same idempotence problem as the switcher: without stripping, every rebuild adds another ten
    # og:locale:alternate tags to the English page, which is then the source for the next rebuild.
    out = re.sub(r'\n?<meta property="og:locale:alternate" content="[^"]*">', "", out)
    others = "".join(f'\n<meta property="og:locale:alternate" content="{LOCALES[l][2]}">'
                     for l in LOCALES if l != locale)
    out = re.sub(r'(<meta property="og:locale" content="[^"]*">)', r"\1" + others, out, count=1)

    # Strip whatever a previous run of this script left behind, then add exactly one of each.
    out = re.sub(r"\n?/\* i18n:start \*/.*?/\* i18n:end \*/\n?", "", out, flags=re.S)
    out = re.sub(r'\n?<nav class="i18n".*?</nav>\n?', "", out, flags=re.S)
    css = SWITCHER_CSS + (CJK_CSS if not Face(locale).latin else "")
    out = out.replace("</style>", css + "</style>", 1)
    out = out.replace("</body>", _switcher(locale, page_url) + "</body>", 1)
    return out, misses


# ---------------------------------------------------------------- commands

def cmd_extract():
    CONTENT.mkdir(exist_ok=True)
    for src in PAGES:
        segs = extract((ROOT / src).read_text())
        name = src.replace("/index.html", "").replace("index.html", "home").replace("/", "-")
        path = CONTENT / f"{name}.json"
        existing = json.loads(path.read_text()) if path.exists() else {}
        merged = {s["en"]: {"kind": s["kind"], **existing.get(s["en"], {})} for s in segs}
        path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n")
        words = sum(len(s["en"].split()) for s in segs)
        print(f"{name:16} {len(segs):3} segments  ~{words:4} words")


def _table(name, locale):
    data = json.loads((CONTENT / f"{name}.json").read_text())
    missing = [en for en, v in data.items() if locale not in v]
    #: Strings that live only inside the JSON-LD are replaced by `_apply_ld`, never by the text
    #: scan, because the scan deliberately refuses to touch anything inside a <script>. Without
    #: this they are reported as "not found in source" on every page and every locale, which is
    #: forty lines of noise hiding any real miss.
    ld_only = {en for en, v in data.items() if v.get("kind") == "ld"}
    return [(en, v.get(locale, en)) for en, v in data.items()], missing, ld_only


def cmd_build(check_only=False):
    problems, written = [], 0
    for src, page_url in PAGES.items():
        name = src.replace("/index.html", "").replace("index.html", "home").replace("/", "-")
        source = strip_injected((ROOT / src).read_text())

        # The English page is rewritten in place with the same reciprocal alternates and the same
        # switcher. hreflang has to point both ways: a set where only the translations declare
        # their siblings is ignored wholesale, which is the usual way this ends up doing nothing.
        english, _ = build_page(source, "en", page_url, [(s, s) for s in
                                                         json.loads((CONTENT / f"{name}.json")
                                                                    .read_text())])
        if not check_only:
            (ROOT / src).write_text(english)
            written += 1

        for locale in TRANSLATED:
            table, missing, ld_only = _table(name, locale)
            if missing:
                problems.append(f"{name} [{locale}]: {len(missing)} untranslated")
                continue
            out, misses = build_page(source, locale, page_url, table)
            misses = [m for m in misses if m not in ld_only]
            if misses:
                problems.append(f"{name} [{locale}]: {len(misses)} segments not found in source: "
                                + "; ".join(repr(m[:40]) for m in misses[:3]))
            if not check_only:
                dest = ROOT / LOCALES[locale][0] / page_url / "index.html"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(out)
                written += 1
    for p in problems:
        print(p)
    print(f"\n{written} pages written, {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    sys.exit(cmd_extract() if cmd == "extract" else cmd_build(cmd == "check"))
