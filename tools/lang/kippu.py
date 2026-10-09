"""lf.wtf/kippu, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Written against the app's own words: the path is Reise / Viaje / Voyage / Viaggio / 旅行 /
여행 / Reizen / Viagem / 旅行 because that is the tab; Know-how is Wissen / Saber hacer /
Savoir-faire / Da sapere / 豆知識 / 알아두기 / Weetjes / Dicas / 旅行须知 because that is the
button. The Japanese page is read by residents and by people choosing for a friend, so it
carries the same promise without pretending the reader is the learner.
"""

KEEP = {"Kippu", "lf.wtf", "L@LF.WTF", "Dollop", "JLPT N5", "Plus", "Kippu Plus", "Levi Foster"}

T = {
    "Kippu: learn Japanese for your trip, then the JLPT N5": (
        "Kippu: Japanisch lernen für die Reise, dann für den JLPT N5",
        "Kippu: aprende japonés para tu viaje, y luego el JLPT N5",
        "Kippu: aprende japonés para tu viaje, y luego el JLPT N5",
        "Kippu : apprendre le japonais pour le voyage, puis le JLPT N5",
        "Kippu: impara il giapponese per il viaggio, poi il JLPT N5",
        "Kippu：旅のための日本語、そして JLPT N5",
        "Kippu: 여행을 위한 일본어, 그다음 JLPT N5",
        "Kippu: Japans leren voor je reis, daarna het JLPT N5",
        "Kippu: aprenda japonês para a viagem, depois o JLPT N5",
        "Kippu：为旅行学日语，然后是 JLPT N5"),

    "Learn Japanese on iPhone for a trip to Japan, then go on to the JLPT N5. Real phrases with what staff say back, hiragana and katakana, kanji with stroke order, and short sittings that bring back what you are about to forget.": (
        "Japanisch auf dem iPhone lernen, für die Reise nach Japan und danach für den JLPT N5. Echte Sätze mit dem, was das Personal antwortet, Hiragana und Katakana, Kanji mit Strichfolge und kurze Lektionen, die zurückholen, was du gerade vergessen würdest.",
        "Aprende japonés en el iPhone para un viaje a Japón y sigue después con el JLPT N5. Frases reales con lo que responde el personal, hiragana y katakana, kanji con orden de trazos y sesiones cortas que recuperan lo que estás a punto de olvidar.",
        "Aprende japonés en el iPhone para un viaje a Japón y sigue después con el JLPT N5. Frases reales con lo que contesta el personal, hiragana y katakana, kanji con orden de trazos y sesiones cortas que recuperan lo que estás a punto de olvidar.",
        "Apprenez le japonais sur iPhone pour un voyage au Japon, puis passez au JLPT N5. De vraies phrases avec ce que le personnel répond, hiragana et katakana, kanji avec l'ordre des traits, et des séances courtes qui ramènent ce que vous êtes sur le point d'oublier.",
        "Impara il giapponese su iPhone per un viaggio in Giappone, poi passa al JLPT N5. Frasi vere con quello che risponde il personale, hiragana e katakana, kanji con l'ordine dei tratti e sessioni brevi che riportano quello che stai per dimenticare.",
        "iPhone で、日本を旅するための日本語を学び、そのまま JLPT N5 へ。店員さんの返答つきの実際のフレーズ、ひらがなとカタカナ、筆順つきの漢字、そして忘れかけたものを先に戻してくれる短い学習。",
        "iPhone에서 일본 여행을 위한 일본어를 배우고, 이어서 JLPT N5까지. 직원의 답변이 함께 나오는 실제 표현, 히라가나와 가타카나, 필순이 있는 한자, 그리고 잊기 직전인 것을 먼저 되돌려 주는 짧은 학습.",
        "Leer Japans op de iPhone voor een reis naar Japan, en ga daarna door naar het JLPT N5. Echte zinnen met wat het personeel terugzegt, hiragana en katakana, kanji met streepvolgorde, en korte sessies die terughalen wat je bijna vergeten bent.",
        "Aprenda japonês no iPhone para uma viagem ao Japão e siga depois para o JLPT N5. Frases reais com o que o atendente responde, hiragana e katakana, kanji com ordem dos traços e sessões curtas que trazem de volta o que você está prestes a esquecer.",
        "在 iPhone 上学去日本旅行要用的日语，然后继续冲 JLPT N5。附有店员回答的真实句子、平假名和片假名、带笔顺的汉字，以及会把你快忘的内容先带回来的短时学习。"),

    "Japanese for iPhone. Real phrases with what staff say back, both kana, kanji with stroke order, and short sittings that bring back what you are about to forget.": (
        "Japanisch fürs iPhone. Echte Sätze mit dem, was das Personal antwortet, beide Kana, Kanji mit Strichfolge und kurze Lektionen, die zurückholen, was du gerade vergessen würdest.",
        "Japonés para iPhone. Frases reales con lo que responde el personal, los dos silabarios, kanji con orden de trazos y sesiones cortas que recuperan lo que estás a punto de olvidar.",
        "Japonés para iPhone. Frases reales con lo que contesta el personal, los dos silabarios, kanji con orden de trazos y sesiones cortas que recuperan lo que estás a punto de olvidar.",
        "Le japonais pour iPhone. De vraies phrases avec ce que le personnel répond, les deux kana, les kanji avec l'ordre des traits, et des séances courtes qui ramènent ce que vous êtes sur le point d'oublier.",
        "Giapponese per iPhone. Frasi vere con quello che risponde il personale, entrambi i kana, kanji con l'ordine dei tratti e sessioni brevi che riportano quello che stai per dimenticare.",
        "iPhone のための日本語。店員さんの返答つきの実際のフレーズ、両方のかな、筆順つきの漢字、そして忘れかけたものを先に戻してくれる短い学習。",
        "iPhone을 위한 일본어. 직원의 답변이 함께 나오는 실제 표현, 두 가나, 필순이 있는 한자, 그리고 잊기 직전인 것을 먼저 되돌려 주는 짧은 학습.",
        "Japans voor iPhone. Echte zinnen met wat het personeel terugzegt, beide kana, kanji met streepvolgorde, en korte sessies die terughalen wat je bijna vergeten bent.",
        "Japonês para iPhone. Frases reais com o que o atendente responde, os dois kana, kanji com ordem dos traços e sessões curtas que trazem de volta o que você está prestes a esquecer.",
        "iPhone 上的日语。附有店员回答的真实句子、两套假名、带笔顺的汉字，以及会把你快忘的内容先带回来的短时学习。"),

    "The Kippu icon: a tilted cobalt train ticket on pale paper.": (
        "Das Kippu-Symbol: eine schräg liegende kobaltblaue Fahrkarte auf hellem Papier.",
        "El icono de Kippu: un billete de tren azul cobalto inclinado sobre papel claro.",
        "El ícono de Kippu: un boleto de tren azul cobalto inclinado sobre papel claro.",
        "L'icône de Kippu : un billet de train bleu cobalt incliné sur du papier clair.",
        "L'icona di Kippu: un biglietto del treno blu cobalto inclinato su carta chiara.",
        "Kippu のアイコン：淡い紙の上に斜めに置かれたコバルトブルーの切符。",
        "Kippu 아이콘: 옅은 종이 위에 비스듬히 놓인 코발트색 기차표.",
        "Het Kippu-icoon: een schuin liggend kobaltblauw treinkaartje op licht papier.",
        "O ícone do Kippu: uma passagem de trem azul-cobalto inclinada sobre papel claro.",
        "Kippu 的图标：浅色纸上一张斜放的钴蓝色火车票。"),

    "Japanese for iPhone and iPad": (
        "Japanisch für iPhone und iPad", "Japonés para iPhone y iPad", "Japonés para iPhone y iPad",
        "Le japonais pour iPhone et iPad", "Giapponese per iPhone e iPad", "iPhone と iPad のための日本語",
        "iPhone과 iPad를 위한 일본어", "Japans voor iPhone en iPad", "Japonês para iPhone e iPad", "iPhone 和 iPad 上的日语"),

    "The Japanese you need for the trip. Then the JLPT N5.": (
        "Das Japanisch, das du für die Reise brauchst. Danach der JLPT N5.",
        "El japonés que necesitas para el viaje. Y después, el JLPT N5.",
        "El japonés que necesitas para el viaje. Y después, el JLPT N5.",
        "Le japonais qu'il vous faut pour le voyage. Puis le JLPT N5.",
        "Il giapponese che ti serve per il viaggio. Poi il JLPT N5.",
        "旅に必要な日本語。そして JLPT N5 へ。",
        "여행에 필요한 일본어. 그다음은 JLPT N5.",
        "Het Japans dat je nodig hebt voor de reis. Daarna het JLPT N5.",
        "O japonês que você precisa para a viagem. Depois, o JLPT N5.",
        "旅行要用的日语。然后是 JLPT N5。"),

    "Real phrases with what the staff say back. Both kana, then kanji with their stroke order. Short sittings that bring back what you are about to forget, before you forget it.": (
        "Echte Sätze mit dem, was das Personal antwortet. Beide Kana, dann Kanji mit ihrer Strichfolge. Kurze Lektionen, die zurückholen, was du gerade vergessen würdest, bevor du es vergisst.",
        "Frases reales con lo que responde el personal. Los dos silabarios, y luego kanji con su orden de trazos. Sesiones cortas que recuperan lo que estás a punto de olvidar, antes de que lo olvides.",
        "Frases reales con lo que contesta el personal. Los dos silabarios, y luego kanji con su orden de trazos. Sesiones cortas que recuperan lo que estás a punto de olvidar, antes de que lo olvides.",
        "De vraies phrases avec ce que le personnel répond. Les deux kana, puis les kanji avec l'ordre des traits. Des séances courtes qui ramènent ce que vous êtes sur le point d'oublier, avant que vous ne l'oubliiez.",
        "Frasi vere con quello che risponde il personale. Entrambi i kana, poi i kanji con il loro ordine dei tratti. Sessioni brevi che riportano quello che stai per dimenticare, prima che tu lo dimentichi.",
        "店員さんの返答つきの実際のフレーズ。両方のかな、それから筆順つきの漢字。忘れかけたものを、忘れる前に戻してくれる短い学習。",
        "직원의 답변이 함께 나오는 실제 표현. 두 가나, 그다음 필순이 있는 한자. 잊기 직전인 것을 잊기 전에 되돌려 주는 짧은 학습.",
        "Echte zinnen met wat het personeel terugzegt. Beide kana, daarna kanji met hun streepvolgorde. Korte sessies die terughalen wat je bijna vergeten bent, voordat je het vergeet.",
        "Frases reais com o que o atendente responde. Os dois kana, depois kanji com a ordem dos traços. Sessões curtas que trazem de volta o que você está prestes a esquecer, antes que esqueça.",
        "附有店员回答的真实句子。两套假名，然后是带笔顺的汉字。在你忘掉之前，把快忘的内容先带回来的短时学习。"),

    "Which sound is this?": (
        "Welcher Laut ist das?", "¿Qué sonido es este?", "¿Qué sonido es este?", "Quel est ce son ?",
        "Che suono è?", "この音は？", "이 소리는?", "Welke klank is dit?", "Que som é este?", "这是什么音？"),

    "Tap the reading. This is the kind of check the app asks, with the same right and wrong colours.": (
        "Tippe auf die Lesung. So eine Frage stellt die App, mit denselben Farben für richtig und falsch.",
        "Toca la lectura. Este es el tipo de comprobación que hace la aplicación, con los mismos colores para acierto y error.",
        "Toca la lectura. Este es el tipo de revisión que hace la aplicación, con los mismos colores para acierto y error.",
        "Touchez la lecture. C'est le genre de question que pose l'application, avec les mêmes couleurs pour juste et faux.",
        "Tocca la lettura. È il tipo di verifica che fa l'app, con gli stessi colori per giusto e sbagliato.",
        "読み方をタップしてください。アプリが出すのはこの種の確認問題で、正解と不正解の色も同じです。",
        "읽는 법을 탭하세요. 앱이 내는 확인 문제가 이런 식이고, 맞음과 틀림의 색도 같습니다.",
        "Tik op de uitspraak. Dit is het soort controle dat de app doet, met dezelfde kleuren voor goed en fout.",
        "Toque na leitura. É o tipo de verificação que o app faz, com as mesmas cores de certo e errado.",
        "点一下读音。这就是应用里的检查题，对错的颜色也一样。"),

    "Download on the App Store": (
        "Im App Store laden", "Descargar en el App Store", "Descargar en el App Store",
        "Télécharger dans l'App Store", "Scarica dall'App Store", "App Store でダウンロード",
        "App Store에서 다운로드", "Download in de App Store", "Baixar na App Store", "在 App Store 下载"),

    "Free to start. iPhone and iPad, iOS 18 and later. Kippu Plus opens everything, with the first week free.": (
        "Der Einstieg ist kostenlos. iPhone und iPad, iOS 18 und neuer. Kippu Plus öffnet alles, mit einer kostenlosen ersten Woche.",
        "Gratis para empezar. iPhone y iPad, iOS 18 o posterior. Kippu Plus lo abre todo, con la primera semana gratis.",
        "Gratis para empezar. iPhone y iPad, iOS 18 o posterior. Kippu Plus lo abre todo, con la primera semana gratis.",
        "Gratuit pour commencer. iPhone et iPad, iOS 18 ou plus récent. Kippu Plus ouvre tout, avec la première semaine offerte.",
        "Gratis per iniziare. iPhone e iPad, iOS 18 o successivo. Kippu Plus apre tutto, con la prima settimana gratis.",
        "無料で始められます。iPhone と iPad、iOS 18 以降。Kippu Plus ですべてが開き、最初の1週間は無料です。",
        "무료로 시작. iPhone과 iPad, iOS 18 이상. Kippu Plus로 전부 열리며, 첫 일주일은 무료입니다.",
        "Gratis om te beginnen. iPhone en iPad, iOS 18 en later. Kippu Plus opent alles, met de eerste week gratis.",
        "Grátis para começar. iPhone e iPad, iOS 18 ou posterior. O Kippu Plus abre tudo, com a primeira semana grátis.",
        "免费开始。iPhone 和 iPad，iOS 18 及以上。Kippu Plus 解锁全部内容，第一周免费。"),

    "Two paths, one app": (
        "Zwei Wege, eine App", "Dos rutas, una aplicación", "Dos rutas, una aplicación", "Deux parcours, une application",
        "Due percorsi, un'app", "ふたつのコース、ひとつのアプリ", "두 가지 코스, 하나의 앱", "Twee routes, één app",
        "Duas trilhas, um app", "两条路线，一个应用"),

    "For the trip": (
        "Für die Reise", "Para el viaje", "Para el viaje", "Pour le voyage", "Per il viaggio", "旅のために",
        "여행을 위해", "Voor de reis", "Para a viagem", "为了旅行"),

    "Travel": (
        "Reise", "Viaje", "Viaje", "Voyage", "Viaggio", "旅行", "여행", "Reizen", "Viagem", "旅行"),

    "Eleven short modules in the order a trip happens: arriving, the konbini, restaurants, hotels and ryokan, trains, shopping, health, being polite, sights, reading the city. Each phrase comes with what the staff say back and how you answer.": (
        "Elf kurze Module in der Reihenfolge einer Reise: Ankunft, Konbini, Restaurants, Hotels und Ryokan, Züge, Einkaufen, Gesundheit, Höflichkeit, Sehenswürdigkeiten, sich in der Stadt zurechtfinden. Zu jedem Satz gehört, was das Personal antwortet und was du darauf sagst.",
        "Once módulos cortos en el orden en que ocurre un viaje: la llegada, el konbini, restaurantes, hoteles y ryokan, trenes, compras, salud, ser educado, lugares que ver, orientarse en la ciudad. Cada frase viene con lo que responde el personal y cómo contestas.",
        "Once módulos cortos en el orden en que ocurre un viaje: la llegada, el konbini, restaurantes, hoteles y ryokan, trenes, compras, salud, ser educado, lugares que ver, ubicarse en la ciudad. Cada frase viene con lo que contesta el personal y cómo respondes.",
        "Onze modules courts dans l'ordre d'un voyage : l'arrivée, le konbini, les restaurants, hôtels et ryokan, les trains, les achats, la santé, la politesse, les visites, se repérer en ville. Chaque phrase vient avec ce que le personnel répond et ce que vous dites ensuite.",
        "Undici moduli brevi nell'ordine in cui si svolge un viaggio: l'arrivo, il konbini, ristoranti, hotel e ryokan, treni, acquisti, salute, buone maniere, cose da vedere, orientarsi in città. Ogni frase arriva con quello che risponde il personale e con quello che dici tu.",
        "旅の流れにそった11の短いモジュール：到着、コンビニ、レストラン、ホテルと旅館、電車、買い物、体調、マナー、観光、街の中で迷わないために。どのフレーズにも店員さんの返答と、それにどう答えるかが付いています。",
        "여행 순서 그대로 짧은 모듈 11개: 도착, 편의점, 식당, 호텔과 료칸, 전철, 쇼핑, 몸이 아플 때, 예의, 볼거리, 도시에서 길 찾기. 모든 표현에 직원이 뭐라고 답하는지, 그리고 어떻게 대답하면 되는지가 함께 나옵니다.",
        "Elf korte modules in de volgorde van een reis: aankomst, de konbini, restaurants, hotels en ryokan, treinen, winkelen, gezondheid, beleefd zijn, bezienswaardigheden, de weg vinden in de stad. Bij elke zin hoort wat het personeel terugzegt en wat jij dan antwoordt.",
        "Onze módulos curtos na ordem em que a viagem acontece: a chegada, o konbini, restaurantes, hotéis e ryokan, trens, compras, saúde, boas maneiras, o que ver, se achar na cidade. Cada frase vem com o que o atendente responde e como você continua.",
        "十一个短模块，按旅行发生的顺序：抵达、便利店、餐厅、酒店和旅馆、电车、购物、身体不适、礼貌、景点、在城市里认路。每句话都附有店员会怎么回答，以及你接下来怎么说。"),

    "For the exam": (
        "Für die Prüfung", "Para el examen", "Para el examen", "Pour l'examen", "Per l'esame", "試験のために",
        "시험을 위해", "Voor het examen", "Para a prova", "为了考试"),

    "Twenty-two units covering the exam: both kana, 690 words, 103 kanji with stroke order, 72 grammar points, listening, reading passages, and a thirty-question mock test.": (
        "Zweiundzwanzig Einheiten für die Prüfung: beide Kana, 690 Wörter, 103 Kanji mit Strichfolge, 72 Grammatikpunkte, Hörverstehen, Lesetexte und ein Probetest mit dreißig Fragen.",
        "Veintidós unidades que cubren el examen: los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, textos de lectura y un examen de prueba de treinta preguntas.",
        "Veintidós unidades que cubren el examen: los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, textos de lectura y un examen de prueba de treinta preguntas.",
        "Vingt-deux unités qui couvrent l'examen : les deux kana, 690 mots, 103 kanji avec l'ordre des traits, 72 points de grammaire, compréhension orale, textes de lecture et un test blanc de trente questions.",
        "Ventidue unità che coprono l'esame: entrambi i kana, 690 parole, 103 kanji con l'ordine dei tratti, 72 punti di grammatica, ascolto, brani di lettura e un test di prova da trenta domande.",
        "試験範囲をカバーする22ユニット：ひらがなとカタカナ、単語690語、筆順つきの漢字103字、文法72項目、聴解、読解、30問の模擬試験。",
        "시험 범위를 다루는 22개 단원: 두 가나, 단어 690개, 필순이 있는 한자 103자, 문법 72개, 듣기, 독해 지문, 30문항 모의고사.",
        "Tweeëntwintig eenheden die het examen dekken: beide kana, 690 woorden, 103 kanji met streepvolgorde, 72 grammaticapunten, luisteren, leesteksten en een proeftoets van dertig vragen.",
        "Vinte e duas unidades que cobrem a prova: os dois kana, 690 palavras, 103 kanji com ordem dos traços, 72 pontos de gramática, compreensão auditiva, textos de leitura e um simulado de trinta questões.",
        "二十二个单元覆盖考试：两套假名、690个单词、103个带笔顺的汉字、72个语法点、听力、阅读短文，以及一套三十题的模拟考试。"),

    "Choose on the first screen and switch whenever you like. What you learn on one path counts on the other.": (
        "Wähle auf dem ersten Bildschirm und wechsle, wann du willst. Was du auf dem einen Weg lernst, zählt auch auf dem anderen.",
        "Elige en la primera pantalla y cambia cuando quieras. Lo que aprendes en una ruta cuenta en la otra.",
        "Elige en la primera pantalla y cambia cuando quieras. Lo que aprendes en una ruta cuenta en la otra.",
        "Choisissez sur le premier écran et changez quand vous voulez. Ce que vous apprenez sur un parcours compte sur l'autre.",
        "Scegli nella prima schermata e cambia quando vuoi. Quello che impari su un percorso conta anche sull'altro.",
        "最初の画面で選び、いつでも切り替えられます。片方のコースで学んだことは、もう片方でも数えられます。",
        "첫 화면에서 고르고 언제든 바꿀 수 있습니다. 한 코스에서 배운 것은 다른 코스에서도 인정됩니다.",
        "Kies op het eerste scherm en wissel wanneer je wilt. Wat je op de ene route leert, telt op de andere.",
        "Escolha na primeira tela e troque quando quiser. O que você aprende em uma trilha conta na outra.",
        "在第一个屏幕上选择，随时可以切换。你在一条路线上学到的，在另一条路线上也算数。"),

    "How Japan works": (
        "Wie Japan funktioniert", "Cómo funciona Japón", "Cómo funciona Japón", "Comment marche le Japon",
        "Come funziona il Giappone", "日本の仕組み", "일본이 돌아가는 방식", "Hoe Japan werkt",
        "Como o Japão funciona", "日本是怎么运转的"),

    "Fifty quick cards on the things nobody teaches in a phrasebook: train types and station numbers, IC cards, the last train, tipping, shoes, onsen etiquette, the emergency numbers. Each one has a one-question check, so it sticks.": (
        "Fünfzig kurze Karten zu dem, was kein Sprachführer erklärt: Zugtypen und Stationsnummern, IC-Karten, der letzte Zug, Trinkgeld, Schuhe, Onsen-Etikette, die Notrufnummern. Jede mit einer Kontrollfrage, damit es hängen bleibt.",
        "Cincuenta tarjetas rápidas sobre lo que ninguna guía de frases enseña: tipos de tren y números de estación, tarjetas IC, el último tren, las propinas, los zapatos, la etiqueta del onsen, los números de emergencia. Cada una con una pregunta de comprobación, para que se quede.",
        "Cincuenta tarjetas rápidas sobre lo que ninguna guía de frases enseña: tipos de tren y números de estación, tarjetas IC, el último tren, las propinas, los zapatos, la etiqueta del onsen, los números de emergencia. Cada una con una pregunta de repaso, para que se quede.",
        "Cinquante fiches rapides sur ce qu'aucun guide de conversation n'apprend : types de trains et numéros de gares, cartes IC, le dernier train, le pourboire, les chaussures, les usages au onsen, les numéros d'urgence. Chacune avec une question de contrôle, pour que ça reste.",
        "Cinquanta schede rapide sulle cose che nessun frasario insegna: tipi di treno e numeri delle stazioni, carte IC, l'ultimo treno, la mancia, le scarpe, le regole dell'onsen, i numeri di emergenza. Ognuna con una domanda di verifica, così resta.",
        "会話集には載っていないことを50枚のカードで：電車の種類と駅ナンバー、ICカード、終電、チップ、靴、温泉のマナー、緊急連絡先。それぞれに確認問題が1問あるので、身につきます。",
        "회화집에는 없는 것들을 빠른 카드 50장으로: 전철 종류와 역 번호, IC 카드, 막차, 팁, 신발, 온천 예절, 긴급 전화번호. 카드마다 확인 문제가 하나 있어 머리에 남습니다.",
        "Vijftig korte kaarten over wat geen enkel taalgidsje leert: treinsoorten en stationsnummers, IC-kaarten, de laatste trein, fooi, schoenen, onsen-etiquette, de alarmnummers. Elk met één controlevraag, zodat het blijft hangen.",
        "Cinquenta cartões rápidos sobre o que nenhum guia de frases ensina: tipos de trem e números das estações, cartões IC, o último trem, gorjeta, sapatos, etiqueta do onsen, os números de emergência. Cada um com uma pergunta de verificação, para fixar.",
        "五十张小卡片，讲会话手册里没人教的事：电车种类和车站编号、IC卡、末班车、小费、脱鞋、温泉礼仪、紧急电话。每张一道检查题，记得牢。"),

    "How you learn": (
        "So lernst du", "Cómo aprendes", "Cómo aprendes", "Comment vous apprenez", "Come impari", "学び方",
        "배우는 방식", "Zo leer je", "Como você aprende", "学习方式"),

    "Short sittings": (
        "Kurze Lektionen", "Sesiones cortas", "Sesiones cortas", "Des séances courtes", "Sessioni brevi", "短い時間で",
        "짧게 자주", "Korte sessies", "Sessões curtas", "每次一小会儿"),

    "A few minutes at a time. What you are about to forget comes back first, so the time goes where it does the most good.": (
        "Ein paar Minuten am Stück. Was du gerade vergessen würdest, kommt zuerst zurück, damit die Zeit dorthin geht, wo sie am meisten bringt.",
        "Unos minutos cada vez. Lo que estás a punto de olvidar vuelve primero, así que el tiempo va donde más rinde.",
        "Unos minutos cada vez. Lo que estás a punto de olvidar vuelve primero, así que el tiempo va donde más rinde.",
        "Quelques minutes à la fois. Ce que vous êtes sur le point d'oublier revient en premier, pour que le temps aille là où il sert le plus.",
        "Pochi minuti alla volta. Quello che stai per dimenticare torna per primo, così il tempo va dove rende di più.",
        "一度に数分だけ。忘れかけたものが最初に戻ってくるので、時間はいちばん効くところに使われます。",
        "한 번에 몇 분씩. 잊기 직전인 것이 먼저 돌아오므로, 시간이 가장 효과 있는 곳에 쓰입니다.",
        "Een paar minuten per keer. Wat je bijna vergeten bent, komt als eerste terug, zodat de tijd gaat waar hij het meeste oplevert.",
        "Alguns minutos de cada vez. O que você está prestes a esquecer volta primeiro, então o tempo vai para onde rende mais.",
        "每次几分钟。快忘的先回来，所以时间花在最有用的地方。"),

    "At your own pace": (
        "In deinem Tempo", "A tu ritmo", "A tu ritmo", "À votre rythme", "Al tuo ritmo", "自分のペースで",
        "내 속도대로", "In je eigen tempo", "No seu ritmo", "按自己的节奏"),

    "Learn ahead, review a module, or go over everything you know, whenever you like. Nothing is locked behind a calendar.": (
        "Lerne voraus, wiederhole ein Modul oder geh alles durch, was du kannst, wann du willst. Nichts hängt an einem Kalender.",
        "Adelántate, repasa un módulo o repasa todo lo que sabes, cuando quieras. Nada está cerrado detrás de un calendario.",
        "Adelántate, repasa un módulo o repasa todo lo que sabes, cuando quieras. Nada está cerrado detrás de un calendario.",
        "Prenez de l'avance, révisez un module ou repassez tout ce que vous savez, quand vous voulez. Rien n'est verrouillé derrière un calendrier.",
        "Vai avanti, ripassa un modulo o rivedi tutto quello che sai, quando vuoi. Niente è bloccato dietro un calendario.",
        "先に進む、モジュールを復習する、覚えたことを全部見直す。どれもいつでも。カレンダーに縛られるものはありません。",
        "앞서 배우거나, 한 모듈을 복습하거나, 아는 것을 전부 훑어보거나, 원할 때 언제든. 달력에 묶인 것은 없습니다.",
        "Loop vooruit, herhaal een module of ga alles na wat je kent, wanneer je wilt. Niets zit achter een kalender.",
        "Adiante-se, revise um módulo ou reveja tudo o que já sabe, quando quiser. Nada fica trancado atrás de um calendário.",
        "提前学、复习某个模块，或把学过的全部过一遍，随时都可以。没有任何东西被日历锁住。"),

    "A voice on every line": (
        "Eine Stimme auf jeder Zeile", "Una voz en cada línea", "Una voz en cada línea", "Une voix sur chaque ligne",
        "Una voce su ogni riga", "すべての行に音声", "모든 문장에 음성", "Een stem bij elke regel",
        "Uma voz em cada linha", "每一句都有配音"),

    "Every word, phrase and sentence is spoken, a little slower than street speed so each syllable is there to hear. Staff replies use a second voice.": (
        "Jedes Wort, jeder Satz und jede Wendung wird gesprochen, etwas langsamer als auf der Straße, damit jede Silbe zu hören ist. Die Antworten des Personals kommen von einer zweiten Stimme.",
        "Cada palabra, frase y oración se pronuncia, un poco más despacio que en la calle para que cada sílaba se oiga. Las respuestas del personal usan una segunda voz.",
        "Cada palabra, frase y oración se pronuncia, un poco más despacio que en la calle para que cada sílaba se oiga. Las respuestas del personal usan una segunda voz.",
        "Chaque mot, chaque phrase est prononcé, un peu plus lentement que dans la rue pour que chaque syllabe s'entende. Les réponses du personnel utilisent une seconde voix.",
        "Ogni parola e ogni frase viene pronunciata, un po' più lenta della velocità di strada così ogni sillaba si sente. Le risposte del personale usano una seconda voce.",
        "すべての単語、フレーズ、文が読み上げられます。街で聞くより少しゆっくりなので、一音一音が聞き取れます。店員さんの返答は別の声です。",
        "모든 단어, 표현, 문장이 읽힙니다. 거리에서 듣는 것보다 조금 느려서 음절 하나하나가 들립니다. 직원의 답변은 다른 목소리입니다.",
        "Elk woord, elke zin wordt uitgesproken, iets langzamer dan op straat zodat elke lettergreep te horen is. Antwoorden van het personeel komen van een tweede stem.",
        "Cada palavra, frase e oração é falada, um pouco mais devagar que na rua para que cada sílaba se ouça. As respostas do atendente usam uma segunda voz.",
        "每个词、每个短语、每个句子都有配音，比街上的语速稍慢一点，每个音节都听得清。店员的回答用另一个声音。"),

    "Three games": (
        "Drei Spiele", "Tres juegos", "Tres juegos", "Trois jeux", "Tre giochi", "3つのゲーム", "세 가지 게임",
        "Drie spellen", "Três jogos", "三个游戏"),

    "Match pairs, race the clock, or catch falling kanji by typing their readings. Only what you already know shows up, so a game is always practice.": (
        "Paare finden, gegen die Uhr, oder fallende Kanji auffangen, indem du ihre Lesung tippst. Es erscheint nur, was du schon kennst, ein Spiel ist also immer Übung.",
        "Empareja, corre contra el reloj o atrapa kanji que caen escribiendo su lectura. Solo aparece lo que ya sabes, así que un juego siempre es práctica.",
        "Empareja, corre contra el reloj o atrapa kanji que caen escribiendo su lectura. Solo aparece lo que ya sabes, así que un juego siempre es práctica.",
        "Associez des paires, courez contre la montre ou attrapez des kanji qui tombent en tapant leur lecture. Seul ce que vous savez déjà apparaît, un jeu est donc toujours de l'entraînement.",
        "Abbina le coppie, corri contro il tempo o prendi i kanji che cadono scrivendo la loro lettura. Compare solo quello che sai già, quindi un gioco è sempre esercizio.",
        "ペアを合わせる、時間と競う、落ちてくる漢字の読みを打って受け止める。出てくるのは覚えたものだけなので、ゲームはいつでも練習になります。",
        "짝을 맞추고, 시간과 겨루고, 떨어지는 한자의 읽는 법을 입력해 받아냅니다. 이미 아는 것만 나오므로 게임은 언제나 연습입니다.",
        "Zoek paren, race tegen de klok of vang vallende kanji door hun uitspraak te typen. Alleen wat je al kent komt voorbij, dus een spel is altijd oefening.",
        "Combine pares, corra contra o relógio ou pegue kanji que caem digitando a leitura deles. Só aparece o que você já sabe, então um jogo é sempre prática.",
        "配对、和时间赛跑，或者通过输入读音接住落下的汉字。只出现你已经学过的内容，所以游戏永远是练习。"),

    "Keep going": (
        "Dranbleiben", "Sigue adelante", "Sigue adelante", "Continuer", "Continua così", "続ける", "꾸준히",
        "Volhouden", "Continue", "坚持下去"),

    "A placement check so you start at the right level. A streak, a level that grows with what you remember, and an evening reminder if you want one.": (
        "Ein kurzer Einstufungstest, damit du auf der richtigen Stufe anfängst. Eine Serie, ein Level, das mit dem wächst, was du behältst, und eine abendliche Erinnerung, wenn du magst.",
        "Una prueba de nivel para empezar donde te corresponde. Una racha, un nivel que crece con lo que recuerdas y un recordatorio nocturno si lo quieres.",
        "Una prueba de nivel para empezar donde te corresponde. Una racha, un nivel que crece con lo que recuerdas y un recordatorio nocturno si lo quieres.",
        "Un test de niveau pour commencer au bon endroit. Une série, un niveau qui grandit avec ce que vous retenez, et un rappel du soir si vous le souhaitez.",
        "Un test di livello per partire dal punto giusto. Una serie, un livello che cresce con quello che ricordi e un promemoria serale se lo vuoi.",
        "レベルチェックで、ちょうどいいところから始められます。連続記録、覚えた分だけ上がるレベル、必要なら夜のリマインダー。",
        "레벨 테스트로 알맞은 곳에서 시작합니다. 연속 기록, 기억하는 만큼 올라가는 레벨, 원하면 저녁 알림.",
        "Een niveautest zodat je op de juiste plek begint. Een reeks, een level dat groeit met wat je onthoudt, en een avondherinnering als je wilt.",
        "Um teste de nível para começar no lugar certo. Uma sequência, um nível que cresce com o que você lembra e um lembrete noturno se quiser.",
        "水平测试让你从合适的地方开始。连续打卡、随记住的内容增长的等级，以及想要的话可以开的晚间提醒。"),

    "Both kana units, the first module of each path and the Guide are free. Kippu Plus opens every module on both paths, the three games and all seven themes.": (
        "Beide Kana, das erste Modul jedes Wegs und der Ratgeber sind kostenlos. Kippu Plus öffnet jedes Modul auf beiden Wegen, die drei Spiele und alle sieben Designs.",
        "Los dos silabarios, el primer módulo de cada ruta y la Guía son gratis. Kippu Plus abre todos los módulos de ambas rutas, los tres juegos y los siete temas.",
        "Los dos silabarios, el primer módulo de cada ruta y la Guía son gratis. Kippu Plus abre todos los módulos de ambas rutas, los tres juegos y los siete temas.",
        "Les deux kana, le premier module de chaque parcours et le Guide sont gratuits. Kippu Plus ouvre tous les modules des deux parcours, les trois jeux et les sept thèmes.",
        "Entrambi i kana, il primo modulo di ogni percorso e la Guida sono gratis. Kippu Plus apre tutti i moduli di entrambi i percorsi, i tre giochi e i sette temi.",
        "両方のかな、各コースの最初のモジュール、ガイドは無料です。Kippu Plus で両コースのすべてのモジュール、3つのゲーム、7つのテーマが開きます。",
        "두 가나, 각 코스의 첫 모듈, 가이드는 무료입니다. Kippu Plus로 두 코스의 모든 모듈, 세 가지 게임, 테마 7종이 열립니다.",
        "Beide kana, de eerste module van elke route en de Gids zijn gratis. Kippu Plus opent elke module op beide routes, de drie spellen en alle zeven thema's.",
        "Os dois kana, o primeiro módulo de cada trilha e o Guia são grátis. O Kippu Plus abre todos os módulos das duas trilhas, os três jogos e os sete temas.",
        "两套假名、每条路线的第一个模块和指南都是免费的。Kippu Plus 解锁两条路线的全部模块、三个游戏和全部七个主题。"),

    "a year": ("pro Jahr", "al año", "al año", "par an", "all'anno", "年額", "연간", "per jaar", "por ano", "每年"),
    "Seven months free": ("Sieben Monate geschenkt", "Siete meses gratis", "Siete meses gratis", "Sept mois offerts",
                          "Sette mesi gratis", "7か月分お得", "일곱 달 무료", "Zeven maanden gratis", "Sete meses grátis", "省下七个月"),
    "a month": ("pro Monat", "al mes", "al mes", "par mois", "al mese", "月額", "월간", "per maand", "por mês", "每月"),

    "The first week is free on either plan. Cancel any time in your Apple account. Prices shown in US dollars; the App Store shows yours.": (
        "Die erste Woche ist bei beiden Plänen kostenlos. Kündbar jederzeit in deinem Apple-Konto. Preise in US-Dollar; der App Store zeigt deine.",
        "La primera semana es gratis con cualquiera de los dos planes. Cancela cuando quieras en tu cuenta de Apple. Precios en dólares estadounidenses; el App Store muestra los tuyos.",
        "La primera semana es gratis con cualquiera de los dos planes. Cancela cuando quieras en tu cuenta de Apple. Precios en dólares estadounidenses; el App Store muestra los tuyos.",
        "La première semaine est offerte avec l'un ou l'autre. Résiliable à tout moment dans votre compte Apple. Prix en dollars américains ; l'App Store affiche les vôtres.",
        "La prima settimana è gratis con entrambi i piani. Disdici quando vuoi dal tuo account Apple. Prezzi in dollari americani; l'App Store mostra i tuoi.",
        "どちらのプランも最初の1週間は無料。Apple アカウントからいつでも解約できます。表示は米ドルで、App Store にはお住まいの地域の価格が表示されます。",
        "어느 플랜이든 첫 일주일은 무료. Apple 계정에서 언제든 해지할 수 있습니다. 표시는 미국 달러이며, App Store에는 현지 가격이 나옵니다.",
        "De eerste week is gratis bij beide plannen. Opzeggen kan altijd in je Apple-account. Prijzen in Amerikaanse dollars; de App Store toont de jouwe.",
        "A primeira semana é grátis em qualquer plano. Cancele quando quiser na sua conta Apple. Preços em dólares americanos; a App Store mostra os seus.",
        "两种方案的第一周都免费。可随时在 Apple 账户里取消。此处以美元显示，App Store 会显示你所在地区的价格。"),

    "What it does not do": (
        "Was die App nicht tut", "Lo que no hace", "Lo que no hace", "Ce qu'elle ne fait pas", "Cosa non fa",
        "しないこと", "하지 않는 것", "Wat het niet doet", "O que ele não faz", "它不做的事"),

    "No account and nothing to sign in to. No advertising, no analytics, no tracking. Your progress stays on your phone and, if you use iCloud, in your own private iCloud database, which Apple holds and I cannot read. Every lesson, recording and game is on the device, so the app works on the plane.": (
        "Kein Konto und nichts zum Anmelden. Keine Werbung, keine Analyse, kein Tracking. Dein Fortschritt bleibt auf deinem Telefon und, wenn du iCloud nutzt, in deiner eigenen privaten iCloud-Datenbank, die Apple verwahrt und die ich nicht lesen kann. Jede Lektion, jede Aufnahme und jedes Spiel ist auf dem Gerät, die App funktioniert also auch im Flugzeug.",
        "Sin cuenta y sin nada en lo que iniciar sesión. Sin publicidad, sin analítica, sin rastreo. Tu progreso se queda en tu teléfono y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que yo no puedo leer. Cada lección, grabación y juego está en el dispositivo, así que la aplicación funciona en el avión.",
        "Sin cuenta y sin nada en lo que iniciar sesión. Sin publicidad, sin analítica, sin rastreo. Tu progreso se queda en tu teléfono y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que yo no puedo leer. Cada lección, grabación y juego está en el dispositivo, así que la aplicación funciona en el avión.",
        "Pas de compte et rien où se connecter. Pas de publicité, pas d'analyse d'audience, pas de pistage. Votre progression reste sur votre téléphone et, si vous utilisez iCloud, dans votre propre base de données iCloud privée, qu'Apple héberge et que je ne peux pas lire. Chaque leçon, enregistrement et jeu est sur l'appareil, l'application fonctionne donc dans l'avion.",
        "Nessun account e niente a cui accedere. Nessuna pubblicità, nessuna analisi, nessun tracciamento. I tuoi progressi restano sul tuo telefono e, se usi iCloud, nel tuo database iCloud privato, che Apple custodisce e che io non posso leggere. Ogni lezione, registrazione e gioco è sul dispositivo, quindi l'app funziona in aereo.",
        "アカウントもサインインもありません。広告も、解析も、トラッキングもありません。学習の進み具合は端末に残り、iCloud を使っていればあなた自身のプライベートな iCloud データベースにも保存されます。それは Apple が保管し、私には読めません。すべてのレッスン、音声、ゲームが端末の中にあるので、飛行機の中でも使えます。",
        "계정도 없고 로그인할 것도 없습니다. 광고도, 분석도, 추적도 없습니다. 진행 상황은 휴대폰에 남고, iCloud를 쓰면 본인의 비공개 iCloud 데이터베이스에도 저장됩니다. 그것은 Apple이 보관하며 저는 읽을 수 없습니다. 모든 수업, 녹음, 게임이 기기 안에 있어서 비행기 안에서도 됩니다.",
        "Geen account en niets om op in te loggen. Geen advertenties, geen analytics, geen tracking. Je voortgang blijft op je telefoon en, als je iCloud gebruikt, in je eigen privé-iCloud-database, die Apple bewaart en die ik niet kan lezen. Elke les, opname en elk spel staat op het apparaat, dus de app werkt in het vliegtuig.",
        "Sem conta e sem nada para entrar. Sem publicidade, sem análise, sem rastreamento. Seu progresso fica no seu celular e, se você usa o iCloud, no seu próprio banco de dados privado do iCloud, que a Apple guarda e que eu não consigo ler. Cada lição, gravação e jogo está no aparelho, então o app funciona no avião.",
        "没有账户，没有需要登录的东西。没有广告，没有分析，没有追踪。你的进度留在手机上；如果你使用 iCloud，也会保存在你自己的私有 iCloud 数据库中，由 Apple 保管，我无法读取。每一课、每段录音、每个游戏都在设备里，所以在飞机上也能用。"),

    "The privacy policy": (
        "Die Datenschutzerklärung", "La política de privacidad", "La política de privacidad",
        "La politique de confidentialité", "L'informativa sulla privacy", "プライバシーポリシー",
        "개인정보 처리방침", "Het privacybeleid", "A política de privacidade", "隐私政策"),

    "says the same at greater length, and says nothing else.": (
        "sagt dasselbe ausführlicher, und sonst nichts.",
        "dice lo mismo con más detalle, y no dice nada más.",
        "dice lo mismo con más detalle, y no dice nada más.",
        "dit la même chose plus longuement, et rien d'autre.",
        "dice la stessa cosa più per esteso, e non dice altro.",
        "には同じことがもう少し詳しく書いてあり、それ以外のことは書いてありません。",
        "에는 같은 내용이 더 길게 적혀 있고, 그 밖의 내용은 없습니다.",
        "zegt hetzelfde, uitgebreider, en verder niets.",
        "diz a mesma coisa com mais detalhes, e não diz mais nada.",
        "把同样的话说得更详细一些，除此之外什么也没有。"),

    "Questions": ("Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問", "자주 묻는 질문",
                  "Vragen", "Perguntas", "常见问题"),

    "Is Kippu for a trip or for the JLPT?": (
        "Ist Kippu für die Reise oder für den JLPT?", "¿Kippu es para un viaje o para el JLPT?",
        "¿Kippu es para un viaje o para el JLPT?", "Kippu, c'est pour un voyage ou pour le JLPT ?",
        "Kippu è per un viaggio o per il JLPT?", "Kippu は旅行用ですか、JLPT 用ですか？",
        "Kippu는 여행용인가요, JLPT용인가요?", "Is Kippu voor een reis of voor het JLPT?",
        "O Kippu é para uma viagem ou para o JLPT?", "Kippu 是为旅行还是为 JLPT？"),

    "Both, and you choose on the first screen. The travel path is eleven short modules in the order a trip happens, from arriving to reading the city. The N5 path is the whole exam: both kana, 690 words, 103 kanji, 72 grammar points, listening, reading and a mock test. You can switch between them at any time and everything you learn on one counts on the other.": (
        "Beides, und du wählst auf dem ersten Bildschirm. Der Reiseweg besteht aus elf kurzen Modulen in der Reihenfolge einer Reise, von der Ankunft bis zum Zurechtfinden in der Stadt. Der N5-Weg ist die ganze Prüfung: beide Kana, 690 Wörter, 103 Kanji, 72 Grammatikpunkte, Hören, Lesen und ein Probetest. Du kannst jederzeit wechseln, und alles, was du auf dem einen lernst, zählt auf dem anderen.",
        "Para las dos cosas, y lo eliges en la primera pantalla. La ruta de viaje son once módulos cortos en el orden en que ocurre un viaje, desde la llegada hasta orientarse en la ciudad. La ruta N5 es el examen completo: los dos silabarios, 690 palabras, 103 kanji, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba. Puedes cambiar entre ellas en cualquier momento y todo lo que aprendes en una cuenta en la otra.",
        "Para las dos cosas, y lo eliges en la primera pantalla. La ruta de viaje son once módulos cortos en el orden en que ocurre un viaje, desde la llegada hasta ubicarse en la ciudad. La ruta N5 es el examen completo: los dos silabarios, 690 palabras, 103 kanji, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba. Puedes cambiar entre ellas en cualquier momento y todo lo que aprendes en una cuenta en la otra.",
        "Les deux, et vous choisissez sur le premier écran. Le parcours voyage, ce sont onze modules courts dans l'ordre d'un voyage, de l'arrivée jusqu'à se repérer en ville. Le parcours N5, c'est tout l'examen : les deux kana, 690 mots, 103 kanji, 72 points de grammaire, compréhension orale, lecture et un test blanc. Vous pouvez passer de l'un à l'autre à tout moment et tout ce que vous apprenez sur l'un compte sur l'autre.",
        "Entrambi, e scegli nella prima schermata. Il percorso viaggio è fatto di undici moduli brevi nell'ordine in cui si svolge un viaggio, dall'arrivo all'orientarsi in città. Il percorso N5 è l'intero esame: entrambi i kana, 690 parole, 103 kanji, 72 punti di grammatica, ascolto, lettura e un test di prova. Puoi passare dall'uno all'altro in qualsiasi momento e tutto quello che impari su uno conta sull'altro.",
        "どちらにも使え、最初の画面で選びます。旅行コースは、到着から街の中で迷わないためにまで、旅の流れにそった11の短いモジュール。N5 コースは試験の全範囲で、ひらがなとカタカナ、690語、103字の漢字、72の文法項目、聴解、読解、模擬試験です。いつでも切り替えられ、片方で学んだことはすべてもう片方でも数えられます。",
        "둘 다이고, 첫 화면에서 고릅니다. 여행 코스는 도착부터 도시에서 길 찾기까지 여행 순서 그대로 짧은 모듈 11개입니다. N5 코스는 시험 전체입니다. 두 가나, 단어 690개, 한자 103자, 문법 72개, 듣기, 독해, 모의고사. 언제든 둘 사이를 오갈 수 있고, 한쪽에서 배운 것은 전부 다른 쪽에서도 인정됩니다.",
        "Allebei, en je kiest op het eerste scherm. De reisroute bestaat uit elf korte modules in de volgorde van een reis, van aankomst tot de weg vinden in de stad. De N5-route is het hele examen: beide kana, 690 woorden, 103 kanji, 72 grammaticapunten, luisteren, lezen en een proeftoets. Je kunt op elk moment wisselen en alles wat je op de ene leert, telt op de andere.",
        "Os dois, e você escolhe na primeira tela. A trilha de viagem são onze módulos curtos na ordem em que a viagem acontece, da chegada a se achar na cidade. A trilha N5 é a prova inteira: os dois kana, 690 palavras, 103 kanji, 72 pontos de gramática, compreensão auditiva, leitura e um simulado. Você pode alternar entre elas a qualquer momento e tudo o que aprende em uma conta na outra.",
        "都可以，在第一个屏幕上选择。旅行路线是按旅行顺序排列的十一个短模块，从抵达到在城市里认路。N5 路线是完整的考试：两套假名、690个单词、103个汉字、72个语法点、听力、阅读和模拟考试。你随时可以在两条路线之间切换，在一条路线上学到的一切在另一条上都算数。"),

    "Do I need to know hiragana before I start?": (
        "Muss ich Hiragana können, bevor ich anfange?", "¿Necesito saber hiragana antes de empezar?",
        "¿Necesito saber hiragana antes de empezar?", "Faut-il connaître les hiragana avant de commencer ?",
        "Devo conoscere l'hiragana prima di iniziare?", "始める前にひらがなを知っている必要がありますか？",
        "시작하기 전에 히라가나를 알아야 하나요?", "Moet ik hiragana kennen voordat ik begin?",
        "Preciso saber hiragana antes de começar?", "开始之前需要会平假名吗？"),

    "No. Both kana come first on either path, and a short placement check lets you skip what you already know. Every word shows its reading until you no longer need it, and every kanji is introduced before it appears in a sentence.": (
        "Nein. Auf beiden Wegen kommen zuerst die beiden Kana, und ein kurzer Einstufungstest lässt dich überspringen, was du schon kannst. Jedes Wort zeigt seine Lesung, bis du sie nicht mehr brauchst, und jedes Kanji wird vorgestellt, bevor es in einem Satz auftaucht.",
        "No. En ambas rutas van primero los dos silabarios, y una breve prueba de nivel te deja saltarte lo que ya sabes. Cada palabra muestra su lectura hasta que ya no la necesitas, y cada kanji se presenta antes de aparecer en una oración.",
        "No. En ambas rutas van primero los dos silabarios, y una breve prueba de nivel te deja saltarte lo que ya sabes. Cada palabra muestra su lectura hasta que ya no la necesitas, y cada kanji se presenta antes de aparecer en una oración.",
        "Non. Sur les deux parcours, les deux kana viennent en premier, et un court test de niveau vous laisse sauter ce que vous savez déjà. Chaque mot affiche sa lecture jusqu'à ce que vous n'en ayez plus besoin, et chaque kanji est présenté avant d'apparaître dans une phrase.",
        "No. Su entrambi i percorsi vengono prima i due kana, e un breve test di livello ti lascia saltare quello che sai già. Ogni parola mostra la sua lettura finché non ti serve più, e ogni kanji viene presentato prima di comparire in una frase.",
        "いいえ。どちらのコースでも最初はひらがなとカタカナで、短いレベルチェックで知っているものは飛ばせます。どの単語も、必要なくなるまで読み方が表示され、どの漢字も文の中に出てくる前に紹介されます。",
        "아니요. 어느 코스든 두 가나가 먼저 나오고, 짧은 레벨 테스트로 이미 아는 것은 건너뛸 수 있습니다. 모든 단어는 더 이상 필요 없을 때까지 읽는 법을 보여 주고, 모든 한자는 문장에 나오기 전에 먼저 소개됩니다.",
        "Nee. Op beide routes komen eerst beide kana, en een korte niveautest laat je overslaan wat je al kent. Elk woord toont zijn uitspraak tot je die niet meer nodig hebt, en elke kanji wordt geïntroduceerd voordat hij in een zin verschijnt.",
        "Não. Nas duas trilhas os dois kana vêm primeiro, e um teste de nível rápido deixa você pular o que já sabe. Cada palavra mostra sua leitura até você não precisar mais, e cada kanji é apresentado antes de aparecer numa frase.",
        "不需要。两条路线都是先学两套假名，一次简短的水平测试可以让你跳过已经会的。每个词都会显示读音，直到你不再需要；每个汉字在出现在句子里之前都会先介绍。"),

    "Is Kippu free?": (
        "Ist Kippu kostenlos?", "¿Kippu es gratis?", "¿Kippu es gratis?", "Kippu est-il gratuit ?", "Kippu è gratis?",
        "Kippu は無料ですか？", "Kippu는 무료인가요?", "Is Kippu gratis?", "O Kippu é grátis?", "Kippu 免费吗？"),

    "It is free to start, with both kana units, the first module of each path and the travel Guide included. Kippu Plus opens every module, the three games and all seven themes, at 9.99 US dollars a month or 49.99 a year. The first week is free and you can cancel in your Apple account at any time.": (
        "Der Einstieg ist kostenlos, mit beiden Kana, dem ersten Modul jedes Wegs und dem Reise-Ratgeber. Kippu Plus öffnet jedes Modul, die drei Spiele und alle sieben Designs, für 9,99 US-Dollar im Monat oder 49,99 im Jahr. Die erste Woche ist kostenlos, und du kannst jederzeit in deinem Apple-Konto kündigen.",
        "Es gratis para empezar, con los dos silabarios, el primer módulo de cada ruta y la Guía de viaje incluidos. Kippu Plus abre todos los módulos, los tres juegos y los siete temas, por 9,99 dólares estadounidenses al mes o 49,99 al año. La primera semana es gratis y puedes cancelar en tu cuenta de Apple en cualquier momento.",
        "Es gratis para empezar, con los dos silabarios, el primer módulo de cada ruta y la Guía de viaje incluidos. Kippu Plus abre todos los módulos, los tres juegos y los siete temas, por 9.99 dólares estadounidenses al mes o 49.99 al año. La primera semana es gratis y puedes cancelar en tu cuenta de Apple en cualquier momento.",
        "Il est gratuit pour commencer, avec les deux kana, le premier module de chaque parcours et le Guide de voyage inclus. Kippu Plus ouvre tous les modules, les trois jeux et les sept thèmes, pour 9,99 dollars américains par mois ou 49,99 par an. La première semaine est offerte et vous pouvez résilier dans votre compte Apple à tout moment.",
        "È gratis per iniziare, con entrambi i kana, il primo modulo di ogni percorso e la Guida di viaggio inclusi. Kippu Plus apre tutti i moduli, i tre giochi e i sette temi, a 9,99 dollari americani al mese o 49,99 all'anno. La prima settimana è gratis e puoi disdire dal tuo account Apple in qualsiasi momento.",
        "無料で始められ、両方のかな、各コースの最初のモジュール、旅行ガイドが含まれます。Kippu Plus ですべてのモジュール、3つのゲーム、7つのテーマが開き、月額 9.99 米ドルまたは年額 49.99 米ドルです。最初の1週間は無料で、Apple アカウントからいつでも解約できます。",
        "무료로 시작할 수 있고, 두 가나, 각 코스의 첫 모듈, 여행 가이드가 포함됩니다. Kippu Plus로 모든 모듈, 세 가지 게임, 테마 7종이 열리며, 월 9.99 미국 달러 또는 연 49.99 달러입니다. 첫 일주일은 무료이고 Apple 계정에서 언제든 해지할 수 있습니다.",
        "Het is gratis om te beginnen, met beide kana, de eerste module van elke route en de reisgids inbegrepen. Kippu Plus opent elke module, de drie spellen en alle zeven thema's, voor 9,99 Amerikaanse dollar per maand of 49,99 per jaar. De eerste week is gratis en je kunt op elk moment opzeggen in je Apple-account.",
        "É grátis para começar, com os dois kana, o primeiro módulo de cada trilha e o Guia de viagem inclusos. O Kippu Plus abre todos os módulos, os três jogos e os sete temas, por 9,99 dólares americanos por mês ou 49,99 por ano. A primeira semana é grátis e você pode cancelar na sua conta Apple a qualquer momento.",
        "开始是免费的，包含两套假名、每条路线的第一个模块和旅行指南。Kippu Plus 解锁全部模块、三个游戏和全部七个主题，每月 9.99 美元或每年 49.99 美元。第一周免费，可随时在 Apple 账户里取消。"),

    "Does it work offline?": (
        "Funktioniert es offline?", "¿Funciona sin conexión?", "¿Funciona sin conexión?", "Fonctionne-t-il hors ligne ?",
        "Funziona offline?", "オフラインでも使えますか？", "오프라인에서도 되나요?", "Werkt het offline?",
        "Funciona offline?", "离线能用吗？"),

    "Yes. Every lesson, every recording and every game is on the phone. The only thing that uses the network is syncing your progress between your own devices through iCloud, and that waits until you are connected.": (
        "Ja. Jede Lektion, jede Aufnahme und jedes Spiel ist auf dem Telefon. Das Einzige, was das Netz nutzt, ist der Abgleich deines Fortschritts zwischen deinen eigenen Geräten über iCloud, und der wartet, bis du verbunden bist.",
        "Sí. Cada lección, cada grabación y cada juego están en el teléfono. Lo único que usa la red es la sincronización de tu progreso entre tus propios dispositivos a través de iCloud, y eso espera a que tengas conexión.",
        "Sí. Cada lección, cada grabación y cada juego están en el teléfono. Lo único que usa la red es la sincronización de tu progreso entre tus propios dispositivos a través de iCloud, y eso espera a que tengas conexión.",
        "Oui. Chaque leçon, chaque enregistrement et chaque jeu sont sur le téléphone. La seule chose qui utilise le réseau, c'est la synchronisation de votre progression entre vos propres appareils via iCloud, et elle attend que vous soyez connecté.",
        "Sì. Ogni lezione, ogni registrazione e ogni gioco sono sul telefono. L'unica cosa che usa la rete è la sincronizzazione dei tuoi progressi tra i tuoi dispositivi tramite iCloud, e quella aspetta finché non sei connesso.",
        "はい。すべてのレッスン、音声、ゲームが端末の中にあります。ネットワークを使うのは、iCloud を通じてあなたの端末どうしで進み具合を同期するときだけで、それも接続されるまで待ちます。",
        "네. 모든 수업, 모든 녹음, 모든 게임이 휴대폰 안에 있습니다. 네트워크를 쓰는 것은 iCloud를 통해 본인 기기들 사이에서 진행 상황을 동기화할 때뿐이고, 그것도 연결될 때까지 기다립니다.",
        "Ja. Elke les, elke opname en elk spel staat op de telefoon. Het enige dat het netwerk gebruikt, is het synchroniseren van je voortgang tussen je eigen apparaten via iCloud, en dat wacht tot je verbinding hebt.",
        "Sim. Cada lição, cada gravação e cada jogo estão no celular. A única coisa que usa a rede é a sincronização do seu progresso entre os seus próprios aparelhos pelo iCloud, e isso espera até você estar conectado.",
        "能。每一课、每段录音、每个游戏都在手机里。唯一用到网络的是通过 iCloud 在你自己的设备之间同步进度，而这会等到你联网时再进行。"),

    "Who speaks the recordings?": (
        "Wer spricht die Aufnahmen?", "¿Quién habla en las grabaciones?", "¿Quién habla en las grabaciones?",
        "Qui parle dans les enregistrements ?", "Chi parla nelle registrazioni?", "音声は誰が話していますか？",
        "녹음은 누가 말하나요?", "Wie spreekt de opnames in?", "Quem fala nas gravações?", "录音是谁读的？"),

    "A natural Japanese voice, recorded for every word, phrase and sentence in the app, slightly slower than street speed so you can hear each syllable. Staff replies use a second voice, so a conversation sounds like two people.": (
        "Eine natürliche japanische Stimme, aufgenommen für jedes Wort, jede Wendung und jeden Satz in der App, etwas langsamer als auf der Straße, damit du jede Silbe hörst. Die Antworten des Personals kommen von einer zweiten Stimme, ein Gespräch klingt also nach zwei Personen.",
        "Una voz japonesa natural, grabada para cada palabra, frase y oración de la aplicación, un poco más despacio que en la calle para que oigas cada sílaba. Las respuestas del personal usan una segunda voz, así que una conversación suena a dos personas.",
        "Una voz japonesa natural, grabada para cada palabra, frase y oración de la aplicación, un poco más despacio que en la calle para que oigas cada sílaba. Las respuestas del personal usan una segunda voz, así que una conversación suena a dos personas.",
        "Une voix japonaise naturelle, enregistrée pour chaque mot et chaque phrase de l'application, un peu plus lentement que dans la rue pour que vous entendiez chaque syllabe. Les réponses du personnel utilisent une seconde voix, une conversation sonne donc comme deux personnes.",
        "Una voce giapponese naturale, registrata per ogni parola e ogni frase dell'app, un po' più lenta della velocità di strada così senti ogni sillaba. Le risposte del personale usano una seconda voce, quindi una conversazione suona come due persone.",
        "自然な日本語の声で、アプリ内のすべての単語、フレーズ、文が録音されています。街で聞くより少しゆっくりなので、一音一音が聞き取れます。店員さんの返答は別の声なので、会話が二人のやりとりに聞こえます。",
        "자연스러운 일본어 목소리로 앱의 모든 단어, 표현, 문장이 녹음되어 있습니다. 거리에서 듣는 것보다 조금 느려서 음절 하나하나가 들립니다. 직원의 답변은 다른 목소리라서 대화가 두 사람처럼 들립니다.",
        "Een natuurlijke Japanse stem, opgenomen voor elk woord en elke zin in de app, iets langzamer dan op straat zodat je elke lettergreep hoort. Antwoorden van het personeel komen van een tweede stem, zodat een gesprek als twee mensen klinkt.",
        "Uma voz japonesa natural, gravada para cada palavra, frase e oração do app, um pouco mais devagar que na rua para você ouvir cada sílaba. As respostas do atendente usam uma segunda voz, então uma conversa soa como duas pessoas.",
        "自然的日语人声，为应用里的每个词、每个短语、每个句子录制，比街上的语速稍慢一点，每个音节都听得清。店员的回答用另一个声音，所以对话听起来像两个人。"),

    "Do I need an account?": (
        "Brauche ich ein Konto?", "¿Necesito una cuenta?", "¿Necesito una cuenta?", "Faut-il un compte ?",
        "Serve un account?", "アカウントは必要ですか？", "계정이 필요한가요?", "Heb ik een account nodig?",
        "Preciso de uma conta?", "需要账户吗？"),

    "No. There is nothing to sign up for and nothing to sign in to. Progress is kept on your phone and, if you use iCloud, in your own private iCloud database, which Apple holds and I cannot read.": (
        "Nein. Es gibt nichts zu registrieren und nichts zum Anmelden. Der Fortschritt bleibt auf deinem Telefon und, wenn du iCloud nutzt, in deiner eigenen privaten iCloud-Datenbank, die Apple verwahrt und die ich nicht lesen kann.",
        "No. No hay nada en lo que registrarse ni nada en lo que iniciar sesión. El progreso se guarda en tu teléfono y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que yo no puedo leer.",
        "No. No hay nada en lo que registrarse ni nada en lo que iniciar sesión. El progreso se guarda en tu teléfono y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que yo no puedo leer.",
        "Non. Il n'y a rien où s'inscrire et rien où se connecter. La progression est conservée sur votre téléphone et, si vous utilisez iCloud, dans votre propre base de données iCloud privée, qu'Apple héberge et que je ne peux pas lire.",
        "No. Non c'è niente a cui registrarsi e niente a cui accedere. I progressi restano sul tuo telefono e, se usi iCloud, nel tuo database iCloud privato, che Apple custodisce e che io non posso leggere.",
        "いいえ。登録するものもサインインするものもありません。進み具合は端末に保存され、iCloud を使っていればあなた自身のプライベートな iCloud データベースにも保存されます。それは Apple が保管し、私には読めません。",
        "아니요. 가입할 것도 로그인할 것도 없습니다. 진행 상황은 휴대폰에 보관되고, iCloud를 쓰면 본인의 비공개 iCloud 데이터베이스에도 저장됩니다. 그것은 Apple이 보관하며 저는 읽을 수 없습니다.",
        "Nee. Er is niets om je voor aan te melden en niets om op in te loggen. Voortgang blijft op je telefoon en, als je iCloud gebruikt, in je eigen privé-iCloud-database, die Apple bewaart en die ik niet kan lezen.",
        "Não. Não há nada para se cadastrar nem nada para entrar. O progresso fica no seu celular e, se você usa o iCloud, no seu próprio banco de dados privado do iCloud, que a Apple guarda e que eu não consigo ler.",
        "不需要。没有任何要注册或登录的东西。进度保存在你的手机上；如果你使用 iCloud，也会保存在你自己的私有 iCloud 数据库中，由 Apple 保管，我无法读取。"),

    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy", "プライバシー", "개인정보",
                "Privacy", "Privacidade", "隐私"),

    "Also here:": ("Auch hier:", "También aquí:", "También aquí:", "Aussi ici :", "Anche qui:", "こちらも：", "이곳의 다른 앱:",
                   "Ook hier:", "Também aqui:", "这里还有："),

    ", a colour mixing game for the flight over.": (
        ", ein Farbmischspiel für den Flug hin.",
        ", un juego de mezcla de colores para el vuelo de ida.",
        ", un juego de mezcla de colores para el vuelo de ida.",
        ", un jeu de mélange de couleurs pour le vol aller.",
        ", un gioco di mescolanza dei colori per il volo di andata.",
        "、行きの飛行機で遊べる色混ぜゲーム。",
        ", 가는 비행기에서 할 색 혼합 게임.",
        ", een kleurmengspel voor de heenvlucht.",
        ", um jogo de mistura de cores para o voo de ida.",
        "，一款可以在去程航班上玩的调色游戏。"),

    "Right. Next one.": ("Richtig. Nächster.", "Correcto. Siguiente.", "Correcto. Siguiente.", "Juste. Au suivant.",
                         "Giusto. Prossimo.", "正解。次へ。", "정답. 다음.", "Goed. Volgende.", "Certo. Próximo.", "对。下一个。"),
    "Not quite. It is": ("Nicht ganz. Es ist", "No exactamente. Es", "No exactamente. Es", "Pas tout à fait. C'est",
                         "Non proprio. È", "違います。正解は", "아니에요. 정답은", "Niet helemaal. Het is", "Não é isso. É", "不对。正确的是"),
    "That is every one here. The app has all 92 kana and 103 kanji.": (
        "Das waren alle hier. Die App hat alle 92 Kana und 103 Kanji.",
        "Esos eran todos los de aquí. La aplicación tiene los 92 kana y 103 kanji.",
        "Esos eran todos los de aquí. La aplicación tiene los 92 kana y 103 kanji.",
        "C'était le dernier ici. L'application a les 92 kana et 103 kanji.",
        "Erano tutti quelli qui. L'app ha tutti i 92 kana e 103 kanji.",
        "ここにあるのはこれで全部です。アプリには92のかなと103の漢字がすべてあります。",
        "여기 있는 건 이게 전부입니다. 앱에는 가나 92자와 한자 103자가 모두 있습니다.",
        "Dat waren ze hier allemaal. De app heeft alle 92 kana en 103 kanji.",
        "Esses eram todos daqui. O app tem todos os 92 kana e 103 kanji.",
        "这里的就这些了。应用里有全部92个假名和103个汉字。"),
    "right": ("richtig", "aciertos", "aciertos", "justes", "giuste", "正解", "정답", "goed", "certas", "对"),

    "Kippu: Learn Japanese": (
        "Kippu: Japanisch lernen", "Kippu: Aprende japonés", "Kippu: Aprende japonés", "Kippu : Apprendre le japonais",
        "Kippu: Impara il giapponese", "Kippu：日本語を学ぶ", "Kippu: 일본어 배우기", "Kippu: Japans leren",
        "Kippu: Aprenda japonês", "Kippu：学日语"),

    "A Japanese learning app for iPhone and iPad with two paths: the Japanese you need for a trip to Japan, and the JLPT N5. Eleven travel modules with what staff say back, fifty cards on how Japan works, both kana, 690 words, 103 kanji with stroke order, 72 grammar points, listening, reading and a mock test. Every word and sentence is spoken, short sittings bring back what you are about to forget, and three games practice what you know.": (
        "Eine App zum Japanischlernen für iPhone und iPad mit zwei Wegen: das Japanisch für die Reise nach Japan und der JLPT N5. Elf Reisemodule mit dem, was das Personal antwortet, fünfzig Karten dazu, wie Japan funktioniert, beide Kana, 690 Wörter, 103 Kanji mit Strichfolge, 72 Grammatikpunkte, Hören, Lesen und ein Probetest. Jedes Wort und jeder Satz wird gesprochen, kurze Lektionen holen zurück, was du gerade vergessen würdest, und drei Spiele üben, was du kannst.",
        "Una aplicación para aprender japonés en iPhone y iPad con dos rutas: el japonés que necesitas para un viaje a Japón y el JLPT N5. Once módulos de viaje con lo que responde el personal, cincuenta tarjetas sobre cómo funciona Japón, los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba. Cada palabra y oración se pronuncia, las sesiones cortas recuperan lo que estás a punto de olvidar y tres juegos practican lo que sabes.",
        "Una aplicación para aprender japonés en iPhone y iPad con dos rutas: el japonés que necesitas para un viaje a Japón y el JLPT N5. Once módulos de viaje con lo que contesta el personal, cincuenta tarjetas sobre cómo funciona Japón, los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba. Cada palabra y oración se pronuncia, las sesiones cortas recuperan lo que estás a punto de olvidar y tres juegos practican lo que sabes.",
        "Une application pour apprendre le japonais sur iPhone et iPad avec deux parcours : le japonais qu'il vous faut pour un voyage au Japon, et le JLPT N5. Onze modules de voyage avec ce que le personnel répond, cinquante fiches sur le fonctionnement du Japon, les deux kana, 690 mots, 103 kanji avec l'ordre des traits, 72 points de grammaire, compréhension orale, lecture et un test blanc. Chaque mot et chaque phrase est prononcé, des séances courtes ramènent ce que vous êtes sur le point d'oublier, et trois jeux font pratiquer ce que vous savez.",
        "Un'app per imparare il giapponese su iPhone e iPad con due percorsi: il giapponese che ti serve per un viaggio in Giappone e il JLPT N5. Undici moduli di viaggio con quello che risponde il personale, cinquanta schede su come funziona il Giappone, entrambi i kana, 690 parole, 103 kanji con l'ordine dei tratti, 72 punti di grammatica, ascolto, lettura e un test di prova. Ogni parola e frase viene pronunciata, sessioni brevi riportano quello che stai per dimenticare, e tre giochi esercitano quello che sai.",
        "iPhone と iPad のための日本語学習アプリ。コースはふたつ、日本を旅するための日本語と JLPT N5。店員さんの返答つきの旅行モジュール11、日本の仕組みがわかるカード50枚、ひらがなとカタカナ、690語、筆順つきの漢字103字、文法72項目、聴解、読解、模擬試験。すべての単語と文が読み上げられ、短い学習が忘れかけたものを先に戻し、3つのゲームで覚えたことを練習できます。",
        "iPhone과 iPad를 위한 일본어 학습 앱. 코스는 두 가지, 일본 여행에 필요한 일본어와 JLPT N5. 직원의 답변이 함께 나오는 여행 모듈 11개, 일본이 돌아가는 방식을 담은 카드 50장, 두 가나, 단어 690개, 필순이 있는 한자 103자, 문법 72개, 듣기, 독해, 모의고사. 모든 단어와 문장이 읽히고, 짧은 학습이 잊기 직전인 것을 먼저 되돌리며, 세 가지 게임으로 아는 것을 연습합니다.",
        "Een app om Japans te leren voor iPhone en iPad met twee routes: het Japans dat je nodig hebt voor een reis naar Japan, en het JLPT N5. Elf reismodules met wat het personeel terugzegt, vijftig kaarten over hoe Japan werkt, beide kana, 690 woorden, 103 kanji met streepvolgorde, 72 grammaticapunten, luisteren, lezen en een proeftoets. Elk woord en elke zin wordt uitgesproken, korte sessies halen terug wat je bijna vergeten bent, en drie spellen oefenen wat je kent.",
        "Um app para aprender japonês no iPhone e iPad com duas trilhas: o japonês que você precisa para uma viagem ao Japão e o JLPT N5. Onze módulos de viagem com o que o atendente responde, cinquenta cartões sobre como o Japão funciona, os dois kana, 690 palavras, 103 kanji com ordem dos traços, 72 pontos de gramática, compreensão auditiva, leitura e um simulado. Cada palavra e frase é falada, sessões curtas trazem de volta o que você está prestes a esquecer, e três jogos praticam o que você sabe.",
        "一款 iPhone 和 iPad 上的日语学习应用，有两条路线：去日本旅行要用的日语，以及 JLPT N5。十一个附有店员回答的旅行模块，五十张讲日本怎么运转的卡片，两套假名、690个单词、103个带笔顺的汉字、72个语法点、听力、阅读和模拟考试。每个词和句子都有配音，短时学习把快忘的内容先带回来，三个游戏练习你已经会的。"),

    "Eleven travel modules in the order a trip happens, each phrase with what staff say back": (
        "Elf Reisemodule in der Reihenfolge einer Reise, jeder Satz mit dem, was das Personal antwortet",
        "Once módulos de viaje en el orden en que ocurre un viaje, cada frase con lo que responde el personal",
        "Once módulos de viaje en el orden en que ocurre un viaje, cada frase con lo que contesta el personal",
        "Onze modules de voyage dans l'ordre d'un voyage, chaque phrase avec ce que le personnel répond",
        "Undici moduli di viaggio nell'ordine in cui si svolge un viaggio, ogni frase con quello che risponde il personale",
        "旅の流れにそった旅行モジュール11、どのフレーズにも店員さんの返答つき",
        "여행 순서 그대로 여행 모듈 11개, 모든 표현에 직원의 답변 포함",
        "Elf reismodules in de volgorde van een reis, elke zin met wat het personeel terugzegt",
        "Onze módulos de viagem na ordem em que a viagem acontece, cada frase com o que o atendente responde",
        "按旅行顺序排列的十一个旅行模块，每句话都附有店员的回答"),

    "Fifty know-how cards on trains, IC cards, cash, shoes, onsen etiquette and emergency numbers": (
        "Fünfzig Wissenskarten zu Zügen, IC-Karten, Bargeld, Schuhen, Onsen-Etikette und Notrufnummern",
        "Cincuenta tarjetas de saber hacer sobre trenes, tarjetas IC, efectivo, zapatos, etiqueta del onsen y números de emergencia",
        "Cincuenta tarjetas de saber hacer sobre trenes, tarjetas IC, efectivo, zapatos, etiqueta del onsen y números de emergencia",
        "Cinquante fiches savoir-faire sur les trains, les cartes IC, les espèces, les chaussures, les usages au onsen et les numéros d'urgence",
        "Cinquanta schede da sapere su treni, carte IC, contanti, scarpe, regole dell'onsen e numeri di emergenza",
        "電車、ICカード、現金、靴、温泉のマナー、緊急連絡先についての豆知識カード50枚",
        "전철, IC 카드, 현금, 신발, 온천 예절, 긴급 전화번호에 관한 알아두기 카드 50장",
        "Vijftig weetjeskaarten over treinen, IC-kaarten, contant geld, schoenen, onsen-etiquette en alarmnummers",
        "Cinquenta cartões de dicas sobre trens, cartões IC, dinheiro, sapatos, etiqueta do onsen e números de emergência",
        "五十张旅行须知卡片：电车、IC卡、现金、脱鞋、温泉礼仪和紧急电话"),

    "The JLPT N5 in twenty-two units: both kana, 690 words, 103 kanji with stroke order, 72 grammar points, listening, reading and a thirty-question mock test": (
        "Der JLPT N5 in zweiundzwanzig Einheiten: beide Kana, 690 Wörter, 103 Kanji mit Strichfolge, 72 Grammatikpunkte, Hören, Lesen und ein Probetest mit dreißig Fragen",
        "El JLPT N5 en veintidós unidades: los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba de treinta preguntas",
        "El JLPT N5 en veintidós unidades: los dos silabarios, 690 palabras, 103 kanji con orden de trazos, 72 puntos de gramática, comprensión auditiva, lectura y un examen de prueba de treinta preguntas",
        "Le JLPT N5 en vingt-deux unités : les deux kana, 690 mots, 103 kanji avec l'ordre des traits, 72 points de grammaire, compréhension orale, lecture et un test blanc de trente questions",
        "Il JLPT N5 in ventidue unità: entrambi i kana, 690 parole, 103 kanji con l'ordine dei tratti, 72 punti di grammatica, ascolto, lettura e un test di prova da trenta domande",
        "22ユニットで JLPT N5：ひらがなとカタカナ、690語、筆順つきの漢字103字、文法72項目、聴解、読解、30問の模擬試験",
        "22개 단원으로 JLPT N5: 두 가나, 단어 690개, 필순이 있는 한자 103자, 문법 72개, 듣기, 독해, 30문항 모의고사",
        "Het JLPT N5 in tweeëntwintig eenheden: beide kana, 690 woorden, 103 kanji met streepvolgorde, 72 grammaticapunten, luisteren, lezen en een proeftoets van dertig vragen",
        "O JLPT N5 em vinte e duas unidades: os dois kana, 690 palavras, 103 kanji com ordem dos traços, 72 pontos de gramática, compreensão auditiva, leitura e um simulado de trinta questões",
        "二十二个单元的 JLPT N5：两套假名、690个单词、103个带笔顺的汉字、72个语法点、听力、阅读和三十题模拟考试"),

    "Every word and sentence spoken aloud, every kanji with its reading": (
        "Jedes Wort und jeder Satz gesprochen, jedes Kanji mit seiner Lesung",
        "Cada palabra y oración pronunciada, cada kanji con su lectura",
        "Cada palabra y oración pronunciada, cada kanji con su lectura",
        "Chaque mot et chaque phrase prononcés, chaque kanji avec sa lecture",
        "Ogni parola e frase pronunciata, ogni kanji con la sua lettura",
        "すべての単語と文に音声、すべての漢字に読み方",
        "모든 단어와 문장에 음성, 모든 한자에 읽는 법",
        "Elk woord en elke zin uitgesproken, elke kanji met zijn uitspraak",
        "Cada palavra e frase falada, cada kanji com sua leitura",
        "每个词和句子都有配音，每个汉字都标注读音"),

    "Short sittings that bring back what you are about to forget first": (
        "Kurze Lektionen, die zuerst zurückholen, was du gerade vergessen würdest",
        "Sesiones cortas que recuperan primero lo que estás a punto de olvidar",
        "Sesiones cortas que recuperan primero lo que estás a punto de olvidar",
        "Des séances courtes qui ramènent d'abord ce que vous êtes sur le point d'oublier",
        "Sessioni brevi che riportano per primo quello che stai per dimenticare",
        "忘れかけたものを先に戻してくれる短い学習",
        "잊기 직전인 것을 먼저 되돌려 주는 짧은 학습",
        "Korte sessies die eerst terughalen wat je bijna vergeten bent",
        "Sessões curtas que trazem de volta primeiro o que você está prestes a esquecer",
        "把快忘的内容先带回来的短时学习"),

    "Three games: match pairs, race the clock, catch falling kanji": (
        "Drei Spiele: Paare finden, gegen die Uhr, fallende Kanji auffangen",
        "Tres juegos: emparejar, correr contra el reloj, atrapar kanji que caen",
        "Tres juegos: emparejar, correr contra el reloj, atrapar kanji que caen",
        "Trois jeux : associer des paires, courir contre la montre, attraper des kanji qui tombent",
        "Tre giochi: abbinare le coppie, correre contro il tempo, prendere i kanji che cadono",
        "3つのゲーム：ペア合わせ、タイムアタック、落ちてくる漢字を受け止める",
        "세 가지 게임: 짝 맞추기, 시간과 겨루기, 떨어지는 한자 받아내기",
        "Drie spellen: paren zoeken, racen tegen de klok, vallende kanji vangen",
        "Três jogos: combinar pares, correr contra o relógio, pegar kanji que caem",
        "三个游戏：配对、和时间赛跑、接住落下的汉字"),

    "A placement check, a streak, a level that grows with what you remember, and an optional evening reminder": (
        "Ein Einstufungstest, eine Serie, ein Level, das mit dem wächst, was du behältst, und eine optionale abendliche Erinnerung",
        "Una prueba de nivel, una racha, un nivel que crece con lo que recuerdas y un recordatorio nocturno opcional",
        "Una prueba de nivel, una racha, un nivel que crece con lo que recuerdas y un recordatorio nocturno opcional",
        "Un test de niveau, une série, un niveau qui grandit avec ce que vous retenez, et un rappel du soir en option",
        "Un test di livello, una serie, un livello che cresce con quello che ricordi e un promemoria serale facoltativo",
        "レベルチェック、連続記録、覚えた分だけ上がるレベル、任意の夜のリマインダー",
        "레벨 테스트, 연속 기록, 기억하는 만큼 올라가는 레벨, 선택할 수 있는 저녁 알림",
        "Een niveautest, een reeks, een level dat groeit met wat je onthoudt, en een optionele avondherinnering",
        "Um teste de nível, uma sequência, um nível que cresce com o que você lembra e um lembrete noturno opcional",
        "水平测试、连续打卡、随记住的内容增长的等级，以及可选的晚间提醒"),

    "Works offline, syncs through your own iCloud, in ten languages": (
        "Funktioniert offline, gleicht über dein eigenes iCloud ab, in zehn Sprachen",
        "Funciona sin conexión, se sincroniza a través de tu propio iCloud, en diez idiomas",
        "Funciona sin conexión, se sincroniza a través de tu propio iCloud, en diez idiomas",
        "Fonctionne hors ligne, se synchronise via votre propre iCloud, en dix langues",
        "Funziona offline, si sincronizza tramite il tuo iCloud, in dieci lingue",
        "オフラインで使え、あなた自身の iCloud で同期、10言語対応",
        "오프라인에서 작동, 본인의 iCloud로 동기화, 10개 언어",
        "Werkt offline, synchroniseert via je eigen iCloud, in tien talen",
        "Funciona offline, sincroniza pelo seu próprio iCloud, em dez idiomas",
        "离线可用，通过你自己的 iCloud 同步，支持十种语言"),

    "Free to start: both kana units, the first module of each path and the travel Guide. Kippu Plus opens every module, the three games and all seven themes, at 9.99 US dollars a month or 49.99 a year, with the first week free.": (
        "Kostenloser Einstieg: beide Kana, das erste Modul jedes Wegs und der Reise-Ratgeber. Kippu Plus öffnet jedes Modul, die drei Spiele und alle sieben Designs, für 9,99 US-Dollar im Monat oder 49,99 im Jahr, mit einer kostenlosen ersten Woche.",
        "Gratis para empezar: los dos silabarios, el primer módulo de cada ruta y la Guía de viaje. Kippu Plus abre todos los módulos, los tres juegos y los siete temas, por 9,99 dólares estadounidenses al mes o 49,99 al año, con la primera semana gratis.",
        "Gratis para empezar: los dos silabarios, el primer módulo de cada ruta y la Guía de viaje. Kippu Plus abre todos los módulos, los tres juegos y los siete temas, por 9.99 dólares estadounidenses al mes o 49.99 al año, con la primera semana gratis.",
        "Gratuit pour commencer : les deux kana, le premier module de chaque parcours et le Guide de voyage. Kippu Plus ouvre tous les modules, les trois jeux et les sept thèmes, pour 9,99 dollars américains par mois ou 49,99 par an, avec la première semaine offerte.",
        "Gratis per iniziare: entrambi i kana, il primo modulo di ogni percorso e la Guida di viaggio. Kippu Plus apre tutti i moduli, i tre giochi e i sette temi, a 9,99 dollari americani al mese o 49,99 all'anno, con la prima settimana gratis.",
        "無料で始められます：両方のかな、各コースの最初のモジュール、旅行ガイド。Kippu Plus ですべてのモジュール、3つのゲーム、7つのテーマが開き、月額 9.99 米ドルまたは年額 49.99 米ドル、最初の1週間は無料。",
        "무료로 시작: 두 가나, 각 코스의 첫 모듈, 여행 가이드. Kippu Plus로 모든 모듈, 세 가지 게임, 테마 7종이 열리며, 월 9.99 미국 달러 또는 연 49.99 달러, 첫 일주일은 무료.",
        "Gratis om te beginnen: beide kana, de eerste module van elke route en de reisgids. Kippu Plus opent elke module, de drie spellen en alle zeven thema's, voor 9,99 Amerikaanse dollar per maand of 49,99 per jaar, met de eerste week gratis.",
        "Grátis para começar: os dois kana, o primeiro módulo de cada trilha e o Guia de viagem. O Kippu Plus abre todos os módulos, os três jogos e os sete temas, por 9,99 dólares americanos por mês ou 49,99 por ano, com a primeira semana grátis.",
        "免费开始：两套假名、每条路线的第一个模块和旅行指南。Kippu Plus 解锁全部模块、三个游戏和全部七个主题，每月 9.99 美元或每年 49.99 美元，第一周免费。"),
}

KEEP |= {"Discord", "X", "Instagram"}  # names, the same in every language
