"""lf.wtf/cyano, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

"Cyanotype" is the searchable word and every language has its own: Cyanotypie, cianotipia,
cyanotype, サイアノタイプ, 사이아노타입, 蓝晒. The titles lead with it. So does "blueprint", which is
the word most people arrive by: Blaupause, cianotipo, blauwdruk, 蓝图.

The measured numbers stay numbers. 177 and 165 becoming 69 and 225 is the page's central claim and
the one thing a translator must never round or soften.
"""

KEEP = {
    "CYANO", "FRMT", "MODUL8", "lf.wtf", "Levi Foster", "iPhone",
}

T = {
    "CYANO: Cyanotype App for iPhone. Real Chemistry, Simulated.": (
        "CYANO: Cyanotypie-App für iPhone. Echte Chemie, simuliert.",
        "CYANO: app de cianotipia para iPhone. Química real, simulada.",
        "CYANO: app de cianotipia para iPhone. Química real, simulada.",
        "CYANO : app de cyanotype pour iPhone. De la vraie chimie, simulée.",
        "CYANO: app di cianotipia per iPhone. Chimica vera, simulata.",
        "CYANO｜iPhone 用サイアノタイプアプリ。本物の化学を、そのまま計算。",
        "CYANO｜iPhone 사이아노타입 앱. 진짜 화학을 그대로 계산합니다.",
        "CYANO: cyanotypie-app voor iPhone. Echte chemie, gesimuleerd.",
        "CYANO: app de cianotipia para iPhone. Química de verdade, simulada.",
        "CYANO｜iPhone 蓝晒应用。真实化学，如实模拟。"),
    "Turn your photos into real cyanotypes. CYANO simulates the actual chemistry of the 1842 "
    "sunprint process, not a blue filter: ultraviolet sensitivity, Prussian blue forming through "
    "Beer-Lambert, tea and tannin toning. Free on iPhone.": (
        "Mach aus deinen Fotos echte Cyanotypien. CYANO simuliert die tatsächliche Chemie des "
        "Sonnendruckverfahrens von 1842, keinen Blaufilter: Ultraviolettempfindlichkeit, "
        "Berliner Blau, das über Beer-Lambert entsteht, Tonung mit Tee und Tannin. Kostenlos "
        "auf iPhone.",
        "Convierte tus fotos en cianotipias de verdad. CYANO simula la química real del proceso "
        "de impresión al sol de 1842, no un filtro azul: sensibilidad ultravioleta, azul de "
        "Prusia formándose por Beer-Lambert, virado con té y taninos. Gratis en iPhone.",
        "Convierte tus fotos en cianotipias de verdad. CYANO simula la química real del proceso "
        "de impresión al sol de 1842, no un filtro azul: sensibilidad ultravioleta, azul de "
        "Prusia formándose por Beer-Lambert, virado con té y taninos. Gratis en iPhone.",
        "Transformez vos photos en vrais cyanotypes. CYANO simule la chimie réelle du procédé "
        "d'insolation de 1842, pas un filtre bleu : sensibilité à l'ultraviolet, bleu de Prusse "
        "formé par Beer-Lambert, virage au thé et au tanin. Gratuit sur iPhone.",
        "Trasforma le tue foto in cianotipie vere. CYANO simula la chimica reale del procedimento "
        "di stampa al sole del 1842, non un filtro blu: sensibilità all'ultravioletto, blu di "
        "Prussia formato per Beer-Lambert, viraggio con tè e tannino. Gratis su iPhone.",
        "あなたの写真を本物のサイアノタイプに。CYANO は青いフィルターではなく、1842 年の日光写真の"
        "化学そのものを計算します。紫外線への感度、ベール・ランベルト則で立ち上がるプルシアン"
        "ブルー、紅茶とタンニンによる調色。iPhone で無料。",
        "당신의 사진을 진짜 사이아노타입으로. CYANO는 파란 필터가 아니라 1842년 태양광 인화 공정의 "
        "실제 화학을 계산합니다. 자외선 감도, 베어-람베르트 법칙으로 쌓이는 프러시안 블루, 홍차와 "
        "타닌 조색. iPhone에서 무료.",
        "Maak van je foto's echte cyanotypieën. CYANO simuleert de werkelijke chemie van het "
        "zonnedrukproces uit 1842, geen blauwfilter: ultraviolette gevoeligheid, Pruisisch blauw "
        "dat via Beer-Lambert ontstaat, toning met thee en tannine. Gratis op iPhone.",
        "Transforme suas fotos em cianotipias de verdade. O CYANO simula a química real do "
        "processo de impressão ao sol de 1842, não um filtro azul: sensibilidade ultravioleta, "
        "azul da Prússia se formando por Beer-Lambert, viragem com chá e tanino. Grátis no iPhone.",
        "把你的照片变成真正的蓝晒。CYANO 模拟的是 1842 年日光晒印工艺的真实化学，而不是一层蓝色"
        "滤镜：紫外线感光度、依比尔-朗伯定律生成的普鲁士蓝、茶与单宁调色。iPhone 上免费。"),
    "CYANO: Cyanotype App for iPhone": (
        "CYANO: Cyanotypie-App für iPhone", "CYANO: app de cianotipia para iPhone",
        "CYANO: app de cianotipia para iPhone", "CYANO : app de cyanotype pour iPhone",
        "CYANO: app di cianotipia per iPhone", "CYANO｜iPhone 用サイアノタイプアプリ",
        "CYANO｜iPhone 사이아노타입 앱", "CYANO: cyanotypie-app voor iPhone",
        "CYANO: app de cianotipia para iPhone", "CYANO｜iPhone 蓝晒应用"),
    "Turn your photos into real cyanotypes. The chemistry of the 1842 sunprint process, simulated. "
    "Not a blue filter.": (
        "Mach aus deinen Fotos echte Cyanotypien. Die Chemie des Sonnendruckverfahrens von 1842, "
        "simuliert. Kein Blaufilter.",
        "Convierte tus fotos en cianotipias de verdad. La química del proceso de impresión al sol "
        "de 1842, simulada. No un filtro azul.",
        "Convierte tus fotos en cianotipias de verdad. La química del proceso de impresión al sol "
        "de 1842, simulada. No un filtro azul.",
        "Transformez vos photos en vrais cyanotypes. La chimie du procédé d'insolation de 1842, "
        "simulée. Pas un filtre bleu.",
        "Trasforma le tue foto in cianotipie vere. La chimica del procedimento di stampa al sole "
        "del 1842, simulata. Non un filtro blu.",
        "あなたの写真を本物のサイアノタイプに。1842 年の日光写真の化学を、そのまま計算します。"
        "青いフィルターではありません。",
        "당신의 사진을 진짜 사이아노타입으로. 1842년 태양광 인화 공정의 화학을 그대로 계산합니다. "
        "파란 필터가 아닙니다.",
        "Maak van je foto's echte cyanotypieën. De chemie van het zonnedrukproces uit 1842, "
        "gesimuleerd. Geen blauwfilter.",
        "Transforme suas fotos em cianotipias de verdade. A química do processo de impressão ao "
        "sol de 1842, simulada. Não é um filtro azul.",
        "把你的照片变成真正的蓝晒。1842 年日光晒印工艺的化学，如实模拟。不是蓝色滤镜。"),
    "A maple in autumn colour rendered as a cyanotype by CYANO.": (
        "Ein Ahorn in Herbstfarbe, von CYANO als Cyanotypie wiedergegeben.",
        "Un arce con color de otoño representado como cianotipia por CYANO.",
        "Un arce con color de otoño representado como cianotipia por CYANO.",
        "Un érable aux couleurs d'automne rendu en cyanotype par CYANO.",
        "Un acero nei colori d'autunno reso come cianotipia da CYANO.",
        "紅葉したカエデを CYANO がサイアノタイプとして描いたもの。",
        "단풍 든 단풍나무를 CYANO가 사이아노타입으로 그려 낸 것.",
        "Een esdoorn in herfstkleur, door CYANO weergegeven als cyanotypie.",
        "Um bordo em cor de outono representado como cianotipia pelo CYANO.",
        "一棵秋色的枫树，由 CYANO 呈现为蓝晒。"),
    "Turn your photos into real cyanotypes. The chemistry, simulated. Not a blue filter.": (
        "Mach aus deinen Fotos echte Cyanotypien. Die Chemie, simuliert. Kein Blaufilter.",
        "Convierte tus fotos en cianotipias de verdad. La química, simulada. No un filtro azul.",
        "Convierte tus fotos en cianotipias de verdad. La química, simulada. No un filtro azul.",
        "Transformez vos photos en vrais cyanotypes. La chimie, simulée. Pas un filtre bleu.",
        "Trasforma le tue foto in cianotipie vere. La chimica, simulata. Non un filtro blu.",
        "あなたの写真を本物のサイアノタイプに。化学を、そのまま計算します。青いフィルターでは"
        "ありません。",
        "당신의 사진을 진짜 사이아노타입으로. 화학을 그대로 계산합니다. 파란 필터가 아닙니다.",
        "Maak van je foto's echte cyanotypieën. De chemie, gesimuleerd. Geen blauwfilter.",
        "Transforme suas fotos em cianotipias de verdade. A química, simulada. Não é um filtro "
        "azul.",
        "把你的照片变成真正的蓝晒。化学，如实模拟。不是蓝色滤镜。"),
    "The CYANO app icon: a pale sun over a Prussian blue horizon.": (
        "Das CYANO App-Symbol: eine blasse Sonne über einem Horizont in Berliner Blau.",
        "El icono de la app CYANO: un sol pálido sobre un horizonte azul de Prusia.",
        "El icono de la app CYANO: un sol pálido sobre un horizonte azul de Prusia.",
        "L'icône de l'app CYANO : un soleil pâle au-dessus d'un horizon bleu de Prusse.",
        "L'icona dell'app CYANO: un sole pallido su un orizzonte blu di Prussia.",
        "CYANO のアプリアイコン。プルシアンブルーの水平線の上に、淡い太陽。",
        "CYANO 앱 아이콘. 프러시안 블루 수평선 위의 옅은 태양.",
        "Het CYANO-app-icoon: een bleke zon boven een Pruisisch blauwe horizon.",
        "O ícone do app CYANO: um sol pálido sobre um horizonte azul da Prússia.",
        "CYANO 应用图标：普鲁士蓝的地平线上，一轮浅色的太阳。"),
    "Cyanotype Photos": ("Cyanotypie-Fotos", "Fotos en cianotipia", "Fotos en cianotipia",
                         "Photos au cyanotype", "Foto in cianotipia", "サイアノタイプ写真",
                         "사이아노타입 사진", "Cyanotypiefoto's", "Fotos em cianotipia", "蓝晒照片"),
    "Not a blue filter.": ("Kein Blaufilter.", "No es un filtro azul.", "No es un filtro azul.",
                           "Pas un filtre bleu.", "Non un filtro blu.", "青いフィルターではない。",
                           "파란 필터가 아닙니다.", "Geen blauwfilter.", "Não é um filtro azul.",
                           "不是蓝色滤镜。"),
    "The chemistry.": ("Die Chemie.", "La química.", "La química.", "La chimie.", "La chimica.",
                       "化学そのもの。", "화학입니다.", "De chemie.", "A química.", "是化学。"),
    "A cyanotype is the oldest surviving photographic process. Paper brushed with iron salts, a\n"
    "      negative laid on top, left out in the sun. What develops is Prussian blue, washed out in "
    "plain\n      water. It is where the word blueprint comes from.": (
        "Die Cyanotypie ist das älteste noch erhaltene fotografische Verfahren. Papier, mit "
        "Eisensalzen bestrichen, ein Negativ darauf gelegt, in die Sonne gelegt. Was entsteht, ist "
        "Berliner Blau, in klarem Wasser ausgewaschen. Daher kommt das Wort Blaupause.",
        "La cianotipia es el proceso fotográfico más antiguo que sobrevive. Papel pincelado con "
        "sales de hierro, un negativo encima, dejado al sol. Lo que se revela es azul de Prusia, "
        "lavado en agua corriente. De ahí viene la palabra cianotipo.",
        "La cianotipia es el proceso fotográfico más antiguo que sobrevive. Papel pincelado con "
        "sales de hierro, un negativo encima, dejado al sol. Lo que se revela es azul de Prusia, "
        "lavado en agua corriente. De ahí viene la palabra cianotipo.",
        "Le cyanotype est le plus ancien procédé photographique encore pratiqué. Du papier "
        "badigeonné de sels de fer, un négatif posé dessus, laissé au soleil. Ce qui se développe "
        "est du bleu de Prusse, rincé à l'eau claire. C'est de là que vient le mot bleu, au sens "
        "de plan.",
        "La cianotipia è il più antico procedimento fotografico ancora in uso. Carta pennellata "
        "con sali di ferro, un negativo appoggiato sopra, lasciata al sole. Quello che si sviluppa "
        "è blu di Prussia, lavato in acqua pura. È da qui che viene la parola cianografia.",
        "サイアノタイプは、現存する最も古い写真の技法です。鉄塩を刷毛で塗った紙にネガを重ね、"
        "日なたに置く。現れるのはプルシアンブルーで、ただの水で洗い流して仕上げます。"
        "設計図を「青焼き」と呼ぶのは、ここから来ています。",
        "사이아노타입은 지금까지 살아남은 가장 오래된 사진 공정입니다. 철염을 붓으로 바른 종이 "
        "위에 네거티브를 얹고, 햇빛 아래 둡니다. 나타나는 것은 프러시안 블루이고, 맑은 물로 씻어 "
        "냅니다. 설계도를 청사진이라 부르는 것이 여기서 왔습니다.",
        "De cyanotypie is het oudste nog bestaande fotografische procedé. Papier bestreken met "
        "ijzerzouten, een negatief erop gelegd, in de zon gezet. Wat er ontstaat is Pruisisch "
        "blauw, uitgewassen in schoon water. Daar komt het woord blauwdruk vandaan.",
        "A cianotipia é o processo fotográfico mais antigo que sobreviveu. Papel pincelado com "
        "sais de ferro, um negativo posto por cima, deixado ao sol. O que se revela é azul da "
        "Prússia, lavado em água limpa. É daí que vem a palavra blueprint.",
        "蓝晒是现存最古老的摄影工艺。用铁盐刷过的纸，上面压一张底片，放到太阳底下。"
        "显出来的是普鲁士蓝，用清水冲洗即可。英文里\"蓝图\"这个词就是从这里来的。"),
    "CYANO does that chemistry in software.": (
        "CYANO rechnet diese Chemie in Software durch.",
        "CYANO hace esa química en software.", "CYANO hace esa química en software.",
        "CYANO fait cette chimie en logiciel.", "CYANO fa quella chimica via software.",
        "CYANO はその化学をソフトウェアで行います。",
        "CYANO는 그 화학을 소프트웨어로 계산합니다.", "CYANO doet die chemie in software.",
        "O CYANO faz essa química em software.", "CYANO 用软件把这套化学跑出来。"),
    "Not a colour swap tuned by eye, but\n      the sensitiser's ultraviolet response integrated "
    "against sunlight across the spectrum, and\n      Prussian blue built up through the "
    "Beer-Lambert law. No darkroom, no chemicals, no printer.": (
        "Kein nach Augenmaß eingestellter Farbtausch, sondern die Ultraviolettantwort des "
        "Sensibilisators, über das Spektrum gegen das Sonnenlicht integriert, und Berliner Blau, "
        "aufgebaut über das Beer-Lambert-Gesetz. Keine Dunkelkammer, keine Chemikalien, kein "
        "Drucker.",
        "No un cambio de color ajustado a ojo, sino la respuesta ultravioleta del sensibilizador "
        "integrada frente a la luz solar a lo largo del espectro, y azul de Prusia construido "
        "mediante la ley de Beer-Lambert. Sin cuarto oscuro, sin productos químicos, sin impresora.",
        "No un cambio de color ajustado a ojo, sino la respuesta ultravioleta del sensibilizador "
        "integrada frente a la luz solar a lo largo del espectro, y azul de Prusia construido "
        "mediante la ley de Beer-Lambert. Sin cuarto oscuro, sin químicos, sin impresora.",
        "Pas un échange de couleurs réglé à l'oeil, mais la réponse ultraviolette du "
        "sensibilisateur intégrée contre la lumière du soleil sur tout le spectre, et du bleu de "
        "Prusse construit par la loi de Beer-Lambert. Sans chambre noire, sans produits chimiques, "
        "sans imprimante.",
        "Non uno scambio di colori regolato a occhio, ma la risposta all'ultravioletto del "
        "sensibilizzante integrata contro la luce solare su tutto lo spettro, e blu di Prussia "
        "costruito con la legge di Beer-Lambert. Niente camera oscura, niente prodotti chimici, "
        "niente stampante.",
        "目分量で決めた色の置き換えではなく、増感剤の紫外線応答を太陽光のスペクトルに対して"
        "積分し、ベール・ランベルト則にしたがってプルシアンブルーを積み上げます。"
        "暗室も薬品もプリンターも要りません。",
        "눈대중으로 맞춘 색 교체가 아니라, 감광제의 자외선 응답을 태양광 스펙트럼에 대해 적분하고, "
        "베어-람베르트 법칙에 따라 프러시안 블루를 쌓아 올립니다. 암실도, 약품도, 프린터도 필요 "
        "없습니다.",
        "Geen op het oog afgestemde kleurwissel, maar de ultraviolette respons van de "
        "sensibilisator geïntegreerd tegen zonlicht over het spectrum, en Pruisisch blauw "
        "opgebouwd via de wet van Beer-Lambert. Geen donkere kamer, geen chemicaliën, geen printer.",
        "Não uma troca de cor ajustada no olho, mas a resposta ultravioleta do sensibilizador "
        "integrada contra a luz do sol ao longo do espectro, e azul da Prússia construído pela lei "
        "de Beer-Lambert. Sem câmara escura, sem produtos químicos, sem impressora.",
        "不是凭眼睛调出来的颜色替换，而是把感光剂的紫外响应在整个光谱上对太阳光积分，"
        "再依比尔-朗伯定律一层层叠出普鲁士蓝。不需要暗房、不需要药水、不需要打印机。"),
    "Coming to the App Store": (
        "Bald im App Store", "Próximamente en la App Store", "Próximamente en la App Store",
        "Bientôt sur l'App Store", "Presto sull'App Store", "まもなく App Store に登場",
        "곧 App Store에 출시", "Binnenkort in de App Store", "Em breve na App Store",
        "即将上架 App Store"),
    "Free": ("Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료", "Gratis",
             "Grátis", "免费"),
    "No subscription": ("Kein Abo", "Sin suscripción", "Sin suscripción", "Sans abonnement",
                        "Nessun abbonamento", "定額課金なし", "구독 없음", "Geen abonnement",
                        "Sem assinatura", "无订阅"),
    "No account": ("Kein Konto", "Sin cuenta", "Sin cuenta", "Sans compte", "Nessun account",
                   "アカウント不要", "계정 없음", "Geen account", "Sem conta", "无账号"),
    "Nothing leaves your phone": (
        "Nichts verlässt dein Telefon", "Nada sale de tu móvil", "Nada sale de tu celular",
        "Rien ne quitte votre téléphone", "Niente esce dal telefono", "端末の外には出ない",
        "휴대폰 밖으로 나가지 않음", "Er gaat niets van je telefoon af",
        "Nada sai do seu telefone", "什么都不会离开你的手机"),
    "Yellow flowers in front of a city skyline under a clear blue sky, as the phone photographed "
    "it.": (
        "Gelbe Blumen vor einer Stadtsilhouette unter klarem blauem Himmel, so wie das Telefon es "
        "fotografiert hat.",
        "Flores amarillas ante el perfil de una ciudad bajo un cielo azul despejado, tal como lo "
        "fotografió el móvil.",
        "Flores amarillas ante el perfil de una ciudad bajo un cielo azul despejado, tal como lo "
        "fotografió el celular.",
        "Des fleurs jaunes devant une silhouette urbaine sous un ciel bleu dégagé, telles que le "
        "téléphone les a photographiées.",
        "Fiori gialli davanti allo skyline di una città sotto un cielo azzurro limpido, come li ha "
        "fotografati il telefono.",
        "澄んだ青空の下、街のスカイラインを背にした黄色い花。スマートフォンが撮ったそのまま。",
        "맑은 파란 하늘 아래 도시 스카이라인을 배경으로 한 노란 꽃. 휴대폰이 찍은 그대로.",
        "Gele bloemen voor een stadssilhouet onder een strakblauwe lucht, zoals de telefoon het "
        "fotografeerde.",
        "Flores amarelas diante do horizonte de uma cidade sob um céu azul limpo, como o telefone "
        "fotografou.",
        "晴朗蓝天下，城市天际线前的黄色花朵，手机拍下来的样子。"),
    "The same frame as a cyanotype: the yellow flowers have gone almost black while the sky has "
    "burned out to bare paper.": (
        "Dasselbe Bild als Cyanotypie: Die gelben Blumen sind fast schwarz geworden, während der "
        "Himmel bis auf das blanke Papier ausgebrannt ist.",
        "El mismo fotograma como cianotipia: las flores amarillas han quedado casi negras "
        "mientras el cielo se ha quemado hasta el papel desnudo.",
        "El mismo cuadro como cianotipia: las flores amarillas quedaron casi negras mientras el "
        "cielo se quemó hasta el papel desnudo.",
        "La même image en cyanotype : les fleurs jaunes sont devenues presque noires tandis que le "
        "ciel a brûlé jusqu'au papier nu.",
        "Lo stesso fotogramma come cianotipia: i fiori gialli sono diventati quasi neri mentre il "
        "cielo si è bruciato fino alla carta nuda.",
        "同じ一枚をサイアノタイプにしたもの。黄色い花はほとんど黒く沈み、空は紙の地肌まで"
        "飛んでいる。",
        "같은 프레임을 사이아노타입으로 한 것. 노란 꽃은 거의 검게 가라앉고, 하늘은 종이 바탕까지 "
        "날아갔습니다.",
        "Hetzelfde beeld als cyanotypie: de gele bloemen zijn bijna zwart geworden terwijl de "
        "lucht is uitgebrand tot kaal papier.",
        "O mesmo quadro como cianotipia: as flores amarelas ficaram quase pretas enquanto o céu "
        "estourou até o papel nu.",
        "同一张画面做成蓝晒：黄色的花几乎全黑，而天空已经烧到只剩纸的本色。"),
    "Photograph": ("Foto", "Fotografía", "Fotografía", "Photographie", "Fotografia", "写真",
                   "사진", "Foto", "Fotografia", "照片"),
    "Cyanotype": ("Cyanotypie", "Cianotipia", "Cianotipia", "Cyanotype", "Cianotipia",
                  "サイアノタイプ", "사이아노타입", "Cyanotypie", "Cianotipia", "蓝晒"),
    "Same frame. Drag it.": ("Gleiches Bild. Zieh daran.", "Mismo fotograma. Arrastra.",
                             "Mismo cuadro. Arrastra.", "Même image. Faites glisser.",
                             "Stesso fotogramma. Trascina.", "同じ一枚。ドラッグしてみてください。",
                             "같은 프레임. 끌어 보세요.", "Zelfde beeld. Sleep maar.",
                             "Mesmo quadro. Arraste.", "同一张画面。拖动看看。"),
    "Why it looks like that": (
        "Warum es so aussieht", "Por qué se ve así", "Por qué se ve así",
        "Pourquoi ça ressemble à ça", "Perché viene così", "なぜそう見えるのか",
        "왜 그렇게 보이는가", "Waarom het er zo uitziet", "Por que fica assim", "为什么会是这样"),
    "The paper cannot see most of your photograph.": (
        "Das Papier kann den größten Teil deines Fotos nicht sehen.",
        "El papel no puede ver la mayor parte de tu fotografía.",
        "El papel no puede ver la mayor parte de tu fotografía.",
        "Le papier ne voit pas la plus grande partie de votre photographie.",
        "La carta non riesce a vedere gran parte della tua fotografia.",
        "この紙は、あなたの写真の大部分を見ることができません。",
        "이 종이는 당신 사진의 대부분을 보지 못합니다.",
        "Het papier kan het grootste deel van je foto niet zien.",
        "O papel não consegue ver a maior parte da sua fotografia.",
        "这种纸看不见你照片里的大部分内容。"),
    "Cyanotype paper is blind to red and green. It responds only to ultraviolet and the deepest\n"
    "      blue, which means it reads a scene at completely the wrong brightness, and that is the "
    "whole\n      point of it.": (
        "Cyanotypie-Papier ist blind für Rot und Grün. Es reagiert nur auf Ultraviolett und das "
        "tiefste Blau, liest eine Szene also mit völlig falscher Helligkeit, und genau darin "
        "besteht der Reiz.",
        "El papel de cianotipia es ciego al rojo y al verde. Solo responde al ultravioleta y al "
        "azul más profundo, lo que significa que lee una escena con un brillo completamente "
        "equivocado, y en eso consiste todo.",
        "El papel de cianotipia es ciego al rojo y al verde. Solo responde al ultravioleta y al "
        "azul más profundo, lo que significa que lee una escena con un brillo completamente "
        "equivocado, y en eso consiste todo.",
        "Le papier au cyanotype est aveugle au rouge et au vert. Il ne répond qu'à l'ultraviolet "
        "et au bleu le plus profond, ce qui veut dire qu'il lit une scène avec une luminosité "
        "complètement fausse, et c'est tout l'intérêt.",
        "La carta per cianotipia è cieca al rosso e al verde. Risponde solo all'ultravioletto e al "
        "blu più profondo, il che significa che legge una scena con una luminosità completamente "
        "sbagliata, ed è tutto lì il punto.",
        "サイアノタイプの紙は、赤と緑に対して盲目です。反応するのは紫外線といちばん深い青だけ。"
        "つまり、場面をまったく違う明るさとして読み取るわけで、それこそがこの技法の要です。",
        "사이아노타입 종이는 빨강과 초록에 눈이 멀어 있습니다. 자외선과 가장 깊은 파랑에만 "
        "반응하므로, 장면을 완전히 엉뚱한 밝기로 읽습니다. 그리고 그것이 이 공정의 핵심입니다.",
        "Cyanotypiepapier is blind voor rood en groen. Het reageert alleen op ultraviolet en het "
        "diepste blauw, wat betekent dat het een tafereel op een volkomen verkeerde helderheid "
        "leest, en dat is er juist het punt van.",
        "O papel de cianotipia é cego ao vermelho e ao verde. Ele responde só ao ultravioleta e ao "
        "azul mais profundo, o que significa que lê uma cena com um brilho completamente errado, e "
        "é justamente esse o ponto.",
        "蓝晒纸对红色和绿色是盲的。它只对紫外线和最深的蓝作出反应，也就是说，"
        "它会以完全错误的亮度来读一个场景，而这正是它的全部意义所在。"),
    "Look at the picture above. To the camera, those yellow flowers and that sky are the same\n"
    "      brightness: measure them and the flowers come out at 177, the sky at 165. You could not "
    "tell\n      them apart in a black and white conversion.": (
        "Sieh dir das Bild oben an. Für die Kamera sind diese gelben Blumen und dieser Himmel "
        "gleich hell: Miss sie nach, und die Blumen kommen auf 177, der Himmel auf 165. In einer "
        "Schwarzweißumsetzung könntest du sie nicht auseinanderhalten.",
        "Mira la imagen de arriba. Para la cámara, esas flores amarillas y ese cielo tienen el "
        "mismo brillo: mídelos y las flores salen a 177, el cielo a 165. No podrías distinguirlos "
        "en una conversión a blanco y negro.",
        "Mira la imagen de arriba. Para la cámara, esas flores amarillas y ese cielo tienen el "
        "mismo brillo: mídelos y las flores salen a 177, el cielo a 165. No podrías distinguirlos "
        "en una conversión a blanco y negro.",
        "Regardez l'image ci-dessus. Pour l'appareil, ces fleurs jaunes et ce ciel ont la même "
        "luminosité : mesurez-les et les fleurs sortent à 177, le ciel à 165. Vous ne pourriez pas "
        "les distinguer dans une conversion en noir et blanc.",
        "Guarda l'immagine qui sopra. Per la fotocamera quei fiori gialli e quel cielo hanno la "
        "stessa luminosità: misurali e i fiori escono a 177, il cielo a 165. In una conversione in "
        "bianco e nero non li distingueresti.",
        "上の写真を見てください。カメラにとって、この黄色い花とこの空は同じ明るさです。"
        "測ってみると花は 177、空は 165。白黒に変換したら見分けがつきません。",
        "위의 사진을 보세요. 카메라에게 저 노란 꽃과 저 하늘은 같은 밝기입니다. 재어 보면 꽃은 "
        "177, 하늘은 165. 흑백으로 변환하면 둘을 구별할 수 없습니다.",
        "Kijk naar de foto hierboven. Voor de camera zijn die gele bloemen en die lucht even "
        "helder: meet ze en de bloemen komen uit op 177, de lucht op 165. In een zwart-witomzetting "
        "zou je ze niet uit elkaar kunnen houden.",
        "Olhe a imagem acima. Para a câmera, aquelas flores amarelas e aquele céu têm o mesmo "
        "brilho: meça e as flores dão 177, o céu 165. Você não conseguiria distingui-los numa "
        "conversão para preto e branco.",
        "看看上面这张照片。对相机来说，那些黄花和那片天空是同样的亮度：测一下，花是 177，"
        "天空是 165。转成黑白，你根本分不出它们。"),
    "On the paper they end up at opposite ends. The flowers fall to 69 and the sky rises to 225,\n"
    "      because yellow carries almost no light this sensitiser can use while the sky is carrying "
    "more\n      than the sheet can hold. Nothing was adjusted to make that happen; it is what the "
    "chemistry\n      does.": (
        "Auf dem Papier landen sie an entgegengesetzten Enden. Die Blumen fallen auf 69 und der "
        "Himmel steigt auf 225, weil Gelb fast kein Licht trägt, das dieser Sensibilisator nutzen "
        "kann, während der Himmel mehr trägt, als das Blatt fassen kann. Dafür wurde nichts "
        "nachgeregelt; das ist es, was die Chemie tut.",
        "En el papel acaban en extremos opuestos. Las flores caen a 69 y el cielo sube a 225, "
        "porque el amarillo apenas lleva luz que este sensibilizador pueda usar mientras que el "
        "cielo lleva más de la que la hoja puede aguantar. No se ajustó nada para que pasara eso; "
        "es lo que hace la química.",
        "En el papel acaban en extremos opuestos. Las flores caen a 69 y el cielo sube a 225, "
        "porque el amarillo apenas lleva luz que este sensibilizador pueda usar mientras que el "
        "cielo lleva más de la que la hoja puede aguantar. No se ajustó nada para que pasara eso; "
        "es lo que hace la química.",
        "Sur le papier, elles se retrouvent aux extrémités opposées. Les fleurs tombent à 69 et le "
        "ciel monte à 225, parce que le jaune ne porte presque aucune lumière que ce "
        "sensibilisateur puisse utiliser, tandis que le ciel en porte plus que la feuille ne peut "
        "en retenir. Rien n'a été ajusté pour que cela arrive ; c'est ce que fait la chimie.",
        "Sulla carta finiscono agli estremi opposti. I fiori scendono a 69 e il cielo sale a 225, "
        "perché il giallo porta quasi nessuna luce che questo sensibilizzante possa usare mentre "
        "il cielo ne porta più di quanta il foglio ne regga. Non è stato regolato niente perché "
        "succedesse; è quello che fa la chimica.",
        "ところが紙の上では、二つは正反対の端に落ち着きます。花は 69 まで下がり、空は 225 まで"
        "上がる。黄色にはこの増感剤が使える光がほとんど乗っておらず、空には紙が受け止めきれない"
        "ほど乗っているからです。そうなるように何かを調整したわけではありません。"
        "化学がそうするのです。",
        "그런데 종이 위에서는 둘이 정반대 끝에 놓입니다. 꽃은 69로 떨어지고 하늘은 225로 "
        "올라갑니다. 노랑에는 이 감광제가 쓸 수 있는 빛이 거의 실려 있지 않고, 하늘에는 종이가 "
        "감당할 수 있는 것보다 많이 실려 있기 때문입니다. 그렇게 되도록 무언가를 조정한 것이 "
        "아닙니다. 화학이 그렇게 하는 것입니다.",
        "Op het papier belanden ze aan tegenovergestelde kanten. De bloemen zakken naar 69 en de "
        "lucht stijgt naar 225, omdat geel bijna geen licht draagt dat deze sensibilisator kan "
        "gebruiken terwijl de lucht er meer draagt dan het vel aankan. Er is niets bijgesteld om "
        "dat te laten gebeuren; het is wat de chemie doet.",
        "No papel eles acabam em extremos opostos. As flores caem para 69 e o céu sobe para 225, "
        "porque o amarelo quase não carrega luz que este sensibilizador consiga usar enquanto o "
        "céu carrega mais do que a folha aguenta. Nada foi ajustado para isso acontecer; é o que a "
        "química faz.",
        "可是在纸上，它们落到了两个相反的极端。花掉到 69，天空升到 225，"
        "因为黄色几乎不带这种感光剂用得上的光，而天空带的比这张纸能承受的还多。"
        "没有人为此调过任何东西；这就是化学干的事。"),
    "Two colours your camera recorded as equally bright come out at opposite ends of the print.": (
        "Zwei Farben, die deine Kamera als gleich hell aufgezeichnet hat, kommen an "
        "entgegengesetzten Enden des Drucks heraus.",
        "Dos colores que tu cámara registró igual de brillantes salen en extremos opuestos de la "
        "copia.",
        "Dos colores que tu cámara registró igual de brillantes salen en extremos opuestos de la "
        "copia.",
        "Deux couleurs que votre appareil a enregistrées aussi claires l'une que l'autre "
        "ressortent aux extrémités opposées du tirage.",
        "Due colori che la tua fotocamera ha registrato ugualmente luminosi escono agli estremi "
        "opposti della stampa.",
        "カメラが同じ明るさとして記録した二つの色が、プリントの上では正反対の端に出ます。",
        "카메라가 똑같은 밝기로 기록한 두 색이 인화지 위에서는 정반대 끝에 놓입니다.",
        "Twee kleuren die je camera even helder vastlegde komen aan tegenovergestelde kanten van "
        "de afdruk uit.",
        "Duas cores que a sua câmera registrou igualmente claras saem em extremos opostos da cópia.",
        "两种被你的相机记录为同样明亮的颜色，在成品上会落到两个相反的极端。"),
    "A filter cannot get there. A filter is a list somebody wrote down in advance, so it can make "
    "a\n      photograph blue, but it has no idea which blue was carrying ultraviolet. That is the\n"
    "      difference between something that looks vaguely antique and something that looks like it "
    "came\n      out of a tray.": (
        "Ein Filter kommt da nicht hin. Ein Filter ist eine Liste, die jemand vorab aufgeschrieben "
        "hat, er kann ein Foto also blau machen, aber er hat keine Ahnung, welches Blau "
        "Ultraviolett trug. Das ist der Unterschied zwischen etwas, das vage antik aussieht, und "
        "etwas, das aussieht, als käme es aus der Schale.",
        "Un filtro no llega ahí. Un filtro es una lista que alguien escribió de antemano, así que "
        "puede poner azul una fotografía, pero no tiene ni idea de qué azul llevaba ultravioleta. "
        "Esa es la diferencia entre algo que parece vagamente antiguo y algo que parece salido de "
        "una cubeta.",
        "Un filtro no llega ahí. Un filtro es una lista que alguien escribió de antemano, así que "
        "puede poner azul una fotografía, pero no tiene ni idea de qué azul llevaba ultravioleta. "
        "Esa es la diferencia entre algo que parece vagamente antiguo y algo que parece salido de "
        "una charola.",
        "Un filtre n'y arrive pas. Un filtre est une liste que quelqu'un a écrite à l'avance, il "
        "peut donc rendre une photographie bleue, mais il n'a aucune idée de quel bleu portait de "
        "l'ultraviolet. C'est la différence entre quelque chose qui a vaguement l'air ancien et "
        "quelque chose qui a l'air de sortir d'une cuvette.",
        "Un filtro non ci arriva. Un filtro è un elenco che qualcuno ha scritto in anticipo, "
        "quindi può rendere blu una fotografia, ma non ha idea di quale blu portasse "
        "ultravioletto. È la differenza fra qualcosa che sembra vagamente antico e qualcosa che "
        "sembra uscito da una bacinella.",
        "フィルターではそこに届きません。フィルターは誰かが前もって書き出した一覧表なので、"
        "写真を青くすることはできても、どの青が紫外線を運んでいたのかは分かりません。"
        "なんとなく古めかしく見えるものと、現像バットから上がってきたように見えるものとの違いは、"
        "そこにあります。",
        "필터로는 거기에 닿지 못합니다. 필터는 누군가 미리 적어 둔 목록이라서, 사진을 파랗게 만들 "
        "수는 있어도 어느 파랑이 자외선을 싣고 있었는지는 알지 못합니다. 어딘가 예스러워 보이는 "
        "것과 현상 트레이에서 막 건져 낸 것처럼 보이는 것의 차이가 거기에 있습니다.",
        "Een filter komt daar niet. Een filter is een lijst die iemand vooraf heeft opgeschreven, "
        "dus het kan een foto blauw maken, maar het heeft geen idee welk blauw ultraviolet "
        "meedroeg. Dat is het verschil tussen iets dat er vagelijk antiek uitziet en iets dat "
        "eruitziet alsof het uit een bak komt.",
        "Um filtro não chega lá. Um filtro é uma lista que alguém escreveu de antemão, então ele "
        "pode deixar uma fotografia azul, mas não faz ideia de qual azul carregava ultravioleta. "
        "Essa é a diferença entre algo que parece vagamente antigo e algo que parece ter saído de "
        "uma bandeja.",
        "滤镜到不了那里。滤镜是有人事先写好的一张清单，所以它可以把照片变蓝，"
        "却根本不知道哪一种蓝带着紫外线。看上去有点古旧，和看上去像刚从显影盘里捞出来，"
        "差别就在这里。"),
}

