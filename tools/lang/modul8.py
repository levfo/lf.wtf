"""lf.wtf/modul8, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

**The nineteen effect names are lifted from the app's own String Catalog**, not translated afresh.
MODUL8 already ships in these ten languages, and a site that calls an effect one thing while the
button in the app calls it another reads as machine translation even when both are correct on their
own. They were pulled straight out of `GlitchArt/Localizable.xcstrings`, so the two cannot drift.

**The ten Premium effects that arrived in 2.0, and the Dead Air and Y2K preset packs, use the names
from the app's own localised App Store listing for 2.0** (the `description` of the iTunes lookup
for each storefront), for the same reason. The listing is the one place those names are published
per language, so the page says Bandsalat, Masticada, テープ噛み and 绞带 exactly where the app does.
Words for the 2.0 features follow the listing too: German Stempel and Masken, French tampons, and so
on. Premium stays in Latin letters everywhere, as it already did on this page before 2.0.

Preset names (the CRT and Cyber presets in the gallery captions) stay in English throughout,
because that is what the app shows on its preset row in every language. The two Premium packs are
the exception: the listing translates Dead Air, so the page does as well, and Y2K stays Y2K except
in Chinese, where the listing calls it 千禧.
"""

KEEP = {
    "MODUL8", "FRMT", "CYANO", "Levi Foster", "iPhone", "App Store",
    "Free · iPhone · iOS 17+",
    "Effects: VHS · Chroma · Interlace · Sync · Static · Scanlines",
    "Effects: Datamosh · Corruption · Pixel Shift · Pixel Sort · Feedback",
    "Effects: CRT · Crush · Dither · RGB Split · Invert · Film · Noise · Distortion",
    "Effects: Satellite · Ghosting · Slow Scan · Teletext · Fax · Repost · Webcam · Handheld · "
    "Magnet · Chewed",
    "CRT + Scanlines + RGB Split", "VHS + Chroma + RGB Split",
    "Distortion + RGB Split + Noise", "Crush + Dither + Scanlines + Sort",
    "Distortion + RGB Split + Sort",
    "Shinjuku crossing · Distortion + RGB Split + Pixel Sort · rendered on device",
    "MODUL8 - Glitch Art Effects",
}

#: Straight from GlitchArt/Localizable.xcstrings, so the page and the app agree.
EFFECTS = {
    "NOISE": ("RAUSCHEN", "RUIDO", "RUIDO", "BRUIT", "RUMORE", "ノイズ", "노이즈", "RUIS",
              "RUÍDO", "噪点"),
    "PIXEL SHIFT": ("VERSATZ", "CORRIMIENTO", "CORRIMIENTO", "DÉCALAGE", "SPOSTA", "シフト",
                    "픽셀 시프트", "VERSCHUIF", "DESLOCAR", "像素偏移"),
    "RGB SPLIT": ("RGB", "RGB", "RGB", "RVB", "RGB", "RGB分離", "RGB 분리", "RGB", "RGB",
                  "RGB 分离"),
    "SCANLINES": ("BILDZEILEN", "LÍNEAS", "LÍNEAS", "LIGNES", "RIGHE", "走査線", "주사선",
                  "LIJNEN", "LINHAS", "扫描线"),
    "DISTORTION": ("VERZERRUNG", "DISTORSIÓN", "DISTORSIÓN", "DISTORSION", "DISTORSIONE", "歪み",
                   "왜곡", "VERVORMING", "DISTORÇÃO", "畸变"),
    "CORRUPTION": ("DEFEKT", "CORRUPCIÓN", "CORRUPCIÓN", "CORRUPTION", "CORRUZIONE", "破損",
                   "손상", "CORRUPTIE", "CORRUPÇÃO", "数据损坏"),
    "FEEDBACK": ("RÜCKKOPPLUNG", "REALIM.", "REALIM.", "RETOUR", "FEEDBACK", "反復", "피드백",
                 "TERUGKOPP.", "REALIM.", "反馈"),
    "VHS": ("VHS",) * 10,
    "CRT": ("CRT", "CRT", "CRT", "CRT", "CRT", "CRT", "CRT", "BEELDBUIS", "CRT", "显像管"),
    "CHROMA": ("CHROMA", "CROMA", "CROMA", "CHROMA", "CROMA", "色ずれ", "색 어긋남", "CHROMA",
               "CROMA", "色度偏移"),
    "FILM": ("FILM", "PELÍCULA", "PELÍCULA", "PELLICULE", "PELLICOLA", "フィルム", "필름", "FILM",
             "FILME", "胶片"),
    "CRUSH": ("CRUSH", "CRUSH", "CRUSH", "CRUSH", "CRUSH", "劣化", "열화", "CRUSH", "CRUSH",
              "位深压碎"),
    "INTERLACE": ("ZEILEN", "ENTRELAZ.", "ENTRELAZ.", "ENTRELACÉ", "INTERLACCIO", "インタレース",
                  "인터레이스", "INTERLACE", "ENTRELAÇ.", "隔行扫描"),
    "INVERT": ("INVERTIEREN", "INVERTIR", "INVERTIR", "INVERSION", "INVERTI", "色反転", "색 반전",
               "OMKEREN", "INVERTER", "反色"),
    "DATAMOSH": ("DATAMOSH", "DATAMOSH", "DATAMOSH", "DATAMOSH", "DATAMOSH", "モッシュ", "모시",
                 "DATAMOSH", "DATAMOSH", "数据莫氏"),
    "DITHER": ("DITHER", "TRAMADO", "TRAMADO", "TRAMAGE", "DITHER", "ディザ", "디더", "DITHER",
               "DITHER", "抖动"),
    "STATIC": ("BILDRAUSCHEN", "NIEVE", "NIEVE", "NEIGE", "NEVE", "砂嵐", "지지직", "SNEEUW",
               "CHUVISCO", "雪花"),
    "SORT": ("SORTIEREN", "ORDENAR", "ORDENAR", "TRI", "ORDINA", "ソート", "픽셀 정렬", "SORTEER",
             "ORDENAR", "像素排序"),
    "SYNC": ("SYNC", "SINCRONÍA", "SINCRONÍA", "SYNCHRO", "SYNC", "同期ずれ", "동기 오류", "SYNC",
             "SINCRONIA", "信号同步"),
}

#: The ten Premium effects new in 2.0, named as the app's localised 2.0 App Store listing names them.
PREMIUM_EFFECTS = {
    "SATELLITE": ("SATELLIT", "SATÉLITE", "SATÉLITE", "SATELLITE", "SATELLITE", "衛星放送",
                  "위성 방송", "SATELLIET", "SATÉLITE", "卫星"),
    "GHOSTING": ("GEISTERBILD", "DOBLE IMAGEN", "DOBLE IMAGEN", "DÉDOUBLEMENT", "SDOPPIAMENTO",
                 "ゴースト障害", "고스트 현상", "SPOOKBEELD", "SOMBRA", "鬼影"),
    "SLOW SCAN": ("SLOW SCAN", "SLOW SCAN", "SLOW SCAN", "SLOW SCAN", "SLOW SCAN", "低速走査",
                  "저속 주사", "SLOW SCAN", "SLOW SCAN", "慢扫描"),
    "TELETEXT": ("VIDEOTEXT", "TELETEXTO", "TELETEXTO", "TÉLÉTEXTE", "TELEVIDEO", "文字放送",
                 "문자방송", "TELETEKST", "TELETEXTO", "图文电视"),
    "FAX": ("FAX", "FAX", "FAX", "FAX", "FAX", "FAX", "팩스", "FAX", "FAX", "传真"),
    "REPOST": ("REPOST", "RESUBIDA", "RESUBIDA", "REPOST", "REPOST", "再投稿", "재업로드", "REPOST",
               "REPOST", "电子包浆"),
    "WEBCAM": ("WEBCAM", "WEBCAM", "WEBCAM", "WEBCAM", "WEBCAM", "WEBカメラ", "웹캠", "WEBCAM",
               "WEBCAM", "摄像头"),
    "HANDHELD": ("HANDHELD", "PORTÁTIL", "PORTÁTIL", "CONSOLE", "CONSOLE", "携帯ゲーム機",
                 "휴대 게임기", "HANDHELD", "PORTÁTIL", "掌机"),
    "MAGNET": ("MAGNET", "IMÁN", "IMÁN", "AIMANT", "CALAMITA", "磁石", "자석", "MAGNEET", "ÍMÃ",
               "磁化"),
    "CHEWED": ("BANDSALAT", "MASTICADA", "MASTICADA", "BANDE MANGÉE", "NASTRO MANGIATO",
               "テープ噛み", "테이프 씹힘", "BANDSALADE", "ENROSCADA", "绞带"),
}

T = dict(EFFECTS)
T.update(PREMIUM_EFFECTS)

