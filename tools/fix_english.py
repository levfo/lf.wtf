"""Two corrections to the English pages, applied before anything is translated from them.

**Em-dashes.** House style forbids them in published copy. Every one here separates a name from a
descriptor, so a colon carries the same job. Not an en-dash and not a spaced hyphen, which keep the
same rhythm and defeat the point. The three privacy titles are rewritten rather than repunctuated,
because "Privacy: FRMT" reads worse than "FRMT Privacy Policy" and the latter also puts the brand
first, which is the better title.

**FAQ structured data.** Google requires FAQPage markup to match content a visitor can actually see,
and four of FRMT's five answers were reworded against the visible copy while a fifth question was
missing from the schema entirely. Rather than hand-correcting them, the schema is rebuilt *from* the
page: the visible questions and answers become the mainEntity, so the two cannot drift again. Run
this after editing the visible FAQ and the schema follows.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DASHES = {
    "index.html": [
        ("Levi Foster — iPhone Apps", "Levi Foster: iPhone Apps"),
        (">FRMT — Film Simulation<", ">FRMT: Film Simulation<"),
        (">MODUL8 — Glitch Art Effects<", ">MODUL8: Glitch Art Effects<"),
        (">CYANO &mdash; Cyanotype Photos<", ">CYANO: Cyanotype Photos<"),
    ],
    "frmt/index.html": [("FRMT — Film Simulation App for iPhone",
                         "FRMT: Film Simulation App for iPhone")],
    "cyano/index.html": [(">FRMT &mdash; Film Simulation<", ">FRMT: Film Simulation<"),
                         (">MODUL8 &mdash; Glitch Art Effects<", ">MODUL8: Glitch Art Effects<")],
    "modul8/index.html": [
        ("MODUL8 — Glitch Art App for iPhone | Free Glitch Photo Effects",
         "MODUL8: Glitch Art App for iPhone | Free Glitch Photo Effects"),
        ("MODUL8 — Glitch Art App for iPhone", "MODUL8: Glitch Art App for iPhone"),
    ],
    "frmt/privacy/index.html": [("<title>Privacy &mdash; FRMT</title>",
                                 "<title>FRMT Privacy Policy</title>")],
    "cyano/privacy/index.html": [("<title>Privacy &mdash; CYANO</title>",
                                  "<title>CYANO Privacy Policy</title>")],
    "modul8/privacy/index.html": [
        ("Privacy Policy — MODUL8", "MODUL8 Privacy Policy"),
        ("<strong>Device identifiers</strong> —", "<strong>Device identifiers</strong>:"),
        ("<strong>Usage data</strong> —", "<strong>Usage data</strong>:"),
    ],
}

#: A heading that is a question, followed by its paragraph. Covers all three pages: FRMT uses h4,
#: CYANO and MODUL8 use h3.
PAIR = re.compile(r"<h[34][^>]*>([^<]*\?)</h[34]>\s*<p[^>]*>(.*?)</p>", re.S)


def _text(html):
    """Visible text, with the markup dropped, entities resolved and whitespace collapsed.

    The schema carries one line; the page carries the same words wrapped across four. Collapsing is
    what makes them the same answer.
    """
    t = re.sub(r"<[^>]+>", "", html)
    for entity, char in (("&mdash;", ": "), ("&amp;", "&"), ("&nbsp;", " "), ("&#39;", "'"),
                         ("&quot;", '"'), ("&lt;", "<"), ("&gt;", ">")):
        t = t.replace(entity, char)
    return re.sub(r"\s+", " ", t).strip()


def main():
    for rel, swaps in DASHES.items():
        p = ROOT / rel
        s = p.read_text()
        for old, new in swaps:
            if old not in s:
                print(f"  MISS {rel}: {old[:48]!r}")
                continue
            s = s.replace(old, new)
        p.write_text(s)
        left = len(re.findall("—|&mdash;", s))
        print(f"{rel:28} em-dashes remaining: {left}")

    for rel in ["frmt/index.html", "cyano/index.html", "modul8/index.html"]:
        p = ROOT / rel
        s = p.read_text()
        pairs = [(_text(q), _text(a)) for q, a in PAIR.findall(s.split("<body", 1)[1])]

        def rewrite(m):
            data = json.loads(m.group(2))
            for node in data.get("@graph", []):
                if node.get("@type") != "FAQPage":
                    continue
                node["mainEntity"] = [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]
            return (m.group(1) + "\n" + json.dumps(data, ensure_ascii=False, indent=2)
                    + "\n" + m.group(3))

        s = re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',
                   rewrite, s, flags=re.S)
        p.write_text(s)
        print(f"{rel:28} FAQ schema rebuilt from {len(pairs)} visible question(s)")


if __name__ == "__main__":
    main()
