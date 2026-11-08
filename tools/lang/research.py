"""AI Research translations (research). English stays the source of layout and copy.
One JSON per locale (research_<locale>.json) so translators can work in parallel without clobbering each other."""
import json
from pathlib import Path
HERE=Path(__file__).parent
LOCALES=['de','es','es-MX','fr','it','ja','ko','nl','pt-BR','zh-Hans']
EN=list(json.loads((HERE.parent.parent/'content/research.json').read_text(encoding='utf-8')))
parts={loc:json.loads((HERE/f'research_{loc}.json').read_text(encoding='utf-8')) for loc in LOCALES}
KEEP={'lf.wtf','Levi Foster','© Levi Foster','SmolLM2-135M'}
T={en:tuple(parts[loc][en] for loc in LOCALES) for en in EN if en not in KEEP}