T.update({
    "MODUL8: Glitch Art App for iPhone | Free Glitch Photo Effects": (
        "MODUL8: Glitch-Art-App für iPhone | Kostenlose Glitch-Fotoeffekte",
        "MODUL8: app de glitch art para iPhone | Efectos glitch gratis",
        "MODUL8: app de glitch art para iPhone | Efectos glitch gratis",
        "MODUL8 : app de glitch art pour iPhone | Effets glitch gratuits",
        "MODUL8: app di glitch art per iPhone | Effetti glitch gratis",
        "MODUL8｜iPhone 用グリッチアートアプリ | 無料のグリッチ加工",
        "MODUL8｜iPhone 글리치 아트 앱 | 무료 글리치 사진 효과",
        "MODUL8: glitch-art-app voor iPhone | Gratis glitch-fotoeffecten",
        "MODUL8: app de glitch art para iPhone | Efeitos glitch grátis",
        "MODUL8｜iPhone 故障艺术应用 | 免费故障照片特效"),
    "MODUL8: Glitch Art App for iPhone": (
        "MODUL8: Glitch-Art-App für iPhone", "MODUL8: app de glitch art para iPhone",
        "MODUL8: app de glitch art para iPhone", "MODUL8 : app de glitch art pour iPhone",
        "MODUL8: app di glitch art per iPhone", "MODUL8｜iPhone 用グリッチアートアプリ",
        "MODUL8｜iPhone 글리치 아트 앱", "MODUL8: glitch-art-app voor iPhone",
        "MODUL8: app de glitch art para iPhone", "MODUL8｜iPhone 故障艺术应用"),
    "A Tokyo crossing dissolved into vertical streaks by MODUL8's pixel sorting.": (
        "Eine Tokioter Kreuzung, vom Pixel Sorting in MODUL8 in senkrechte Schlieren aufgelöst.",
        "Un cruce de Tokio disuelto en vetas verticales por la ordenación de píxeles de MODUL8.",
        "Un cruce de Tokio disuelto en vetas verticales por la ordenación de píxeles de MODUL8.",
        "Un carrefour de Tokyo dissous en traînées verticales par le tri de pixels de MODUL8.",
        "Un incrocio di Tokyo dissolto in strisce verticali dal pixel sorting di MODUL8.",
        "MODUL8 のピクセルソートによって、縦の筋へと溶けていった東京の交差点。",
        "MODUL8의 픽셀 정렬로 세로 줄기로 녹아내린 도쿄의 교차로.",
        "Een Tokiose kruising opgelost in verticale strepen door de pixel sorting van MODUL8.",
        "Um cruzamento de Tóquio dissolvido em riscos verticais pela ordenação de pixels do MODUL8.",
        "被 MODUL8 的像素排序化成一道道竖直条纹的东京路口。"),
    "MODUL8 app icon": ("MODUL8 App-Symbol", "Icono de la app MODUL8", "Icono de la app MODUL8",
                        "Icône de l'app MODUL8", "Icona dell'app MODUL8",
                        "MODUL8 のアプリアイコン", "MODUL8 앱 아이콘", "MODUL8-app-icoon",
                        "Ícone do app MODUL8", "MODUL8 应用图标"),
    "Get it free": ("Kostenlos holen", "Consíguela gratis", "Consíguela gratis",
                    "Obtenir gratuitement", "Scaricala gratis", "無料で入手", "무료로 받기",
                    "Gratis downloaden", "Baixe grátis", "免费获取"),
    "Glitch art app for iPhone": (
        "Glitch-Art-App für iPhone", "App de glitch art para iPhone",
        "App de glitch art para iPhone", "App de glitch art pour iPhone",
        "App di glitch art per iPhone", "iPhone 用グリッチアートアプリ",
        "iPhone 글리치 아트 앱", "Glitch-art-app voor iPhone",
        "App de glitch art para iPhone", "iPhone 故障艺术应用"),
    # Three fragments of one headline, in this order and no other.
    "Break your": ("Zerstör deine", "Rompe tus", "Rompe tus", "Cassez vos", "Rompi le tue",
                   "写真を", "사진을", "Sloop je", "Quebre suas", "把你的照片"),
    "photos on": ("Fotos", "fotos", "fotos", "photos", "foto", "わざと", "일부러", "foto's",
                  "fotos", "故意"),
    "purpose.": ("mit Absicht.", "a propósito.", "a propósito.", "exprès.", "apposta.",
                 "壊してみる。", "부숴 보세요.", "met opzet.", "de propósito.", "弄坏。"),
    "Download on the App Store": (
        "Im App Store laden", "Descargar en la App Store", "Descargar en la App Store",
        "Télécharger dans l'App Store", "Scarica dall'App Store", "App Store でダウンロード",
        "App Store에서 다운로드", "Downloaden in de App Store", "Baixar na App Store",
        "在 App Store 下载"),
    "A Tokyo crossing rendered through MODUL8: the buildings smeared upward into long vertical "
    "streaks by pixel sorting, colour channels pulled apart, the crowd still recognisable "
    "underneath.": (
        "Eine Tokioter Kreuzung durch MODUL8: die Gebäude vom Pixel Sorting nach oben zu langen "
        "senkrechten Schlieren verschmiert, die Farbkanäle auseinandergezogen, die Menge darunter "
        "noch erkennbar.",
        "Un cruce de Tokio pasado por MODUL8: los edificios embadurnados hacia arriba en largas "
        "vetas verticales por la ordenación de píxeles, los canales de color separados, la multitud "
        "todavía reconocible debajo.",
        "Un cruce de Tokio pasado por MODUL8: los edificios embadurnados hacia arriba en largas "
        "vetas verticales por la ordenación de píxeles, los canales de color separados, la multitud "
        "todavía reconocible debajo.",
        "Un carrefour de Tokyo passé dans MODUL8 : les immeubles étirés vers le haut en longues "
        "traînées verticales par le tri de pixels, les canaux de couleur écartés, la foule encore "
        "reconnaissable dessous.",
        "Un incrocio di Tokyo passato per MODUL8: i palazzi spalmati verso l'alto in lunghe strisce "
        "verticali dal pixel sorting, i canali di colore separati, la folla ancora riconoscibile "
        "sotto.",
        "MODUL8 を通した東京の交差点。ピクセルソートによってビルが上へ長い縦の筋に引き伸ばされ、"
        "色チャンネルは引き離され、その下に人の群れがまだ見て取れる。",
        "MODUL8를 통과한 도쿄의 교차로. 픽셀 정렬로 건물들이 위로 긴 세로 줄기가 되어 번지고, "
        "색 채널은 서로 벌어졌으며, 그 아래로 사람들의 무리는 아직 알아볼 수 있습니다.",
        "Een Tokiose kruising door MODUL8: de gebouwen door pixel sorting omhoog uitgesmeerd tot "
        "lange verticale strepen, de kleurkanalen uit elkaar getrokken, de menigte er nog "
        "herkenbaar onder.",
        "Um cruzamento de Tóquio passado pelo MODUL8: os prédios borrados para cima em longos "
        "riscos verticais pela ordenação de pixels, os canais de cor separados, a multidão ainda "
        "reconhecível embaixo.",
        "经过 MODUL8 处理的东京路口：楼群被像素排序向上抹成一道道长长的竖直条纹，色彩通道被拉开，"
        "底下的人群仍然认得出来。"),
    "The idea": ("Die Idee", "La idea", "La idea", "L'idée", "L'idea", "考え方", "생각",
                 "Het idee", "A ideia", "想法"),
    "A filter paints over a photo. MODUL8 damages it.": (
        "Ein Filter malt über ein Foto. MODUL8 beschädigt es.",
        "Un filtro pinta encima de una foto. MODUL8 la daña.",
        "Un filtro pinta encima de una foto. MODUL8 la daña.",
        "Un filtre peint par-dessus une photo. MODUL8 l'abîme.",
        "Un filtro dipinge sopra una foto. MODUL8 la danneggia.",
        "フィルターは写真の上に塗る。MODUL8 は写真を壊す。",
        "필터는 사진 위에 덧칠합니다. MODUL8은 사진을 망가뜨립니다.",
        "Een filter schildert over een foto. MODUL8 beschadigt hem.",
        "Um filtro pinta por cima de uma foto. O MODUL8 a danifica.",
        "滤镜是在照片上面涂。MODUL8 是把照片弄坏。"),
    "Most glitch apps ship one look. They lay a fixed pattern of coloured lines over whatever you\n"
    "      give them, and every photo comes out wearing the same costume. You can spot the app "
    "from\n      across a feed.": (
        "Die meisten Glitch-Apps liefern einen einzigen Look. Sie legen ein festes Muster aus "
        "farbigen Linien über alles, was du ihnen gibst, und jedes Foto kommt im selben Kostüm "
        "heraus. Man erkennt die App quer durch einen Feed.",
        "La mayoría de las apps de glitch traen un solo aspecto. Ponen un patrón fijo de líneas de "
        "color sobre lo que les des, y cada foto sale con el mismo disfraz. Reconoces la app desde "
        "el otro lado de un feed.",
        "La mayoría de las apps de glitch traen un solo aspecto. Ponen un patrón fijo de líneas de "
        "color sobre lo que les des, y cada foto sale con el mismo disfraz. Reconoces la app desde "
        "el otro lado de un feed.",
        "La plupart des apps de glitch livrent un seul rendu. Elles posent un motif fixe de lignes "
        "colorées sur tout ce que vous leur donnez, et chaque photo ressort avec le même costume. "
        "On repère l'app à l'autre bout d'un fil.",
        "Quasi tutte le app di glitch escono con un solo look. Mettono un motivo fisso di righe "
        "colorate su qualunque cosa gli dai, e ogni foto esce con lo stesso costume. L'app la "
        "riconosci in fondo a un feed.",
        "たいていのグリッチアプリは、ひとつの見た目しか持っていません。渡されたものが何であれ、"
        "色の線の決まった模様を上に載せるので、どの写真も同じ衣装を着て出てきます。"
        "フィードの向こう側からでも、どのアプリか分かってしまいます。",
        "대부분의 글리치 앱은 하나의 룩만 가지고 있습니다. 무엇을 주든 색 선의 정해진 무늬를 위에 "
        "얹기 때문에, 어떤 사진이든 같은 옷을 입고 나옵니다. 피드 저편에서도 어떤 앱인지 알아볼 "
        "수 있습니다.",
        "De meeste glitch-apps leveren één look. Ze leggen een vast patroon van gekleurde lijnen "
        "over wat je ze ook geeft, en elke foto komt eruit in hetzelfde kostuum. Je herkent de app "
        "van de overkant van een feed.",
        "A maioria dos apps de glitch entrega um visual só. Eles põem um padrão fixo de linhas "
        "coloridas sobre o que você der, e cada foto sai vestindo a mesma fantasia. Dá para "
        "reconhecer o app do outro lado de um feed.",
        "多数故障类应用只有一种外观。你给它什么，它都把一套固定的彩色线条图案盖上去，"
        "于是每张照片都穿着同一件戏服出来。隔着一整条信息流你都认得出是哪个应用。"),
    "MODUL8 works the other way round. Each effect is a small simulation of one real failure, and\n"
    "      it reads the actual pixels underneath before deciding what to do to them. Pixel Sort "
    "finds the\n      bright regions in your specific frame and drags them until the buildings turn "
    "to vertical\n      rain. Datamosh picks blocks and pastes them somewhere they do not belong. "
    "VHS bleeds colour\n      sideways the way a worn tape head did. Feed two different photos to "
    "the same settings and you\n      get two different pictures, because the damage is a response "
    "to the image rather than a layer\n      on top of it.": (
        "MODUL8 arbeitet andersherum. Jeder Effekt ist eine kleine Simulation eines echten "
        "Fehlers, und er liest die tatsächlichen Pixel darunter, bevor er entscheidet, was er mit "
        "ihnen macht. Pixel Sort findet die hellen Bereiche in genau deinem Bild und zieht sie, "
        "bis die Gebäude zu senkrechtem Regen werden. Datamosh greift Blöcke und klebt sie "
        "irgendwohin, wo sie nicht hingehören. VHS lässt Farbe seitwärts auslaufen, so wie es ein "
        "abgenutzter Bandkopf tat. Gib zwei verschiedene Fotos in dieselben Einstellungen, und du "
        "bekommst zwei verschiedene Bilder, weil der Schaden eine Antwort auf das Bild ist und "
        "keine Schicht darüber.",
        "MODUL8 funciona al revés. Cada efecto es una pequeña simulación de un fallo real, y lee "
        "los píxeles que hay debajo antes de decidir qué hacer con ellos. La ordenación de píxeles "
        "encuentra las zonas brillantes de tu fotograma concreto y las arrastra hasta que los "
        "edificios se vuelven lluvia vertical. Datamosh coge bloques y los pega donde no van. VHS "
        "sangra el color de lado como hacía un cabezal de cinta gastado. Da dos fotos distintas a "
        "los mismos ajustes y obtienes dos imágenes distintas, porque el daño es una respuesta a la "
        "imagen y no una capa encima de ella.",
        "MODUL8 funciona al revés. Cada efecto es una pequeña simulación de una falla real, y lee "
        "los píxeles que hay debajo antes de decidir qué hacer con ellos. La ordenación de píxeles "
        "encuentra las zonas brillantes de tu cuadro concreto y las arrastra hasta que los "
        "edificios se vuelven lluvia vertical. Datamosh agarra bloques y los pega donde no van. VHS "
        "sangra el color de lado como hacía un cabezal de cinta gastado. Da dos fotos distintas a "
        "los mismos ajustes y obtienes dos imágenes distintas, porque el daño es una respuesta a la "
        "imagen y no una capa encima de ella.",
        "MODUL8 fonctionne à l'envers. Chaque effet est une petite simulation d'une panne réelle, "
        "et il lit les pixels qui se trouvent dessous avant de décider quoi leur faire. Le tri de "
        "pixels repère les zones claires de votre image précise et les tire jusqu'à ce que les "
        "immeubles deviennent une pluie verticale. Datamosh prend des blocs et les colle là où ils "
        "n'ont rien à faire. VHS fait baver la couleur latéralement comme le faisait une tête de "
        "lecture usée. Donnez deux photos différentes aux mêmes réglages et vous obtenez deux "
        "images différentes, parce que le dommage est une réponse à l'image et non une couche "
        "posée dessus.",
        "MODUL8 lavora al contrario. Ogni effetto è una piccola simulazione di un guasto vero, e "
        "legge i pixel che stanno sotto prima di decidere cosa farne. Il pixel sorting trova le "
        "zone chiare del tuo fotogramma preciso e le trascina finché i palazzi diventano pioggia "
        "verticale. Datamosh prende blocchi e li incolla dove non c'entrano. VHS fa sbavare il "
        "colore di lato come faceva una testina consumata. Dai due foto diverse alle stesse "
        "impostazioni e ottieni due immagini diverse, perché il danno è una risposta all'immagine e "
        "non uno strato sopra di essa.",
        "MODUL8 は逆向きに働きます。どのエフェクトも、ひとつの実在する故障の小さなシミュレーション"
        "であり、下にある実際の画素を読んでから、それをどうするかを決めます。ピクセルソートは"
        "あなたのその一枚のなかの明るい領域を見つけ、ビルが縦の雨になるまで引き伸ばします。"
        "データモッシュはブロックを拾い、本来あるはずのない場所へ貼りつけます。VHS は"
        "すり減ったテープヘッドがそうしたように、色を横へにじませます。同じ設定に別々の写真を"
        "渡せば、別々の絵が出てきます。損傷が、上に載せたレイヤーではなく、"
        "その画像への応答だからです。",
        "MODUL8는 반대로 작동합니다. 각 효과는 실제로 있었던 고장 하나를 작게 시뮬레이션한 "
        "것이고, 아래에 있는 실제 픽셀을 읽은 다음에 무엇을 할지 정합니다. 픽셀 정렬은 바로 그 "
        "프레임 안의 밝은 영역을 찾아, 건물이 세로로 내리는 비가 될 때까지 끌어당깁니다. "
        "데이터모시는 블록을 집어 있어서는 안 될 자리에 붙입니다. VHS는 닳아 버린 테이프 헤드가 "
        "그랬듯이 색을 옆으로 번지게 합니다. 같은 설정에 다른 사진 두 장을 주면 다른 그림 두 장이 "
        "나옵니다. 손상이 위에 얹은 레이어가 아니라 그 이미지에 대한 반응이기 때문입니다.",
        "MODUL8 werkt andersom. Elk effect is een kleine simulatie van één echte storing, en het "
        "leest de werkelijke pixels eronder voordat het besluit wat het ermee doet. Pixel sorting "
        "vindt de heldere gebieden in jouw specifieke beeld en trekt ze uit tot de gebouwen "
        "verticale regen worden. Datamosh pakt blokken en plakt ze ergens waar ze niet horen. VHS "
        "laat kleur zijwaarts uitlopen zoals een versleten bandkop deed. Geef twee verschillende "
        "foto's aan dezelfde instellingen en je krijgt twee verschillende beelden, want de schade "
        "is een antwoord op het beeld en geen laag erbovenop.",
        "O MODUL8 funciona ao contrário. Cada efeito é uma pequena simulação de uma falha real, e "
        "lê os pixels que estão embaixo antes de decidir o que fazer com eles. A ordenação de "
        "pixels encontra as regiões claras do seu quadro específico e as arrasta até os prédios "
        "virarem chuva vertical. O datamosh pega blocos e cola onde eles não pertencem. O VHS "
        "sangra a cor de lado do jeito que uma cabeça de fita gasta fazia. Dê duas fotos diferentes "
        "aos mesmos ajustes e você recebe duas imagens diferentes, porque o dano é uma resposta à "
        "imagem e não uma camada em cima dela.",
        "MODUL8 反过来做。每一种效果都是对某一个真实故障的小型模拟，"
        "它会先读取底下真实的像素，再决定要对它们做什么。像素排序会找出你这一张画面里的明亮区域，"
        "把它们一路拖到楼群变成竖直的雨。数据莫氏挑出区块，贴到根本不属于它们的位置。"
        "VHS 让颜色像磨损的磁头那样向侧面渗开。用同样的设置喂两张不同的照片，"
        "你会得到两张不同的画面，因为这种损坏是对图像的回应，而不是盖在上面的一层。"),
    "The original photograph of a Tokyo crossing on a clear day: office towers, signage, a crowd "
    "on the striped crossing.": (
        "Das Originalfoto einer Tokioter Kreuzung an einem klaren Tag: Bürotürme, Schilder, eine "
        "Menge auf dem gestreiften Zebrastreifen.",
        "La fotografía original de un cruce de Tokio en un día despejado: torres de oficinas, "
        "carteles, una multitud sobre el paso de cebra.",
        "La fotografía original de un cruce de Tokio en un día despejado: torres de oficinas, "
        "carteles, una multitud sobre el paso de cebra.",
        "La photographie originale d'un carrefour de Tokyo par temps clair : tours de bureaux, "
        "enseignes, une foule sur le passage zébré.",
        "La fotografia originale di un incrocio di Tokyo in una giornata limpida: torri di uffici, "
        "insegne, una folla sulle strisce.",
        "よく晴れた日の東京の交差点、元の写真。オフィスビル、看板、縞模様の横断歩道を渡る人の群れ。",
        "맑은 날 도쿄 교차로의 원본 사진. 오피스 빌딩, 간판, 줄무늬 횡단보도 위의 인파.",
        "De originele foto van een Tokiose kruising op een heldere dag: kantoortorens, "
        "reclameborden, een menigte op het gestreepte zebrapad.",
        "A fotografia original de um cruzamento de Tóquio num dia claro: torres de escritórios, "
        "letreiros, uma multidão sobre a faixa listrada.",
        "晴天里东京路口的原始照片：写字楼、招牌，以及斑马线上的人群。"),
    "The same frame after MODUL8: buildings dissolved into vertical streaks, colour fringing on "
    "every edge, the crossing stretched into ribbons.": (
        "Dasselbe Bild nach MODUL8: Gebäude in senkrechte Schlieren aufgelöst, Farbsäume an jeder "
        "Kante, der Zebrastreifen zu Bändern gedehnt.",
        "El mismo fotograma tras MODUL8: edificios disueltos en vetas verticales, franjas de color "
        "en cada borde, el paso de cebra estirado en cintas.",
        "El mismo cuadro tras MODUL8: edificios disueltos en vetas verticales, franjas de color en "
        "cada borde, el paso de cebra estirado en cintas.",
        "La même image après MODUL8 : les immeubles dissous en traînées verticales, des franges "
        "colorées sur chaque arête, le passage étiré en rubans.",
        "Lo stesso fotogramma dopo MODUL8: palazzi dissolti in strisce verticali, frange di colore "
        "su ogni bordo, le strisce pedonali stirate in nastri.",
        "MODUL8 を通したあとの同じ一枚。ビルは縦の筋へ溶け、あらゆる輪郭に色のふちが立ち、"
        "横断歩道はリボンのように引き伸ばされている。",
        "MODUL8를 거친 뒤의 같은 프레임. 건물은 세로 줄기로 녹아내리고, 모든 가장자리에 색 테두리가 "
        "생기고, 횡단보도는 리본처럼 늘어났습니다.",
        "Hetzelfde beeld na MODUL8: gebouwen opgelost in verticale strepen, kleurranden op elke "
        "rand, het zebrapad uitgerekt tot linten.",
        "O mesmo quadro depois do MODUL8: prédios dissolvidos em riscos verticais, franjas de cor "
        "em cada borda, a faixa esticada em fitas.",
        "经过 MODUL8 之后的同一张画面：楼群化成竖直条纹，每一道边缘都镶上色边，"
        "斑马线被拉成一条条飘带。"),
    "Photo": ("Foto", "Foto", "Foto", "Photo", "Foto", "写真", "사진", "Foto", "Foto", "照片"),
    "Drag it. One frame, three stacked effects. The sorting follows the brightness of this\n"
    "        particular sky, which is why the towers melt upward and the crowd does not.": (
        "Zieh daran. Ein Bild, drei gestapelte Effekte. Das Sortieren folgt der Helligkeit genau "
        "dieses Himmels, und darum schmelzen die Türme nach oben und die Menge nicht.",
        "Arrastra. Un fotograma, tres efectos apilados. La ordenación sigue el brillo de este "
        "cielo en concreto, y por eso las torres se funden hacia arriba y la multitud no.",
        "Arrastra. Un cuadro, tres efectos apilados. La ordenación sigue el brillo de este cielo "
        "en concreto, y por eso las torres se funden hacia arriba y la multitud no.",
        "Faites glisser. Une image, trois effets empilés. Le tri suit la luminosité de ce ciel "
        "précis, et c'est pourquoi les tours fondent vers le haut et pas la foule.",
        "Trascina. Un fotogramma, tre effetti impilati. L'ordinamento segue la luminosità di "
        "questo cielo preciso, ed è per questo che le torri si sciolgono verso l'alto e la folla "
        "no.",
        "ドラッグしてみてください。一枚の画像に、三つの重ねたエフェクト。ソートはこの空の明るさに"
        "従っているので、ビルは上へ溶けていくのに、人の群れは溶けません。",
        "끌어 보세요. 한 프레임, 세 겹으로 쌓은 효과. 정렬이 바로 이 하늘의 밝기를 따라가기 "
        "때문에, 건물은 위로 녹아내리고 인파는 그대로입니다.",
        "Sleep maar. Eén beeld, drie gestapelde effecten. Het sorteren volgt de helderheid van "
        "juist deze lucht, en daarom smelten de torens omhoog en de menigte niet.",
        "Arraste. Um quadro, três efeitos empilhados. A ordenação segue o brilho deste céu "
        "específico, e é por isso que as torres derretem para cima e a multidão não.",
        "拖动看看。一张画面，三层叠加的效果。排序跟随的是这片天空的亮度，"
        "所以楼群会向上融化，而人群不会。"),
    "What is actually in there": (
        "Was tatsächlich drinsteckt", "Qué hay realmente dentro", "Qué hay realmente dentro",
        "Ce qu'il y a vraiment dedans", "Cosa c'è davvero dentro", "実際に入っているもの",
        "실제로 들어 있는 것", "Wat er werkelijk in zit", "O que tem de fato ali dentro",
        "里面究竟有什么"),
    "Analogue video": ("Analoges Video", "Vídeo analógico", "Video analógico",
                       "Vidéo analogique", "Video analogico", "アナログ映像", "아날로그 영상",
                       "Analoge video", "Vídeo analógico", "模拟视频"),
    "VHS tracking errors, head switching noise at the bottom of the frame, chroma delay,\n"
    "            interlacing comb, signal sync loss, analogue static. This is the family that "
    "makes a\n            picture look like it was recorded off a television at two in the morning.": (
        "VHS-Spurfehler, Kopfumschaltrauschen am unteren Bildrand, Chroma-Verzögerung, "
        "Zeilenkamm, Verlust der Signalsynchronisation, analoges Rauschen. Das ist die Familie, "
        "die ein Bild aussehen lässt, als wäre es um zwei Uhr morgens vom Fernseher aufgenommen "
        "worden.",
        "Errores de tracking de VHS, ruido de conmutación de cabezales en la parte baja del "
        "fotograma, retardo de croma, peine de entrelazado, pérdida de sincronía, nieve analógica. "
        "Esta es la familia que hace que una imagen parezca grabada de la televisión a las dos de "
        "la madrugada.",
        "Errores de tracking de VHS, ruido de conmutación de cabezales en la parte baja del cuadro, "
        "retardo de croma, peine de entrelazado, pérdida de sincronía, nieve analógica. Esta es la "
        "familia que hace que una imagen parezca grabada de la televisión a las dos de la "
        "madrugada.",
        "Erreurs de piste VHS, bruit de commutation de têtes en bas de l'image, retard de "
        "chrominance, peigne d'entrelacement, perte de synchro, neige analogique. C'est la famille "
        "qui donne à une image l'air d'avoir été enregistrée à la télévision à deux heures du "
        "matin.",
        "Errori di tracking VHS, rumore di commutazione testine in fondo al fotogramma, ritardo di "
        "crominanza, pettine da interlacciamento, perdita di sincronismo, neve analogica. È la "
        "famiglia che fa sembrare un'immagine registrata dalla televisione alle due di notte.",
        "VHS のトラッキングエラー、画面下端のヘッドスイッチングノイズ、色信号の遅れ、"
        "インタレースのくし状のずれ、同期の喪失、アナログの砂嵐。深夜二時のテレビから録画した"
        "ように見せるのは、この一群です。",
        "VHS 트래킹 오류, 화면 아래쪽의 헤드 스위칭 노이즈, 크로마 지연, 인터레이스 빗살 무늬, "
        "신호 동기 상실, 아날로그 지지직. 새벽 두 시의 텔레비전에서 녹화한 것처럼 보이게 만드는 "
        "것이 이 무리입니다.",
        "VHS-trackingfouten, kopschakelruis onderaan het beeld, chromavertraging, interlacekam, "
        "verlies van signaalsynchronisatie, analoge sneeuw. Dit is de familie die een beeld eruit "
        "laat zien alsof het om twee uur 's nachts van de televisie is opgenomen.",
        "Erros de tracking de VHS, ruído de comutação de cabeças na parte de baixo do quadro, "
        "atraso de croma, pente de entrelaçamento, perda de sincronismo, chuvisco analógico. Esta "
        "é a família que faz uma imagem parecer gravada da televisão às duas da manhã.",
        "VHS 的循迹错误、画面底部的磁头切换噪声、色度延迟、隔行扫描的梳状撕裂、信号失步、"
        "模拟雪花。让一张画面看起来像是凌晨两点从电视上录下来的，就是这一族。"),
    "Data corruption": ("Datenverfall", "Corrupción de datos", "Corrupción de datos",
                        "Corruption de données", "Corruzione dei dati", "データ破損",
                        "데이터 손상", "Datacorruptie", "Corrupção de dados", "数据损坏"),
    "Datamosh copies blocks from one part of the frame into another and smears the motion\n"
    "            between them, the way a video file does when the keyframes go missing. Corruption "
    "and\n            Pixel Shift tear rows sideways. Pixel Sort reorders pixels by brightness "
    "until solid\n            objects run like wet paint.": (
        "Datamosh kopiert Blöcke aus einem Teil des Bildes in einen anderen und verschmiert die "
        "Bewegung dazwischen, so wie es eine Videodatei tut, wenn die Keyframes fehlen. Corruption "
        "und Pixel Shift reißen Zeilen seitwärts. Pixel Sort ordnet Pixel nach Helligkeit um, bis "
        "feste Gegenstände laufen wie nasse Farbe.",
        "Datamosh copia bloques de una parte del fotograma a otra y embadurna el movimiento entre "
        "ellos, como hace un archivo de vídeo cuando faltan los fotogramas clave. Corrupción y "
        "Corrimiento desgarran filas de lado. La ordenación de píxeles los reordena por brillo "
        "hasta que los objetos sólidos chorrean como pintura fresca.",
        "Datamosh copia bloques de una parte del cuadro a otra y embadurna el movimiento entre "
        "ellos, como hace un archivo de video cuando faltan los cuadros clave. Corrupción y "
        "Corrimiento desgarran filas de lado. La ordenación de píxeles los reordena por brillo "
        "hasta que los objetos sólidos chorrean como pintura fresca.",
        "Datamosh copie des blocs d'une partie de l'image vers une autre et étale le mouvement "
        "entre eux, comme le fait un fichier vidéo quand les images clés manquent. Corruption et "
        "Décalage déchirent les rangées latéralement. Le tri de pixels les réordonne par luminosité "
        "jusqu'à ce que les objets solides coulent comme de la peinture fraîche.",
        "Datamosh copia blocchi da una parte del fotogramma a un'altra e spalma il movimento fra "
        "loro, come fa un file video quando mancano i fotogrammi chiave. Corruzione e Sposta "
        "strappano le righe di lato. Il pixel sorting riordina i pixel per luminosità finché gli "
        "oggetti solidi colano come vernice fresca.",
        "データモッシュは画面のある部分からブロックをコピーして別の場所へ移し、"
        "そのあいだの動きを引き伸ばします。キーフレームが失われた動画ファイルがそうなるのと"
        "同じです。破損とシフトは行を横へ引き裂きます。ピクセルソートは画素を明るさ順に並べ替え、"
        "固い物体が濡れた絵の具のように流れ出すまで続けます。",
        "데이터모시는 화면의 한 부분에서 블록을 복사해 다른 곳으로 옮기고, 그 사이의 움직임을 "
        "문질러 늘립니다. 키프레임이 사라진 동영상 파일이 그렇게 되듯이. 손상과 픽셀 시프트는 행을 "
        "옆으로 찢습니다. 픽셀 정렬은 픽셀을 밝기순으로 다시 늘어놓아, 단단한 물체가 젖은 물감처럼 "
        "흘러내리게 만듭니다.",
        "Datamosh kopieert blokken van het ene deel van het beeld naar het andere en smeert de "
        "beweging ertussen uit, zoals een videobestand doet als de keyframes wegvallen. Corruptie "
        "en Verschuif scheuren rijen zijwaarts. Pixel sorting herschikt pixels op helderheid tot "
        "vaste voorwerpen lopen als natte verf.",
        "O datamosh copia blocos de uma parte do quadro para outra e borra o movimento entre eles, "
        "do jeito que um arquivo de vídeo faz quando os quadros-chave somem. Corrupção e Deslocar "
        "rasgam linhas de lado. A ordenação de pixels os reorganiza por brilho até objetos sólidos "
        "escorrerem como tinta fresca.",
        "数据莫氏把画面某一处的区块复制到另一处，并把两者之间的运动抹开，"
        "就像视频文件丢了关键帧时那样。数据损坏和像素偏移把一行行画面向侧面撕开。"
        "像素排序按亮度重排像素，直到坚固的物体像未干的颜料一样流下来。"),
    "Display and colour": ("Anzeige und Farbe", "Pantalla y color", "Pantalla y color",
                           "Affichage et couleur", "Display e colore", "表示と色",
                           "디스플레이와 색", "Weergave en kleur", "Tela e cor", "显示与色彩"),
    "CRT adds phosphor glow, barrel curvature and a shadow mask. Bit Crush and Dither drop\n"
    "            the colour depth to something a machine from 1994 could hold. RGB Split pulls the "
    "three\n            channels apart. Film Grain and Noise put texture back on top.": (
        "CRT fügt Phosphorglühen, Tonnenkrümmung und eine Lochmaske hinzu. Bit Crush und Dither "
        "senken die Farbtiefe auf etwas, das eine Maschine von 1994 halten konnte. RGB Split zieht "
        "die drei Kanäle auseinander. Filmkorn und Rauschen legen wieder Textur darüber.",
        "CRT añade brillo de fósforo, curvatura de barril y una máscara de sombra. Crush y Tramado "
        "bajan la profundidad de color a algo que una máquina de 1994 pudiera sostener. La "
        "separación RGB separa los tres canales. Grano de película y Ruido devuelven textura por "
        "encima.",
        "CRT añade brillo de fósforo, curvatura de barril y una máscara de sombra. Crush y Tramado "
        "bajan la profundidad de color a algo que una máquina de 1994 pudiera sostener. La "
        "separación RGB separa los tres canales. Grano de película y Ruido devuelven textura por "
        "encima.",
        "CRT ajoute la lueur du phosphore, une courbure en barillet et un masque d'ombre. Crush et "
        "Tramage font tomber la profondeur de couleur à ce qu'une machine de 1994 pouvait tenir. "
        "La séparation RVB écarte les trois canaux. Grain de pellicule et Bruit remettent de la "
        "texture par-dessus.",
        "CRT aggiunge il bagliore dei fosfori, la curvatura a barile e una maschera d'ombra. Crush "
        "e Dither abbassano la profondità di colore a quello che una macchina del 1994 poteva "
        "reggere. La separazione RGB allontana i tre canali. Grana pellicola e Rumore rimettono "
        "texture sopra.",
        "CRT は蛍光体の光、樽型の歪み、シャドウマスクを加えます。劣化とディザは、色深度を "
        "1994 年の機械が扱えた程度まで落とします。RGB 分離は三つのチャンネルを引き離します。"
        "フィルム粒子とノイズが、その上に質感を戻します。",
        "CRT는 인광체의 발광, 배럴 곡률, 섀도 마스크를 더합니다. 열화와 디더는 색 깊이를 1994년의 "
        "기계가 감당할 수 있던 수준까지 떨어뜨립니다. RGB 분리는 세 채널을 벌려 놓습니다. 필름 "
        "입자와 노이즈가 그 위에 질감을 되돌려 놓습니다.",
        "CRT voegt fosforgloed, tonvormige kromming en een schaduwmasker toe. Crush en Dither laten "
        "de kleurdiepte zakken tot iets wat een machine uit 1994 aankon. RGB-splitsing trekt de "
        "drie kanalen uit elkaar. Filmkorrel en Ruis leggen er weer textuur overheen.",
        "O CRT acrescenta brilho de fósforo, curvatura em barril e uma máscara de sombra. Crush e "
        "Dither derrubam a profundidade de cor para algo que uma máquina de 1994 aguentasse. A "
        "separação RGB afasta os três canais. Grão de filme e Ruído devolvem textura por cima.",
        "显像管加上荧光粉的辉光、桶形畸变和荫罩。位深压碎与抖动把色深降到 1994 年的机器扛得住的"
        "程度。RGB 分离把三个通道拉开。胶片颗粒和噪点再把质感放回上面。"),
    "Same photo, different damage": (
        "Gleiches Foto, anderer Schaden", "Misma foto, distinto daño", "Misma foto, distinto daño",
        "Même photo, dommage différent", "Stessa foto, danno diverso",
        "同じ写真、違う壊し方", "같은 사진, 다른 손상", "Zelfde foto, andere schade",
        "Mesma foto, dano diferente", "同一张照片，不同的损坏"),
    "The stack decides the picture.": (
        "Der Stapel entscheidet das Bild.", "La pila decide la imagen.",
        "La pila decide la imagen.", "La pile décide de l'image.",
        "È lo stack a decidere l'immagine.", "積み方が絵を決めます。",
        "쌓는 방식이 그림을 결정합니다.", "De stapel bepaalt het beeld.",
        "A pilha decide a imagem.", "叠法决定画面。"),
    "Five renders from two source frames, changed only by which effects were switched on and what\n"
    "      order they ran in. Order matters: sorting a photo and then splitting the channels is not "
    "the\n      same picture as splitting the channels first and sorting after.": (
        "Fünf Renderings aus zwei Ausgangsbildern, verändert nur dadurch, welche Effekte "
        "eingeschaltet waren und in welcher Reihenfolge sie liefen. Die Reihenfolge zählt: ein "
        "Foto zu sortieren und dann die Kanäle zu trennen ergibt nicht dasselbe Bild wie erst die "
        "Kanäle zu trennen und danach zu sortieren.",
        "Cinco renders a partir de dos fotogramas fuente, cambiados solo por qué efectos estaban "
        "activados y en qué orden se ejecutaron. El orden importa: ordenar una foto y luego separar "
        "los canales no da la misma imagen que separar los canales primero y ordenar después.",
        "Cinco renders a partir de dos cuadros fuente, cambiados solo por qué efectos estaban "
        "activados y en qué orden se ejecutaron. El orden importa: ordenar una foto y luego separar "
        "los canales no da la misma imagen que separar los canales primero y ordenar después.",
        "Cinq rendus à partir de deux images sources, changés seulement par les effets activés et "
        "leur ordre d'exécution. L'ordre compte : trier une photo puis séparer les canaux ne donne "
        "pas la même image que séparer les canaux d'abord et trier ensuite.",
        "Cinque render da due fotogrammi di partenza, cambiati solo per quali effetti erano accesi "
        "e in che ordine sono girati. L'ordine conta: ordinare una foto e poi separare i canali non "
        "dà la stessa immagine di separare i canali prima e ordinare dopo.",
        "二枚の元画像から得た五通りのレンダリング。違うのは、どのエフェクトを入れたかと、"
        "どの順番で走らせたかだけです。順序は効きます。ソートしてからチャンネルを分けるのと、"
        "チャンネルを分けてからソートするのとでは、別の絵になります。",
        "두 장의 원본에서 나온 다섯 가지 렌더. 달라진 것은 어떤 효과를 켰는지와 어떤 순서로 "
        "돌렸는지뿐입니다. 순서는 중요합니다. 사진을 정렬한 뒤 채널을 나누는 것과, 채널을 먼저 "
        "나눈 뒤 정렬하는 것은 같은 그림이 아닙니다.",
        "Vijf renders uit twee bronbeelden, alleen veranderd door welke effecten aan stonden en in "
        "welke volgorde ze draaiden. Volgorde doet ertoe: een foto sorteren en dan de kanalen "
        "splitsen is niet hetzelfde beeld als eerst de kanalen splitsen en daarna sorteren.",
        "Cinco renders a partir de dois quadros de origem, mudados só por quais efeitos estavam "
        "ligados e em que ordem rodaram. A ordem importa: ordenar uma foto e depois separar os "
        "canais não dá a mesma imagem que separar os canais primeiro e ordenar depois.",
        "从两张源画面得到的五个结果，唯一的变化是开了哪些效果、以及它们按什么顺序运行。"
        "顺序是有影响的：先排序再分通道，和先分通道再排序，得到的不是同一张画面。"),
})

