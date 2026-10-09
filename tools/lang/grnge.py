"""lf.wtf/grnge, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Written against the app's own words, from GRNGE's Localizable.xcstrings: the effects are
Fotokopie / Fotocopia / Photocopie / コピー / 복사 / 复印 and so on, the Stack is Stapel / Capas /
Couches / 重ね / 레이어 / 叠层, and the headline is the one on the app's home card. The app speaks
to the reader informally in every language (du, tú, tu, 해요체), so this page does too, French
included, which is why it says "tu" where the other product pages say "vous". Mexican Spanish uses
the app's own es-MX words: plumón, pluma, aerosol, esténcil, calcomanía.

The copier brand name is a trademark and appears nowhere. Photocopy is the name of an effect, and is
used only as that.
"""

KEEP = {"GRNGE", "GRNGE Pro", "lf.wtf", "L@LF.WTF", "CYANO", "Levi Foster"}

T = {
    "GRNGE: photocopy, stipple, halftone and dither photo effects for iPhone": (
        "GRNGE: Fotokopie-, Punkt-, Raster- und Dither-Effekte für Fotos auf dem iPhone",
        "GRNGE: efectos de fotocopia, puntillismo, trama y dither para fotos en iPhone",
        "GRNGE: efectos de fotocopia, puntillismo, trama y dither para fotos en iPhone",
        "GRNGE : effets photocopie, pointillé, trame et tramage pour tes photos sur iPhone",
        "GRNGE: effetti fotocopia, puntinato, retino e dither per le foto su iPhone",
        "GRNGE：写真をコピー、点描、網点、ディザに変える iPhone アプリ",
        "GRNGE: 사진을 복사, 점묘, 망점, 디더 효과로 바꾸는 iPhone 앱",
        "GRNGE: fotokopie-, stippel-, raster- en dither-effecten voor foto's op iPhone",
        "GRNGE: efeitos de fotocópia, pontilhado, retícula e dither para fotos no iPhone",
        "GRNGE：把照片变成复印、点描、网点和抖动效果的 iPhone 应用"),

    "Turn photos into black-and-white photocopy, stipple, halftone and dither prints on iPhone. Layer them in color inks, draw on them, cut out the subject, add stickers, and save at post, story, square or poster size.": (
        "Mach aus Fotos Schwarz-Weiß-Drucke auf dem iPhone: Fotokopie, Punktiert, Raster oder Dither. Leg sie in farbigen Tinten übereinander, zeichne darauf, schneide das Motiv aus, kleb Sticker drauf und sichere sie als Post, Story, Quadrat oder Poster.",
        "Convierte tus fotos en impresiones en blanco y negro en el iPhone: fotocopia, puntillismo, trama o dither. Superponlas en tintas de color, dibuja encima, recorta el sujeto, añade pegatinas y guárdalas en tamaño post, historia, cuadrado o póster.",
        "Convierte tus fotos en impresiones en blanco y negro en el iPhone: fotocopia, puntillismo, trama o dither. Superponlas en tintas de color, dibuja encima, recorta el sujeto, agrega calcomanías y guárdalas en tamaño post, historia, cuadrado o póster.",
        "Transforme tes photos en tirages noir et blanc sur iPhone : photocopie, pointillé, trame ou tramage. Superpose-les en encres de couleur, dessine dessus, découpe le sujet, ajoute des autocollants et enregistre-les au format publication, story, carré ou affiche.",
        "Trasforma le foto in stampe in bianco e nero su iPhone: fotocopia, puntinato, retino o dither. Sovrapponile in inchiostri colorati, disegnaci sopra, ritaglia il soggetto, aggiungi adesivi e salvale in formato post, storia, quadrato o poster.",
        "iPhone で写真を白黒のプリントに。コピー、点描、網点、ディザ。カラーインクで重ねて、上から描いて、被写体を切り抜いて、シールを貼って、投稿、ストーリー、正方形、ポスターのサイズで保存。",
        "iPhone에서 사진을 흑백 인쇄물로. 복사, 점묘, 망점, 디더. 컬러 잉크로 겹치고, 위에 그리고, 피사체를 오려내고, 스티커를 붙여서 게시물, 스토리, 정사각형, 포스터 크기로 저장하세요.",
        "Maak van foto's zwart-witafdrukken op je iPhone: fotokopie, stippel, raster of dither. Leg ze in kleurinkten over elkaar, teken erop, knip het onderwerp uit, plak stickers erop en bewaar ze als post, story, vierkant of poster.",
        "Transforme fotos em impressões em preto e branco no iPhone: fotocópia, pontilhado, retícula ou dither. Sobreponha em tintas coloridas, desenhe por cima, recorte o assunto, adicione adesivos e salve no tamanho de post, story, quadrado ou pôster.",
        "在 iPhone 上把照片变成黑白印刷品：复印、点描、网点或抖动。用彩色墨叠印，在上面涂鸦，抠出主体，贴上贴纸，再按帖子、快拍、方形或海报尺寸保存。"),

    "Black-and-white prints from your photos, on iPhone. Layer them in color inks, draw on them, cut out the subject, add stickers, and save at the size you post.": (
        "Schwarz-Weiß-Drucke aus deinen Fotos, auf dem iPhone. Leg sie in farbigen Tinten übereinander, zeichne darauf, schneide das Motiv aus, kleb Sticker drauf und sichere sie in der Größe, in der du postest.",
        "Impresiones en blanco y negro de tus fotos, en el iPhone. Superponlas en tintas de color, dibuja encima, recorta el sujeto, añade pegatinas y guárdalas al tamaño en que publicas.",
        "Impresiones en blanco y negro de tus fotos, en el iPhone. Superponlas en tintas de color, dibuja encima, recorta el sujeto, agrega calcomanías y guárdalas al tamaño en que publicas.",
        "Des tirages noir et blanc de tes photos, sur iPhone. Superpose-les en encres de couleur, dessine dessus, découpe le sujet, ajoute des autocollants et enregistre-les au format de tes publications.",
        "Stampe in bianco e nero delle tue foto, su iPhone. Sovrapponile in inchiostri colorati, disegnaci sopra, ritaglia il soggetto, aggiungi adesivi e salvale nel formato in cui pubblichi.",
        "あなたの写真から白黒のプリントを、iPhone で。カラーインクで重ねて、上から描いて、被写体を切り抜いて、シールを貼って、投稿するサイズで保存。",
        "내 사진으로 만드는 흑백 인쇄물, iPhone에서. 컬러 잉크로 겹치고, 위에 그리고, 피사체를 오려내고, 스티커를 붙여서 올릴 크기로 저장하세요.",
        "Zwart-witafdrukken van je foto's, op je iPhone. Leg ze in kleurinkten over elkaar, teken erop, knip het onderwerp uit, plak stickers erop en bewaar ze op het formaat waarop je post.",
        "Impressões em preto e branco das suas fotos, no iPhone. Sobreponha em tintas coloridas, desenhe por cima, recorte o assunto, adicione adesivos e salve no tamanho em que você posta.",
        "用你的照片做黑白印刷品，在 iPhone 上。用彩色墨叠印，在上面涂鸦，抠出主体，贴上贴纸，按你发帖的尺寸保存。"),

    "The GRNGE icon: a black-and-white eye with an orange marker ring around it.": (
        "Das GRNGE-Symbol: ein schwarz-weißes Auge mit einem orangen Markerkreis darum.",
        "El icono de GRNGE: un ojo en blanco y negro rodeado por un círculo de rotulador naranja.",
        "El ícono de GRNGE: un ojo en blanco y negro rodeado por un círculo de plumón naranja.",
        "L'icône de GRNGE : un œil noir et blanc entouré d'un cercle de marqueur orange.",
        "L'icona di GRNGE: un occhio in bianco e nero cerchiato con un pennarello arancione.",
        "GRNGE のアイコン：オレンジのマーカーで丸く囲まれた白黒の目。",
        "GRNGE 아이콘: 주황색 마커로 동그라미를 친 흑백 눈.",
        "Het GRNGE-icoon: een zwart-wit oog met een oranje stiftcirkel eromheen.",
        "O ícone do GRNGE: um olho em preto e branco com um círculo de marcador laranja em volta.",
        "GRNGE 的图标：一只黑白的眼睛，被橙色马克笔圈了起来。"),

    "Photo effects for iPhone": (
        "Fotoeffekte fürs iPhone", "Efectos de foto para iPhone", "Efectos de foto para iPhone",
        "Effets photo pour iPhone", "Effetti foto per iPhone", "iPhone のための写真エフェクト",
        "iPhone을 위한 사진 효과", "Foto-effecten voor iPhone", "Efeitos de foto para iPhone",
        "iPhone 照片效果"),

    "Start here": (
        "Hier starten", "Empieza aquí", "Empieza aquí", "Commence ici", "Inizia qui", "ここから",
        "여기서 시작", "Begin hier", "Comece aqui", "从这里开始"),

    "Start with a photo.": (
        "Fang mit einem Foto an.", "Empieza con una foto.", "Empieza con una foto.",
        "Commence par une photo.", "Inizia da una foto.", "写真から始めよう。", "사진 한 장으로 시작.",
        "Begin met een foto.", "Comece com uma foto.", "从一张照片开始。"),

    "GRNGE turns it into a black-and-white print: photocopy, stipple, halftone or dither. Then layer it in color inks, draw on it, cut out the subject, add stickers, and save it at the size you post.": (
        "GRNGE macht daraus einen Schwarz-Weiß-Druck: Fotokopie, Punktiert, Raster oder Dither. Dann leg ihn in farbigen Tinten übereinander, zeichne darauf, schneide das Motiv aus, kleb Sticker drauf und sichere ihn in der Größe, in der du postest.",
        "GRNGE la convierte en una impresión en blanco y negro: fotocopia, puntillismo, trama o dither. Luego superponla en tintas de color, dibuja encima, recorta el sujeto, añade pegatinas y guárdala al tamaño en que publicas.",
        "GRNGE la convierte en una impresión en blanco y negro: fotocopia, puntillismo, trama o dither. Luego superponla en tintas de color, dibuja encima, recorta el sujeto, agrega calcomanías y guárdala al tamaño en que publicas.",
        "GRNGE en fait un tirage noir et blanc : photocopie, pointillé, trame ou tramage. Ensuite, superpose-le en encres de couleur, dessine dessus, découpe le sujet, ajoute des autocollants et enregistre-le au format de tes publications.",
        "GRNGE la trasforma in una stampa in bianco e nero: fotocopia, puntinato, retino o dither. Poi sovrapponila in inchiostri colorati, disegnaci sopra, ritaglia il soggetto, aggiungi adesivi e salvala nel formato in cui pubblichi.",
        "GRNGE がそれを白黒のプリントにします。コピー、点描、網点、ディザ。そこからカラーインクで重ねて、上から描いて、被写体を切り抜いて、シールを貼り、投稿するサイズで保存できます。",
        "GRNGE가 흑백 인쇄물로 바꿔 줘요. 복사, 점묘, 망점, 디더. 그다음 컬러 잉크로 겹치고, 위에 그리고, 피사체를 오려내고, 스티커를 붙여서 올릴 크기로 저장하세요.",
        "GRNGE maakt er een zwart-witafdruk van: fotokopie, stippel, raster of dither. Leg hem daarna in kleurinkten over elkaar, teken erop, knip het onderwerp uit, plak stickers erop en bewaar hem op het formaat waarop je post.",
        "O GRNGE transforma a foto numa impressão em preto e branco: fotocópia, pontilhado, retícula ou dither. Depois, sobreponha em tintas coloridas, desenhe por cima, recorte o assunto, adicione adesivos e salve no tamanho em que você posta.",
        "GRNGE 把它变成一张黑白印刷品：复印、点描、网点或抖动。然后用彩色墨叠印，在上面涂鸦，抠出主体，贴上贴纸，按你发帖的尺寸保存。"),

    "Download on the App Store": (
        "Im App Store laden", "Descargar en el App Store", "Descargar en el App Store",
        "Télécharger dans l'App Store", "Scarica dall'App Store", "App Store でダウンロード",
        "App Store에서 다운로드", "Download in de App Store", "Baixar na App Store", "在 App Store 下载"),

    "Free. iPhone, iOS 17 and later. GRNGE Pro opens everything, with a free week on the yearly plan.": (
        "Kostenlos. iPhone, ab iOS 17. GRNGE Pro schaltet alles frei, beim Jahresabo mit einer Gratiswoche.",
        "Gratis. iPhone, iOS 17 o posterior. GRNGE Pro lo desbloquea todo, con una semana gratis en el plan anual.",
        "Gratis. iPhone, iOS 17 o posterior. GRNGE Pro lo desbloquea todo, con una semana gratis en el plan anual.",
        "Gratuit. iPhone, iOS 17 ou plus récent. GRNGE Pro débloque tout, avec une semaine offerte sur la formule annuelle.",
        "Gratis. iPhone, iOS 17 o successivo. GRNGE Pro sblocca tutto, con una settimana gratis sul piano annuale.",
        "無料。iPhone、iOS 17 以降。GRNGE Pro ですべて使えるようになります。年額プランは最初の1週間無料。",
        "무료. iPhone, iOS 17 이상. GRNGE Pro로 모든 기능을 열 수 있고, 연간 플랜은 첫 1주일이 무료예요.",
        "Gratis. iPhone, iOS 17 en later. GRNGE Pro opent alles, met een gratis week bij het jaarabonnement.",
        "Grátis. iPhone, iOS 17 ou posterior. O GRNGE Pro libera tudo, com uma semana grátis no plano anual.",
        "免费。iPhone，iOS 17 及以上。GRNGE Pro 解锁全部功能，年度方案首周免费。"),

    "A skateboarder crouching on his board, printed in hard black and white on off-white paper.": (
        "Ein Skateboarder, der auf seinem Brett hockt, in hartem Schwarz-Weiß auf cremefarbenem Papier gedruckt.",
        "Un skater agachado sobre su tabla, impreso en blanco y negro duro sobre papel crudo.",
        "Un patinador agachado sobre su patineta, impreso en blanco y negro duro sobre papel crudo.",
        "Un skateur accroupi sur sa planche, imprimé en noir et blanc dur sur du papier crème.",
        "Uno skater accovacciato sulla tavola, stampato in un bianco e nero duro su carta color crema.",
        "スケートボードの上でしゃがむ男性。オフホワイトの紙に、強い白黒で刷られている。",
        "보드 위에 웅크린 스케이트보더가 미색 종이 위에 강한 흑백으로 인쇄되어 있다.",
        "Een skateboarder die op zijn plank hurkt, hard zwart-wit gedrukt op gebroken wit papier.",
        "Um skatista agachado na prancha, impresso em preto e branco duro sobre papel creme.",
        "一个蹲在滑板上的滑手，以强烈的黑白印在米白色的纸上。"),

    "The original color photo of the skateboarder.": (
        "Das farbige Originalfoto des Skateboarders.",
        "La foto original en color del skater.",
        "La foto original a color del patinador.",
        "La photo couleur d'origine du skateur.",
        "La foto originale a colori dello skater.",
        "元のカラー写真。",
        "스케이트보더의 원본 컬러 사진.",
        "De originele kleurenfoto van de skateboarder.",
        "A foto original colorida do skatista.",
        "滑手的原始彩色照片。"),

    "Four prints from one photo": (
        "Vier Drucke aus einem Foto", "Cuatro impresiones de una foto", "Cuatro impresiones de una foto",
        "Quatre tirages d'une seule photo", "Quattro stampe da una foto", "1枚の写真から4つのプリント",
        "사진 한 장, 인쇄물 네 가지", "Vier afdrukken van één foto", "Quatro impressões de uma foto",
        "一张照片，四种印法"),

    "A portrait of a woman in sunglasses and a leather jacket.": (
        "Porträt einer Frau mit Sonnenbrille und Lederjacke.",
        "Retrato de una mujer con gafas de sol y chaqueta de cuero.",
        "Retrato de una mujer con lentes de sol y chamarra de piel.",
        "Portrait d'une femme en lunettes de soleil et blouson de cuir.",
        "Ritratto di una donna con occhiali da sole e giacca di pelle.",
        "サングラスと革ジャンの女性のポートレート。",
        "선글라스를 쓰고 가죽 재킷을 입은 여성의 인물 사진.",
        "Portret van een vrouw met zonnebril en leren jas.",
        "Retrato de uma mulher de óculos escuros e jaqueta de couro.",
        "一位戴墨镜、穿皮夹克的女性肖像。"),

    "Original": (
        "Original", "Original", "Original", "Original", "Originale", "オリジナル", "원본",
        "Origineel", "Original", "原图"),

    "The same portrait in hard black and white with grain.": (
        "Dasselbe Porträt in hartem Schwarz-Weiß mit Körnung.",
        "El mismo retrato en blanco y negro duro, con grano.",
        "El mismo retrato en blanco y negro duro, con grano.",
        "Le même portrait en noir et blanc dur, avec du grain.",
        "Lo stesso ritratto in bianco e nero duro, con grana.",
        "同じポートレートを、ざらつきのある強い白黒で。",
        "같은 인물 사진을 거친 입자가 있는 강한 흑백으로.",
        "Hetzelfde portret in hard zwart-wit met korrel.",
        "O mesmo retrato em preto e branco duro, com granulado.",
        "同一张肖像，强烈的黑白，带颗粒。"),

    "Photocopy": (
        "Fotokopie", "Fotocopia", "Fotocopia", "Photocopie", "Fotocopia", "コピー", "복사",
        "Fotokopie", "Fotocópia", "复印"),

    "The same portrait drawn in scattered dots.": (
        "Dasselbe Porträt aus verstreuten Punkten.",
        "El mismo retrato hecho de puntos dispersos.",
        "El mismo retrato hecho de puntos dispersos.",
        "Le même portrait fait de points épars.",
        "Lo stesso ritratto fatto di punti sparsi.",
        "同じポートレートを、散らばった点で。",
        "같은 인물 사진을 흩어진 점으로.",
        "Hetzelfde portret opgebouwd uit losse stippen.",
        "O mesmo retrato feito de pontos espalhados.",
        "同一张肖像，由散落的点组成。"),

    "Stipple": (
        "Punktiert", "Puntillismo", "Puntillismo", "Pointillé", "Puntinato", "点描", "점묘",
        "Stippel", "Pontilhado", "点描"),

    "The same portrait in a grid of round dots, like a newspaper photo.": (
        "Dasselbe Porträt aus einem Raster runder Punkte, wie ein Zeitungsfoto.",
        "El mismo retrato en una retícula de puntos redondos, como una foto de periódico.",
        "El mismo retrato en una retícula de puntos redondos, como una foto de periódico.",
        "Le même portrait en une grille de points ronds, comme une photo de journal.",
        "Lo stesso ritratto in una griglia di punti rotondi, come una foto di giornale.",
        "同じポートレートを、新聞写真のような丸い網点で。",
        "같은 인물 사진을 신문 사진처럼 둥근 망점으로.",
        "Hetzelfde portret in een raster van ronde stippen, zoals een krantenfoto.",
        "O mesmo retrato numa grade de pontos redondos, como uma foto de jornal.",
        "同一张肖像，由整齐的圆点组成，像报纸上的照片。"),

    "Halftone": (
        "Raster", "Trama", "Trama", "Trame", "Retino", "網点", "망점", "Raster", "Retícula", "网点"),

    "The same portrait in fine black and white pixels.": (
        "Dasselbe Porträt aus feinen schwarzen und weißen Pixeln.",
        "El mismo retrato en finos píxeles blancos y negros.",
        "El mismo retrato en finos píxeles blancos y negros.",
        "Le même portrait en fins pixels noirs et blancs.",
        "Lo stesso ritratto in minuscoli pixel bianchi e neri.",
        "同じポートレートを、細かい白と黒のピクセルで。",
        "같은 인물 사진을 촘촘한 흑백 픽셀로.",
        "Hetzelfde portret in fijne zwarte en witte pixels.",
        "O mesmo retrato em pixels pretos e brancos finos.",
        "同一张肖像，由细小的黑白像素组成。"),

    "Dither": (
        "Dither", "Dither", "Dither", "Tramage", "Dither", "ディザ", "디더", "Dither", "Dither", "抖动"),

    "Three dials do the same thing on all four. Ink goes lighter or darker, Grit goes from clean to dirty, Wear goes from fresh to worn. Hold the picture to see the photo again.": (
        "Drei Regler wirken bei allen vier gleich. Tinte geht heller oder dunkler, Körnung von sauber bis dreckig, Abnutzung von frisch bis abgenutzt. Halte das Bild gedrückt, um wieder das Foto zu sehen.",
        "Tres controles hacen lo mismo en los cuatro. Tinta va de más claro a más oscuro, Grano de limpio a sucio, Desgaste de nuevo a gastado. Mantén pulsada la imagen para volver a ver la foto.",
        "Tres controles hacen lo mismo en los cuatro. Tinta va de más claro a más oscuro, Grano de limpio a sucio, Desgaste de nuevo a gastado. Mantén presionada la imagen para volver a ver la foto.",
        "Trois réglages font la même chose sur les quatre. Encre va de plus clair à plus foncé, Grain de net à sale, Usure de neuf à usé. Maintiens l'image pour revoir la photo.",
        "Tre cursori fanno la stessa cosa su tutti e quattro. Inchiostro va da più chiaro a più scuro, Grana da pulito a sporco, Usura da nuovo a consumato. Tieni premuta l'immagine per rivedere la foto.",
        "3つのダイヤルは、4つすべてで同じ働きをします。インクで薄く濃く、ザラつきできれいから汚しまで、劣化で新品から使い古しまで。長押しすると元の写真が見られます。",
        "세 개의 다이얼은 네 가지 모두에서 똑같이 작동해요. 잉크는 연하게에서 진하게, 거칠기는 깨끗하게에서 지저분하게, 닳음은 새것에서 낡음까지. 사진을 길게 누르면 원본을 다시 볼 수 있어요.",
        "Drie schuiven doen bij alle vier hetzelfde. Inkt gaat lichter of donkerder, Korrel van schoon naar vuil, Slijtage van nieuw naar versleten. Houd de afbeelding vast om de foto weer te zien.",
        "Três controles fazem a mesma coisa nos quatro. Tinta vai de mais claro a mais escuro, Granulado de limpo a sujo, Desgaste de novo a gasto. Toque e segure a imagem para ver a foto de novo.",
        "三个旋钮在四种效果上作用一样。墨量调浅或调深，颗粒从干净到脏污，磨损从崭新到陈旧。按住画面就能看回原照片。"),

    "The portrait as a black print with an orange halftone laid over it, slightly out of line.": (
        "Das Porträt als schwarzer Druck, darüber ein oranger Raster, leicht versetzt.",
        "El retrato como impresión negra con una trama naranja encima, un poco desplazada.",
        "El retrato como impresión negra con una trama naranja encima, un poco desfasada.",
        "Le portrait en tirage noir avec une trame orange par-dessus, légèrement décalée.",
        "Il ritratto come stampa nera con un retino arancione sopra, leggermente spostato.",
        "黒で刷ったポートレートに、オレンジの網点を少しずらして重ねたもの。",
        "검정으로 인쇄한 인물 사진 위에 주황색 망점을 살짝 어긋나게 겹친 모습.",
        "Het portret als zwarte afdruk met een oranje raster erover, iets verschoven.",
        "O retrato como impressão preta com uma retícula laranja por cima, levemente deslocada.",
        "黑色印出的肖像，上面叠了一层稍微错位的橙色网点。"),

    "Stack": (
        "Stapel", "Capas", "Capas", "Couches", "Livelli", "重ね", "레이어", "Lagen", "Camadas", "叠层"),

    "Layer it in color": (
        "Leg Farbe darüber", "Superponla en color", "Superponla en color", "Superpose-la en couleur",
        "Sovrapponila a colori", "色を重ねる", "색을 겹치기", "Leg er kleur overheen",
        "Sobreponha em cores", "叠上颜色"),

    "Print the same photo again in orange, pink or blue and lay it over the first. Each sheet has its own effect, ink and strength. Let it show through, or shift it out of line. Recipes on the home screen set up a whole stack in one tap, and stay editable.": (
        "Druck dasselbe Foto noch einmal in Orange, Pink oder Blau und leg es über das erste. Jedes Blatt hat seinen eigenen Effekt, seine Tinte und seine Stärke. Lass es durchscheinen oder verschieb es aus der Linie. Rezepte auf dem Startbildschirm legen mit einem Tippen einen ganzen Stapel an, und alles bleibt bearbeitbar.",
        "Imprime la misma foto otra vez en naranja, rosa o azul y ponla sobre la primera. Cada capa tiene su propio efecto, su tinta y su intensidad. Deja que se transparente o desplázala para que no coincida. Las recetas de la pantalla de inicio montan todas las capas con un toque, y siguen siendo editables.",
        "Imprime la misma foto otra vez en naranja, rosa o azul y ponla sobre la primera. Cada capa tiene su propio efecto, su tinta y su intensidad. Deja que se transparente o desfásala para que no coincida. Las recetas de la pantalla de inicio arman todas las capas con un toque, y siguen siendo editables.",
        "Imprime la même photo encore une fois en orange, rose ou bleu et pose-la sur la première. Chaque couche a son propre effet, son encre et son intensité. Laisse-la transparaître, ou décale-la. Les recettes de l'écran d'accueil montent toutes les couches d'un seul geste, et tout reste modifiable.",
        "Stampa di nuovo la stessa foto in arancione, rosa o blu e mettila sopra la prima. Ogni livello ha il suo effetto, il suo inchiostro e la sua intensità. Lascialo trasparire, o spostalo fuori registro. Le ricette nella schermata iniziale preparano tutti i livelli con un tocco, e restano modificabili.",
        "同じ写真をオレンジ、ピンク、青でもう一度刷って、最初のプリントに重ねます。版ごとにエフェクト、インク、濃度を選べます。下を透けさせたり、ずらしたり。ホーム画面のレシピなら、ワンタップで重ねた状態から始められて、あとから自由に変えられます。",
        "같은 사진을 주황, 분홍, 파랑으로 한 번 더 인쇄해서 첫 장 위에 겹치세요. 장마다 효과, 잉크, 농도가 따로 있어요. 아래가 비치게 하거나, 살짝 어긋나게 할 수 있어요. 홈 화면의 레시피는 한 번 탭으로 여러 장을 한꺼번에 준비하고, 그대로 편집할 수 있어요.",
        "Druk dezelfde foto nog eens af in oranje, roze of blauw en leg hem over de eerste. Elke laag heeft zijn eigen effect, inkt en sterkte. Laat hem doorschijnen, of verschuif hem. Recepten op het beginscherm zetten met één tik een hele stapel klaar, en alles blijft bewerkbaar.",
        "Imprima a mesma foto de novo em laranja, rosa ou azul e coloque por cima da primeira. Cada camada tem seu próprio efeito, tinta e intensidade. Deixe transparecer, ou desloque para fora do registro. As receitas da tela inicial montam todas as camadas com um toque, e continuam editáveis.",
        "把同一张照片用橙色、粉色或蓝色再印一遍，叠在第一张上。每一层都有自己的效果、墨色和浓度。可以让它透出下面，也可以让它错位。主屏幕上的配方一点就叠好一整组，之后照样能改。"),

    "The portrait with an orange marker ring around the sunglasses, a black zigzag and three pink stars.": (
        "Das Porträt mit einem orangen Markerkreis um die Sonnenbrille, einem schwarzen Zickzack und drei pinken Sternen.",
        "El retrato con un círculo de rotulador naranja alrededor de las gafas de sol, un zigzag negro y tres estrellas rosas.",
        "El retrato con un círculo de plumón naranja alrededor de los lentes de sol, un zigzag negro y tres estrellas rosas.",
        "Le portrait avec un cercle de marqueur orange autour des lunettes, un zigzag noir et trois étoiles roses.",
        "Il ritratto con un cerchio di pennarello arancione intorno agli occhiali, uno zigzag nero e tre stelle rosa.",
        "サングラスをオレンジのマーカーで囲み、黒いジグザグとピンクの星を3つ描き込んだポートレート。",
        "선글라스 둘레에 주황색 마커 동그라미, 검은 지그재그, 분홍 별 세 개를 그린 인물 사진.",
        "Het portret met een oranje stiftcirkel om de zonnebril, een zwarte zigzag en drie roze sterren.",
        "O retrato com um círculo de marcador laranja em volta dos óculos, um zigue-zague preto e três estrelas rosa.",
        "肖像的墨镜被橙色马克笔圈起来，旁边有一道黑色锯齿线和三颗粉色星星。"),

    "Scribble": (
        "Kritzeln", "Garabato", "Garabato", "Gribouillis", "Scarabocchi", "落書き", "낙서",
        "Krabbel", "Rabisco", "涂鸦"),

    "Draw on it": (
        "Zeichne darauf", "Dibuja encima", "Dibuja encima", "Dessine dessus", "Disegnaci sopra",
        "上から描く", "위에 그리기", "Teken erop", "Desenhe por cima", "在上面画"),

    "Marker, pen, spray, splat and stencil, in black, white, orange, pink or blue. Rough or clean. Scribbles sit on their own sheet, over or under the prints.": (
        "Marker, Stift, Spray, Klecks und Schablone, in Schwarz, Weiß, Orange, Pink oder Blau. Roh oder sauber. Kritzeleien liegen auf einem eigenen Blatt, über oder unter den Drucken.",
        "Rotulador, bolígrafo, espray, salpicadura y plantilla, en negro, blanco, naranja, rosa o azul. En bruto o limpio. Los garabatos van en su propia capa, encima o debajo de las impresiones.",
        "Plumón, pluma, aerosol, salpicadura y esténcil, en negro, blanco, naranja, rosa o azul. En bruto o limpio. Los garabatos van en su propia capa, encima o debajo de las impresiones.",
        "Marqueur, stylo, bombe, éclaboussure et pochoir, en noir, blanc, orange, rose ou bleu. Brut ou net. Les gribouillis ont leur propre couche, au-dessus ou en dessous des tirages.",
        "Pennarello, penna, spray, schizzo e stencil, in nero, bianco, arancione, rosa o blu. Grezzo o pulito. Gli scarabocchi stanno su un livello tutto loro, sopra o sotto le stampe.",
        "マーカー、ペン、スプレー、しぶき、ステンシル。色は黒、白、オレンジ、ピンク、青。ラフにも、きれいにも。落書きは専用の版にのるので、プリントの上にも下にも置けます。",
        "마커, 펜, 스프레이, 물감 튀김, 스텐실. 검정, 흰색, 주황, 분홍, 파랑으로. 거칠게도, 깨끗하게도. 낙서는 따로 한 장에 담겨서 인쇄물 위나 아래에 둘 수 있어요.",
        "Stift, pen, spuitbus, spetter en sjabloon, in zwart, wit, oranje, roze of blauw. Ruw of schoon. Krabbels krijgen hun eigen laag, boven of onder de afdrukken.",
        "Marcador, caneta, spray, respingo e estêncil, em preto, branco, laranja, rosa ou azul. Bruto ou limpo. Os rabiscos ficam numa camada própria, acima ou abaixo das impressões.",
        "马克笔、钢笔、喷漆、泼溅和模板，黑、白、橙、粉、蓝五色。可以粗糙，也可以干净。涂鸦单独占一层，放在印刷层的上面或下面都行。"),

    "The portrait cut out with a white sticker edge, on a pink halftone background.": (
        "Das Porträt, mit weißem Stickerrand ausgeschnitten, auf pinkem Rasterhintergrund.",
        "El retrato recortado con borde blanco de pegatina, sobre un fondo de trama rosa.",
        "El retrato recortado con borde blanco de calcomanía, sobre un fondo de trama rosa.",
        "Le portrait découpé avec un bord blanc d'autocollant, sur un fond de trame rose.",
        "Il ritratto ritagliato con un bordo bianco da adesivo, su uno sfondo a retino rosa.",
        "白いシールのふちで切り抜いたポートレート。背景はピンクの網点。",
        "흰 스티커 테두리로 오려낸 인물 사진, 분홍 망점 배경 위에.",
        "Het portret uitgeknipt met een witte stickerrand, op een roze rasterachtergrond.",
        "O retrato recortado com borda branca de adesivo, sobre um fundo de retícula rosa.",
        "用白色贴纸边抠出来的肖像，背景是粉色网点。"),

    "Cut": (
        "Ausschneiden", "Recortar", "Recortar", "Découper", "Ritaglia", "切り抜き", "자르기",
        "Knippen", "Recortar", "剪切"),

    "Cut out the subject": (
        "Motiv ausschneiden", "Recorta el sujeto", "Recorta el sujeto", "Découpe le sujet",
        "Ritaglia il soggetto", "被写体を切り抜く", "피사체 오려내기", "Knip het onderwerp uit",
        "Recorte o assunto", "抠出主体"),

    "GRNGE finds the person, pet or object in the photo and cuts it out with a clean, torn or sticker edge. Drag, pinch and twist to place it.": (
        "GRNGE findet die Person, das Tier oder den Gegenstand im Foto und schneidet es mit sauberem, gerissenem oder Sticker-Rand aus. Ziehen, zoomen und drehen, um es zu platzieren.",
        "GRNGE encuentra a la persona, la mascota o el objeto de la foto y lo recorta con un borde limpio, rasgado o de pegatina. Arrastra, pellizca y gira para colocarlo.",
        "GRNGE encuentra a la persona, la mascota o el objeto de la foto y lo recorta con un borde limpio, rasgado o de calcomanía. Arrastra, pellizca y gira para colocarlo.",
        "GRNGE trouve la personne, l'animal ou l'objet dans la photo et le découpe avec un bord net, déchiré ou autocollant. Fais glisser, pince et tourne pour le placer.",
        "GRNGE trova la persona, l'animale o l'oggetto nella foto e lo ritaglia con un bordo pulito, strappato o da adesivo. Trascina, pizzica e ruota per posizionarlo.",
        "GRNGE が写真の中の人、ペット、モノを見つけて、きれい、ちぎり、シールのふちで切り抜きます。ドラッグ、ピンチ、回転で位置を決めます。",
        "GRNGE가 사진 속 사람, 반려동물, 물건을 찾아서 깨끗하게, 찢어서, 또는 스티커 테두리로 오려내요. 드래그, 핀치, 회전으로 위치를 잡으세요.",
        "GRNGE vindt de persoon, het huisdier of het voorwerp in de foto en knipt het uit met een schone, gescheurde of stickerrand. Sleep, knijp en draai om het te plaatsen.",
        "O GRNGE encontra a pessoa, o bicho ou o objeto na foto e recorta com borda limpa, rasgada ou de adesivo. Arraste, pince e gire para posicionar.",
        "GRNGE 会找出照片里的人、宠物或物体，用干净、撕边或贴纸边把它抠出来。拖动、捏合、旋转来摆放。"),

    "A black-and-white print of a crow with an orange burst and a crown stuck on it.": (
        "Ein Schwarz-Weiß-Druck einer Krähe mit einer orangen Explosion und einer Krone darauf.",
        "Una impresión en blanco y negro de un cuervo con un estallido naranja y una corona pegados.",
        "Una impresión en blanco y negro de un cuervo con un estallido naranja y una corona pegados.",
        "Un tirage noir et blanc d'un corbeau avec une explosion orange et une couronne collées dessus.",
        "Una stampa in bianco e nero di un corvo con un'esplosione arancione e una corona attaccate sopra.",
        "カラスの白黒プリントに、オレンジのバーストと王冠を貼ったもの。",
        "까마귀 흑백 인쇄물에 주황색 폭발과 왕관을 붙인 모습.",
        "Een zwart-witafdruk van een kraai met een oranje knal en een kroon erop geplakt.",
        "Uma impressão em preto e branco de um corvo com uma explosão laranja e uma coroa coladas.",
        "一张乌鸦的黑白印刷品，上面贴着橙色爆炸和一顶皇冠。"),

    "Stick": (
        "Kleben", "Pegar", "Pegar", "Coller", "Incolla", "貼る", "붙이기", "Plakken", "Colar", "贴纸"),

    "Stick things on": (
        "Kleb was drauf", "Pega cosas encima", "Pega cosas encima", "Colle des trucs dessus",
        "Attaccaci sopra qualcosa", "シールを貼る", "스티커 붙이기", "Plak er iets op",
        "Cole coisas por cima", "贴点东西上去"),

    "Bursts, stars, sparks, crowns, arrows, crosses, bolts, smileys and hearts, printed in the same inks with the same rough edge.": (
        "Explosionen, Sterne, Funken, Kronen, Pfeile, Kreuze, Blitze, Smileys und Herzen, gedruckt in denselben Tinten und mit demselben rauen Rand.",
        "Estallidos, estrellas, chispas, coronas, flechas, aspas, rayos, caritas sonrientes y corazones, impresos con las mismas tintas y el mismo borde áspero.",
        "Estallidos, estrellas, chispas, coronas, flechas, taches, rayos, caritas felices y corazones, impresos con las mismas tintas y el mismo borde áspero.",
        "Explosions, étoiles, étincelles, couronnes, flèches, croix, éclairs, smileys et cœurs, imprimés dans les mêmes encres avec le même bord brut.",
        "Esplosioni, stelle, scintille, corone, frecce, croci, fulmini, faccine e cuori, stampati con gli stessi inchiostri e lo stesso bordo grezzo.",
        "バースト、星、火花、王冠、矢印、バツ、稲妻、スマイル、ハート。どれも同じインクで、同じラフなふちで刷られます。",
        "폭발, 별, 불꽃, 왕관, 화살표, 엑스, 번개, 스마일, 하트. 모두 같은 잉크, 같은 거친 테두리로 인쇄돼요.",
        "Knallen, sterren, vonken, kronen, pijlen, kruizen, bliksems, smileys en harten, gedrukt in dezelfde inkten met dezelfde ruwe rand.",
        "Explosões, estrelas, faíscas, coroas, setas, xis, raios, carinhas e corações, impressos nas mesmas tintas com a mesma borda áspera.",
        "爆炸、星星、火花、皇冠、箭头、叉、闪电、笑脸和爱心，用同样的墨色、同样粗糙的边缘印出来。"),

    "The skateboarder printed on pink paper, with the filename grnge_0015 and the GRNGE stamp along the bottom.": (
        "Der Skateboarder auf pinkem Papier gedruckt, unten mit dem Dateinamen grnge_0015 und dem GRNGE-Stempel.",
        "El skater impreso en papel rosa, con el nombre de archivo grnge_0015 y el sello GRNGE en la parte de abajo.",
        "El patinador impreso en papel rosa, con el nombre de archivo grnge_0015 y el sello GRNGE en la parte de abajo.",
        "Le skateur imprimé sur du papier rose, avec le nom de fichier grnge_0015 et le tampon GRNGE en bas.",
        "Lo skater stampato su carta rosa, con il nome del file grnge_0015 e il timbro GRNGE in basso.",
        "ピンクの紙に刷ったスケーター。下にファイル名 grnge_0015 と GRNGE スタンプ。",
        "분홍 종이에 인쇄한 스케이트보더. 아래쪽에 파일 이름 grnge_0015와 GRNGE 스탬프.",
        "De skateboarder gedrukt op roze papier, onderaan de bestandsnaam grnge_0015 en de GRNGE-stempel.",
        "O skatista impresso em papel rosa, com o nome do arquivo grnge_0015 e o carimbo GRNGE embaixo.",
        "印在粉色纸上的滑手，底部有文件名 grnge_0015 和 GRNGE 印记。"),

    "Print": (
        "Drucken", "Imprimir", "Imprimir", "Imprimer", "Stampa", "プリント", "인쇄", "Afdrukken",
        "Imprimir", "打印"),

    "Print it": (
        "Druck es aus", "Imprímelo", "Imprímelo", "Imprime-le", "Stampalo", "プリントする",
        "인쇄하기", "Druk het af", "Imprima", "打印出来"),

    "Post, story, square or A3 poster. White, newsprint, kraft, pink or orange paper, or clear paper for a PNG with no background. Print saves it to Photos. Share sends it anywhere else.": (
        "Post, Story, Quadrat oder A3-Poster. Weißes Papier, Zeitungspapier, Kraftpapier, Pink oder Orange, oder transparentes Papier für ein PNG ohne Hintergrund. Drucken sichert es in Fotos. Teilen schickt es überallhin sonst.",
        "Post, historia, cuadrado o póster A3. Papel blanco, de periódico, kraft, rosa o naranja, o papel transparente para un PNG sin fondo. Imprimir la guarda en Fotos. Compartir la envía a cualquier otro sitio.",
        "Post, historia, cuadrado o póster A3. Papel blanco, periódico, kraft, rosa o naranja, o papel transparente para un PNG sin fondo. Imprimir la guarda en Fotos. Compartir la envía a cualquier otro lugar.",
        "Publication, story, carré ou affiche A3. Papier blanc, journal, kraft, rose ou orange, ou papier transparent pour un PNG sans fond. Imprimer l'enregistre dans Photos. Partager l'envoie partout ailleurs.",
        "Post, storia, quadrato o poster A3. Carta bianca, di giornale, kraft, rosa o arancione, oppure carta trasparente per un PNG senza sfondo. Stampa la salva in Foto. Condividi la manda ovunque.",
        "投稿、ストーリー、正方形、A3 ポスター。紙は白、新聞紙、クラフト、ピンク、オレンジ、または背景のない PNG になる透明な紙。プリントで写真に保存、共有でほかのどこへでも。",
        "게시물, 스토리, 정사각형, A3 포스터. 흰색, 신문 용지, 크래프트, 분홍, 주황 용지, 또는 배경 없는 PNG가 되는 투명 용지. 인쇄하면 사진에 저장되고, 공유로 어디든 보낼 수 있어요.",
        "Post, story, vierkant of A3-poster. Wit papier, krantenpapier, kraft, roze of oranje, of transparant papier voor een PNG zonder achtergrond. Afdrukken bewaart hem in Foto's. Deel stuurt hem overal anders heen.",
        "Post, story, quadrado ou pôster A3. Papel branco, jornal, kraft, rosa ou laranja, ou papel transparente para um PNG sem fundo. Imprimir salva em Fotos. Compartilhar manda para qualquer outro lugar.",
        "帖子、快拍、方形或 A3 海报。白纸、新闻纸、牛皮纸、粉色或橙色纸，或者用透明纸得到没有背景的 PNG。打印会存进照片，分享可以发到任何别处。"),

    "GRNGE is free to download and free to use. GRNGE Pro opens the rest.": (
        "GRNGE ist kostenlos zum Laden und zum Benutzen. GRNGE Pro schaltet den Rest frei.",
        "GRNGE es gratis para descargar y para usar. GRNGE Pro desbloquea el resto.",
        "GRNGE es gratis para descargar y para usar. GRNGE Pro desbloquea el resto.",
        "GRNGE est gratuit à télécharger et à utiliser. GRNGE Pro débloque le reste.",
        "GRNGE è gratis da scaricare e da usare. GRNGE Pro sblocca il resto.",
        "GRNGE はダウンロードも利用も無料。GRNGE Pro で残りのすべてが使えるようになります。",
        "GRNGE는 다운로드도 사용도 무료예요. GRNGE Pro로 나머지가 모두 열려요.",
        "GRNGE is gratis te downloaden en gratis te gebruiken. GRNGE Pro opent de rest.",
        "O GRNGE é grátis para baixar e para usar. O GRNGE Pro libera o resto.",
        "GRNGE 下载免费，使用也免费。GRNGE Pro 解锁其余全部。"),

    "Free": (
        "Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료", "Gratis", "Grátis", "免费"),

    "Photocopy and Stipple": (
        "Fotokopie und Punktiert", "Fotocopia y Puntillismo", "Fotocopia y Puntillismo",
        "Photocopie et Pointillé", "Fotocopia e Puntinato", "コピーと点描", "복사와 점묘",
        "Fotokopie en Stippel", "Fotocópia e Pontilhado", "复印和点描"),

    "Ink, Grit and Wear": (
        "Tinte, Körnung und Abnutzung", "Tinta, Grano y Desgaste", "Tinta, Grano y Desgaste",
        "Encre, Grain et Usure", "Inchiostro, Grana e Usura", "インク、ザラつき、劣化",
        "잉크, 거칠기, 닳음", "Inkt, Korrel en Slijtage", "Tinta, Granulado e Desgaste",
        "墨量、颗粒和磨损"),

    "Two sheets in the stack": (
        "Zwei Blätter im Stapel", "Dos capas", "Dos capas", "Deux couches", "Due livelli",
        "重ねられる版は2枚まで", "레이어 두 장", "Twee lagen", "Duas camadas", "两层叠层"),

    "Marker, pen and eraser": (
        "Marker, Stift und Radierer", "Rotulador, bolígrafo y borrador", "Plumón, pluma y borrador",
        "Marqueur, stylo et gomme", "Pennarello, penna e gomma", "マーカー、ペン、消しゴム",
        "마커, 펜, 지우개", "Stift, pen en gum", "Marcador, caneta e borracha", "马克笔、钢笔和橡皮"),

    "Burst, star and arrow stickers": (
        "Sticker: Explosion, Stern und Pfeil", "Pegatinas de estallido, estrella y flecha",
        "Calcomanías de estallido, estrella y flecha", "Autocollants explosion, étoile et flèche",
        "Adesivi esplosione, stella e freccia", "バースト、星、矢印のシール", "폭발, 별, 화살표 스티커",
        "Stickers: knal, ster en pijl", "Adesivos de explosão, estrela e seta", "爆炸、星星和箭头贴纸"),

    "1080 px prints with the GRNGE stamp, on white or newsprint": (
        "Drucke mit 1080 px und GRNGE-Stempel, auf Weiß oder Zeitungspapier",
        "Impresiones de 1080 px con el sello GRNGE, en papel blanco o de periódico",
        "Impresiones de 1080 px con el sello GRNGE, en papel blanco o periódico",
        "Tirages en 1080 px avec le tampon GRNGE, sur papier blanc ou journal",
        "Stampe a 1080 px con il timbro GRNGE, su carta bianca o di giornale",
        "GRNGE スタンプ入りの 1080 px プリント、白か新聞紙に",
        "GRNGE 스탬프가 찍힌 1080 px 인쇄, 흰색 또는 신문 용지",
        "Afdrukken van 1080 px met de GRNGE-stempel, op wit of krantenpapier",
        "Impressões de 1080 px com o carimbo GRNGE, em papel branco ou jornal",
        "带 GRNGE 印记的 1080 px 输出，白纸或新闻纸"),

    "Halftone and Dither": (
        "Raster und Dither", "Trama y Dither", "Trama y Dither", "Trame et Tramage",
        "Retino e Dither", "網点とディザ", "망점과 디더", "Raster en Dither", "Retícula e Dither",
        "网点和抖动"),

    "As many sheets as you like, in color inks, see-through and shifted": (
        "So viele Blätter, wie du willst, in farbigen Tinten, durchscheinend und versetzt",
        "Todas las capas que quieras, en tintas de color, transparentes y desplazadas",
        "Todas las capas que quieras, en tintas de color, transparentes y desfasadas",
        "Autant de couches que tu veux, en encres de couleur, transparentes et décalées",
        "Tutti i livelli che vuoi, con inchiostri colorati, trasparenti e spostati",
        "版はいくつでも。カラーインク、透け、ずらしも",
        "레이어 제한 없음. 컬러 잉크, 비침, 어긋남까지",
        "Zoveel lagen als je wilt, in kleurinkten, doorschijnend en verschoven",
        "Quantas camadas quiser, em tintas coloridas, transparentes e deslocadas",
        "叠层不限，彩色墨、透明叠印和错位"),

    "Spray, splat and stencil": (
        "Spray, Klecks und Schablone", "Espray, salpicadura y plantilla",
        "Aerosol, salpicadura y esténcil", "Bombe, éclaboussure et pochoir",
        "Spray, schizzo e stencil", "スプレー、しぶき、ステンシル", "스프레이, 물감 튀김, 스텐실",
        "Spuitbus, spetter en sjabloon", "Spray, respingo e estêncil", "喷漆、泼溅和模板"),

    "Cut-outs and every sticker": (
        "Ausschnitte und alle Sticker", "Recortes y todas las pegatinas",
        "Recortes y todas las calcomanías", "Découpes et tous les autocollants",
        "Ritagli e tutti gli adesivi", "切り抜きとすべてのシール", "오려내기와 모든 스티커",
        "Uitknipsels en alle stickers", "Recortes e todos os adesivos", "抠图和全部贴纸"),

    "Every paper stock": (
        "Alle Papiersorten", "Todos los papeles", "Todos los papeles", "Tous les papiers",
        "Tutte le carte", "すべての用紙", "모든 용지", "Alle papiersoorten", "Todos os papéis",
        "全部纸张"),

    "Full-size and A3 poster prints, stamp optional": (
        "Volle Größe und A3-Poster, Stempel optional", "Tamaño completo y póster A3, sello opcional",
        "Tamaño completo y póster A3, sello opcional", "Taille réelle et affiche A3, tampon facultatif",
        "Grandezza piena e poster A3, timbro facoltativo", "フルサイズと A3 ポスター、スタンプなしも可",
        "원본 크기와 A3 포스터 인쇄, 스탬프는 선택", "Ware grootte en A3-poster, stempel optioneel",
        "Tamanho real e pôster A3, carimbo opcional", "原尺寸和 A3 海报输出，印记可选"),

    "a year": (
        "pro Jahr", "al año", "al año", "par an", "all'anno", "年額", "연간", "per jaar", "por ano",
        "每年"),

    "7 days free": (
        "7 Tage gratis", "7 días gratis", "7 días gratis", "7 jours offerts", "7 giorni gratis",
        "7日間無料", "7일 무료", "7 dagen gratis", "7 dias grátis", "免费 7 天"),

    "a month": (
        "pro Monat", "al mes", "al mes", "par mois", "al mese", "月額", "월간", "per maand",
        "por mês", "每月"),

    "Pro tools work in the editor, so you can try them first. When you print, subscribe or print without them. The free week is on the yearly plan. Cancel any time in your Apple account. Prices shown in US dollars; the App Store shows yours.": (
        "Pro-Werkzeuge funktionieren im Editor, du kannst sie also erst ausprobieren. Beim Drucken abonnierst du oder druckst ohne sie. Die Gratiswoche gibt es beim Jahresabo. Kündigen kannst du jederzeit in deinem Apple-Konto. Preise in US-Dollar; der App Store zeigt deine.",
        "Las herramientas Pro funcionan en el editor, así que puedes probarlas antes. Al imprimir, te suscribes o imprimes sin ellas. La semana gratis es del plan anual. Cancela cuando quieras en tu cuenta de Apple. Precios en dólares estadounidenses; el App Store muestra los tuyos.",
        "Las herramientas Pro funcionan en el editor, así que puedes probarlas antes. Al imprimir, te suscribes o imprimes sin ellas. La semana gratis es del plan anual. Cancela cuando quieras en tu cuenta de Apple. Precios en dólares estadounidenses; el App Store muestra los tuyos.",
        "Les outils Pro fonctionnent dans l'éditeur, tu peux donc les essayer d'abord. Au moment d'imprimer, abonne-toi ou imprime sans eux. La semaine offerte concerne la formule annuelle. Résilie quand tu veux dans ton compte Apple. Prix indiqués en dollars américains ; l'App Store affiche les tiens.",
        "Gli strumenti Pro funzionano nell'editor, quindi puoi provarli prima. Quando stampi, ti abboni o stampi senza. La settimana gratis è sul piano annuale. Disdici quando vuoi nel tuo account Apple. Prezzi in dollari statunitensi; l'App Store mostra i tuoi.",
        "Pro のツールもエディタで使えるので、先に試せます。プリントするときに、登録するか、Pro なしでプリントするかを選べます。無料の1週間は年額プランのみ。解約は Apple アカウントでいつでも。価格は米ドル表示です。実際の価格は App Store に表示されます。",
        "Pro 도구도 편집기에서 쓸 수 있어서 먼저 써 볼 수 있어요. 인쇄할 때 구독하거나, Pro 없이 인쇄하면 돼요. 무료 1주일은 연간 플랜에만 있어요. 해지는 Apple 계정에서 언제든지. 가격은 미국 달러 기준이며, 실제 가격은 App Store에 표시돼요.",
        "Pro-gereedschap werkt in de editor, dus je kunt het eerst proberen. Bij het afdrukken neem je een abonnement of druk je af zonder. De gratis week hoort bij het jaarabonnement. Opzeggen kan altijd in je Apple-account. Prijzen in Amerikaanse dollars; de App Store toont de jouwe.",
        "As ferramentas Pro funcionam no editor, então você pode experimentar antes. Na hora de imprimir, assine ou imprima sem elas. A semana grátis é do plano anual. Cancele quando quiser na sua conta Apple. Preços em dólares americanos; a App Store mostra os seus.",
        "Pro 工具在编辑器里就能用，可以先试。打印时，订阅，或者不带它们打印。免费的一周只限年度方案。随时可在你的 Apple 账户中取消。价格以美元显示，App Store 会显示你所在地区的价格。"),

    "What it does not do": (
        "Was die App nicht tut", "Lo que no hace", "Lo que no hace", "Ce qu'elle ne fait pas",
        "Cosa non fa", "しないこと", "하지 않는 것", "Wat het niet doet", "O que ele não faz",
        "它不做的事"),

    "No account and nothing to sign in to. No advertising, no analytics, no tracking. The app has no network code: photos are processed on the phone and stay there unless you share them.": (
        "Kein Konto und nichts zum Anmelden. Keine Werbung, keine Analyse, kein Tracking. Die App hat keinen Netzwerkcode: Fotos werden auf dem Telefon verarbeitet und bleiben dort, solange du sie nicht teilst.",
        "Sin cuenta y sin nada en lo que iniciar sesión. Sin publicidad, sin analítica, sin rastreo. La app no tiene código de red: las fotos se procesan en el teléfono y se quedan ahí, salvo que las compartas.",
        "Sin cuenta y sin nada en lo que iniciar sesión. Sin publicidad, sin analítica, sin rastreo. La app no tiene código de red: las fotos se procesan en el teléfono y se quedan ahí, salvo que las compartas.",
        "Pas de compte, rien où se connecter. Pas de publicité, pas d'analyse d'audience, pas de pistage. L'app n'a aucun code réseau : les photos sont traitées sur le téléphone et y restent, sauf si tu les partages.",
        "Nessun account e niente a cui accedere. Nessuna pubblicità, nessuna analisi, nessun tracciamento. L'app non ha codice di rete: le foto vengono elaborate sul telefono e restano lì, a meno che tu non le condivida.",
        "アカウントも、サインインするものもありません。広告も、解析も、トラッキングもなし。アプリにはネットワークのコードがありません。写真は端末の中で処理され、共有しない限り端末から出ません。",
        "계정도, 로그인할 것도 없어요. 광고도, 분석도, 추적도 없어요. 앱에는 네트워크 코드가 없어서, 사진은 휴대폰 안에서 처리되고 공유하지 않는 한 그대로 남아요.",
        "Geen account en niets om op in te loggen. Geen advertenties, geen analytics, geen tracking. De app heeft geen netwerkcode: foto's worden op de telefoon verwerkt en blijven daar, tenzij je ze deelt.",
        "Sem conta e sem nada para entrar. Sem publicidade, sem análise, sem rastreamento. O app não tem código de rede: as fotos são processadas no telefone e ficam lá, a não ser que você as compartilhe.",
        "没有账户，也没有需要登录的东西。没有广告，没有分析，没有追踪。应用里没有联网代码：照片在手机上处理，除非你分享，否则一直留在手机里。"),

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

    "Questions": (
        "Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問", "자주 묻는 질문",
        "Vragen", "Perguntas", "常见问题"),

    "Is GRNGE free?": (
        "Ist GRNGE kostenlos?", "¿GRNGE es gratis?", "¿GRNGE es gratis?", "GRNGE est-il gratuit ?",
        "GRNGE è gratis?", "GRNGE は無料ですか？", "GRNGE는 무료인가요?", "Is GRNGE gratis?",
        "O GRNGE é grátis?", "GRNGE 免费吗？"),

    "Yes, to download and to use. Photocopy and Stipple, two sheets, marker and pen, and 1080 px prints with the GRNGE stamp are free. GRNGE Pro opens everything else at 5.99 US dollars a month or 29.99 a year, and the yearly plan starts with a free week. Cancel any time in your Apple account.": (
        "Ja, zum Laden und zum Benutzen. Fotokopie und Punktiert, zwei Blätter, Marker und Stift sowie Drucke mit 1080 px und GRNGE-Stempel sind kostenlos. GRNGE Pro schaltet alles andere frei, für 5,99 US-Dollar im Monat oder 29,99 im Jahr, und das Jahresabo beginnt mit einer Gratiswoche. Kündigen kannst du jederzeit in deinem Apple-Konto.",
        "Sí, para descargar y para usar. Fotocopia y Puntillismo, dos capas, rotulador y bolígrafo, e impresiones de 1080 px con el sello GRNGE son gratis. GRNGE Pro desbloquea todo lo demás por 5,99 dólares estadounidenses al mes o 29,99 al año, y el plan anual empieza con una semana gratis. Cancela cuando quieras en tu cuenta de Apple.",
        "Sí, para descargar y para usar. Fotocopia y Puntillismo, dos capas, plumón y pluma, e impresiones de 1080 px con el sello GRNGE son gratis. GRNGE Pro desbloquea todo lo demás por 5.99 dólares estadounidenses al mes o 29.99 al año, y el plan anual empieza con una semana gratis. Cancela cuando quieras en tu cuenta de Apple.",
        "Oui, à télécharger et à utiliser. Photocopie et Pointillé, deux couches, le marqueur et le stylo, et des tirages en 1080 px avec le tampon GRNGE sont gratuits. GRNGE Pro débloque tout le reste pour 5,99 dollars américains par mois ou 29,99 par an, et la formule annuelle commence par une semaine offerte. Résilie quand tu veux dans ton compte Apple.",
        "Sì, da scaricare e da usare. Fotocopia e Puntinato, due livelli, pennarello e penna e stampe a 1080 px con il timbro GRNGE sono gratis. GRNGE Pro sblocca tutto il resto a 5,99 dollari statunitensi al mese o 29,99 all'anno, e il piano annuale parte con una settimana gratis. Disdici quando vuoi nel tuo account Apple.",
        "はい、ダウンロードも利用も無料です。コピーと点描、2枚の版、マーカーとペン、GRNGE スタンプ入りの 1080 px プリントは無料。GRNGE Pro ではほかのすべてが使えるようになり、月額 5.99 米ドルまたは年額 29.99 米ドル。年額プランは最初の1週間が無料です。解約は Apple アカウントでいつでもできます。",
        "네, 다운로드도 사용도 무료예요. 복사와 점묘, 레이어 두 장, 마커와 펜, GRNGE 스탬프가 찍힌 1080 px 인쇄는 무료예요. GRNGE Pro는 나머지를 모두 열어 주며, 월 5.99 미국 달러 또는 연 29.99 미국 달러예요. 연간 플랜은 첫 1주일이 무료예요. 해지는 Apple 계정에서 언제든지 할 수 있어요.",
        "Ja, om te downloaden en te gebruiken. Fotokopie en Stippel, twee lagen, stift en pen, en afdrukken van 1080 px met de GRNGE-stempel zijn gratis. GRNGE Pro opent al het andere voor 5,99 Amerikaanse dollar per maand of 29,99 per jaar, en het jaarabonnement begint met een gratis week. Opzeggen kan altijd in je Apple-account.",
        "Sim, para baixar e para usar. Fotocópia e Pontilhado, duas camadas, marcador e caneta, e impressões de 1080 px com o carimbo GRNGE são grátis. O GRNGE Pro libera todo o resto por 5,99 dólares americanos por mês ou 29,99 por ano, e o plano anual começa com uma semana grátis. Cancele quando quiser na sua conta Apple.",
        "是的，下载和使用都免费。复印和点描、两层叠层、马克笔和钢笔，以及带 GRNGE 印记的 1080 px 输出都是免费的。GRNGE Pro 解锁其余全部，每月 5.99 美元或每年 29.99 美元，年度方案首周免费。随时可在你的 Apple 账户中取消。"),

    "Does it print on paper?": (
        "Druckt die App auf Papier?", "¿Imprime en papel?", "¿Imprime en papel?",
        "Est-ce que ça imprime sur papier ?", "Stampa su carta?", "紙に印刷されるのですか？",
        "종이에 인쇄되나요?", "Drukt het af op papier?", "Ele imprime em papel?", "会打印到纸上吗？"),

    "No. Print makes an image and saves it to Photos, sized for a post, a story, a square or an A3 poster. The paper color is part of the picture. The poster size is 300 dpi, so a print shop can print it.": (
        "Nein. Drucken erzeugt ein Bild und sichert es in Fotos, in der Größe für einen Post, eine Story, ein Quadrat oder ein A3-Poster. Die Papierfarbe ist Teil des Bildes. Die Postergröße hat 300 dpi, eine Druckerei kann sie also drucken.",
        "No. Imprimir crea una imagen y la guarda en Fotos, al tamaño de un post, una historia, un cuadrado o un póster A3. El color del papel forma parte de la imagen. El tamaño póster es de 300 ppp, así que una imprenta puede imprimirlo.",
        "No. Imprimir crea una imagen y la guarda en Fotos, al tamaño de un post, una historia, un cuadrado o un póster A3. El color del papel forma parte de la imagen. El tamaño póster es de 300 ppp, así que una imprenta puede imprimirlo.",
        "Non. Imprimer crée une image et l'enregistre dans Photos, au format d'une publication, d'une story, d'un carré ou d'une affiche A3. La couleur du papier fait partie de l'image. Le format affiche est en 300 dpi, un imprimeur peut donc l'imprimer.",
        "No. Stampa crea un'immagine e la salva in Foto, nel formato di un post, una storia, un quadrato o un poster A3. Il colore della carta fa parte dell'immagine. Il formato poster è a 300 dpi, quindi una tipografia può stamparlo.",
        "いいえ。プリントは画像を作って写真に保存します。サイズは投稿、ストーリー、正方形、A3 ポスターから選べます。紙の色も画像の一部です。ポスターサイズは 300 dpi なので、印刷所で刷れます。",
        "아니요. 인쇄하면 이미지가 만들어져 사진에 저장돼요. 크기는 게시물, 스토리, 정사각형, A3 포스터 중에서 골라요. 용지 색도 이미지의 일부예요. 포스터 크기는 300 dpi라서 인쇄소에서 뽑을 수 있어요.",
        "Nee. Afdrukken maakt een afbeelding en bewaart die in Foto's, op het formaat van een post, een story, een vierkant of een A3-poster. De papierkleur hoort bij het beeld. Het posterformaat is 300 dpi, dus een drukkerij kan het drukken.",
        "Não. Imprimir cria uma imagem e salva em Fotos, no tamanho de um post, um story, um quadrado ou um pôster A3. A cor do papel faz parte da imagem. O tamanho pôster tem 300 dpi, então uma gráfica pode imprimir.",
        "不会。打印会生成一张图片并存进照片，尺寸可选帖子、快拍、方形或 A3 海报。纸张颜色是画面的一部分。海报尺寸为 300 dpi，印刷店可以直接印。"),

    "Do my photos leave my phone?": (
        "Verlassen meine Fotos mein Telefon?", "¿Mis fotos salen de mi teléfono?",
        "¿Mis fotos salen de mi teléfono?", "Mes photos quittent-elles mon téléphone ?",
        "Le mie foto escono dal telefono?", "写真が端末の外に出ることはありますか？",
        "내 사진이 휴대폰 밖으로 나가나요?", "Verlaten mijn foto's mijn telefoon?",
        "Minhas fotos saem do meu telefone?", "我的照片会离开手机吗？"),

    "No. Every effect runs on the phone, and the app has no network code. A print leaves only when you share it.": (
        "Nein. Jeder Effekt läuft auf dem Telefon, und die App hat keinen Netzwerkcode. Ein Druck verlässt es nur, wenn du ihn teilst.",
        "No. Todos los efectos se ejecutan en el teléfono, y la app no tiene código de red. Una impresión solo sale cuando la compartes.",
        "No. Todos los efectos se ejecutan en el teléfono, y la app no tiene código de red. Una impresión solo sale cuando la compartes.",
        "Non. Chaque effet tourne sur le téléphone, et l'app n'a aucun code réseau. Un tirage ne part que si tu le partages.",
        "No. Ogni effetto gira sul telefono, e l'app non ha codice di rete. Una stampa esce solo quando la condividi.",
        "いいえ。エフェクトはすべて端末の中で動き、アプリにはネットワークのコードがありません。プリントが外に出るのは、あなたが共有したときだけです。",
        "아니요. 모든 효과는 휴대폰 안에서 처리되고, 앱에는 네트워크 코드가 없어요. 인쇄물은 직접 공유할 때만 밖으로 나가요.",
        "Nee. Elk effect draait op de telefoon, en de app heeft geen netwerkcode. Een afdruk gaat alleen weg als je hem deelt.",
        "Não. Todos os efeitos rodam no telefone, e o app não tem código de rede. Uma impressão só sai quando você compartilha.",
        "不会。所有效果都在手机上运行，应用里也没有联网代码。只有你分享时，作品才会离开手机。"),

    "Which photos work?": (
        "Welche Fotos funktionieren?", "¿Qué fotos funcionan?", "¿Qué fotos funcionan?",
        "Quelles photos marchent ?", "Quali foto funzionano?", "どんな写真でも使えますか？",
        "어떤 사진이든 되나요?", "Welke foto's werken?", "Quais fotos funcionam?", "什么照片都可以吗？"),

    "Any photo from your library, or one you take in the app. Dark and flat photos are evened out before they print. Cutting out needs a clear subject: a person, a pet or an object.": (
        "Jedes Foto aus deiner Mediathek oder eins, das du in der App aufnimmst. Dunkle und flaue Fotos werden vor dem Drucken ausgeglichen. Zum Ausschneiden braucht es ein klares Motiv: eine Person, ein Tier oder einen Gegenstand.",
        "Cualquier foto de tu fototeca, o una que hagas desde la app. Las fotos oscuras o planas se equilibran antes de imprimirse. Para recortar hace falta un sujeto claro: una persona, una mascota o un objeto.",
        "Cualquier foto de tu fototeca, o una que tomes desde la app. Las fotos oscuras o planas se equilibran antes de imprimirse. Para recortar hace falta un sujeto claro: una persona, una mascota o un objeto.",
        "N'importe quelle photo de ta photothèque, ou une que tu prends dans l'app. Les photos sombres ou ternes sont rééquilibrées avant l'impression. Pour découper, il faut un sujet net : une personne, un animal ou un objet.",
        "Qualsiasi foto della tua libreria, o una che scatti nell'app. Le foto scure o piatte vengono bilanciate prima della stampa. Per ritagliare serve un soggetto chiaro: una persona, un animale o un oggetto.",
        "ライブラリの写真でも、アプリで撮った写真でも使えます。暗い写真や眠い写真は、プリントの前に整えられます。切り抜きには、人、ペット、モノなど、はっきりした被写体が必要です。",
        "보관함의 사진이든, 앱에서 찍은 사진이든 다 돼요. 어둡거나 밋밋한 사진은 인쇄 전에 고르게 맞춰져요. 오려내기에는 사람, 반려동물, 물건처럼 뚜렷한 피사체가 필요해요.",
        "Elke foto uit je bibliotheek, of een die je in de app maakt. Donkere en vlakke foto's worden vóór het afdrukken bijgetrokken. Uitknippen werkt met een duidelijk onderwerp: een persoon, een huisdier of een voorwerp.",
        "Qualquer foto da sua fototeca, ou uma que você tirar no app. Fotos escuras ou sem contraste são equilibradas antes de imprimir. Para recortar, é preciso um assunto claro: uma pessoa, um bicho ou um objeto.",
        "图库里的任何照片都行，也可以在应用里拍。偏暗或发灰的照片会在打印前自动调匀。抠图需要一个清楚的主体：人、宠物或物体。"),

    "Do I need an account?": (
        "Brauche ich ein Konto?", "¿Necesito una cuenta?", "¿Necesito una cuenta?",
        "Faut-il un compte ?", "Serve un account?", "アカウントは必要ですか？", "계정이 필요한가요?",
        "Heb ik een account nodig?", "Preciso de uma conta?", "需要账户吗？"),

    "No. There is nothing to sign up for. Your prints are kept in the app on your phone, and in Photos once you print them.": (
        "Nein. Es gibt nichts, wofür du dich anmelden musst. Deine Drucke bleiben in der App auf deinem Telefon, und in Fotos, sobald du sie druckst.",
        "No. No hay nada en lo que registrarse. Tus impresiones se guardan en la app, en tu teléfono, y en Fotos cuando las imprimes.",
        "No. No hay nada en lo que registrarse. Tus impresiones se guardan en la app, en tu teléfono, y en Fotos cuando las imprimes.",
        "Non. Il n'y a rien à quoi s'inscrire. Tes tirages sont gardés dans l'app sur ton téléphone, et dans Photos une fois imprimés.",
        "No. Non c'è niente a cui iscriversi. Le tue stampe restano nell'app sul telefono, e in Foto quando le stampi.",
        "いいえ。登録するものは何もありません。プリントは端末のアプリの中に残り、プリントすると写真にも保存されます。",
        "아니요. 가입할 것이 없어요. 인쇄물은 휴대폰의 앱 안에 보관되고, 인쇄하면 사진에도 저장돼요.",
        "Nee. Er is niets om je voor aan te melden. Je afdrukken blijven in de app op je telefoon, en in Foto's zodra je ze afdrukt.",
        "Não. Não há nada para se cadastrar. Suas impressões ficam no app, no seu telefone, e em Fotos quando você imprime.",
        "不需要。没有任何需要注册的东西。你的作品保存在手机上的应用里，打印后也会存进照片。"),

    "Privacy": (
        "Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy", "プライバシー",
        "개인정보", "Privacy", "Privacidade", "隐私"),

    "Also here:": (
        "Auch hier:", "También aquí:", "También aquí:", "Aussi ici :", "Anche qui:", "こちらも：",
        "이곳의 다른 앱:", "Ook hier:", "Também aqui:", "这里还有："),

    ", which turns photos into cyanotypes.": (
        ", das Fotos in Cyanotypien verwandelt.",
        ", que convierte fotos en cianotipias.",
        ", que convierte fotos en cianotipias.",
        ", qui transforme les photos en cyanotypes.",
        ", che trasforma le foto in cianotipie.",
        "、写真をサイアノタイプにするアプリ。",
        ", 사진을 시아노타입으로 바꿔 주는 앱.",
        ", dat foto's in cyanotypieën verandert.",
        ", que transforma fotos em cianótipos.",
        "，把照片变成蓝晒。"),

    # ------------------------------------------------------------------ JSON-LD only

    "A photo effects app for iPhone that turns photos into black-and-white prints: Photocopy, Stipple, Halftone and Dither. Prints can be layered in color inks, drawn on, cut out around the subject with a clean, torn or sticker edge, decorated with stickers, and saved at post, story, square or A3 poster size on white, newsprint, kraft, pink, orange or clear paper.": (
        "Eine Fotoeffekt-App fürs iPhone, die Fotos in Schwarz-Weiß-Drucke verwandelt: Fotokopie, Punktiert, Raster und Dither. Drucke lassen sich in farbigen Tinten übereinanderlegen, bemalen, mit sauberem, gerissenem oder Sticker-Rand um das Motiv ausschneiden, mit Stickern bekleben und als Post, Story, Quadrat oder A3-Poster auf weißem Papier, Zeitungspapier, Kraftpapier, Pink, Orange oder transparent sichern.",
        "Una app de efectos de foto para iPhone que convierte fotos en impresiones en blanco y negro: Fotocopia, Puntillismo, Trama y Dither. Las impresiones se pueden superponer en tintas de color, dibujar, recortar alrededor del sujeto con borde limpio, rasgado o de pegatina, decorar con pegatinas y guardar en tamaño post, historia, cuadrado o póster A3 sobre papel blanco, de periódico, kraft, rosa, naranja o transparente.",
        "Una app de efectos de foto para iPhone que convierte fotos en impresiones en blanco y negro: Fotocopia, Puntillismo, Trama y Dither. Las impresiones se pueden superponer en tintas de color, dibujar, recortar alrededor del sujeto con borde limpio, rasgado o de calcomanía, decorar con calcomanías y guardar en tamaño post, historia, cuadrado o póster A3 sobre papel blanco, periódico, kraft, rosa, naranja o transparente.",
        "Une app d'effets photo pour iPhone qui transforme les photos en tirages noir et blanc : Photocopie, Pointillé, Trame et Tramage. Les tirages peuvent être superposés en encres de couleur, dessinés, découpés autour du sujet avec un bord net, déchiré ou autocollant, décorés d'autocollants et enregistrés au format publication, story, carré ou affiche A3 sur papier blanc, journal, kraft, rose, orange ou transparent.",
        "Un'app di effetti foto per iPhone che trasforma le foto in stampe in bianco e nero: Fotocopia, Puntinato, Retino e Dither. Le stampe si possono sovrapporre con inchiostri colorati, disegnare, ritagliare intorno al soggetto con un bordo pulito, strappato o da adesivo, decorare con adesivi e salvare in formato post, storia, quadrato o poster A3 su carta bianca, di giornale, kraft, rosa, arancione o trasparente.",
        "写真を白黒のプリントにする iPhone の写真エフェクトアプリ。コピー、点描、網点、ディザ。プリントはカラーインクで重ねたり、上から描いたり、被写体をきれい、ちぎり、シールのふちで切り抜いたり、シールを貼ったりでき、投稿、ストーリー、正方形、A3 ポスターのサイズで、白、新聞紙、クラフト、ピンク、オレンジ、透明の紙に保存できます。",
        "사진을 흑백 인쇄물로 바꾸는 iPhone 사진 효과 앱. 복사, 점묘, 망점, 디더. 인쇄물은 컬러 잉크로 겹치고, 위에 그리고, 깨끗한, 찢은, 스티커 테두리로 피사체를 오려내고, 스티커를 붙여서 게시물, 스토리, 정사각형, A3 포스터 크기로 흰색, 신문 용지, 크래프트, 분홍, 주황, 투명 용지에 저장할 수 있다.",
        "Een foto-effectenapp voor iPhone die foto's omzet in zwart-witafdrukken: Fotokopie, Stippel, Raster en Dither. Afdrukken kun je in kleurinkten over elkaar leggen, bekrabbelen, rond het onderwerp uitknippen met een schone, gescheurde of stickerrand, beplakken met stickers en bewaren als post, story, vierkant of A3-poster op wit papier, krantenpapier, kraft, roze, oranje of transparant papier.",
        "Um app de efeitos de foto para iPhone que transforma fotos em impressões em preto e branco: Fotocópia, Pontilhado, Retícula e Dither. As impressões podem ser sobrepostas em tintas coloridas, rabiscadas, recortadas em volta do assunto com borda limpa, rasgada ou de adesivo, decoradas com adesivos e salvas em tamanho post, story, quadrado ou pôster A3 em papel branco, jornal, kraft, rosa, laranja ou transparente.",
        "一款把照片变成黑白印刷品的 iPhone 照片效果应用：复印、点描、网点和抖动。作品可以用彩色墨叠印、在上面涂鸦、用干净、撕边或贴纸边抠出主体、贴上贴纸，并按帖子、快拍、方形或 A3 海报尺寸，保存在白纸、新闻纸、牛皮纸、粉色、橙色或透明纸上。"),

    "Four black-and-white effects: Photocopy, Stipple, Halftone and Dither": (
        "Vier Schwarz-Weiß-Effekte: Fotokopie, Punktiert, Raster und Dither",
        "Cuatro efectos en blanco y negro: Fotocopia, Puntillismo, Trama y Dither",
        "Cuatro efectos en blanco y negro: Fotocopia, Puntillismo, Trama y Dither",
        "Quatre effets noir et blanc : Photocopie, Pointillé, Trame et Tramage",
        "Quattro effetti in bianco e nero: Fotocopia, Puntinato, Retino e Dither",
        "4つの白黒エフェクト：コピー、点描、網点、ディザ",
        "네 가지 흑백 효과: 복사, 점묘, 망점, 디더",
        "Vier zwart-witeffecten: Fotokopie, Stippel, Raster en Dither",
        "Quatro efeitos em preto e branco: Fotocópia, Pontilhado, Retícula e Dither",
        "四种黑白效果：复印、点描、网点和抖动"),

    "Three dials on every effect: Ink, Grit and Wear": (
        "Drei Regler für jeden Effekt: Tinte, Körnung und Abnutzung",
        "Tres controles en cada efecto: Tinta, Grano y Desgaste",
        "Tres controles en cada efecto: Tinta, Grano y Desgaste",
        "Trois réglages sur chaque effet : Encre, Grain et Usure",
        "Tre cursori su ogni effetto: Inchiostro, Grana e Usura",
        "どのエフェクトにも3つのダイヤル：インク、ザラつき、劣化",
        "모든 효과에 세 가지 다이얼: 잉크, 거칠기, 닳음",
        "Drie schuiven bij elk effect: Inkt, Korrel en Slijtage",
        "Três controles em cada efeito: Tinta, Granulado e Desgaste",
        "每种效果都有三个旋钮：墨量、颗粒和磨损"),

    "Stack prints of the same photo in black, orange, pink and blue inks, see-through and shifted": (
        "Drucke desselben Fotos in schwarzer, oranger, pinker und blauer Tinte stapeln, durchscheinend und versetzt",
        "Superpone impresiones de la misma foto en tintas negra, naranja, rosa y azul, transparentes y desplazadas",
        "Superpone impresiones de la misma foto en tintas negra, naranja, rosa y azul, transparentes y desfasadas",
        "Superpose des tirages de la même photo en encres noire, orange, rose et bleue, transparents et décalés",
        "Sovrapponi stampe della stessa foto con inchiostri nero, arancione, rosa e blu, trasparenti e spostate",
        "同じ写真のプリントを黒、オレンジ、ピンク、青のインクで重ねる。透けもずらしも",
        "같은 사진의 인쇄물을 검정, 주황, 분홍, 파랑 잉크로 겹치기, 비침과 어긋남까지",
        "Afdrukken van dezelfde foto stapelen in zwarte, oranje, roze en blauwe inkt, doorschijnend en verschoven",
        "Sobreponha impressões da mesma foto em tintas preta, laranja, rosa e azul, transparentes e deslocadas",
        "把同一张照片的印刷层用黑、橙、粉、蓝墨叠在一起，可透明叠印、可错位"),

    "Scribble with marker, pen, spray, splat and stencil": (
        "Kritzeln mit Marker, Stift, Spray, Klecks und Schablone",
        "Garabatea con rotulador, bolígrafo, espray, salpicadura y plantilla",
        "Garabatea con plumón, pluma, aerosol, salpicadura y esténcil",
        "Gribouille au marqueur, au stylo, à la bombe, à l'éclaboussure et au pochoir",
        "Scarabocchia con pennarello, penna, spray, schizzo e stencil",
        "マーカー、ペン、スプレー、しぶき、ステンシルで落書き",
        "마커, 펜, 스프레이, 물감 튀김, 스텐실로 낙서",
        "Krabbelen met stift, pen, spuitbus, spetter en sjabloon",
        "Rabisque com marcador, caneta, spray, respingo e estêncil",
        "用马克笔、钢笔、喷漆、泼溅和模板涂鸦"),

    "Cut out the subject with a clean, torn or sticker edge": (
        "Das Motiv mit sauberem, gerissenem oder Sticker-Rand ausschneiden",
        "Recorta el sujeto con borde limpio, rasgado o de pegatina",
        "Recorta el sujeto con borde limpio, rasgado o de calcomanía",
        "Découpe le sujet avec un bord net, déchiré ou autocollant",
        "Ritaglia il soggetto con un bordo pulito, strappato o da adesivo",
        "被写体を、きれい、ちぎり、シールのふちで切り抜く",
        "피사체를 깨끗한, 찢은, 스티커 테두리로 오려내기",
        "Knip het onderwerp uit met een schone, gescheurde of stickerrand",
        "Recorte o assunto com borda limpa, rasgada ou de adesivo",
        "用干净、撕边或贴纸边抠出主体"),

    "Stickers printed in the same inks": (
        "Sticker, gedruckt in denselben Tinten",
        "Pegatinas impresas con las mismas tintas",
        "Calcomanías impresas con las mismas tintas",
        "Des autocollants imprimés dans les mêmes encres",
        "Adesivi stampati con gli stessi inchiostri",
        "同じインクで刷られるシール",
        "같은 잉크로 인쇄되는 스티커",
        "Stickers, gedrukt in dezelfde inkten",
        "Adesivos impressos nas mesmas tintas",
        "用同样墨色印出的贴纸"),

    "Save at post, story, square or A3 poster size, on colored or clear paper": (
        "Sichern als Post, Story, Quadrat oder A3-Poster, auf farbigem oder transparentem Papier",
        "Guarda en tamaño post, historia, cuadrado o póster A3, en papel de color o transparente",
        "Guarda en tamaño post, historia, cuadrado o póster A3, en papel de color o transparente",
        "Enregistre au format publication, story, carré ou affiche A3, sur papier de couleur ou transparent",
        "Salva in formato post, storia, quadrato o poster A3, su carta colorata o trasparente",
        "投稿、ストーリー、正方形、A3 ポスターのサイズで、色紙や透明な紙に保存",
        "게시물, 스토리, 정사각형, A3 포스터 크기로, 컬러 또는 투명 용지에 저장",
        "Bewaren als post, story, vierkant of A3-poster, op gekleurd of transparant papier",
        "Salve em tamanho post, story, quadrado ou pôster A3, em papel colorido ou transparente",
        "按帖子、快拍、方形或 A3 海报尺寸保存，可用彩色纸或透明纸"),

    "No account, no network code, photos processed on the phone": (
        "Kein Konto, kein Netzwerkcode, Fotos werden auf dem Telefon verarbeitet",
        "Sin cuenta, sin código de red, fotos procesadas en el teléfono",
        "Sin cuenta, sin código de red, fotos procesadas en el teléfono",
        "Pas de compte, pas de code réseau, photos traitées sur le téléphone",
        "Nessun account, nessun codice di rete, foto elaborate sul telefono",
        "アカウントなし、ネットワークのコードなし、写真は端末の中で処理",
        "계정 없음, 네트워크 코드 없음, 사진은 휴대폰 안에서 처리",
        "Geen account, geen netwerkcode, foto's verwerkt op de telefoon",
        "Sem conta, sem código de rede, fotos processadas no telefone",
        "无需账户，没有联网代码，照片在手机上处理"),

    "Free to download, with Photocopy and Stipple, two sheets, marker and pen, and 1080 px prints with the GRNGE stamp. GRNGE Pro opens everything else at 5.99 US dollars a month or 29.99 a year, and the yearly plan starts with a free week.": (
        "Kostenlos zum Laden, mit Fotokopie und Punktiert, zwei Blättern, Marker und Stift sowie Drucken mit 1080 px und GRNGE-Stempel. GRNGE Pro schaltet alles andere frei, für 5,99 US-Dollar im Monat oder 29,99 im Jahr, und das Jahresabo beginnt mit einer Gratiswoche.",
        "Gratis para descargar, con Fotocopia y Puntillismo, dos capas, rotulador y bolígrafo, e impresiones de 1080 px con el sello GRNGE. GRNGE Pro desbloquea todo lo demás por 5,99 dólares estadounidenses al mes o 29,99 al año, y el plan anual empieza con una semana gratis.",
        "Gratis para descargar, con Fotocopia y Puntillismo, dos capas, plumón y pluma, e impresiones de 1080 px con el sello GRNGE. GRNGE Pro desbloquea todo lo demás por 5.99 dólares estadounidenses al mes o 29.99 al año, y el plan anual empieza con una semana gratis.",
        "Gratuit à télécharger, avec Photocopie et Pointillé, deux couches, le marqueur et le stylo, et des tirages en 1080 px avec le tampon GRNGE. GRNGE Pro débloque tout le reste pour 5,99 dollars américains par mois ou 29,99 par an, et la formule annuelle commence par une semaine offerte.",
        "Gratis da scaricare, con Fotocopia e Puntinato, due livelli, pennarello e penna e stampe a 1080 px con il timbro GRNGE. GRNGE Pro sblocca tutto il resto a 5,99 dollari statunitensi al mese o 29,99 all'anno, e il piano annuale parte con una settimana gratis.",
        "ダウンロード無料。コピーと点描、2枚の版、マーカーとペン、GRNGE スタンプ入りの 1080 px プリントを無料で使えます。GRNGE Pro ではほかのすべてが使えるようになり、月額 5.99 米ドルまたは年額 29.99 米ドル。年額プランは最初の1週間が無料です。",
        "다운로드 무료. 복사와 점묘, 레이어 두 장, 마커와 펜, GRNGE 스탬프가 찍힌 1080 px 인쇄를 무료로 쓸 수 있다. GRNGE Pro는 나머지를 모두 열어 주며 월 5.99 미국 달러 또는 연 29.99 미국 달러이고, 연간 플랜은 첫 1주일이 무료다.",
        "Gratis te downloaden, met Fotokopie en Stippel, twee lagen, stift en pen, en afdrukken van 1080 px met de GRNGE-stempel. GRNGE Pro opent al het andere voor 5,99 Amerikaanse dollar per maand of 29,99 per jaar, en het jaarabonnement begint met een gratis week.",
        "Grátis para baixar, com Fotocópia e Pontilhado, duas camadas, marcador e caneta, e impressões de 1080 px com o carimbo GRNGE. O GRNGE Pro libera todo o resto por 5,99 dólares americanos por mês ou 29,99 por ano, e o plano anual começa com uma semana grátis.",
        "免费下载，可免费使用复印和点描、两层叠层、马克笔和钢笔，以及带 GRNGE 印记的 1080 px 输出。GRNGE Pro 解锁其余全部，每月 5.99 美元或每年 29.99 美元，年度方案首周免费。"),
}

KEEP |= {"Discord"}  # the community server, a name in every language
