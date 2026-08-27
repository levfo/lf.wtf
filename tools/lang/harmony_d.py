"""Harmony Palette page, part D: languages, the respect cards, the FAQ and the footer.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The FAQ answers are written once here in their wrapped form. merge.py matches the flattened copies
that live in the JSON-LD by collapsing whitespace, so the structured data and the visible page keep
saying the same thing in every language without either being typed twice.

The paragraph about translated colour names has to be rewritten per language rather than
translated. In German the example is Mitternachtsblau against Midnight Blue, which only makes its
point in German; every other language needs its own real pair, taken from the app's own
ColorNames.<locale>.json and CuratedPalettes.<locale>.json.
"""

T = {
    "eleven languages,": (
        "elf Sprachen,", "once idiomas,", "once idiomas,", "onze langues,", "undici lingue,",
        "11 の言語で、", "11개 언어,", "elf talen,", "onze idiomas,", "11 种语言，"),
    "colors included": (
        "Farben inbegriffen", "colores incluidos", "colores incluidos", "couleurs comprises",
        "colori compresi", "色の名前まで", "색 이름까지", "kleuren inbegrepen",
        "cores inclusas", "连颜色一起"),
    "Most apps translate their buttons. This one translates the colors.": (
        "Die meisten Apps übersetzen ihre Schaltflächen. Diese übersetzt die Farben.",
        "La mayoría de las apps traducen sus botones. Esta traduce los colores.",
        "La mayoría de las apps traducen sus botones. Esta traduce los colores.",
        "La plupart des applications traduisent leurs boutons. Celle-ci traduit les couleurs.",
        "La maggior parte delle app traduce i propri pulsanti. Questa traduce i colori.",
        "たいていのアプリはボタンを翻訳します。これは色を翻訳します。",
        "대부분의 앱은 버튼을 번역합니다. 이 앱은 색을 번역합니다.",
        "De meeste apps vertalen hun knoppen. Deze vertaalt de kleuren.",
        "A maioria dos apps traduz seus botões. Este traduz as cores.",
        "多数应用翻译的是按钮。这一款翻译的是颜色。"),
    "All 279 color names and all 160 curated palettes, with their descriptions and their search\n      tags, exist in every language the app ships in. A German user gets Mitternachtsblau, not\n      Midnight Blue sitting inside an otherwise German interface. So does the palette called\n      Sternennacht, described as van Gogh's swirling night piece, and the tags you would search\n      it by.": (
        "Alle 279 Farbnamen und alle 160 kuratierten Paletten, mit ihren Beschreibungen und ihren "
        "Such-Schlagwörtern, gibt es in jeder Sprache, in der die App erscheint. Wer sie auf "
        "Deutsch benutzt, bekommt Mitternachtsblau und nicht Midnight Blue mitten in einer sonst "
        "deutschen Oberfläche. Ebenso die Palette Sternennacht, beschrieben als van Goghs "
        "wirbelndes Nachtstück, und die Schlagwörter, mit denen Sie danach suchen würden.",
        "Los 279 nombres de color y las 160 paletas seleccionadas, con sus descripciones y sus "
        "etiquetas de búsqueda, existen en todos los idiomas en los que sale la app. Quien la use "
        "en español obtiene Azul medianoche, y no Midnight Blue metido en una interfaz por lo "
        "demás en español. Lo mismo con la paleta llamada Noche estrellada, descrita como la "
        "arremolinada obra nocturna de van Gogh, y con las etiquetas por las que la buscarías.",
        "Los 279 nombres de color y las 160 paletas seleccionadas, con sus descripciones y sus "
        "etiquetas de búsqueda, existen en todos los idiomas en los que sale la app. Quien la use "
        "en español obtiene Azul medianoche, y no Midnight Blue metido en una interfaz por lo "
        "demás en español. Lo mismo con la paleta llamada Noche estrellada, descrita como la "
        "arremolinada obra nocturna de van Gogh, y con las etiquetas por las que la buscarías.",
        "Les 279 noms de couleurs et les 160 palettes sélectionnées, avec leurs descriptions et "
        "leurs mots-clés de recherche, existent dans chaque langue où l'application paraît. Qui "
        "l'utilise en français obtient Bleu de minuit, et non Midnight Blue posé au milieu d'une "
        "interface par ailleurs française. Idem pour la palette appelée Nuit étoilée, décrite "
        "comme la nuit tourbillonnante de van Gogh, et pour les mots-clés par lesquels vous la "
        "chercheriez.",
        "Tutti i 279 nomi di colore e tutte le 160 palette selezionate, con le loro descrizioni e "
        "le loro etichette di ricerca, esistono in ogni lingua in cui esce l'app. Chi la usa in "
        "italiano ottiene Blu mezzanotte, e non Midnight Blue piazzato in un'interfaccia per il "
        "resto italiana. Lo stesso vale per la palette chiamata Notte stellata, descritta come la "
        "notte vorticosa di van Gogh, e per le etichette con cui la cercheresti.",
        "279 の色名と 160 の厳選パレットは、説明文も検索用のタグも含めて、"
        "アプリが対応するすべての言語に存在します。日本語で使えば、"
        "日本語のインターフェースの真ん中に Midnight Blue が残るのではなく、真夜中の青になります。"
        "ゴッホの渦巻く夜の絵と説明された星月夜というパレットも、"
        "それを探すときのタグも同じです。",
        "279개의 색 이름과 160개의 엄선 팔레트는 설명과 검색 태그까지, 앱이 나오는 모든 언어에 "
        "존재합니다. 한국어로 쓰면 온통 한국어인 화면 한가운데에 Midnight Blue가 남는 대신 한밤의 "
        "파랑이 됩니다. 반 고흐의 소용돌이치는 밤 그림이라고 설명된 별이 빛나는 밤이라는 팔레트도, "
        "그것을 찾을 때 쓰는 태그도 마찬가지입니다.",
        "Alle 279 kleurnamen en alle 160 samengestelde paletten, met hun beschrijvingen en hun "
        "zoeklabels, bestaan in elke taal waarin de app uitkomt. Wie hem in het Nederlands "
        "gebruikt krijgt Middernachtblauw, en niet Midnight Blue midden in een verder Nederlandse "
        "interface. Dat geldt ook voor het palet Sterrennacht, omschreven als van Goghs "
        "kolkende nachtstuk, en voor de labels waarmee je het zou zoeken.",
        "Todos os 279 nomes de cor e todas as 160 paletas selecionadas, com suas descrições e suas "
        "etiquetas de busca, existem em todos os idiomas em que o app sai. Quem usa em português "
        "recebe Azul meia-noite, e não Midnight Blue plantado no meio de uma interface no resto em "
        "português. O mesmo vale para a paleta chamada Noite estrelada, descrita como a noite "
        "rodopiante de van Gogh, e para as etiquetas com que você a procuraria.",
        "279 个色名和 160 套精选调色板，连同它们的说明和搜索标签，"
        "在这款应用发布的每一种语言里都存在。用简体中文的人得到的是午夜蓝，"
        "而不是一片中文界面中间夹着的 Midnight Blue。"
        "那套叫星月夜、说明为凡·高旋转的夜色的调色板是这样，"
        "你用来搜它的标签也是这样。"),
    "Search understands both at once, which matters more than it sounds: if you first met a\n      palette as Ocean Sunrise, in a tutorial or a screenshot, it is still there under that name no\n      matter which language you now run the app in. Translation adds a way to find something. It\n      never takes one away.": (
        "Die Suche versteht beides zugleich, was wichtiger ist, als es klingt: Wenn Ihnen eine "
        "Palette zuerst als Ocean Sunrise begegnet ist, in einer Anleitung oder auf einem "
        "Screenshot, ist sie unter diesem Namen weiter da, egal in welcher Sprache Sie die App "
        "jetzt benutzen. Übersetzung fügt einen Weg hinzu, etwas zu finden. Sie nimmt nie einen "
        "weg.",
        "La búsqueda entiende los dos a la vez, y eso importa más de lo que parece: si conociste "
        "una paleta como Ocean Sunrise, en un tutorial o en una captura, sigue estando ahí con ese "
        "nombre sea cual sea el idioma en el que ahora uses la app. Traducir añade una manera de "
        "encontrar algo. Nunca quita ninguna.",
        "La búsqueda entiende los dos a la vez, y eso importa más de lo que parece: si conociste "
        "una paleta como Ocean Sunrise, en un tutorial o en una captura, sigue estando ahí con ese "
        "nombre sea cual sea el idioma en el que ahora uses la app. Traducir añade una manera de "
        "encontrar algo. Nunca quita ninguna.",
        "La recherche comprend les deux à la fois, et cela compte plus qu'il n'y paraît : si vous "
        "avez d'abord rencontré une palette sous le nom Ocean Sunrise, dans un tutoriel ou sur une "
        "capture, elle est toujours là sous ce nom quelle que soit la langue dans laquelle vous "
        "utilisez maintenant l'application. Traduire ajoute une façon de trouver quelque chose. "
        "Cela n'en retire jamais aucune.",
        "La ricerca capisce entrambi insieme, e conta più di quanto sembri: se hai conosciuto una "
        "palette come Ocean Sunrise, in un tutorial o in uno screenshot, è ancora lì con quel nome "
        "qualunque sia la lingua in cui usi ora l'app. Tradurre aggiunge un modo per trovare "
        "qualcosa. Non ne toglie mai uno.",
        "検索は両方を同時に理解します。これは聞こえる以上に大事なことです。あるパレットに最初に "
        "Ocean Sunrise という名前で出会ったのなら、チュートリアルでもスクリーンショットでも、"
        "いま何語でアプリを使っていてもその名前でちゃんとそこにあります。翻訳は見つけ方を"
        "増やすものであって、減らすものではありません。",
        "검색은 둘을 동시에 이해합니다. 이는 들리는 것보다 중요합니다. 어떤 팔레트를 튜토리얼이나 "
        "스크린샷에서 Ocean Sunrise라는 이름으로 처음 만났다면, 지금 앱을 어떤 언어로 쓰고 있든 그 "
        "이름으로 그대로 거기 있습니다. 번역은 무언가를 찾는 길을 하나 더합니다. 결코 하나를 "
        "빼앗지 않습니다.",
        "De zoekfunctie begrijpt beide tegelijk, en dat doet er meer toe dan het klinkt: als je een "
        "palet eerst als Ocean Sunrise tegenkwam, in een tutorial of op een schermafbeelding, staat "
        "het er nog steeds onder die naam, in welke taal je de app nu ook gebruikt. Vertalen voegt "
        "een manier toe om iets te vinden. Het neemt er nooit een weg.",
        "A busca entende os dois ao mesmo tempo, e isso importa mais do que parece: se você "
        "conheceu uma paleta como Ocean Sunrise, num tutorial ou numa captura, ela continua ali "
        "com esse nome seja qual for o idioma em que você usa o app agora. Traduzir acrescenta um "
        "jeito de encontrar algo. Nunca tira nenhum.",
        "搜索同时认得两者，这比听上去更要紧：如果你最初是在教程或截图里"
        "以 Ocean Sunrise 认识某套调色板的，那么无论你现在用哪种语言，"
        "它都还在那个名字下面。翻译是多给了一条找到东西的路，从不拿走任何一条。"),
    "quietly, it respects you": (
        "im Stillen respektiert es Sie", "sin ruido, te respeta", "sin ruido, te respeta",
        "discrètement, elle vous respecte", "in silenzio, ti rispetta", "静かに、あなたを尊重します",
        "조용히, 당신을 존중합니다", "stilletjes respecteert het je",
        "sem alarde, ele respeita você", "它安静地尊重你"),
    "No account": (
        "Kein Konto", "Sin cuenta", "Sin cuenta", "Pas de compte", "Nessun account",
        "アカウント不要", "계정 없음", "Geen account", "Sem conta", "无需账号"),
    "Nothing to sign up for. Open it and it works.": (
        "Nichts zum Anmelden. Öffnen, und es läuft.",
        "Nada a lo que registrarse. La abres y funciona.",
        "Nada a lo que registrarse. La abres y funciona.",
        "Rien à quoi s'inscrire. Vous l'ouvrez et elle marche.",
        "Niente a cui iscriversi. La apri e funziona.",
        "登録するものは何もありません。開けば動きます。",
        "가입할 것이 없습니다. 열면 작동합니다.",
        "Nergens voor aanmelden. Je opent hem en hij werkt.",
        "Nada para se cadastrar. Você abre e funciona.",
        "没有什么要注册的。打开就能用。"),
    "Works offline": (
        "Funktioniert offline", "Funciona sin conexión", "Funciona sin conexión",
        "Fonctionne hors ligne", "Funziona offline", "オフラインで動作", "오프라인에서 작동",
        "Werkt offline", "Funciona off-line", "离线可用"),
    "Every part of it, including extracting colors from a photo.": (
        "Jeder Teil davon, auch das Herausziehen von Farben aus einem Foto.",
        "Todas sus partes, incluida la extracción de colores de una foto.",
        "Todas sus partes, incluida la extracción de colores de una foto.",
        "Toutes ses parties, y compris l'extraction de couleurs depuis une photo.",
        "Ogni sua parte, compresa l'estrazione dei colori da una foto.",
        "写真から色を抜き出すところも含めて、すべての部分が。",
        "사진에서 색을 뽑아내는 부분까지, 전부.",
        "Elk onderdeel ervan, ook het extraheren van kleuren uit een foto.",
        "Todas as suas partes, inclusive a extração de cores de uma foto.",
        "每一处都能，包括从照片里提取颜色。"),
    "Photos stay put": (
        "Fotos bleiben, wo sie sind", "Las fotos se quedan donde están",
        "Las fotos se quedan donde están", "Les photos restent où elles sont",
        "Le foto restano dove sono", "写真はそのまま", "사진은 그대로",
        "Foto's blijven waar ze zijn", "As fotos ficam onde estão", "照片留在原处"),
    "Color extraction runs on the device. Your pictures are never uploaded anywhere.": (
        "Die Farbextraktion läuft auf dem Gerät. Ihre Bilder werden nirgendwohin hochgeladen.",
        "La extracción de color se hace en el dispositivo. Tus imágenes no se suben a ninguna "
        "parte.",
        "La extracción de color se hace en el dispositivo. Tus imágenes no se suben a ninguna "
        "parte.",
        "L'extraction des couleurs se fait sur l'appareil. Vos images ne sont envoyées nulle part.",
        "L'estrazione dei colori avviene sul dispositivo. Le tue immagini non vengono caricate da "
        "nessuna parte.",
        "色の抽出は端末の中で行われます。あなたの画像がどこかへ送られることはありません。",
        "색 추출은 기기 안에서 이뤄집니다. 당신의 사진은 어디로도 올라가지 않습니다.",
        "Kleurextractie gebeurt op het apparaat. Je afbeeldingen worden nergens heen geüpload.",
        "A extração de cores acontece no dispositivo. Suas imagens não são enviadas para lugar "
        "nenhum.",
        "取色在设备上完成。你的图片不会被上传到任何地方。"),
    "No tracking, no ads": (
        "Kein Tracking, keine Werbung", "Sin rastreo, sin anuncios", "Sin rastreo, sin anuncios",
        "Pas de pistage, pas de publicité", "Nessun tracciamento, nessuna pubblicità",
        "追跡なし、広告なし", "추적 없음, 광고 없음", "Geen tracking, geen advertenties",
        "Sem rastreamento, sem anúncios", "不追踪，不投广告"),
    "No advertising, no analytics, no data collection of any kind.": (
        "Keine Werbung, keine Analyse, keinerlei Datenerhebung.",
        "Ni publicidad, ni analíticas, ni recogida de datos de ningún tipo.",
        "Ni publicidad, ni analíticas, ni recolección de datos de ningún tipo.",
        "Pas de publicité, pas d'analytique, aucune collecte de données d'aucune sorte.",
        "Nessuna pubblicità, nessuna analisi, nessuna raccolta di dati di alcun tipo.",
        "広告も、解析も、いかなるデータ収集もありません。",
        "광고도, 분석도, 어떤 종류의 데이터 수집도 없습니다.",
        "Geen advertenties, geen analytics, geen enkele vorm van gegevensverzameling.",
        "Sem publicidade, sem analytics, sem coleta de dados de nenhum tipo.",
        "没有广告，没有分析统计，没有任何形式的数据收集。"),
    "iCloud sync": (
        "iCloud-Sync", "Sincronización con iCloud", "Sincronización con iCloud",
        "Synchronisation iCloud", "Sincronizzazione iCloud", "iCloud 同期", "iCloud 동기화",
        "iCloud-synchronisatie", "Sincronização com iCloud", "iCloud 同步"),
    "Palettes and folders follow you between your own devices, through your private database.": (
        "Paletten und Ordner folgen Ihnen zwischen Ihren eigenen Geräten, über Ihre private "
        "Datenbank.",
        "Las paletas y las carpetas te siguen entre tus propios dispositivos, a través de tu base "
        "de datos privada.",
        "Las paletas y las carpetas te siguen entre tus propios dispositivos, a través de tu base "
        "de datos privada.",
        "Les palettes et les dossiers vous suivent entre vos propres appareils, via votre base de "
        "données privée.",
        "Le palette e le cartelle ti seguono tra i tuoi dispositivi, attraverso il tuo database "
        "privato.",
        "パレットとフォルダは、あなた自身のプライベートなデータベースを通って、"
        "あなたの端末のあいだをついてきます。",
        "팔레트와 폴더는 당신의 비공개 데이터베이스를 통해 당신의 기기 사이를 따라다닙니다.",
        "Paletten en mappen volgen je tussen je eigen apparaten, via je privédatabase.",
        "As paletas e as pastas seguem você entre os seus próprios dispositivos, pelo seu banco de "
        "dados privado.",
        "调色板和文件夹会通过你自己的私有数据库，在你的设备之间跟着你走。"),
    "iPhone and iPad": (
        "iPhone und iPad", "iPhone y iPad", "iPhone y iPad", "iPhone et iPad", "iPhone e iPad",
        "iPhone と iPad", "iPhone과 iPad", "iPhone en iPad", "iPhone e iPad", "iPhone 和 iPad"),
    "iOS 17.2 or later. One purchase covers both.": (
        "iOS 17.2 oder neuer. Ein Kauf deckt beides ab.",
        "iOS 17.2 o posterior. Una compra cubre los dos.",
        "iOS 17.2 o posterior. Una compra cubre los dos.",
        "iOS 17.2 ou version ultérieure. Un seul achat couvre les deux.",
        "iOS 17.2 o successivo. Un solo acquisto copre entrambi.",
        "iOS 17.2 以降。ひとつの購入で両方に使えます。",
        "iOS 17.2 이상. 한 번의 구매로 둘 다 씁니다.",
        "iOS 17.2 of nieuwer. Eén aankoop dekt beide.",
        "iOS 17.2 ou posterior. Uma compra cobre os dois.",
        "iOS 17.2 或更新版本。买一次，两边都能用。"),
    "questions": (
        "Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問", "질문",
        "Vragen", "Perguntas", "常见问题"),
    "What is the difference between the RGB and RYB color wheels?": (
        "Was ist der Unterschied zwischen dem RGB- und dem RYB-Farbkreis?",
        "¿Cuál es la diferencia entre las ruedas de color RGB y RYB?",
        "¿Cuál es la diferencia entre las ruedas de color RGB y RYB?",
        "Quelle est la différence entre les roues chromatiques RVB et RJB ?",
        "Qual è la differenza tra la ruota dei colori RGB e quella RYB?",
        "RGB のカラーホイールと RYB のカラーホイールは何が違うのですか。",
        "RGB 색상환과 RYB 색상환은 무엇이 다른가요?",
        "Wat is het verschil tussen het RGB- en het RYB-kleurenwiel?",
        "Qual é a diferença entre as rodas de cores RGB e RYB?",
        "RGB 色轮和 RYB 色轮有什么区别？"),
    "RGB is how a screen mixes light, so the complement of red is cyan. RYB is the wheel taught\n        in art schools and refined by Johannes Itten at the Bauhaus, where the complement of red is\n        green. Neither is wrong; they answer different questions. A palette that looks balanced on\n        one can look lopsided on the other, so you get both and can switch between them on the same\n        color.": (
        "RGB ist die Art, wie ein Bildschirm Licht mischt, also ist die Komplementärfarbe von Rot "
        "Cyan. RYB ist der Kreis, der an Kunsthochschulen gelehrt und von Johannes Itten am "
        "Bauhaus verfeinert wurde, dort ist die Komplementärfarbe von Rot Grün. Keiner von beiden "
        "ist falsch; sie beantworten verschiedene Fragen. Eine Palette, die auf dem einen "
        "ausgewogen aussieht, kann auf dem anderen schief wirken, deshalb bekommen Sie beide und "
        "können bei derselben Farbe zwischen ihnen wechseln.",
        "RGB es cómo una pantalla mezcla la luz, así que el complementario del rojo es el cian. "
        "RYB es la rueda que se enseña en las escuelas de arte y que Johannes Itten refinó en la "
        "Bauhaus, donde el complementario del rojo es el verde. Ninguna es incorrecta; responden a "
        "preguntas distintas. Una paleta que se ve equilibrada en una puede verse desequilibrada "
        "en la otra, así que tienes las dos y puedes alternar entre ellas sobre el mismo color.",
        "RGB es cómo una pantalla mezcla la luz, así que el complementario del rojo es el cian. "
        "RYB es la rueda que se enseña en las escuelas de arte y que Johannes Itten refinó en la "
        "Bauhaus, donde el complementario del rojo es el verde. Ninguna es incorrecta; responden a "
        "preguntas distintas. Una paleta que se ve equilibrada en una puede verse desequilibrada "
        "en la otra, así que tienes las dos y puedes alternar entre ellas sobre el mismo color.",
        "RVB, c'est la façon dont un écran mélange la lumière, donc le complémentaire du rouge est "
        "le cyan. RJB est la roue enseignée dans les écoles d'art et affinée par Johannes Itten au "
        "Bauhaus, où le complémentaire du rouge est le vert. Aucune n'est fausse ; elles répondent "
        "à des questions différentes. Une palette qui paraît équilibrée sur l'une peut paraître "
        "bancale sur l'autre, vous avez donc les deux et vous pouvez basculer de l'une à l'autre "
        "sur la même couleur.",
        "RGB è il modo in cui uno schermo mescola la luce, quindi il complementare del rosso è il "
        "ciano. RYB è la ruota insegnata nelle scuole d'arte e affinata da Johannes Itten al "
        "Bauhaus, dove il complementare del rosso è il verde. Nessuna delle due è sbagliata; "
        "rispondono a domande diverse. Una palette che su una sembra equilibrata può sembrare "
        "sbilanciata sull'altra, quindi le hai entrambe e puoi passare dall'una all'altra sullo "
        "stesso colore.",
        "RGB は画面が光を混ぜるやり方で、そこでは赤の補色はシアンです。RYB は美術学校で教えられ、"
        "Bauhaus で Johannes Itten が磨き上げたホイールで、そこでは赤の補色は緑です。"
        "どちらも間違いではなく、違う問いに答えています。一方で釣り合って見えるパレットが"
        "もう一方では偏って見えることがあるので、両方を用意し、同じ色のまま切り替えられます。",
        "RGB는 화면이 빛을 섞는 방식이라 빨강의 보색이 사이언입니다. RYB는 미술학교에서 가르치고 "
        "Johannes Itten이 Bauhaus에서 다듬은 색상환이라 빨강의 보색이 초록입니다. 어느 쪽도 틀리지 "
        "않았고, 서로 다른 질문에 답할 뿐입니다. 한쪽에서 균형 있어 보이는 팔레트가 다른 쪽에서는 "
        "쏠려 보일 수 있어서, 둘 다 제공하고 같은 색에서 서로 오갈 수 있게 했습니다.",
        "RGB is hoe een scherm licht mengt, dus de tegenhanger van rood is cyaan. RYB is het wiel "
        "dat op kunstacademies wordt onderwezen en door Johannes Itten aan het Bauhaus is "
        "verfijnd, waar de tegenhanger van rood groen is. Geen van beide is fout; ze beantwoorden "
        "verschillende vragen. Een palet dat op het ene in balans lijkt, kan op het andere scheef "
        "ogen, dus je krijgt ze allebei en kunt er bij dezelfde kleur tussen wisselen.",
        "RGB é como uma tela mistura luz, então o complementar do vermelho é o ciano. RYB é a roda "
        "ensinada nas escolas de arte e refinada por Johannes Itten na Bauhaus, onde o "
        "complementar do vermelho é o verde. Nenhuma está errada; elas respondem a perguntas "
        "diferentes. Uma paleta que parece equilibrada numa pode parecer torta na outra, então "
        "você tem as duas e pode alternar entre elas na mesma cor.",
        "RGB 是屏幕相加混合光的方式，所以红色的补色是青色。"
        "RYB 是美术院校教授、由 Johannes Itten 在 Bauhaus 精炼过的色轮，其中红色的补色是绿色。"
        "两者都不算错，它们回答的是不同的问题。"
        "在其中一个上看着平衡的调色板，在另一个上可能就偏了，"
        "所以两个都给你，并且可以在同一个颜色上来回切换。"),
    "Does Harmony Palette check color contrast for accessibility?": (
        "Prüft Harmony Palette den Farbkontrast für die Barrierefreiheit?",
        "¿Harmony Palette comprueba el contraste de color para accesibilidad?",
        "¿Harmony Palette verifica el contraste de color para accesibilidad?",
        "Harmony Palette vérifie-t-elle le contraste des couleurs pour l'accessibilité ?",
        "Harmony Palette controlla il contrasto dei colori per l'accessibilità?",
        "Harmony Palette はアクセシビリティのために色のコントラストを確認しますか。",
        "Harmony Palette가 접근성을 위한 색 대비를 검사하나요?",
        "Controleert Harmony Palette het kleurcontrast voor toegankelijkheid?",
        "O Harmony Palette verifica o contraste de cor para acessibilidade?",
        "Harmony Palette 会为无障碍检查颜色对比度吗？"),
    "Yes. It reports the WCAG 2.1 contrast ratio for any foreground and background pair and\n        grades it AA and AAA for normal and large text. If a pair falls short it can adjust the last\n        color you touched until it reaches 4.5:1. It also shows how a palette reads under\n        protanopia, deuteranopia, tritanopia and achromatopsia.": (
        "Ja. Sie nennt für jedes Paar aus Vorder- und Hintergrund das WCAG 2.1 Kontrastverhältnis "
        "und bewertet es mit AA und AAA für normalen und großen Text. Reicht ein Paar nicht, kann "
        "sie die zuletzt angefasste Farbe nachziehen, bis 4.5:1 erreicht ist. Sie zeigt außerdem, "
        "wie eine Palette bei Protanopie, Deuteranopie, Tritanopie und Achromatopsie wirkt.",
        "Sí. Da la relación de contraste WCAG 2.1 de cualquier par de primer plano y fondo y la "
        "califica AA y AAA para texto normal y grande. Si un par se queda corto, puede ajustar el "
        "último color que tocaste hasta llegar a 4.5:1. También muestra cómo se lee una paleta con "
        "protanopia, deuteranopia, tritanopia y acromatopsia.",
        "Sí. Da la relación de contraste WCAG 2.1 de cualquier par de primer plano y fondo y la "
        "califica AA y AAA para texto normal y grande. Si un par se queda corto, puede ajustar el "
        "último color que tocaste hasta llegar a 4.5:1. También muestra cómo se lee una paleta con "
        "protanopia, deuteranopia, tritanopia y acromatopsia.",
        "Oui. Elle donne le rapport de contraste WCAG 2.1 de n'importe quel couple premier plan et "
        "arrière-plan et le note AA et AAA pour le texte normal et le grand texte. Si un couple "
        "est insuffisant, elle peut ajuster la dernière couleur touchée jusqu'à atteindre 4.5:1. "
        "Elle montre aussi comment une palette se lit sous protanopie, deutéranopie, tritanopie et "
        "achromatopsie.",
        "Sì. Indica il rapporto di contrasto WCAG 2.1 di qualsiasi coppia di primo piano e sfondo "
        "e lo valuta AA e AAA per il testo normale e quello grande. Se una coppia non basta, può "
        "regolare l'ultimo colore che hai toccato fino a raggiungere 4.5:1. Mostra anche come si "
        "legge una palette sotto protanopia, deuteranopia, tritanopia e acromatopsia.",
        "はい。前景と背景のどの組み合わせについても WCAG 2.1 のコントラスト比を示し、"
        "通常の文字と大きな文字について AA と AAA を判定します。基準に届かない場合は、"
        "最後に触った色を 4.5:1 に届くまで調整できます。1 型色覚、2 型色覚、3 型色覚、"
        "全色盲でパレットがどう見えるかも示します。",
        "네. 전경과 배경의 어떤 조합에 대해서도 WCAG 2.1 명도 대비를 알려주고, 일반 텍스트와 큰 "
        "텍스트에 대해 AA와 AAA로 매깁니다. 기준에 못 미치면 마지막에 만진 색을 4.5:1에 닿을 "
        "때까지 조정할 수 있습니다. 적색맹, 녹색맹, 청색맹, 전색맹에서 팔레트가 어떻게 보이는지도 "
        "보여줍니다.",
        "Ja. Het geeft de WCAG 2.1 contrastverhouding van elk voorgrond- en achtergrondpaar en "
        "beoordeelt die met AA en AAA voor gewone en grote tekst. Schiet een paar tekort, dan kan "
        "het de laatst aangeraakte kleur bijstellen tot 4.5:1 is bereikt. Het laat ook zien hoe "
        "een palet leest bij protanopie, deuteranopie, tritanopie en achromatopsie.",
        "Sim. Ele informa a relação de contraste WCAG 2.1 de qualquer par de primeiro plano e "
        "fundo e a classifica em AA e AAA para texto normal e grande. Se um par não alcançar, ele "
        "pode ajustar a última cor que você tocou até chegar a 4.5:1. Ele também mostra como uma "
        "paleta se lê sob protanopia, deuteranopia, tritanopia e acromatopsia.",
        "会。对任意一组前景色与背景色，它都会给出 WCAG 2.1 的对比度，"
        "并按正文和大字评定 AA 与 AAA。若某一组不达标，"
        "它可以把你最后碰过的那个颜色调到 4.5:1 为止。"
        "它还会显示这套调色板在红色盲、绿色盲、蓝色盲和全色盲下是什么样子。"),
    "Can I export a palette as code?": (
        "Kann ich eine Palette als Code exportieren?", "¿Puedo exportar una paleta como código?",
        "¿Puedo exportar una paleta como código?", "Puis-je exporter une palette en code ?",
        "Posso esportare una palette come codice?", "パレットをコードとして書き出せますか。",
        "팔레트를 코드로 내보낼 수 있나요?", "Kan ik een palet als code exporteren?",
        "Posso exportar uma paleta como código?", "我可以把调色板导出为代码吗？"),
    "Yes. Pro exports ready-to-paste snippets for SwiftUI, UIKit, CSS custom properties and\n        Tailwind, plus multi-page PDF and SVG. The free tier gives you HEX, RGB, HSL and HSV values\n        to copy by hand.": (
        "Ja. Pro exportiert fertig einfügbare Schnipsel für SwiftUI, UIKit, CSS-Custom-Properties "
        "und Tailwind, dazu mehrseitiges PDF und SVG. Die kostenlose Stufe gibt Ihnen HEX-, RGB-, "
        "HSL- und HSV-Werte zum Abschreiben.",
        "Sí. Pro exporta fragmentos listos para pegar para SwiftUI, UIKit, propiedades "
        "personalizadas de CSS y Tailwind, además de PDF de varias páginas y SVG. El nivel "
        "gratuito te da valores HEX, RGB, HSL y HSV para copiar a mano.",
        "Sí. Pro exporta fragmentos listos para pegar para SwiftUI, UIKit, propiedades "
        "personalizadas de CSS y Tailwind, además de PDF de varias páginas y SVG. El nivel "
        "gratuito te da valores HEX, RGB, HSL y HSV para copiar a mano.",
        "Oui. Pro exporte des extraits prêts à coller pour SwiftUI, UIKit, les propriétés "
        "personnalisées CSS et Tailwind, plus du PDF multipage et du SVG. La formule gratuite vous "
        "donne les valeurs HEX, RVB, TSL et TSV à recopier à la main.",
        "Sì. Pro esporta frammenti pronti da incollare per SwiftUI, UIKit, proprietà "
        "personalizzate CSS e Tailwind, più PDF multipagina e SVG. Il livello gratuito ti dà i "
        "valori HEX, RGB, HSL e HSV da copiare a mano.",
        "はい。Pro は SwiftUI、UIKit、CSS のカスタムプロパティ、Tailwind 用の、"
        "そのまま貼り付けられる断片を書き出します。複数ページの PDF と SVG も出せます。"
        "無料の範囲では HEX、RGB、HSL、HSV の値を手で写せます。",
        "네. Pro는 SwiftUI, UIKit, CSS 커스텀 프로퍼티, Tailwind용으로 바로 붙여 넣을 수 있는 "
        "조각을 내보내고, 여러 쪽짜리 PDF와 SVG도 냅니다. 무료 등급에서는 HEX, RGB, HSL, HSV 값을 "
        "손으로 옮겨 적을 수 있습니다.",
        "Ja. Pro exporteert kant-en-klare snippets voor SwiftUI, UIKit, CSS custom properties en "
        "Tailwind, plus meerpagina-PDF en SVG. De gratis laag geeft je HEX-, RGB-, HSL- en "
        "HSV-waarden om met de hand over te nemen.",
        "Sim. O Pro exporta trechos prontos para colar para SwiftUI, UIKit, propriedades "
        "personalizadas de CSS e Tailwind, além de PDF de várias páginas e SVG. O nível gratuito "
        "te dá valores HEX, RGB, HSL e HSV para copiar à mão.",
        "可以。Pro 会导出可直接粘贴的 SwiftUI、UIKit、CSS 自定义属性和 Tailwind 代码片段，"
        "还有多页 PDF 和 SVG。免费版给你 HEX、RGB、HSL 和 HSV 数值，可以手抄。"),
    "Is Harmony Palette free?": (
        "Ist Harmony Palette kostenlos?", "¿Harmony Palette es gratis?",
        "¿Harmony Palette es gratis?", "Harmony Palette est-elle gratuite ?",
        "Harmony Palette è gratis?", "Harmony Palette は無料ですか。",
        "Harmony Palette는 무료인가요?", "Is Harmony Palette gratis?",
        "O Harmony Palette é grátis?", "Harmony Palette 免费吗？"),
    "The free tier is a real tool rather than a demo: the full wheel, four harmony types, up to\n        fifteen saved palettes and color extraction from photos. Pro adds the other four harmonies,\n        unlimited palettes, the curated library, the accessibility suite and the export formats, at\n        $2.99 a month or $14.99 a year with a seven day trial, or $29.99 once.": (
        "Die kostenlose Stufe ist ein echtes Werkzeug und keine Demo: der ganze Kreis, vier "
        "Harmonietypen, bis zu fünfzehn gespeicherte Paletten und Farbextraktion aus Fotos. Pro "
        "ergänzt die anderen vier Harmonien, unbegrenzt Paletten, die kuratierte Bibliothek, die "
        "Barrierefreiheits-Werkzeuge und die Exportformate, für $2.99 im Monat oder $14.99 im Jahr "
        "mit sieben Tagen zum Ausprobieren, oder $29.99 einmalig.",
        "El nivel gratuito es una herramienta de verdad y no una demo: la rueda entera, cuatro "
        "tipos de armonía, hasta quince paletas guardadas y extracción de color de fotos. Pro "
        "añade las otras cuatro armonías, paletas sin límite, la biblioteca seleccionada, las "
        "herramientas de accesibilidad y los formatos de exportación, por $2.99 al mes o $14.99 al "
        "año con siete días de prueba, o $29.99 una sola vez.",
        "El nivel gratuito es una herramienta de verdad y no una demo: la rueda entera, cuatro "
        "tipos de armonía, hasta quince paletas guardadas y extracción de color de fotos. Pro "
        "agrega las otras cuatro armonías, paletas sin límite, la biblioteca seleccionada, las "
        "herramientas de accesibilidad y los formatos de exportación, por $2.99 al mes o $14.99 al "
        "año con siete días de prueba, o $29.99 una sola vez.",
        "La formule gratuite est un vrai outil et non une démo : la roue entière, quatre types "
        "d'harmonie, jusqu'à quinze palettes enregistrées et l'extraction de couleurs depuis des "
        "photos. Pro ajoute les quatre autres harmonies, les palettes sans limite, la bibliothèque "
        "sélectionnée, les outils d'accessibilité et les formats d'export, pour $2.99 par mois ou "
        "$14.99 par an avec sept jours d'essai, ou $29.99 une fois.",
        "Il livello gratuito è uno strumento vero e non una demo: la ruota intera, quattro tipi di "
        "armonia, fino a quindici palette salvate e l'estrazione dei colori dalle foto. Pro "
        "aggiunge le altre quattro armonie, palette senza limite, la libreria selezionata, gli "
        "strumenti di accessibilità e i formati di esportazione, a $2.99 al mese o $14.99 all'anno "
        "con sette giorni di prova, oppure $29.99 una volta sola.",
        "無料の範囲はデモではなく本物の道具です。ホイールのすべて、4 種類の調和、"
        "保存できるパレット 15 まで、写真からの色の抽出。Pro は残り 4 種類の調和、"
        "無制限のパレット、厳選ライブラリ、アクセシビリティの道具、書き出し形式を加えます。"
        "月 $2.99 または年 $14.99 で 7 日間試せます。$29.99 の買い切りもあります。",
        "무료 등급은 데모가 아니라 진짜 도구입니다. 색상환 전부, 4가지 조화, 저장 팔레트 열다섯 "
        "개까지, 그리고 사진에서 색 추출. Pro는 나머지 4가지 조화, 무제한 팔레트, 엄선된 "
        "라이브러리, 접근성 도구, 내보내기 형식을 더합니다. 월 $2.99 또는 연 $14.99에 7일 시험 "
        "사용이 딸려 있고, $29.99 한 번도 있습니다.",
        "De gratis laag is een echt gereedschap en geen demo: het hele wiel, vier harmonietypes, "
        "tot vijftien bewaarde paletten en kleurextractie uit foto's. Pro voegt de andere vier "
        "harmonieën toe, onbeperkt paletten, de samengestelde bibliotheek, het "
        "toegankelijkheidsgereedschap en de exportformaten, voor $2.99 per maand of $14.99 per "
        "jaar met zeven dagen proef, of $29.99 eenmalig.",
        "O nível gratuito é uma ferramenta de verdade e não uma demo: a roda inteira, quatro tipos "
        "de harmonia, até quinze paletas salvas e extração de cores de fotos. O Pro acrescenta as "
        "outras quatro harmonias, paletas sem limite, a biblioteca selecionada, as ferramentas de "
        "acessibilidade e os formatos de exportação, por $2.99 por mês ou $14.99 por ano com sete "
        "dias de teste, ou $29.99 uma vez só.",
        "免费版是真正的工具，不是演示：完整色轮、4 种配色关系、最多十五套已存调色板，"
        "以及从照片提取颜色。Pro 增加另外 4 种配色关系、不限量的调色板、精选库、"
        "无障碍工具和各种导出格式，每月 $2.99 或每年 $14.99，带七天试用，"
        "也可以 $29.99 一次买断。"),
    "Does it work offline, and does it collect any data?": (
        "Funktioniert es offline, und erhebt es Daten?",
        "¿Funciona sin conexión y recoge algún dato?",
        "¿Funciona sin conexión y recolecta algún dato?",
        "Fonctionne-t-elle hors ligne, et collecte-t-elle des données ?",
        "Funziona offline, e raccoglie dati?",
        "オフラインで動きますか。データを収集しますか。",
        "오프라인에서 작동하나요? 데이터를 수집하나요?",
        "Werkt het offline, en verzamelt het gegevens?",
        "Funciona off-line, e coleta algum dado?",
        "它能离线用吗？会收集数据吗？"),
    "It works entirely offline and there is no account. Photo analysis happens on the device and\n        your pictures are never uploaded. Nothing is tracked, there is no advertising, and no data is\n        collected. If you are signed in to iCloud, palettes and folders sync between your own devices\n        through your private database.": (
        "Es funktioniert vollständig offline und es gibt kein Konto. Die Fotoanalyse geschieht auf "
        "dem Gerät und Ihre Bilder werden nie hochgeladen. Nichts wird verfolgt, es gibt keine "
        "Werbung, und es werden keine Daten erhoben. Wenn Sie bei iCloud angemeldet sind, gleichen "
        "sich Paletten und Ordner über Ihre private Datenbank zwischen Ihren eigenen Geräten ab.",
        "Funciona del todo sin conexión y no hay cuenta. El análisis de las fotos se hace en el "
        "dispositivo y tus imágenes nunca se suben. No se rastrea nada, no hay publicidad y no se "
        "recoge ningún dato. Si has iniciado sesión en iCloud, las paletas y las carpetas se "
        "sincronizan entre tus propios dispositivos a través de tu base de datos privada.",
        "Funciona del todo sin conexión y no hay cuenta. El análisis de las fotos se hace en el "
        "dispositivo y tus imágenes nunca se suben. No se rastrea nada, no hay publicidad y no se "
        "recolecta ningún dato. Si iniciaste sesión en iCloud, las paletas y las carpetas se "
        "sincronizan entre tus propios dispositivos a través de tu base de datos privada.",
        "Elle fonctionne entièrement hors ligne et il n'y a pas de compte. L'analyse des photos se "
        "fait sur l'appareil et vos images ne sont jamais envoyées. Rien n'est pisté, il n'y a pas "
        "de publicité, et aucune donnée n'est collectée. Si vous êtes connecté à iCloud, les "
        "palettes et les dossiers se synchronisent entre vos propres appareils via votre base de "
        "données privée.",
        "Funziona interamente offline e non c'è nessun account. L'analisi delle foto avviene sul "
        "dispositivo e le tue immagini non vengono mai caricate. Non si traccia niente, non c'è "
        "pubblicità e non si raccoglie alcun dato. Se hai fatto l'accesso a iCloud, palette e "
        "cartelle si sincronizzano tra i tuoi dispositivi attraverso il tuo database privato.",
        "完全にオフラインで動き、アカウントはありません。写真の解析は端末の中で行われ、"
        "あなたの画像が送られることはありません。追跡はなく、広告もなく、"
        "データの収集もありません。iCloud にサインインしていれば、"
        "パレットとフォルダはあなたのプライベートなデータベースを通って端末間で同期します。",
        "완전히 오프라인에서 작동하고 계정도 없습니다. 사진 분석은 기기 안에서 이뤄지고 당신의 "
        "사진은 절대 올라가지 않습니다. 아무것도 추적하지 않고, 광고가 없으며, 데이터를 수집하지 "
        "않습니다. iCloud에 로그인해 두었다면 팔레트와 폴더가 당신의 비공개 데이터베이스를 통해 "
        "당신의 기기 사이에서 동기화됩니다.",
        "Het werkt volledig offline en er is geen account. De foto-analyse gebeurt op het apparaat "
        "en je afbeeldingen worden nooit geüpload. Er wordt niets getrackt, er is geen reclame en "
        "er worden geen gegevens verzameld. Als je bij iCloud bent aangemeld, synchroniseren "
        "paletten en mappen tussen je eigen apparaten via je privédatabase.",
        "Funciona inteiramente off-line e não há conta. A análise das fotos acontece no "
        "dispositivo e suas imagens nunca são enviadas. Nada é rastreado, não há publicidade e "
        "nenhum dado é coletado. Se você estiver conectado ao iCloud, paletas e pastas sincronizam "
        "entre os seus próprios dispositivos pelo seu banco de dados privado.",
        "它完全可以离线使用，也没有账号。照片分析在设备上完成，你的图片不会被上传。"
        "不追踪任何东西，没有广告，也不收集数据。"
        "如果你登录了 iCloud，调色板和文件夹会通过你的私有数据库在你自己的设备之间同步。"),
    "What languages does Harmony Palette support?": (
        "Welche Sprachen unterstützt Harmony Palette?", "¿Qué idiomas admite Harmony Palette?",
        "¿Qué idiomas admite Harmony Palette?", "Quelles langues Harmony Palette prend-elle en "
        "charge ?", "Quali lingue supporta Harmony Palette?",
        "Harmony Palette はどの言語に対応していますか。",
        "Harmony Palette는 어떤 언어를 지원하나요?", "Welke talen ondersteunt Harmony Palette?",
        "Quais idiomas o Harmony Palette suporta?", "Harmony Palette 支持哪些语言？"),
    "Eleven: English, German, Spanish, Latin American Spanish, French, Italian, Japanese, Korean,\n        Dutch, Brazilian Portuguese and Simplified Chinese. All 279 color names and all 160 curated\n        palettes are translated too, and search matches both the translated name and the English one.": (
        "Elf: Englisch, Deutsch, Spanisch, lateinamerikanisches Spanisch, Französisch, "
        "Italienisch, Japanisch, Koreanisch, Niederländisch, brasilianisches Portugiesisch und "
        "vereinfachtes Chinesisch. Alle 279 Farbnamen und alle 160 kuratierten Paletten sind "
        "ebenfalls übersetzt, und die Suche findet sowohl den übersetzten als auch den englischen "
        "Namen.",
        "Once: inglés, alemán, español, español de Latinoamérica, francés, italiano, japonés, "
        "coreano, neerlandés, portugués de Brasil y chino simplificado. Los 279 nombres de color y "
        "las 160 paletas seleccionadas también están traducidos, y la búsqueda encuentra tanto el "
        "nombre traducido como el inglés.",
        "Once: inglés, alemán, español, español de Latinoamérica, francés, italiano, japonés, "
        "coreano, neerlandés, portugués de Brasil y chino simplificado. Los 279 nombres de color y "
        "las 160 paletas seleccionadas también están traducidos, y la búsqueda encuentra tanto el "
        "nombre traducido como el inglés.",
        "Onze : anglais, allemand, espagnol, espagnol d'Amérique latine, français, italien, "
        "japonais, coréen, néerlandais, portugais du Brésil et chinois simplifié. Les 279 noms de "
        "couleurs et les 160 palettes sélectionnées sont traduits aussi, et la recherche trouve "
        "aussi bien le nom traduit que l'anglais.",
        "Undici: inglese, tedesco, spagnolo, spagnolo latinoamericano, francese, italiano, "
        "giapponese, coreano, olandese, portoghese brasiliano e cinese semplificato. Anche tutti i "
        "279 nomi di colore e tutte le 160 palette selezionate sono tradotti, e la ricerca trova "
        "sia il nome tradotto sia quello inglese.",
        "11 です。英語、ドイツ語、スペイン語、ラテンアメリカのスペイン語、フランス語、"
        "イタリア語、日本語、韓国語、オランダ語、ブラジルのポルトガル語、簡体字中国語。"
        "279 の色名と 160 の厳選パレットも翻訳されており、"
        "検索は訳された名前と英語の名前のどちらにも一致します。",
        "11개입니다. 영어, 독일어, 스페인어, 라틴아메리카 스페인어, 프랑스어, 이탈리아어, 일본어, "
        "한국어, 네덜란드어, 브라질 포르투갈어, 간체 중국어. 279개의 색 이름과 160개의 엄선 "
        "팔레트도 함께 번역되어 있고, 검색은 번역된 이름과 영어 이름 양쪽에 모두 걸립니다.",
        "Elf: Engels, Duits, Spaans, Latijns-Amerikaans Spaans, Frans, Italiaans, Japans, "
        "Koreaans, Nederlands, Braziliaans Portugees en vereenvoudigd Chinees. Alle 279 "
        "kleurnamen en alle 160 samengestelde paletten zijn ook vertaald, en de zoekfunctie vindt "
        "zowel de vertaalde als de Engelse naam.",
        "Onze: inglês, alemão, espanhol, espanhol da América Latina, francês, italiano, japonês, "
        "coreano, neerlandês, português do Brasil e chinês simplificado. Os 279 nomes de cor e as "
        "160 paletas selecionadas também estão traduzidos, e a busca encontra tanto o nome "
        "traduzido quanto o inglês.",
        "11 种：英语、德语、西班牙语、拉丁美洲西班牙语、法语、意大利语、日语、韩语、荷兰语、"
        "巴西葡萄牙语和简体中文。279 个色名和 160 套精选调色板同样有翻译，"
        "搜索对译名和英文名都能匹配。"),
    "go pick some colors": (
        "gehen Sie Farben aussuchen", "ve a elegir colores", "ve a elegir colores",
        "allez choisir des couleurs", "vai a scegliere dei colori", "さあ、色を選びに",
        "이제 색을 고르러", "ga kleuren uitkiezen", "vá escolher umas cores", "去挑颜色吧"),
    "Free to start, no account, and the wheel is the first thing you see.": (
        "Kostenlos zum Anfangen, kein Konto, und der Kreis ist das Erste, was Sie sehen.",
        "Gratis para empezar, sin cuenta, y la rueda es lo primero que ves.",
        "Gratis para empezar, sin cuenta, y la rueda es lo primero que ves.",
        "Gratuit pour commencer, pas de compte, et la roue est la première chose que vous voyez.",
        "Gratis per iniziare, nessun account, e la ruota è la prima cosa che vedi.",
        "始めるのは無料、アカウントは不要、そして最初に目に入るのはホイールです。",
        "시작은 무료, 계정은 없고, 가장 먼저 보이는 것은 색상환입니다.",
        "Gratis om te beginnen, geen account, en het wiel is het eerste wat je ziet.",
        "Grátis para começar, sem conta, e a roda é a primeira coisa que você vê.",
        "免费上手，无需账号，而且你看到的第一样东西就是色轮。"),
    "More from Levi Foster": (
        "Mehr von Levi Foster", "Más de Levi Foster", "Más de Levi Foster",
        "Plus de Levi Foster", "Altro da Levi Foster", "Levi Foster の他の作品",
        "Levi Foster의 다른 작업", "Meer van Levi Foster", "Mais de Levi Foster",
        "Levi Foster 的其他作品"),
    "A camera that develops a negative instead of filtering the photo.": (
        "Eine Kamera, die ein Negativ entwickelt, statt das Foto zu filtern.",
        "Una cámara que revela un negativo en vez de filtrar la foto.",
        "Una cámara que revela un negativo en vez de filtrar la foto.",
        "Un appareil photo qui développe un négatif au lieu de filtrer la photo.",
        "Una fotocamera che sviluppa un negativo invece di filtrare la foto.",
        "写真にフィルターをかけるのではなく、ネガを現像するカメラ。",
        "사진에 필터를 씌우는 대신 네거티브를 현상하는 카메라.",
        "Een camera die een negatief ontwikkelt in plaats van de foto te filteren.",
        "Uma câmera que revela um negativo em vez de filtrar a foto.",
        "一台冲洗底片、而不是给照片加滤镜的相机。"),
    "Cyanotype prints, worked out from the chemistry of the 1842 process.": (
        "Cyanotypie-Abzüge, aus der Chemie des Verfahrens von 1842 hergeleitet.",
        "Copias en cianotipia, calculadas a partir de la química del proceso de 1842.",
        "Copias en cianotipia, calculadas a partir de la química del proceso de 1842.",
        "Des tirages au cyanotype, calculés à partir de la chimie du procédé de 1842.",
        "Stampe alla cianotipia, ricavate dalla chimica del procedimento del 1842.",
        "1842 年の技法の化学から計算して作るサイアノタイプのプリント。",
        "1842년 공정의 화학에서 계산해 낸 사이아노타입 인화.",
        "Cyanotypie-afdrukken, uitgerekend vanuit de chemie van het proces uit 1842.",
        "Cópias em cianotipia, calculadas a partir da química do processo de 1842.",
        "蓝晒印相，从 1842 年那套工艺的化学一步步算出来。"),
    "Nineteen stackable glitch effects, layered and reordered. Free.": (
        "Neunzehn stapelbare Glitch-Effekte, geschichtet und umsortiert. Kostenlos.",
        "Diecinueve efectos glitch apilables, en capas y reordenables. Gratis.",
        "Diecinueve efectos glitch apilables, en capas y reordenables. Gratis.",
        "Dix-neuf effets glitch empilables, en couches et réordonnables. Gratuit.",
        "Diciannove effetti glitch impilabili, a livelli e riordinabili. Gratis.",
        "重ねられるグリッチ効果が 19 種類。層にして、並べ替えられます。無料。",
        "쌓을 수 있는 글리치 효과 열아홉 가지. 층으로 겹치고 순서를 바꿉니다. 무료.",
        "Negentien stapelbare glitch-effecten, gelaagd en herschikbaar. Gratis.",
        "Dezenove efeitos glitch empilháveis, em camadas e reordenáveis. Grátis.",
        "十九种可叠加的故障效果，分层并可重新排序。免费。"),
    "Privacy": (
        "Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
        "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "Terms": (
        "Nutzungsbedingungen", "Términos", "Términos", "Conditions", "Termini", "利用規約",
        "이용약관", "Voorwaarden", "Termos", "条款"),
    "Support": (
        "Support", "Soporte", "Soporte", "Assistance", "Assistenza", "サポート", "지원",
        "Ondersteuning", "Suporte", "支持"),
    "Built in Fort Worth, Texas.": (
        "Gebaut in Fort Worth, Texas.", "Hecho en Fort Worth, Texas.",
        "Hecho en Fort Worth, Texas.", "Fait à Fort Worth, Texas.",
        "Fatto a Fort Worth, Texas.", "テキサス州 Fort Worth で作っています。",
        "Texas의 Fort Worth에서 만듭니다.", "Gemaakt in Fort Worth, Texas.",
        "Feito em Fort Worth, Texas.", "在 Texas 的 Fort Worth 制作。"),
    "Harmony Palette - Color Harmony & Design Tool": (
        "Harmony Palette - Farbharmonie und Design-Werkzeug",
        "Harmony Palette - Armonía de color y herramienta de diseño",
        "Harmony Palette - Armonía de color y herramienta de diseño",
        "Harmony Palette - Harmonie des couleurs et outil de design",
        "Harmony Palette - Armonia cromatica e strumento di design",
        "Harmony Palette - 配色とデザインの道具",
        "Harmony Palette - 색 조화와 디자인 도구",
        "Harmony Palette - Kleurharmonie en ontwerpgereedschap",
        "Harmony Palette - Harmonia de cores e ferramenta de design",
        "Harmony Palette - 配色与设计工具"),
    "A color harmony and palette app for iPhone and iPad. An interactive color wheel in both the RGB and the traditional RYB model, eight harmony types, 160 curated palettes, a WCAG contrast checker, color blindness simulation, on-device color extraction from photos, and export to PDF, SVG, SwiftUI, UIKit, CSS and Tailwind.": (
        "Eine App für Farbharmonie und Paletten für iPhone und iPad. Ein interaktiver Farbkreis im "
        "RGB- und im traditionellen RYB-Modell, acht Harmonietypen, 160 kuratierte Paletten, ein "
        "WCAG-Kontrastprüfer, Farbenblindheitssimulation, Farbextraktion aus Fotos auf dem Gerät "
        "und Export nach PDF, SVG, SwiftUI, UIKit, CSS und Tailwind.",
        "Una app de armonía de color y paletas para iPhone y iPad. Una rueda de color interactiva "
        "en el modelo RGB y en el RYB tradicional, ocho tipos de armonía, 160 paletas "
        "seleccionadas, un comprobador de contraste WCAG, simulación de daltonismo, extracción de "
        "color de fotos en el dispositivo y exportación a PDF, SVG, SwiftUI, UIKit, CSS y "
        "Tailwind.",
        "Una app de armonía de color y paletas para iPhone y iPad. Una rueda de color interactiva "
        "en el modelo RGB y en el RYB tradicional, ocho tipos de armonía, 160 paletas "
        "seleccionadas, un verificador de contraste WCAG, simulación de daltonismo, extracción de "
        "color de fotos en el dispositivo y exportación a PDF, SVG, SwiftUI, UIKit, CSS y "
        "Tailwind.",
        "Une application d'harmonie des couleurs et de palettes pour iPhone et iPad. Une roue "
        "chromatique interactive dans le modèle RVB et dans le modèle RJB traditionnel, huit types "
        "d'harmonie, 160 palettes sélectionnées, un vérificateur de contraste WCAG, une simulation "
        "du daltonisme, l'extraction de couleurs depuis des photos sur l'appareil, et l'export "
        "vers PDF, SVG, SwiftUI, UIKit, CSS et Tailwind.",
        "Un'app di armonia cromatica e palette per iPhone e iPad. Una ruota dei colori interattiva "
        "nel modello RGB e in quello RYB tradizionale, otto tipi di armonia, 160 palette "
        "selezionate, un controllo del contrasto WCAG, la simulazione del daltonismo, l'estrazione "
        "dei colori dalle foto sul dispositivo e l'esportazione in PDF, SVG, SwiftUI, UIKit, CSS e "
        "Tailwind.",
        "iPhone と iPad のための配色とパレットのアプリ。RGB と伝統的な RYB の両方のモデルによる"
        "対話的なカラーホイール、8 種類の調和、厳選された 160 のパレット、WCAG "
        "コントラストチェッカー、色覚シミュレーション、端末内での写真からの色の抽出、そして "
        "PDF、SVG、SwiftUI、UIKit、CSS、Tailwind への書き出し。",
        "iPhone과 iPad를 위한 색 조화와 팔레트 앱. RGB와 전통적인 RYB 두 모델을 오가는 색상환, "
        "8가지 조화, 엄선된 160개의 팔레트, WCAG 명도 대비 검사기, 색각 이상 시뮬레이션, 기기 "
        "안에서 이뤄지는 사진 색 추출, 그리고 PDF, SVG, SwiftUI, UIKit, CSS, Tailwind로의 "
        "내보내기.",
        "Een app voor kleurharmonie en paletten voor iPhone en iPad. Een interactief kleurenwiel "
        "in zowel het RGB- als het traditionele RYB-model, acht harmonietypes, 160 samengestelde "
        "paletten, een WCAG-contrastchecker, kleurenblindheidssimulatie, kleurextractie uit foto's "
        "op het apparaat, en export naar PDF, SVG, SwiftUI, UIKit, CSS en Tailwind.",
        "Um app de harmonia de cores e paletas para iPhone e iPad. Uma roda de cores interativa no "
        "modelo RGB e no RYB tradicional, oito tipos de harmonia, 160 paletas selecionadas, um "
        "verificador de contraste WCAG, simulação de daltonismo, extração de cores de fotos no "
        "dispositivo, e exportação para PDF, SVG, SwiftUI, UIKit, CSS e Tailwind.",
        "一款为 iPhone 和 iPad 打造的配色与调色板应用。"
        "可在 RGB 与传统 RYB 两种模型之间切换的交互式色轮、8 种配色关系、精选的 160 套调色板、"
        "WCAG 对比度检查器、色觉模拟、在设备上完成的照片取色，"
        "以及导出为 PDF、SVG、SwiftUI、UIKit、CSS 和 Tailwind。"),
    "Interactive color wheel in both RGB and the traditional RYB (Itten) model": (
        "Interaktiver Farbkreis im RGB- und im traditionellen RYB-Modell (Itten)",
        "Rueda de color interactiva en el modelo RGB y en el RYB tradicional (Itten)",
        "Rueda de color interactiva en el modelo RGB y en el RYB tradicional (Itten)",
        "Roue chromatique interactive dans le modèle RVB et dans le modèle RJB traditionnel "
        "(Itten)",
        "Ruota dei colori interattiva nel modello RGB e in quello RYB tradizionale (Itten)",
        "RGB と伝統的な RYB (Itten) の両モデルによる対話的なカラーホイール",
        "RGB와 전통적인 RYB (Itten) 두 모델을 지원하는 대화형 색상환",
        "Interactief kleurenwiel in zowel RGB als het traditionele RYB-model (Itten)",
        "Roda de cores interativa no modelo RGB e no RYB tradicional (Itten)",
        "支持 RGB 与传统 RYB (Itten) 两种模型的交互式色轮"),
    "Eight harmony types: complementary, analogous, monochromatic, triadic, split-complementary, square, rectangular and compound": (
        "Acht Harmonietypen: komplementär, analog, monochrom, triadisch, geteilt komplementär, "
        "quadratisch, rechteckig und zusammengesetzt",
        "Ocho tipos de armonía: complementario, análogo, monocromático, triádico, complementario "
        "dividido, cuadrado, rectangular y compuesto",
        "Ocho tipos de armonía: complementario, análogo, monocromático, triádico, complementario "
        "dividido, cuadrado, rectangular y compuesto",
        "Huit types d'harmonie : complémentaire, analogue, monochrome, triadique, complémentaire "
        "divisé, carré, rectangulaire et composé",
        "Otto tipi di armonia: complementare, analogo, monocromatico, triadico, complementare "
        "diviso, quadrato, rettangolare e composto",
        "8 種類の調和: 補色、類似色、単色、三色、分裂補色、矩形、長方形、複合",
        "8가지 조화: 보색, 유사색, 단색, 삼색, 분할 보색, 사각, 직사각, 복합",
        "Acht harmonietypes: complementair, analoog, monochroom, triadisch, gesplitst "
        "complementair, vierkant, rechthoekig en samengesteld",
        "Oito tipos de harmonia: complementar, análogo, monocromático, triádico, complementar "
        "dividido, quadrado, retangular e composto",
        "8 种配色关系：互补、邻近、单色、三等分、分裂互补、正方、矩形和复合"),
    "160 curated palettes across ten categories, each with search tags": (
        "160 kuratierte Paletten in zehn Kategorien, jede mit Such-Schlagwörtern",
        "160 paletas seleccionadas en diez categorías, cada una con etiquetas de búsqueda",
        "160 paletas seleccionadas en diez categorías, cada una con etiquetas de búsqueda",
        "160 palettes sélectionnées dans dix catégories, chacune avec des mots-clés de recherche",
        "160 palette selezionate in dieci categorie, ognuna con etichette di ricerca",
        "10 のカテゴリーにわたる厳選された 160 のパレット、それぞれに検索タグ付き",
        "열 개 분류에 걸친 엄선된 160개의 팔레트, 각각 검색 태그 포함",
        "160 samengestelde paletten in tien categorieën, elk met zoeklabels",
        "160 paletas selecionadas em dez categorias, cada uma com etiquetas de busca",
        "分布在十个类别中的 160 套精选调色板，每套都带搜索标签"),
    "279 named colors, translated into every language the app ships in": (
        "279 benannte Farben, übersetzt in jede Sprache, in der die App erscheint",
        "279 colores con nombre, traducidos a todos los idiomas en los que sale la app",
        "279 colores con nombre, traducidos a todos los idiomas en los que sale la app",
        "279 couleurs nommées, traduites dans chaque langue où l'application paraît",
        "279 colori con un nome, tradotti in ogni lingua in cui esce l'app",
        "名前の付いた 279 の色、アプリが対応するすべての言語に翻訳済み",
        "이름이 붙은 279개의 색, 앱이 나오는 모든 언어로 번역",
        "279 kleuren met een naam, vertaald in elke taal waarin de app uitkomt",
        "279 cores com nome, traduzidas para todos os idiomas em que o app sai",
        "279 个有名字的颜色，已翻译成这款应用发布的每一种语言"),
    "WCAG 2.1 contrast checker with AA and AAA grades for normal and large text": (
        "WCAG 2.1 Kontrastprüfer mit AA- und AAA-Bewertung für normalen und großen Text",
        "Comprobador de contraste WCAG 2.1 con calificaciones AA y AAA para texto normal y grande",
        "Verificador de contraste WCAG 2.1 con calificaciones AA y AAA para texto normal y grande",
        "Vérificateur de contraste WCAG 2.1 avec notes AA et AAA pour le texte normal et le grand "
        "texte",
        "Controllo del contrasto WCAG 2.1 con valutazioni AA e AAA per il testo normale e quello "
        "grande",
        "通常の文字と大きな文字について AA と AAA を判定する WCAG 2.1 コントラストチェッカー",
        "일반 텍스트와 큰 텍스트에 대해 AA와 AAA를 매기는 WCAG 2.1 명도 대비 검사기",
        "WCAG 2.1 contrastchecker met AA- en AAA-beoordelingen voor gewone en grote tekst",
        "Verificador de contraste WCAG 2.1 com notas AA e AAA para texto normal e grande",
        "按正文和大字评定 AA 与 AAA 的 WCAG 2.1 对比度检查器"),
    "Color blindness simulation for protanopia, deuteranopia, tritanopia and achromatopsia": (
        "Farbenblindheitssimulation für Protanopie, Deuteranopie, Tritanopie und Achromatopsie",
        "Simulación de daltonismo para protanopia, deuteranopia, tritanopia y acromatopsia",
        "Simulación de daltonismo para protanopia, deuteranopia, tritanopia y acromatopsia",
        "Simulation du daltonisme pour la protanopie, la deutéranopie, la tritanopie et "
        "l'achromatopsie",
        "Simulazione del daltonismo per protanopia, deuteranopia, tritanopia e acromatopsia",
        "1 型色覚、2 型色覚、3 型色覚、全色盲の色覚シミュレーション",
        "적색맹, 녹색맹, 청색맹, 전색맹에 대한 색각 이상 시뮬레이션",
        "Kleurenblindheidssimulatie voor protanopie, deuteranopie, tritanopie en achromatopsie",
        "Simulação de daltonismo para protanopia, deuteranopia, tritanopia e acromatopsia",
        "针对红色盲、绿色盲、蓝色盲和全色盲的色觉模拟"),
    "Color extraction from photos using K-means clustering, entirely on device": (
        "Farbextraktion aus Fotos mit K-means-Clustering, vollständig auf dem Gerät",
        "Extracción de color de fotos con agrupamiento K-means, enteramente en el dispositivo",
        "Extracción de color de fotos con agrupamiento K-means, enteramente en el dispositivo",
        "Extraction de couleurs depuis des photos par regroupement K-means, entièrement sur "
        "l'appareil",
        "Estrazione dei colori dalle foto con clustering K-means, interamente sul dispositivo",
        "K-means クラスタリングによる写真からの色の抽出、すべて端末内で",
        "K-means 군집화를 이용한 사진 색 추출, 전부 기기 안에서",
        "Kleurextractie uit foto's met K-means-clustering, volledig op het apparaat",
        "Extração de cores de fotos com agrupamento K-means, inteiramente no dispositivo",
        "使用 K-means 聚类从照片提取颜色，全程在设备上完成"),
    "Export to PDF and SVG, and code for SwiftUI, UIKit, CSS and Tailwind": (
        "Export nach PDF und SVG, und Code für SwiftUI, UIKit, CSS und Tailwind",
        "Exportación a PDF y SVG, y código para SwiftUI, UIKit, CSS y Tailwind",
        "Exportación a PDF y SVG, y código para SwiftUI, UIKit, CSS y Tailwind",
        "Export vers PDF et SVG, et code pour SwiftUI, UIKit, CSS et Tailwind",
        "Esportazione in PDF e SVG, e codice per SwiftUI, UIKit, CSS e Tailwind",
        "PDF と SVG への書き出し、および SwiftUI、UIKit、CSS、Tailwind 用のコード",
        "PDF와 SVG로 내보내기, 그리고 SwiftUI, UIKit, CSS, Tailwind용 코드",
        "Export naar PDF en SVG, en code voor SwiftUI, UIKit, CSS en Tailwind",
        "Exportação para PDF e SVG, e código para SwiftUI, UIKit, CSS e Tailwind",
        "导出为 PDF 和 SVG，以及 SwiftUI、UIKit、CSS 和 Tailwind 代码"),
    "Palettes and folders sync between your own devices through iCloud": (
        "Paletten und Ordner gleichen sich über iCloud zwischen Ihren eigenen Geräten ab",
        "Las paletas y las carpetas se sincronizan entre tus propios dispositivos a través de "
        "iCloud",
        "Las paletas y las carpetas se sincronizan entre tus propios dispositivos a través de "
        "iCloud",
        "Les palettes et les dossiers se synchronisent entre vos propres appareils via iCloud",
        "Palette e cartelle si sincronizzano tra i tuoi dispositivi attraverso iCloud",
        "パレットとフォルダは iCloud を通じてあなたの端末のあいだで同期します",
        "팔레트와 폴더가 iCloud를 통해 당신의 기기 사이에서 동기화됩니다",
        "Paletten en mappen synchroniseren tussen je eigen apparaten via iCloud",
        "Paletas e pastas sincronizam entre os seus próprios dispositivos pelo iCloud",
        "调色板和文件夹通过 iCloud 在你自己的设备之间同步"),
    "Works offline, with no account, no advertising and no data collection": (
        "Funktioniert offline, ohne Konto, ohne Werbung und ohne Datenerhebung",
        "Funciona sin conexión, sin cuenta, sin publicidad y sin recogida de datos",
        "Funciona sin conexión, sin cuenta, sin publicidad y sin recolección de datos",
        "Fonctionne hors ligne, sans compte, sans publicité et sans collecte de données",
        "Funziona offline, senza account, senza pubblicità e senza raccolta di dati",
        "オフラインで動作し、アカウントも広告もデータ収集もなし",
        "오프라인에서 작동하며 계정도, 광고도, 데이터 수집도 없음",
        "Werkt offline, zonder account, zonder reclame en zonder gegevensverzameling",
        "Funciona off-line, sem conta, sem publicidade e sem coleta de dados",
        "离线可用，无账号、无广告、不收集数据"),
    "Pro Monthly": (
        "Pro monatlich", "Pro mensual", "Pro mensual", "Pro mensuel", "Pro mensile",
        "Pro 月額", "Pro 월간", "Pro maandelijks", "Pro mensal", "Pro 月度"),
    "Pro Annual": (
        "Pro jährlich", "Pro anual", "Pro anual", "Pro annuel", "Pro annuale",
        "Pro 年額", "Pro 연간", "Pro jaarlijks", "Pro anual", "Pro 年度"),
    "Pro Lifetime": (
        "Pro auf Dauer", "Pro para siempre", "Pro para siempre", "Pro à vie", "Pro per sempre",
        "Pro 買い切り", "Pro 평생", "Pro voorgoed", "Pro para sempre", "Pro 永久"),
    "Harmony Palette: Color Wheel & Palette App for iPhone and iPad": (
        "Harmony Palette: Farbkreis- und Paletten-App für iPhone und iPad",
        "Harmony Palette: rueda de color y app de paletas para iPhone y iPad",
        "Harmony Palette: rueda de color y app de paletas para iPhone y iPad",
        "Harmony Palette : roue chromatique et application de palettes pour iPhone et iPad",
        "Harmony Palette: ruota dei colori e app di palette per iPhone e iPad",
        "Harmony Palette: iPhone と iPad のためのカラーホイールとパレットアプリ",
        "Harmony Palette: iPhone과 iPad를 위한 색상환과 팔레트 앱",
        "Harmony Palette: kleurenwiel en palet-app voor iPhone en iPad",
        "Harmony Palette: roda de cores e app de paletas para iPhone e iPad",
        "Harmony Palette：为 iPhone 和 iPad 打造的色轮与调色板应用"),
}
