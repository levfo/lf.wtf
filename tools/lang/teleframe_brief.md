# Teleframe translation brief

Files to translate (keys are the English segments, in document order):
- content/teleframe.json         -> landing page https://lf.wtf/teleframe/ (SEO page)
- content/teleframe-thanks.json  -> download page after payment (noindex)

Write, per locale, two JSON objects mapping EVERY English key to its translation:
- tools/lang/teleframe_<locale>.json
- tools/lang/teleframe-thanks_<locale>.json
Locale codes: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans. UTF-8, ensure_ascii false, indent 2.

Keep unchanged (copy the English): Teleframe, lf.wtf, Levi Foster, Discord, REC, teleframe@lf.wtf,
画面録画機 2026年製, keyboard shortcuts (Ctrl+Alt+R ...), "Videos\Teleframe", file names, numbers, "H.264", "MP4",
"AAC", "kbps", "fps", ratio names (16:9, 9:16 ...), and the app's UI words LOW, MAX, HIGH, More info / Run anyway
(SmartScreen button labels: use the label Windows shows in that language, e.g. de "Weitere Informationen" /
"Trotzdem ausführen", fr "Informations complémentaires" / "Exécuter quand même", ja "詳細情報" / "実行",
ko "추가 정보" / "실행", zh "更多信息" / "仍要运行", es "Más información" / "Ejecutar de todas formas",
it "Ulteriori informazioni" / "Esegui comunque", nl "Meer informatie" / "Toch uitvoeren",
pt-BR "Mais informações" / "Executar assim mesmo"). The app interface itself is English (the page says so).

Facts must stay identical: no added claims, no superlatives, no "best", no "free". Prices stay "$9.99" where
written (the page script swaps in the local price).

## SEO (the landing page must rank for people looking for a screen recorder in each language)
Use the phrase people actually search in that market, naturally, in the <title>, meta description, og
title/description, the eyebrow "Screen recorder for Windows", the H1 and at least one H2 and FAQ. Suggested:
- de: "Bildschirmrekorder für Windows", "Bildschirm aufnehmen"
- nl: "schermrecorder voor Windows", "scherm opnemen"
- es: "grabador de pantalla para Windows", "grabar la pantalla"
- es-MX: "grabador de pantalla para Windows", "grabar pantalla en PC" (Mexican Spanish: tú, "computadora")
- fr: "enregistreur d'écran pour Windows", "enregistrer l'écran"
- it: "registratore dello schermo per Windows", "registrare lo schermo"
- ja: "画面録画ソフト（Windows）", "PCの画面録画"
- ko: "윈도우 화면 녹화 프로그램", "PC 화면 녹화"
- pt-BR: "gravador de tela para Windows", "gravar a tela do PC"
- zh-Hans: "Windows 录屏软件", "电脑录屏"
Title stays under ~60 characters of visible width where possible (CJK: ~30 chars), brand "Teleframe |" first.
Meta description ~150 chars (CJK ~80). The H1 is shown uppercase in Latin scripts; keep it short.

## Voice
Plain, warm, direct, like a person who made the app. Native phrasing, not literal. Use the informal
"you" the market expects for consumer software (de du, fr vous, es/es-MX tú, it tu, nl je, pt-BR você).
Avoid AI tells: no "not X but Y" contrasts, no dash-joined clauses (no em/en dashes), no triplet slogans,
no hype words. Keep sentence count similar to the English.

## Fragments split by inline elements
Some sentences are split around a link, <kbd> or a price, and each piece is a separate key. The pieces are
re-joined IN THE SAME ORDER with the element in between, so translate each piece so the joined sentence reads
correctly in your language. Keys are trimmed; the page keeps one space on each side of the element (CJK pages too, so do not add spaces of your own). The splits:
- "Price:" [price] "once. No subscription."
- [Ctrl+Alt+R] " record," [Ctrl+Alt+P] " pause," [Ctrl+Alt+D] " delete the last clip," [Ctrl+Alt+S] " save,"
  [Ctrl+Alt+H] " hide the controls. You can change them."  (shortcut first, then its action)
- "Open the" [link: "download page"] "and enter the email you paid with. ..."  (FAQ answer on the page;
  the JSON-LD has the same answer as one full sentence, translate that one fully)
- "Made by" [link: Levi Foster]
- thanks page: "A copy of the link is on its way to" [email address] ". Keep that email, ..."
- thanks page: "Haven't bought Teleframe yet?" [link: "See Teleframe"] "."
If word order needs the element elsewhere, rephrase each piece so it still works in this order.

## Check before finishing
python -c "import json,sys; e=json.load(open('content/teleframe.json',encoding='utf-8')); t=json.load(open('tools/lang/teleframe_LOC.json',encoding='utf-8')); m=[k for k in e if k not in t]; print(len(m),'missing')"
(and the same for teleframe-thanks). Both must print 0 missing. Do not edit any other file.
