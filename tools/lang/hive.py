"""lf.wtf/hive, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The translations live one locale per file, `hive_<locale>.json`, each mapping every English segment of
content/hive.json to its translation. They were written in parallel, one pair of languages at a time,
so one file per locale kept them from overwriting each other. This module folds them into the `T` that
merge.py expects.

Hive is a paid tool for people who run several AI agents, so the copy is plain and specific rather
than playful. Address: du, tú, vous, tu, je, você, です/ます, 해요체 and 你. French takes vous here,
unlike Carmeet, because this page sells a subscription. The word Hive is the product name and is never
translated, including where the English says "your hive" for a person's own workspace (dein Hive, tu
Hive, votre Hive). A seat is a Platz, plaza (Spain), puesto (Mexico), place, posto, 席, 자리, plek,
vaga and 席位, one word per language throughout.

Kept in English everywhere: product and client names (Claude Code, Codex, Cursor, Grok Bot, Sesame,
Zapier, Stripe, Cloudflare), every hub_ tool name, the code blocks, the seat handles in the message
log (reviewer → builder), the note keys goal, deploy and style, and the protocol names MCP,
Streamable HTTP, OAuth 2.1, PKCE and PBKDF2. Prices say US dollars in every language, because "$"
alone reads as pesos in Mexico and as nothing in particular in Japan.
"""
import json
from pathlib import Path

LOCALES = ["de", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pt-BR", "zh-Hans"]
HERE = Path(__file__).resolve().parent

_parts = {loc: json.loads((HERE / f"hive_{loc}.json").read_text(encoding="utf-8")) for loc in LOCALES}
_english = json.loads((HERE.parent.parent / "content" / "hive.json").read_text(encoding="utf-8"))

KEEP = set()
T = {en: tuple(_parts[loc][en] for loc in LOCALES) for en in _english}