# ---------------------------------------------------------------- captions, interface, deal, FAQ
T.update({
    "A Tokyo street pushed through the CRT preset: green and magenta phosphor separation, barrel "
    "curvature bending the buildings, a visible shadow mask over everything.": (
        "Eine Tokioter Straße durch das CRT-Preset: grüne und magentafarbene Phosphortrennung, "
        "Tonnenkrümmung, die die Gebäude biegt, eine sichtbare Lochmaske über allem.",
        "Una calle de Tokio pasada por el preajuste CRT: separación de fósforo verde y magenta, "
        "curvatura de barril doblando los edificios, una máscara de sombra visible sobre todo.",
        "Una calle de Tokio pasada por el preajuste CRT: separación de fósforo verde y magenta, "
        "curvatura de barril doblando los edificios, una máscara de sombra visible sobre todo.",
        "Une rue de Tokyo passée par le préréglage CRT : séparation des phosphores vert et "
        "magenta, courbure en barillet qui plie les immeubles, un masque d'ombre visible sur tout.",
        "Una strada di Tokyo passata per il preset CRT: separazione dei fosfori verde e magenta, "
        "curvatura a barile che piega i palazzi, una maschera d'ombra visibile su tutto.",
        "東京の街路を CRT プリセットに通したもの。緑とマゼンタの蛍光体が分離し、樽型の歪みが"
        "ビルを曲げ、全体にシャドウマスクが見えている。",
        "도쿄의 거리를 CRT 프리셋에 통과시킨 것. 초록과 마젠타 인광체가 갈라지고, 배럴 곡률이 "
        "건물을 휘게 하며, 전체에 섀도 마스크가 보입니다.",
        "Een Tokiose straat door de CRT-preset: groene en magenta fosforscheiding, tonvormige "
        "kromming die de gebouwen buigt, een zichtbaar schaduwmasker over alles.",
        "Uma rua de Tóquio passada pelo preset CRT: separação de fósforo verde e magenta, "
        "curvatura em barril entortando os prédios, uma máscara de sombra visível sobre tudo.",
        "经过 CRT 预设的东京街道：绿色与洋红的荧光粉分离，桶形畸变把楼弯了过去，"
        "整幅画面上都能看到荫罩。"),
    "The same street through VHS: colour bleeding sideways off the neon, tracking tear across the "
    "lower frame, everything softened like a worn tape.": (
        "Dieselbe Straße durch VHS: Farbe, die seitwärts vom Neon ausläuft, ein Spurriss über den "
        "unteren Bildrand, alles weich wie ein abgenutztes Band.",
        "La misma calle pasada por VHS: color sangrando de lado desde el neón, desgarro de "
        "tracking en la parte baja, todo suavizado como una cinta gastada.",
        "La misma calle pasada por VHS: color sangrando de lado desde el neón, desgarro de "
        "tracking en la parte baja, todo suavizado como una cinta gastada.",
        "La même rue en VHS : la couleur qui bave latéralement depuis le néon, une déchirure de "
        "piste en bas de l'image, tout adouci comme une bande usée.",
        "La stessa strada in VHS: il colore che sbava di lato dal neon, uno strappo di tracking in "
        "basso, tutto ammorbidito come un nastro consumato.",
        "同じ街路を VHS で。ネオンから色が横へにじみ出し、画面下部にトラッキングの裂けが走り、"
        "すり減ったテープのように全体が甘くなっている。",
        "같은 거리를 VHS로. 네온에서 색이 옆으로 번져 나오고, 화면 아래쪽에 트래킹 찢김이 지나가며, "
        "닳은 테이프처럼 전체가 부드러워졌습니다.",
        "Dezelfde straat via VHS: kleur die zijwaarts van het neon afloopt, een trackingscheur over "
        "de onderkant van het beeld, alles verzacht als een versleten band.",
        "A mesma rua pelo VHS: cor sangrando de lado a partir do neon, rasgo de tracking na parte "
        "de baixo do quadro, tudo suavizado como uma fita gasta.",
        "同一条街道经过 VHS：颜色从霓虹上向侧面渗开，画面下方划过一道循迹撕裂，"
        "整体像一盘磨损的带子那样发软。"),
    "The same street through the Cyber preset: sharp red and cyan channel offset on every edge, a "
    "slow wave running through the geometry.": (
        "Dieselbe Straße durch das Cyber-Preset: scharfer Rot- und Cyan-Kanalversatz an jeder "
        "Kante, eine langsame Welle, die durch die Geometrie läuft.",
        "La misma calle pasada por el preajuste Cyber: desplazamiento nítido de los canales rojo y "
        "cian en cada borde, una onda lenta recorriendo la geometría.",
        "La misma calle pasada por el preajuste Cyber: desplazamiento nítido de los canales rojo y "
        "cian en cada borde, una onda lenta recorriendo la geometría.",
        "La même rue via le préréglage Cyber : décalage net des canaux rouge et cyan sur chaque "
        "arête, une onde lente qui parcourt la géométrie.",
        "La stessa strada con il preset Cyber: sfasamento netto dei canali rosso e ciano su ogni "
        "bordo, un'onda lenta che attraversa la geometria.",
        "同じ街路を Cyber プリセットで。あらゆる輪郭で赤とシアンのチャンネルが鋭くずれ、"
        "形の上をゆっくりとした波が走っている。",
        "같은 거리를 Cyber 프리셋으로. 모든 가장자리에서 빨강과 시안 채널이 날카롭게 어긋나고, "
        "형태 위로 느린 물결이 지나갑니다.",
        "Dezelfde straat via de Cyber-preset: scherpe rode en cyaan kanaalverschuiving op elke "
        "rand, een trage golf die door de geometrie loopt.",
        "A mesma rua pelo preset Cyber: deslocamento nítido dos canais vermelho e ciano em cada "
        "borda, uma onda lenta percorrendo a geometria.",
        "同一条街道经过 Cyber 预设：每一道边缘上红与青通道锐利地错开，"
        "一道缓慢的波从几何结构里穿过。"),
    "A yellow Japanese surveillance camera warning sign reduced to a coarse dithered palette with "
    "visible scanlines, like a screenshot from an old games console.": (
        "Ein gelbes japanisches Warnschild für Überwachungskameras, auf eine grobe gerasterte "
        "Palette mit sichtbaren Bildzeilen reduziert, wie ein Screenshot von einer alten "
        "Spielkonsole.",
        "Un cartel amarillo japonés de aviso de cámaras de vigilancia reducido a una paleta "
        "tramada gruesa con líneas visibles, como una captura de una consola antigua.",
        "Un letrero amarillo japonés de aviso de cámaras de vigilancia reducido a una paleta "
        "tramada gruesa con líneas visibles, como una captura de una consola antigua.",
        "Un panneau jaune japonais avertissant de la vidéosurveillance réduit à une palette "
        "tramée grossière avec des lignes visibles, comme une capture d'une vieille console.",
        "Un cartello giallo giapponese di avviso videosorveglianza ridotto a una palette "
        "retinata grossolana con righe visibili, come uno screenshot di una vecchia console.",
        "監視カメラ設置を知らせる黄色い日本語の看板を、粗いディザのパレットと目に見える走査線まで"
        "落としたもの。古いゲーム機のスクリーンショットのように。",
        "감시 카메라를 알리는 노란 일본어 표지판을, 거친 디더 팔레트와 눈에 보이는 주사선까지 "
        "떨어뜨린 것. 오래된 게임기의 스크린숏처럼.",
        "Een geel Japans waarschuwingsbord voor bewakingscamera's teruggebracht tot een grof "
        "gedither palet met zichtbare scanlijnen, als een schermafbeelding van een oude "
        "spelcomputer.",
        "Uma placa amarela japonesa de aviso de câmeras de vigilância reduzida a uma paleta "
        "pontilhada grosseira com linhas visíveis, como uma captura de um console antigo.",
        "一块黄色的日文监控摄像头警示牌，被压成粗糙的抖动调色板，还带着可见的扫描线，"
        "像是老游戏机的截图。"),
    "The Shinjuku crossing with buildings dragged into long vertical streaks by pixel sorting.": (
        "Die Kreuzung in Shinjuku, deren Gebäude vom Pixel Sorting zu langen senkrechten Schlieren "
        "gezogen wurden.",
        "El cruce de Shinjuku con los edificios arrastrados en largas vetas verticales por la "
        "ordenación de píxeles.",
        "El cruce de Shinjuku con los edificios arrastrados en largas vetas verticales por la "
        "ordenación de píxeles.",
        "Le carrefour de Shinjuku dont les immeubles sont tirés en longues traînées verticales par "
        "le tri de pixels.",
        "L'incrocio di Shinjuku con i palazzi trascinati in lunghe strisce verticali dal pixel "
        "sorting.",
        "ピクセルソートによって、ビルが長い縦の筋へと引き伸ばされた新宿の交差点。",
        "픽셀 정렬로 건물들이 긴 세로 줄기로 끌려 나온 신주쿠의 교차로.",
        "De kruising in Shinjuku met gebouwen die door pixel sorting tot lange verticale strepen "
        "zijn getrokken.",
        "O cruzamento de Shinjuku com os prédios arrastados em longos riscos verticais pela "
        "ordenação de pixels.",
        "新宿路口，楼群被像素排序拖成长长的竖直条纹。"),
    "The untouched source photograph of the surveillance camera sign, for comparison.": (
        "Das unbearbeitete Ausgangsfoto des Überwachungskameraschilds, zum Vergleich.",
        "La fotografía fuente sin tocar del cartel de cámaras de vigilancia, para comparar.",
        "La fotografía fuente sin tocar del letrero de cámaras de vigilancia, para comparar.",
        "La photographie source intacte du panneau de vidéosurveillance, pour comparaison.",
        "La fotografia sorgente intatta del cartello della videosorveglianza, per confronto.",
        "比較用の、監視カメラの看板の未加工の元写真。",
        "비교를 위한, 감시 카메라 표지판의 손대지 않은 원본 사진.",
        "De onbewerkte bronfoto van het bewakingscamerabord, ter vergelijking.",
        "A fotografia de origem intocada da placa de câmeras de vigilância, para comparação.",
        "作为对照的监控摄像头警示牌原始照片，未经处理。"),
    "Untouched source": ("Unbearbeitete Quelle", "Fuente sin tocar", "Fuente sin tocar",
                         "Source intacte", "Sorgente intatta", "未加工の元画像", "손대지 않은 원본",
                         "Onbewerkte bron", "Origem intocada", "未处理的原图"),
    "The interface": ("Die Oberfläche", "La interfaz", "La interfaz", "L'interface",
                      "L'interfaccia", "画面", "인터페이스", "De interface", "A interface",
                      "界面"),
    "MODUL8 running on iPhone: the glitched canvas at the top, a row of preset buttons, and the "
    "layer list showing Noise, Distortion and RGB Split.": (
        "MODUL8 auf dem iPhone: oben die geglitchte Leinwand, eine Reihe Preset-Tasten und die "
        "Ebenenliste mit Rauschen, Verzerrung und RGB.",
        "MODUL8 en iPhone: el lienzo con glitch arriba, una fila de botones de preajuste y la "
        "lista de capas con Ruido, Distorsión y RGB.",
        "MODUL8 en iPhone: el lienzo con glitch arriba, una fila de botones de preajuste y la "
        "lista de capas con Ruido, Distorsión y RGB.",
        "MODUL8 sur iPhone : la toile glitchée en haut, une rangée de boutons de préréglage, et la "
        "liste des calques avec Bruit, Distorsion et RVB.",
        "MODUL8 su iPhone: la tela glitchata in alto, una fila di pulsanti preset e l'elenco dei "
        "livelli con Rumore, Distorsione e RGB.",
        "iPhone で動く MODUL8。上にグリッチのかかったキャンバス、プリセットボタンの列、"
        "そしてノイズ・歪み・RGB分離が並んだレイヤー一覧。",
        "iPhone에서 실행 중인 MODUL8. 위에는 글리치가 걸린 캔버스, 프리셋 버튼 한 줄, 그리고 "
        "노이즈, 왜곡, RGB 분리가 늘어선 레이어 목록.",
        "MODUL8 op iPhone: het geglitchte canvas bovenaan, een rij presetknoppen en de lagenlijst "
        "met Ruis, Vervorming en RGB.",
        "MODUL8 rodando no iPhone: a tela glitchada no topo, uma fileira de botões de preset e a "
        "lista de camadas com Ruído, Distorção e RGB.",
        "在 iPhone 上运行的 MODUL8：上方是带故障效果的画布，一排预设按钮，"
        "以及列出噪点、畸变和 RGB 分离的图层列表。"),
    "The layer stack with three effects listed and a drag handle on each, above the horizontal "
    "effect rack.": (
        "Der Ebenenstapel mit drei aufgeführten Effekten und je einem Ziehgriff, über dem "
        "waagerechten Effektregal.",
        "La pila de capas con tres efectos listados y un asa de arrastre en cada uno, sobre el "
        "estante horizontal de efectos.",
        "La pila de capas con tres efectos listados y un asa de arrastre en cada uno, sobre el "
        "estante horizontal de efectos.",
        "La pile de calques avec trois effets listés et une poignée de déplacement sur chacun, "
        "au-dessus du râtelier d'effets horizontal.",
        "Lo stack dei livelli con tre effetti elencati e una maniglia di trascinamento su ognuno, "
        "sopra la rastrelliera orizzontale degli effetti.",
        "三つのエフェクトが並び、それぞれにドラッグ用のつまみが付いたレイヤースタック。"
        "その下に横並びのエフェクトの棚。",
        "세 개의 효과가 나열되고 각각에 드래그 손잡이가 달린 레이어 스택. 그 아래로 가로로 놓인 "
        "효과 선반.",
        "De lagenstapel met drie effecten en op elk een sleepgreep, boven het horizontale "
        "effectenrek.",
        "A pilha de camadas com três efeitos listados e uma alça de arraste em cada um, acima da "
        "prateleira horizontal de efeitos.",
        "图层堆栈中列出三种效果，每一项都带有拖动手柄，下方是横向排列的效果架。"),
    "A melted pixel-sorted crossing on the canvas with four effects stacked below it.": (
        "Eine geschmolzene, pixelsortierte Kreuzung auf der Leinwand, darunter vier gestapelte "
        "Effekte.",
        "Un cruce fundido por ordenación de píxeles en el lienzo, con cuatro efectos apilados "
        "debajo.",
        "Un cruce fundido por ordenación de píxeles en el lienzo, con cuatro efectos apilados "
        "debajo.",
        "Un carrefour fondu par tri de pixels sur la toile, avec quatre effets empilés en dessous.",
        "Un incrocio sciolto dal pixel sorting sulla tela, con quattro effetti impilati sotto.",
        "ピクセルソートで溶けた交差点がキャンバスに映り、その下に四つのエフェクトが積まれている。",
        "픽셀 정렬로 녹아내린 교차로가 캔버스에 있고, 그 아래에 네 개의 효과가 쌓여 있습니다.",
        "Een gesmolten, pixel-gesorteerde kruising op het canvas met vier effecten eronder "
        "gestapeld.",
        "Um cruzamento derretido por ordenação de pixels na tela, com quatro efeitos empilhados "
        "abaixo.",
        "画布上是被像素排序融化的路口，下面叠着四种效果。"),
    "On the device": ("Auf dem Gerät", "En el dispositivo", "En el dispositivo",
                      "Sur l'appareil", "Sul dispositivo", "端末の上で", "기기 안에서",
                      "Op het toestel", "No aparelho", "在设备上"),
    "Your photos stay on your phone.": (
        "Deine Fotos bleiben auf deinem Telefon.", "Tus fotos se quedan en tu móvil.",
        "Tus fotos se quedan en tu celular.", "Vos photos restent sur votre téléphone.",
        "Le tue foto restano sul tuo telefono.", "写真は端末に留まります。",
        "당신의 사진은 휴대폰에 남습니다.", "Je foto's blijven op je telefoon.",
        "Suas fotos ficam no seu telefone.", "你的照片留在你的手机里。"),
    "Video too": ("Auch Video", "También vídeo", "También video", "La vidéo aussi", "Anche video",
                  "動画も", "영상도", "Video ook", "Vídeo também", "视频也可以"),
    "The deal": ("Das Angebot", "El trato", "El trato", "Le deal", "L'accordo", "料金のこと",
                 "조건", "De deal", "O acordo", "价格是这样的"),
    "Free. Premium is optional.": (
        "Kostenlos. Premium ist optional.", "Gratis. Premium es opcional.",
        "Gratis. Premium es opcional.", "Gratuit. Premium est facultatif.",
        "Gratis. Premium è facoltativo.", "無料。Premium は任意です。",
        "무료. Premium은 선택입니다.", "Gratis. Premium is optioneel.",
        "Grátis. O Premium é opcional.", "免费。Premium 是可选的。"),
    "Free": ("Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료", "Gratis",
             "Grátis", "免费"),
    "Premium": ("Premium",) * 10,
    "Privacy policy": ("Datenschutzerklärung", "Política de privacidad", "Política de privacidad",
                       "Politique de confidentialité", "Informativa sulla privacy",
                       "プライバシーポリシー", "개인정보 처리방침", "Privacybeleid",
                       "Política de privacidade", "隐私政策"),
    "Questions": ("Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問",
                  "질문", "Vragen", "Perguntas", "常见问题"),
    "The things people ask first.": (
        "Was zuerst gefragt wird.", "Lo que la gente pregunta primero.",
        "Lo que la gente pregunta primero.", "Ce que les gens demandent en premier.",
        "Le cose che chiedono per prime.", "最初に聞かれること。",
        "사람들이 가장 먼저 묻는 것들.", "Wat mensen als eerste vragen.",
        "O que as pessoas perguntam primeiro.", "大家最先问的问题。"),
    "MODUL8 is built by": ("MODUL8 wird gebaut von", "MODUL8 lo hace", "MODUL8 lo hace",
                           "MODUL8 est fait par", "MODUL8 è fatto da", "MODUL8 をつくっているのは",
                           "MODUL8를 만드는 사람은", "MODUL8 wordt gemaakt door",
                           "O MODUL8 é feito por", "MODUL8 由"),
    "in Fort Worth, Texas": ("in Fort Worth, Texas", "en Fort Worth, Texas",
                             "en Fort Worth, Texas", "à Fort Worth, Texas",
                             "a Fort Worth, Texas", "（テキサス州フォートワース）",
                             "(텍사스주 포트워스)", "in Fort Worth, Texas",
                             "em Fort Worth, Texas", "在美国得州沃斯堡打造"),
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "FRMT film simulation": ("FRMT Filmsimulation", "FRMT simulación de película",
                             "FRMT simulación de película", "FRMT simulation argentique",
                             "FRMT simulazione di pellicola", "FRMT フィルムシミュレーション",
                             "FRMT 필름 시뮬레이션", "FRMT filmsimulatie",
                             "FRMT simulação de filme", "FRMT 胶片模拟"),
    "CYANO cyanotype": ("CYANO Cyanotypie", "CYANO cianotipia", "CYANO cianotipia",
                        "CYANO cyanotype", "CYANO cianotipia", "CYANO サイアノタイプ",
                        "CYANO 사이아노타입", "CYANO cyanotypie", "CYANO cianotipia",
                        "CYANO 蓝晒"),
})

