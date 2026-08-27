"""Harmony Palette page, part A: head, hero, and the opening argument.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The English argues rather than sells. Kept that way: several of these languages will inflate a
plain sentence into marketing if you let them, and that would be a mistranslation even where every
word was right. Prices stay in dollars because they are dollars; writing "2,99 $" would imply a
local price the App Store is not going to charge.
"""

T = {
    "Harmony Palette: Color Wheel": (
        "Harmony Palette: Farbkreis", "Harmony Palette: rueda de color",
        "Harmony Palette: rueda de color", "Harmony Palette : roue chromatique",
        "Harmony Palette: ruota dei colori", "Harmony Palette: カラーホイール",
        "Harmony Palette: 색상환", "Harmony Palette: kleurenwiel",
        "Harmony Palette: roda de cores", "Harmony Palette：色轮"),
    "Palette App for iPhone and iPad": (
        "Paletten-App für iPhone und iPad", "app de paletas para iPhone y iPad",
        "app de paletas para iPhone y iPad", "application de palettes pour iPhone et iPad",
        "app di palette per iPhone e iPad", "iPhone と iPad のためのパレットアプリ",
        "iPhone과 iPad를 위한 팔레트 앱", "palet-app voor iPhone en iPad",
        "app de paletas para iPhone e iPad", "为 iPhone 和 iPad 打造的调色板应用"),
    "A color harmony app for designers. Eight harmony types on an interactive RGB and RYB color wheel, 160 curated palettes, a WCAG contrast checker, color blindness simulation, and export to PDF, SVG, SwiftUI, UIKit, CSS and Tailwind. In eleven languages, color names included.": (
        "Eine Farbharmonie-App für Gestalterinnen und Gestalter. Acht Harmonietypen auf einem "
        "interaktiven RGB- und RYB-Farbkreis, 160 kuratierte Paletten, ein WCAG-Kontrastprüfer, "
        "Farbenblindheitssimulation und Export nach PDF, SVG, SwiftUI, UIKit, CSS und Tailwind. "
        "In elf Sprachen, Farbnamen inklusive.",
        "Una app de armonía de color para diseñadores. Ocho tipos de armonía en una rueda de color "
        "RGB y RYB interactiva, 160 paletas seleccionadas, un comprobador de contraste WCAG, "
        "simulación de daltonismo y exportación a PDF, SVG, SwiftUI, UIKit, CSS y Tailwind. En "
        "once idiomas, nombres de color incluidos.",
        "Una app de armonía de color para diseñadores. Ocho tipos de armonía en una rueda de color "
        "RGB y RYB interactiva, 160 paletas seleccionadas, un verificador de contraste WCAG, "
        "simulación de daltonismo y exportación a PDF, SVG, SwiftUI, UIKit, CSS y Tailwind. En "
        "once idiomas, nombres de color incluidos.",
        "Une application d'harmonie des couleurs pour les designers. Huit types d'harmonie sur une "
        "roue chromatique RVB et RJB interactive, 160 palettes sélectionnées, un vérificateur de "
        "contraste WCAG, une simulation du daltonisme et l'export vers PDF, SVG, SwiftUI, UIKit, "
        "CSS et Tailwind. En onze langues, noms de couleurs compris.",
        "Un'app di armonia cromatica per designer. Otto tipi di armonia su una ruota dei colori RGB "
        "e RYB interattiva, 160 palette selezionate, un controllo del contrasto WCAG, la "
        "simulazione del daltonismo e l'esportazione in PDF, SVG, SwiftUI, UIKit, CSS e Tailwind. "
        "In undici lingue, nomi dei colori compresi.",
        "デザイナーのための配色アプリ。RGB と RYB の対話的なカラーホイール上に 8 種類の調和、"
        "厳選された 160 のパレット、WCAG コントラストチェッカー、色覚シミュレーション、そして "
        "PDF、SVG、SwiftUI、UIKit、CSS、Tailwind への書き出し。11 の言語で、色名まで。",
        "디자이너를 위한 색 조화 앱. RGB와 RYB 색상환에서 고를 수 있는 8가지 조화, 엄선된 160개의 "
        "팔레트, WCAG 명도 대비 검사기, 색각 이상 시뮬레이션, 그리고 PDF, SVG, SwiftUI, UIKit, "
        "CSS, Tailwind로의 내보내기. 11개 언어로, 색 이름까지.",
        "Een kleurharmonie-app voor ontwerpers. Acht harmonietypes op een interactief RGB- en "
        "RYB-kleurenwiel, 160 samengestelde paletten, een WCAG-contrastchecker, "
        "kleurenblindheidssimulatie en export naar PDF, SVG, SwiftUI, UIKit, CSS en Tailwind. "
        "In elf talen, kleurnamen inbegrepen.",
        "Um app de harmonia de cores para designers. Oito tipos de harmonia numa roda de cores RGB "
        "e RYB interativa, 160 paletas selecionadas, um verificador de contraste WCAG, simulação "
        "de daltonismo e exportação para PDF, SVG, SwiftUI, UIKit, CSS e Tailwind. Em onze "
        "idiomas, nomes de cores inclusos.",
        "为设计师打造的配色应用。可交互的 RGB 与 RYB 色轮上有 8 种配色关系、精选的 160 套调色板、"
        "WCAG 对比度检查器、色觉模拟，以及导出为 PDF、SVG、SwiftUI、UIKit、CSS 和 Tailwind。"
        "支持 11 种语言，连色名一起。"),
    "Harmony Palette: Color Wheel & Palette App for iPhone": (
        "Harmony Palette: Farbkreis- und Paletten-App fürs iPhone",
        "Harmony Palette: rueda de color y paletas para iPhone",
        "Harmony Palette: rueda de color y paletas para iPhone",
        "Harmony Palette : roue chromatique et palettes pour iPhone",
        "Harmony Palette: ruota dei colori e palette per iPhone",
        "Harmony Palette: iPhone のカラーホイールとパレットアプリ",
        "Harmony Palette: iPhone용 색상환과 팔레트 앱",
        "Harmony Palette: kleurenwiel en palet-app voor iPhone",
        "Harmony Palette: roda de cores e paletas para iPhone",
        "Harmony Palette：iPhone 上的色轮与调色板应用"),
    "Where color gets along. Eight harmony types, 160 curated palettes, a WCAG contrast checker, and export to code. In eleven languages.": (
        "Wo Farben miteinander auskommen. Acht Harmonietypen, 160 kuratierte Paletten, ein "
        "WCAG-Kontrastprüfer und Export als Code. In elf Sprachen.",
        "Donde los colores se llevan bien. Ocho tipos de armonía, 160 paletas seleccionadas, un "
        "comprobador de contraste WCAG y exportación a código. En once idiomas.",
        "Donde los colores se llevan bien. Ocho tipos de armonía, 160 paletas seleccionadas, un "
        "verificador de contraste WCAG y exportación a código. En once idiomas.",
        "Là où les couleurs s'entendent. Huit types d'harmonie, 160 palettes sélectionnées, un "
        "vérificateur de contraste WCAG et l'export vers du code. En onze langues.",
        "Dove i colori vanno d'accordo. Otto tipi di armonia, 160 palette selezionate, un "
        "controllo del contrasto WCAG e l'esportazione in codice. In undici lingue.",
        "色どうしがうまくやっていく場所。8 種類の調和、厳選された 160 のパレット、WCAG "
        "コントラストチェッカー、そしてコードへの書き出し。11 の言語で。",
        "색끼리 잘 어울리는 곳. 8가지 조화, 엄선된 160개의 팔레트, WCAG 명도 대비 검사기, 그리고 "
        "코드로의 내보내기. 11개 언어로.",
        "Waar kleuren met elkaar overweg kunnen. Acht harmonietypes, 160 samengestelde paletten, "
        "een WCAG-contrastchecker en export naar code. In elf talen.",
        "Onde as cores se entendem. Oito tipos de harmonia, 160 paletas selecionadas, um "
        "verificador de contraste WCAG e exportação para código. Em onze idiomas.",
        "让颜色相处得来的地方。8 种配色关系、精选的 160 套调色板、WCAG 对比度检查器，"
        "以及导出为代码。支持 11 种语言。"),
    "The Harmony Palette title and the line where color gets along, over a row of color swatches, with flat cut-paper shapes and a googly-eyed green blob.": (
        "Der Titel Harmony Palette und die Zeile wo Farben miteinander auskommen, über einer Reihe "
        "von Farbfeldern, mit flachen Scherenschnittformen und einem grünen Klecks mit Kulleraugen.",
        "El título Harmony Palette y la frase donde los colores se llevan bien, sobre una fila de "
        "muestras de color, con formas planas de papel recortado y una mancha verde con ojos "
        "saltones.",
        "El título Harmony Palette y la frase donde los colores se llevan bien, sobre una fila de "
        "muestras de color, con formas planas de papel recortado y una mancha verde con ojos "
        "saltones.",
        "Le titre Harmony Palette et la phrase là où les couleurs s'entendent, au-dessus d'une "
        "rangée d'échantillons de couleur, avec des formes plates en papier découpé et une tache "
        "verte aux yeux mobiles.",
        "Il titolo Harmony Palette e la frase dove i colori vanno d'accordo, sopra una fila di "
        "campioni di colore, con forme piatte di carta ritagliata e una macchia verde con occhi "
        "mobili.",
        "Harmony Palette のタイトルと、色どうしがうまくやっていくという一行。カラースウォッチの列の"
        "上に置かれ、切り紙のような平らな図形と、目玉のついた緑の塊が添えられている。",
        "Harmony Palette라는 제목과 색끼리 잘 어울린다는 문구가 색상 견본 줄 위에 놓여 있고, 평평한 "
        "종이 오림 도형과 눈알이 달린 초록색 덩어리가 함께 있다.",
        "De titel Harmony Palette en de regel waar kleuren met elkaar overweg kunnen, boven een rij "
        "kleurstalen, met platte uitgeknipte vormen en een groene klodder met wiebeloogjes.",
        "O título Harmony Palette e a frase onde as cores se entendem, sobre uma fileira de "
        "amostras de cor, com formas planas de papel recortado e uma mancha verde de olhos "
        "esbugalhados.",
        "Harmony Palette 的标题和「让颜色相处得来」这行字，压在一排色块之上，"
        "旁边是剪纸般的平面图形和一个长着活动眼珠的绿色团块。"),
    "Where color gets along. Eight harmony types, 160 curated palettes, a contrast checker, and export to code.": (
        "Wo Farben miteinander auskommen. Acht Harmonietypen, 160 kuratierte Paletten, ein "
        "Kontrastprüfer und Export als Code.",
        "Donde los colores se llevan bien. Ocho tipos de armonía, 160 paletas seleccionadas, un "
        "comprobador de contraste y exportación a código.",
        "Donde los colores se llevan bien. Ocho tipos de armonía, 160 paletas seleccionadas, un "
        "verificador de contraste y exportación a código.",
        "Là où les couleurs s'entendent. Huit types d'harmonie, 160 palettes sélectionnées, un "
        "vérificateur de contraste et l'export vers du code.",
        "Dove i colori vanno d'accordo. Otto tipi di armonia, 160 palette selezionate, un "
        "controllo del contrasto e l'esportazione in codice.",
        "色どうしがうまくやっていく場所。8 種類の調和、厳選された 160 のパレット、"
        "コントラストチェッカー、そしてコードへの書き出し。",
        "색끼리 잘 어울리는 곳. 8가지 조화, 엄선된 160개의 팔레트, 명도 대비 검사기, 그리고 코드로의 "
        "내보내기.",
        "Waar kleuren met elkaar overweg kunnen. Acht harmonietypes, 160 samengestelde paletten, "
        "een contrastchecker en export naar code.",
        "Onde as cores se entendem. Oito tipos de harmonia, 160 paletas selecionadas, um "
        "verificador de contraste e exportação para código.",
        "让颜色相处得来的地方。8 种配色关系、精选的 160 套调色板、对比度检查器，以及导出为代码。"),
    "where color gets along.": (
        "wo Farben miteinander auskommen.", "donde los colores se llevan bien.",
        "donde los colores se llevan bien.", "là où les couleurs s'entendent.",
        "dove i colori vanno d'accordo.", "色どうしがうまくやっていく場所。",
        "색끼리 잘 어울리는 곳.", "waar kleuren met elkaar overweg kunnen.",
        "onde as cores se entendem.", "让颜色相处得来的地方。"),
    "A color wheel you can actually work on, 160 palettes worth stealing from,\n      and the accessibility tools you were going to skip. Built for people who pick colors for\n      a living, and for anyone who just likes them.": (
        "Ein Farbkreis, an dem sich wirklich arbeiten lässt, 160 Paletten, bei denen sich Klauen "
        "lohnt, und die Barrierefreiheits-Werkzeuge, die Sie überspringen wollten. Gebaut für "
        "Menschen, die beruflich Farben wählen, und für alle, die Farben einfach mögen.",
        "Una rueda de color en la que se puede trabajar de verdad, 160 paletas de las que merece "
        "la pena robar y las herramientas de accesibilidad que ibas a saltarte. Hecha para quienes "
        "eligen colores para ganarse la vida, y para cualquiera a quien simplemente le gusten.",
        "Una rueda de color en la que sí se puede trabajar, 160 paletas de las que vale la pena "
        "robar y las herramientas de accesibilidad que ibas a saltarte. Hecha para quienes eligen "
        "colores para ganarse la vida, y para cualquiera a quien simplemente le gusten.",
        "Une roue chromatique sur laquelle on peut vraiment travailler, 160 palettes dans "
        "lesquelles il vaut la peine de piocher, et les outils d'accessibilité que vous alliez "
        "sauter. Faite pour les gens qui choisissent des couleurs pour vivre, et pour tous ceux "
        "qui les aiment tout simplement.",
        "Una ruota dei colori su cui si può davvero lavorare, 160 palette da cui vale la pena "
        "rubare e gli strumenti di accessibilità che stavi per saltare. Fatta per chi sceglie "
        "colori di mestiere, e per chiunque semplicemente li ami.",
        "本当に作業できるカラーホイール、盗む価値のある 160 のパレット、そして飛ばすつもりだった"
        "アクセシビリティの道具。色を選ぶことを仕事にしている人のために、そして色が好きなだけの人の"
        "ためにも作られています。",
        "실제로 작업할 수 있는 색상환, 훔쳐 올 만한 160개의 팔레트, 그리고 그냥 건너뛰려던 접근성 "
        "도구. 색을 고르는 일로 먹고사는 사람을 위해, 그리고 그저 색을 좋아하는 사람을 위해 "
        "만들었습니다.",
        "Een kleurenwiel waar je echt op kunt werken, 160 paletten waar het de moeite waard is uit "
        "te stelen, en de toegankelijkheidsgereedschappen die je zou overslaan. Gemaakt voor "
        "mensen die voor hun brood kleuren kiezen, en voor iedereen die ze gewoon mooi vindt.",
        "Uma roda de cores em que dá mesmo para trabalhar, 160 paletas das quais vale a pena "
        "roubar e as ferramentas de acessibilidade que você ia pular. Feita para quem escolhe "
        "cores para viver, e para qualquer um que simplesmente goste delas.",
        "一个真的能在上面动手的色轮、160 套值得偷师的调色板，以及你本来打算跳过的无障碍工具。"
        "为靠选色吃饭的人而做，也为只是喜欢颜色的人而做。"),
    "Get it on the App Store": (
        "Im App Store laden", "Consíguela en el App Store", "Consíguela en el App Store",
        "Télécharger dans l'App Store", "Scaricala su App Store", "App Store で入手",
        "App Store에서 받기", "Downloaden in de App Store", "Baixe na App Store",
        "在 App Store 下载"),
    "Free to use. Pro from $2.99/month or $29.99 once.": (
        "Kostenlos nutzbar. Pro ab $2.99 im Monat oder $29.99 einmalig.",
        "Gratis. Pro desde $2.99 al mes o $29.99 una sola vez.",
        "Gratis. Pro desde $2.99 al mes o $29.99 una sola vez.",
        "Gratuite. Pro à partir de $2.99 par mois ou $29.99 une fois pour toutes.",
        "Gratis. Pro da $2.99 al mese o $29.99 una volta sola.",
        "無料で使えます。Pro は月 $2.99 から、または $29.99 の買い切り。",
        "무료로 씁니다. Pro는 월 $2.99부터, 또는 $29.99 한 번.",
        "Gratis te gebruiken. Pro vanaf $2.99 per maand of $29.99 eenmalig.",
        "Grátis. Pro a partir de $2.99 por mês ou $29.99 uma vez só.",
        "免费使用。Pro 每月 $2.99 起，或 $29.99 一次买断。"),
    "color wheel · palettes · contrast · extraction · eleven languages": (
        "Farbkreis · Paletten · Kontrast · Extraktion · elf Sprachen",
        "rueda de color · paletas · contraste · extracción · once idiomas",
        "rueda de color · paletas · contraste · extracción · once idiomas",
        "roue chromatique · palettes · contraste · extraction · onze langues",
        "ruota dei colori · palette · contrasto · estrazione · undici lingue",
        "カラーホイール · パレット · コントラスト · 抽出 · 11 の言語",
        "색상환 · 팔레트 · 명도 대비 · 추출 · 11개 언어",
        "kleurenwiel · paletten · contrast · extractie · elf talen",
        "roda de cores · paletas · contraste · extração · onze idiomas",
        "色轮 · 调色板 · 对比度 · 提取 · 11 种语言"),
    "Color is the subject here,": (
        "Farbe ist hier das Thema,", "Aquí el tema es el color,", "Aquí el tema es el color,",
        "Ici, le sujet, c'est la couleur,", "Qui il soggetto è il colore,",
        "ここでは色が主題であって、", "여기서 주인공은 색이지,",
        "Kleur is hier het onderwerp,", "Aqui o assunto é a cor,", "在这里，颜色是主角，"),
    "not the decoration.": (
        "nicht die Deko.", "no la decoración.", "no la decoración.", "pas la décoration.",
        "non la decorazione.", "飾りではありません。", "장식이 아닙니다.",
        "niet de versiering.", "não a decoração.", "不是装饰。"),
    "Most design tools treat color as a setting: a small square you click, buried in\n      an inspector, on the way to doing something else. Harmony Palette is the opposite kind of\n      program. Color is the whole screen, the interface is loud on purpose, and the point is to\n      spend time with it rather than get past it.": (
        "Die meisten Design-Werkzeuge behandeln Farbe als Einstellung: ein kleines Quadrat zum "
        "Anklicken, vergraben in einem Inspektor, auf dem Weg zu etwas anderem. Harmony Palette "
        "ist das gegenteilige Programm. Farbe ist der ganze Bildschirm, die Oberfläche ist mit "
        "Absicht laut, und es geht darum, Zeit mit ihr zu verbringen statt an ihr vorbei.",
        "La mayoría de las herramientas de diseño tratan el color como un ajuste: un cuadradito en "
        "el que haces clic, enterrado en un inspector, camino de hacer otra cosa. Harmony Palette "
        "es el programa contrario. El color es toda la pantalla, la interfaz es ruidosa a "
        "propósito, y la idea es pasar tiempo con él en vez de dejarlo atrás.",
        "La mayoría de las herramientas de diseño tratan el color como un ajuste: un cuadradito en "
        "el que haces clic, enterrado en un inspector, camino de hacer otra cosa. Harmony Palette "
        "es el programa contrario. El color es toda la pantalla, la interfaz es ruidosa a "
        "propósito, y la idea es pasar tiempo con él en vez de dejarlo atrás.",
        "La plupart des outils de design traitent la couleur comme un réglage : un petit carré sur "
        "lequel on clique, enfoui dans un inspecteur, en route vers autre chose. Harmony Palette "
        "est le programme inverse. La couleur occupe tout l'écran, l'interface est bruyante "
        "exprès, et l'idée est de passer du temps avec elle plutôt que de la dépasser.",
        "La maggior parte degli strumenti di design tratta il colore come un'impostazione: un "
        "quadratino da cliccare, sepolto in un ispettore, mentre vai a fare altro. Harmony Palette "
        "è il programma opposto. Il colore è tutto lo schermo, l'interfaccia è rumorosa di "
        "proposito, e il punto è passarci del tempo invece di superarlo.",
        "たいていのデザインツールは色を設定として扱います。インスペクタの奥に埋もれた、"
        "別の作業に向かう途中でクリックする小さな四角。Harmony Palette はその逆の種類のプログラム"
        "です。色が画面のすべてで、インターフェースはわざと騒がしく、要点は色を通り過ぎることでは"
        "なく色と時間を過ごすことにあります。",
        "대부분의 디자인 도구는 색을 설정으로 다룹니다. 다른 일을 하러 가는 길에 인스펙터 깊숙한 "
        "곳에서 클릭하는 작은 네모 하나. Harmony Palette는 그 반대편의 프로그램입니다. 색이 화면 "
        "전부이고, 인터페이스는 일부러 시끄러우며, 핵심은 색을 지나쳐 가는 것이 아니라 색과 시간을 "
        "보내는 데 있습니다.",
        "De meeste ontwerpgereedschappen behandelen kleur als een instelling: een klein vierkantje "
        "waar je op klikt, begraven in een inspector, op weg naar iets anders. Harmony Palette is "
        "het tegenovergestelde programma. Kleur is het hele scherm, de interface is met opzet "
        "luid, en het gaat erom er tijd mee door te brengen in plaats van eraan voorbij te gaan.",
        "A maioria das ferramentas de design trata a cor como um ajuste: um quadradinho em que "
        "você clica, enterrado num inspetor, a caminho de fazer outra coisa. O Harmony Palette é o "
        "programa oposto. A cor é a tela inteira, a interface é barulhenta de propósito, e a ideia "
        "é passar tempo com ela em vez de passar por ela.",
        "多数设计工具把颜色当作一项设置：埋在检查器深处、你在去做别的事的路上顺手点一下的小方块。"
        "Harmony Palette 是相反的那类程序。颜色就是整个屏幕，界面是故意吵闹的，"
        "重点是与颜色相处，而不是快点绕过它。"),
    "That is a design decision, not an accident. The thick outlines and flat blocks are there\n      because a color needs a hard edge to be judged against. Put a swatch on a soft gradient and\n      you cannot tell what you are looking at. Put it in a black box next to another black box and\n      you can.": (
        "Das ist eine Gestaltungsentscheidung, kein Zufall. Die dicken Konturen und flachen Blöcke "
        "sind da, weil eine Farbe eine harte Kante braucht, an der man sie beurteilen kann. Setzen "
        "Sie ein Farbfeld auf einen weichen Verlauf, und Sie können nicht sagen, was Sie da sehen. "
        "Setzen Sie es in einen schwarzen Kasten neben einen anderen schwarzen Kasten, und Sie "
        "können es.",
        "Es una decisión de diseño, no un accidente. Los contornos gruesos y los bloques planos "
        "están ahí porque un color necesita un borde duro contra el que juzgarlo. Pon una muestra "
        "sobre un degradado suave y no sabrás qué estás mirando. Ponla en una caja negra junto a "
        "otra caja negra y sí lo sabrás.",
        "Es una decisión de diseño, no un accidente. Los contornos gruesos y los bloques planos "
        "están ahí porque un color necesita un borde duro contra el que juzgarlo. Pon una muestra "
        "sobre un degradado suave y no sabrás qué estás mirando. Ponla en una caja negra junto a "
        "otra caja negra y sí lo sabrás.",
        "C'est une décision de design, pas un accident. Les contours épais et les aplats sont là "
        "parce qu'une couleur a besoin d'un bord net pour être jugée. Posez un échantillon sur un "
        "dégradé doux et vous ne saurez pas ce que vous regardez. Posez-le dans une boîte noire à "
        "côté d'une autre boîte noire et vous le saurez.",
        "È una decisione di progetto, non un incidente. I contorni spessi e i blocchi piatti ci "
        "sono perché un colore ha bisogno di un bordo netto contro cui essere giudicato. Metti un "
        "campione su una sfumatura morbida e non capisci cosa stai guardando. Mettilo in una "
        "scatola nera accanto a un'altra scatola nera e lo capisci.",
        "これは事故ではなく設計上の判断です。太い輪郭と平らな面があるのは、色を判断するには硬い縁が"
        "必要だからです。柔らかいグラデーションの上に色見本を置けば、何を見ているのか分からなく"
        "なります。黒い箱に入れて別の黒い箱の隣に置けば、分かります。",
        "이것은 사고가 아니라 설계상의 결정입니다. 두꺼운 윤곽선과 평평한 면이 있는 이유는 색을 "
        "판단하려면 단단한 가장자리가 필요하기 때문입니다. 부드러운 그러데이션 위에 견본을 올려두면 "
        "무엇을 보고 있는지 알 수 없습니다. 검은 상자에 넣어 다른 검은 상자 옆에 두면 알 수 "
        "있습니다.",
        "Dat is een ontwerpbeslissing, geen ongeluk. De dikke contouren en platte blokken zijn er "
        "omdat een kleur een harde rand nodig heeft om tegen beoordeeld te worden. Zet een staal "
        "op een zacht verloop en je ziet niet waar je naar kijkt. Zet het in een zwarte doos naast "
        "een andere zwarte doos en dat lukt wel.",
        "É uma decisão de projeto, não um acidente. Os contornos grossos e os blocos chapados "
        "estão ali porque uma cor precisa de uma borda dura contra a qual ser julgada. Ponha uma "
        "amostra sobre um degradê suave e você não saberá o que está vendo. Ponha numa caixa preta "
        "ao lado de outra caixa preta e saberá.",
        "这是设计决定，不是意外。粗轮廓和平涂色块之所以在这里，是因为要判断一个颜色，"
        "它需要一条硬边。把色块放在柔和的渐变上，你说不清自己在看什么；"
        "把它放进黑框里、挨着另一个黑框，你就说得清了。"),
}
