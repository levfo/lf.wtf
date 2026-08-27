"""lf.wtf/harmony, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The page is long enough that keeping it in one file made it unreadable, so the table is assembled
from four parts that follow the page top to bottom: A head and hero, B the two wheels and the eight
harmonies, C the curated library and export, D languages, FAQ and footer.

This page argues rather than sells, and it argues about colour specifically. It shares no framing
with FRMT, CYANO or MODUL8 and should not acquire any in translation: nothing here simulates a
physical process, and no sentence should start sounding like it does.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import harmony_a
import harmony_b
import harmony_c
import harmony_d

#: Identical in every language: the wordmark, the app names, and the language switcher, which lists
#: each language in its own words and would be nonsense translated. "Pro" is the tier's name rather
#: than the adjective, so it travels untranslated the way the App Store shows it.
KEEP = {
    "harmony", "palette", "Harmony Palette", "Pro",
    "FRMT", "CYANO", "MODUL8", "lf.wtf", "Levi Foster", "iPhone", "iPad", "App Store",
    "English", "Deutsch", "Español", "Español (LatAm)", "Français", "Italiano",
    "日本語", "한국어", "Nederlands", "Português (BR)", "简体中文",
}

T = {}
for part in (harmony_a, harmony_b, harmony_c, harmony_d):
    overlap = set(T) & set(part.T)
    assert not overlap, f"duplicated between parts: {sorted(overlap)[:3]}"
    T.update(part.T)