# ---------------------------------------------------------------- FAQ and structured data
_DIFFERENT_ANSWER = (
    "Die meisten legen ein festes Muster über alles, was du ihnen gibst, und jedes Foto kommt im "
    "selben Kostüm heraus. Jeder MODUL8-Effekt bildet einen bestimmten Hardwarefehler nach und "
    "liest die Pixel darunter, bevor er entscheidet, was er tut, also liefern dieselben "
    "Einstellungen auf verschiedenen Fotos verschiedene Ergebnisse.",
    "La mayoría pone un patrón fijo sobre lo que le des, y cada foto sale con el mismo disfraz. "
    "Cada efecto de MODUL8 modela un fallo de hardware concreto y lee los píxeles de debajo antes "
    "de decidir qué hacer, así que los mismos ajustes dan resultados distintos en fotos distintas.",
    "La mayoría pone un patrón fijo sobre lo que le des, y cada foto sale con el mismo disfraz. "
    "Cada efecto de MODUL8 modela una falla de hardware concreta y lee los píxeles de debajo antes "
    "de decidir qué hacer, así que los mismos ajustes dan resultados distintos en fotos distintas.",
    "La plupart posent un motif fixe sur tout ce que vous leur donnez, et chaque photo ressort avec "
    "le même costume. Chaque effet de MODUL8 modélise une panne matérielle précise et lit les "
    "pixels en dessous avant de décider quoi faire, si bien que les mêmes réglages donnent des "
    "résultats différents sur des photos différentes.",
    "Quasi tutte mettono un motivo fisso su qualunque cosa gli dai, e ogni foto esce con lo stesso "
    "costume. Ogni effetto di MODUL8 modella un guasto hardware preciso e legge i pixel sotto prima "
    "di decidere cosa fare, quindi le stesse impostazioni danno risultati diversi su foto diverse.",
    "たいていは、渡されたものが何であれ決まった模様を上に載せるので、どの写真も同じ衣装を着て"
    "出てきます。MODUL8 のエフェクトはそれぞれ特定のハードウェア故障を再現し、"
    "下にある画素を読んでから何をするかを決めます。だから同じ設定でも、写真が違えば結果は"
    "違います。",
    "대부분은 무엇을 주든 정해진 무늬를 얹기 때문에, 어떤 사진이든 같은 옷을 입고 나옵니다. "
    "MODUL8의 각 효과는 특정한 하드웨어 고장을 모델링하고, 아래에 있는 픽셀을 읽은 뒤에 무엇을 "
    "할지 정합니다. 그래서 같은 설정이라도 사진이 다르면 결과가 다릅니다.",
    "De meeste leggen een vast patroon over wat je ze ook geeft, en elke foto komt eruit in "
    "hetzelfde kostuum. Elk MODUL8-effect modelleert één specifieke hardwarestoring en leest de "
    "pixels eronder voordat het besluit wat het doet, dus dezelfde instellingen geven verschillende "
    "resultaten op verschillende foto's.",
    "A maioria põe um padrão fixo sobre o que você der, e cada foto sai vestindo a mesma fantasia. "
    "Cada efeito do MODUL8 modela uma falha de hardware específica e lê os pixels embaixo antes de "
    "decidir o que fazer, então os mesmos ajustes dão resultados diferentes em fotos diferentes.",
    "多数应用是你给它什么，它都盖上一套固定的图案，于是每张照片都穿着同一件戏服出来。"
    "MODUL8 的每一种效果都模拟某一个具体的硬件故障，并且会先读取底下的像素再决定要做什么，"
    "所以同样的设置在不同照片上会给出不同的结果。")

T.update({
    "Is MODUL8 free?": ("Ist MODUL8 kostenlos?", "¿MODUL8 es gratis?", "¿MODUL8 es gratis?",
                        "MODUL8 est-il gratuit ?", "MODUL8 è gratis?", "MODUL8 は無料ですか。",
                        "MODUL8는 무료인가요?", "Is MODUL8 gratis?", "O MODUL8 é grátis?",
                        "MODUL8 是免费的吗？"),
    "What effects are in it?": (
        "Welche Effekte sind drin?", "¿Qué efectos trae?", "¿Qué efectos trae?",
        "Quels effets contient-il ?", "Che effetti ci sono?", "どんなエフェクトが入っていますか。",
        "어떤 효과가 들어 있나요?", "Welke effecten zitten erin?", "Que efeitos tem nele?",
        "里面有哪些效果？"),
    "How is it different from other glitch apps?": (
        "Wie unterscheidet es sich von anderen Glitch-Apps?",
        "¿En qué se diferencia de otras apps de glitch?",
        "¿En qué se diferencia de otras apps de glitch?",
        "En quoi diffère-t-il des autres apps de glitch ?",
        "In cosa differisce dalle altre app di glitch?",
        "ほかのグリッチアプリと何が違うのですか。",
        "다른 글리치 앱과 무엇이 다른가요?",
        "Waarin verschilt het van andere glitch-apps?",
        "Como ele é diferente de outros apps de glitch?", "它和其他故障类应用有什么不同？"),
    "Most of them lay a fixed pattern over whatever you give them, so every photo comes out\n"
    "        wearing the same costume. Each MODUL8 effect models one specific hardware failure and "
    "reads\n        the pixels underneath before deciding what to do, so the same settings give "
    "different\n        results on different photographs.": _DIFFERENT_ANSWER,
    "Does it upload my photos?": (
        "Lädt es meine Fotos hoch?", "¿Sube mis fotos?", "¿Sube mis fotos?",
        "Est-ce qu'il envoie mes photos ?", "Carica le mie foto?",
        "写真をアップロードしますか。", "제 사진을 업로드하나요?", "Uploadt het mijn foto's?",
        "Ele envia minhas fotos?", "它会上传我的照片吗？"),
    "Can it make glitch videos?": (
        "Kann es Glitch-Videos machen?", "¿Puede hacer vídeos glitch?",
        "¿Puede hacer videos glitch?", "Peut-il faire des vidéos glitch ?",
        "Può fare video glitch?", "グリッチ動画はつくれますか。", "글리치 영상도 만들 수 있나요?",
        "Kan het glitch-video's maken?", "Ele consegue fazer vídeos glitch?",
        "它能做故障视频吗？"),
    "Which iPhones does it work on?": (
        "Auf welchen iPhones läuft es?", "¿En qué iPhones funciona?", "¿En qué iPhones funciona?",
        "Sur quels iPhone fonctionne-t-il ?", "Su quali iPhone funziona?",
        "どの iPhone で使えますか。", "어떤 iPhone에서 쓸 수 있나요?",
        "Op welke iPhones werkt het?", "Em quais iPhones funciona?", "支持哪些 iPhone？"),
    "Reorderable effect layers": (
        "Umsortierbare Effektebenen", "Capas de efectos reordenables",
        "Capas de efectos reordenables", "Calques d'effets réordonnables",
        "Livelli di effetti riordinabili", "順序を入れ替えられるエフェクトレイヤー",
        "순서를 바꿀 수 있는 효과 레이어", "Herschikbare effectlagen",
        "Camadas de efeitos reordenáveis", "可重新排序的效果图层"),
})

