"""lf.wtf/dollop, part A: head, hero, the argument, the five modes.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Two things have to survive translation intact. The first is the claim itself: blue and yellow make
green *because paint subtracts light*, and every language states the mechanism rather than the
result. Softening it to "the colours combine realistically" would throw away the only sentence the
page is really making.

The second is the mode names. These are the names the app will show once its own catalog is
translated, so they are chosen here first and reused there, not invented twice. From Life is the
painter's term for working from the thing in front of you, and each language uses its own: nach der
Natur, del natural, d'apres nature, dal vero, 写生.
"""

T = {
    # ------------------------------------------------------------------ head

    "Dollop: a color mixing game where blue and yellow make green": (
        "Dollop: ein Farbmischspiel, in dem Blau und Gelb Grün ergeben",
        "Dollop: un juego de mezcla de colores donde el azul y el amarillo dan verde",
        "Dollop: un juego de mezcla de colores donde el azul y el amarillo dan verde",
        "Dollop : un jeu de mélange de couleurs où le bleu et le jaune donnent du vert",
        "Dollop: un gioco di mescolanza dei colori in cui blu e giallo danno il verde",
        "Dollop：青と黄を混ぜると緑になる色混ぜゲーム",
        "Dollop: 파랑과 노랑을 섞으면 초록이 되는 색 혼합 게임",
        "Dollop: een kleurmengspel waarin blauw en geel groen worden",
        "Dollop: um jogo de mistura de cores em que azul e amarelo dão verde",
        "Dollop：蓝加黄会变成绿的调色游戏"),

    "A slow, calming color mixing puzzle for iPhone. The paint is simulated rather than blended, "
    "so blue and yellow make green instead of gray. Free, no account, no ads, no internet needed.": (
        "Ein ruhiges, entschleunigtes Farbmisch-Puzzle fürs iPhone. Die Farbe wird simuliert statt "
        "überblendet, deshalb ergeben Blau und Gelb Grün statt Grau. Kostenlos, ohne Konto, ohne "
        "Werbung, ohne Internet.",
        "Un puzle de mezcla de colores lento y relajante para iPhone. La pintura se simula en vez "
        "de fundirse, así que el azul y el amarillo dan verde y no gris. Gratis, sin cuenta, sin "
        "anuncios y sin internet.",
        "Un juego de mezcla de colores lento y relajante para iPhone. La pintura se simula en vez "
        "de fundirse, así que el azul y el amarillo dan verde y no gris. Gratis, sin cuenta, sin "
        "anuncios y sin internet.",
        "Un puzzle de mélange de couleurs lent et apaisant pour iPhone. La peinture est simulée "
        "plutôt que fondue : le bleu et le jaune donnent donc du vert, pas du gris. Gratuit, sans "
        "compte, sans publicité, sans connexion.",
        "Un puzzle di mescolanza dei colori lento e rilassante per iPhone. La vernice è simulata "
        "invece che sfumata, così blu e giallo danno verde e non grigio. Gratis, senza account, "
        "senza pubblicità, senza internet.",
        "iPhone のためのゆっくり静かな色混ぜパズル。絵の具はブレンドではなくシミュレーション"
        "なので、青と黄は灰色ではなく緑になります。無料、アカウント不要、広告なし、通信なし。",
        "iPhone을 위한 느리고 차분한 색 혼합 퍼즐. 물감을 겹쳐 섞는 대신 시뮬레이션하기 때문에 "
        "파랑과 노랑이 회색이 아니라 초록이 됩니다. 무료, 계정 없음, 광고 없음, 인터넷 없이.",
        "Een traag, rustgevend kleurmengspel voor iPhone. De verf wordt gesimuleerd in plaats van "
        "gemengd, dus blauw en geel worden groen in plaats van grijs. Gratis, zonder account, "
        "zonder advertenties, zonder internet.",
        "Um quebra-cabeça de mistura de cores lento e tranquilo para iPhone. A tinta é simulada em "
        "vez de mesclada, então azul e amarelo dão verde, não cinza. Grátis, sem conta, sem "
        "anúncios e sem internet.",
        "一款慢节奏、让人平静的 iPhone 调色解谜游戏。颜料是被模拟出来的，而不是简单混合，"
        "所以蓝加黄得到的是绿色而不是灰色。免费，无需账号，没有广告，不联网。"),

    "A slow, calming paint puzzle for iPhone. The pigment is simulated, not blended.": (
        "Ein ruhiges, entschleunigtes Farbpuzzle fürs iPhone. Das Pigment wird simuliert, nicht "
        "überblendet.",
        "Un puzle de pintura lento y relajante para iPhone. El pigmento se simula, no se funde.",
        "Un juego de pintura lento y relajante para iPhone. El pigmento se simula, no se funde.",
        "Un puzzle de peinture lent et apaisant pour iPhone. Le pigment est simulé, pas fondu.",
        "Un puzzle di pittura lento e rilassante per iPhone. Il pigmento è simulato, non sfumato.",
        "iPhone のためのゆっくり静かな絵の具パズル。顔料はブレンドではなくシミュレーションです。",
        "iPhone을 위한 느리고 차분한 물감 퍼즐. 안료는 섞는 것이 아니라 시뮬레이션됩니다.",
        "Een traag, rustgevend verfspel voor iPhone. Het pigment wordt gesimuleerd, niet gemengd.",
        "Um quebra-cabeça de tinta lento e tranquilo para iPhone. O pigmento é simulado, não "
        "mesclado.",
        "一款慢节奏、让人平静的 iPhone 颜料解谜游戏。颜料是模拟出来的，不是混合出来的。"),

    "The Dollop icon: a blue dollop and a yellow dollop overlapping, green where they cross.": (
        "Das Dollop-Symbol: ein blauer und ein gelber Farbklecks überlappen sich, und dort, wo sie "
        "sich kreuzen, ist es grün.",
        "El icono de Dollop: una gota azul y una gota amarilla superpuestas, verdes donde se cruzan.",
        "El ícono de Dollop: una gota azul y una gota amarilla superpuestas, verdes donde se cruzan.",
        "L'icône de Dollop : une noisette de bleu et une de jaune qui se chevauchent, vertes là où "
        "elles se croisent.",
        "L'icona di Dollop: una goccia blu e una gialla che si sovrappongono, verdi dove si "
        "incrociano.",
        "Dollop のアイコン：青と黄の絵の具が重なり、重なった部分は緑。",
        "Dollop 아이콘: 파란 물감과 노란 물감이 겹치고, 겹친 자리는 초록.",
        "Het Dollop-icoon: een blauwe en een gele klodder die elkaar overlappen, groen waar ze "
        "elkaar kruisen.",
        "O ícone do Dollop: um pingo azul e um pingo amarelo se sobrepondo, verdes onde se cruzam.",
        "Dollop 图标：一团蓝色和一团黄色相互重叠，交叠处是绿色。"),

    # ------------------------------------------------------------------ hero

    "A color game for iPhone": (
        "Ein Farbspiel fürs iPhone",
        "Un juego de color para iPhone",
        "Un juego de color para iPhone",
        "Un jeu de couleur pour iPhone",
        "Un gioco di colore per iPhone",
        "iPhone のための色のゲーム",
        "iPhone을 위한 색 게임",
        "Een kleurspel voor iPhone",
        "Um jogo de cor para iPhone",
        "一款 iPhone 上的颜色游戏"),

    "Blue and yellow make green.": (
        "Blau und Gelb ergeben Grün.",
        "El azul y el amarillo dan verde.",
        "El azul y el amarillo dan verde.",
        "Le bleu et le jaune donnent du vert.",
        "Il blu e il giallo danno il verde.",
        "青と黄で緑になる。",
        "파랑과 노랑을 섞으면 초록.",
        "Blauw en geel worden groen.",
        "Azul e amarelo dão verde.",
        "蓝加黄，得到绿。"),

    "On a screen they make gray. Dollop is a puzzle about mixing paint, and the paint in\n"
    "  it is simulated rather than blended, so it behaves the way paint behaves. You are given a "
    "color.\n  You mix it.": (
        "Auf einem Bildschirm ergeben sie Grau. Dollop ist ein Puzzle über das Mischen von Farbe, "
        "und diese Farbe wird simuliert statt überblendet, also verhält sie sich wie Farbe. Du "
        "bekommst einen Farbton. Du mischst ihn.",
        "En una pantalla dan gris. Dollop es un puzle sobre mezclar pintura, y esa pintura se "
        "simula en vez de fundirse, así que se comporta como se comporta la pintura. Te dan un "
        "color. Lo mezclas.",
        "En una pantalla dan gris. Dollop es un juego sobre mezclar pintura, y esa pintura se "
        "simula en vez de fundirse, así que se comporta como se comporta la pintura. Te dan un "
        "color. Lo mezclas.",
        "Sur un écran, ils donnent du gris. Dollop est un puzzle sur le mélange de la peinture, et "
        "cette peinture est simulée plutôt que fondue : elle se comporte donc comme de la "
        "peinture. On vous donne une couleur. Vous la mélangez.",
        "Su uno schermo danno grigio. Dollop è un puzzle sul mescolare la vernice, e quella "
        "vernice è simulata invece che sfumata, quindi si comporta come si comporta la vernice. Ti "
        "viene dato un colore. Lo mescoli.",
        "画面の上では灰色になります。Dollop は絵の具を混ぜるパズルで、その絵の具はブレンドでは"
        "なくシミュレーションなので、絵の具のとおりに振る舞います。色がひとつ示されます。それを"
        "混ぜてつくります。",
        "화면에서는 회색이 됩니다. Dollop은 물감을 섞는 퍼즐이고, 그 물감은 겹쳐 섞는 대신 "
        "시뮬레이션되기 때문에 실제 물감처럼 움직입니다. 색이 하나 주어집니다. 그 색을 만들면 "
        "됩니다.",
        "Op een scherm worden ze grijs. Dollop is een puzzel over het mengen van verf, en die verf "
        "wordt gesimuleerd in plaats van gemengd, dus gedraagt ze zich zoals verf zich gedraagt. Je "
        "krijgt een kleur. Die meng je.",
        "Numa tela eles dão cinza. Dollop é um quebra-cabeça sobre misturar tinta, e essa tinta é "
        "simulada em vez de mesclada, então ela se comporta como tinta se comporta. Você recebe uma "
        "cor. Você a mistura.",
        "在屏幕上它们只会变成灰色。Dollop 是一款关于调颜料的解谜游戏，而这里的颜料是被模拟出来"
        "的，不是简单混合，所以它的表现和真颜料一样。你会拿到一个颜色，把它调出来。"),

    "Target": (
        "Ziel", "Objetivo", "Objetivo", "Cible", "Obiettivo",
        "目標", "목표", "Doel", "Alvo", "目标"),

    "Yours": (
        "Deins", "El tuyo", "El tuyo", "Le vôtre", "Il tuo",
        "あなたの色", "내 색", "Die van jou", "O seu", "你的"),

    "Scrape it off": (
        "Abkratzen", "Ráspalo", "Ráspalo", "Tout gratter", "Raschia via",
        "こそげ落とす", "긁어내기", "Eraf schrapen", "Raspar tudo", "刮掉重来"),

    "New color": (
        "Neue Farbe", "Color nuevo", "Color nuevo", "Nouvelle couleur", "Nuovo colore",
        "新しい色", "새로운 색", "Nieuwe kleur", "Nova cor", "换个颜色"),

    "Tap a pigment to put a dollop on the\n  board. This is the game itself, running the app's own "
    "arithmetic rather than a picture of it.": (
        "Tippe ein Pigment an, um einen Klecks auf das Brett zu setzen. Das hier ist das Spiel "
        "selbst: es rechnet mit derselben Arithmetik wie die App und ist kein Bild davon.",
        "Toca un pigmento para poner una gota en el tablero. Esto es el juego mismo, ejecutando la "
        "misma aritmética que la app y no una imagen de ella.",
        "Toca un pigmento para poner una gota en el tablero. Esto es el juego mismo, ejecutando la "
        "misma aritmética que la app y no una imagen de ella.",
        "Touchez un pigment pour déposer une noisette sur la planche. C'est le jeu lui-même, qui "
        "fait tourner l'arithmétique de l'app, pas une image de celle-ci.",
        "Tocca un pigmento per mettere una goccia sulla tavola. Questo è il gioco stesso, che "
        "esegue la stessa aritmetica dell'app e non un'immagine di essa.",
        "顔料をタップすると、板に絵の具がひとつ落ちます。これは画像ではなく、アプリと同じ計算を"
        "そのまま動かしているゲームそのものです。",
        "안료를 탭하면 판 위에 물감이 한 덩이 놓입니다. 이것은 그림이 아니라, 앱과 똑같은 계산을 "
        "그대로 돌리는 게임 그 자체입니다.",
        "Tik op een pigment om een klodder op het bord te zetten. Dit is het spel zelf: het draait "
        "dezelfde rekensom als de app, het is er geen plaatje van.",
        "Toque em um pigmento para colocar um pingo no tabuleiro. Isto é o jogo em si, rodando a "
        "mesma aritmética do app e não uma imagem dela.",
        "点一下颜料，就会有一团落到板上。这不是截图，而是游戏本身，跑的就是 App 里的那套算术。"),

    "Coming to the App Store": (
        "Bald im App Store",
        "Próximamente en el App Store",
        "Próximamente en el App Store",
        "Bientôt sur l'App Store",
        "Presto sull'App Store",
        "App Store にまもなく登場",
        "곧 App Store에 출시",
        "Binnenkort in de App Store",
        "Em breve na App Store",
        "即将上架 App Store"),

    "Free. iPhone, iOS 17 and later. One optional purchase, no subscription.": (
        "Kostenlos. iPhone, iOS 17 und neuer. Ein optionaler Kauf, kein Abo.",
        "Gratis. iPhone, iOS 17 o posterior. Una compra opcional, sin suscripción.",
        "Gratis. iPhone, iOS 17 o posterior. Una compra opcional, sin suscripción.",
        "Gratuit. iPhone, iOS 17 ou version ultérieure. Un achat facultatif, pas d'abonnement.",
        "Gratis. iPhone, iOS 17 o successivo. Un acquisto facoltativo, nessun abbonamento.",
        "無料。iPhone、iOS 17 以降。任意の購入がひとつだけ、サブスクリプションはありません。",
        "무료. iPhone, iOS 17 이상. 선택 구매 하나뿐, 구독 없음.",
        "Gratis. iPhone, iOS 17 en later. Eén optionele aankoop, geen abonnement.",
        "Grátis. iPhone, iOS 17 ou posterior. Uma compra opcional, sem assinatura.",
        "免费。iPhone，iOS 17 及以上。只有一项可选内购，没有订阅。"),

    # ------------------------------------------------------------- the argument

    "Why it is green and not gray": (
        "Warum es Grün wird und nicht Grau",
        "Por qué sale verde y no gris",
        "Por qué sale verde y no gris",
        "Pourquoi c'est vert et pas gris",
        "Perché viene verde e non grigio",
        "なぜ灰色ではなく緑になるのか",
        "왜 회색이 아니라 초록인가",
        "Waarom het groen wordt en niet grijs",
        "Por que fica verde e não cinza",
        "为什么是绿色，而不是灰色"),

    "A screen adds light. Red, green and blue emitters sum, so blue light plus yellow light gives "
    "you\n  something pale and washed out. Paint does the opposite. Every pigment": (
        "Ein Bildschirm addiert Licht. Rote, grüne und blaue Emitter summieren sich, also ergibt "
        "blaues Licht plus gelbes Licht etwas Blasses, Ausgewaschenes. Farbe macht das Gegenteil. "
        "Jedes Pigment",
        "Una pantalla suma luz. Los emisores rojo, verde y azul se suman, así que luz azul más luz "
        "amarilla da algo pálido y lavado. La pintura hace lo contrario. Cada pigmento",
        "Una pantalla suma luz. Los emisores rojo, verde y azul se suman, así que luz azul más luz "
        "amarilla da algo pálido y lavado. La pintura hace lo contrario. Cada pigmento",
        "Un écran ajoute de la lumière. Les émetteurs rouge, vert et bleu s'additionnent : la "
        "lumière bleue plus la lumière jaune donne donc quelque chose de pâle et délavé. La "
        "peinture fait l'inverse. Chaque pigment",
        "Uno schermo somma luce. Gli emettitori rosso, verde e blu si sommano, quindi luce blu più "
        "luce gialla dà qualcosa di pallido e slavato. La vernice fa l'opposto. Ogni pigmento",
        "画面は光を足します。赤・緑・青の発光が足し合わさるので、青い光と黄色い光を足すと、"
        "淡くて色の抜けたものになります。絵の具はその逆です。どの顔料も、スペクトルの一部を",
        "화면은 빛을 더합니다. 빨강, 초록, 파랑 발광이 더해지므로 파란빛에 노란빛을 더하면 "
        "창백하고 바랜 색이 됩니다. 물감은 그 반대입니다. 모든 안료는 스펙트럼의 일부를",
        "Een scherm telt licht op. Rode, groene en blauwe emitters tellen bij elkaar op, dus blauw "
        "licht plus geel licht geeft iets bleeks en uitgewassens. Verf doet het omgekeerde. Elk "
        "pigment",
        "Uma tela soma luz. Os emissores vermelho, verde e azul se somam, então luz azul mais luz "
        "amarela dá algo pálido e lavado. A tinta faz o contrário. Todo pigmento",
        "屏幕做的是加法。红、绿、蓝三种发光叠加，所以蓝光加黄光只会得到一种发白、发灰的颜色。"
        "颜料正好相反。每一种颜料都会"),

    "removes": (
        "entfernt", "elimina", "elimina", "retire", "rimuove",
        "取り除きます", "덜어냅니다", "verwijdert", "remove", "减去"),

    "part of the\n  spectrum, and what reaches your eye is only the light that nothing absorbed. "
    "Blue pigment takes out\n  the red end, yellow pigment takes out the blue end, and the middle "
    "survives. The middle is green.": (
        "einen Teil des Spektrums, und was dein Auge erreicht, ist nur das Licht, das nichts "
        "geschluckt hat. Blaues Pigment nimmt das rote Ende heraus, gelbes Pigment das blaue Ende, "
        "und die Mitte überlebt. Die Mitte ist Grün.",
        "una parte del espectro, y a tu ojo solo llega la luz que nada absorbió. El pigmento azul "
        "se lleva el extremo rojo, el amarillo se lleva el extremo azul, y sobrevive el centro. El "
        "centro es verde.",
        "una parte del espectro, y a tu ojo solo llega la luz que nada absorbió. El pigmento azul "
        "se lleva el extremo rojo, el amarillo se lleva el extremo azul, y sobrevive el centro. El "
        "centro es verde.",
        "une partie du spectre, et ce qui atteint votre œil n'est que la lumière que rien n'a "
        "absorbée. Le pigment bleu retire l'extrémité rouge, le pigment jaune retire l'extrémité "
        "bleue, et le milieu survit. Le milieu, c'est le vert.",
        "una parte dello spettro, e all'occhio arriva soltanto la luce che nulla ha assorbito. Il "
        "pigmento blu toglie l'estremo rosso, quello giallo toglie l'estremo blu, e sopravvive il "
        "centro. Il centro è verde.",
        "。目に届くのは、何にも吸われずに残った光だけです。青い顔料は赤側を、黄色い顔料は青側を"
        "取り去り、真ん中が残ります。その真ん中が緑です。",
        ". 눈에 닿는 것은 아무것도 흡수하지 않은 빛뿐입니다. 파란 안료는 빨강 쪽을, 노란 안료는 "
        "파랑 쪽을 걷어내고 가운데가 남습니다. 그 가운데가 초록입니다.",
        "een deel van het spectrum, en wat je oog bereikt is alleen het licht dat niets heeft "
        "opgeslokt. Blauw pigment haalt het rode uiteinde weg, geel pigment het blauwe, en het "
        "midden blijft over. Het midden is groen.",
        "uma parte do espectro, e o que chega ao seu olho é só a luz que nada absorveu. O pigmento "
        "azul tira a ponta vermelha, o amarelo tira a ponta azul, e o meio sobrevive. O meio é "
        "verde.",
        "光谱里的一段，最后进到眼睛里的，只剩没有被任何颜料吸收掉的那部分光。蓝颜料吃掉红的那一"
        "端，黄颜料吃掉蓝的那一端，中间被留了下来。中间就是绿色。"),

    "Most color games blend two RGB values and hand you mud. Dollop keeps every pigment as sixteen\n"
    "  reflectance readings from 400 to 700 nanometers and mixes them under Kubelka-Munk theory, "
    "which is\n  the approximation the paint industry uses to predict a batch before anyone stirs "
    "it. The ratio\n  matters and the order does not: two parts blue to one part yellow lands "
    "somewhere different from\n  one to one, exactly as it would on a palette.": (
        "Die meisten Farbspiele überblenden zwei RGB-Werte und geben dir Matsch zurück. Dollop hält "
        "jedes Pigment als sechzehn Reflexionswerte von 400 bis 700 Nanometern und mischt sie nach "
        "der Kubelka-Munk-Theorie, mit der die Farbenindustrie eine Charge vorhersagt, bevor "
        "jemand rührt. Das Verhältnis zählt, die Reihenfolge nicht: zwei Teile Blau auf einen Teil "
        "Gelb landen woanders als eins zu eins, genau wie auf einer Palette.",
        "La mayoría de los juegos de color funden dos valores RGB y te devuelven barro. Dollop "
        "guarda cada pigmento como dieciséis lecturas de reflectancia de 400 a 700 nanómetros y "
        "las mezcla con la teoría de Kubelka-Munk, la aproximación que usa la industria de la "
        "pintura para predecir un lote antes de que nadie remueva nada. La proporción importa y el "
        "orden no: dos partes de azul por una de amarillo caen en un sitio distinto que uno a uno, "
        "igual que en una paleta.",
        "La mayoría de los juegos de color funden dos valores RGB y te devuelven lodo. Dollop "
        "guarda cada pigmento como dieciséis lecturas de reflectancia de 400 a 700 nanómetros y "
        "las mezcla con la teoría de Kubelka-Munk, la aproximación que usa la industria de la "
        "pintura para predecir un lote antes de que alguien lo revuelva. La proporción importa y el "
        "orden no: dos partes de azul por una de amarillo caen en un lugar distinto que uno a uno, "
        "igual que en una paleta.",
        "La plupart des jeux de couleur fondent deux valeurs RVB et vous rendent de la boue. "
        "Dollop garde chaque pigment sous forme de seize mesures de réflectance de 400 à 700 "
        "nanomètres et les mélange selon la théorie de Kubelka-Munk, l'approximation dont "
        "l'industrie de la peinture se sert pour prévoir un lot avant que quiconque ne remue. Le "
        "rapport compte, l'ordre non : deux parts de bleu pour une de jaune n'arrivent pas au même "
        "endroit qu'une pour une, exactement comme sur une palette.",
        "La maggior parte dei giochi di colore sfuma due valori RGB e ti restituisce fango. Dollop "
        "tiene ogni pigmento come sedici letture di riflettanza da 400 a 700 nanometri e le mescola "
        "secondo la teoria di Kubelka-Munk, l'approssimazione che l'industria della vernice usa per "
        "prevedere una partita prima che qualcuno la mescoli. Il rapporto conta e l'ordine no: due "
        "parti di blu per una di giallo finiscono altrove rispetto a uno a uno, esattamente come su "
        "una tavolozza.",
        "たいていの色ゲームは RGB のふたつの値をブレンドして、濁った色を返します。Dollop は"
        "どの顔料も 400 から 700 ナノメートルまでの十六個の反射率として持ち、クベルカ・ムンク"
        "理論で混ぜます。塗料の業界が、実際にかき混ぜる前に仕上がりを予測するのに使っている近似"
        "です。比率は効き、順序は効きません。青二に対して黄一は、一対一とは違うところに着地"
        "します。パレットの上とまったく同じです。",
        "대부분의 색 게임은 RGB 값 두 개를 섞어 탁한 색을 돌려줍니다. Dollop은 모든 안료를 "
        "400에서 700나노미터까지 열여섯 개의 반사율로 가지고 있고, 쿠벨카-뭉크 이론으로 "
        "섞습니다. 페인트 업계가 실제로 젓기 전에 결과를 예측할 때 쓰는 근사입니다. 비율은 "
        "영향을 주고 순서는 주지 않습니다. 파랑 둘에 노랑 하나는 일 대 일과 다른 곳에 "
        "떨어집니다. 팔레트 위에서와 똑같이.",
        "De meeste kleurspellen mengen twee RGB-waarden en geven je modder terug. Dollop houdt elk "
        "pigment vast als zestien reflectiemetingen van 400 tot 700 nanometer en mengt ze volgens "
        "de Kubelka-Munk-theorie, de benadering waarmee de verfindustrie een charge voorspelt "
        "voordat iemand roert. De verhouding doet ertoe, de volgorde niet: twee delen blauw op één "
        "deel geel komt ergens anders uit dan één op één, precies zoals op een palet.",
        "A maioria dos jogos de cor mescla dois valores RGB e te devolve lama. O Dollop guarda cada "
        "pigmento como dezesseis leituras de refletância de 400 a 700 nanômetros e as mistura pela "
        "teoria de Kubelka-Munk, a aproximação que a indústria de tintas usa para prever um lote "
        "antes de alguém mexer. A proporção importa e a ordem não: duas partes de azul para uma de "
        "amarelo cai em outro lugar que não um para um, exatamente como numa paleta.",
        "多数颜色游戏只是把两个 RGB 值混在一起，给你一坨浑浊。Dollop 把每一种颜料都存成从 400 到 "
        "700 纳米的十六个反射率读数，再按库贝尔卡-蒙克理论去混合，那正是涂料行业在真正搅拌之前"
        "用来预测一批漆的近似方法。比例有影响，先后没有：两份蓝配一份黄，落点和一比一并不相同，"
        "和在调色板上完全一样。"),

    # ---------------------------------------------------------------- the modes

    "Five ways to play": (
        "Fünf Arten zu spielen",
        "Cinco formas de jugar",
        "Cinco formas de jugar",
        "Cinq façons de jouer",
        "Cinque modi di giocare",
        "五つの遊び方",
        "다섯 가지 플레이 방식",
        "Vijf manieren om te spelen",
        "Cinco formas de jogar",
        "五种玩法"),

    "Zen": ("Zen", "Zen", "Zen", "Zen", "Zen", "禅", "젠", "Zen", "Zen", "禅"),

    "Colors one after another, for as long as you want. Nothing is timed and nothing is scored.": (
        "Ein Farbton nach dem anderen, so lange du willst. Nichts wird gestoppt und nichts "
        "gewertet.",
        "Colores uno tras otro, todo el tiempo que quieras. Nada se cronometra y nada se puntúa.",
        "Colores uno tras otro, todo el tiempo que quieras. Nada se cronometra y nada se puntúa.",
        "Des couleurs l'une après l'autre, aussi longtemps que vous voulez. Rien n'est "
        "chronométré, rien n'est noté.",
        "Colori uno dopo l'altro, per tutto il tempo che vuoi. Niente è cronometrato e niente è "
        "valutato.",
        "色がひとつずつ、好きなだけ続きます。時間も計られず、点もつきません。",
        "색이 하나씩 계속 이어집니다, 원하는 만큼. 시간도 재지 않고 점수도 없습니다.",
        "Kleuren na elkaar, zolang je wilt. Er wordt niets geklokt en niets beoordeeld.",
        "Cores uma depois da outra, pelo tempo que você quiser. Nada é cronometrado e nada é "
        "pontuado.",
        "一个接一个的颜色，想调多久就调多久。不计时，也不打分。"),

    "Daily": (
        "Täglich", "Diario", "Diario", "Quotidien", "Quotidiano",
        "デイリー", "데일리", "Dagelijks", "Diário", "每日"),

    "One color a day, the same one for everybody, worked out on your phone from the date. There\n"
    "      are five hundred and fifty five of them, spaced far enough apart that no two days feel "
    "like\n      the same puzzle.": (
        "Ein Farbton pro Tag, für alle derselbe, auf deinem Telefon aus dem Datum errechnet. Es "
        "sind fünfhundertfünfundfünfzig, weit genug voneinander entfernt, dass sich keine zwei Tage "
        "wie dasselbe Rätsel anfühlen.",
        "Un color al día, el mismo para todo el mundo, calculado en tu teléfono a partir de la "
        "fecha. Hay quinientos cincuenta y cinco, lo bastante separados como para que no haya dos "
        "días que se sientan igual.",
        "Un color al día, el mismo para todos, calculado en tu teléfono a partir de la fecha. Hay "
        "quinientos cincuenta y cinco, lo bastante separados como para que no haya dos días que se "
        "sientan igual.",
        "Une couleur par jour, la même pour tout le monde, calculée sur votre téléphone à partir de "
        "la date. Il y en a cinq cent cinquante-cinq, assez éloignées les unes des autres pour que "
        "deux jours ne se ressemblent jamais.",
        "Un colore al giorno, lo stesso per tutti, calcolato sul tuo telefono a partire dalla data. "
        "Sono cinquecentocinquantacinque, abbastanza distanti perché due giorni non sembrino mai lo "
        "stesso enigma.",
        "一日にひとつの色。誰にとっても同じ色で、日付から端末の中で計算されます。全部で五百五十"
        "五色あり、十分に離れているので、同じ日が二度あるようには感じません。",
        "하루에 색 하나. 모두에게 같은 색이고, 날짜로부터 기기 안에서 계산됩니다. 555개가 있고 "
        "서로 충분히 떨어져 있어서 어느 이틀도 같은 문제처럼 느껴지지 않습니다.",
        "Eén kleur per dag, voor iedereen dezelfde, op je telefoon uit de datum berekend. Het zijn "
        "er vijfhonderdvijfenvijftig, ver genoeg uit elkaar dat geen twee dagen als dezelfde puzzel "
        "aanvoelen.",
        "Uma cor por dia, a mesma para todo mundo, calculada no seu telefone a partir da data. São "
        "quinhentas e cinquenta e cinco, distantes o bastante para que dois dias nunca pareçam o "
        "mesmo quebra-cabeça.",
        "每天一个颜色，所有人拿到的都一样，由日期在你自己的手机上算出来。一共五百五十五个，"
        "彼此拉得够开，不会有两天像是同一道题。"),

    "Blind": (
        "Blind", "A ciegas", "A ciegas", "À l'aveugle", "Alla cieca",
        "ブラインド", "블라인드", "Blind", "Às cegas", "盲配"),

    "A few seconds to look, then the target is covered and you mix it from memory. One peek, ten\n"
    "      seconds in.": (
        "Ein paar Sekunden hinsehen, dann wird das Ziel abgedeckt und du mischst aus dem "
        "Gedächtnis. Ein Blick, nach zehn Sekunden.",
        "Unos segundos para mirar y luego se tapa el objetivo: lo mezclas de memoria. Un vistazo, a "
        "los diez segundos.",
        "Unos segundos para mirar y luego se tapa el objetivo: lo mezclas de memoria. Un vistazo, a "
        "los diez segundos.",
        "Quelques secondes pour regarder, puis la cible est masquée et vous la mélangez de "
        "mémoire. Un coup d'œil, au bout de dix secondes.",
        "Qualche secondo per guardare, poi l'obiettivo viene coperto e lo mescoli a memoria. Una "
        "sbirciata, dopo dieci secondi.",
        "数秒だけ見せて、目標は隠れます。あとは記憶だけで混ぜます。十秒後に、一度だけ覗けます。",
        "몇 초만 보여준 뒤 목표가 가려지고, 기억만으로 섞습니다. 10초 뒤에 딱 한 번 엿볼 수 "
        "있습니다.",
        "Een paar seconden kijken, dan wordt het doel afgedekt en meng je uit je hoofd. Één blik, "
        "na tien seconden.",
        "Alguns segundos para olhar, aí o alvo é coberto e você mistura de memória. Uma espiada, "
        "dez segundos depois.",
        "只给你几秒钟看，然后目标被盖住，靠记忆去调。十秒之后，可以偷看一次。"),

    "Included in the unlock": (
        "Im Kauf enthalten",
        "Incluido en el desbloqueo",
        "Incluido en el desbloqueo",
        "Compris dans le déverrouillage",
        "Incluso nello sblocco",
        "アンロックに含まれます",
        "잠금 해제에 포함",
        "Inbegrepen bij de ontgrendeling",
        "Incluído no desbloqueio",
        "包含在解锁内容中"),

    "Precise": (
        "Präzise", "Preciso", "Preciso", "Précis", "Preciso",
        "精密", "정밀", "Precies", "Preciso", "精准"),

    "The same colors, held to a tolerance most eyes cannot resolve. This is the one that will\n"
    "      keep you there.": (
        "Dieselben Farben, aber mit einer Toleranz, die die meisten Augen nicht mehr auflösen. Das "
        "ist der Modus, der dich festhält.",
        "Los mismos colores, con una tolerancia que la mayoría de los ojos no distingue. Este es el "
        "que te retiene.",
        "Los mismos colores, con una tolerancia que la mayoría de los ojos no distingue. Este es el "
        "que te retiene.",
        "Les mêmes couleurs, avec une tolérance que la plupart des yeux ne savent pas départager. "
        "C'est celui qui vous retient.",
        "Gli stessi colori, con una tolleranza che la maggior parte degli occhi non riesce a "
        "distinguere. È questo che ti tiene lì.",
        "同じ色を、ほとんどの目には見分けられない許容差で合わせます。いちばん長く居座ることに"
        "なるのはこれです。",
        "같은 색을, 대부분의 눈으로는 구분하지 못하는 허용 오차까지 맞춥니다. 오래 붙잡아 두는 "
        "쪽은 이 모드입니다.",
        "Dezelfde kleuren, maar met een tolerantie die de meeste ogen niet meer kunnen "
        "onderscheiden. Dit is degene die je vasthoudt.",
        "As mesmas cores, com uma tolerância que a maioria dos olhos não consegue distinguir. Este "
        "é o que segura você ali.",
        "还是那些颜色，只是容差收到大多数眼睛分辨不出的程度。会把你留住的就是这一个。"),

    "From Life": (
        "Nach der Natur", "Del natural", "Del natural", "D'après nature", "Dal vero",
        "実物から", "실물에서", "Naar de natuur", "Do natural", "写生"),

    "Photograph anything, point at a color in it, and mix that. When no paint on the tray can\n"
    "      reach it, the app says so instead of quietly substituting something close.": (
        "Fotografiere irgendetwas, zeig auf eine Farbe darin und mische die. Wenn keine Farbe auf "
        "der Palette dorthin reicht, sagt die App das, statt stillschweigend etwas Ähnliches "
        "einzusetzen.",
        "Fotografía cualquier cosa, señala un color dentro y mézclalo. Cuando ninguna pintura de la "
        "bandeja puede llegar hasta él, la app lo dice en vez de sustituirlo en silencio por algo "
        "parecido.",
        "Fotografía cualquier cosa, señala un color dentro y mézclalo. Cuando ninguna pintura de la "
        "bandeja puede llegar hasta él, la app lo dice en vez de sustituirlo en silencio por algo "
        "parecido.",
        "Photographiez n'importe quoi, désignez une couleur dedans et mélangez-la. Quand aucune "
        "peinture du plateau ne peut l'atteindre, l'app le dit au lieu d'y substituer discrètement "
        "quelque chose d'approchant.",
        "Fotografa qualsiasi cosa, indica un colore al suo interno e mescola quello. Quando nessuna "
        "vernice del vassoio riesce ad arrivarci, l'app lo dice invece di sostituirlo in silenzio "
        "con qualcosa di simile.",
        "何でも写真に撮り、その中の色を指して、それを混ぜます。トレイのどの絵の具でも届かない色"
        "なら、近い色をこっそり差し替えたりせず、届かないと言います。",
        "무엇이든 사진으로 찍고, 그 안의 색을 짚어서 그 색을 섞습니다. 트레이의 어떤 물감으로도 "
        "닿을 수 없는 색이면, 비슷한 색으로 슬쩍 바꾸지 않고 닿을 수 없다고 말해 줍니다.",
        "Fotografeer wat je wilt, wijs een kleur erin aan en meng die. Als geen verf op het "
        "palet erbij kan, zegt de app dat, in plaats van er stilletjes iets vergelijkbaars voor in "
        "de plaats te zetten.",
        "Fotografe qualquer coisa, aponte para uma cor dentro dela e misture aquilo. Quando nenhuma "
        "tinta da bandeja alcança, o app avisa em vez de trocar em silêncio por algo parecido.",
        "拍下任何东西，指着照片里的某个颜色，把它调出来。如果盘里的颜料根本够不到那个颜色，"
        "App 会直说，而不是悄悄换一个接近的。"),

    "Zen and Daily are free forever, and they are whole modes rather than a\n  sample of one. A "
    "single purchase of": (
        "Zen und Täglich sind für immer kostenlos, und sie sind vollständige Modi, keine Kostprobe "
        "davon. Ein einziger Kauf von",
        "Zen y Diario son gratis para siempre, y son modos completos, no una muestra de uno. Una "
        "sola compra de",
        "Zen y Diario son gratis para siempre, y son modos completos, no una muestra de uno. Una "
        "sola compra de",
        "Zen et Quotidien sont gratuits pour toujours, et ce sont des modes entiers, pas un "
        "échantillon. Un seul achat de",
        "Zen e Quotidiano sono gratis per sempre, e sono modalità intere, non l'assaggio di una. "
        "Un solo acquisto di",
        "禅とデイリーはずっと無料で、しかも試供品ではなく丸ごとひとつのモードです。",
        "젠과 데일리는 영원히 무료이고, 맛보기가 아니라 온전한 모드입니다. 단 한 번의",
        "Zen en Dagelijks zijn voor altijd gratis, en het zijn hele modi, geen proefje ervan. Eén "
        "aankoop van",
        "Zen e Diário são grátis para sempre, e são modos inteiros, não uma amostra de um. Uma "
        "única compra de",
        "禅和每日永远免费，而且是完整的模式，不是试玩。只需一次"),

    "unlocks the other three, paid once and never\n  again. No subscription, no advertising, and "
    "nothing that runs out and asks you to wait.": (
        "schaltet die anderen drei frei, einmal bezahlt und nie wieder. Kein Abo, keine Werbung "
        "und nichts, was zur Neige geht und dich warten lässt.",
        "desbloquea los otros tres, pagado una vez y nunca más. Sin suscripción, sin publicidad y "
        "sin nada que se agote y te haga esperar.",
        "desbloquea los otros tres, pagado una vez y nunca más. Sin suscripción, sin publicidad y "
        "sin nada que se acabe y te haga esperar.",
        "déverrouille les trois autres, payé une fois et plus jamais. Pas d'abonnement, pas de "
        "publicité, et rien qui s'épuise et vous fasse attendre.",
        "sblocca gli altri tre, pagato una volta e mai più. Nessun abbonamento, nessuna pubblicità "
        "e niente che si esaurisca e ti faccia aspettare.",
        "を一度だけ支払えば、残りの三つが開きます。二度目はありません。サブスクリプションも広告"
        "もなく、切れて待たされるものもありません。",
        "구매로 나머지 셋이 열립니다. 한 번 내면 그걸로 끝입니다. 구독도 광고도 없고, 다 써 버려서 "
        "기다리게 만드는 것도 없습니다.",
        "ontgrendelt de andere drie, één keer betaald en nooit meer. Geen abonnement, geen "
        "advertenties, en niets dat opraakt en je laat wachten.",
        "desbloqueia os outros três, pago uma vez e nunca mais. Sem assinatura, sem publicidade e "
        "sem nada que acabe e peça que você espere.",
        "购买，就能解锁另外三个，付一次，不再有第二次。没有订阅，没有广告，也没有会耗尽、"
        "逼你等待的东西。"),
}
