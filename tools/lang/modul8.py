"""lf.wtf/modul8, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

**The nineteen effect names are lifted from the app's own String Catalog**, not translated afresh.
MODUL8 already ships in these ten languages, and a site that calls an effect one thing while the
button in the app calls it another reads as machine translation even when both are correct on their
own. They were pulled straight out of `GlitchArt/Localizable.xcstrings`, so the two cannot drift.

Preset names (VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried) stay in English throughout,
because that is what the app shows on its preset row in every language.
"""

KEEP = {
    "MODUL8", "FRMT", "CYANO", "Levi Foster", "iPhone", "App Store",
    "Free · iPhone · iOS 15+",
    "Effects: VHS · Chroma · Interlace · Sync · Static · Scanlines",
    "Effects: Datamosh · Corruption · Pixel Shift · Pixel Sort · Feedback",
    "Effects: CRT · Crush · Dither · RGB Split · Invert · Film · Noise · Distortion",
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

T = dict(EFFECTS)

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
    "MODUL8 is a free glitch art app for iPhone. 19 stackable effects modelled on real hardware "
    "failures: VHS, CRT, datamosh, pixel sorting, RGB split. Runs on device.": (
        "MODUL8 ist eine kostenlose Glitch-Art-App für iPhone. 19 stapelbare Effekte, echten "
        "Hardwarefehlern nachgebildet: VHS, CRT, Datamosh, Pixel Sorting, RGB-Trennung. Läuft auf "
        "dem Gerät.",
        "MODUL8 es una app de glitch art gratis para iPhone. 19 efectos apilables modelados sobre "
        "fallos reales de hardware: VHS, CRT, datamosh, ordenación de píxeles, separación RGB. "
        "Funciona en el dispositivo.",
        "MODUL8 es una app de glitch art gratis para iPhone. 19 efectos apilables modelados sobre "
        "fallas reales de hardware: VHS, CRT, datamosh, ordenación de píxeles, separación RGB. "
        "Funciona en el dispositivo.",
        "MODUL8 est une app de glitch art gratuite pour iPhone. 19 effets empilables modélisés sur "
        "de vraies pannes de matériel : VHS, CRT, datamosh, tri de pixels, séparation RVB. "
        "Fonctionne sur l'appareil.",
        "MODUL8 è un'app di glitch art gratis per iPhone. 19 effetti impilabili modellati su guasti "
        "hardware reali: VHS, CRT, datamosh, pixel sorting, separazione RGB. Gira sul dispositivo.",
        "MODUL8 は iPhone 用の無料グリッチアートアプリです。実在のハードウェア故障を再現した、"
        "積み重ねられる 19 のエフェクト。VHS、CRT、データモッシュ、ピクセルソート、RGB 分離。"
        "処理は端末上で完結します。",
        "MODUL8는 iPhone용 무료 글리치 아트 앱입니다. 실제 하드웨어 고장을 모델링한, 쌓아 올릴 수 "
        "있는 19가지 효과. VHS, CRT, 데이터모시, 픽셀 정렬, RGB 분리. 기기 안에서 처리합니다.",
        "MODUL8 is een gratis glitch-art-app voor iPhone. 19 stapelbare effecten gemodelleerd op "
        "echte hardwarestoringen: VHS, CRT, datamosh, pixel sorting, RGB-splitsing. Draait op het "
        "toestel.",
        "O MODUL8 é um app de glitch art grátis para iPhone. 19 efeitos empilháveis modelados "
        "sobre falhas reais de hardware: VHS, CRT, datamosh, ordenação de pixels, separação RGB. "
        "Roda no aparelho.",
        "MODUL8 是一款 iPhone 上的免费故障艺术应用。19 种可叠加效果，"
        "每一种都对应真实硬件的故障：VHS、CRT、数据莫氏、像素排序、RGB 分离。全部在设备上运行。"),
    "MODUL8: Glitch Art App for iPhone": (
        "MODUL8: Glitch-Art-App für iPhone", "MODUL8: app de glitch art para iPhone",
        "MODUL8: app de glitch art para iPhone", "MODUL8 : app de glitch art pour iPhone",
        "MODUL8: app di glitch art per iPhone", "MODUL8｜iPhone 用グリッチアートアプリ",
        "MODUL8｜iPhone 글리치 아트 앱", "MODUL8: glitch-art-app voor iPhone",
        "MODUL8: app de glitch art para iPhone", "MODUL8｜iPhone 故障艺术应用"),
    "19 stackable glitch effects modelled on real hardware failures: VHS, CRT, datamosh, pixel "
    "sorting. Free on iPhone.": (
        "19 stapelbare Glitch-Effekte, echten Hardwarefehlern nachgebildet: VHS, CRT, Datamosh, "
        "Pixel Sorting. Kostenlos auf iPhone.",
        "19 efectos glitch apilables modelados sobre fallos reales de hardware: VHS, CRT, "
        "datamosh, ordenación de píxeles. Gratis en iPhone.",
        "19 efectos glitch apilables modelados sobre fallas reales de hardware: VHS, CRT, "
        "datamosh, ordenación de píxeles. Gratis en iPhone.",
        "19 effets glitch empilables modélisés sur de vraies pannes de matériel : VHS, CRT, "
        "datamosh, tri de pixels. Gratuit sur iPhone.",
        "19 effetti glitch impilabili modellati su guasti hardware reali: VHS, CRT, datamosh, "
        "pixel sorting. Gratis su iPhone.",
        "実在のハードウェア故障を再現した、積み重ねられる 19 のグリッチエフェクト。VHS、CRT、"
        "データモッシュ、ピクセルソート。iPhone で無料。",
        "실제 하드웨어 고장을 모델링한, 쌓아 올릴 수 있는 19가지 글리치 효과. VHS, CRT, "
        "데이터모시, 픽셀 정렬. iPhone에서 무료.",
        "19 stapelbare glitch-effecten gemodelleerd op echte hardwarestoringen: VHS, CRT, "
        "datamosh, pixel sorting. Gratis op iPhone.",
        "19 efeitos glitch empilháveis modelados sobre falhas reais de hardware: VHS, CRT, "
        "datamosh, ordenação de pixels. Grátis no iPhone.",
        "19 种可叠加的故障效果，对应真实硬件的故障：VHS、CRT、数据莫氏、像素排序。iPhone 上免费。"),
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
    "MODUL8 is an image modulation kit for iPhone. Nineteen effects, each one modelled on a\n"
    "      specific way that real hardware used to fail: tape that lost tracking, tubes that "
    "bloomed at\n      the edges, compression that gave up halfway through a frame. Stack them, "
    "reorder them, and\n      turn a photo into something that looks like it came off a machine "
    "that was already dying.": (
        "MODUL8 ist ein Baukasten zur Bildmodulation für iPhone. Neunzehn Effekte, jeder einer "
        "bestimmten Art nachgebildet, auf die echte Hardware früher versagte: Band, das die Spur "
        "verlor, Röhren, die an den Rändern blühten, Kompression, die mitten im Bild aufgab. "
        "Staple sie, ordne sie um, und mach aus einem Foto etwas, das aussieht, als käme es aus "
        "einer Maschine, die schon im Sterben lag.",
        "MODUL8 es un kit de modulación de imagen para iPhone. Diecinueve efectos, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: cinta que perdía el "
        "tracking, tubos que florecían por los bordes, compresión que se rendía a mitad de "
        "fotograma. Apílalos, reordénalos y convierte una foto en algo que parece salido de una "
        "máquina que ya se estaba muriendo.",
        "MODUL8 es un kit de modulación de imagen para iPhone. Diecinueve efectos, cada uno "
        "modelado sobre una forma concreta en que fallaba el hardware real: cinta que perdía el "
        "tracking, tubos que florecían por los bordes, compresión que se rendía a mitad de cuadro. "
        "Apílalos, reordénalos y convierte una foto en algo que parece salido de una máquina que "
        "ya se estaba muriendo.",
        "MODUL8 est un kit de modulation d'image pour iPhone. Dix-neuf effets, chacun modélisé sur "
        "une façon précise dont le matériel tombait en panne : la bande qui perdait la piste, les "
        "tubes qui fleurissaient sur les bords, la compression qui abandonnait au milieu d'une "
        "image. Empilez-les, réordonnez-les, et transformez une photo en quelque chose qui semble "
        "sorti d'une machine déjà mourante.",
        "MODUL8 è un kit di modulazione dell'immagine per iPhone. Diciannove effetti, ognuno "
        "modellato su un modo preciso in cui l'hardware vero si guastava: il nastro che perdeva il "
        "tracking, i tubi che fiorivano ai bordi, la compressione che si arrendeva a metà "
        "fotogramma. Impilali, riordinali, e trasforma una foto in qualcosa che sembra uscito da "
        "una macchina già morente.",
        "MODUL8 は iPhone のための画像モジュレーションキットです。十九のエフェクトは、いずれも"
        "実在のハードウェアが壊れたときの特定の壊れ方を再現しています。トラッキングを失ったテープ、"
        "端がにじんだブラウン管、一枚の途中で諦めた圧縮。積み重ね、順序を入れ替えれば、"
        "すでに死にかけていた機械から出てきたような一枚になります。",
        "MODUL8는 iPhone을 위한 이미지 변조 키트입니다. 열아홉 가지 효과가 각각 실제 하드웨어가 "
        "고장 나던 특정한 방식을 모델링합니다. 트래킹을 잃은 테이프, 가장자리가 번진 브라운관, "
        "한 프레임 도중에 포기해 버린 압축. 쌓고, 순서를 바꾸면, 이미 죽어 가던 기계에서 나온 것 "
        "같은 사진이 됩니다.",
        "MODUL8 is een beeldmodulatiekit voor iPhone. Negentien effecten, elk gemodelleerd op een "
        "specifieke manier waarop echte hardware kapotging: band die de tracking verloor, buizen "
        "die aan de randen opbloeiden, compressie die halverwege een beeld opgaf. Stapel ze, "
        "herschik ze, en maak van een foto iets dat eruitziet alsof het van een machine komt die "
        "al aan het sterven was.",
        "O MODUL8 é um kit de modulação de imagem para iPhone. Dezenove efeitos, cada um modelado "
        "sobre um jeito específico pelo qual o hardware de verdade falhava: fita que perdia o "
        "tracking, tubos que floresciam nas bordas, compressão que desistia no meio de um quadro. "
        "Empilhe, reordene, e transforme uma foto em algo que parece ter saído de uma máquina que "
        "já estava morrendo.",
        "MODUL8 是一套 iPhone 上的图像调制工具。十九种效果，每一种都对应真实硬件当年出错的某种"
        "具体方式：跑了带的磁带、边缘晕开的显像管、在一帧中途放弃的压缩。把它们叠起来、换个顺序，"
        "一张照片就会变成像是从一台已经在垂死的机器里吐出来的东西。"),
    "It is free, every effect runs on your phone, and your photos never leave the device.": (
        "Sie ist kostenlos, jeder Effekt läuft auf deinem Telefon, und deine Fotos verlassen das "
        "Gerät nie.",
        "Es gratis, cada efecto se ejecuta en tu móvil, y tus fotos nunca salen del dispositivo.",
        "Es gratis, cada efecto se ejecuta en tu celular, y tus fotos nunca salen del dispositivo.",
        "C'est gratuit, chaque effet tourne sur votre téléphone, et vos photos ne quittent jamais "
        "l'appareil.",
        "È gratis, ogni effetto gira sul tuo telefono, e le tue foto non lasciano mai il "
        "dispositivo.",
        "無料で、どのエフェクトもあなたの端末の上で動き、写真が端末の外に出ることはありません。",
        "무료이고, 모든 효과가 당신의 휴대폰에서 돌아가며, 사진은 절대 기기를 떠나지 않습니다.",
        "Het is gratis, elk effect draait op je telefoon, en je foto's verlaten het toestel nooit.",
        "É grátis, cada efeito roda no seu telefone, e suas fotos nunca saem do aparelho.",
        "它是免费的，每一种效果都在你的手机上运行，你的照片永远不会离开设备。"),
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
    "Nothing is baked in. Nineteen effects, any number of them at once, in any order you like.": (
        "Nichts ist festgelegt. Neunzehn Effekte, beliebig viele auf einmal, in beliebiger "
        "Reihenfolge.",
        "Nada está fijado. Diecinueve efectos, todos los que quieras a la vez, en el orden que "
        "quieras.",
        "Nada está fijado. Diecinueve efectos, todos los que quieras a la vez, en el orden que "
        "quieras.",
        "Rien n'est figé. Dix-neuf effets, autant que vous voulez à la fois, dans l'ordre qui vous "
        "plaît.",
        "Niente è fissato. Diciannove effetti, quanti ne vuoi insieme, nell'ordine che preferisci.",
        "決め打ちのものはありません。十九のエフェクトを、いくつでも同時に、好きな順序で。",
        "정해진 것은 없습니다. 열아홉 가지 효과를, 몇 개든 한꺼번에, 원하는 순서로.",
        "Niets ligt vast. Negentien effecten, zoveel tegelijk als je wilt, in welke volgorde je "
        "maar wilt.",
        "Nada é fixo. Dezenove efeitos, quantos você quiser de uma vez, na ordem que preferir.",
        "没有任何东西是写死的。十九种效果，想同时用几种就用几种，顺序随你。"),
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
    "Nineteen effects. Every one of them is a real failure mode.": (
        "Neunzehn Effekte. Jeder davon ist ein echter Fehlermodus.",
        "Diecinueve efectos. Cada uno es un modo de fallo real.",
        "Diecinueve efectos. Cada uno es un modo de falla real.",
        "Dix-neuf effets. Chacun est un mode de panne réel.",
        "Diciannove effetti. Ognuno è una modalità di guasto reale.",
        "十九のエフェクト。そのどれもが、実在した壊れ方です。",
        "열아홉 가지 효과. 그 하나하나가 실제로 있었던 고장 방식입니다.",
        "Negentien effecten. Elk ervan is een echte storingsmodus.",
        "Dezenove efeitos. Cada um deles é um modo de falha real.",
        "十九种效果。每一种都是真实存在过的失效方式。"),
    "They are not variations on a theme. Each one models something different, which is why "
    "stacking\n      them gets interesting instead of muddy.": (
        "Sie sind keine Variationen eines Themas. Jeder bildet etwas anderes nach, und darum wird "
        "das Stapeln interessant statt matschig.",
        "No son variaciones sobre un tema. Cada uno modela algo distinto, y por eso apilarlos "
        "resulta interesante en vez de embarrado.",
        "No son variaciones sobre un tema. Cada uno modela algo distinto, y por eso apilarlos "
        "resulta interesante en vez de embarrado.",
        "Ce ne sont pas des variations sur un thème. Chacun modélise quelque chose de différent, "
        "et c'est pourquoi les empiler devient intéressant au lieu de devenir boueux.",
        "Non sono variazioni su un tema. Ognuno modella qualcosa di diverso, ed è per questo che "
        "impilarli diventa interessante invece che fangoso.",
        "同じ主題の変奏ではありません。どれも別のものを再現しているので、重ねると濁るのではなく、"
        "面白くなります。",
        "하나의 주제에 대한 변주가 아닙니다. 각각이 서로 다른 것을 모델링하기 때문에, 쌓으면 "
        "탁해지는 대신 흥미로워집니다.",
        "Het zijn geen variaties op een thema. Elk modelleert iets anders, en daarom wordt stapelen "
        "interessant in plaats van modderig.",
        "Não são variações sobre um tema. Cada um modela algo diferente, e é por isso que empilhá-los "
        "fica interessante em vez de embolado.",
        "它们不是同一个主题的变奏。每一种模拟的都是不同的东西，所以叠起来会变得有意思，"
        "而不是糊成一团。"),
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
    "One screen. Everything on it does one thing.": (
        "Ein Bildschirm. Alles darauf tut genau eine Sache.",
        "Una pantalla. Todo lo que hay en ella hace una cosa.",
        "Una pantalla. Todo lo que hay en ella hace una cosa.",
        "Un écran. Tout ce qui s'y trouve fait une seule chose.",
        "Una schermata. Tutto quello che c'è sopra fa una cosa sola.",
        "画面はひとつ。その上のものは、それぞれひとつの働きしかしません。",
        "화면 하나. 그 위에 있는 것들은 각각 한 가지 일만 합니다.",
        "Eén scherm. Alles erop doet één ding.",
        "Uma tela. Tudo nela faz uma coisa.", "只有一个界面。上面的每样东西只做一件事。"),
    "The canvas is at the top and it updates while you drag. Underneath it are nine presets to "
    "get\n      you somewhere in one tap, then the layer stack showing exactly what is running and "
    "in what\n      order, then the effect rack. Tap an effect to open its own parameters. No "
    "menus, no modes, no\n      hunting.": (
        "Die Leinwand liegt oben und aktualisiert sich, während du ziehst. Darunter neun Presets, "
        "die dich mit einem Tippen irgendwohin bringen, dann der Ebenenstapel, der genau zeigt, "
        "was läuft und in welcher Reihenfolge, dann das Effektregal. Tippe einen Effekt an, um "
        "seine eigenen Parameter zu öffnen. Keine Menüs, keine Modi, kein Suchen.",
        "El lienzo está arriba y se actualiza mientras arrastras. Debajo hay nueve preajustes para "
        "llegar a algún sitio con un toque, luego la pila de capas que muestra exactamente qué se "
        "está ejecutando y en qué orden, y luego el estante de efectos. Toca un efecto para abrir "
        "sus propios parámetros. Sin menús, sin modos, sin buscar.",
        "El lienzo está arriba y se actualiza mientras arrastras. Debajo hay nueve preajustes para "
        "llegar a algún lado con un toque, luego la pila de capas que muestra exactamente qué se "
        "está ejecutando y en qué orden, y luego el estante de efectos. Toca un efecto para abrir "
        "sus propios parámetros. Sin menús, sin modos, sin buscar.",
        "La toile est en haut et se met à jour pendant que vous faites glisser. En dessous, neuf "
        "préréglages pour arriver quelque part en une touche, puis la pile de calques qui montre "
        "exactement ce qui tourne et dans quel ordre, puis le râtelier d'effets. Touchez un effet "
        "pour ouvrir ses propres paramètres. Pas de menus, pas de modes, pas de chasse au trésor.",
        "La tela sta in alto e si aggiorna mentre trascini. Sotto ci sono nove preset per "
        "arrivare da qualche parte con un tocco, poi lo stack dei livelli che mostra esattamente "
        "cosa sta girando e in che ordine, poi la rastrelliera degli effetti. Tocca un effetto per "
        "aprire i suoi parametri. Niente menu, niente modalità, niente caccia al tesoro.",
        "キャンバスは上にあり、ドラッグしているあいだも更新され続けます。その下に、"
        "一タップでどこかへ連れていってくれる九つのプリセット、次に、何がどの順で走っているかを"
        "そのまま示すレイヤースタック、そしてエフェクトの棚。エフェクトをタップすれば、"
        "そのエフェクト固有のパラメータが開きます。メニューもモードも、探し回ることもありません。",
        "캔버스는 위에 있고, 끄는 동안에도 계속 갱신됩니다. 그 아래에 한 번의 탭으로 어딘가에 "
        "도달하게 해 주는 아홉 개의 프리셋, 그다음에 무엇이 어떤 순서로 돌고 있는지 그대로 보여 "
        "주는 레이어 스택, 그리고 효과 선반. 효과를 누르면 그 효과만의 파라미터가 열립니다. "
        "메뉴도, 모드도, 뒤져 찾는 일도 없습니다.",
        "Het canvas zit bovenaan en werkt bij terwijl je sleept. Daaronder negen presets om je met "
        "één tik ergens te brengen, dan de lagenstapel die precies laat zien wat er draait en in "
        "welke volgorde, dan het effectenrek. Tik op een effect om de eigen parameters te openen. "
        "Geen menu's, geen modi, geen zoeken.",
        "A tela de trabalho fica no topo e se atualiza enquanto você arrasta. Abaixo dela há nove "
        "presets para chegar a algum lugar com um toque, depois a pilha de camadas mostrando "
        "exatamente o que está rodando e em que ordem, e então a prateleira de efeitos. Toque num "
        "efeito para abrir os parâmetros dele. Sem menus, sem modos, sem caçada.",
        "画布在最上面，你拖动的时候它就在更新。下面是九个预设，一下就能把你带到某个地方；"
        "再往下是图层堆栈，如实显示正在运行的是什么、按什么顺序；再往下是效果架。"
        "点一个效果就能打开它自己的参数。没有菜单，没有模式，也不用到处找。"),
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
    "Load a photo from your library, or shoot one in the app.": (
        "Lade ein Foto aus deiner Mediathek, oder nimm eines in der App auf.",
        "Carga una foto de tu fototeca, o haz una en la app.",
        "Carga una foto de tu fototeca, o toma una en la app.",
        "Chargez une photo depuis votre photothèque, ou prenez-en une dans l'app.",
        "Carica una foto dalla tua libreria, o scattane una nell'app.",
        "ライブラリから写真を読み込むか、アプリの中で一枚撮ります。",
        "보관함에서 사진을 불러오거나, 앱 안에서 한 장 찍으세요.",
        "Laad een foto uit je bibliotheek, of maak er een in de app.",
        "Carregue uma foto da sua fototeca, ou tire uma no app.",
        "从图库里载入一张照片，或者直接在应用里拍一张。"),
    "Tap a preset. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static or Fried.": (
        "Tippe ein Preset an. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static oder Fried.",
        "Toca un preajuste. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static o Fried.",
        "Toca un preajuste. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static o Fried.",
        "Touchez un préréglage. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static ou Fried.",
        "Tocca un preset. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static o Fried.",
        "プリセットをタップします。VHS、CRT、Cyber、Ghost、Retro、Film、Melt、Static、Fried。",
        "프리셋을 누르세요. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried.",
        "Tik op een preset. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static of Fried.",
        "Toque num preset. VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static ou Fried.",
        "点一个预设。VHS、CRT、Cyber、Ghost、Retro、Film、Melt、Static 或 Fried。"),
    "Open any effect and move its sliders. Intensity, and then whatever else that particular "
    "effect has: block size, tracking, spacing, curvature, threshold.": (
        "Öffne einen beliebigen Effekt und bewege seine Regler. Intensität, und dann alles andere, "
        "was dieser Effekt hat: Blockgröße, Spur, Abstand, Krümmung, Schwelle.",
        "Abre cualquier efecto y mueve sus controles. Intensidad, y luego lo que tenga ese efecto "
        "en concreto: tamaño de bloque, tracking, separación, curvatura, umbral.",
        "Abre cualquier efecto y mueve sus controles. Intensidad, y luego lo que tenga ese efecto "
        "en concreto: tamaño de bloque, tracking, separación, curvatura, umbral.",
        "Ouvrez n'importe quel effet et bougez ses curseurs. L'intensité, puis tout ce que cet "
        "effet possède en propre : taille de bloc, piste, espacement, courbure, seuil.",
        "Apri qualsiasi effetto e muovi i suoi cursori. Intensità, e poi quello che quel "
        "particolare effetto ha: dimensione dei blocchi, tracking, spaziatura, curvatura, soglia.",
        "どのエフェクトも開いて、スライダーを動かせます。強度、そしてそのエフェクト固有の項目。"
        "ブロックサイズ、トラッキング、間隔、曲率、しきい値。",
        "어떤 효과든 열어서 슬라이더를 움직이세요. 강도, 그리고 그 효과에만 있는 것들. 블록 크기, "
        "트래킹, 간격, 곡률, 임계값.",
        "Open elk effect en beweeg de schuifjes. Intensiteit, en verder wat dat specifieke effect "
        "heeft: blokgrootte, tracking, afstand, kromming, drempel.",
        "Abra qualquer efeito e mova os controles. Intensidade, e depois o que aquele efeito tiver: "
        "tamanho de bloco, tracking, espaçamento, curvatura, limiar.",
        "打开任意一个效果，拖动它的滑块。强度，以及这个效果特有的那些：块大小、循迹、间距、"
        "曲率、阈值。"),
    "Drag the layers into a different order and watch the picture change.": (
        "Zieh die Ebenen in eine andere Reihenfolge und sieh zu, wie sich das Bild ändert.",
        "Arrastra las capas a otro orden y mira cómo cambia la imagen.",
        "Arrastra las capas a otro orden y mira cómo cambia la imagen.",
        "Faites glisser les calques dans un autre ordre et regardez l'image changer.",
        "Trascina i livelli in un altro ordine e guarda l'immagine cambiare.",
        "レイヤーを別の順序へドラッグして、絵が変わるのを見てください。",
        "레이어를 다른 순서로 끌어다 놓고, 그림이 바뀌는 것을 보세요.",
        "Sleep de lagen in een andere volgorde en kijk hoe het beeld verandert.",
        "Arraste as camadas para outra ordem e veja a imagem mudar.",
        "把图层拖成另一种顺序，看着画面变化。"),
    "Export to your camera roll, or save the whole stack as a preset of your own.": (
        "Exportiere in deine Aufnahmen, oder sichere den ganzen Stapel als eigenes Preset.",
        "Exporta a tu carrete, o guarda toda la pila como un preajuste tuyo.",
        "Exporta a tu carrete, o guarda toda la pila como un preajuste tuyo.",
        "Exportez vers votre pellicule, ou enregistrez toute la pile comme votre propre "
        "préréglage.",
        "Esporta nel tuo rullino, o salva tutto lo stack come un preset tuo.",
        "カメラロールに書き出すか、積み方まるごとを自分のプリセットとして保存します。",
        "카메라 롤로 내보내거나, 쌓아 놓은 전체를 나만의 프리셋으로 저장하세요.",
        "Exporteer naar je filmrol, of bewaar de hele stapel als je eigen preset.",
        "Exporte para o seu rolo da câmera, ou salve a pilha inteira como um preset seu.",
        "导出到相机胶卷，或者把整套叠法存成你自己的预设。"),
    "On the device": ("Auf dem Gerät", "En el dispositivo", "En el dispositivo",
                      "Sur l'appareil", "Sul dispositivo", "端末の上で", "기기 안에서",
                      "Op het toestel", "No aparelho", "在设备上"),
    "Your photos stay on your phone.": (
        "Deine Fotos bleiben auf deinem Telefon.", "Tus fotos se quedan en tu móvil.",
        "Tus fotos se quedan en tu celular.", "Vos photos restent sur votre téléphone.",
        "Le tue foto restano sul tuo telefono.", "写真は端末に留まります。",
        "당신의 사진은 휴대폰에 남습니다.", "Je foto's blijven op je telefoon.",
        "Suas fotos ficam no seu telefone.", "你的照片留在你的手机里。"),
    "Every effect runs locally. There is no upload, no account, no render queue and no server\n"
    "          holding a copy of anything you shot. The app is six megabytes and the editing works "
    "in\n          aeroplane mode.": (
        "Jeder Effekt läuft lokal. Es gibt keinen Upload, kein Konto, keine Renderwarteschlange "
        "und keinen Server, der eine Kopie von irgendetwas hält, das du aufgenommen hast. Die App "
        "ist sechs Megabyte groß, und das Bearbeiten funktioniert im Flugmodus.",
        "Cada efecto se ejecuta localmente. No hay subida, ni cuenta, ni cola de render, ni "
        "servidor guardando una copia de nada de lo que hayas hecho. La app ocupa seis megabytes y "
        "la edición funciona en modo avión.",
        "Cada efecto se ejecuta localmente. No hay subida, ni cuenta, ni cola de render, ni "
        "servidor guardando una copia de nada de lo que hayas tomado. La app ocupa seis megabytes "
        "y la edición funciona en modo avión.",
        "Chaque effet tourne localement. Il n'y a pas d'envoi, pas de compte, pas de file de "
        "rendu et pas de serveur qui garde une copie de ce que vous avez photographié. L'app pèse "
        "six mégaoctets et l'édition fonctionne en mode avion.",
        "Ogni effetto gira in locale. Non c'è upload, non c'è account, non c'è coda di rendering e "
        "non c'è server che tenga una copia di quello che hai scattato. L'app pesa sei megabyte e "
        "l'editing funziona in modalità aereo.",
        "どのエフェクトも端末の中で動きます。アップロードも、アカウントも、レンダリング待ちの列も、"
        "あなたが撮ったものの控えを持つサーバーもありません。アプリは 6 メガバイトで、"
        "編集は機内モードでも動きます。",
        "모든 효과가 기기 안에서 돌아갑니다. 업로드도, 계정도, 렌더 대기열도, 당신이 찍은 것의 "
        "사본을 가진 서버도 없습니다. 앱은 6메가바이트이고, 편집은 비행기 모드에서도 됩니다.",
        "Elk effect draait lokaal. Er is geen upload, geen account, geen renderwachtrij en geen "
        "server met een kopie van wat je ook hebt geschoten. De app is zes megabyte en het bewerken "
        "werkt in vliegtuigmodus.",
        "Cada efeito roda localmente. Não há upload, não há conta, não há fila de renderização e "
        "não há servidor guardando cópia de nada do que você fotografou. O app tem seis megabytes e "
        "a edição funciona em modo avião.",
        "每一种效果都在本地运行。没有上传、没有账号、没有渲染队列，"
        "也没有任何服务器留着你拍的东西的副本。这个应用只有六兆字节，编辑在飞行模式下照样能用。"),
    "It is also why the sliders feel live: you are dragging the real image rather than waiting\n"
    "          on a round trip to somebody's GPU. The free version does serve ads, which is the "
    "one part\n          that talks to the network. Premium removes them.": (
        "Es ist auch der Grund, warum sich die Regler live anfühlen: Du ziehst am echten Bild und "
        "wartest nicht auf den Hin- und Rückweg zur GPU von irgendwem. Die kostenlose Fassung "
        "zeigt Werbung, und das ist der eine Teil, der mit dem Netz spricht. Premium entfernt sie.",
        "Es también por lo que los controles se sienten en vivo: estás arrastrando la imagen real "
        "en vez de esperar una ida y vuelta a la GPU de alguien. La versión gratuita sí muestra "
        "anuncios, que son la única parte que habla con la red. Premium los quita.",
        "Es también por lo que los controles se sienten en vivo: estás arrastrando la imagen real "
        "en vez de esperar una ida y vuelta a la GPU de alguien. La versión gratuita sí muestra "
        "anuncios, que son la única parte que habla con la red. Premium los quita.",
        "C'est aussi pourquoi les curseurs paraissent vivants : vous faites glisser l'image réelle "
        "au lieu d'attendre un aller-retour vers le GPU de quelqu'un. La version gratuite affiche "
        "de la publicité, la seule partie qui parle au réseau. Premium la supprime.",
        "È anche il motivo per cui i cursori sembrano vivi: stai trascinando l'immagine vera "
        "invece di aspettare un andata e ritorno alla GPU di qualcun altro. La versione gratuita "
        "mostra pubblicità, che è l'unica parte che parla con la rete. Premium la toglie.",
        "スライダーが生きているように感じられるのも同じ理由です。誰かの GPU との往復を待つのでは"
        "なく、実際の画像そのものをドラッグしているからです。無料版には広告が入り、"
        "ネットワークと話すのはその部分だけです。Premium にすると広告はなくなります。",
        "슬라이더가 살아 있는 것처럼 느껴지는 이유이기도 합니다. 누군가의 GPU를 왕복하기를 "
        "기다리는 게 아니라, 실제 이미지를 직접 끌고 있으니까요. 무료 버전에는 광고가 붙는데, "
        "네트워크와 이야기하는 부분은 그것뿐입니다. Premium은 광고를 없앱니다.",
        "Het is ook waarom de schuifjes live aanvoelen: je sleept het echte beeld in plaats van te "
        "wachten op een retourtje naar iemands GPU. De gratis versie toont wel advertenties, het "
        "enige deel dat met het netwerk praat. Premium haalt ze weg.",
        "É também por isso que os controles parecem ao vivo: você está arrastando a imagem real em "
        "vez de esperar uma ida e volta até a GPU de alguém. A versão gratuita exibe anúncios, que "
        "são a única parte que fala com a rede. O Premium os remove.",
        "这也是滑块用起来像实时的原因：你拖的是真实的图像，而不是在等一次往返别人 GPU 的来回。"
        "免费版确实会有广告，那是唯一与网络打交道的部分。Premium 会去掉它们。"),
    "Video too": ("Auch Video", "También vídeo", "También video", "La vidéo aussi", "Anche video",
                  "動画も", "영상도", "Video ook", "Vídeo também", "视频也可以"),
    "Loops, not just stills.": (
        "Schleifen, nicht nur Standbilder.", "Bucles, no solo fijos.", "Bucles, no solo fijos.",
        "Des boucles, pas seulement des images fixes.", "Loop, non solo fermi immagine.",
        "静止画だけでなく、ループも。", "정지 이미지만이 아니라 루프도.",
        "Loops, niet alleen stills.", "Loops, não só imagens paradas.", "不只是静图，还有循环。"),
    "Turn any finished image into a seamless looping video with the effect parameters animating\n"
    "          across the loop. The tracking drifts, the sort threshold moves, the channels "
    "breathe. It\n          exports straight to your camera roll at a size that posts cleanly.": (
        "Mach aus jedem fertigen Bild ein nahtlos geschleiftes Video, in dem sich die "
        "Effektparameter über die Schleife hinweg bewegen. Die Spur driftet, die Sortierschwelle "
        "wandert, die Kanäle atmen. Es wird direkt in deine Aufnahmen exportiert, in einer Größe, "
        "die sich sauber posten lässt.",
        "Convierte cualquier imagen terminada en un vídeo en bucle sin costuras con los parámetros "
        "de los efectos animándose a lo largo del bucle. El tracking deriva, el umbral de "
        "ordenación se mueve, los canales respiran. Se exporta directo a tu carrete a un tamaño que "
        "se publica limpio.",
        "Convierte cualquier imagen terminada en un video en bucle sin costuras con los parámetros "
        "de los efectos animándose a lo largo del bucle. El tracking deriva, el umbral de "
        "ordenación se mueve, los canales respiran. Se exporta directo a tu carrete a un tamaño que "
        "se publica limpio.",
        "Transformez n'importe quelle image finie en vidéo bouclée sans raccord, avec les "
        "paramètres des effets qui s'animent sur la boucle. La piste dérive, le seuil de tri "
        "bouge, les canaux respirent. L'export va droit dans votre pellicule, à une taille qui se "
        "publie proprement.",
        "Trasforma qualsiasi immagine finita in un video in loop senza stacchi, con i parametri "
        "degli effetti che si animano lungo il loop. Il tracking va alla deriva, la soglia di "
        "ordinamento si sposta, i canali respirano. Esce dritto nel tuo rullino a una dimensione "
        "che si pubblica pulita.",
        "仕上がった画像はどれでも、エフェクトのパラメータがループのあいだ動き続ける、"
        "継ぎ目のないループ動画にできます。トラッキングは流れ、ソートのしきい値は動き、"
        "チャンネルは呼吸します。書き出しはそのままカメラロールへ、きれいに投稿できるサイズで。",
        "완성된 이미지는 무엇이든, 효과 파라미터가 루프 내내 움직이는 이음매 없는 루프 영상으로 "
        "만들 수 있습니다. 트래킹이 흐르고, 정렬 임계값이 움직이고, 채널이 숨을 쉽니다. 내보내기는 "
        "곧장 카메라 롤로, 깔끔하게 올라가는 크기로.",
        "Maak van elk afgerond beeld een naadloos loopende video waarin de effectparameters over de "
        "loop heen animeren. De tracking drijft, de sorteerdrempel beweegt, de kanalen ademen. Het "
        "exporteert rechtstreeks naar je filmrol op een formaat dat netjes post.",
        "Transforme qualquer imagem pronta num vídeo em loop sem emenda, com os parâmetros dos "
        "efeitos se animando ao longo do loop. O tracking deriva, o limiar de ordenação se move, os "
        "canais respiram. Exporta direto para o seu rolo da câmera num tamanho que posta limpo.",
        "任何一张完成的图像都能变成无缝循环的视频，效果参数会在整个循环里持续变化。"
        "循迹在漂移，排序阈值在移动，通道在呼吸。导出直接进相机胶卷，尺寸适合干净地发布。"),
    "The deal": ("Das Angebot", "El trato", "El trato", "Le deal", "L'accordo", "料金のこと",
                 "조건", "De deal", "O acordo", "价格是这样的"),
    "Free. Premium is optional.": (
        "Kostenlos. Premium ist optional.", "Gratis. Premium es opcional.",
        "Gratis. Premium es opcional.", "Gratuit. Premium est facultatif.",
        "Gratis. Premium è facoltativo.", "無料。Premium は任意です。",
        "무료. Premium은 선택입니다.", "Gratis. Premium is optioneel.",
        "Grátis. O Premium é opcional.", "免费。Premium 是可选的。"),
    "Every one of the nineteen effects and all nine presets are free, with no limit on how many\n"
    "        you stack. Nothing is held hostage behind a paywall and nothing you export is "
    "watermarked.\n        Premium is about output and comfort, not about unlocking the tools.": (
        "Alle neunzehn Effekte und alle neun Presets sind kostenlos, ohne Grenze, wie viele du "
        "stapelst. Nichts wird hinter einer Bezahlschranke festgehalten, und nichts, was du "
        "exportierst, trägt ein Wasserzeichen. Bei Premium geht es um Ausgabe und Bequemlichkeit, "
        "nicht darum, die Werkzeuge freizuschalten.",
        "Los diecinueve efectos y los nueve preajustes son gratis, sin límite de cuántos apiles. "
        "Nada queda secuestrado tras un muro de pago y nada de lo que exportas lleva marca de agua. "
        "Premium va de salida y comodidad, no de desbloquear las herramientas.",
        "Los diecinueve efectos y los nueve preajustes son gratis, sin límite de cuántos apiles. "
        "Nada queda secuestrado tras un muro de pago y nada de lo que exportas lleva marca de agua. "
        "Premium va de salida y comodidad, no de desbloquear las herramientas.",
        "Les dix-neuf effets et les neuf préréglages sont tous gratuits, sans limite sur le nombre "
        "que vous empilez. Rien n'est retenu derrière un péage et rien de ce que vous exportez "
        "n'est filigrané. Premium concerne la sortie et le confort, pas le déverrouillage des "
        "outils.",
        "Tutti e diciannove gli effetti e tutti e nove i preset sono gratis, senza limite a quanti "
        "ne impili. Niente è tenuto in ostaggio dietro un paywall e niente di quello che esporti "
        "porta filigrane. Premium riguarda l'output e la comodità, non lo sblocco degli strumenti.",
        "十九のエフェクトも九つのプリセットも、すべて無料です。いくつ重ねてもかまいません。"
        "課金の壁の向こうに人質に取られているものはなく、書き出したものに透かしも入りません。"
        "Premium は出力と快適さの話であって、道具を解放するための話ではありません。",
        "열아홉 가지 효과와 아홉 개의 프리셋 모두 무료이고, 몇 개를 쌓든 제한이 없습니다. 결제 "
        "장벽 뒤에 붙잡아 둔 것은 없고, 내보낸 것에 워터마크도 없습니다. Premium은 출력과 편의에 "
        "대한 것이지, 도구를 푸는 것에 대한 것이 아닙니다.",
        "Alle negentien effecten en alle negen presets zijn gratis, zonder limiet op hoeveel je er "
        "stapelt. Er wordt niets gegijzeld achter een betaalmuur en niets wat je exporteert draagt "
        "een watermerk. Premium gaat over uitvoer en gemak, niet over het vrijspelen van het "
        "gereedschap.",
        "Todos os dezenove efeitos e todos os nove presets são grátis, sem limite de quantos você "
        "empilha. Nada fica refém atrás de um paywall e nada do que você exporta leva marca "
        "d'água. O Premium é sobre saída e conforto, não sobre destravar as ferramentas.",
        "十九种效果和九个预设全部免费，叠多少层都不限。没有任何东西被扣在付费墙后面，"
        "你导出的东西也不会带水印。Premium 关乎输出和省事，而不是解锁工具。"),
    "Free": ("Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료", "Gratis",
             "Grátis", "免费"),
    "All 19 effects, all 9 presets, unlimited stacking, save and share, no watermark": (
        "Alle 19 Effekte, alle 9 Presets, unbegrenztes Stapeln, Sichern und Teilen, kein "
        "Wasserzeichen",
        "Los 19 efectos, los 9 preajustes, apilado ilimitado, guardar y compartir, sin marca de "
        "agua",
        "Los 19 efectos, los 9 preajustes, apilado ilimitado, guardar y compartir, sin marca de "
        "agua",
        "Les 19 effets, les 9 préréglages, empilage illimité, enregistrer et partager, sans "
        "filigrane",
        "Tutti i 19 effetti, tutti i 9 preset, impilamento illimitato, salva e condividi, nessuna "
        "filigrana",
        "19 のエフェクトすべて、9 つのプリセットすべて、重ね放題、保存と共有、透かしなし",
        "19가지 효과 전부, 9개 프리셋 전부, 무제한 쌓기, 저장과 공유, 워터마크 없음",
        "Alle 19 effecten, alle 9 presets, onbeperkt stapelen, bewaren en delen, geen watermerk",
        "Todos os 19 efeitos, todos os 9 presets, empilhamento ilimitado, salvar e compartilhar, "
        "sem marca d'água",
        "全部 19 种效果、全部 9 个预设、无限叠加、保存与分享、无水印"),
    "Premium": ("Premium",) * 10,
    "Full resolution export, looping video export, saving your own presets, no ads": (
        "Export in voller Auflösung, Export als Videoschleife, eigene Presets sichern, keine "
        "Werbung",
        "Exportación a resolución completa, exportación de vídeo en bucle, guardar tus propios "
        "preajustes, sin anuncios",
        "Exportación a resolución completa, exportación de video en bucle, guardar tus propios "
        "preajustes, sin anuncios",
        "Export en pleine résolution, export en vidéo bouclée, enregistrement de vos propres "
        "préréglages, sans publicité",
        "Esportazione a piena risoluzione, esportazione video in loop, salvataggio dei tuoi preset, "
        "nessuna pubblicità",
        "フル解像度での書き出し、ループ動画の書き出し、自分のプリセットの保存、広告なし",
        "원본 해상도 내보내기, 루프 영상 내보내기, 나만의 프리셋 저장, 광고 없음",
        "Export op volle resolutie, export als loopende video, je eigen presets bewaren, geen "
        "advertenties",
        "Exportação em resolução total, exportação de vídeo em loop, salvar seus próprios presets, "
        "sem anúncios",
        "完整分辨率导出、循环视频导出、保存自己的预设、无广告"),
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
#
# The effect roll-call is left in the app's own names, joined the way the visible list is, so a
# reader can match every word against a button.
_EFFECT_LIST = tuple(
    ", ".join(EFFECTS[k][i] for k in
              ["NOISE", "PIXEL SHIFT", "RGB SPLIT", "SCANLINES", "DISTORTION", "CORRUPTION",
               "FEEDBACK", "VHS", "CRT", "CHROMA", "FILM", "CRUSH", "INTERLACE", "INVERT",
               "DATAMOSH", "DITHER", "STATIC", "SORT", "SYNC"])
    for i in range(10))

_FREE_ANSWER = (
    "Ja. Alle 19 Effekte, alle 9 Presets und unbegrenztes Stapeln sind kostenlos, und nichts, was "
    "du exportierst, trägt ein Wasserzeichen. Premium ergänzt Export in voller Auflösung, Export "
    "als Videoschleife, das Sichern eigener Presets, und entfernt die Werbung.",
    "Sí. Los 19 efectos, los 9 preajustes y el apilado ilimitado son gratis, y nada de lo que "
    "exportas lleva marca de agua. Premium añade exportación a resolución completa, exportación de "
    "vídeo en bucle, guardar tus propios preajustes, y quita los anuncios.",
    "Sí. Los 19 efectos, los 9 preajustes y el apilado ilimitado son gratis, y nada de lo que "
    "exportas lleva marca de agua. Premium añade exportación a resolución completa, exportación de "
    "video en bucle, guardar tus propios preajustes, y quita los anuncios.",
    "Oui. Les 19 effets, les 9 préréglages et l'empilage illimité sont gratuits, et rien de ce que "
    "vous exportez n'est filigrané. Premium ajoute l'export en pleine résolution, l'export en "
    "vidéo bouclée, l'enregistrement de vos propres préréglages, et supprime la publicité.",
    "Sì. Tutti i 19 effetti, tutti i 9 preset e l'impilamento illimitato sono gratis, e niente di "
    "quello che esporti porta filigrane. Premium aggiunge l'esportazione a piena risoluzione, "
    "l'esportazione video in loop, il salvataggio dei tuoi preset, e toglie la pubblicità.",
    "はい。19 のエフェクト、9 つのプリセット、そして重ね放題はすべて無料で、書き出したものに"
    "透かしも入りません。Premium では、フル解像度での書き出し、ループ動画の書き出し、"
    "自分のプリセットの保存が加わり、広告がなくなります。",
    "네. 19가지 효과, 9개 프리셋, 무제한 쌓기가 모두 무료이고, 내보낸 것에 워터마크도 없습니다. "
    "Premium은 원본 해상도 내보내기, 루프 영상 내보내기, 나만의 프리셋 저장을 더하고 광고를 "
    "없앱니다.",
    "Ja. Alle 19 effecten, alle 9 presets en onbeperkt stapelen zijn gratis, en niets wat je "
    "exporteert draagt een watermerk. Premium voegt export op volle resolutie toe, export als "
    "loopende video, het bewaren van je eigen presets, en haalt de advertenties weg.",
    "Sim. Todos os 19 efeitos, todos os 9 presets e o empilhamento ilimitado são grátis, e nada do "
    "que você exporta leva marca d'água. O Premium acrescenta exportação em resolução total, "
    "exportação de vídeo em loop, salvar seus próprios presets, e remove os anúncios.",
    "是的。19 种效果、9 个预设和无限叠加全部免费，你导出的东西也不带水印。"
    "Premium 增加完整分辨率导出、循环视频导出、保存自己的预设，并去掉广告。")

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

_UPLOAD_ANSWER = (
    "Nein. Jeder Effekt läuft lokal auf deinem iPhone. Es gibt kein Konto, keine "
    "Renderwarteschlange und keinen Server, der deine Bilder hält. Die kostenlose Fassung zeigt "
    "Werbung, und das ist der einzige Teil der App, der das Netz benutzt.",
    "No. Cada efecto se ejecuta localmente en tu iPhone. No hay cuenta, ni cola de render, ni "
    "servidor guardando tus imágenes. La versión gratuita muestra anuncios, que son la única parte "
    "de la app que usa la red.",
    "No. Cada efecto se ejecuta localmente en tu iPhone. No hay cuenta, ni cola de render, ni "
    "servidor guardando tus imágenes. La versión gratuita muestra anuncios, que son la única parte "
    "de la app que usa la red.",
    "Non. Chaque effet tourne localement sur votre iPhone. Il n'y a pas de compte, pas de file de "
    "rendu et pas de serveur qui garde vos images. La version gratuite affiche de la publicité, la "
    "seule partie de l'app qui utilise le réseau.",
    "No. Ogni effetto gira in locale sul tuo iPhone. Non c'è account, non c'è coda di rendering e "
    "non c'è server che tenga le tue immagini. La versione gratuita mostra pubblicità, l'unica "
    "parte dell'app che usa la rete.",
    "いいえ。どのエフェクトもあなたの iPhone の中で動きます。アカウントも、レンダリング待ちの"
    "列も、あなたの画像を持つサーバーもありません。無料版には広告が入り、"
    "ネットワークを使うのはアプリのなかでその部分だけです。",
    "아니요. 모든 효과가 당신의 iPhone 안에서 돌아갑니다. 계정도, 렌더 대기열도, 당신의 이미지를 "
    "가진 서버도 없습니다. 무료 버전에는 광고가 붙는데, 앱에서 네트워크를 쓰는 부분은 그것뿐입니다.",
    "Nee. Elk effect draait lokaal op je iPhone. Er is geen account, geen renderwachtrij en geen "
    "server met jouw beelden. De gratis versie toont advertenties, het enige deel van de app dat "
    "het netwerk gebruikt.",
    "Não. Cada efeito roda localmente no seu iPhone. Não há conta, não há fila de renderização e "
    "não há servidor guardando suas imagens. A versão gratuita exibe anúncios, que são a única "
    "parte do app que usa a rede.",
    "不会。每一种效果都在你的 iPhone 本地运行。没有账号、没有渲染队列，也没有服务器存着你的图像。"
    "免费版会显示广告，那是这个应用里唯一用到网络的部分。")

_VIDEO_ANSWER = (
    "Ja. Jedes fertige Bild lässt sich als nahtlos geschleiftes Video exportieren, in dem sich die "
    "Effektparameter über die Schleife hinweg bewegen, direkt in deine Aufnahmen.",
    "Sí. Cualquier imagen terminada se puede exportar como vídeo en bucle sin costuras con los "
    "parámetros de los efectos animándose a lo largo del bucle, directo a tu carrete.",
    "Sí. Cualquier imagen terminada se puede exportar como video en bucle sin costuras con los "
    "parámetros de los efectos animándose a lo largo del bucle, directo a tu carrete.",
    "Oui. N'importe quelle image finie peut être exportée en vidéo bouclée sans raccord, avec les "
    "paramètres des effets qui s'animent sur la boucle, directement dans votre pellicule.",
    "Sì. Qualsiasi immagine finita può essere esportata come video in loop senza stacchi, con i "
    "parametri degli effetti che si animano lungo il loop, dritto nel tuo rullino.",
    "はい。仕上がった画像はどれでも、エフェクトのパラメータがループのあいだ動き続ける継ぎ目のない"
    "ループ動画として、そのままカメラロールへ書き出せます。",
    "네. 완성된 이미지는 무엇이든, 효과 파라미터가 루프 내내 움직이는 이음매 없는 루프 영상으로 "
    "곧장 카메라 롤에 내보낼 수 있습니다.",
    "Ja. Elk afgerond beeld kan worden geëxporteerd als naadloos loopende video waarin de "
    "effectparameters over de loop heen animeren, rechtstreeks naar je filmrol.",
    "Sim. Qualquer imagem pronta pode ser exportada como vídeo em loop sem emenda, com os "
    "parâmetros dos efeitos se animando ao longo do loop, direto para o seu rolo da câmera.",
    "可以。任何一张完成的图像都能导出为无缝循环视频，效果参数会在整个循环里持续变化，"
    "直接存进相机胶卷。")

T.update({
    "Is MODUL8 free?": ("Ist MODUL8 kostenlos?", "¿MODUL8 es gratis?", "¿MODUL8 es gratis?",
                        "MODUL8 est-il gratuit ?", "MODUL8 è gratis?", "MODUL8 は無料ですか。",
                        "MODUL8는 무료인가요?", "Is MODUL8 gratis?", "O MODUL8 é grátis?",
                        "MODUL8 是免费的吗？"),
    "Yes. All 19 effects, all 9 presets and unlimited stacking are free, and nothing you export\n"
    "        is watermarked. Premium adds full resolution export, looping video export, saving your "
    "own\n        presets, and removes ads.": _FREE_ANSWER,
    "Yes. All 19 effects, all 9 presets and unlimited stacking are free, and nothing you export "
    "carries a watermark. Premium adds full resolution export, looping video export, saving your "
    "own presets, and removes ads.": _FREE_ANSWER,
    "What effects are in it?": (
        "Welche Effekte sind drin?", "¿Qué efectos trae?", "¿Qué efectos trae?",
        "Quels effets contient-il ?", "Che effetti ci sono?", "どんなエフェクトが入っていますか。",
        "어떤 효과가 들어 있나요?", "Welke effecten zitten erin?", "Que efeitos tem nele?",
        "里面有哪些效果？"),
    "Noise, Pixel Shift, RGB Split, Scanlines, Distortion, Corruption, Feedback, VHS, CRT,\n"
    "        Chroma, Film Grain, Bit Crush, Interlace, Invert, Datamosh, Dither, Analogue Static, "
    "Pixel\n        Sort and Signal Sync. Any number at once, in any order.": tuple(
        _EFFECT_LIST[i] + suffix for i, suffix in enumerate([
            ". Beliebig viele auf einmal, in beliebiger Reihenfolge.",
            ". Todos los que quieras a la vez, en el orden que quieras.",
            ". Todos los que quieras a la vez, en el orden que quieras.",
            ". Autant que vous voulez à la fois, dans n'importe quel ordre.",
            ". Quanti ne vuoi insieme, in qualsiasi ordine.",
            "。いくつでも同時に、好きな順序で。",
            ". 몇 개든 한꺼번에, 어떤 순서로든.",
            ". Zoveel tegelijk als je wilt, in welke volgorde dan ook.",
            ". Quantos você quiser de uma vez, em qualquer ordem.",
            "。想同时用几种就用几种，顺序随你。"])),
    "Noise, Pixel Shift, RGB Split, Scanlines, Distortion, Corruption, Feedback, VHS, CRT, Chroma, "
    "Film Grain, Bit Crush, Interlace, Invert, Datamosh, Dither, Analogue Static, Pixel Sort and "
    "Signal Sync. Any number of them can run at once, in any order.": tuple(
        _EFFECT_LIST[i] + suffix for i, suffix in enumerate([
            ". Beliebig viele davon können gleichzeitig laufen, in beliebiger Reihenfolge.",
            ". Pueden ejecutarse todos a la vez, en el orden que quieras.",
            ". Pueden ejecutarse todos a la vez, en el orden que quieras.",
            ". Autant qu'on veut peuvent tourner en même temps, dans n'importe quel ordre.",
            ". Quanti se ne vuole possono girare insieme, in qualsiasi ordine.",
            "。いくつでも同時に走らせられ、順序も自由です。",
            ". 몇 개든 동시에 돌릴 수 있고, 순서도 자유입니다.",
            ". Zoveel als je wilt kunnen tegelijk draaien, in welke volgorde dan ook.",
            ". Quantos quiser podem rodar ao mesmo tempo, em qualquer ordem.",
            "。想同时跑几种都可以，顺序也随意。"])),
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
    "Most glitch apps lay a fixed pattern over whatever you give them, so every photo comes out "
    "looking the same. Each MODUL8 effect models one specific hardware failure and reads the pixels "
    "underneath before deciding what to do, so the same settings produce different results on "
    "different photographs.": _DIFFERENT_ANSWER,
    "Does it upload my photos?": (
        "Lädt es meine Fotos hoch?", "¿Sube mis fotos?", "¿Sube mis fotos?",
        "Est-ce qu'il envoie mes photos ?", "Carica le mie foto?",
        "写真をアップロードしますか。", "제 사진을 업로드하나요?", "Uploadt het mijn foto's?",
        "Ele envia minhas fotos?", "它会上传我的照片吗？"),
    "No. Every effect runs locally on your iPhone. There is no account, no render queue and no\n"
    "        server holding your images. The free version serves ads, which is the only part of the "
    "app\n        that touches the network.": _UPLOAD_ANSWER,
    "No. Every effect runs locally on your iPhone. There is no account, no render queue and no "
    "server holding your images. The free version does serve ads, which is the only part of the app "
    "that uses the network.": _UPLOAD_ANSWER,
    "Does MODUL8 upload my photos?": (
        "Lädt MODUL8 meine Fotos hoch?", "¿MODUL8 sube mis fotos?", "¿MODUL8 sube mis fotos?",
        "MODUL8 envoie-t-il mes photos ?", "MODUL8 carica le mie foto?",
        "MODUL8 は写真をアップロードしますか。", "MODUL8가 제 사진을 업로드하나요?",
        "Uploadt MODUL8 mijn foto's?", "O MODUL8 envia minhas fotos?", "MODUL8 会上传我的照片吗？"),
    "Can it make glitch videos?": (
        "Kann es Glitch-Videos machen?", "¿Puede hacer vídeos glitch?",
        "¿Puede hacer videos glitch?", "Peut-il faire des vidéos glitch ?",
        "Può fare video glitch?", "グリッチ動画はつくれますか。", "글리치 영상도 만들 수 있나요?",
        "Kan het glitch-video's maken?", "Ele consegue fazer vídeos glitch?",
        "它能做故障视频吗？"),
    "Yes. Any finished image can be exported as a seamless looping video with the effect\n"
    "        parameters animating across the loop, straight to your camera roll.": _VIDEO_ANSWER,
    "Yes. Any finished image can be exported as a seamless looping video with the effect parameters "
    "animating across the loop, saved straight to your camera roll.": _VIDEO_ANSWER,
    "Can MODUL8 make glitch videos?": (
        "Kann MODUL8 Glitch-Videos machen?", "¿MODUL8 puede hacer vídeos glitch?",
        "¿MODUL8 puede hacer videos glitch?", "MODUL8 peut-il faire des vidéos glitch ?",
        "MODUL8 può fare video glitch?", "MODUL8 でグリッチ動画はつくれますか。",
        "MODUL8로 글리치 영상을 만들 수 있나요?", "Kan MODUL8 glitch-video's maken?",
        "O MODUL8 consegue fazer vídeos glitch?", "MODUL8 能做故障视频吗？"),
    "Which iPhones does it work on?": (
        "Auf welchen iPhones läuft es?", "¿En qué iPhones funciona?", "¿En qué iPhones funciona?",
        "Sur quels iPhone fonctionne-t-il ?", "Su quali iPhone funziona?",
        "どの iPhone で使えますか。", "어떤 iPhone에서 쓸 수 있나요?",
        "Op welke iPhones werkt het?", "Em quais iPhones funciona?", "支持哪些 iPhone？"),
    "Any iPhone running iOS 15 or later. The app is about 6 MB.": (
        "Jedes iPhone mit iOS 15 oder neuer. Die App ist etwa 6 MB groß.",
        "Cualquier iPhone con iOS 15 o posterior. La app ocupa unos 6 MB.",
        "Cualquier iPhone con iOS 15 o posterior. La app ocupa unos 6 MB.",
        "Tout iPhone sous iOS 15 ou version ultérieure. L'app pèse environ 6 Mo.",
        "Qualsiasi iPhone con iOS 15 o successivo. L'app pesa circa 6 MB.",
        "iOS 15 以降が動く iPhone。アプリの大きさはおよそ 6 MB です。",
        "iOS 15 이상이 설치된 iPhone. 앱 크기는 약 6 MB입니다.",
        "Elke iPhone met iOS 15 of nieuwer. De app is ongeveer 6 MB.",
        "Qualquer iPhone com iOS 15 ou posterior. O app tem cerca de 6 MB.",
        "任何运行 iOS 15 或更高版本的 iPhone。应用大约 6 MB。"),
    "Which iPhones does MODUL8 support?": (
        "Welche iPhones unterstützt MODUL8?", "¿Qué iPhones admite MODUL8?",
        "¿Qué iPhones admite MODUL8?", "Quels iPhone MODUL8 prend-il en charge ?",
        "Quali iPhone supporta MODUL8?", "MODUL8 はどの iPhone に対応していますか。",
        "MODUL8는 어떤 iPhone을 지원하나요?", "Welke iPhones ondersteunt MODUL8?",
        "Quais iPhones o MODUL8 suporta?", "MODUL8 支持哪些 iPhone？"),
    "What glitch effects does MODUL8 include?": (
        "Welche Glitch-Effekte enthält MODUL8?", "¿Qué efectos glitch incluye MODUL8?",
        "¿Qué efectos glitch incluye MODUL8?", "Quels effets glitch MODUL8 inclut-il ?",
        "Quali effetti glitch include MODUL8?", "MODUL8 にはどんなグリッチエフェクトが"
        "入っていますか。", "MODUL8에는 어떤 글리치 효과가 들어 있나요?",
        "Welke glitch-effecten bevat MODUL8?", "Que efeitos glitch o MODUL8 inclui?",
        "MODUL8 包含哪些故障效果？"),
    "A glitch art app for iPhone with 19 stackable effects, each modelled on a specific way real "
    "hardware used to fail: VHS tracking, CRT phosphor bloom, datamosh block corruption, pixel "
    "sorting and RGB channel separation. All processing runs on device.": (
        "Eine Glitch-Art-App für iPhone mit 19 stapelbaren Effekten, jeder einer bestimmten Art "
        "nachgebildet, auf die echte Hardware früher versagte: VHS-Spur, CRT-Phosphorblüte, "
        "Datamosh-Blockfehler, Pixel Sorting und RGB-Kanaltrennung. Die gesamte Verarbeitung läuft "
        "auf dem Gerät.",
        "Una app de glitch art para iPhone con 19 efectos apilables, cada uno modelado sobre una "
        "forma concreta en que fallaba el hardware real: tracking de VHS, floración del fósforo del "
        "CRT, corrupción de bloques por datamosh, ordenación de píxeles y separación de canales "
        "RGB. Todo el procesado se ejecuta en el dispositivo.",
        "Una app de glitch art para iPhone con 19 efectos apilables, cada uno modelado sobre una "
        "forma concreta en que fallaba el hardware real: tracking de VHS, floración del fósforo del "
        "CRT, corrupción de bloques por datamosh, ordenación de píxeles y separación de canales "
        "RGB. Todo el procesamiento se ejecuta en el dispositivo.",
        "Une app de glitch art pour iPhone avec 19 effets empilables, chacun modélisé sur une façon "
        "précise dont le matériel tombait en panne : piste VHS, floraison du phosphore CRT, "
        "corruption de blocs en datamosh, tri de pixels et séparation des canaux RVB. Tout le "
        "traitement tourne sur l'appareil.",
        "Un'app di glitch art per iPhone con 19 effetti impilabili, ognuno modellato su un modo "
        "preciso in cui l'hardware vero si guastava: tracking VHS, fioritura del fosforo CRT, "
        "corruzione a blocchi da datamosh, pixel sorting e separazione dei canali RGB. Tutta "
        "l'elaborazione gira sul dispositivo.",
        "積み重ねられる 19 のエフェクトを備えた iPhone 用グリッチアートアプリ。いずれも実在の"
        "ハードウェアが壊れたときの特定の壊れ方を再現しています。VHS のトラッキング、"
        "CRT の蛍光体のにじみ、データモッシュのブロック破損、ピクセルソート、RGB チャンネル分離。"
        "処理はすべて端末上で行われます。",
        "쌓아 올릴 수 있는 19가지 효과를 갖춘 iPhone용 글리치 아트 앱. 각각 실제 하드웨어가 고장 "
        "나던 특정한 방식을 모델링했습니다. VHS 트래킹, CRT 인광체 번짐, 데이터모시 블록 손상, 픽셀 "
        "정렬, RGB 채널 분리. 모든 처리가 기기 안에서 이루어집니다.",
        "Een glitch-art-app voor iPhone met 19 stapelbare effecten, elk gemodelleerd op een "
        "specifieke manier waarop echte hardware kapotging: VHS-tracking, CRT-fosforbloei, "
        "datamosh-blokcorruptie, pixel sorting en RGB-kanaalscheiding. Alle verwerking draait op "
        "het toestel.",
        "Um app de glitch art para iPhone com 19 efeitos empilháveis, cada um modelado sobre um "
        "jeito específico pelo qual o hardware de verdade falhava: tracking de VHS, floração do "
        "fósforo do CRT, corrupção de blocos por datamosh, ordenação de pixels e separação de "
        "canais RGB. Todo o processamento roda no aparelho.",
        "一款 iPhone 故障艺术应用，19 种可叠加效果，每一种都对应真实硬件当年出错的某种具体方式："
        "VHS 循迹、CRT 荧光粉晕开、datamosh 区块损坏、像素排序和 RGB 通道分离。全部处理都在设备上"
        "进行。"),
    "19 stackable glitch effects": (
        "19 stapelbare Glitch-Effekte", "19 efectos glitch apilables",
        "19 efectos glitch apilables", "19 effets glitch empilables",
        "19 effetti glitch impilabili", "積み重ねられる 19 のグリッチエフェクト",
        "쌓아 올릴 수 있는 19가지 글리치 효과", "19 stapelbare glitch-effecten",
        "19 efeitos glitch empilháveis", "19 种可叠加的故障效果"),
    "Reorderable effect layers": (
        "Umsortierbare Effektebenen", "Capas de efectos reordenables",
        "Capas de efectos reordenables", "Calques d'effets réordonnables",
        "Livelli di effetti riordinabili", "順序を入れ替えられるエフェクトレイヤー",
        "순서를 바꿀 수 있는 효과 레이어", "Herschikbare effectlagen",
        "Camadas de efeitos reordenáveis", "可重新排序的效果图层"),
    "Nine presets: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried": (
        "Neun Presets: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Nueve preajustes: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Nueve preajustes: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Neuf préréglages : VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Nove preset: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "九つのプリセット：VHS、CRT、Cyber、Ghost、Retro、Film、Melt、Static、Fried",
        "아홉 개의 프리셋: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Negen presets: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "Nove presets: VHS, CRT, Cyber, Ghost, Retro, Film, Melt, Static, Fried",
        "九个预设：VHS、CRT、Cyber、Ghost、Retro、Film、Melt、Static、Fried"),
    "Per-effect parameter control": (
        "Parametersteuerung pro Effekt", "Control de parámetros por efecto",
        "Control de parámetros por efecto", "Contrôle des paramètres effet par effet",
        "Controllo dei parametri per ogni effetto", "エフェクトごとのパラメータ調整",
        "효과별 파라미터 조절", "Parameterregeling per effect",
        "Controle de parâmetros por efeito", "逐效果的参数控制"),
    "Looping video export": (
        "Export als Videoschleife", "Exportación de vídeo en bucle",
        "Exportación de video en bucle", "Export en vidéo bouclée",
        "Esportazione video in loop", "ループ動画の書き出し", "루프 영상 내보내기",
        "Export als loopende video", "Exportação de vídeo em loop", "循环视频导出"),
    "On-device processing, no upload": (
        "Verarbeitung auf dem Gerät, kein Upload", "Procesado en el dispositivo, sin subida",
        "Procesamiento en el dispositivo, sin subida", "Traitement sur l'appareil, sans envoi",
        "Elaborazione sul dispositivo, nessun upload", "処理は端末上、アップロードなし",
        "기기 내 처리, 업로드 없음", "Verwerking op het toestel, geen upload",
        "Processamento no aparelho, sem upload", "在设备上处理，不上传"),
})