# ---------------------------------------------------------------- 2.0
#
# Everything the 2.0 release changed: 29 effects with the free/Premium split, video, settings that
# move, stamps and masks, the preset packs, GPU rendering, no ads. The keys are written with their
# line wrapping collapsed; merge.py matches them against the page and the FAQ schema alike.
#
# The effect roll-call in the FAQ answer uses the names the app's localised 2.0 listing uses, so a
# reader can match every word against a button.
T.update({
    "MODUL8 is a free glitch art app for iPhone. 29 stackable effects for photos and video, "
    "modelled on real hardware failures: VHS, CRT, datamosh, pixel sorting, satellite dropout. "
    "Runs on device.": (
        "MODUL8 ist eine kostenlose Glitch-Art-App für iPhone. 29 stapelbare Effekte für Fotos und "
        "Video, echten Hardwarefehlern nachgebildet: VHS, CRT, Datamosh, Pixel Sorting, "
        "abreißendes Satellitensignal. Läuft auf dem Gerät.",
        "MODUL8 es una app de glitch art gratis para iPhone. 29 efectos apilables para fotos y "
        "vídeo, modelados sobre fallos reales de hardware: VHS, CRT, datamosh, ordenación de "
        "píxeles, señal de satélite perdida. Funciona en el dispositivo.",
        "MODUL8 es una app de glitch art gratis para iPhone. 29 efectos apilables para fotos y "
        "video, modelados sobre fallas reales de hardware: VHS, CRT, datamosh, ordenación de "
        "píxeles, señal de satélite perdida. Funciona en el dispositivo.",
        "MODUL8 est une app de glitch art gratuite pour iPhone. 29 effets empilables pour photos et "
        "vidéos, modélisés sur de vraies pannes de matériel : VHS, CRT, datamosh, tri de pixels, "
        "signal satellite qui décroche. Fonctionne sur l'appareil.",
        "MODUL8 è un'app di glitch art gratis per iPhone. 29 effetti impilabili per foto e video, "
        "modellati su guasti hardware reali: VHS, CRT, datamosh, pixel sorting, segnale "
        "satellitare perso. Gira sul dispositivo.",
        "MODUL8 は iPhone 用の無料グリッチアートアプリです。写真にも動画にも使える、実在の"
        "ハードウェア故障を再現した、積み重ねられる 29 のエフェクト。VHS、CRT、データモッシュ、"
        "ピクセルソート、途切れた衛星放送。処理は端末上で完結します。",
        "MODUL8는 iPhone용 무료 글리치 아트 앱입니다. 실제 하드웨어 고장을 모델링한, 사진과 "
        "동영상에 쌓아 올릴 수 있는 29가지 효과. VHS, CRT, 데이터모시, 픽셀 정렬, 끊긴 위성 신호. "
        "기기 안에서 처리합니다.",
        "MODUL8 is een gratis glitch-art-app voor iPhone. 29 stapelbare effecten voor foto's en "
        "video, gemodelleerd op echte hardwarestoringen: VHS, CRT, datamosh, pixel sorting, "
        "wegvallend satellietsignaal. Draait op het toestel.",
        "O MODUL8 é um app de glitch art grátis para iPhone. 29 efeitos empilháveis para fotos e "
        "vídeos, modelados sobre falhas reais de hardware: VHS, CRT, datamosh, ordenação de "
        "pixels, sinal de satélite caindo. Roda no aparelho.",
        "MODUL8 是一款 iPhone 上的免费故障艺术应用。29 种可叠加效果，照片和视频都能用，"
        "每一种都对应真实硬件的故障：VHS、CRT、数据莫氏、像素排序、失锁的卫星信号。"
        "全部在设备上运行。"),
    "29 stackable glitch effects for photos and video, modelled on real hardware failures: VHS, "
    "CRT, datamosh, pixel sorting. Free on iPhone.": (
        "29 stapelbare Glitch-Effekte für Fotos und Video, echten Hardwarefehlern nachgebildet: "
        "VHS, CRT, Datamosh, Pixel Sorting. Kostenlos auf iPhone.",
        "29 efectos glitch apilables para fotos y vídeo, modelados sobre fallos reales de "
        "hardware: VHS, CRT, datamosh, ordenación de píxeles. Gratis en iPhone.",
        "29 efectos glitch apilables para fotos y video, modelados sobre fallas reales de "
        "hardware: VHS, CRT, datamosh, ordenación de píxeles. Gratis en iPhone.",
        "29 effets glitch empilables pour photos et vidéos, modélisés sur de vraies pannes de "
        "matériel : VHS, CRT, datamosh, tri de pixels. Gratuit sur iPhone.",
        "29 effetti glitch impilabili per foto e video, modellati su guasti hardware reali: VHS, "
        "CRT, datamosh, pixel sorting. Gratis su iPhone.",
        "写真にも動画にも使える、実在のハードウェア故障を再現した、積み重ねられる 29 の"
        "グリッチエフェクト。VHS、CRT、データモッシュ、ピクセルソート。iPhone で無料。",
        "실제 하드웨어 고장을 모델링한, 사진과 동영상에 쌓아 올릴 수 있는 29가지 글리치 효과. "
        "VHS, CRT, 데이터모시, 픽셀 정렬. iPhone에서 무료.",
        "29 stapelbare glitch-effecten voor foto's en video, gemodelleerd op echte "
        "hardwarestoringen: VHS, CRT, datamosh, pixel sorting. Gratis op iPhone.",
        "29 efeitos glitch empilháveis para fotos e vídeos, modelados sobre falhas reais de "
        "hardware: VHS, CRT, datamosh, ordenação de pixels. Grátis no iPhone.",
        "29 种可叠加的故障效果，照片和视频都能用，对应真实硬件的故障：VHS、CRT、数据莫氏、"
        "像素排序。iPhone 上免费。"),
    "MODUL8 is an image modulation kit for iPhone. Twenty-nine effects, each one modelled on a "
    "specific way that real hardware used to fail: tape that lost tracking, tubes that bloomed at "
    "the edges, a satellite feed losing lock, compression that gave up halfway through a frame. "
    "Stack them, reorder them, and turn a photo or a video clip into something that looks like it "
    "came off a machine that was already dying.": (
        "MODUL8 ist ein Baukasten zur Bildmodulation für iPhone. Neunundzwanzig Effekte, jeder "
        "einer bestimmten Art nachgebildet, auf die echte Hardware früher versagte: Band, das die "
        "Spur verlor, Röhren, die an den Rändern blühten, ein Satellitensignal, das abriss, "
        "Kompression, die mitten im Bild aufgab. Staple sie, ordne sie um, und mach aus einem Foto "
        "oder einem Videoclip etwas, das aussieht, als käme es aus einer Maschine, die schon im "
        "Sterben lag.",
        "MODUL8 es un kit de modulación de imagen para iPhone. Veintinueve efectos, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: cinta que perdía el "
        "tracking, tubos que florecían por los bordes, una señal de satélite que se caía, "
        "compresión que se rendía a mitad de fotograma. Apílalos, reordénalos y convierte una foto "
        "o un clip de vídeo en algo que parece salido de una máquina que ya se estaba muriendo.",
        "MODUL8 es un kit de modulación de imagen para iPhone. Veintinueve efectos, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: cinta que perdía el "
        "tracking, tubos que florecían por los bordes, una señal de satélite que se caía, "
        "compresión que se rendía a mitad de cuadro. Apílalos, reordénalos y convierte una foto o "
        "un clip de video en algo que parece salido de una máquina que ya se estaba muriendo.",
        "MODUL8 est un kit de modulation d'image pour iPhone. Vingt-neuf effets, chacun modélisé "
        "sur une façon précise dont le matériel tombait en panne : la bande qui perdait la piste, "
        "les tubes qui fleurissaient sur les bords, un signal satellite qui décrochait, la "
        "compression qui abandonnait au milieu d'une image. Empilez-les, réordonnez-les, et "
        "transformez une photo ou un clip vidéo en quelque chose qui semble sorti d'une machine "
        "déjà mourante.",
        "MODUL8 è un kit di modulazione dell'immagine per iPhone. Ventinove effetti, ognuno "
        "modellato su un modo preciso in cui l'hardware vero si guastava: il nastro che perdeva il "
        "tracking, i tubi che fiorivano ai bordi, un segnale satellitare che perdeva l'aggancio, la "
        "compressione che si arrendeva a metà fotogramma. Impilali, riordinali, e trasforma una "
        "foto o una clip video in qualcosa che sembra uscito da una macchina già morente.",
        "MODUL8 は iPhone のための画像モジュレーションキットです。二十九のエフェクトは、"
        "いずれも実在のハードウェアが壊れたときの特定の壊れ方を再現しています。トラッキングを"
        "失ったテープ、端がにじんだブラウン管、受信が途切れた衛星放送、一枚の途中で諦めた圧縮。"
        "積み重ね、順序を入れ替えれば、写真も動画のクリップも、すでに死にかけていた機械から"
        "出てきたような姿になります。",
        "MODUL8는 iPhone을 위한 이미지 변조 키트입니다. 스물아홉 가지 효과가 각각 실제 하드웨어가 "
        "고장 나던 특정한 방식을 모델링합니다. 트래킹을 잃은 테이프, 가장자리가 번진 브라운관, "
        "신호를 놓친 위성 방송, 한 프레임 도중에 포기해 버린 압축. 쌓고, 순서를 바꾸면, 사진이든 "
        "동영상 클립이든 이미 죽어 가던 기계에서 나온 것처럼 됩니다.",
        "MODUL8 is een beeldmodulatiekit voor iPhone. Negenentwintig effecten, elk gemodelleerd "
        "op een specifieke manier waarop echte hardware kapotging: band die de tracking verloor, "
        "buizen die aan de randen opbloeiden, een satellietsignaal dat wegviel, compressie die "
        "halverwege een beeld opgaf. Stapel ze, herschik ze, en maak van een foto of een videoclip "
        "iets dat eruitziet alsof het van een machine komt die al aan het sterven was.",
        "O MODUL8 é um kit de modulação de imagem para iPhone. Vinte e nove efeitos, cada um "
        "modelado sobre um jeito específico pelo qual o hardware de verdade falhava: fita que "
        "perdia o tracking, tubos que floresciam nas bordas, um sinal de satélite que caía, "
        "compressão que desistia no meio de um quadro. Empilhe, reordene, e transforme uma foto ou "
        "um clipe de vídeo em algo que parece ter saído de uma máquina que já estava morrendo.",
        "MODUL8 是一套 iPhone 上的图像调制工具。二十九种效果，每一种都对应真实硬件当年出错的"
        "某种具体方式：跑了带的磁带、边缘晕开的显像管、失锁的卫星信号、在一帧中途放弃的压缩。"
        "把它们叠起来、换个顺序，一张照片或一段视频就会变成像是从一台已经在垂死的机器里"
        "吐出来的东西。"),
    "The nineteen classic effects are free, there are no ads, everything renders on your phone, "
    "and nothing you open in it is ever uploaded.": (
        "Die neunzehn klassischen Effekte sind kostenlos, es gibt keine Werbung, alles wird auf "
        "deinem Telefon gerechnet, und nichts, was du darin öffnest, wird je hochgeladen.",
        "Los diecinueve efectos clásicos son gratis, no hay anuncios, todo se procesa en tu móvil "
        "y nada de lo que abres en ella se sube nunca.",
        "Los diecinueve efectos clásicos son gratis, no hay anuncios, todo se procesa en tu "
        "celular y nada de lo que abres en ella se sube nunca.",
        "Les dix-neuf effets classiques sont gratuits, il n'y a pas de publicité, tout est calculé "
        "sur votre téléphone, et rien de ce que vous y ouvrez n'est jamais envoyé.",
        "I diciannove effetti classici sono gratis, non c'è pubblicità, tutto viene elaborato sul "
        "tuo telefono, e niente di quello che ci apri viene mai caricato.",
        "定番の十九のエフェクトは無料で、広告はなく、描画はすべてあなたの端末の上で行われ、"
        "開いたものがアップロードされることは一度もありません。",
        "기본 효과 열아홉 가지는 무료이고, 광고는 없으며, 모든 렌더링이 당신의 휴대폰에서 "
        "이루어지고, 앱에서 연 것은 무엇도 업로드되지 않습니다.",
        "De negentien klassieke effecten zijn gratis, er zijn geen advertenties, alles wordt op je "
        "telefoon gerenderd, en niets wat je erin opent wordt ooit geüpload.",
        "Os dezenove efeitos clássicos são grátis, não há anúncios, tudo é renderizado no seu "
        "telefone, e nada do que você abre nele é enviado, nunca.",
        "十九种经典效果免费，没有广告，一切都在你的手机上渲染，你在里面打开的任何东西都不会"
        "被上传。"),
    "Nothing is baked in. Twenty-nine effects, stacked in any order you like.": (
        "Nichts ist festgelegt. Neunundzwanzig Effekte, gestapelt in beliebiger Reihenfolge.",
        "Nada está fijado. Veintinueve efectos, apilados en el orden que quieras.",
        "Nada está fijado. Veintinueve efectos, apilados en el orden que quieras.",
        "Rien n'est figé. Vingt-neuf effets, empilés dans l'ordre qui vous plaît.",
        "Niente è fissato. Ventinove effetti, impilati nell'ordine che preferisci.",
        "決め打ちのものはありません。二十九のエフェクトを、好きな順序で重ねて。",
        "정해진 것은 없습니다. 스물아홉 가지 효과를, 원하는 순서로 쌓아서.",
        "Niets ligt vast. Negenentwintig effecten, gestapeld in welke volgorde je maar wilt.",
        "Nada é fixo. Vinte e nove efeitos, empilhados na ordem que você preferir.",
        "没有任何东西是写死的。二十九种效果，按你喜欢的顺序叠加。"),
    "Twenty-nine effects. Every one of them is a real failure mode.": (
        "Neunundzwanzig Effekte. Jeder davon ist ein echter Fehlermodus.",
        "Veintinueve efectos. Cada uno es un modo de fallo real.",
        "Veintinueve efectos. Cada uno es un modo de falla real.",
        "Vingt-neuf effets. Chacun est un mode de panne réel.",
        "Ventinove effetti. Ognuno è una modalità di guasto reale.",
        "二十九のエフェクト。そのどれもが、実在した壊れ方です。",
        "스물아홉 가지 효과. 그 하나하나가 실제로 있었던 고장 방식입니다.",
        "Negenentwintig effecten. Elk ervan is een echte storingsmodus.",
        "Vinte e nove efeitos. Cada um deles é um modo de falha real.",
        "二十九种效果。每一种都是真实存在过的失效方式。"),
    "They are not variations on a theme. Each one models something different, which is why "
    "stacking them gets interesting instead of muddy. Nineteen classics are free, and ten more "
    "come with Premium.": (
        "Sie sind keine Variationen eines Themas. Jeder bildet etwas anderes nach, und darum wird "
        "das Stapeln interessant statt matschig. Neunzehn Klassiker sind kostenlos, zehn weitere "
        "gibt es mit Premium.",
        "No son variaciones sobre un tema. Cada uno modela algo distinto, y por eso apilarlos "
        "resulta interesante en vez de embarrado. Diecinueve clásicos son gratis, y diez más "
        "vienen con Premium.",
        "No son variaciones sobre un tema. Cada uno modela algo distinto, y por eso apilarlos "
        "resulta interesante en vez de embarrado. Diecinueve clásicos son gratis, y diez más "
        "vienen con Premium.",
        "Ce ne sont pas des variations sur un thème. Chacun modélise quelque chose de différent, "
        "et c'est pourquoi les empiler devient intéressant au lieu de devenir boueux. Dix-neuf "
        "classiques sont gratuits, et dix de plus viennent avec Premium.",
        "Non sono variazioni su un tema. Ognuno modella qualcosa di diverso, ed è per questo che "
        "impilarli diventa interessante invece che fangoso. Diciannove classici sono gratis, e "
        "altri dieci arrivano con Premium.",
        "同じ主題の変奏ではありません。どれも別のものを再現しているので、重ねると濁るのではなく、"
        "面白くなります。定番の十九は無料で、さらに十が Premium で加わります。",
        "하나의 주제에 대한 변주가 아닙니다. 각각이 서로 다른 것을 모델링하기 때문에, 쌓으면 "
        "탁해지는 대신 흥미로워집니다. 기본 열아홉 가지는 무료이고, 열 가지가 Premium으로 "
        "더해집니다.",
        "Het zijn geen variaties op een thema. Elk modelleert iets anders, en daarom wordt stapelen "
        "interessant in plaats van modderig. Negentien klassiekers zijn gratis, en nog tien komen "
        "met Premium.",
        "Não são variações sobre um tema. Cada um modela algo diferente, e é por isso que "
        "empilhá-los fica interessante em vez de embolado. Dezenove clássicos são grátis, e mais "
        "dez vêm com o Premium.",
        "它们不是同一个主题的变奏。每一种模拟的都是不同的东西，所以叠起来会变得有意思，"
        "而不是糊成一团。十九种经典效果免费，另外十种随 Premium 提供。"),
    "Ten more with Premium": (
        "Zehn weitere mit Premium", "Diez más con Premium", "Diez más con Premium",
        "Dix de plus avec Premium", "Altri dieci con Premium", "Premium でさらに十",
        "Premium으로 열 가지 더", "Nog tien met Premium", "Mais dez com o Premium",
        "Premium 再加十种"),
    "New in 2.0, and each one another machine to fail through: a satellite feed losing lock, a "
    "broadcast arriving twice and leaving a ghost, slow-scan television, teletext, a fax line, a "
    "picture reposted until it wears out, a webcam, a handheld games console, a magnet held to a "
    "tube, and tape chewed up by the deck.": (
        "Neu in 2.0, und jeder davon eine weitere Maschine, an der etwas kaputtgehen kann: ein "
        "Satellitensignal, das abreißt, eine Sendung, die doppelt ankommt und ein Geisterbild "
        "hinterlässt, Slow-Scan-Fernsehen, Videotext, eine Faxleitung, ein Bild, das so oft neu "
        "gepostet wurde, bis es verschlissen ist, eine Webcam, eine Handheld-Konsole, ein Magnet "
        "an der Bildröhre und Band, das der Rekorder zu Bandsalat gekaut hat.",
        "Nuevos en la 2.0, y cada uno otra máquina con la que fallar: una señal de satélite que se "
        "cae, una emisión que llega dos veces y deja una doble imagen, televisión de barrido "
        "lento, teletexto, una línea de fax, una imagen resubida hasta gastarse, una webcam, una "
        "consola portátil, un imán pegado a un tubo y una cinta masticada por el aparato.",
        "Nuevos en la 2.0, y cada uno otra máquina con la cual fallar: una señal de satélite que "
        "se cae, una transmisión que llega dos veces y deja una doble imagen, televisión de "
        "barrido lento, teletexto, una línea de fax, una imagen resubida hasta gastarse, una "
        "webcam, una consola portátil, un imán pegado a un cinescopio y una cinta masticada por la "
        "videocasetera.",
        "Nouveaux dans la 2.0, et chacun une machine de plus par laquelle tomber en panne : un "
        "signal satellite qui décroche, une émission qui arrive deux fois et laisse un "
        "dédoublement, la télévision à balayage lent, le télétexte, une ligne de fax, une image "
        "repostée jusqu'à l'usure, une webcam, une console portable, un aimant posé contre un tube, "
        "et une bande mangée par le magnétoscope.",
        "Nuovi nella 2.0, e ognuno un'altra macchina attraverso cui guastarsi: un segnale "
        "satellitare che perde l'aggancio, una trasmissione che arriva due volte e lascia uno "
        "sdoppiamento, la televisione a scansione lenta, il televideo, una linea fax, un'immagine "
        "ripostata finché non si consuma, una webcam, una console portatile, una calamita "
        "appoggiata a un tubo catodico, e un nastro mangiato dal videoregistratore.",
        "2.0 で新しく加わったもので、どれもまた別の機械の壊れ方です。受信が途切れた衛星放送、"
        "二重に届いてゴーストを残す放送、低速走査テレビ、文字放送、FAX の回線、再投稿を重ねて"
        "すり減った画像、Web カメラ、携帯ゲーム機、ブラウン管に近づけた磁石、そしてデッキに"
        "噛まれたテープ。",
        "2.0에서 새로 들어온 것들로, 하나하나가 또 다른 기계의 고장 방식입니다. 신호를 놓친 위성 "
        "방송, 두 번 도착해 고스트를 남기는 방송, 저속 주사 텔레비전, 문자방송, 팩스 회선, "
        "재업로드를 거듭하다 닳아 버린 사진, 웹캠, 휴대 게임기, 브라운관에 갖다 댄 자석, 그리고 "
        "데크에 씹힌 테이프.",
        "Nieuw in 2.0, en elk een volgende machine om door kapot te gaan: een satellietsignaal dat "
        "wegvalt, een uitzending die twee keer aankomt en een spookbeeld achterlaat, "
        "slow-scan-televisie, teletekst, een faxlijn, een beeld dat zo vaak opnieuw gepost is tot "
        "het versleten is, een webcam, een handheld spelcomputer, een magneet tegen een beeldbuis, "
        "en band die door de recorder is opgevreten.",
        "Novos na 2.0, e cada um mais uma máquina por onde falhar: um sinal de satélite caindo, "
        "uma transmissão que chega duas vezes e deixa uma sombra, televisão de varredura lenta, "
        "teletexto, uma linha de fax, uma imagem repostada até se gastar, uma webcam, um videogame "
        "portátil, um ímã encostado num tubo e uma fita enroscada pelo aparelho.",
        "2.0 新增，每一种都是又一台可以出故障的机器：失锁的卫星信号、到达两次而留下鬼影的广播、"
        "慢扫描电视、图文电视、一条传真线路、被反复转发直到包浆的图片、摄像头、掌机、"
        "贴在显像管上的磁铁，以及被录像机绞坏的磁带。"),
    "Free · 19 classics": (
        "Kostenlos · 19 Klassiker", "Gratis · 19 clásicos", "Gratis · 19 clásicos",
        "Gratuit · 19 classiques", "Gratis · 19 classici", "無料 · 定番の 19 種類",
        "무료 · 기본 19가지", "Gratis · 19 klassiekers", "Grátis · 19 clássicos",
        "免费 · 19 种经典效果"),
    "Premium · 10 new in 2.0": (
        "Premium · 10 neue in 2.0", "Premium · 10 nuevos en la 2.0", "Premium · 10 nuevos en la 2.0",
        "Premium · 10 nouveaux dans la 2.0", "Premium · 10 nuovi nella 2.0",
        "Premium · 2.0 で新しい 10 種類", "Premium · 2.0의 새 효과 10가지",
        "Premium · 10 nieuw in 2.0", "Premium · 10 novos na 2.0", "Premium · 2.0 新增 10 种"),
    "Rebuilt for 2.0. Everything renders on the GPU.": (
        "Neu gebaut für 2.0. Alles wird auf der GPU gerechnet.",
        "Rehecha para la 2.0. Todo se procesa en la GPU.",
        "Rehecha para la 2.0. Todo se procesa en la GPU.",
        "Reconstruite pour la 2.0. Tout est calculé sur le GPU.",
        "Rifatta per la 2.0. Tutto viene elaborato sulla GPU.",
        "2.0 で作り直しました。描画はすべて GPU で。",
        "2.0에서 새로 만들었습니다. 모든 렌더링은 GPU에서.",
        "Opnieuw gebouwd voor 2.0. Alles wordt op de GPU gerenderd.",
        "Refeito para a 2.0. Tudo é renderizado na GPU.",
        "为 2.0 重做。所有渲染都在 GPU 上完成。"),
    "The preview is sharp and it updates while you drag, and a 4K still takes a moment instead of "
    "half a minute. The layer stack shows exactly what is running and in what order, and every "
    "setting has its own level meter. Nothing is a single slider.": (
        "Die Vorschau ist scharf und aktualisiert sich, während du ziehst, und ein 4K-Foto braucht "
        "einen Moment statt einer halben Minute. Der Ebenenstapel zeigt genau, was läuft und in "
        "welcher Reihenfolge, und jeder Regler hat seine eigene Pegelanzeige. Nichts ist nur ein "
        "einzelner Schieberegler.",
        "La vista previa es nítida y se actualiza mientras arrastras, y una foto en 4K tarda un "
        "momento en lugar de medio minuto. La pila de capas muestra exactamente qué se está "
        "ejecutando y en qué orden, y cada control tiene su propio medidor de nivel. Nada se "
        "reduce a un solo control.",
        "La vista previa es nítida y se actualiza mientras arrastras, y una foto en 4K tarda un "
        "momento en vez de medio minuto. La pila de capas muestra exactamente qué se está "
        "ejecutando y en qué orden, y cada control tiene su propio medidor de nivel. Nada se "
        "reduce a un solo control.",
        "L'aperçu est net et se met à jour pendant que vous faites glisser, et une photo en 4K "
        "prend un instant au lieu d'une demi-minute. La pile de calques montre exactement ce qui "
        "tourne et dans quel ordre, et chaque réglage a son propre vumètre. Rien ne se résume à un "
        "curseur unique.",
        "L'anteprima è nitida e si aggiorna mentre trascini, e una foto in 4K richiede un attimo "
        "invece di mezzo minuto. La pila dei livelli mostra esattamente cosa sta girando e in che "
        "ordine, e ogni controllo ha il suo indicatore di livello. Niente si riduce a un solo "
        "cursore.",
        "プレビューはシャープで、ドラッグしているあいだにも更新され、4K の静止画も 30 秒ではなく"
        "一瞬で仕上がります。レイヤーの重なりには、何がどの順番で動いているかがそのまま表示され、"
        "パラメータごとにレベルメーターが付いています。スライダー 1 本で終わるものはありません。",
        "미리보기는 선명하고 끄는 동안에도 갱신되며, 4K 사진도 30초가 아니라 금방 끝납니다. "
        "레이어 스택은 무엇이 어떤 순서로 돌고 있는지 정확히 보여 주고, 설정마다 레벨 미터가 "
        "따로 있습니다. 슬라이더 하나로 끝나는 것은 없습니다.",
        "De preview is scherp en werkt bij terwijl je sleept, en een 4K-foto kost een moment in "
        "plaats van een halve minuut. De lagenstapel laat precies zien wat er draait en in welke "
        "volgorde, en elke regelaar heeft zijn eigen niveaumeter. Niets is maar één schuifje.",
        "A prévia é nítida e se atualiza enquanto você arrasta, e uma foto em 4K leva um instante "
        "em vez de meio minuto. A pilha de camadas mostra exatamente o que está rodando e em que "
        "ordem, e cada controle tem seu próprio medidor de nível. Nada se resume a um controle só.",
        "预览清晰，拖动时就会随之更新，一张 4K 静态图以前要半分钟，现在转眼就好。图层栈清楚显示"
        "正在运行什么、按什么顺序，每个参数都有自己的电平表。没有什么是一根滑杆了事的。"),
    "Open a photo, or a video clip, from your library.": (
        "Öffne ein Foto oder einen Videoclip aus deiner Mediathek.",
        "Abre una foto, o un clip de vídeo, de tu fototeca.",
        "Abre una foto, o un clip de video, de tu fototeca.",
        "Ouvrez une photo, ou un clip vidéo, depuis votre photothèque.",
        "Apri una foto, o una clip video, dalla tua libreria.",
        "ライブラリから写真を、あるいは動画のクリップを開きます。",
        "보관함에서 사진이나 동영상 클립을 엽니다.",
        "Open een foto, of een videoclip, uit je bibliotheek.",
        "Abra uma foto, ou um clipe de vídeo, da sua biblioteca.",
        "从图库里打开一张照片，或一段视频。"),
    "Start from a preset. Nine are built in, and Premium adds two packs, Dead Air and Y2K.": (
        "Fang mit einem Preset an. Neun sind eingebaut, und Premium bringt zwei Pakete dazu, "
        "Sendepause und Y2K.",
        "Empieza por un preajuste. Nueve vienen incluidos, y Premium añade dos paquetes, Fin de "
        "emisión e Y2K.",
        "Empieza con un preajuste. Nueve vienen incluidos, y Premium agrega dos paquetes, Fuera "
        "del aire y Y2K.",
        "Partez d'un préréglage. Neuf sont intégrés, et Premium ajoute deux packs, Blanc "
        "d'antenne et Y2K.",
        "Parti da un preset. Nove sono inclusi, e Premium aggiunge due pack, Fuori onda e Y2K.",
        "プリセットから始めます。9 種類を収録し、Premium ではプリセットパック「放送事故」と"
        "「Y2K」が加わります。",
        "프리셋에서 시작합니다. 기본 9종이 들어 있고, Premium에는 방송 사고와 Y2K, 두 가지 팩이 "
        "더해집니다.",
        "Begin bij een preset. Negen zitten erin, en Premium voegt twee pakketten toe, Storing en "
        "Y2K.",
        "Comece por um preset. Nove vêm prontos, e o Premium acrescenta dois pacotes, Fora do ar e "
        "Y2K.",
        "从一个预设开始。内置九个，Premium 再加两套合集：“停播”和“千禧”。"),
    "Open any effect and move its settings. Any of them can drift, step or sweep on its own.": (
        "Öffne einen beliebigen Effekt und bewege seine Regler. Jeder davon kann von selbst "
        "driften, springen oder schwingen.",
        "Abre cualquier efecto y mueve sus controles. Cualquiera de ellos puede derivar, saltar o "
        "barrer por sí solo.",
        "Abre cualquier efecto y mueve sus controles. Cualquiera de ellos puede derivar, saltar o "
        "barrer por sí solo.",
        "Ouvrez n'importe quel effet et déplacez ses réglages. Chacun peut dériver, sauter ou "
        "balayer tout seul.",
        "Apri qualsiasi effetto e muovi i suoi controlli. Ognuno può oscillare, andare a scatti o "
        "spazzare da solo.",
        "どのエフェクトでも開いて、パラメータを動かします。どれも、ゆらぎ、ステップ、スイープで"
        "ひとりでに動かせます。",
        "어떤 효과든 열어 설정을 움직입니다. 어느 설정이든 스스로 흔들리고, 계단처럼 바뀌고, "
        "쓸고 지나가게 할 수 있습니다.",
        "Open een willekeurig effect en verschuif zijn regelaars. Elk ervan kan vanzelf zweven, "
        "verspringen of zwaaien.",
        "Abra qualquer efeito e mexa nos controles. Qualquer um deles pode oscilar, pular ou "
        "varrer sozinho.",
        "打开任意一个效果，调它的参数。每个参数都能自己漂移、跳变或扫动。"),
    "Put the layers in a different order and watch the picture change.": (
        "Bring die Ebenen in eine andere Reihenfolge und sieh zu, wie sich das Bild ändert.",
        "Cambia el orden de las capas y mira cómo cambia la imagen.",
        "Cambia el orden de las capas y mira cómo cambia la imagen.",
        "Changez l'ordre des calques et regardez l'image changer.",
        "Cambia l'ordine dei livelli e guarda l'immagine cambiare.",
        "レイヤーの順番を入れ替えて、絵が変わるのを見ます。",
        "레이어의 순서를 바꾸고 그림이 달라지는 것을 봅니다.",
        "Zet de lagen in een andere volgorde en zie het beeld veranderen.",
        "Mude a ordem das camadas e veja a imagem mudar.",
        "把图层换个顺序，看着画面跟着变。"),
    "Burn in a camcorder, digicam, VCR or CCTV date, or mask the subject so it stays clean while "
    "the background breaks, or the other way round.": (
        "Brenn ein Datum ein wie ein Camcorder, eine Digicam, ein Videorekorder oder eine "
        "Überwachungskamera, oder maskiere das Motiv, damit es sauber bleibt, während der "
        "Hintergrund zerbricht, oder umgekehrt.",
        "Graba la fecha como una videocámara, una cámara digital, un vídeo doméstico o una cámara "
        "de vigilancia, o enmascara al sujeto para que quede limpio mientras el fondo se rompe, o "
        "al revés.",
        "Graba la fecha como una videocámara, una cámara digital, una videocasetera o una cámara "
        "de seguridad, o enmascara al sujeto para que quede limpio mientras el fondo se rompe, o "
        "al revés.",
        "Incrustez une date façon caméscope, appareil numérique, magnétoscope ou caméra de "
        "surveillance, ou masquez le sujet pour qu'il reste net pendant que l'arrière-plan se "
        "casse, ou l'inverse.",
        "Imprimi una data da videocamera, fotocamera digitale, videoregistratore o telecamera di "
        "sorveglianza, oppure maschera il soggetto perché resti pulito mentre lo sfondo si rompe, "
        "o il contrario.",
        "ビデオカメラ、デジカメ、ビデオデッキ、防犯カメラ風の日付を焼き込んだり、被写体に"
        "マスクをかけて、背景だけを壊して被写体はきれいなまま残したり、その逆にしたりします。",
        "캠코더, 디카, VCR, CCTV 스타일의 날짜를 새겨 넣거나, 피사체를 마스킹해 배경만 망가지는 "
        "동안 피사체는 깨끗하게 두거나, 그 반대로 합니다.",
        "Brand een datum in zoals een camcorder, digitale camera, videorecorder of "
        "beveiligingscamera, of maskeer het onderwerp zodat het schoon blijft terwijl de "
        "achtergrond breekt, of andersom.",
        "Grave a data como uma filmadora, uma câmera digital, um videocassete ou uma câmera de "
        "segurança, ou mascare o assunto para ele ficar limpo enquanto o fundo quebra, ou o "
        "contrário.",
        "烙上摄像机、数码相机、录像机或监控摄像头风格的日期，或者给主体加上蒙版，让背景碎掉而"
        "主体保持干净，也可以反过来。"),
    "Save to your camera roll, or save the whole stack to use again.": (
        "Sichere in deine Aufnahmen, oder sichere den ganzen Stapel, um ihn wieder zu verwenden.",
        "Guarda en tu carrete, o guarda la pila entera para volver a usarla.",
        "Guarda en tu carrete, o guarda la pila entera para volver a usarla.",
        "Enregistrez dans votre pellicule, ou enregistrez toute la pile pour la réutiliser.",
        "Salva nel rullino, oppure salva l'intera pila per riusarla.",
        "カメラロールに保存するか、重ねた組み合わせをまるごと保存して、また使います。",
        "카메라 롤에 저장하거나, 쌓은 조합을 통째로 저장해 다시 씁니다.",
        "Bewaar in je filmrol, of bewaar de hele stapel om opnieuw te gebruiken.",
        "Salve no rolo da câmera, ou salve a pilha inteira para usar de novo.",
        "存进相机胶卷，或者把整组叠加保存下来，下次再用。"),
    "Everything is processed on the device. There is no upload, no render queue and no server "
    "holding a copy of anything you shot. The app is about four megabytes.": (
        "Alles wird auf dem Gerät verarbeitet. Es gibt keinen Upload, keine Renderwarteschlange "
        "und keinen Server, der eine Kopie von irgendetwas hält, das du aufgenommen hast. Die App "
        "ist etwa vier Megabyte groß.",
        "Todo se procesa en el dispositivo. No hay subida, ni cola de render, ni servidor "
        "guardando una copia de nada de lo que has fotografiado. La app ocupa unos cuatro megas.",
        "Todo se procesa en el dispositivo. No hay subida, ni cola de render, ni servidor "
        "guardando una copia de nada de lo que fotografiaste. La app pesa unos cuatro megas.",
        "Tout est traité sur l'appareil. Il n'y a pas d'envoi, pas de file de rendu et pas de "
        "serveur qui garde une copie de quoi que ce soit que vous avez photographié. L'app fait "
        "environ quatre mégaoctets.",
        "Tutto viene elaborato sul dispositivo. Non c'è upload, non c'è coda di rendering e non "
        "c'è server che tenga una copia di niente di quello che hai scattato. L'app pesa circa "
        "quattro megabyte.",
        "処理はすべて端末の上で行われます。アップロードも、レンダリング待ちの列も、あなたが"
        "撮ったものの複製を持つサーバーもありません。アプリの大きさは約 4 MB です。",
        "모든 처리는 기기 안에서 이루어집니다. 업로드도, 렌더 대기열도, 당신이 찍은 것의 사본을 "
        "가진 서버도 없습니다. 앱 크기는 약 4MB입니다.",
        "Alles wordt op het toestel verwerkt. Er is geen upload, geen renderwachtrij en geen "
        "server met een kopie van wat je ook hebt geschoten. De app is ongeveer vier megabyte.",
        "Tudo é processado no aparelho. Não há envio, não há fila de renderização e não há "
        "servidor guardando cópia de nada que você fotografou. O app tem cerca de quatro "
        "megabytes.",
        "一切都在设备上处理。没有上传，没有渲染队列，也没有服务器存着你拍下的任何东西的副本。"
        "这个应用大约只有 4 MB。"),
    "It is also why the settings feel live: you are dragging the real image on your own phone's "
    "GPU rather than waiting on a round trip to somebody else's. And there are no ads, in the "
    "free version or in Premium.": (
        "Darum fühlen sich die Regler auch so unmittelbar an: Du ziehst am echten Bild, auf der "
        "GPU deines eigenen Telefons, statt auf den Umweg über die von jemand anderem zu warten. "
        "Und Werbung gibt es keine, weder in der kostenlosen Fassung noch in Premium.",
        "Por eso también los controles se sienten en vivo: arrastras la imagen real en la GPU de "
        "tu propio móvil en lugar de esperar un viaje de ida y vuelta a la de otro. Y no hay "
        "anuncios, ni en la versión gratuita ni en Premium.",
        "Por eso también los controles se sienten en vivo: arrastras la imagen real en la GPU de "
        "tu propio celular en vez de esperar un viaje de ida y vuelta a la de otro. Y no hay "
        "anuncios, ni en la versión gratuita ni en Premium.",
        "C'est aussi pour cela que les réglages réagissent en direct : vous faites glisser la "
        "vraie image sur le GPU de votre propre téléphone, au lieu d'attendre un aller-retour vers "
        "celui de quelqu'un d'autre. Et il n'y a pas de publicité, ni dans la version gratuite ni "
        "dans Premium.",
        "È anche per questo che i controlli sembrano dal vivo: trascini l'immagine vera sulla GPU "
        "del tuo telefono invece di aspettare un viaggio di andata e ritorno verso quella di "
        "qualcun altro. E non c'è pubblicità, né nella versione gratuita né in Premium.",
        "パラメータの反応がライブに感じられるのも、そのためです。ほかの誰かの GPU との往復を"
        "待つのではなく、あなた自身の端末の GPU の上で本物の画像を動かしているからです。"
        "そして広告は、無料版にも Premium にもありません。",
        "설정이 실시간으로 느껴지는 것도 그래서입니다. 다른 누군가의 GPU를 오가는 왕복을 기다리는 "
        "대신, 당신의 휴대폰 GPU 위에서 진짜 이미지를 움직이고 있으니까요. 그리고 광고는 무료 "
        "버전에도 Premium에도 없습니다.",
        "Daarom voelen de regelaars ook zo direct aan: je sleept aan het echte beeld op de GPU van "
        "je eigen telefoon, in plaats van te wachten op een retourtje naar die van iemand anders. "
        "En er zijn geen advertenties, niet in de gratis versie en niet in Premium.",
        "É também por isso que os controles parecem ao vivo: você está arrastando a imagem de "
        "verdade na GPU do seu próprio telefone em vez de esperar uma ida e volta até a de outra "
        "pessoa. E não há anúncios, nem na versão gratuita nem no Premium.",
        "这也是参数调起来如此跟手的原因：你是在自己手机的 GPU 上拖动真实的图像，而不是等着去"
        "别人的 GPU 那里走一个来回。而且没有广告，免费版没有，Premium 也没有。"),
    "Clips and loops, not just stills.": (
        "Clips und Loops, nicht nur Standbilder.", "Clips y bucles, no solo fotos fijas.",
        "Clips y bucles, no solo fotos fijas.",
        "Des clips et des boucles, pas seulement des images fixes.", "Clip e loop, non solo foto.",
        "静止画だけでなく、クリップもループも。", "정지 사진만이 아니라 클립과 루프도.",
        "Clips en loops, niet alleen stilstaande beelden.", "Clipes e loops, não só fotos paradas.",
        "不只是静态图，还有视频和循环动画。"),
    "Open a video clip and watch it play through your effects, then trim up to a minute and save "
    "it at 1080p or 4K with its sound. Or turn a still into a three-second loop. Any setting can "
    "drift, step or sweep on its own, and loops and videos carry the movement: the tracking "
    "drifts, the channels breathe. Video and loops come with Premium.": (
        "Öffne einen Videoclip und sieh zu, wie er durch deine Effekte läuft, dann kürze ihn auf "
        "bis zu eine Minute und sichere ihn in 1080p oder 4K, mit Ton. Oder mach aus einem "
        "Standbild einen Loop von drei Sekunden. Jeder Regler kann von selbst driften, springen "
        "oder schwingen, und Loops und Videos nehmen die Bewegung mit: Die Spur driftet, die "
        "Kanäle atmen. Video und Loops gibt es mit Premium.",
        "Abre un clip de vídeo y míralo reproducirse a través de tus efectos, luego recórtalo "
        "hasta un minuto y guárdalo en 1080p o 4K, con su sonido. O convierte una foto fija en un "
        "bucle de tres segundos. Cualquier control puede derivar, saltar o barrer por sí solo, y "
        "los bucles y los vídeos conservan el movimiento: el tracking deriva, los canales "
        "respiran. El vídeo y los bucles vienen con Premium.",
        "Abre un clip de video y míralo reproducirse a través de tus efectos, luego recórtalo "
        "hasta un minuto y guárdalo en 1080p o 4K, con su sonido. O convierte una foto fija en un "
        "bucle de tres segundos. Cualquier control puede derivar, saltar o barrer por sí solo, y "
        "los bucles y los videos conservan el movimiento: el tracking deriva, los canales "
        "respiran. El video y los bucles vienen con Premium.",
        "Ouvrez un clip vidéo et regardez-le passer à travers vos effets, puis coupez jusqu'à une "
        "minute et enregistrez en 1080p ou en 4K, avec le son. Ou transformez une image fixe en "
        "boucle de trois secondes. N'importe quel réglage peut dériver, sauter ou balayer tout "
        "seul, et les boucles comme les vidéos gardent le mouvement : la piste dérive, les canaux "
        "respirent. La vidéo et les boucles viennent avec Premium.",
        "Apri una clip video e guardala scorrere attraverso i tuoi effetti, poi tagliala fino a un "
        "minuto e salvala in 1080p o 4K, con il suo audio. Oppure trasforma una foto in un loop di "
        "tre secondi. Qualsiasi controllo può oscillare, andare a scatti o spazzare da solo, e "
        "loop e video si portano dietro il movimento: il tracking deriva, i canali respirano. "
        "Video e loop arrivano con Premium.",
        "動画のクリップを開くと、エフェクトを通した映像がそのまま再生されます。最大 1 分まで"
        "トリミングして、音声付きのまま 1080p か 4K で保存できます。あるいは静止画を 3 秒の"
        "ループにすることも。どのパラメータもゆらぎ、ステップ、スイープでひとりでに動かせて、"
        "ループにも動画にもその動きが残ります。トラッキングは漂い、チャンネルは呼吸します。"
        "動画とループは Premium の機能です。",
        "동영상 클립을 열면 효과를 거친 영상이 그대로 재생되고, 최대 1분까지 잘라 소리와 함께 "
        "1080p 또는 4K로 저장할 수 있습니다. 또는 정지 사진을 3초 루프로 만들 수도 있습니다. "
        "어떤 설정이든 스스로 흔들리고, 계단처럼 바뀌고, 쓸고 지나가게 할 수 있으며, 루프와 "
        "동영상에는 그 움직임이 그대로 담깁니다. 트래킹은 흘러가고, 채널은 숨을 쉽니다. "
        "동영상과 루프는 Premium 기능입니다.",
        "Open een videoclip en zie hem door je effecten spelen, knip hem dan tot een minuut en "
        "bewaar hem in 1080p of 4K, met geluid. Of maak van een stilstaand beeld een loop van drie "
        "seconden. Elke regelaar kan vanzelf zweven, verspringen of zwaaien, en loops en video's "
        "nemen die beweging mee: de tracking drijft, de kanalen ademen. Video en loops komen met "
        "Premium.",
        "Abra um clipe de vídeo e veja ele rodar através dos seus efeitos, depois corte até um "
        "minuto e salve em 1080p ou 4K, com o som. Ou transforme uma foto parada num loop de três "
        "segundos. Qualquer controle pode oscilar, pular ou varrer sozinho, e os loops e vídeos "
        "levam o movimento junto: o tracking deriva, os canais respiram. Vídeo e loops vêm com o "
        "Premium.",
        "打开一段视频，看着它穿过你的效果播放，然后剪到一分钟以内，连同声音以 1080p 或 4K "
        "保存。也可以把一张静态图做成三秒循环动画。任何参数都能自己漂移、跳变或扫动，"
        "循环动画和视频都会带上这种变化：循迹在漂，通道在呼吸。视频和循环动画随 Premium 提供。"),
    "The nineteen classic effects, the layers and the built-in presets work without a "
    "subscription, and there are no ads. Premium adds everything new in 2.0 and bigger exports. "
    "You can try any Premium feature on your own photo first: only saving asks.": (
        "Die neunzehn klassischen Effekte, die Ebenen und die eingebauten Presets funktionieren "
        "ohne Abo, und es gibt keine Werbung. Premium bringt alles Neue aus 2.0 und größere "
        "Exporte. Du kannst jede Premium-Funktion vorher an deinem eigenen Foto ausprobieren: Erst "
        "beim Sichern wird gefragt.",
        "Los diecinueve efectos clásicos, las capas y los preajustes incluidos funcionan sin "
        "suscripción, y no hay anuncios. Premium añade todo lo nuevo de la 2.0 y exportaciones más "
        "grandes. Puedes probar cualquier función Premium primero en tu propia foto: solo al "
        "guardar se te pregunta.",
        "Los diecinueve efectos clásicos, las capas y los preajustes incluidos funcionan sin "
        "suscripción, y no hay anuncios. Premium agrega todo lo nuevo de la 2.0 y exportaciones "
        "más grandes. Puedes probar cualquier función Premium primero en tu propia foto: solo al "
        "guardar se te pregunta.",
        "Les dix-neuf effets classiques, les calques et les préréglages intégrés fonctionnent sans "
        "abonnement, et il n'y a pas de publicité. Premium ajoute tout ce qui est nouveau dans la "
        "2.0 et des exports plus grands. Vous pouvez essayer n'importe quelle fonction Premium sur "
        "votre propre photo d'abord : seul l'enregistrement la demande.",
        "I diciannove effetti classici, i livelli e i preset inclusi funzionano senza abbonamento, "
        "e non c'è pubblicità. Premium aggiunge tutto ciò che è nuovo nella 2.0 ed esportazioni "
        "più grandi. Puoi provare qualsiasi funzione Premium prima sulla tua foto: solo il "
        "salvataggio te lo chiede.",
        "定番の十九のエフェクト、レイヤー、収録のプリセットはサブスクリプションなしで使え、"
        "広告もありません。Premium では 2.0 の新機能すべてと、より大きな書き出しが加わります。"
        "Premium の機能はどれも、まず自分の写真で試せます。確認が入るのは保存するときだけです。",
        "기본 효과 열아홉 가지, 레이어, 기본 프리셋은 구독 없이 쓸 수 있고, 광고도 없습니다. "
        "Premium은 2.0의 새로운 것 전부와 더 큰 내보내기를 더합니다. Premium 기능은 모두 내 "
        "사진으로 먼저 써 볼 수 있고, 저장할 때만 묻습니다.",
        "De negentien klassieke effecten, de lagen en de ingebouwde presets werken zonder "
        "abonnement, en er zijn geen advertenties. Premium voegt alles toe wat nieuw is in 2.0, "
        "en grotere exports. Je kunt elke Premium-functie eerst op je eigen foto proberen: alleen "
        "bewaren vraagt erom.",
        "Os dezenove efeitos clássicos, as camadas e os presets prontos funcionam sem assinatura, "
        "e não há anúncios. O Premium acrescenta tudo o que é novo na 2.0 e exportações maiores. "
        "Você pode experimentar qualquer recurso Premium antes na sua própria foto: só na hora de "
        "salvar ele pergunta.",
        "十九种经典效果、图层和内置预设无需订阅即可使用，也没有广告。Premium 增加 2.0 的全部"
        "新功能和更大的导出尺寸。任何 Premium 功能都能先在自己的照片上试用，只有保存时才会询问。"),
    "19 classic effects, layers, the built-in presets, saves at 1024 pixels, no ads": (
        "19 klassische Effekte, Ebenen, die eingebauten Presets, Sichern in 1024 Pixeln, keine "
        "Werbung",
        "19 efectos clásicos, capas, los preajustes incluidos, guardado a 1024 píxeles, sin "
        "anuncios",
        "19 efectos clásicos, capas, los preajustes incluidos, guardado a 1024 píxeles, sin "
        "anuncios",
        "19 effets classiques, calques, préréglages intégrés, enregistrement en 1024 pixels, "
        "aucune publicité",
        "19 effetti classici, livelli, i preset inclusi, salvataggio a 1024 pixel, nessuna "
        "pubblicità",
        "定番の 19 のエフェクト、レイヤー、収録のプリセット、1024 ピクセルでの保存、広告なし",
        "기본 효과 19가지, 레이어, 기본 프리셋, 1024픽셀 저장, 광고 없음",
        "19 klassieke effecten, lagen, de ingebouwde presets, bewaren in 1024 pixels, geen "
        "advertenties",
        "19 efeitos clássicos, camadas, os presets prontos, salvamento em 1024 pixels, sem "
        "anúncios",
        "19 种经典效果、图层、内置预设，以 1024 像素保存，无广告"),
    "Video, the ten new effects, settings that move, date stamps, masks, the Dead Air and Y2K "
    "preset packs, exports at 2048 pixels and 4K, three-second loops": (
        "Video, die zehn neuen Effekte, Regler, die sich von selbst bewegen, Datumsstempel, "
        "Masken, die Preset-Pakete Sendepause und Y2K, Export in 2048 Pixeln und 4K, Loops von "
        "drei Sekunden",
        "Vídeo, los diez efectos nuevos, controles que se mueven solos, marcas de fecha, "
        "máscaras, los paquetes de preajustes Fin de emisión e Y2K, exportación a 2048 píxeles y "
        "4K, bucles de tres segundos",
        "Video, los diez efectos nuevos, controles que se mueven solos, marcas de fecha, "
        "máscaras, los paquetes de preajustes Fuera del aire y Y2K, exportación a 2048 píxeles y "
        "4K, bucles de tres segundos",
        "La vidéo, les dix nouveaux effets, des réglages qui bougent tout seuls, les dates "
        "incrustées, les masques, les packs de préréglages Blanc d'antenne et Y2K, l'export en "
        "2048 pixels et en 4K, les boucles de trois secondes",
        "Video, i dieci nuovi effetti, controlli che si muovono da soli, date impresse, maschere, "
        "i pack di preset Fuori onda e Y2K, esportazione a 2048 pixel e 4K, loop di tre secondi",
        "動画、新しい 10 のエフェクト、ひとりでに動くパラメータ、日付スタンプ、マスク、"
        "プリセットパック「放送事故」と「Y2K」、2048 ピクセルと 4K での書き出し、3 秒のループ",
        "동영상, 새 효과 10가지, 스스로 움직이는 설정, 날짜 스탬프, 마스킹, 방송 사고와 Y2K 프리셋 "
        "팩, 2048픽셀과 4K 내보내기, 3초 루프",
        "Video, de tien nieuwe effecten, regelaars die vanzelf bewegen, datumstempels, maskers, "
        "de presetpakketten Storing en Y2K, export in 2048 pixels en 4K, loops van drie seconden",
        "Vídeo, os dez efeitos novos, controles que se mexem sozinhos, carimbos de data, "
        "máscaras, os pacotes de presets Fora do ar e Y2K, exportação em 2048 pixels e 4K, loops "
        "de três segundos",
        "视频、十种新效果、会自己动的参数、日期水印、蒙版、“停播”和“千禧”预设合集、2048 像素"
        "与 4K 导出、三秒循环动画"),
    "Plans": ("Abos", "Planes", "Planes", "Formules", "Piani", "プラン", "플랜", "Abonnement",
              "Planos", "方案"),
    "Monthly or yearly. The yearly plan starts with a 7-day free trial, and the app shows prices "
    "in your own currency.": (
        "Monatlich oder jährlich. Das Jahresabo beginnt mit einer 7-tägigen Gratis-Testphase, und "
        "die App zeigt die Preise in deiner Währung.",
        "Mensual o anual. El plan anual empieza con una prueba gratuita de 7 días, y la app "
        "muestra los precios en tu propia moneda.",
        "Mensual o anual. El plan anual empieza con una prueba gratis de 7 días, y la app muestra "
        "los precios en tu propia moneda.",
        "Au mois ou à l'année. La formule annuelle commence par un essai gratuit de 7 jours, et "
        "l'app affiche les prix dans votre devise.",
        "Mensile o annuale. Il piano annuale inizia con una prova gratuita di 7 giorni, e l'app "
        "mostra i prezzi nella tua valuta.",
        "月額と年額があり、年額プランは 7 日間の無料体験から始まります。価格はお住まいの国の"
        "通貨でアプリ内に表示されます。",
        "월간 또는 연간. 연간 플랜은 7일 무료 체험으로 시작하며, 가격은 앱에서 현지 통화로 "
        "표시됩니다.",
        "Per maand of per jaar. Het jaarabonnement begint met een gratis proefperiode van 7 dagen, "
        "en de app toont de prijzen in je eigen valuta.",
        "Mensal ou anual. O plano anual começa com um teste grátis de 7 dias, e o app mostra os "
        "preços na sua moeda.",
        "按月或按年。年付方案先享 7 天免费试用，应用内会以你所在地区的货币显示价格。"),

    # ---- FAQ answers (the schema carries the same text, and merge.py matches both)
    "Yes. The 19 classic effects, layers and the built-in presets work without a subscription and "
    "save at 1024 pixels, and there are no ads. Premium adds video, the ten new effects, settings "
    "that move, date stamps, masks and two preset packs, plus exports at 2048 pixels and 4K and "
    "three-second loops. It is monthly or yearly, and the yearly plan starts with a 7-day free "
    "trial.": (
        "Ja. Die 19 klassischen Effekte, Ebenen und die eingebauten Presets funktionieren ohne Abo "
        "und sichern in 1024 Pixeln, und es gibt keine Werbung. Premium bringt Video, die zehn "
        "neuen Effekte, Regler, die sich von selbst bewegen, Datumsstempel, Masken und zwei "
        "Preset-Pakete, dazu Export in 2048 Pixeln und 4K und Loops von drei Sekunden. Es läuft "
        "monatlich oder jährlich, und das Jahresabo beginnt mit einer 7-tägigen Gratis-Testphase.",
        "Sí. Los 19 efectos clásicos, las capas y los preajustes incluidos funcionan sin "
        "suscripción y guardan a 1024 píxeles, y no hay anuncios. Premium añade vídeo, los diez "
        "efectos nuevos, controles que se mueven solos, marcas de fecha, máscaras y dos paquetes "
        "de preajustes, además de exportación a 2048 píxeles y 4K y bucles de tres segundos. Es "
        "mensual o anual, y el plan anual empieza con una prueba gratuita de 7 días.",
        "Sí. Los 19 efectos clásicos, las capas y los preajustes incluidos funcionan sin "
        "suscripción y guardan a 1024 píxeles, y no hay anuncios. Premium agrega video, los diez "
        "efectos nuevos, controles que se mueven solos, marcas de fecha, máscaras y dos paquetes "
        "de preajustes, además de exportación a 2048 píxeles y 4K y bucles de tres segundos. Es "
        "mensual o anual, y el plan anual empieza con una prueba gratis de 7 días.",
        "Oui. Les 19 effets classiques, les calques et les préréglages intégrés fonctionnent sans "
        "abonnement et s'enregistrent en 1024 pixels, et il n'y a pas de publicité. Premium "
        "ajoute la vidéo, les dix nouveaux effets, des réglages qui bougent tout seuls, les dates "
        "incrustées, les masques et deux packs de préréglages, plus l'export en 2048 pixels et en "
        "4K et les boucles de trois secondes. C'est au mois ou à l'année, et la formule annuelle "
        "commence par un essai gratuit de 7 jours.",
        "Sì. I 19 effetti classici, i livelli e i preset inclusi funzionano senza abbonamento e "
        "salvano a 1024 pixel, e non c'è pubblicità. Premium aggiunge video, i dieci nuovi "
        "effetti, controlli che si muovono da soli, date impresse, maschere e due pack di preset, "
        "più esportazione a 2048 pixel e 4K e loop di tre secondi. È mensile o annuale, e il "
        "piano annuale inizia con una prova gratuita di 7 giorni.",
        "はい。定番の 19 のエフェクト、レイヤー、収録のプリセットはサブスクリプションなしで使え、"
        "1024 ピクセルで保存でき、広告もありません。Premium では動画、新しい 10 のエフェクト、"
        "ひとりでに動くパラメータ、日付スタンプ、マスク、2 つのプリセットパックに加え、"
        "2048 ピクセルと 4K での書き出しと 3 秒のループが使えます。月額と年額があり、年額プランは "
        "7 日間の無料体験から始まります。",
        "네. 기본 효과 19가지, 레이어, 기본 프리셋은 구독 없이 쓸 수 있고 1024픽셀로 저장되며, "
        "광고도 없습니다. Premium은 동영상, 새 효과 10가지, 스스로 움직이는 설정, 날짜 스탬프, "
        "마스킹, 프리셋 팩 두 가지에 더해 2048픽셀과 4K 내보내기, 3초 루프를 제공합니다. 월간 "
        "또는 연간이며, 연간 플랜은 7일 무료 체험으로 시작합니다.",
        "Ja. De 19 klassieke effecten, lagen en de ingebouwde presets werken zonder abonnement en "
        "bewaren in 1024 pixels, en er zijn geen advertenties. Premium voegt video toe, de tien "
        "nieuwe effecten, regelaars die vanzelf bewegen, datumstempels, maskers en twee "
        "presetpakketten, plus export in 2048 pixels en 4K en loops van drie seconden. Het is per "
        "maand of per jaar, en het jaarabonnement begint met een gratis proefperiode van 7 dagen.",
        "Sim. Os 19 efeitos clássicos, as camadas e os presets prontos funcionam sem assinatura e "
        "salvam em 1024 pixels, e não há anúncios. O Premium acrescenta vídeo, os dez efeitos "
        "novos, controles que se mexem sozinhos, carimbos de data, máscaras e dois pacotes de "
        "presets, mais exportação em 2048 pixels e 4K e loops de três segundos. É mensal ou "
        "anual, e o plano anual começa com um teste grátis de 7 dias.",
        "是的。19 种经典效果、图层和内置预设无需订阅即可使用，以 1024 像素保存，也没有广告。"
        "Premium 增加视频、十种新效果、会自己动的参数、日期水印、蒙版和两套预设合集，另有 "
        "2048 像素与 4K 导出以及三秒循环动画。可按月或按年订阅，年付方案先享 7 天免费试用。"),
    "Twenty-nine. Nineteen classics are free: Noise, Pixel Shift, RGB Split, Scanlines, "
    "Distortion, Corruption, Feedback, VHS, CRT, Chroma, Film, Crush, Interlace, Invert, Datamosh, "
    "Dither, Static, Sort and Sync. Ten more come with Premium: Satellite, Ghosting, Slow Scan, "
    "Teletext, Fax, Repost, Webcam, Handheld, Magnet and Chewed. Stack them in any order.": (
        "Neunundzwanzig. Neunzehn Klassiker sind kostenlos: Rauschen, Versatz, RGB, Bildzeilen, "
        "Verzerrung, Defekt, Rückkopplung, VHS, CRT, Chroma, Film, Crush, Zeilen, Invertieren, "
        "Datamosh, Dither, Bildrauschen, Sortieren und Sync. Zehn weitere gibt es mit Premium: "
        "Satellit, Geisterbild, Slow Scan, Videotext, Fax, Repost, Webcam, Handheld, Magnet und "
        "Bandsalat. Staple sie in beliebiger Reihenfolge.",
        "Veintinueve. Diecinueve clásicos son gratis: Ruido, Corrimiento, RGB, Líneas, "
        "Distorsión, Corrupción, Realimentación, VHS, CRT, Croma, Película, Crush, Entrelazado, "
        "Invertir, Datamosh, Tramado, Nieve, Ordenar y Sincronía. Diez más vienen con Premium: "
        "Satélite, Doble imagen, Slow Scan, Teletexto, Fax, Resubida, Webcam, Portátil, Imán y "
        "Masticada. Apílalos en el orden que quieras.",
        "Veintinueve. Diecinueve clásicos son gratis: Ruido, Corrimiento, RGB, Líneas, "
        "Distorsión, Corrupción, Realimentación, VHS, CRT, Croma, Película, Crush, Entrelazado, "
        "Invertir, Datamosh, Tramado, Nieve, Ordenar y Sincronía. Diez más vienen con Premium: "
        "Satélite, Doble imagen, Slow Scan, Teletexto, Fax, Resubida, Webcam, Portátil, Imán y "
        "Masticada. Apílalos en el orden que quieras.",
        "Vingt-neuf. Dix-neuf classiques sont gratuits : Bruit, Décalage, RVB, Lignes, "
        "Distorsion, Corruption, Retour, VHS, CRT, Chroma, Pellicule, Crush, Entrelacé, "
        "Inversion, Datamosh, Tramage, Neige, Tri et Synchro. Dix de plus viennent avec Premium : "
        "Satellite, Dédoublement, Slow Scan, Télétexte, Fax, Repost, Webcam, Console, Aimant et "
        "Bande mangée. Empilez-les dans l'ordre que vous voulez.",
        "Ventinove. Diciannove classici sono gratis: Rumore, Sposta, RGB, Righe, Distorsione, "
        "Corruzione, Feedback, VHS, CRT, Croma, Pellicola, Crush, Interlaccio, Inverti, Datamosh, "
        "Dither, Neve, Ordina e Sync. Altri dieci arrivano con Premium: Satellite, Sdoppiamento, "
        "Slow Scan, Televideo, Fax, Repost, Webcam, Console, Calamita e Nastro mangiato. Impilali "
        "nell'ordine che vuoi.",
        "29 種類です。定番の 19 種類は無料です：ノイズ、シフト、RGB分離、走査線、歪み、破損、"
        "反復、VHS、CRT、色ずれ、フィルム、劣化、インタレース、色反転、モッシュ、ディザ、砂嵐、"
        "ソート、同期ずれ。Premium でさらに 10 種類：衛星放送、ゴースト障害、低速走査、文字放送、"
        "FAX、再投稿、Webカメラ、携帯ゲーム機、磁石、テープ噛み。好きな順番で重ねられます。",
        "스물아홉 가지입니다. 기본 19가지는 무료입니다: 노이즈, 픽셀 시프트, RGB 분리, 주사선, "
        "왜곡, 손상, 피드백, VHS, CRT, 색 어긋남, 필름, 열화, 인터레이스, 색 반전, 모시, 디더, "
        "지지직, 픽셀 정렬, 동기 오류. Premium으로 10가지 더: 위성 방송, 고스트 현상, 저속 주사, "
        "문자방송, 팩스, 재업로드, 웹캠, 휴대 게임기, 자석, 테이프 씹힘. 원하는 순서로 쌓을 수 "
        "있습니다.",
        "Negenentwintig. Negentien klassiekers zijn gratis: Ruis, Verschuif, RGB, Lijnen, "
        "Vervorming, Corruptie, Terugkoppeling, VHS, Beeldbuis, Chroma, Film, Crush, Interlace, "
        "Omkeren, Datamosh, Dither, Sneeuw, Sorteer en Sync. Nog tien komen met Premium: "
        "Satelliet, Spookbeeld, Slow Scan, Teletekst, Fax, Repost, Webcam, Handheld, Magneet en "
        "Bandsalade. Stapel ze in elke volgorde die je wilt.",
        "Vinte e nove. Dezenove clássicos são grátis: Ruído, Deslocar, RGB, Linhas, Distorção, "
        "Corrupção, Realimentação, VHS, CRT, Croma, Filme, Crush, Entrelaçamento, Inverter, "
        "Datamosh, Dither, Chuvisco, Ordenar e Sincronia. Mais dez vêm com o Premium: Satélite, "
        "Sombra, Slow Scan, Teletexto, Fax, Repost, Webcam, Portátil, Ímã e Enroscada. Empilhe na "
        "ordem que quiser.",
        "二十九种。十九种经典效果免费：噪点、像素偏移、RGB 分离、扫描线、畸变、数据损坏、反馈、"
        "VHS、显像管、色度偏移、胶片、位深压碎、隔行扫描、反色、数据莫氏、抖动、雪花、像素排序"
        "和信号同步。Premium 再加十种：卫星、鬼影、慢扫描、图文电视、传真、电子包浆、摄像头、"
        "掌机、磁化和绞带。可以按任意顺序叠加。"),
    "No. Everything is processed on your iPhone and nothing is uploaded. There is no render queue "
    "and no server holding your images, and there are no ads.": (
        "Nein. Alles wird auf deinem iPhone verarbeitet, und nichts wird hochgeladen. Es gibt "
        "keine Renderwarteschlange und keinen Server, der deine Bilder hält, und es gibt keine "
        "Werbung.",
        "No. Todo se procesa en tu iPhone y no se sube nada. No hay cola de render ni servidor "
        "guardando tus imágenes, y no hay anuncios.",
        "No. Todo se procesa en tu iPhone y no se sube nada. No hay cola de render ni servidor "
        "guardando tus imágenes, y no hay anuncios.",
        "Non. Tout est traité sur votre iPhone et rien n'est envoyé. Il n'y a pas de file de "
        "rendu ni de serveur qui garde vos images, et il n'y a pas de publicité.",
        "No. Tutto viene elaborato sul tuo iPhone e non viene caricato nulla. Non c'è coda di "
        "rendering né server che tenga le tue immagini, e non c'è pubblicità.",
        "いいえ。処理はすべてあなたの iPhone の中で行われ、何もアップロードされません。"
        "レンダリング待ちの列も、あなたの画像を持つサーバーもなく、広告もありません。",
        "아니요. 모든 처리는 당신의 iPhone 안에서 이루어지고, 아무것도 업로드되지 않습니다. 렌더 "
        "대기열도, 당신의 이미지를 가진 서버도 없으며, 광고도 없습니다.",
        "Nee. Alles wordt op je iPhone verwerkt en er wordt niets geüpload. Er is geen "
        "renderwachtrij en geen server met jouw beelden, en er zijn geen advertenties.",
        "Não. Tudo é processado no seu iPhone e nada é enviado. Não há fila de renderização nem "
        "servidor guardando suas imagens, e não há anúncios.",
        "不会。一切都在你的 iPhone 上处理，不会上传任何内容。没有渲染队列，也没有服务器存着你的"
        "图像，而且没有广告。"),
    "Yes. Open a clip, trim it to a minute or less and save it at 1080p or 4K with its sound. You "
    "can also turn a still into a three-second loop, with any setting drifting, stepping or "
    "sweeping across it. Video and loops come with Premium.": (
        "Ja. Öffne einen Clip, kürze ihn auf höchstens eine Minute und sichere ihn in 1080p oder "
        "4K, mit Ton. Du kannst auch aus einem Standbild einen Loop von drei Sekunden machen, in "
        "dem jeder Regler driftet, springt oder schwingt. Video und Loops gibt es mit Premium.",
        "Sí. Abre un clip, recórtalo a un minuto o menos y guárdalo en 1080p o 4K con su sonido. "
        "También puedes convertir una foto fija en un bucle de tres segundos, con cualquier "
        "control derivando, saltando o barriendo a lo largo de él. El vídeo y los bucles vienen "
        "con Premium.",
        "Sí. Abre un clip, recórtalo a un minuto o menos y guárdalo en 1080p o 4K con su sonido. "
        "También puedes convertir una foto fija en un bucle de tres segundos, con cualquier "
        "control derivando, saltando o barriendo a lo largo de él. El video y los bucles vienen "
        "con Premium.",
        "Oui. Ouvrez un clip, coupez-le à une minute ou moins et enregistrez-le en 1080p ou en 4K "
        "avec le son. Vous pouvez aussi transformer une image fixe en boucle de trois secondes, "
        "avec n'importe quel réglage qui dérive, saute ou balaie tout du long. La vidéo et les "
        "boucles viennent avec Premium.",
        "Sì. Apri una clip, tagliala a un minuto o meno e salvala in 1080p o 4K con il suo audio. "
        "Puoi anche trasformare una foto in un loop di tre secondi, con qualsiasi controllo che "
        "oscilla, va a scatti o spazza lungo tutto il loop. Video e loop arrivano con Premium.",
        "はい。クリップを開き、1 分以内にトリミングして、音声付きのまま 1080p か 4K で保存"
        "できます。静止画を 3 秒のループにして、どのパラメータもそのあいだゆらぎ、ステップ、"
        "スイープさせることもできます。動画とループは Premium の機能です。",
        "네. 클립을 열어 1분 이하로 자르고 소리와 함께 1080p 또는 4K로 저장할 수 있습니다. 정지 "
        "사진을 3초 루프로 만들어, 어떤 설정이든 그 동안 흔들리고, 계단처럼 바뀌고, 쓸고 "
        "지나가게 할 수도 있습니다. 동영상과 루프는 Premium 기능입니다.",
        "Ja. Open een clip, knip hem tot een minuut of korter en bewaar hem in 1080p of 4K met "
        "geluid. Je kunt ook van een stilstaand beeld een loop van drie seconden maken, waarin "
        "elke regelaar zweeft, verspringt of zwaait. Video en loops komen met Premium.",
        "Sim. Abra um clipe, corte para um minuto ou menos e salve em 1080p ou 4K com o som. Você "
        "também pode transformar uma foto parada num loop de três segundos, com qualquer controle "
        "oscilando, pulando ou varrendo ao longo dele. Vídeo e loops vêm com o Premium.",
        "可以。打开一段视频，剪到一分钟以内，连同声音以 1080p 或 4K 保存。也可以把一张静态图"
        "做成三秒循环动画，让任意参数在其中漂移、跳变或扫动。视频和循环动画随 Premium 提供。"),
    "Any iPhone running iOS 17 or later. The app is about 4 MB.": (
        "Jedes iPhone mit iOS 17 oder neuer. Die App ist etwa 4 MB groß.",
        "Cualquier iPhone con iOS 17 o posterior. La app ocupa unos 4 MB.",
        "Cualquier iPhone con iOS 17 o posterior. La app pesa unos 4 MB.",
        "N'importe quel iPhone sous iOS 17 ou plus récent. L'app fait environ 4 Mo.",
        "Qualsiasi iPhone con iOS 17 o successivo. L'app pesa circa 4 MB.",
        "iOS 17 以降を搭載したすべての iPhone で使えます。アプリの大きさは約 4 MB です。",
        "iOS 17 이상을 실행하는 모든 iPhone에서 쓸 수 있습니다. 앱 크기는 약 4MB입니다.",
        "Elke iPhone met iOS 17 of nieuwer. De app is ongeveer 4 MB.",
        "Qualquer iPhone com iOS 17 ou posterior. O app tem cerca de 4 MB.",
        "任何运行 iOS 17 或更高版本的 iPhone。应用大约 4 MB。"),

    # ---- structured data: MobileApplication description and featureList
    "A glitch art app for iPhone with 29 stackable effects for photos and video, each modelled on "
    "a specific way real hardware used to fail: VHS tracking, CRT phosphor bloom, a satellite feed "
    "losing lock, datamosh block corruption, pixel sorting and RGB channel separation. Everything "
    "renders on the GPU and all processing runs on device.": (
        "Eine Glitch-Art-App für iPhone mit 29 stapelbaren Effekten für Fotos und Video, jeder "
        "einer bestimmten Art nachgebildet, auf die echte Hardware früher versagte: VHS-Spurfehler, "
        "CRT-Phosphorblühen, ein Satellitensignal, das abreißt, Datamosh-Blockfehler, Pixel "
        "Sorting und RGB-Kanaltrennung. Alles wird auf der GPU gerechnet, und die gesamte "
        "Verarbeitung läuft auf dem Gerät.",
        "Una app de glitch art para iPhone con 29 efectos apilables para fotos y vídeo, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: tracking de VHS, "
        "florecimiento del fósforo en CRT, una señal de satélite que se cae, corrupción de bloques "
        "por datamosh, ordenación de píxeles y separación de canales RGB. Todo se procesa en la "
        "GPU y en el dispositivo.",
        "Una app de glitch art para iPhone con 29 efectos apilables para fotos y video, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: tracking de VHS, "
        "florecimiento del fósforo en CRT, una señal de satélite que se cae, corrupción de bloques "
        "por datamosh, ordenación de píxeles y separación de canales RGB. Todo se procesa en la "
        "GPU y en el dispositivo.",
        "Une app de glitch art pour iPhone avec 29 effets empilables pour photos et vidéos, chacun "
        "modélisé sur une façon précise dont le matériel tombait en panne : piste VHS, bavure du "
        "phosphore CRT, signal satellite qui décroche, corruption de blocs par datamosh, tri de "
        "pixels et séparation des canaux RVB. Tout est calculé sur le GPU et tout le traitement se "
        "fait sur l'appareil.",
        "Un'app di glitch art per iPhone con 29 effetti impilabili per foto e video, ognuno "
        "modellato su un modo preciso in cui l'hardware vero si guastava: tracking VHS, bagliore "
        "dei fosfori CRT, un segnale satellitare che perde l'aggancio, corruzione dei blocchi da "
        "datamosh, pixel sorting e separazione dei canali RGB. Tutto viene elaborato sulla GPU e "
        "sul dispositivo.",
        "写真にも動画にも使える、積み重ねられる 29 のエフェクトを備えた iPhone 用グリッチアート"
        "アプリ。どれも実在のハードウェアの特定の壊れ方を再現しています。VHS のトラッキング、"
        "CRT の蛍光体のにじみ、受信が途切れた衛星放送、データモッシュのブロック破損、"
        "ピクセルソート、RGB チャンネルの分離。描画はすべて GPU で行い、処理は端末上で完結します。",
        "사진과 동영상에 쌓아 올릴 수 있는 29가지 효과를 갖춘 iPhone용 글리치 아트 앱. 각 효과는 "
        "실제 하드웨어가 고장 나던 특정한 방식을 모델링합니다. VHS 트래킹, CRT 인광체 번짐, 신호를 "
        "놓친 위성 방송, 데이터모시 블록 손상, 픽셀 정렬, RGB 채널 분리. 모든 렌더링은 GPU에서, "
        "모든 처리는 기기 안에서 이루어집니다.",
        "Een glitch-art-app voor iPhone met 29 stapelbare effecten voor foto's en video, elk "
        "gemodelleerd op een specifieke manier waarop echte hardware kapotging: VHS-tracking, "
        "fosforgloed van een CRT, een satellietsignaal dat wegvalt, blokcorruptie door datamosh, "
        "pixel sorting en RGB-kanaalsplitsing. Alles wordt op de GPU gerenderd en alle verwerking "
        "gebeurt op het toestel.",
        "Um app de glitch art para iPhone com 29 efeitos empilháveis para fotos e vídeos, cada um "
        "modelado sobre um jeito específico pelo qual o hardware de verdade falhava: tracking de "
        "VHS, brilho do fósforo de CRT, um sinal de satélite caindo, corrupção de blocos por "
        "datamosh, ordenação de pixels e separação de canais RGB. Tudo é renderizado na GPU e todo "
        "o processamento roda no aparelho.",
        "一款 iPhone 上的故障艺术应用，提供 29 种可叠加效果，照片和视频都能用，每一种都对应"
        "真实硬件当年出错的某种具体方式：VHS 循迹、CRT 荧光粉晕光、失锁的卫星信号、数据莫氏的"
        "区块损坏、像素排序和 RGB 通道分离。所有渲染都在 GPU 上完成，所有处理都在设备上运行。"),
    "29 stackable glitch effects: 19 classics free, 10 more with Premium": (
        "29 stapelbare Glitch-Effekte: 19 Klassiker kostenlos, 10 weitere mit Premium",
        "29 efectos glitch apilables: 19 clásicos gratis, 10 más con Premium",
        "29 efectos glitch apilables: 19 clásicos gratis, 10 más con Premium",
        "29 effets glitch empilables : 19 classiques gratuits, 10 de plus avec Premium",
        "29 effetti glitch impilabili: 19 classici gratis, altri 10 con Premium",
        "積み重ねられる 29 のグリッチエフェクト：定番の 19 は無料、さらに 10 が Premium で",
        "쌓아 올릴 수 있는 글리치 효과 29가지: 기본 19가지 무료, Premium으로 10가지 더",
        "29 stapelbare glitch-effecten: 19 klassiekers gratis, nog 10 met Premium",
        "29 efeitos glitch empilháveis: 19 clássicos grátis, mais 10 com o Premium",
        "29 种可叠加的故障效果：19 种经典效果免费，另有 10 种随 Premium 提供"),
    "Video: trim a clip up to a minute and save it at 1080p or 4K with its sound": (
        "Video: einen Clip auf bis zu eine Minute kürzen und in 1080p oder 4K mit Ton sichern",
        "Vídeo: recorta un clip hasta un minuto y guárdalo en 1080p o 4K con su sonido",
        "Video: recorta un clip hasta un minuto y guárdalo en 1080p o 4K con su sonido",
        "Vidéo : coupez un clip jusqu'à une minute et enregistrez-le en 1080p ou en 4K avec le son",
        "Video: taglia una clip fino a un minuto e salvala in 1080p o 4K con il suo audio",
        "動画：クリップを最大 1 分までトリミングし、音声付きのまま 1080p か 4K で保存",
        "동영상: 클립을 최대 1분까지 잘라 소리와 함께 1080p 또는 4K로 저장",
        "Video: knip een clip tot een minuut en bewaar hem in 1080p of 4K met geluid",
        "Vídeo: corte um clipe até um minuto e salve em 1080p ou 4K com o som",
        "视频：把一段视频剪到一分钟以内，连同声音以 1080p 或 4K 保存"),
    "Settings that drift, step or sweep on their own": (
        "Regler, die von selbst driften, springen oder schwingen",
        "Controles que derivan, saltan o barren por sí solos",
        "Controles que derivan, saltan o barren por sí solos",
        "Des réglages qui dérivent, sautent ou balaient tout seuls",
        "Controlli che oscillano, vanno a scatti o spazzano da soli",
        "ゆらぎ、ステップ、スイープでひとりでに動くパラメータ",
        "스스로 흔들리고, 계단처럼 바뀌고, 쓸고 지나가는 설정",
        "Regelaars die vanzelf zweven, verspringen of zwaaien",
        "Controles que oscilam, pulam ou varrem sozinhos",
        "能自己漂移、跳变或扫动的参数"),
    "Camcorder, digicam, VCR and CCTV date stamps": (
        "Datumsstempel wie von Camcorder, Digicam, Videorekorder und Überwachungskamera",
        "Marcas de fecha de videocámara, cámara digital, vídeo doméstico y cámara de vigilancia",
        "Marcas de fecha de videocámara, cámara digital, videocasetera y cámara de seguridad",
        "Dates incrustées façon caméscope, appareil numérique, magnétoscope et caméra de "
        "surveillance",
        "Date impresse da videocamera, fotocamera digitale, videoregistratore e telecamera di "
        "sorveglianza",
        "ビデオカメラ、デジカメ、ビデオデッキ、防犯カメラ風の日付スタンプ",
        "캠코더, 디카, VCR, CCTV 스타일 날짜 스탬프",
        "Datumstempels zoals van een camcorder, digitale camera, videorecorder en "
        "beveiligingscamera",
        "Carimbos de data de filmadora, câmera digital, videocassete e câmera de segurança",
        "摄像机、数码相机、录像机和监控摄像头风格的日期水印"),
    "Masks that keep the subject clean and break only the background, or the other way round": (
        "Masken, die das Motiv sauber lassen und nur den Hintergrund zerstören, oder umgekehrt",
        "Máscaras que dejan limpio al sujeto y rompen solo el fondo, o al revés",
        "Máscaras que dejan limpio al sujeto y rompen solo el fondo, o al revés",
        "Des masques qui gardent le sujet net et ne cassent que l'arrière-plan, ou l'inverse",
        "Maschere che lasciano pulito il soggetto e rompono solo lo sfondo, o il contrario",
        "被写体はきれいなまま背景だけを壊す、またはその逆にするマスク",
        "피사체는 깨끗하게 두고 배경만 망가뜨리거나, 그 반대로 하는 마스킹",
        "Maskers die het onderwerp schoon laten en alleen de achtergrond breken, of andersom",
        "Máscaras que deixam o assunto limpo e quebram só o fundo, ou o contrário",
        "让主体保持干净、只破坏背景的蒙版，也可以反过来"),
    "Nine built-in presets, the Dead Air and Y2K Premium packs, and saved stacks": (
        "Neun eingebaute Presets, die Premium-Pakete Sendepause und Y2K, und gesicherte Stapel",
        "Nueve preajustes incluidos, los paquetes Premium Fin de emisión e Y2K, y combinaciones "
        "guardadas",
        "Nueve preajustes incluidos, los paquetes Premium Fuera del aire y Y2K, y combinaciones "
        "guardadas",
        "Neuf préréglages intégrés, les packs Premium Blanc d'antenne et Y2K, et des combinaisons "
        "enregistrées",
        "Nove preset inclusi, i pack Premium Fuori onda e Y2K, e combinazioni salvate",
        "収録の 9 つのプリセット、Premium のプリセットパック「放送事故」と「Y2K」、保存した組み合わせ",
        "기본 프리셋 9종, Premium 프리셋 팩 방송 사고와 Y2K, 저장한 조합",
        "Negen ingebouwde presets, de Premium-pakketten Storing en Y2K, en bewaarde combinaties",
        "Nove presets prontos, os pacotes Premium Fora do ar e Y2K, e combinações salvas",
        "九个内置预设、“停播”和“千禧”两套 Premium 预设合集，以及保存的组合"),
    "Export at 1024 pixels free, or at 2048 pixels and 4K and as three-second loops with "
    "Premium": (
        "Export in 1024 Pixeln kostenlos, mit Premium in 2048 Pixeln und 4K und als Loops von "
        "drei Sekunden",
        "Exportación a 1024 píxeles gratis, o a 2048 píxeles y 4K y como bucles de tres segundos "
        "con Premium",
        "Exportación a 1024 píxeles gratis, o a 2048 píxeles y 4K y como bucles de tres segundos "
        "con Premium",
        "Export en 1024 pixels gratuit, ou en 2048 pixels et en 4K et en boucles de trois "
        "secondes avec Premium",
        "Esportazione a 1024 pixel gratis, oppure a 2048 pixel e 4K e come loop di tre secondi con "
        "Premium",
        "無料では 1024 ピクセルで書き出し、Premium では 2048 ピクセルと 4K、3 秒のループでも書き出し",
        "무료는 1024픽셀 내보내기, Premium은 2048픽셀과 4K, 3초 루프 내보내기",
        "Export in 1024 pixels gratis, of in 2048 pixels en 4K en als loops van drie seconden met "
        "Premium",
        "Exportação em 1024 pixels grátis, ou em 2048 pixels e 4K e como loops de três segundos "
        "com o Premium",
        "免费以 1024 像素导出，Premium 可导出 2048 像素与 4K，以及三秒循环动画"),
    "GPU rendering and on-device processing, no upload, no ads": (
        "Rendering auf der GPU und Verarbeitung auf dem Gerät, kein Upload, keine Werbung",
        "Procesado en la GPU y en el dispositivo, sin subidas, sin anuncios",
        "Procesado en la GPU y en el dispositivo, sin subidas, sin anuncios",
        "Rendu sur le GPU et traitement sur l'appareil, aucun envoi, aucune publicité",
        "Rendering sulla GPU ed elaborazione sul dispositivo, nessun upload, nessuna pubblicità",
        "GPU による描画と端末内での処理、アップロードなし、広告なし",
        "GPU 렌더링과 기기 내 처리, 업로드 없음, 광고 없음",
        "Renderen op de GPU en verwerking op het toestel, geen upload, geen advertenties",
        "Renderização na GPU e processamento no aparelho, sem envio, sem anúncios",
        "GPU 渲染，设备端处理，不上传，无广告"),
})

KEEP |= {"Discord", "X", "Instagram"}  # names, the same in every language
