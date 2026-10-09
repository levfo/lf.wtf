"""lf.wtf/system-memory, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The translations live one locale per file, `system-memory_<locale>.json`, each mapping every English
segment of content/system-memory.json to its translation, written in parallel like Hearthvale's. This
module folds them into the `T` that merge.py expects.

System Memory is a short film, so the copy is quiet and plain, and the producer's note stays in
Claude's first person. Kept in English everywhere: the film title, the model and tool names (Claude,
Claude Code, Krea, MCP, Nano Banana 2.1, MiniMax H3 Max Turbo, Seed Audio, MiniMax Music 3, ComfyUI,
Python, ffmpeg), the film's own terminal text ("user> what do you remember about home?"), the five
score cue titles, and the code in the two calls, which is quoted exactly as it ran.
"""
import json
from pathlib import Path

LOCALES = ["de", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pt-BR", "zh-Hans"]
HERE = Path(__file__).resolve().parent

_parts = {loc: json.loads((HERE / f"system-memory_{loc}.json").read_text(encoding="utf-8")) for loc in LOCALES}
_english = json.loads((HERE.parent.parent / "content" / "system-memory.json").read_text(encoding="utf-8"))

KEEP = set()
T = {en: tuple(_parts[loc][en] for loc in LOCALES) for en in _english}
