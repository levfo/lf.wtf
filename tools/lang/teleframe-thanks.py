"""Teleframe translations (teleframe-thanks). English stays the source of layout and copy; one JSON per locale."""
import json
from pathlib import Path
HERE = Path(__file__).parent
LOCALES = ['de', 'es', 'es-MX', 'fr', 'it', 'ja', 'ko', 'nl', 'pt-BR', 'zh-Hans']
EN = list(json.loads((HERE.parent.parent / 'content/teleframe-thanks.json').read_text(encoding='utf-8')))
parts = {loc: json.loads((HERE / f'teleframe-thanks_{loc}.json').read_text(encoding='utf-8')) for loc in LOCALES
         if (HERE / f'teleframe-thanks_{loc}.json').exists()}
KEEP = {'Teleframe', 'lf.wtf', 'Levi Foster', 'Discord', 'REC', 'teleframe@lf.wtf', '画面録画機 2026年製'}
T = {en: tuple(parts[loc][en] for loc in LOCALES) for en in EN
     if en not in KEEP and all(loc in parts and en in parts[loc] for loc in LOCALES)}
