"""lf.wtf/dollop, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Assembled from two parts that follow the page top to bottom: A head, hero, the argument and the
five modes; B the creature, the feel of it, privacy, the FAQ and the copy the live demonstration
speaks while you play.

This page sells a game, and the temptation in translation is to sell harder. It should not. The
English is quiet and declarative, and every language here stays that way: no exclamation marks, no
"amazing", nothing that would sound like a store listing rather than like the app.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import dollop_a
import dollop_b

#: Identical in every language: the wordmark, the app names, the developer, the domain and the
#: contact address. "Dollop" is a name, not the noun, so it never becomes "Klecks" in German.
KEEP = {
    "dollop", "Dollop", "Dollop: Color Mixing Game",
    "Harmony Palette", "FRMT", "CYANO", "MODUL8",
    "lf.wtf", "L@LF.WTF", "Levi Foster", "iPhone", "App Store",
    "English", "Deutsch", "Español", "Español (MX)", "Français", "Italiano",
    "日本語", "한국어", "Nederlands", "Português (BR)", "简体中文",
}

T = {}
for part in (dollop_a, dollop_b):
    overlap = set(T) & set(part.T)
    assert not overlap, f"duplicated between parts: {sorted(overlap)[:3]}"
    T.update(part.T)
