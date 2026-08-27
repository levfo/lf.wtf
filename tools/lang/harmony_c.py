"""Harmony Palette page, part C: the curated library, the screenshots, export and pricing.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Palette and colour names inside the prose are given in the language the app actually ships them
in, because that is the claim the paragraph is making. Sternennacht, Papayacreme and the Erdtöne
der 70er are what a German reader really sees, and using the English there would quietly disprove
the sentence around it.
"""

T = {
    "a library you didn't": (
        "eine Bibliothek, die Sie", "una biblioteca que no", "una biblioteca que no",
        "une bibliothèque que vous", "una libreria che non", "自分で作らずに済んだ",
        "직접 만들지 않아도 되는", "een bibliotheek die je", "uma biblioteca que você",
        "一座你不必自己"),
    "have to build": (
        "nicht bauen mussten", "tuviste que construir", "tuviste que construir",
        "n'avez pas eu à construire", "hai dovuto costruire", "ライブラリ", "라이브러리",
        "niet hoefde te bouwen", "não teve que construir", "搭建的库"),
    "160 palettes, hand-picked across ten categories: nature, classic art, architecture, fashion,\n      food and drink, geography, decades, abstract, holidays and branding. Starry Night is in there,\n      and Bauhaus, and 70s Earth Tones, and the azure and sand of a Mediterranean coast. Each one\n      carries tags, so you can look for a mood or a season rather than scrolling.": (
        "160 Paletten, von Hand ausgewählt in zehn Kategorien: Natur, klassische Kunst, "
        "Architektur, Mode, Essen und Trinken, Geografie, Jahrzehnte, Abstraktes, Feiertage und "
        "Markenauftritt. Sternennacht ist dabei, und Bauhaus, und die Erdtöne der 70er, und das "
        "Azur und der Sand einer Mittelmeerküste. Jede trägt Schlagwörter, sodass Sie nach einer "
        "Stimmung oder einer Jahreszeit suchen können, statt zu scrollen.",
        "160 paletas, elegidas a mano en diez categorías: naturaleza, arte clásico, arquitectura, "
        "moda, comida y bebida, geografía, décadas, abstracto, festividades y marca. Ahí está "
        "Noche estrellada, y Bauhaus, y los Tonos tierra de los 70, y el azul y la arena de una "
        "costa mediterránea. Cada una lleva etiquetas, para que puedas buscar un ambiente o una "
        "estación en vez de desplazarte.",
        "160 paletas, elegidas a mano en diez categorías: naturaleza, arte clásico, arquitectura, "
        "moda, comida y bebida, geografía, décadas, abstracto, festividades y marca. Ahí está "
        "Noche estrellada, y Bauhaus, y los Tonos tierra de los 70, y el azul y la arena de una "
        "costa mediterránea. Cada una lleva etiquetas, para que puedas buscar un ambiente o una "
        "estación en vez de desplazarte.",
        "160 palettes, choisies à la main dans dix catégories : nature, art classique, "
        "architecture, mode, nourriture et boisson, géographie, décennies, abstrait, fêtes et "
        "identité de marque. La Nuit étoilée y est, et Bauhaus, et les Tons terre des années 70, "
        "et l'azur et le sable d'une côte méditerranéenne. Chacune porte des mots-clés, pour que "
        "vous cherchiez une ambiance ou une saison plutôt que de faire défiler.",
        "160 palette, scelte a mano in dieci categorie: natura, arte classica, architettura, moda, "
        "cibo e bevande, geografia, decenni, astratto, festività e marchio. C'è Notte stellata, e "
        "Bauhaus, e i Toni terra degli anni 70, e l'azzurro e la sabbia di una costa mediterranea. "
        "Ognuna porta delle etichette, così puoi cercare un'atmosfera o una stagione invece di "
        "scorrere.",
        "10 のカテゴリーから手で選んだ 160 のパレット。自然、古典絵画、建築、ファッション、"
        "食べ物と飲み物、地理、年代、抽象、祝祭日、ブランド。星月夜も、Bauhaus も、"
        "70 年代のアースカラーも、地中海沿岸の紺碧と砂の色も入っています。それぞれにタグが付いて"
        "いるので、延々とスクロールする代わりに、気分や季節から探せます。",
        "열 개의 분류에서 손으로 고른 160개의 팔레트. 자연, 고전 미술, 건축, 패션, 음식과 음료, "
        "지리, 시대, 추상, 기념일, 브랜딩. 별이 빛나는 밤도, Bauhaus도, 70년대 어스 톤도, 지중해 "
        "해안의 쪽빛과 모래색도 들어 있습니다. 하나하나에 태그가 붙어 있어서, 하염없이 스크롤하는 "
        "대신 분위기나 계절로 찾을 수 있습니다.",
        "160 paletten, met de hand gekozen in tien categorieën: natuur, klassieke kunst, "
        "architectuur, mode, eten en drinken, geografie, decennia, abstract, feestdagen en "
        "merkidentiteit. De Sterrennacht zit erin, en Bauhaus, en Aardetinten uit de jaren 70, en "
        "het azuur en zand van een mediterrane kust. Elk palet draagt labels, zodat je op een sfeer "
        "of een seizoen kunt zoeken in plaats van te scrollen.",
        "160 paletas, escolhidas a mão em dez categorias: natureza, arte clássica, arquitetura, "
        "moda, comida e bebida, geografia, décadas, abstrato, feriados e marca. A Noite estrelada "
        "está ali, e Bauhaus, e os Tons terrosos dos anos 70, e o azul e a areia de uma costa "
        "mediterrânea. Cada uma leva etiquetas, para você procurar por um clima ou uma estação em "
        "vez de rolar a tela.",
        "从十个类别里手工挑出的 160 套调色板：自然、古典艺术、建筑、时尚、饮食、地理、年代、抽象、"
        "节日和品牌。《星月夜》在里面，Bauhaus 在里面，70 年代大地色在里面，"
        "地中海海岸的天青与沙色也在里面。每一套都带标签，"
        "于是你可以按一种情绪或一个季节去找，而不是一直往下滑。"),
    "There are also 279 named colors, from the ordinary ones through to Papaya Whip and Gainsboro,\n      so a color you land on has a name you can say out loud in a meeting.": (
        "Dazu kommen 279 benannte Farben, von den gewöhnlichen bis zu Papayacreme und Gainsboro, "
        "damit eine Farbe, bei der Sie landen, einen Namen hat, den Sie in einer Besprechung "
        "aussprechen können.",
        "Hay además 279 colores con nombre, desde los corrientes hasta Crema de papaya y "
        "Gainsboro, para que un color en el que aterrizas tenga un nombre que puedas decir en voz "
        "alta en una reunión.",
        "Hay además 279 colores con nombre, desde los corrientes hasta Crema de papaya y "
        "Gainsboro, para que un color en el que aterrizas tenga un nombre que puedas decir en voz "
        "alta en una junta.",
        "Il y a aussi 279 couleurs nommées, des plus ordinaires jusqu'à Crème de papaye et "
        "Gainsboro, pour qu'une couleur sur laquelle vous tombez ait un nom que vous puissiez dire "
        "à voix haute en réunion.",
        "Ci sono anche 279 colori con un nome, da quelli comuni fino a Crema di papaya e "
        "Gainsboro, così un colore su cui capiti ha un nome che puoi dire ad alta voce in una "
        "riunione.",
        "名前の付いた色も 279 あります。ありふれたものからパパイヤホイップやゲインズボロまで。"
        "たどり着いた色に、会議で口に出して言える名前が付いています。",
        "이름이 붙은 색도 279가지 있습니다. 흔한 색부터 파파야 휩과 게인즈버러까지. 그래서 다다른 "
        "색에는 회의에서 소리 내어 말할 수 있는 이름이 있습니다.",
        "Er zijn ook 279 kleuren met een naam, van de gewone tot Papajaschuim en Gainsboro, zodat "
        "een kleur waar je op uitkomt een naam heeft die je in een vergadering hardop kunt zeggen.",
        "Há também 279 cores com nome, das comuns até Creme de mamão e Gainsboro, para que uma cor "
        "em que você chega tenha um nome que dê para falar em voz alta numa reunião.",
        "另外还有 279 个有名字的颜色，从最平常的到木瓜奶油色和庚斯博罗灰。"
        "这样你落到的那个颜色，就有了一个能在会上说出口的名字。"),
    "The Harmony Palette color wheel with a complementary scheme selected, showing red and cyan swatches and a brightness slider.": (
        "Der Farbkreis von Harmony Palette mit ausgewähltem Komplementärschema, mit roten und "
        "cyanfarbenen Feldern und einem Helligkeitsregler.",
        "La rueda de color de Harmony Palette con un esquema complementario seleccionado, con "
        "muestras roja y cian y un control de brillo.",
        "La rueda de color de Harmony Palette con un esquema complementario seleccionado, con "
        "muestras roja y cian y un control de brillo.",
        "La roue chromatique de Harmony Palette avec un schéma complémentaire sélectionné, "
        "montrant des échantillons rouge et cyan et un curseur de luminosité.",
        "La ruota dei colori di Harmony Palette con uno schema complementare selezionato, con "
        "campioni rosso e ciano e un cursore di luminosità.",
        "補色の配色を選んだ状態の Harmony Palette のカラーホイール。赤とシアンの色見本と"
        "明るさのスライダーが見えている。",
        "보색 배색을 고른 상태의 Harmony Palette 색상환. 빨강과 사이언 견본, 그리고 밝기 슬라이더가 "
        "보인다.",
        "Het kleurenwiel van Harmony Palette met een complementair schema geselecteerd, met rode "
        "en cyaan stalen en een helderheidsschuif.",
        "A roda de cores do Harmony Palette com um esquema complementar selecionado, mostrando "
        "amostras vermelha e ciano e um controle de brilho.",
        "选中互补配色时的 Harmony Palette 色轮，可以看到红色与青色的色块和一条亮度滑杆。"),
    "The wheel, in RGB or RYB": (
        "Der Kreis, in RGB oder RYB", "La rueda, en RGB o RYB", "La rueda, en RGB o RYB",
        "La roue, en RVB ou RJB", "La ruota, in RGB o RYB", "ホイール、RGB でも RYB でも",
        "색상환, RGB로도 RYB로도", "Het wiel, in RGB of RYB", "A roda, em RGB ou RYB",
        "色轮，RGB 或 RYB"),
    "A grid of saved palettes in the Harmony Palette library, each showing its colors and a name.": (
        "Ein Raster gespeicherter Paletten in der Bibliothek von Harmony Palette, jede mit ihren "
        "Farben und einem Namen.",
        "Una cuadrícula de paletas guardadas en la biblioteca de Harmony Palette, cada una con sus "
        "colores y un nombre.",
        "Una cuadrícula de paletas guardadas en la biblioteca de Harmony Palette, cada una con sus "
        "colores y un nombre.",
        "Une grille de palettes enregistrées dans la bibliothèque de Harmony Palette, chacune "
        "montrant ses couleurs et un nom.",
        "Una griglia di palette salvate nella libreria di Harmony Palette, ognuna con i suoi "
        "colori e un nome.",
        "Harmony Palette のライブラリに保存されたパレットの一覧。それぞれに色と名前が並んでいる。",
        "Harmony Palette 라이브러리에 저장된 팔레트들의 격자. 각각 색과 이름이 함께 보인다.",
        "Een raster van bewaarde paletten in de bibliotheek van Harmony Palette, elk met zijn "
        "kleuren en een naam.",
        "Uma grade de paletas salvas na biblioteca do Harmony Palette, cada uma mostrando suas "
        "cores e um nome.",
        "Harmony Palette 库中已保存调色板的网格，每一套都显示自己的颜色和名字。"),
    "Your own library, in folders": (
        "Ihre eigene Bibliothek, in Ordnern", "Tu propia biblioteca, en carpetas",
        "Tu propia biblioteca, en carpetas", "Votre bibliothèque, en dossiers",
        "La tua libreria, in cartelle", "自分のライブラリ、フォルダに分けて",
        "내 라이브러리, 폴더로", "Je eigen bibliotheek, in mappen",
        "Sua própria biblioteca, em pastas", "你自己的库，分在文件夹里"),
    "The Explore tab showing featured curated palettes and category tiles for nature and classic art.": (
        "Der Tab Entdecken mit hervorgehobenen kuratierten Paletten und Kategoriekacheln für Natur "
        "und klassische Kunst.",
        "La pestaña Explorar con paletas seleccionadas destacadas y mosaicos de categoría para "
        "naturaleza y arte clásico.",
        "La pestaña Explorar con paletas seleccionadas destacadas y mosaicos de categoría para "
        "naturaleza y arte clásico.",
        "L'onglet Explorer montrant des palettes sélectionnées mises en avant et des tuiles de "
        "catégorie pour la nature et l'art classique.",
        "La scheda Esplora con palette selezionate in evidenza e riquadri di categoria per natura "
        "e arte classica.",
        "おすすめの厳選パレットと、自然や古典絵画のカテゴリータイルが並ぶ「見つける」タブ。",
        "추천 엄선 팔레트와 자연, 고전 미술 분류 타일이 놓인 둘러보기 탭.",
        "Het tabblad Ontdekken met uitgelichte samengestelde paletten en categorietegels voor "
        "natuur en klassieke kunst.",
        "A aba Explorar mostrando paletas selecionadas em destaque e blocos de categoria para "
        "natureza e arte clássica.",
        "「探索」标签页，展示精选调色板和自然、古典艺术的分类方块。"),
    "160 curated palettes": (
        "160 kuratierte Paletten", "160 paletas seleccionadas", "160 paletas seleccionadas",
        "160 palettes sélectionnées", "160 palette selezionate", "厳選された 160 のパレット",
        "엄선된 160개의 팔레트", "160 samengestelde paletten", "160 paletas selecionadas",
        "精选的 160 套调色板"),
    "The Tools tab listing the contrast checker, color blindness simulator, random palette generator and image extractor.": (
        "Der Tab Werkzeuge mit Kontrastprüfer, Farbenblindheitssimulator, "
        "Zufallspaletten-Generator und Bildextraktor.",
        "La pestaña Herramientas con el comprobador de contraste, el simulador de daltonismo, el "
        "generador de paletas al azar y el extractor de imágenes.",
        "La pestaña Herramientas con el verificador de contraste, el simulador de daltonismo, el "
        "generador de paletas al azar y el extractor de imágenes.",
        "L'onglet Outils listant le vérificateur de contraste, le simulateur de daltonisme, le "
        "générateur de palettes aléatoires et l'extracteur d'images.",
        "La scheda Strumenti con il controllo del contrasto, il simulatore di daltonismo, il "
        "generatore di palette casuali e l'estrattore da immagini.",
        "コントラストチェッカー、色覚シミュレーター、ランダムパレット生成、画像からの抽出が"
        "並ぶ「ツール」タブ。",
        "명도 대비 검사기, 색각 이상 시뮬레이터, 무작위 팔레트 생성기, 이미지 추출기가 나열된 도구 "
        "탭.",
        "Het tabblad Gereedschap met de contrastchecker, de kleurenblindheidssimulator, de "
        "willekeurige-paletgenerator en de afbeeldingsextractor.",
        "A aba Ferramentas listando o verificador de contraste, o simulador de daltonismo, o "
        "gerador de paletas aleatórias e o extrator de imagens.",
        "「工具」标签页，列出对比度检查器、色觉模拟器、随机调色板生成器和图像取色器。"),
    "The tools, all four of them": (
        "Die Werkzeuge, alle vier", "Las herramientas, las cuatro",
        "Las herramientas, las cuatro", "Les outils, tous les quatre",
        "Gli strumenti, tutti e quattro", "ツール、その 4 つとも", "도구, 네 가지 모두",
        "Het gereedschap, alle vier", "As ferramentas, todas as quatro", "四件工具，一件不落"),
    "it leaves as code,": (
        "es geht als Code raus,", "sale como código,", "sale como código,",
        "elle sort en code,", "esce come codice,", "出ていくのはコードで、",
        "코드로 나가지,", "het vertrekt als code,", "ela sai como código,", "它以代码的形式离开，"),
    "not as a screenshot": (
        "nicht als Screenshot", "no como captura de pantalla", "no como captura de pantalla",
        "pas en capture d'écran", "non come screenshot", "スクリーンショットではありません",
        "스크린샷으로가 아니라", "niet als schermafbeelding", "não como captura de tela",
        "而不是截图"),
    "A palette that stays in the app is a mood board. A palette you can paste is work.": (
        "Eine Palette, die in der App bleibt, ist ein Moodboard. Eine Palette, die Sie einfügen "
        "können, ist Arbeit.",
        "Una paleta que se queda en la app es un moodboard. Una paleta que puedes pegar es "
        "trabajo.",
        "Una paleta que se queda en la app es un moodboard. Una paleta que puedes pegar es "
        "trabajo.",
        "Une palette qui reste dans l'application est un moodboard. Une palette que vous pouvez "
        "coller est du travail.",
        "Una palette che resta nell'app è un moodboard. Una palette che puoi incollare è lavoro.",
        "アプリの中にとどまるパレットはムードボードです。貼り付けられるパレットは仕事です。",
        "앱 안에 머무는 팔레트는 무드보드입니다. 붙여 넣을 수 있는 팔레트는 작업입니다.",
        "Een palet dat in de app blijft is een moodboard. Een palet dat je kunt plakken is werk.",
        "Uma paleta que fica no app é um moodboard. Uma paleta que dá para colar é trabalho.",
        "留在应用里的调色板是情绪板。能粘贴出去的调色板才是活儿。"),
    "Pro exports SwiftUI and UIKit color extensions, CSS custom properties and a Tailwind config,\n      ready to paste into a project without retyping a single hex value. For the other side of the\n      job there is multi-page PDF for client presentations and SVG for print, plus social images\n      sized for a square post, a portrait post or a story.": (
        "Pro exportiert Farb-Extensions für SwiftUI und UIKit, CSS-Custom-Properties und eine "
        "Tailwind-Konfiguration, fertig zum Einfügen in ein Projekt, ohne einen einzigen Hex-Wert "
        "abzutippen. Für die andere Seite der Arbeit gibt es mehrseitiges PDF für "
        "Kundenpräsentationen und SVG für den Druck, dazu Social-Bilder im Format für einen "
        "quadratischen Beitrag, einen Hochkant-Beitrag oder eine Story.",
        "Pro exporta extensiones de color para SwiftUI y UIKit, propiedades personalizadas de CSS "
        "y una configuración de Tailwind, listas para pegar en un proyecto sin reescribir un solo "
        "valor hexadecimal. Para el otro lado del trabajo hay PDF de varias páginas para "
        "presentaciones a clientes y SVG para imprenta, además de imágenes para redes con el "
        "tamaño de una publicación cuadrada, una vertical o una historia.",
        "Pro exporta extensiones de color para SwiftUI y UIKit, propiedades personalizadas de CSS "
        "y una configuración de Tailwind, listas para pegar en un proyecto sin reescribir un solo "
        "valor hexadecimal. Para el otro lado del trabajo hay PDF de varias páginas para "
        "presentaciones a clientes y SVG para imprenta, además de imágenes para redes con el "
        "tamaño de una publicación cuadrada, una vertical o una historia.",
        "Pro exporte des extensions de couleur SwiftUI et UIKit, des propriétés personnalisées CSS "
        "et une configuration Tailwind, prêtes à coller dans un projet sans retaper une seule "
        "valeur hexadécimale. Pour l'autre versant du travail, il y a du PDF multipage pour les "
        "présentations client et du SVG pour l'impression, plus des images sociales au format d'un "
        "post carré, d'un post vertical ou d'une story.",
        "Pro esporta estensioni di colore per SwiftUI e UIKit, proprietà personalizzate CSS e una "
        "configurazione Tailwind, pronte da incollare in un progetto senza ridigitare un solo "
        "valore esadecimale. Per l'altro lato del lavoro c'è il PDF multipagina per le "
        "presentazioni ai clienti e l'SVG per la stampa, più immagini social nel formato di un "
        "post quadrato, di un post verticale o di una storia.",
        "Pro は SwiftUI と UIKit のカラー拡張、CSS のカスタムプロパティ、Tailwind の設定を"
        "書き出します。16 進数の値を一つも打ち直さずにプロジェクトへ貼り付けられます。"
        "仕事のもう一方の側には、クライアント向けの複数ページ PDF と印刷用の SVG、"
        "さらに正方形の投稿、縦長の投稿、ストーリーの寸法に合わせた SNS 用画像があります。",
        "Pro는 SwiftUI와 UIKit의 색상 익스텐션, CSS 커스텀 프로퍼티, Tailwind 설정을 내보냅니다. "
        "16진수 값을 하나도 다시 치지 않고 프로젝트에 붙여 넣을 수 있습니다. 일의 반대편을 위해서는 "
        "고객 발표용 여러 쪽짜리 PDF와 인쇄용 SVG가 있고, 정사각형 게시물, 세로 게시물, 스토리 "
        "크기에 맞춘 소셜 이미지도 있습니다.",
        "Pro exporteert kleurextensies voor SwiftUI en UIKit, CSS custom properties en een "
        "Tailwind-configuratie, klaar om in een project te plakken zonder ook maar één "
        "hexadecimale waarde over te typen. Voor de andere kant van het werk is er meerpagina-PDF "
        "voor klantpresentaties en SVG voor druk, plus socialebeelden op maat voor een vierkante "
        "post, een staande post of een story.",
        "O Pro exporta extensões de cor para SwiftUI e UIKit, propriedades personalizadas de CSS e "
        "uma configuração do Tailwind, prontas para colar num projeto sem redigitar um único valor "
        "hexadecimal. Para o outro lado do trabalho há PDF de várias páginas para apresentações a "
        "clientes e SVG para impressão, além de imagens para redes no tamanho de um post quadrado, "
        "um post vertical ou um story.",
        "Pro 可以导出 SwiftUI 和 UIKit 的颜色扩展、CSS 自定义属性和一份 Tailwind 配置，"
        "可以直接粘进项目，一个十六进制值都不用重打。"
        "工作的另一头则有给客户演示用的多页 PDF 和给印刷用的 SVG，"
        "还有按方形帖、竖版帖或快拍尺寸做好的社交图片。"),
    "Free gets you HEX, RGB, HSL and HSV to copy by hand, which for a lot of people is all they\n      ever need. CMYK sits with Pro, alongside the print exports it belongs to.": (
        "Kostenlos bekommen Sie HEX, RGB, HSL und HSV zum Abschreiben, was für viele Menschen "
        "alles ist, was sie je brauchen. CMYK sitzt bei Pro, neben den Druckexporten, zu denen es "
        "gehört.",
        "Gratis te da HEX, RGB, HSL y HSV para copiar a mano, que para mucha gente es todo lo que "
        "va a necesitar. CMYK está con Pro, junto a las exportaciones de imprenta a las que "
        "pertenece.",
        "Gratis te da HEX, RGB, HSL y HSV para copiar a mano, que para mucha gente es todo lo que "
        "va a necesitar. CMYK está con Pro, junto a las exportaciones de imprenta a las que "
        "pertenece.",
        "La version gratuite vous donne HEX, RVB, TSL et TSV à recopier à la main, ce qui suffit "
        "à beaucoup de gens pour toujours. CMYK est du côté de Pro, avec les exports pour "
        "l'impression auxquels il appartient.",
        "La versione gratuita ti dà HEX, RGB, HSL e HSV da copiare a mano, che per molte persone è "
        "tutto quello che serviranno mai. CMYK sta con Pro, accanto agli export per la stampa a "
        "cui appartiene.",
        "無料版では HEX、RGB、HSL、HSV を手で写せます。多くの人にとってはそれで一生ぶん足ります。"
        "CMYK は Pro 側にあり、本来の居場所である印刷向けの書き出しの隣に並んでいます。",
        "무료로는 HEX, RGB, HSL, HSV를 손으로 옮겨 적을 수 있고, 많은 사람에게는 그것으로 평생 "
        "충분합니다. CMYK는 Pro 쪽에, 원래 속한 자리인 인쇄용 내보내기 옆에 있습니다.",
        "Gratis krijg je HEX, RGB, HSL en HSV om met de hand over te nemen, en voor veel mensen is "
        "dat alles wat ze ooit nodig hebben. CMYK hoort bij Pro, naast de drukexports waar het "
        "thuishoort.",
        "O gratuito te dá HEX, RGB, HSL e HSV para copiar à mão, o que para muita gente é tudo o "
        "que vai precisar. O CMYK fica com o Pro, ao lado das exportações para impressão a que "
        "pertence.",
        "免费版给你 HEX、RGB、HSL 和 HSV，可以手抄下来，对很多人来说这辈子够用了。"
        "CMYK 跟 Pro 在一起，挨着它本来就该在的那些印刷导出项。"),
    "Free": (
        "Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료",
        "Gratis", "Grátis", "免费"),
    "The full color wheel, both models": (
        "Der ganze Farbkreis, beide Modelle", "La rueda de color entera, los dos modelos",
        "La rueda de color entera, los dos modelos", "La roue chromatique entière, les deux "
        "modèles", "La ruota dei colori intera, entrambi i modelli",
        "カラーホイールのすべて、両方のモデル", "색상환 전부, 두 모델 다",
        "Het hele kleurenwiel, beide modellen", "A roda de cores inteira, os dois modelos",
        "完整色轮，两种模型"),
    "Everything in Free": (
        "Alles aus der kostenlosen Version", "Todo lo de Gratis", "Todo lo de Gratis",
        "Tout ce qu'il y a dans Gratuit", "Tutto quello che c'è in Gratis", "無料版のすべて",
        "무료의 모든 것", "Alles uit Gratis", "Tudo o que há no Grátis", "免费版的全部"),
    "4 harmony types": (
        "4 Harmonietypen", "4 tipos de armonía", "4 tipos de armonía", "4 types d'harmonie",
        "4 tipi di armonia", "4 種類の調和", "4가지 조화", "4 harmonietypes",
        "4 tipos de harmonia", "4 种配色关系"),
    "All 8 harmony types": (
        "Alle 8 Harmonietypen", "Los 8 tipos de armonía", "Los 8 tipos de armonía",
        "Les 8 types d'harmonie", "Tutti gli 8 tipi di armonia", "8 種類すべての調和",
        "8가지 조화 전부", "Alle 8 harmonietypes", "Todos os 8 tipos de harmonia",
        "全部 8 种配色关系"),
    "15 saved palettes, 3 folders": (
        "15 gespeicherte Paletten, 3 Ordner", "15 paletas guardadas, 3 carpetas",
        "15 paletas guardadas, 3 carpetas", "15 palettes enregistrées, 3 dossiers",
        "15 palette salvate, 3 cartelle", "保存できるパレット 15、フォルダ 3",
        "저장 팔레트 15개, 폴더 3개", "15 bewaarde paletten, 3 mappen",
        "15 paletas salvas, 3 pastas", "15 套已存调色板，3 个文件夹"),
    "Unlimited palettes and folders": (
        "Unbegrenzt Paletten und Ordner", "Paletas y carpetas sin límite",
        "Paletas y carpetas sin límite", "Palettes et dossiers sans limite",
        "Palette e cartelle senza limite", "パレットとフォルダは無制限",
        "팔레트와 폴더 무제한", "Onbeperkt paletten en mappen", "Paletas e pastas sem limite",
        "调色板与文件夹不限量"),
    "Color extraction from photos": (
        "Farbextraktion aus Fotos", "Extracción de color de fotos",
        "Extracción de color de fotos", "Extraction de couleurs depuis des photos",
        "Estrazione dei colori dalle foto", "写真からの色の抽出", "사진에서 색 추출",
        "Kleurextractie uit foto's", "Extração de cores de fotos", "从照片提取颜色"),
    "HEX, RGB, HSL and HSV values": (
        "HEX-, RGB-, HSL- und HSV-Werte", "Valores HEX, RGB, HSL y HSV",
        "Valores HEX, RGB, HSL y HSV", "Valeurs HEX, RVB, TSL et TSV",
        "Valori HEX, RGB, HSL e HSV", "HEX、RGB、HSL、HSV の値", "HEX, RGB, HSL, HSV 값",
        "HEX-, RGB-, HSL- en HSV-waarden", "Valores HEX, RGB, HSL e HSV",
        "HEX、RGB、HSL 和 HSV 数值"),
    "CMYK, the contrast checker and vision simulation": (
        "CMYK, der Kontrastprüfer und die Sehsimulation",
        "CMYK, el comprobador de contraste y la simulación de visión",
        "CMYK, el verificador de contraste y la simulación de visión",
        "CMYK, le vérificateur de contraste et la simulation de vision",
        "CMYK, il controllo del contrasto e la simulazione della vista",
        "CMYK、コントラストチェッカー、色覚シミュレーション",
        "CMYK, 명도 대비 검사기, 색각 시뮬레이션",
        "CMYK, de contrastchecker en de zichtsimulatie",
        "CMYK, o verificador de contraste e a simulação de visão",
        "CMYK、对比度检查器和色觉模拟"),
    "Sharing with a watermark": (
        "Teilen mit Wasserzeichen", "Compartir con marca de agua",
        "Compartir con marca de agua", "Partage avec filigrane",
        "Condivisione con filigrana", "透かし入りで共有", "워터마크가 있는 공유",
        "Delen met watermerk", "Compartilhar com marca-d'água", "分享时带水印"),
    "PDF, SVG and code export, no watermark": (
        "PDF-, SVG- und Code-Export, ohne Wasserzeichen",
        "Exportación a PDF, SVG y código, sin marca de agua",
        "Exportación a PDF, SVG y código, sin marca de agua",
        "Export PDF, SVG et code, sans filigrane",
        "Export in PDF, SVG e codice, senza filigrana",
        "PDF、SVG、コードの書き出し、透かしなし",
        "PDF, SVG, 코드 내보내기, 워터마크 없음",
        "PDF-, SVG- en code-export, zonder watermerk",
        "Exportação para PDF, SVG e código, sem marca-d'água",
        "导出 PDF、SVG 和代码，不带水印"),
    "Pro is $2.99 a month or $14.99 a year, both with a\n      seven day trial, or $29.99 once for good, which includes everything added later.": (
        "Pro kostet $2.99 im Monat oder $14.99 im Jahr, beides mit sieben Tagen zum Ausprobieren, "
        "oder $29.99 einmalig für immer, was alles später Hinzugefügte einschließt.",
        "Pro cuesta $2.99 al mes o $14.99 al año, ambos con siete días de prueba, o $29.99 una "
        "sola vez para siempre, que incluye todo lo que se añada después.",
        "Pro cuesta $2.99 al mes o $14.99 al año, ambos con siete días de prueba, o $29.99 una "
        "sola vez para siempre, que incluye todo lo que se agregue después.",
        "Pro coûte $2.99 par mois ou $14.99 par an, les deux avec sept jours d'essai, ou $29.99 "
        "une fois pour toutes, ce qui comprend tout ce qui sera ajouté ensuite.",
        "Pro costa $2.99 al mese o $14.99 all'anno, entrambi con sette giorni di prova, oppure "
        "$29.99 una volta sola per sempre, che comprende tutto quello che verrà aggiunto dopo.",
        "Pro は月 $2.99 または年 $14.99 で、どちらも 7 日間試せます。あるいは $29.99 の買い切りで、"
        "こちらは後から追加されるものもすべて含みます。",
        "Pro는 월 $2.99 또는 연 $14.99이고 둘 다 7일 동안 시험해 볼 수 있습니다. 아니면 $29.99 한 "
        "번으로 영영, 여기에는 나중에 추가되는 것도 모두 포함됩니다.",
        "Pro kost $2.99 per maand of $14.99 per jaar, beide met zeven dagen proef, of $29.99 "
        "eenmalig voorgoed, inclusief alles wat later wordt toegevoegd.",
        "O Pro custa $2.99 por mês ou $14.99 por ano, ambos com sete dias de teste, ou $29.99 uma "
        "vez só para sempre, o que inclui tudo o que for acrescentado depois.",
        "Pro 每月 $2.99 或每年 $14.99，两者都有七天试用；也可以 $29.99 一次买断，"
        "此后新增的一切都包含在内。"),
}
