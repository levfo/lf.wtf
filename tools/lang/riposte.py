"""RIPOSTE translations. English remains the source of layout and copy."""
import json
from pathlib import Path
HERE=Path(__file__).parent
LOCALES=['de','es','es-MX','fr','it','ja','ko','nl','pt-BR','zh-Hans']
EN=list(json.loads((HERE.parent.parent/'content/riposte.json').read_text(encoding='utf-8')))
parts={loc:json.loads((HERE/f'riposte_{loc}.json').read_text(encoding='utf-8')) for loc in LOCALES}
KEEP={'RIPOSTE','lf.wtf','Levi Foster','Discord'}
T={en:tuple(parts[loc][en] for loc in LOCALES) for en in EN if en not in KEEP}