# ---------------------------------------------------------------- physics, controls, FAQ, JSON-LD
T.update({
    "What is actually being computed": (
        "Was tatsächlich gerechnet wird", "Qué se está calculando realmente",
        "Qué se está calculando realmente", "Ce qui est réellement calculé",
        "Cosa viene davvero calcolato", "実際に計算されていること",
        "실제로 계산되고 있는 것", "Wat er werkelijk berekend wordt",
        "O que está de fato sendo calculado", "实际在算的是什么"),
    "Built from the physics, not from a preset.": (
        "Aus der Physik gebaut, nicht aus einem Preset.",
        "Construido desde la física, no desde un preajuste.",
        "Construido desde la física, no desde una predefinición.",
        "Construit à partir de la physique, pas d'un préréglage.",
        "Costruito dalla fisica, non da un preset.",
        "プリセットからではなく、物理から組み上げています。",
        "프리셋이 아니라 물리에서 만들었습니다.",
        "Gebouwd op de fysica, niet op een preset.",
        "Construído a partir da física, não de uma predefinição.",
        "从物理出发构建，而不是从一个预设。"),
    "Every colour on your screen is three numbers. Those three numbers do not say how much\n"
    "      ultraviolet a thing reflected, and ultraviolet is the only part this process cares "
    "about. So\n      the model reconstructs the smoothest full spectrum consistent with the colour "
    "you photographed,\n      then reads the part of it the sensitiser can actually see.": (
        "Jede Farbe auf deinem Bildschirm sind drei Zahlen. Diese drei Zahlen sagen nicht, wie "
        "viel Ultraviolett ein Ding reflektiert hat, und Ultraviolett ist das Einzige, was dieses "
        "Verfahren interessiert. Also rekonstruiert das Modell das glatteste volle Spektrum, das "
        "mit der fotografierten Farbe verträglich ist, und liest dann den Teil davon, den der "
        "Sensibilisator tatsächlich sehen kann.",
        "Cada color de tu pantalla son tres números. Esos tres números no dicen cuánto "
        "ultravioleta reflejó una cosa, y el ultravioleta es lo único que le importa a este "
        "proceso. Así que el modelo reconstruye el espectro completo más suave compatible con el "
        "color que fotografiaste, y luego lee la parte que el sensibilizador puede ver de verdad.",
        "Cada color de tu pantalla son tres números. Esos tres números no dicen cuánto "
        "ultravioleta reflejó una cosa, y el ultravioleta es lo único que le importa a este "
        "proceso. Así que el modelo reconstruye el espectro completo más suave compatible con el "
        "color que fotografiaste, y luego lee la parte que el sensibilizador puede ver de verdad.",
        "Chaque couleur sur votre écran, ce sont trois nombres. Ces trois nombres ne disent pas "
        "combien d'ultraviolet une chose a réfléchi, et l'ultraviolet est la seule partie qui "
        "intéresse ce procédé. Le modèle reconstruit donc le spectre complet le plus lisse "
        "compatible avec la couleur photographiée, puis lit la part que le sensibilisateur voit "
        "réellement.",
        "Ogni colore sul tuo schermo sono tre numeri. Quei tre numeri non dicono quanto "
        "ultravioletto una cosa ha riflesso, e l'ultravioletto è l'unica parte che interessa a "
        "questo procedimento. Così il modello ricostruisce lo spettro completo più liscio "
        "compatibile con il colore che hai fotografato, poi legge la parte che il sensibilizzante "
        "vede davvero.",
        "画面上のどの色も、三つの数値です。その三つは、そのものが紫外線をどれだけ反射したかを"
        "教えてくれません。そしてこの技法が気にするのは紫外線だけです。そこでモデルは、"
        "撮影された色と矛盾しないもっとも滑らかな全スペクトルを復元し、そのうち増感剤が実際に"
        "見える部分だけを読みます。",
        "화면 위의 모든 색은 세 개의 숫자입니다. 그 세 숫자는 어떤 것이 자외선을 얼마나 "
        "반사했는지 말해 주지 않는데, 이 공정이 신경 쓰는 것은 오직 자외선뿐입니다. 그래서 모델은 "
        "당신이 찍은 색과 모순되지 않는 가장 매끄러운 전체 스펙트럼을 복원한 뒤, 그중 감광제가 "
        "실제로 볼 수 있는 부분을 읽습니다.",
        "Elke kleur op je scherm is drie getallen. Die drie getallen zeggen niet hoeveel "
        "ultraviolet iets weerkaatste, en ultraviolet is het enige waar dit procedé om geeft. Dus "
        "reconstrueert het model het gladste volledige spectrum dat verenigbaar is met de kleur "
        "die je fotografeerde, en leest dan het deel dat de sensibilisator werkelijk kan zien.",
        "Cada cor na sua tela são três números. Esses três números não dizem quanto ultravioleta "
        "uma coisa refletiu, e o ultravioleta é a única parte com que este processo se importa. "
        "Então o modelo reconstrói o espectro completo mais suave compatível com a cor que você "
        "fotografou, e depois lê a parte que o sensibilizador realmente enxerga.",
        "你屏幕上的每一种颜色都是三个数字。这三个数字并不告诉你某样东西反射了多少紫外线，"
        "而紫外线正是这道工艺唯一在意的部分。于是模型会重建出与你所拍颜色一致的最平滑的完整光谱，"
        "再只读取其中感光剂真正看得见的那一段。"),
    "That spectrum is integrated against the sensitiser's action curve and the solar spectrum to\n"
    "      get an exposure. The exposure runs through a tonal curve derived from the photochemistry "
    "rather\n      than drawn by hand. The resulting Prussian blue is built up by the Beer-Lambert "
    "law, including\n      the way the pigment clumps at high concentration, without which the deep "
    "tones stall at an\n      unconvincing electric blue.": (
        "Dieses Spektrum wird gegen die Wirkungskurve des Sensibilisators und das Sonnenspektrum "
        "integriert, um eine Belichtung zu erhalten. Die Belichtung läuft durch eine Tonwertkurve, "
        "die aus der Fotochemie abgeleitet und nicht von Hand gezeichnet ist. Das entstehende "
        "Berliner Blau wird über das Beer-Lambert-Gesetz aufgebaut, einschließlich der Art, wie das "
        "Pigment bei hoher Konzentration verklumpt, ohne die die tiefen Töne bei einem "
        "unglaubwürdigen Elektroblau hängen bleiben.",
        "Ese espectro se integra frente a la curva de acción del sensibilizador y el espectro "
        "solar para obtener una exposición. La exposición pasa por una curva tonal derivada de la "
        "fotoquímica en vez de dibujada a mano. El azul de Prusia resultante se construye por la "
        "ley de Beer-Lambert, incluida la forma en que el pigmento se agrega a alta concentración, "
        "sin la cual los tonos profundos se atascan en un azul eléctrico poco convincente.",
        "Ese espectro se integra frente a la curva de acción del sensibilizador y el espectro "
        "solar para obtener una exposición. La exposición pasa por una curva tonal derivada de la "
        "fotoquímica en vez de dibujada a mano. El azul de Prusia resultante se construye por la "
        "ley de Beer-Lambert, incluida la forma en que el pigmento se agrega a alta concentración, "
        "sin la cual los tonos profundos se atascan en un azul eléctrico poco convincente.",
        "Ce spectre est intégré contre la courbe d'action du sensibilisateur et le spectre solaire "
        "pour obtenir une exposition. L'exposition passe par une courbe tonale dérivée de la "
        "photochimie plutôt que tracée à la main. Le bleu de Prusse obtenu est construit par la loi "
        "de Beer-Lambert, y compris la façon dont le pigment s'agrège à forte concentration, sans "
        "quoi les tons profonds calent sur un bleu électrique peu convaincant.",
        "Quello spettro viene integrato contro la curva d'azione del sensibilizzante e lo spettro "
        "solare per ottenere un'esposizione. L'esposizione passa per una curva tonale derivata "
        "dalla fotochimica invece che disegnata a mano. Il blu di Prussia che ne risulta viene "
        "costruito con la legge di Beer-Lambert, compreso il modo in cui il pigmento si aggrega ad "
        "alta concentrazione, senza il quale i toni profondi si fermano su un blu elettrico poco "
        "convincente.",
        "そのスペクトルを、増感剤の作用曲線と太陽光スペクトルに対して積分し、露光量を得ます。"
        "露光量は、手で描いたのではなく写真化学から導いた階調曲線を通ります。生じるプルシアン"
        "ブルーはベール・ランベルト則で積み上げられ、高濃度で顔料が凝集するふるまいも含みます。"
        "これがないと、深い階調は説得力のない電気的な青で止まってしまいます。",
        "그 스펙트럼을 감광제의 작용 곡선과 태양광 스펙트럼에 대해 적분해 노광량을 얻습니다. "
        "노광량은 손으로 그린 것이 아니라 광화학에서 유도한 계조 곡선을 통과합니다. 그렇게 생긴 "
        "프러시안 블루는 베어-람베르트 법칙으로 쌓이며, 고농도에서 안료가 응집하는 방식까지 "
        "포함합니다. 그것이 없으면 깊은 계조는 설득력 없는 형광 파랑에서 멈춰 버립니다.",
        "Dat spectrum wordt geïntegreerd tegen de actiecurve van de sensibilisator en het "
        "zonnespectrum om een belichting te krijgen. De belichting loopt door een tooncurve die uit "
        "de fotochemie is afgeleid in plaats van met de hand getekend. Het ontstane Pruisisch blauw "
        "wordt opgebouwd via de wet van Beer-Lambert, inclusief de manier waarop het pigment bij "
        "hoge concentratie klontert, zonder welke de diepe tonen blijven steken op een "
        "onovertuigend elektrisch blauw.",
        "Esse espectro é integrado contra a curva de ação do sensibilizador e o espectro solar "
        "para obter uma exposição. A exposição passa por uma curva tonal derivada da fotoquímica "
        "em vez de desenhada à mão. O azul da Prússia resultante é construído pela lei de "
        "Beer-Lambert, incluindo o jeito como o pigmento se agrega em alta concentração, sem o qual "
        "os tons profundos empacam num azul elétrico pouco convincente.",
        "把这段光谱对感光剂的作用曲线和太阳光谱作积分，得到曝光量。曝光量再经过一条从光化学"
        "推导出来、而不是手工画出来的影调曲线。由此生成的普鲁士蓝依比尔-朗伯定律逐层叠加，"
        "其中也包括颜料在高浓度下聚集的方式；没有这一点，深色调就会卡在一种不可信的电光蓝上。"),
    "It also reads each photograph before printing it,": (
        "Es liest außerdem jedes Foto, bevor es gedruckt wird,",
        "También lee cada fotografía antes de imprimirla,",
        "También lee cada fotografía antes de imprimirla,",
        "Il lit aussi chaque photographie avant de la tirer,",
        "Legge inoltre ogni fotografia prima di stamparla,",
        "さらに、焼く前に一枚ごとの写真を読み取ります。",
        "또한 인화하기 전에 사진 한 장 한 장을 읽습니다.",
        "Het leest bovendien elke foto voordat het hem afdrukt,",
        "Ele também lê cada fotografia antes de imprimi-la,",
        "它还会在印之前先读一遍每一张照片，"),
    "the way a printer reads a\n      negative and makes a test strip, so the exposure suits the "
    "picture in front of it rather than\n      some imagined average one.": (
        "so wie ein Vergrößerer ein Negativ liest und einen Teststreifen macht, damit die "
        "Belichtung zu dem Bild passt, das vor ihm liegt, und nicht zu irgendeinem gedachten "
        "Durchschnittsbild.",
        "igual que un copista lee un negativo y hace una tira de prueba, para que la exposición "
        "encaje con la imagen que tiene delante y no con una media imaginaria.",
        "igual que un copista lee un negativo y hace una tira de prueba, para que la exposición "
        "encaje con la imagen que tiene delante y no con una media imaginaria.",
        "comme un tireur lit un négatif et fait une bande d'essai, pour que l'exposition convienne "
        "à l'image qu'il a devant lui plutôt qu'à une moyenne imaginaire.",
        "come uno stampatore legge un negativo e fa una striscia di prova, così l'esposizione si "
        "adatta all'immagine che ha davanti invece che a una media immaginaria.",
        "焼き付け職人がネガを読んでテストストリップをつくるのと同じで、"
        "想像上の平均的な一枚ではなく、目の前のその写真に合った露光量になります。",
        "인화 기사가 네거티브를 읽고 테스트 스트립을 만드는 것과 같아서, 상상 속의 평균적인 한 "
        "장이 아니라 눈앞의 그 사진에 맞는 노광량이 됩니다.",
        "zoals een printer een negatief leest en een teststrook maakt, zodat de belichting past bij "
        "het beeld dat voor hem ligt in plaats van bij een bedacht gemiddelde.",
        "do jeito que um copista lê um negativo e faz uma tira de teste, para que a exposição sirva "
        "à imagem que está na frente dele e não a uma média imaginada.",
        "就像放大师读一张底片、做一条试条那样，让曝光贴合眼前这张照片，而不是某张想象中的平均照片。"),
    "The controls": ("Die Regler", "Los controles", "Los controles", "Les commandes",
                     "I comandi", "操作", "조작", "De bediening", "Os controles", "控制"),
    "Four dials, and every one of them is real.": (
        "Vier Räder, und jedes davon ist echt.", "Cuatro diales, y todos son reales.",
        "Cuatro diales, y todos son reales.", "Quatre molettes, et chacune est réelle.",
        "Quattro ghiere, e ognuna è reale.", "四つのダイヤル。どれも実在の変数です。",
        "네 개의 다이얼, 그리고 모두 실제 변수입니다.", "Vier wielen, en elk ervan is echt.",
        "Quatro discos, e todos eles são reais.", "四个拨盘，每一个都是真实的变量。"),
    "Sun": ("Sonne", "Sol", "Sol", "Soleil", "Sole", "日光", "햇빛", "Zon", "Sol", "日照"),
    "How long the sheet was left out. Overexpose it and the shadows merge into one mass, the way "
    "they really do.": (
        "Wie lange das Blatt draußen lag. Überbelichte es, und die Schatten laufen zu einer Masse "
        "zusammen, so wie sie es wirklich tun.",
        "Cuánto tiempo estuvo la hoja al sol. Sobreexponla y las sombras se funden en una sola "
        "masa, como ocurre de verdad.",
        "Cuánto tiempo estuvo la hoja al sol. Sobreexponla y las sombras se funden en una sola "
        "masa, como ocurre de verdad.",
        "Combien de temps la feuille est restée dehors. Surexposez-la et les ombres fusionnent en "
        "une seule masse, comme dans la réalité.",
        "Quanto è rimasto fuori il foglio. Sovraesponilo e le ombre si fondono in un'unica massa, "
        "come succede davvero.",
        "その紙をどれだけ日にさらしたか。露光しすぎれば、影はひとかたまりに溶け合います。"
        "実際にそうなるのと同じように。",
        "그 종이를 얼마나 오래 햇빛에 두었는지. 과다 노광하면 그림자들이 한 덩어리로 뭉칩니다. "
        "실제로 그렇게 되듯이.",
        "Hoe lang het vel buiten heeft gelegen. Overbelicht het en de schaduwen smelten samen tot "
        "één massa, zoals ze echt doen.",
        "Quanto tempo a folha ficou exposta. Superexponha e as sombras se fundem numa massa só, do "
        "jeito que acontece de verdade.",
        "这张纸在太阳底下放了多久。曝光过头，暗部就会糊成一整块，真实情况正是如此。"),
    "Paper": ("Papier", "Papel", "Papel", "Papier", "Carta", "紙", "종이", "Papier", "Papel",
              "纸"),
    "Cotton rag, rough watercolour, or buff. The base colour shows through everywhere, because in "
    "this process the paper is part of the picture.": (
        "Baumwolllumpen, raues Aquarellpapier oder Chamois. Die Grundfarbe scheint überall durch, "
        "denn in diesem Verfahren ist das Papier Teil des Bildes.",
        "Trapo de algodón, acuarela rugosa o crema. El color del soporte se transparenta por todas "
        "partes, porque en este proceso el papel forma parte de la imagen.",
        "Trapo de algodón, acuarela rugosa o crema. El color del soporte se transparenta por todas "
        "partes, porque en este proceso el papel forma parte de la imagen.",
        "Chiffon de coton, aquarelle grain torchon, ou chamois. La couleur du support transparaît "
        "partout, parce que dans ce procédé le papier fait partie de l'image.",
        "Straccio di cotone, acquerello ruvido, o avorio. Il colore del supporto traspare "
        "ovunque, perché in questo procedimento la carta fa parte dell'immagine.",
        "コットンラグ、粗目の水彩紙、あるいはバフ。この技法では紙が絵の一部なので、"
        "地の色がどこにでも透けて出ます。",
        "코튼 래그, 거친 수채화지, 또는 버프. 이 공정에서는 종이가 그림의 일부이기 때문에, 바탕색이 "
        "어디에서나 비쳐 나옵니다.",
        "Katoenlompen, ruw aquarelpapier of gebroken wit. De basiskleur schijnt overal door, want "
        "in dit procedé is het papier onderdeel van het beeld.",
        "Trapo de algodão, aquarela rugosa ou creme. A cor do suporte aparece por toda parte, "
        "porque neste processo o papel faz parte da imagem.",
        "棉浆纸、粗纹水彩纸，或米色纸。纸的底色处处透出来，因为在这道工艺里，纸本身就是画面的一部分。"),
    "Toning": ("Tonung", "Virado", "Virado", "Virage", "Viraggio", "調色", "조색", "Toning",
               "Viragem", "调色"),
    "Tea, tannin or red wine. These convert the Prussian blue into iron tannate rather than "
    "tinting it, which is why a toned print reads as another process instead of a recoloured one.": (
        "Tee, Tannin oder Rotwein. Diese wandeln das Berliner Blau in Eisentannat um, statt es "
        "einzufärben, und darum liest sich ein getonter Druck als anderes Verfahren und nicht als "
        "umgefärbtes.",
        "Té, taninos o vino tinto. Estos convierten el azul de Prusia en tanato de hierro en vez "
        "de teñirlo, y por eso una copia virada se lee como otro proceso y no como una recoloreada.",
        "Té, taninos o vino tinto. Estos convierten el azul de Prusia en tanato de hierro en vez "
        "de teñirlo, y por eso una copia virada se lee como otro proceso y no como una recoloreada.",
        "Thé, tanin ou vin rouge. Ils convertissent le bleu de Prusse en tannate de fer au lieu de "
        "le teinter, et c'est pourquoi un tirage viré se lit comme un autre procédé et non comme "
        "un tirage recoloré.",
        "Tè, tannino o vino rosso. Convertono il blu di Prussia in tannato di ferro invece di "
        "tingerlo, ed è per questo che una stampa virata si legge come un altro procedimento e non "
        "come una ricolorata.",
        "紅茶、タンニン、赤ワイン。これらはプルシアンブルーを染めるのではなく、"
        "タンニン酸鉄へと変えてしまいます。だから調色したプリントは、色を塗り替えたものではなく、"
        "別の技法として見えるのです。",
        "홍차, 타닌, 또는 레드 와인. 이것들은 프러시안 블루를 물들이는 것이 아니라 타닌산철로 "
        "바꿔 버립니다. 그래서 조색한 인화지는 색을 다시 칠한 것이 아니라 다른 공정으로 읽힙니다.",
        "Thee, tannine of rode wijn. Die zetten het Pruisisch blauw om in ijzertannaat in plaats "
        "van het te kleuren, en daarom leest een getoonde afdruk als een ander procedé en niet als "
        "een verkleurde.",
        "Chá, tanino ou vinho tinto. Eles convertem o azul da Prússia em tanato de ferro em vez de "
        "tingi-lo, e é por isso que uma cópia virada se lê como outro processo e não como uma "
        "recolorida.",
        "茶、单宁或红酒。它们不是给普鲁士蓝上色，而是把它转化成单宁酸铁，"
        "所以调过色的成品读起来像是另一种工艺，而不是被重新染过色的。"),
    "Brushed edge": ("Pinselrand", "Borde pincelado", "Borde pincelado", "Bord au pinceau",
                     "Bordo pennellato", "刷毛の縁", "붓 자국 가장자리", "Kwastrand",
                     "Borda pincelada", "刷痕边缘"),
    "The uneven coating of a hand-brushed sheet, seeded per photograph, so two prints of the same "
    "picture are never quite the same.": (
        "Der ungleichmäßige Auftrag eines von Hand bestrichenen Blattes, pro Foto eigens erzeugt, "
        "damit zwei Abzüge desselben Bildes nie ganz gleich sind.",
        "El recubrimiento desigual de una hoja pincelada a mano, con una semilla por fotografía, "
        "para que dos copias de la misma imagen nunca sean del todo iguales.",
        "El recubrimiento desigual de una hoja pincelada a mano, con una semilla por fotografía, "
        "para que dos copias de la misma imagen nunca sean del todo iguales.",
        "L'enduction irrégulière d'une feuille badigeonnée à la main, tirée au sort par "
        "photographie, pour que deux tirages de la même image ne soient jamais tout à fait les "
        "mêmes.",
        "La stesura irregolare di un foglio pennellato a mano, con un seme per fotografia, perché "
        "due stampe della stessa immagine non siano mai del tutto uguali.",
        "手で刷毛塗りした紙のむらのある塗り。写真ごとに種を変えているので、"
        "同じ絵を二枚焼いてもまったく同じにはなりません。",
        "손으로 붓칠한 종이의 고르지 않은 도포. 사진마다 시드를 달리해서, 같은 그림을 두 장 "
        "인화해도 완전히 같지는 않습니다.",
        "De ongelijkmatige coating van een met de hand bestreken vel, per foto anders, zodat twee "
        "afdrukken van hetzelfde beeld nooit helemaal hetzelfde zijn.",
        "A camada irregular de uma folha pincelada à mão, com semente por fotografia, para que "
        "duas cópias da mesma imagem nunca sejam exatamente iguais.",
        "手工刷涂的纸面留下的不均匀涂层，按每张照片取不同的随机种子，"
        "所以同一张画面印两次，永远不会完全一样。"),
    "On your phone": ("Auf deinem Telefon", "En tu móvil", "En tu celular",
                      "Sur votre téléphone", "Sul tuo telefono", "あなたの端末で",
                      "당신의 휴대폰에서", "Op je telefoon", "No seu telefone", "在你的手机上"),
    "Simple in front, heavy underneath.": (
        "Vorn einfach, darunter schwer.", "Sencillo por delante, pesado por debajo.",
        "Sencillo por delante, pesado por debajo.", "Simple devant, lourd dessous.",
        "Semplice davanti, pesante sotto.", "表は簡単、裏は重い。",
        "겉은 단순하고, 속은 무겁습니다.", "Simpel vanvoren, zwaar eronder.",
        "Simples na frente, pesado por baixo.", "前台简单，底下很重。"),
    "A maple in full autumn colour rendered as a cyanotype in the CYANO app.": (
        "Ein Ahorn in voller Herbstfarbe, in der App CYANO als Cyanotypie wiedergegeben.",
        "Un arce en pleno color de otoño representado como cianotipia en la app CYANO.",
        "Un arce en pleno color de otoño representado como cianotipia en la app CYANO.",
        "Un érable en pleines couleurs d'automne rendu en cyanotype dans l'app CYANO.",
        "Un acero in pieno colore autunnale reso come cianotipia nell'app CYANO.",
        "紅葉の盛りのカエデを、CYANO アプリでサイアノタイプにしたもの。",
        "한창 단풍이 든 단풍나무를 CYANO 앱에서 사이아노타입으로 만든 것.",
        "Een esdoorn in volle herfstkleur, in de CYANO-app weergegeven als cyanotypie.",
        "Um bordo em plena cor de outono representado como cianotipia no app CYANO.",
        "秋色正浓的枫树，在 CYANO 应用中呈现为蓝晒。"),
    "Six colours a camera records as equally bright, and what cyanotype paper does to each of "
    "them.": (
        "Sechs Farben, die eine Kamera als gleich hell aufzeichnet, und was Cyanotypie-Papier mit "
        "jeder davon macht.",
        "Seis colores que una cámara registra igual de brillantes, y lo que el papel de cianotipia "
        "hace con cada uno.",
        "Seis colores que una cámara registra igual de brillantes, y lo que el papel de cianotipia "
        "hace con cada uno.",
        "Six couleurs qu'un appareil enregistre aussi claires les unes que les autres, et ce que "
        "le papier au cyanotype fait de chacune.",
        "Sei colori che una fotocamera registra ugualmente luminosi, e cosa ne fa la carta per "
        "cianotipia.",
        "カメラが同じ明るさとして記録する六つの色と、サイアノタイプの紙がそれぞれに対して"
        "することの違い。",
        "카메라가 똑같은 밝기로 기록하는 여섯 가지 색과, 사이아노타입 종이가 각각에 하는 일.",
        "Zes kleuren die een camera even helder vastlegt, en wat cyanotypiepapier met elk ervan "
        "doet.",
        "Seis cores que uma câmera registra igualmente claras, e o que o papel de cianotipia faz "
        "com cada uma.",
        "六种被相机记录为同样明亮的颜色，以及蓝晒纸对它们各自做了什么。"),
    "A photograph beside its cyanotype, showing yellow going black and sky going to paper.": (
        "Ein Foto neben seiner Cyanotypie, das zeigt, wie Gelb schwarz wird und Himmel zu Papier.",
        "Una fotografía junto a su cianotipia, mostrando el amarillo yéndose a negro y el cielo al "
        "papel.",
        "Una fotografía junto a su cianotipia, mostrando el amarillo yéndose a negro y el cielo al "
        "papel.",
        "Une photographie à côté de son cyanotype, montrant le jaune virer au noir et le ciel au "
        "papier.",
        "Una fotografia accanto alla sua cianotipia, che mostra il giallo andare al nero e il "
        "cielo alla carta.",
        "写真とそのサイアノタイプを並べたもの。黄が黒へ、空が紙の地肌へと向かうのが分かる。",
        "사진과 그 사이아노타입을 나란히 둔 것. 노랑이 검정으로, 하늘이 종이 바탕으로 가는 것이 "
        "보입니다.",
        "Een foto naast zijn cyanotypie, waarop geel naar zwart gaat en de lucht naar papier.",
        "Uma fotografia ao lado da sua cianotipia, mostrando o amarelo indo para preto e o céu "
        "indo para o papel.",
        "一张照片和它的蓝晒并排：可以看到黄色走向黑，天空走向纸的本色。"),
    "One water lily print shown untoned and then toned with tea, tannin and wine.": (
        "Ein Seerosendruck, ungetont gezeigt und dann mit Tee, Tannin und Wein getont.",
        "Una copia de un nenúfar mostrada sin virar y luego virada con té, taninos y vino.",
        "Una copia de un nenúfar mostrada sin virar y luego virada con té, taninos y vino.",
        "Un tirage de nénuphar montré non viré puis viré au thé, au tanin et au vin.",
        "Una stampa di ninfea mostrata non virata e poi virata con tè, tannino e vino.",
        "睡蓮のプリントを、調色前と、紅茶・タンニン・ワインで調色した後で並べたもの。",
        "수련 인화지를 조색 전과 홍차, 타닌, 와인으로 조색한 뒤로 나란히 보여 준 것.",
        "Een afdruk van een waterlelie, ongetoond en daarna getoond met thee, tannine en wijn.",
        "Uma cópia de nenúfar mostrada sem viragem e depois virada com chá, tanino e vinho.",
        "同一张睡莲成品，先是未调色，再分别用茶、单宁和红酒调色。"),
    "The paper picker in CYANO, showing cotton rag, rough watercolour and buff.": (
        "Die Papierauswahl in CYANO mit Baumwolllumpen, rauem Aquarellpapier und Chamois.",
        "El selector de papel en CYANO, con trapo de algodón, acuarela rugosa y crema.",
        "El selector de papel en CYANO, con trapo de algodón, acuarela rugosa y crema.",
        "Le sélecteur de papier dans CYANO, avec chiffon de coton, aquarelle grain torchon et "
        "chamois.",
        "Il selettore della carta in CYANO, con straccio di cotone, acquerello ruvido e avorio.",
        "CYANO の紙の選択画面。コットンラグ、粗目の水彩紙、バフ。",
        "CYANO의 종이 선택 화면. 코튼 래그, 거친 수채화지, 버프.",
        "De papierkiezer in CYANO, met katoenlompen, ruw aquarelpapier en gebroken wit.",
        "O seletor de papel no CYANO, com trapo de algodão, aquarela rugosa e creme.",
        "CYANO 中的选纸界面：棉浆纸、粗纹水彩纸和米色纸。"),
    "A hand-coated brushed edge around a cyanotype print in CYANO.": (
        "Ein von Hand aufgetragener Pinselrand um einen Cyanotypie-Druck in CYANO.",
        "Un borde pincelado a mano alrededor de una copia en cianotipia en CYANO.",
        "Un borde pincelado a mano alrededor de una copia en cianotipia en CYANO.",
        "Un bord au pinceau appliqué à la main autour d'un tirage au cyanotype dans CYANO.",
        "Un bordo pennellato a mano attorno a una stampa in cianotipia in CYANO.",
        "CYANO のサイアノタイプ・プリントを囲む、手塗りの刷毛の縁。",
        "CYANO의 사이아노타입 인화지를 둘러싼, 손으로 칠한 붓 자국 가장자리.",
        "Een met de hand aangebrachte kwastrand rond een cyanotypieafdruk in CYANO.",
        "Uma borda pincelada à mão em volta de uma cópia em cianotipia no CYANO.",
        "CYANO 中一张蓝晒成品周围手工涂布的刷痕边缘。"),
    "Choose a photograph and it develops. Move the sun, change the paper, drop it in a toning "
    "bath.\n      Save at full resolution with nothing stamped on it.": (
        "Wähle ein Foto, und es wird entwickelt. Verschiebe die Sonne, wechsle das Papier, leg es "
        "in ein Tonbad. Sichere in voller Auflösung, ohne dass etwas daraufgestempelt wird.",
        "Elige una fotografía y se revela. Mueve el sol, cambia el papel, métela en un baño de "
        "virado. Guarda a resolución completa sin nada estampado encima.",
        "Elige una fotografía y se revela. Mueve el sol, cambia el papel, métela en un baño de "
        "virado. Guarda a resolución completa sin nada estampado encima.",
        "Choisissez une photographie et elle se développe. Déplacez le soleil, changez de papier, "
        "plongez-la dans un bain de virage. Enregistrez en pleine résolution, sans rien "
        "d'estampillé dessus.",
        "Scegli una fotografia e si sviluppa. Sposta il sole, cambia la carta, mettila in un bagno "
        "di viraggio. Salva a piena risoluzione senza niente stampato sopra.",
        "写真を選べば、現像が始まります。日光を動かし、紙を替え、調色浴に沈める。"
        "何も刻印されないまま、フル解像度で保存できます。",
        "사진을 고르면 현상이 시작됩니다. 햇빛을 옮기고, 종이를 바꾸고, 조색액에 담그세요. 아무것도 "
        "찍히지 않은 채 원본 해상도로 저장됩니다.",
        "Kies een foto en hij ontwikkelt. Verschuif de zon, wissel het papier, laat hem in een "
        "toningbad zakken. Bewaar op volle resolutie zonder dat er iets op gestempeld staat.",
        "Escolha uma fotografia e ela revela. Mova o sol, troque o papel, mergulhe num banho de "
        "viragem. Salve em resolução total sem nada carimbado em cima.",
        "选一张照片，它就开始显影。移动太阳、更换纸张、把它放进调色液里。以完整分辨率保存，"
        "上面什么都不会盖。"),
    "Common questions": ("Häufige Fragen", "Preguntas frecuentes", "Preguntas frecuentes",
                         "Questions fréquentes", "Domande frequenti", "よくある質問",
                         "자주 묻는 질문", "Veelgestelde vragen", "Perguntas frequentes",
                         "常见问题"),
    "Questions": ("Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "質問", "질문",
                  "Vragen", "Perguntas", "问题"),
    "Do I need chemicals, paper or a printer?": (
        "Brauche ich Chemikalien, Papier oder einen Drucker?",
        "¿Necesito productos químicos, papel o una impresora?",
        "¿Necesito químicos, papel o una impresora?",
        "Ai-je besoin de produits chimiques, de papier ou d'une imprimante ?",
        "Servono prodotti chimici, carta o una stampante?",
        "薬品や紙、プリンターは必要ですか。",
        "약품이나 종이, 프린터가 필요한가요?",
        "Heb ik chemicaliën, papier of een printer nodig?",
        "Preciso de produtos químicos, papel ou impressora?",
        "我需要药水、纸或者打印机吗？"),
    "None of them. CYANO exists so that people who could never set up a darkroom, buy sensitiser "
    "or\n      wait for a sunny afternoon can still make cyanotypes.": (
        "Nichts davon. CYANO gibt es, damit auch Leute Cyanotypien machen können, die nie eine "
        "Dunkelkammer einrichten, Sensibilisator kaufen oder auf einen sonnigen Nachmittag warten "
        "könnten.",
        "Ninguno. CYANO existe para que quienes nunca podrían montar un cuarto oscuro, comprar "
        "sensibilizador o esperar una tarde soleada puedan hacer cianotipias igualmente.",
        "Ninguno. CYANO existe para que quienes nunca podrían montar un cuarto oscuro, comprar "
        "sensibilizador o esperar una tarde soleada puedan hacer cianotipias igualmente.",
        "Aucun. CYANO existe pour que ceux qui ne pourraient jamais monter une chambre noire, "
        "acheter du sensibilisateur ou attendre un après-midi ensoleillé puissent quand même faire "
        "des cyanotypes.",
        "Nessuno. CYANO esiste perché anche chi non potrebbe mai allestire una camera oscura, "
        "comprare il sensibilizzante o aspettare un pomeriggio di sole possa comunque fare "
        "cianotipie.",
        "どれも要りません。暗室を用意することも、増感剤を買うことも、よく晴れた午後を待つことも"
        "できない人が、それでもサイアノタイプをつくれるように、CYANO はあります。",
        "아무것도 필요 없습니다. 암실을 차릴 수도, 감광제를 살 수도, 화창한 오후를 기다릴 수도 없는 "
        "사람도 사이아노타입을 만들 수 있도록 CYANO가 있습니다.",
        "Geen ervan. CYANO bestaat zodat mensen die nooit een donkere kamer konden inrichten, "
        "sensibilisator konden kopen of op een zonnige middag konden wachten, tóch cyanotypieën "
        "kunnen maken.",
        "Nenhum deles. O CYANO existe para que quem nunca poderia montar uma câmara escura, comprar "
        "sensibilizador ou esperar uma tarde de sol consiga fazer cianotipias mesmo assim.",
        "都不需要。CYANO 的存在，是为了让那些永远也没法搭一间暗房、买感光剂、"
        "或者等一个晴朗下午的人，照样能做出蓝晒。"),
    "Is this a filter?": ("Ist das ein Filter?", "¿Esto es un filtro?", "¿Esto es un filtro?",
                          "Est-ce un filtre ?", "È un filtro?", "これはフィルターですか。",
                          "이건 필터인가요?", "Is dit een filter?", "Isto é um filtro?",
                          "这是滤镜吗？"),
    "No. A filter decides in advance what each colour becomes. CYANO works out how much "
    "ultraviolet\n      each colour was actually carrying and builds the pigment from that.": (
        "Nein. Ein Filter entscheidet vorab, was aus jeder Farbe wird. CYANO rechnet aus, wie viel "
        "Ultraviolett jede Farbe tatsächlich trug, und baut daraus das Pigment auf.",
        "No. Un filtro decide de antemano en qué se convierte cada color. CYANO calcula cuánto "
        "ultravioleta llevaba realmente cada color y construye el pigmento a partir de eso.",
        "No. Un filtro decide de antemano en qué se convierte cada color. CYANO calcula cuánto "
        "ultravioleta llevaba realmente cada color y construye el pigmento a partir de eso.",
        "Non. Un filtre décide à l'avance ce que devient chaque couleur. CYANO calcule combien "
        "d'ultraviolet chaque couleur portait réellement et construit le pigment à partir de là.",
        "No. Un filtro decide in anticipo cosa diventa ogni colore. CYANO calcola quanto "
        "ultravioletto portava davvero ogni colore e da lì costruisce il pigmento.",
        "いいえ。フィルターは、どの色が何になるかを前もって決めます。CYANO は、それぞれの色が"
        "実際にどれだけ紫外線を運んでいたかを計算し、そこから顔料を積み上げます。",
        "아니요. 필터는 어떤 색이 무엇이 될지 미리 정합니다. CYANO는 각 색이 실제로 자외선을 얼마나 "
        "싣고 있었는지를 계산하고, 거기서부터 안료를 쌓아 올립니다.",
        "Nee. Een filter beslist vooraf wat elke kleur wordt. CYANO rekent uit hoeveel ultraviolet "
        "elke kleur werkelijk meedroeg en bouwt het pigment daaruit op.",
        "Não. Um filtro decide de antemão no que cada cor vira. O CYANO calcula quanto ultravioleta "
        "cada cor realmente carregava e constrói o pigmento a partir disso.",
        "不是。滤镜会事先决定每种颜色变成什么。CYANO 会算出每种颜色实际带了多少紫外线，"
        "再由此把颜料一层层叠出来。"),
    "What does it cost?": ("Was kostet es?", "¿Cuánto cuesta?", "¿Cuánto cuesta?",
                           "Combien ça coûte ?", "Quanto costa?", "いくらですか。", "얼마인가요?",
                           "Wat kost het?", "Quanto custa?", "多少钱？"),
    "The app is free and completely usable: unlimited prints, full resolution, no watermark. One\n"
    "      optional purchase of $4.99 unlocks the three toning baths, the other two papers and the "
    "second\n      sensitiser formula. There is no subscription.": (
        "Die App ist kostenlos und vollständig nutzbar: unbegrenzt Abzüge, volle Auflösung, kein "
        "Wasserzeichen. Ein optionaler Kauf für 4,99 $ schaltet die drei Tonbäder, die anderen "
        "beiden Papiere und die zweite Sensibilisatorformel frei. Es gibt kein Abo.",
        "La app es gratuita y completamente usable: copias ilimitadas, resolución completa, sin "
        "marca de agua. Una compra opcional de 4,99 $ desbloquea los tres baños de virado, los "
        "otros dos papeles y la segunda fórmula de sensibilizador. No hay suscripción.",
        "La app es gratuita y completamente usable: copias ilimitadas, resolución completa, sin "
        "marca de agua. Una compra opcional de 4,99 $ desbloquea los tres baños de virado, los "
        "otros dos papeles y la segunda fórmula de sensibilizador. No hay suscripción.",
        "L'app est gratuite et pleinement utilisable : tirages illimités, pleine résolution, sans "
        "filigrane. Un achat facultatif de 4,99 $ débloque les trois bains de virage, les deux "
        "autres papiers et la seconde formule de sensibilisateur. Il n'y a pas d'abonnement.",
        "L'app è gratuita e pienamente utilizzabile: stampe illimitate, piena risoluzione, nessuna "
        "filigrana. Un acquisto facoltativo da 4,99 $ sblocca i tre bagni di viraggio, le altre "
        "due carte e la seconda formula di sensibilizzante. Non c'è abbonamento.",
        "アプリは無料で、そのまま完全に使えます。プリント数は無制限、フル解像度、透かしなし。"
        "任意の 4.99 ドルの購入で、三つの調色浴、残り二種の紙、二つめの増感剤処方が使えるように"
        "なります。定額課金はありません。",
        "앱은 무료이고 그대로 온전히 쓸 수 있습니다. 인화 무제한, 원본 해상도, 워터마크 없음. "
        "선택 구매 4.99달러로 세 가지 조색액, 나머지 두 종류의 종이, 두 번째 감광제 조성이 "
        "열립니다. 구독은 없습니다.",
        "De app is gratis en volledig bruikbaar: onbeperkt afdrukken, volle resolutie, geen "
        "watermerk. Eén optionele aankoop van $4,99 ontgrendelt de drie toningbaden, de andere "
        "twee papieren en de tweede sensibilisatorformule. Er is geen abonnement.",
        "O app é grátis e totalmente utilizável: cópias ilimitadas, resolução total, sem marca "
        "d'água. Uma compra opcional de US$ 4,99 libera os três banhos de viragem, os outros dois "
        "papéis e a segunda fórmula de sensibilizador. Não há assinatura.",
        "这个应用是免费的，而且完全可用：无限张数、完整分辨率、没有水印。"
        "一次可选的 4.99 美元购买会解锁三种调色液、另外两种纸，以及第二种感光剂配方。没有订阅。"),
    "Does it collect anything?": (
        "Sammelt es irgendetwas?", "¿Recoge algo?", "¿Recoge algo?",
        "Est-ce qu'elle collecte quoi que ce soit ?", "Raccoglie qualcosa?",
        "何かを収集しますか。", "무언가를 수집하나요?", "Verzamelt het iets?",
        "Ele coleta alguma coisa?", "它会收集什么吗？"),
    "No. No account, no analytics, no server, and no networking code of its own. Photographs never\n"
    "      leave your phone. The": (
        "Nein. Kein Konto, keine Analyse, kein Server und kein eigener Netzwerkcode. Fotos "
        "verlassen dein Telefon nie. Die",
        "No. Sin cuenta, sin analíticas, sin servidor y sin código de red propio. Las fotografías "
        "nunca salen de tu móvil. La",
        "No. Sin cuenta, sin analíticas, sin servidor y sin código de red propio. Las fotografías "
        "nunca salen de tu celular. La",
        "Non. Pas de compte, pas d'analytique, pas de serveur, et aucun code réseau propre. Les "
        "photographies ne quittent jamais votre téléphone. La",
        "No. Nessun account, nessuna analisi, nessun server e nessun codice di rete proprio. Le "
        "fotografie non lasciano mai il telefono. L'",
        "いいえ。アカウントも、解析も、サーバーも、独自の通信コードもありません。写真が端末の外に"
        "出ることはありません。",
        "아니요. 계정도, 분석도, 서버도, 자체 네트워크 코드도 없습니다. 사진은 절대 휴대폰을 떠나지 "
        "않습니다.",
        "Nee. Geen account, geen analytics, geen server en geen eigen netwerkcode. Foto's verlaten "
        "je telefoon nooit. Het",
        "Não. Sem conta, sem análises, sem servidor e sem código de rede próprio. As fotografias "
        "nunca saem do seu telefone. A",
        "不会。没有账号、没有分析、没有服务器，也没有自己的联网代码。照片永远不会离开你的手机。"),
    "privacy policy": ("Datenschutzerklärung", "política de privacidad", "política de privacidad",
                       "politique de confidentialité", "informativa sulla privacy",
                       "プライバシーポリシー", "개인정보 처리방침", "privacybeleid",
                       "política de privacidade", "隐私政策"),
    "is one page and says so.": (
        "ist eine Seite lang und sagt genau das.", "ocupa una página y lo dice.",
        "ocupa una página y lo dice.", "tient sur une page et le dit.",
        "sta in una pagina e lo dice.", "は一ページで、そう書いてあります。",
        "은 한 페이지이고, 그렇게 적혀 있습니다.", "is één pagina en zegt dat.",
        "tem uma página e diz isso.", "只有一页，上面就是这么写的。"),
    "Make one.": ("Mach eine.", "Haz una.", "Haz una.", "Faites-en un.", "Fanne una.",
                  "一枚つくってみてください。", "한 장 만들어 보세요.", "Maak er een.",
                  "Faça uma.", "做一张试试。"),
    "Free, and the free version is the whole simulation. Nothing is watermarked and nothing is\n"
    "      held back to make a point.": (
        "Kostenlos, und die kostenlose Fassung ist die ganze Simulation. Nichts trägt ein "
        "Wasserzeichen, und nichts wird zurückgehalten, um etwas zu beweisen.",
        "Gratis, y la versión gratuita es la simulación entera. Nada lleva marca de agua y nada se "
        "reserva para dejar claro nada.",
        "Gratis, y la versión gratuita es la simulación entera. Nada lleva marca de agua y nada se "
        "reserva para dejar claro nada.",
        "Gratuit, et la version gratuite est la simulation entière. Rien n'est filigrané et rien "
        "n'est retenu pour faire passer un message.",
        "Gratis, e la versione gratuita è tutta la simulazione. Niente porta filigrane e niente "
        "viene trattenuto per far capire qualcosa.",
        "無料です。そして無料版がシミュレーションのすべてです。透かしも入りませんし、"
        "何かを分からせるために出し惜しみしているものもありません。",
        "무료이고, 무료 버전이 시뮬레이션 전부입니다. 워터마크도 없고, 무언가를 알게 하려고 "
        "아껴 둔 것도 없습니다.",
        "Gratis, en de gratis versie is de hele simulatie. Er staat nergens een watermerk en er "
        "wordt niets achtergehouden om iets duidelijk te maken.",
        "Grátis, e a versão gratuita é a simulação inteira. Nada leva marca d'água e nada é "
        "segurado para provar algum ponto.",
        "免费，而且免费版就是完整的模拟。没有任何水印，也没有为了说明什么而故意留一手。"),
    "Also by Levi Foster": (
        "Ebenfalls von Levi Foster", "También de Levi Foster", "También de Levi Foster",
        "Également de Levi Foster", "Anche di Levi Foster", "Levi Foster のほかの作品",
        "Levi Foster의 다른 작업", "Ook van Levi Foster", "Também de Levi Foster",
        "Levi Foster 的其他作品"),
    "Two more that work the same way.": (
        "Zwei weitere, die genauso arbeiten.", "Dos más que funcionan igual.",
        "Dos más que funcionan igual.", "Deux autres qui fonctionnent de la même façon.",
        "Altre due che funzionano allo stesso modo.", "同じ考え方でつくった、もう二つ。",
        "같은 방식으로 만든 둘 더.", "Nog twee die op dezelfde manier werken.",
        "Mais dois que funcionam do mesmo jeito.", "另外两个，做法是一样的。"),
    "Film Simulation": ("Filmsimulation", "Simulación de película", "Simulación de película",
                        "Simulation argentique", "Simulazione di pellicola",
                        "フィルムシミュレーション", "필름 시뮬레이션", "Filmsimulatie",
                        "Simulação de filme", "胶片模拟"),
    "A camera that models the film itself: light scattering through the emulsion, dye layers\n"
    "        holding each other back, grain forming where the light landed.": (
        "Eine Kamera, die den Film selbst nachbildet: Licht, das durch die Emulsion streut, "
        "Farbschichten, die einander zurückhalten, Korn, das dort entsteht, wo das Licht gelandet "
        "ist.",
        "Una cámara que modela la película en sí: la luz dispersándose por la emulsión, las capas "
        "de colorante frenándose entre sí, el grano formándose donde llegó la luz.",
        "Una cámara que modela la película en sí: la luz dispersándose por la emulsión, las capas "
        "de colorante frenándose entre sí, el grano formándose donde llegó la luz.",
        "Un appareil qui modélise la pellicule elle-même : la lumière qui diffuse dans l'émulsion, "
        "les couches de colorant qui se retiennent, le grain qui se forme là où la lumière est "
        "tombée.",
        "Una fotocamera che modella la pellicola stessa: la luce che diffonde nell'emulsione, gli "
        "strati di colorante che si trattengono a vicenda, la grana che si forma dove la luce è "
        "arrivata.",
        "フィルムそのものを再現するカメラ。乳剤の中で散乱する光、互いを抑え合う色素層、"
        "光が落ちた場所に生まれる粒子。",
        "필름 자체를 모델링하는 카메라. 유제 안에서 산란하는 빛, 서로를 붙잡는 염료층, 빛이 닿은 "
        "자리에 생기는 입자.",
        "Een camera die de film zelf modelleert: licht dat door de emulsie verstrooit, kleurlagen "
        "die elkaar tegenhouden, korrel die ontstaat waar het licht landde.",
        "Uma câmera que modela o filme em si: a luz se espalhando pela emulsão, as camadas de "
        "corante segurando umas às outras, o grão se formando onde a luz caiu.",
        "一款模拟胶片本身的相机：光在乳剂中散射，染料层彼此拖住，颗粒生成在光落下的地方。"),
    "Glitch Art Effects": ("Glitch-Art-Effekte", "Efectos de glitch art", "Efectos de glitch art",
                           "Effets de glitch art", "Effetti glitch art",
                           "グリッチアートエフェクト", "글리치 아트 효과", "Glitch-arteffecten",
                           "Efeitos de glitch art", "故障艺术特效"),
    "Nineteen stackable effects, each modelled on a specific way real hardware used to fail.\n"
    "        Free.": (
        "Neunzehn stapelbare Effekte, jeder einer bestimmten Art nachgebildet, auf die echte "
        "Hardware früher versagte. Kostenlos.",
        "Diecinueve efectos apilables, cada uno modelado sobre una forma concreta en que fallaba "
        "el hardware real. Gratis.",
        "Diecinueve efectos apilables, cada uno modelado sobre una forma concreta en que fallaba "
        "el hardware real. Gratis.",
        "Dix-neuf effets empilables, chacun modélisé sur une façon précise dont le matériel tombait "
        "en panne. Gratuit.",
        "Diciannove effetti impilabili, ognuno modellato su un modo preciso in cui l'hardware vero "
        "si guastava. Gratis.",
        "積み重ねられる十九のエフェクト。いずれも実在のハードウェアが壊れたときの特定の壊れ方を"
        "再現しています。無料。",
        "쌓아 올릴 수 있는 열아홉 가지 효과. 각각 실제 하드웨어가 고장 나던 특정한 방식을 "
        "모델링했습니다. 무료.",
        "Negentien stapelbare effecten, elk gemodelleerd op een specifieke manier waarop echte "
        "hardware kapotging. Gratis.",
        "Dezenove efeitos empilháveis, cada um modelado sobre um jeito específico pelo qual o "
        "hardware de verdade falhava. Grátis.",
        "十九种可叠加的效果，每一种都对应真实硬件当年出错的某种具体方式。免费。"),
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "Support": ("Support", "Soporte", "Soporte", "Assistance", "Assistenza", "サポート", "지원",
                "Ondersteuning", "Suporte", "支持"),
    "CYANO is built by Levi Foster in Fort Worth, Texas": (
        "CYANO wird von Levi Foster in Fort Worth, Texas gebaut",
        "CYANO lo hace Levi Foster en Fort Worth, Texas",
        "CYANO lo hace Levi Foster en Fort Worth, Texas",
        "CYANO est fait par Levi Foster à Fort Worth, Texas",
        "CYANO è fatto da Levi Foster a Fort Worth, Texas",
        "CYANO はテキサス州フォートワースの Levi Foster がつくっています",
        "CYANO는 텍사스주 포트워스의 Levi Foster가 만듭니다",
        "CYANO wordt gemaakt door Levi Foster in Fort Worth, Texas",
        "O CYANO é feito por Levi Foster em Fort Worth, Texas",
        "CYANO 由 Levi Foster 在美国得州沃斯堡打造"),
    "CYANO - Cyanotype Photos": (
        "CYANO - Cyanotypie-Fotos", "CYANO - Fotos en cianotipia", "CYANO - Fotos en cianotipia",
        "CYANO - Photos au cyanotype", "CYANO - Foto in cianotipia",
        "CYANO - サイアノタイプ写真", "CYANO - 사이아노타입 사진", "CYANO - Cyanotypiefoto's",
        "CYANO - Fotos em cianotipia", "CYANO - 蓝晒照片"),
})

