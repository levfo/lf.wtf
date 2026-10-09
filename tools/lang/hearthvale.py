"""lf.wtf/hearthvale, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The translations live one locale per file, `hearthvale_<locale>.json`, each mapping every English
segment of content/hearthvale.json to its translation, written in parallel like Hive's. This module
folds them into the `T` that merge.py expects.

Hearthvale is a free browser game and an AI experiment, so the copy is warm but plain. Kept in English
everywhere: Hearthvale, the model and tool names (Claude, Claude Haiku 5.5, ultracode, three.js), the
two prompts quoted verbatim, the keycaps, and "New kingdom", because that is the label on the game's
own button and the game is English only. The price says US dollars in every language, because "$"
alone reads as pesos in Mexico.
"""
import json
from pathlib import Path

LOCALES = ["de", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pt-BR", "zh-Hans"]
HERE = Path(__file__).resolve().parent

_parts = {loc: json.loads((HERE / f"hearthvale_{loc}.json").read_text(encoding="utf-8")) for loc in LOCALES}
_english = json.loads((HERE.parent.parent / "content" / "hearthvale.json").read_text(encoding="utf-8"))

KEEP = {"Discord", "X", "Instagram"}  # names, the same in every language
T = {en: tuple(_parts[loc][en] for loc in LOCALES) for en in _english if en not in KEEP}