# ---------------------------------------------------------------- structured data
T.update({
    "A cyanotype app for iPhone that simulates the chemistry of the 1842 sunprint process rather "
    "than tinting a photograph blue: the sensitiser's ultraviolet response integrated against "
    "sunlight across the spectrum, and Prussian blue built up through the Beer-Lambert law.": (
        "Eine Cyanotypie-App für iPhone, die die Chemie des Sonnendruckverfahrens von 1842 "
        "simuliert, statt ein Foto blau einzufärben: die Ultraviolettantwort des Sensibilisators, "
        "über das Spektrum gegen das Sonnenlicht integriert, und Berliner Blau, aufgebaut über das "
        "Beer-Lambert-Gesetz.",
        "Una app de cianotipia para iPhone que simula la química del proceso de impresión al sol "
        "de 1842 en vez de teñir una foto de azul: la respuesta ultravioleta del sensibilizador "
        "integrada frente a la luz solar a lo largo del espectro, y azul de Prusia construido "
        "mediante la ley de Beer-Lambert.",
        "Una app de cianotipia para iPhone que simula la química del proceso de impresión al sol "
        "de 1842 en vez de teñir una foto de azul: la respuesta ultravioleta del sensibilizador "
        "integrada frente a la luz solar a lo largo del espectro, y azul de Prusia construido "
        "mediante la ley de Beer-Lambert.",
        "Une app de cyanotype pour iPhone qui simule la chimie du procédé d'insolation de 1842 au "
        "lieu de teinter une photo en bleu : la réponse ultraviolette du sensibilisateur intégrée "
        "contre la lumière du soleil sur tout le spectre, et du bleu de Prusse construit par la "
        "loi de Beer-Lambert.",
        "Un'app di cianotipia per iPhone che simula la chimica del procedimento di stampa al sole "
        "del 1842 invece di tingere di blu una foto: la risposta all'ultravioletto del "
        "sensibilizzante integrata contro la luce solare su tutto lo spettro, e blu di Prussia "
        "costruito con la legge di Beer-Lambert.",
        "写真を青く染めるのではなく、1842 年の日光写真の化学を再現する iPhone 用サイアノタイプ"
        "アプリ。増感剤の紫外線応答を太陽光のスペクトルに対して積分し、ベール・ランベルト則で"
        "プルシアンブルーを積み上げます。",
        "사진을 파랗게 물들이는 대신 1842년 태양광 인화 공정의 화학을 시뮬레이션하는 iPhone용 "
        "사이아노타입 앱. 감광제의 자외선 응답을 태양광 스펙트럼에 대해 적분하고, 베어-람베르트 "
        "법칙으로 프러시안 블루를 쌓아 올립니다.",
        "Een cyanotypie-app voor iPhone die de chemie van het zonnedrukproces uit 1842 simuleert "
        "in plaats van een foto blauw te kleuren: de ultraviolette respons van de sensibilisator "
        "geïntegreerd tegen zonlicht over het spectrum, en Pruisisch blauw opgebouwd via de wet "
        "van Beer-Lambert.",
        "Um app de cianotipia para iPhone que simula a química do processo de impressão ao sol de "
        "1842 em vez de tingir uma foto de azul: a resposta ultravioleta do sensibilizador "
        "integrada contra a luz do sol ao longo do espectro, e azul da Prússia construído pela lei "
        "de Beer-Lambert.",
        "一款 iPhone 蓝晒应用，模拟 1842 年日光晒印工艺的化学，而不是把照片染成蓝色："
        "把感光剂的紫外响应在整个光谱上对太阳光积分，再依比尔-朗伯定律叠出普鲁士蓝。"),
    "Reflectance reconstructed from three numbers, then read where the sensitiser can see": (
        "Reflexion, aus drei Zahlen rekonstruiert und dort gelesen, wo der Sensibilisator sehen "
        "kann",
        "Reflectancia reconstruida a partir de tres números y leída donde el sensibilizador puede "
        "ver",
        "Reflectancia reconstruida a partir de tres números y leída donde el sensibilizador puede "
        "ver",
        "Réflectance reconstruite à partir de trois nombres, puis lue là où le sensibilisateur "
        "voit",
        "Riflettanza ricostruita da tre numeri, poi letta dove il sensibilizzante può vedere",
        "三つの数値から復元した反射率を、増感剤が見える波長で読む",
        "세 개의 숫자로 복원한 반사율을, 감광제가 볼 수 있는 곳에서 읽음",
        "Reflectie gereconstrueerd uit drie getallen, en gelezen waar de sensibilisator kan zien",
        "Refletância reconstruída a partir de três números e lida onde o sensibilizador enxerga",
        "由三个数字重建反射率，再在感光剂看得见的波段读取"),
    "Prussian blue built by the Beer-Lambert law, including pigment aggregation": (
        "Berliner Blau, aufgebaut über das Beer-Lambert-Gesetz, einschließlich Pigmentaggregation",
        "Azul de Prusia construido por la ley de Beer-Lambert, incluida la agregación del pigmento",
        "Azul de Prusia construido por la ley de Beer-Lambert, incluida la agregación del pigmento",
        "Bleu de Prusse construit par la loi de Beer-Lambert, agrégation du pigment comprise",
        "Blu di Prussia costruito con la legge di Beer-Lambert, aggregazione del pigmento inclusa",
        "顔料の凝集も含め、ベール・ランベルト則で積み上げるプルシアンブルー",
        "안료의 응집까지 포함해 베어-람베르트 법칙으로 쌓는 프러시안 블루",
        "Pruisisch blauw opgebouwd via de wet van Beer-Lambert, inclusief pigmentaggregatie",
        "Azul da Prússia construído pela lei de Beer-Lambert, incluindo a agregação do pigmento",
        "依比尔-朗伯定律叠出的普鲁士蓝，含颜料聚集"),
    "A tonal curve derived from the photochemistry rather than drawn by hand": (
        "Eine Tonwertkurve, aus der Fotochemie abgeleitet statt von Hand gezeichnet",
        "Una curva tonal derivada de la fotoquímica en vez de dibujada a mano",
        "Una curva tonal derivada de la fotoquímica en vez de dibujada a mano",
        "Une courbe tonale dérivée de la photochimie plutôt que tracée à la main",
        "Una curva tonale derivata dalla fotochimica invece che disegnata a mano",
        "手で描くのではなく、写真化学から導いた階調曲線",
        "손으로 그린 것이 아니라 광화학에서 유도한 계조 곡선",
        "Een tooncurve afgeleid uit de fotochemie in plaats van met de hand getekend",
        "Uma curva tonal derivada da fotoquímica em vez de desenhada à mão",
        "从光化学推导出来、而非手工绘制的影调曲线"),
    "Exposure chosen per photograph, the way a printer reads a negative": (
        "Belichtung, pro Foto gewählt, so wie ein Vergrößerer ein Negativ liest",
        "Exposición elegida por fotografía, como un copista lee un negativo",
        "Exposición elegida por fotografía, como un copista lee un negativo",
        "Exposition choisie photo par photo, comme un tireur lit un négatif",
        "Esposizione scelta per ogni fotografia, come uno stampatore legge un negativo",
        "焼き付け職人がネガを読むように、一枚ごとに決める露光量",
        "인화 기사가 네거티브를 읽듯이, 사진마다 정하는 노광량",
        "Belichting per foto gekozen, zoals een printer een negatief leest",
        "Exposição escolhida por fotografia, do jeito que um copista lê um negativo",
        "逐张选定的曝光量，就像放大师读一张底片"),
    "Toning that converts the pigment to iron tannate rather than tinting it": (
        "Tonung, die das Pigment in Eisentannat umwandelt, statt es einzufärben",
        "Virado que convierte el pigmento en tanato de hierro en vez de teñirlo",
        "Virado que convierte el pigmento en tanato de hierro en vez de teñirlo",
        "Virage qui convertit le pigment en tannate de fer au lieu de le teinter",
        "Viraggio che converte il pigmento in tannato di ferro invece di tingerlo",
        "顔料を染めるのではなく、タンニン酸鉄へと変える調色",
        "안료를 물들이는 것이 아니라 타닌산철로 바꾸는 조색",
        "Toning die het pigment omzet in ijzertannaat in plaats van het te kleuren",
        "Viragem que converte o pigmento em tanato de ferro em vez de tingi-lo",
        "把颜料转化为单宁酸铁、而不是给它上色的调色"),
    "Three papers, whose base colour shows through the print": (
        "Drei Papiere, deren Grundfarbe durch den Druck scheint",
        "Tres papeles, cuyo color de base se transparenta en la copia",
        "Tres papeles, cuyo color de base se transparenta en la copia",
        "Trois papiers, dont la couleur de base transparaît dans le tirage",
        "Tre carte, il cui colore di base traspare nella stampa",
        "三種の紙。その地の色がプリントを通して見える",
        "세 가지 종이. 그 바탕색이 인화지 너머로 비쳐 나옴",
        "Drie papieren, waarvan de basiskleur door de afdruk schijnt",
        "Três papéis, cuja cor de base aparece através da cópia",
        "三种纸，纸的底色会透过成品显出来"),
    "No account, no server, no subscription": (
        "Kein Konto, kein Server, kein Abo", "Sin cuenta, sin servidor, sin suscripción",
        "Sin cuenta, sin servidor, sin suscripción", "Sans compte, sans serveur, sans abonnement",
        "Nessun account, nessun server, nessun abbonamento",
        "アカウントなし、サーバーなし、定額課金なし", "계정 없음, 서버 없음, 구독 없음",
        "Geen account, geen server, geen abonnement", "Sem conta, sem servidor, sem assinatura",
        "无账号、无服务器、无订阅"),
    "A cyanotype is the oldest surviving photographic process, invented in 1842. Paper is brushed "
    "with iron salts, a negative is laid on top, and it is left in the sun. What develops is "
    "Prussian blue, washed out in plain water. It is the reason old engineering drawings are called "
    "blueprints.": (
        "Die Cyanotypie ist das älteste noch erhaltene fotografische Verfahren, erfunden 1842. "
        "Papier wird mit Eisensalzen bestrichen, ein Negativ daraufgelegt und das Ganze in die "
        "Sonne gelegt. Was entsteht, ist Berliner Blau, in klarem Wasser ausgewaschen. Es ist der "
        "Grund, warum alte technische Zeichnungen Blaupausen heißen.",
        "La cianotipia es el proceso fotográfico más antiguo que sobrevive, inventado en 1842. Se "
        "pincela papel con sales de hierro, se pone un negativo encima y se deja al sol. Lo que se "
        "revela es azul de Prusia, lavado en agua corriente. Es la razón de que a los planos "
        "antiguos se les llame cianotipos.",
        "La cianotipia es el proceso fotográfico más antiguo que sobrevive, inventado en 1842. Se "
        "pincela papel con sales de hierro, se pone un negativo encima y se deja al sol. Lo que se "
        "revela es azul de Prusia, lavado en agua corriente. Es la razón de que a los planos "
        "antiguos se les llame cianotipos.",
        "Le cyanotype est le plus ancien procédé photographique encore pratiqué, inventé en 1842. "
        "On badigeonne du papier de sels de fer, on pose un négatif dessus et on laisse au soleil. "
        "Ce qui se développe est du bleu de Prusse, rincé à l'eau claire. C'est la raison pour "
        "laquelle on appelle les vieux plans techniques des bleus.",
        "La cianotipia è il più antico procedimento fotografico ancora in uso, inventato nel 1842. "
        "Si pennella la carta con sali di ferro, si appoggia sopra un negativo e si lascia al "
        "sole. Quello che si sviluppa è blu di Prussia, lavato in acqua pura. È il motivo per cui "
        "i vecchi disegni tecnici si chiamano cianografie.",
        "サイアノタイプは 1842 年に生まれた、現存する最も古い写真の技法です。紙に鉄塩を刷毛で塗り、"
        "ネガを重ねて日なたに置きます。現れるのはプルシアンブルーで、ただの水で洗い流します。"
        "古い設計図が「青焼き」と呼ばれるのは、これが理由です。",
        "사이아노타입은 1842년에 만들어진, 지금까지 살아남은 가장 오래된 사진 공정입니다. 종이에 "
        "철염을 붓으로 바르고 네거티브를 얹어 햇빛 아래 둡니다. 나타나는 것은 프러시안 블루이고, "
        "맑은 물로 씻어 냅니다. 옛 설계도를 청사진이라 부르는 이유입니다.",
        "De cyanotypie is het oudste nog bestaande fotografische procedé, uitgevonden in 1842. "
        "Papier wordt bestreken met ijzerzouten, er wordt een negatief op gelegd en het geheel "
        "wordt in de zon gezet. Wat er ontstaat is Pruisisch blauw, uitgewassen in schoon water. "
        "Het is de reden dat oude technische tekeningen blauwdrukken heten.",
        "A cianotipia é o processo fotográfico mais antigo que sobreviveu, inventado em 1842. "
        "Pincela-se papel com sais de ferro, põe-se um negativo por cima e deixa-se ao sol. O que "
        "se revela é azul da Prússia, lavado em água limpa. É a razão de os desenhos técnicos "
        "antigos serem chamados de blueprints.",
        "蓝晒是现存最古老的摄影工艺，诞生于 1842 年。用铁盐刷过纸面，压上一张底片，"
        "放到太阳底下。显出来的是普鲁士蓝，用清水冲洗即可。老的工程图之所以被称作\"蓝图\"，"
        "原因就在这里。"),
    "What is a cyanotype?": (
        "Was ist eine Cyanotypie?", "¿Qué es una cianotipia?", "¿Qué es una cianotipia?",
        "Qu'est-ce qu'un cyanotype ?", "Che cos'è una cianotipia?", "サイアノタイプとは何ですか。",
        "사이아노타입이란 무엇인가요?", "Wat is een cyanotypie?", "O que é uma cianotipia?",
        "什么是蓝晒？"),
    "No. A filter decides in advance what each colour becomes. CYANO works out how much "
    "ultraviolet and deep blue light each colour actually carries, then builds up Prussian blue "
    "from that. It is why a yellow flower goes almost black while a blue sky burns out to bare "
    "paper, even when a camera recorded the two at the same brightness.": (
        "Nein. Ein Filter entscheidet vorab, was aus jeder Farbe wird. CYANO rechnet aus, wie viel "
        "ultraviolettes und tiefblaues Licht jede Farbe tatsächlich trägt, und baut daraus "
        "Berliner Blau auf. Darum wird eine gelbe Blume fast schwarz, während ein blauer Himmel "
        "bis auf das blanke Papier ausbrennt, selbst wenn eine Kamera beide gleich hell "
        "aufgezeichnet hat.",
        "No. Un filtro decide de antemano en qué se convierte cada color. CYANO calcula cuánta luz "
        "ultravioleta y azul profunda lleva realmente cada color, y a partir de ahí construye azul "
        "de Prusia. Por eso una flor amarilla queda casi negra mientras un cielo azul se quema "
        "hasta el papel desnudo, aunque una cámara registrara ambos con el mismo brillo.",
        "No. Un filtro decide de antemano en qué se convierte cada color. CYANO calcula cuánta luz "
        "ultravioleta y azul profunda lleva realmente cada color, y a partir de ahí construye azul "
        "de Prusia. Por eso una flor amarilla queda casi negra mientras un cielo azul se quema "
        "hasta el papel desnudo, aunque una cámara registrara ambos con el mismo brillo.",
        "Non. Un filtre décide à l'avance ce que devient chaque couleur. CYANO calcule combien de "
        "lumière ultraviolette et bleu profond chaque couleur porte réellement, puis construit du "
        "bleu de Prusse à partir de là. C'est pourquoi une fleur jaune devient presque noire "
        "tandis qu'un ciel bleu brûle jusqu'au papier nu, même quand un appareil a enregistré les "
        "deux à la même luminosité.",
        "No. Un filtro decide in anticipo cosa diventa ogni colore. CYANO calcola quanta luce "
        "ultravioletta e blu profondo porta davvero ogni colore, e da lì costruisce il blu di "
        "Prussia. È per questo che un fiore giallo diventa quasi nero mentre un cielo azzurro si "
        "brucia fino alla carta nuda, anche quando una fotocamera li ha registrati alla stessa "
        "luminosità.",
        "いいえ。フィルターは、どの色が何になるかを前もって決めます。CYANO は、それぞれの色が"
        "実際にどれだけ紫外線と深い青の光を運んでいるかを計算し、そこからプルシアンブルーを"
        "積み上げます。カメラが同じ明るさとして記録していても、黄色い花がほとんど黒く沈み、"
        "青空が紙の地肌まで飛ぶのは、そのためです。",
        "아니요. 필터는 어떤 색이 무엇이 될지 미리 정합니다. CYANO는 각 색이 실제로 자외선과 깊은 "
        "파랑의 빛을 얼마나 싣고 있는지를 계산하고, 거기서부터 프러시안 블루를 쌓아 올립니다. "
        "카메라가 둘을 같은 밝기로 기록했더라도 노란 꽃은 거의 검게 가라앉고 파란 하늘은 종이 "
        "바탕까지 날아가는 이유입니다.",
        "Nee. Een filter beslist vooraf wat elke kleur wordt. CYANO rekent uit hoeveel ultraviolet "
        "en diepblauw licht elke kleur werkelijk meedraagt, en bouwt daaruit Pruisisch blauw op. "
        "Daarom wordt een gele bloem bijna zwart terwijl een blauwe lucht uitbrandt tot kaal "
        "papier, zelfs als een camera de twee op dezelfde helderheid vastlegde.",
        "Não. Um filtro decide de antemão no que cada cor vira. O CYANO calcula quanta luz "
        "ultravioleta e azul profunda cada cor de fato carrega, e a partir daí constrói o azul da "
        "Prússia. É por isso que uma flor amarela fica quase preta enquanto um céu azul estoura "
        "até o papel nu, mesmo quando uma câmera registrou os dois com o mesmo brilho.",
        "不是。滤镜会事先决定每种颜色变成什么。CYANO 会算出每种颜色实际带了多少紫外线和深蓝光，"
        "再由此叠出普鲁士蓝。所以即便相机把两者记录成同样的亮度，"
        "一朵黄花仍会几乎全黑，而蓝天会烧到只剩纸的本色。"),
    "Is CYANO just a blue filter?": (
        "Ist CYANO nur ein Blaufilter?", "¿CYANO es solo un filtro azul?",
        "¿CYANO es solo un filtro azul?", "CYANO n'est-il qu'un filtre bleu ?",
        "CYANO è solo un filtro blu?", "CYANO は単なる青いフィルターですか。",
        "CYANO는 그냥 파란 필터인가요?", "Is CYANO gewoon een blauwfilter?",
        "O CYANO é só um filtro azul?", "CYANO 只是一个蓝色滤镜吗？"),
    "None of them. CYANO exists so that anyone can make cyanotypes without a darkroom, a chemistry "
    "set or a UV source. Everything happens on the phone.": (
        "Nichts davon. CYANO gibt es, damit jeder Cyanotypien machen kann, ohne Dunkelkammer, "
        "Chemiekasten oder UV-Quelle. Alles passiert auf dem Telefon.",
        "Ninguno. CYANO existe para que cualquiera pueda hacer cianotipias sin cuarto oscuro, sin "
        "juego de química y sin fuente ultravioleta. Todo ocurre en el móvil.",
        "Ninguno. CYANO existe para que cualquiera pueda hacer cianotipias sin cuarto oscuro, sin "
        "juego de química y sin fuente ultravioleta. Todo ocurre en el celular.",
        "Aucun. CYANO existe pour que n'importe qui puisse faire des cyanotypes sans chambre "
        "noire, sans nécessaire de chimie et sans source UV. Tout se passe sur le téléphone.",
        "Nessuno. CYANO esiste perché chiunque possa fare cianotipie senza camera oscura, senza "
        "kit di chimica e senza sorgente UV. Tutto succede sul telefono.",
        "どれも要りません。暗室も、薬品一式も、紫外線光源もなしに、誰でもサイアノタイプを"
        "つくれるように CYANO はあります。すべては端末の上で起こります。",
        "아무것도 필요 없습니다. 암실도, 약품 세트도, 자외선 광원도 없이 누구나 사이아노타입을 만들 "
        "수 있도록 CYANO가 있습니다. 모든 것이 휴대폰 위에서 일어납니다.",
        "Geen ervan. CYANO bestaat zodat iedereen cyanotypieën kan maken zonder donkere kamer, "
        "chemiedoos of UV-bron. Alles gebeurt op de telefoon.",
        "Nenhum deles. O CYANO existe para que qualquer um consiga fazer cianotipias sem câmara "
        "escura, kit de química ou fonte de UV. Tudo acontece no telefone.",
        "都不需要。CYANO 的存在，是为了让任何人都能在没有暗房、没有化学套装、"
        "也没有紫外光源的情况下做出蓝晒。一切都在手机上完成。"),
    "The app is free and fully functional: unlimited prints at full resolution with no watermark. "
    "One optional purchase of 4.99 US dollars unlocks the three toning baths, the other two papers "
    "and the second sensitiser formula. There is no subscription.": (
        "Die App ist kostenlos und voll funktionsfähig: unbegrenzt Abzüge in voller Auflösung ohne "
        "Wasserzeichen. Ein optionaler Kauf für 4,99 US-Dollar schaltet die drei Tonbäder, die "
        "anderen beiden Papiere und die zweite Sensibilisatorformel frei. Es gibt kein Abo.",
        "La app es gratuita y plenamente funcional: copias ilimitadas a resolución completa y sin "
        "marca de agua. Una compra opcional de 4,99 dólares estadounidenses desbloquea los tres "
        "baños de virado, los otros dos papeles y la segunda fórmula de sensibilizador. No hay "
        "suscripción.",
        "La app es gratuita y plenamente funcional: copias ilimitadas a resolución completa y sin "
        "marca de agua. Una compra opcional de 4,99 dólares estadounidenses desbloquea los tres "
        "baños de virado, los otros dos papeles y la segunda fórmula de sensibilizador. No hay "
        "suscripción.",
        "L'app est gratuite et pleinement fonctionnelle : tirages illimités en pleine résolution "
        "sans filigrane. Un achat facultatif de 4,99 dollars américains débloque les trois bains "
        "de virage, les deux autres papiers et la seconde formule de sensibilisateur. Il n'y a pas "
        "d'abonnement.",
        "L'app è gratuita e pienamente funzionante: stampe illimitate a piena risoluzione senza "
        "filigrana. Un acquisto facoltativo da 4,99 dollari statunitensi sblocca i tre bagni di "
        "viraggio, le altre due carte e la seconda formula di sensibilizzante. Non c'è "
        "abbonamento.",
        "アプリは無料で、そのまま完全に使えます。フル解像度で枚数無制限、透かしなし。"
        "任意の 4.99 米ドルの購入で、三つの調色浴、残り二種の紙、二つめの増感剤処方が"
        "使えるようになります。定額課金はありません。",
        "앱은 무료이고 완전히 동작합니다. 원본 해상도로 무제한 인화, 워터마크 없음. 선택 구매 4.99 "
        "미국 달러로 세 가지 조색액, 나머지 두 종류의 종이, 두 번째 감광제 조성이 열립니다. 구독은 "
        "없습니다.",
        "De app is gratis en volledig functioneel: onbeperkt afdrukken op volle resolutie zonder "
        "watermerk. Eén optionele aankoop van 4,99 Amerikaanse dollar ontgrendelt de drie "
        "toningbaden, de andere twee papieren en de tweede sensibilisatorformule. Er is geen "
        "abonnement.",
        "O app é grátis e totalmente funcional: cópias ilimitadas em resolução total sem marca "
        "d'água. Uma compra opcional de 4,99 dólares americanos libera os três banhos de viragem, "
        "os outros dois papéis e a segunda fórmula de sensibilizador. Não há assinatura.",
        "这个应用是免费的，而且功能完整：完整分辨率、无限张数、没有水印。"
        "一次可选的 4.99 美元购买会解锁三种调色液、另外两种纸，以及第二种感光剂配方。没有订阅。"),
    "How much does CYANO cost?": (
        "Was kostet CYANO?", "¿Cuánto cuesta CYANO?", "¿Cuánto cuesta CYANO?",
        "Combien coûte CYANO ?", "Quanto costa CYANO?", "CYANO はいくらですか。",
        "CYANO는 얼마인가요?", "Wat kost CYANO?", "Quanto custa o CYANO?", "CYANO 多少钱？"),
    "No. There is no account, no analytics and no server, and the app contains no networking code "
    "of its own. Photographs never leave the device.": (
        "Nein. Es gibt kein Konto, keine Analyse und keinen Server, und die App enthält keinen "
        "eigenen Netzwerkcode. Fotos verlassen das Gerät nie.",
        "No. No hay cuenta, ni analíticas, ni servidor, y la app no contiene código de red propio. "
        "Las fotografías nunca salen del dispositivo.",
        "No. No hay cuenta, ni analíticas, ni servidor, y la app no contiene código de red propio. "
        "Las fotografías nunca salen del dispositivo.",
        "Non. Il n'y a pas de compte, pas d'analytique et pas de serveur, et l'app ne contient "
        "aucun code réseau propre. Les photographies ne quittent jamais l'appareil.",
        "No. Non c'è account, non ci sono analisi e non c'è server, e l'app non contiene codice di "
        "rete proprio. Le fotografie non lasciano mai il dispositivo.",
        "いいえ。アカウントも、解析も、サーバーもなく、アプリは独自の通信コードを持ちません。"
        "写真が端末の外に出ることはありません。",
        "아니요. 계정도, 분석도, 서버도 없고, 앱은 자체 네트워크 코드를 갖고 있지 않습니다. 사진은 "
        "절대 기기를 떠나지 않습니다.",
        "Nee. Er is geen account, geen analytics en geen server, en de app bevat geen eigen "
        "netwerkcode. Foto's verlaten het toestel nooit.",
        "Não. Não há conta, não há análises e não há servidor, e o app não contém código de rede "
        "próprio. As fotografias nunca saem do aparelho.",
        "不会。没有账号、没有分析、没有服务器，应用本身也没有联网代码。照片永远不会离开设备。"),
    "Does CYANO collect any data?": (
        "Sammelt CYANO Daten?", "¿CYANO recoge datos?", "¿CYANO recoge datos?",
        "CYANO collecte-t-il des données ?", "CYANO raccoglie dati?",
        "CYANO はデータを収集しますか。", "CYANO는 데이터를 수집하나요?",
        "Verzamelt CYANO gegevens?", "O CYANO coleta algum dado?", "CYANO 会收集数据吗？"),
})

# Same again on the cross-links at the foot of the CYANO page.
T["FRMT: Film Simulation"] = tuple("FRMT: " + v for v in T["Film Simulation"])
T["MODUL8: Glitch Art Effects"] = tuple("MODUL8: " + v for v in T["Glitch Art Effects"])

# The visible answer is split around an inline link to the privacy policy; the schema carries it as
# one sentence. Composed from the three fragments so the two say exactly the same thing.
T["No. No account, no analytics, no server, and no networking code of its own. Photographs never "
  "leave your phone. The privacy policy is one page and says so."] = tuple(
    f"{a} {b} {c}".replace("  ", " ").replace(" .", ".").replace("’ ", "’")
    for a, b, c in zip(
        T["No. No account, no analytics, no server, and no networking code of its own. "
          "Photographs never\n      leave your phone. The"],
        T["privacy policy"], T["is one page and says so."]))
