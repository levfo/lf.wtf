"""lf.wtf home page, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Titles and meta descriptions are written for search rather than translated word for word, because
they are the two fields that decide whether the page is found at all. Each carries the local phrase
someone would actually type: Filmsimulation, simulation argentique, フィルムシミュレーション,
胶片模拟.

No em-dashes anywhere, per house style. The English pages had them in their titles and cross
links; those were corrected too, so the separator is a colon on both sides now.
"""

#: Names, handles and marks that are the same in every language.
KEEP = {
    "Levi", "Foster", "Levi Foster", "FRMT", "MODUL8", "CYANO", "MERGE", "lf.wtf",
    "Harmony Palette", "Merge With The Machine", "iPhone", "iPad", "App Store",
    "Instagram", "X", "TikTok", "Etsy", "GitHub", "L@LF.WTF",
}

T = {
    "Levi Foster: iPhone Apps, Photography Tools and Generative Art": (
        "Levi Foster: iPhone-Apps, Fotowerkzeuge und generative Kunst",
        "Levi Foster: apps para iPhone, herramientas de fotografía y arte generativo",
        "Levi Foster: apps para iPhone, herramientas de fotografía y arte generativo",
        "Levi Foster : apps iPhone, outils photo et art génératif",
        "Levi Foster: app per iPhone, strumenti fotografici e arte generativa",
        "Levi Foster｜iPhone アプリ、写真ツール、ジェネラティブアート",
        "Levi Foster｜iPhone 앱, 사진 도구, 제너러티브 아트",
        "Levi Foster: iPhone-apps, fototools en generatieve kunst",
        "Levi Foster: apps para iPhone, ferramentas de fotografia e arte generativa",
        "Levi Foster｜iPhone 应用、摄影工具与生成艺术"),
    "Levi Foster is an independent app developer and artist in Fort Worth, Texas. He makes FRMT "
    "film simulation, MODUL8 glitch art, CYANO cyanotype and Harmony Palette for iPhone, and runs "
    "Merge With The Machine.": (
        "Levi Foster ist unabhängiger App-Entwickler und Künstler in Fort Worth, Texas. Er macht "
        "die Filmsimulation FRMT, die Glitch-Art-App MODUL8, die Cyanotypie-App CYANO und Harmony "
        "Palette für iPhone und betreibt Merge With The Machine.",
        "Levi Foster es desarrollador de apps y artista independiente en Fort Worth, Texas. Hace "
        "la simulación de película FRMT, la app de glitch art MODUL8, la de cianotipia CYANO y "
        "Harmony Palette para iPhone, y lleva Merge With The Machine.",
        "Levi Foster es desarrollador de apps y artista independiente en Fort Worth, Texas. Hace "
        "la simulación de película FRMT, la app de glitch art MODUL8, la de cianotipia CYANO y "
        "Harmony Palette para iPhone, y lleva Merge With The Machine.",
        "Levi Foster est développeur d'apps et artiste indépendant à Fort Worth, au Texas. Il fait "
        "la simulation argentique FRMT, l'app de glitch art MODUL8, l'app de cyanotype CYANO et "
        "Harmony Palette pour iPhone, et mène Merge With The Machine.",
        "Levi Foster è sviluppatore di app e artista indipendente a Fort Worth, Texas. Fa la "
        "simulazione di pellicola FRMT, l'app di glitch art MODUL8, quella di cianotipia CYANO e "
        "Harmony Palette per iPhone, e porta avanti Merge With The Machine.",
        "Levi Foster はテキサス州フォートワースを拠点とする独立系のアプリ開発者であり、"
        "アーティストです。フィルムシミュレーション FRMT、グリッチアート MODUL8、"
        "サイアノタイプ CYANO、Harmony Palette を iPhone 向けに制作し、"
        "Merge With The Machine を運営しています。",
        "Levi Foster는 텍사스주 포트워스에서 활동하는 독립 앱 개발자이자 아티스트입니다. "
        "필름 시뮬레이션 FRMT, 글리치 아트 MODUL8, 사이아노타입 CYANO, Harmony Palette를 "
        "iPhone용으로 만들고 Merge With The Machine을 운영합니다.",
        "Levi Foster is een onafhankelijke app-ontwikkelaar en kunstenaar in Fort Worth, Texas. "
        "Hij maakt de filmsimulatie FRMT, de glitch-art-app MODUL8, de cyanotypie-app CYANO en "
        "Harmony Palette voor iPhone, en runt Merge With The Machine.",
        "Levi Foster é desenvolvedor de apps e artista independente em Fort Worth, Texas. Ele faz "
        "a simulação de filme FRMT, o app de glitch art MODUL8, o de cianotipia CYANO e o Harmony "
        "Palette para iPhone, e toca o Merge With The Machine.",
        "Levi Foster 是一位独立 App 开发者和艺术家，常驻美国得州沃斯堡。他为 iPhone 制作胶片模拟 "
        "FRMT、故障艺术 MODUL8、蓝晒 CYANO 和 Harmony Palette，并经营 Merge With The Machine。"),
    "Independent app developer and artist in Fort Worth, Texas. FRMT film simulation, MODUL8 "
    "glitch art, CYANO cyanotype, Harmony Palette, and Merge With The Machine.": (
        "Unabhängiger App-Entwickler und Künstler in Fort Worth, Texas. Filmsimulation FRMT, "
        "Glitch Art MODUL8, Cyanotypie CYANO, Harmony Palette und Merge With The Machine.",
        "Desarrollador de apps y artista independiente en Fort Worth, Texas. Simulación de "
        "película FRMT, glitch art MODUL8, cianotipia CYANO, Harmony Palette y Merge With The "
        "Machine.",
        "Desarrollador de apps y artista independiente en Fort Worth, Texas. Simulación de "
        "película FRMT, glitch art MODUL8, cianotipia CYANO, Harmony Palette y Merge With The "
        "Machine.",
        "Développeur d'apps et artiste indépendant à Fort Worth, Texas. Simulation argentique "
        "FRMT, glitch art MODUL8, cyanotype CYANO, Harmony Palette et Merge With The Machine.",
        "Sviluppatore di app e artista indipendente a Fort Worth, Texas. Simulazione di pellicola "
        "FRMT, glitch art MODUL8, cianotipia CYANO, Harmony Palette e Merge With The Machine.",
        "テキサス州フォートワース在住の独立系アプリ開発者/アーティスト。フィルムシミュレーション "
        "FRMT、グリッチアート MODUL8、サイアノタイプ CYANO、Harmony Palette、"
        "Merge With The Machine。",
        "텍사스주 포트워스의 독립 앱 개발자이자 아티스트. 필름 시뮬레이션 FRMT, 글리치 아트 "
        "MODUL8, 사이아노타입 CYANO, Harmony Palette, Merge With The Machine.",
        "Onafhankelijke app-ontwikkelaar en kunstenaar in Fort Worth, Texas. Filmsimulatie FRMT, "
        "glitch art MODUL8, cyanotypie CYANO, Harmony Palette en Merge With The Machine.",
        "Desenvolvedor de apps e artista independente em Fort Worth, Texas. Simulação de filme "
        "FRMT, glitch art MODUL8, cianotipia CYANO, Harmony Palette e Merge With The Machine.",
        "常驻得州沃斯堡的独立 App 开发者与艺术家。胶片模拟 FRMT、故障艺术 MODUL8、蓝晒 CYANO、"
        "Harmony Palette，以及 Merge With The Machine。"),
    "An ASCII art portrait of Levi Foster": (
        "Ein ASCII-Art-Porträt von Levi Foster",
        "Un retrato en ASCII art de Levi Foster",
        "Un retrato en ASCII art de Levi Foster",
        "Un portrait en ASCII art de Levi Foster",
        "Un ritratto in ASCII art di Levi Foster",
        "Levi Foster のアスキーアートによる肖像",
        "Levi Foster의 아스키 아트 초상",
        "Een ASCII-artportret van Levi Foster",
        "Um retrato em ASCII art de Levi Foster",
        "Levi Foster 的 ASCII 艺术肖像"),
    "Projects": ("Projekte", "Proyectos", "Proyectos", "Projets", "Progetti", "プロジェクト",
                 "프로젝트", "Projecten", "Projetos", "项目"),
    "ABOUT": ("ÜBER", "ACERCA DE", "ACERCA DE", "À PROPOS", "CHI SONO", "プロフィール", "소개",
              "OVER", "SOBRE", "关于"),
    "Independent app developer and artist": (
        "Unabhängiger App-Entwickler und Künstler",
        "Desarrollador de apps y artista independiente",
        "Desarrollador de apps y artista independiente",
        "Développeur d'apps et artiste indépendant",
        "Sviluppatore di app e artista indipendente",
        "独立系アプリ開発者/アーティスト", "독립 앱 개발자이자 아티스트",
        "Onafhankelijk app-ontwikkelaar en kunstenaar",
        "Desenvolvedor de apps e artista independente", "独立 App 开发者与艺术家"),
    "Fort Worth, Texas": ("Fort Worth, Texas", "Fort Worth, Texas", "Fort Worth, Texas",
                          "Fort Worth, Texas", "Fort Worth, Texas", "テキサス州フォートワース",
                          "텍사스주 포트워스", "Fort Worth, Texas", "Fort Worth, Texas",
                          "美国得州沃斯堡"),
    "I am Levi Foster. I build iPhone apps and make things with code, mostly at the point where\n"
    "      photography stops being a picture and starts being a process. Some of it ships on the "
    "App\n      Store. The rest ends up as prints.": (
        "Ich bin Levi Foster. Ich baue iPhone-Apps und mache Dinge mit Code, meistens genau dort, "
        "wo Fotografie aufhört, ein Bild zu sein, und anfängt, ein Verfahren zu sein. Ein Teil "
        "davon erscheint im App Store. Der Rest endet als Druck.",
        "Soy Levi Foster. Hago apps para iPhone y cosas con código, sobre todo en el punto en el "
        "que la fotografía deja de ser una imagen y pasa a ser un proceso. Parte acaba en la App "
        "Store. El resto acaba en papel.",
        "Soy Levi Foster. Hago apps para iPhone y cosas con código, sobre todo en el punto en el "
        "que la fotografía deja de ser una imagen y pasa a ser un proceso. Parte acaba en la App "
        "Store. El resto acaba impreso.",
        "Je suis Levi Foster. Je fais des apps iPhone et des choses avec du code, surtout à "
        "l'endroit où la photographie cesse d'être une image et devient un procédé. Une partie "
        "sort sur l'App Store. Le reste finit en tirages.",
        "Sono Levi Foster. Faccio app per iPhone e cose con il codice, soprattutto nel punto in "
        "cui la fotografia smette di essere un'immagine e diventa un processo. Una parte esce "
        "sull'App Store. Il resto finisce in stampa.",
        "Levi Foster です。iPhone アプリをつくり、コードでものをつくっています。多くは、"
        "写真が「絵」であることをやめて「工程」になる、その境目のあたりで。"
        "一部は App Store に出し、残りはプリントになります。",
        "저는 Levi Foster입니다. iPhone 앱을 만들고 코드로 무언가를 만듭니다. 대부분은 사진이 "
        "이미지이기를 그만두고 공정이 되는 지점에서요. 일부는 App Store에 내고, 나머지는 "
        "프린트가 됩니다.",
        "Ik ben Levi Foster. Ik bouw iPhone-apps en maak dingen met code, meestal precies daar "
        "waar fotografie ophoudt een plaatje te zijn en een proces wordt. Een deel verschijnt in "
        "de App Store. De rest wordt print.",
        "Sou Levi Foster. Faço apps para iPhone e coisas com código, principalmente no ponto em "
        "que a fotografia deixa de ser uma imagem e passa a ser um processo. Parte sai na App "
        "Store. O resto vira impressão.",
        "我是 Levi Foster。我做 iPhone 应用，也用代码做东西，大多集中在摄影不再是一张画面、"
        "而开始成为一道工序的那个交界处。一部分会上架 App Store，其余的最后变成版画。"),
    # The next four fragments are one sentence broken by inline links, in this fixed order:
    #   [A] FRMT [B] CYANO [C] MODUL8 [D]
    # The links cannot move, so each translation is written to read correctly once assembled. The
    # verb-final languages carry the sentence differently and end on the shared clause.
    "The apps share a bias. I would rather simulate the thing than approximate the look of it,\n"
    "      which is slower and more awkward and gets results a preset cannot. That is the whole "
    "idea\n      behind": (
        "Die Apps teilen eine Neigung. Ich simuliere lieber die Sache selbst, als ihr Aussehen "
        "anzunähern, was langsamer und umständlicher ist und Ergebnisse liefert, zu denen ein "
        "Preset nicht kommt. Das ist der ganze Gedanke hinter",
        "Las apps comparten un sesgo. Prefiero simular la cosa antes que aproximar su aspecto, lo "
        "cual es más lento y más incómodo y da resultados a los que un preajuste no llega. Esa es "
        "toda la idea detrás de",
        "Las apps comparten un sesgo. Prefiero simular la cosa antes que aproximar su aspecto, lo "
        "cual es más lento y más incómodo y da resultados a los que una predefinición no llega. "
        "Esa es toda la idea detrás de",
        "Les apps partagent un parti pris. Je préfère simuler la chose plutôt que d'approcher son "
        "apparence, ce qui est plus lent et plus ingrat et donne des résultats qu'un préréglage "
        "n'atteint pas. C'est toute l'idée derrière",
        "Le app condividono un'inclinazione. Preferisco simulare la cosa piuttosto che "
        "approssimarne l'aspetto, il che è più lento e più scomodo e dà risultati a cui un preset "
        "non arriva. È tutta qui l'idea dietro",
        "アプリにはひとつの傾き　があります。見た目を近似するより、そのもの自体を再現したい。"
        "そのぶん遅く、面倒で、そしてプリセットには出せない結果になります。その考え方が",
        "앱들은 하나의 편향을 공유합니다. 겉모습을 근사하기보다 그것 자체를 시뮬레이션하고 "
        "싶습니다. 더 느리고 더 번거롭지만, 프리셋으로는 나오지 않는 결과가 나옵니다. 그 생각이",
        "De apps delen een voorkeur. Ik simuleer liever het ding zelf dan dat ik de aanblik ervan "
        "benader, wat trager en onhandiger is en resultaten geeft waar een preset niet komt. Dat "
        "is het hele idee achter",
        "Os apps compartilham um viés. Prefiro simular a coisa a aproximar a aparência dela, o que "
        "é mais lento e mais desajeitado e dá resultados que uma predefinição não alcança. É essa "
        "a ideia por trás de",
        "这些应用有一个共同的偏向。比起去近似它的外观，我更愿意去模拟那件事本身，这更慢、更笨拙，"
        "却能得到预设做不到的结果。这就是"),
    "and": ("und", "y", "y", "et", "e", "と", "와", "en", "e", "和"),
    ", and it is why": (
        ", und darum bildet", ", y por eso", ", y por eso", ", et c'est pourquoi",
        ", ed è il motivo per cui", "の根底にあり、", "의 밑바탕이고,", ", en daarom modelleert",
        ", e é por isso que", "背后的全部想法；"),
    "models broken\n      hardware instead of drawing coloured lines over your photo.": (
        "kaputte Hardware nach, statt farbige Linien über dein Foto zu zeichnen.",
        "modela hardware averiado en vez de dibujar líneas de color sobre tu foto.",
        "modela hardware descompuesto en vez de dibujar líneas de color sobre tu foto.",
        "modélise du matériel en panne au lieu de tracer des lignes colorées sur votre photo.",
        "modella hardware guasto invece di disegnare righe colorate sopra la tua foto.",
        "が写真の上に色の線を描くのではなく、壊れたハードウェアそのものを再現しているのも、"
        "同じ理由です。",
        "가 사진 위에 색 선을 그리는 대신 고장 난 하드웨어 자체를 모델링하는 이유이기도 합니다.",
        "kapotte hardware in plaats van gekleurde lijnen over je foto te tekenen.",
        "modela hardware quebrado em vez de desenhar linhas coloridas sobre a sua foto.",
        "也是 MODUL8 去模拟坏掉的硬件、而不是在你的照片上画彩色线条的原因。"),
    "Work": ("Arbeiten", "Trabajo", "Trabajo", "Travaux", "Lavori", "作品", "작업", "Werk",
             "Trabalho", "作品"),
    "FRMT: Film Simulation": (
        "FRMT: Filmsimulation", "FRMT: simulación de película", "FRMT: simulación de película",
        "FRMT : simulation argentique", "FRMT: simulazione di pellicola",
        "FRMT｜フィルムシミュレーション", "FRMT｜필름 시뮬레이션", "FRMT: filmsimulatie",
        "FRMT: simulação de filme", "FRMT｜胶片模拟"),
    "A film simulation camera for iPhone. It models the photographic process itself rather than\n"
    "          applying a colour filter: light scattering through the emulsion, dye layers holding "
    "each\n          other back, grain forming where the light actually landed. Four stocks, built "
    "from\n          published manufacturer measurements, developed from a RAW negative on the "
    "device.": (
        "Eine Filmsimulationskamera für iPhone. Sie bildet den fotografischen Prozess selbst nach, "
        "statt einen Farbfilter anzuwenden: Licht, das durch die Emulsion streut, Farbschichten, "
        "die einander zurückhalten, Korn, das dort entsteht, wo das Licht tatsächlich gelandet "
        "ist. Vier Filme, gebaut aus veröffentlichten Herstellermessungen, auf dem Gerät aus einem "
        "RAW-Negativ entwickelt.",
        "Una cámara de simulación de película para iPhone. Modela el proceso fotográfico en sí en "
        "vez de aplicar un filtro de color: la luz dispersándose por la emulsión, las capas de "
        "colorante frenándose entre sí, el grano formándose donde la luz llegó de verdad. Cuatro "
        "películas, construidas a partir de mediciones publicadas por los fabricantes, reveladas "
        "en el dispositivo desde un negativo RAW.",
        "Una cámara de simulación de película para iPhone. Modela el proceso fotográfico en sí en "
        "vez de aplicar un filtro de color: la luz dispersándose por la emulsión, las capas de "
        "colorante frenándose entre sí, el grano formándose donde la luz llegó de verdad. Cuatro "
        "películas, construidas a partir de mediciones publicadas por los fabricantes, reveladas "
        "en el dispositivo desde un negativo RAW.",
        "Un appareil photo à simulation argentique pour iPhone. Il modélise le procédé "
        "photographique lui-même au lieu d'appliquer un filtre coloré : la lumière qui diffuse "
        "dans l'émulsion, les couches de colorant qui se retiennent, le grain qui se forme là où "
        "la lumière est réellement tombée. Quatre pellicules, construites à partir de mesures "
        "publiées par les fabricants, développées sur l'appareil depuis un négatif RAW.",
        "Una fotocamera a simulazione di pellicola per iPhone. Modella il processo fotografico in "
        "sé invece di applicare un filtro colore: la luce che diffonde nell'emulsione, gli strati "
        "di colorante che si trattengono a vicenda, la grana che si forma dove la luce è davvero "
        "arrivata. Quattro pellicole, costruite da misure pubblicate dai produttori, sviluppate "
        "sul dispositivo da un negativo RAW.",
        "iPhone 用のフィルムシミュレーションカメラ。カラーフィルターをかけるのではなく、"
        "写真という工程そのものを再現します。乳剤の中で散乱する光、互いを抑え合う色素層、"
        "光が実際に落ちた場所に生まれる粒子。メーカー公開の実測値から組み上げた四種のフィルムを、"
        "端末上で RAW ネガから現像します。",
        "iPhone용 필름 시뮬레이션 카메라. 컬러 필터를 씌우는 대신 사진이라는 공정 자체를 "
        "모델링합니다. 유제 안에서 산란하는 빛, 서로를 붙잡는 염료층, 빛이 실제로 닿은 자리에 "
        "생기는 입자. 제조사가 공개한 실측값으로 만든 네 가지 필름을, 기기 안에서 RAW "
        "네거티브로부터 현상합니다.",
        "Een filmsimulatiecamera voor iPhone. Hij modelleert het fotografische proces zelf in "
        "plaats van een kleurfilter toe te passen: licht dat door de emulsie verstrooit, "
        "kleurlagen die elkaar tegenhouden, korrel die ontstaat waar het licht echt is geland. "
        "Vier films, gebouwd op gepubliceerde metingen van de fabrikanten, op het toestel "
        "ontwikkeld vanuit een RAW-negatief.",
        "Uma câmera de simulação de filme para iPhone. Ela modela o próprio processo fotográfico "
        "em vez de aplicar um filtro de cor: a luz se espalhando pela emulsão, as camadas de "
        "corante segurando umas às outras, o grão se formando onde a luz de fato caiu. Quatro "
        "filmes, construídos a partir de medições publicadas pelos fabricantes, revelados no "
        "aparelho a partir de um negativo RAW.",
        "一款 iPhone 上的胶片模拟相机。它模拟的是摄影这道工序本身，而不是套一层颜色滤镜："
        "光在乳剂中散射，染料层彼此拖住，颗粒生成在光真正落下的地方。四款胶片，依据厂商公开的"
        "实测数据构建，在设备上从 RAW 底片完成显影。"),
    "$14.99 once": ("14,99 $ einmalig", "14,99 $ una vez", "14,99 $ una vez",
                    "14,99 $ une fois", "14,99 $ una volta", "14.99 ドル買い切り",
                    "14.99달러 한 번", "$14,99 eenmalig", "US$ 14,99 uma vez", "14.99 美元买断"),
    "MODUL8: Glitch Art Effects": (
        "MODUL8: Glitch-Art-Effekte", "MODUL8: efectos de glitch art",
        "MODUL8: efectos de glitch art", "MODUL8 : effets de glitch art",
        "MODUL8: effetti glitch art", "MODUL8｜グリッチアートエフェクト",
        "MODUL8｜글리치 아트 효과", "MODUL8: glitch-arteffecten",
        "MODUL8: efeitos de glitch art", "MODUL8｜故障艺术特效"),
    "A glitch art app for iPhone. Nineteen stackable effects, each modelled on a specific way\n"
    "          real hardware used to fail: VHS tracking loss, CRT phosphor bloom, datamosh block\n"
    "          corruption, pixel sorting, channel separation. Reorder the layers and the picture "
    "changes.": (
        "Eine Glitch-Art-App für iPhone. Neunzehn stapelbare Effekte, jeder einer bestimmten Art "
        "nachgebildet, auf die echte Hardware früher versagte: VHS-Spurverlust, CRT-Phosphorblüte, "
        "Datamosh-Blockfehler, Pixel Sorting, Kanaltrennung. Ordne die Ebenen um, und das Bild "
        "ändert sich.",
        "Una app de glitch art para iPhone. Diecinueve efectos apilables, cada uno modelado sobre "
        "una forma concreta en que fallaba el hardware real: pérdida de tracking de VHS, floración "
        "del fósforo del CRT, corrupción de bloques por datamosh, ordenación de píxeles, "
        "separación de canales. Reordena las capas y la imagen cambia.",
        "Una app de glitch art para iPhone. Diecinueve efectos apilables, cada uno modelado sobre "
        "una forma concreta en que fallaba el hardware real: pérdida de tracking de VHS, floración "
        "del fósforo del CRT, corrupción de bloques por datamosh, ordenación de píxeles, "
        "separación de canales. Reordena las capas y la imagen cambia.",
        "Une app de glitch art pour iPhone. Dix-neuf effets empilables, chacun modélisé sur une "
        "façon précise dont le matériel tombait en panne : perte de piste VHS, floraison du "
        "phosphore d'un CRT, corruption de blocs en datamosh, tri de pixels, séparation des "
        "canaux. Réordonnez les couches et l'image change.",
        "Un'app di glitch art per iPhone. Diciannove effetti impilabili, ognuno modellato su un "
        "modo preciso in cui l'hardware vero si guastava: perdita di tracking VHS, fioritura del "
        "fosforo CRT, corruzione a blocchi da datamosh, pixel sorting, separazione dei canali. "
        "Riordina i livelli e l'immagine cambia.",
        "iPhone 用のグリッチアートアプリ。積み重ねられる十九のエフェクトは、いずれも実在の"
        "ハードウェアが壊れたときの特定の壊れ方を再現しています。VHS のトラッキング崩れ、"
        "CRT の蛍光体のにじみ、データモッシュのブロック破損、ピクセルソート、チャンネル分離。"
        "レイヤーの順序を変えれば絵も変わります。",
        "iPhone용 글리치 아트 앱. 쌓아 올릴 수 있는 열아홉 가지 효과가 각각 실제 하드웨어가 "
        "고장 나던 특정한 방식을 모델링합니다. VHS 트래킹 이탈, CRT 인광체 번짐, 데이터모시 블록 "
        "손상, 픽셀 소팅, 채널 분리. 레이어 순서를 바꾸면 그림도 바뀝니다.",
        "Een glitch-art-app voor iPhone. Negentien stapelbare effecten, elk gemodelleerd op een "
        "specifieke manier waarop echte hardware kapotging: VHS-trackingverlies, CRT-fosforbloei, "
        "datamosh-blokcorruptie, pixel sorting, kanaalscheiding. Herschik de lagen en het beeld "
        "verandert.",
        "Um app de glitch art para iPhone. Dezenove efeitos empilháveis, cada um modelado sobre um "
        "jeito específico pelo qual o hardware de verdade falhava: perda de tracking do VHS, "
        "floração do fósforo do CRT, corrupção de blocos por datamosh, ordenação de pixels, "
        "separação de canais. Reordene as camadas e a imagem muda.",
        "一款 iPhone 上的故障艺术应用。十九种可叠加的效果，每一种都对应真实硬件当年出错的某种"
        "具体方式：VHS 循迹丢失、CRT 荧光粉晕开、datamosh 区块损坏、像素排序、通道分离。"
        "调换图层顺序，画面就会改变。"),
    "Free": ("Kostenlos", "Gratis", "Gratis", "Gratuit", "Gratis", "無料", "무료", "Gratis",
             "Grátis", "免费"),
    "Cyanotype Photos": (
        "Cyanotypie-Fotos", "Fotos en cianotipia", "Fotos en cianotipia",
        "Photos au cyanotype", "Foto in cianotipia", "サイアノタイプ写真", "사이아노타입 사진",
        "Cyanotypiefoto's", "Fotos em cianotipia", "蓝晒照片"),
    "A cyanotype app for iPhone. It runs the chemistry of the 1842 sunprint process instead of\n"
    "          tinting the picture blue: the paper is blind to red and green, so two colours a "
    "camera\n          recorded as equally bright come out at opposite ends of the print. No "
    "darkroom, no\n          chemicals, no printer.": (
        "Eine Cyanotypie-App für iPhone. Sie rechnet die Chemie des Sonnendruckverfahrens von 1842 "
        "durch, statt das Bild blau einzufärben: Das Papier ist blind für Rot und Grün, also "
        "kommen zwei Farben, die eine Kamera gleich hell aufgezeichnet hat, an entgegengesetzten "
        "Enden des Drucks heraus. Keine Dunkelkammer, keine Chemikalien, kein Drucker.",
        "Una app de cianotipia para iPhone. Ejecuta la química del proceso de impresión al sol de "
        "1842 en vez de teñir la imagen de azul: el papel es ciego al rojo y al verde, así que dos "
        "colores que la cámara registró igual de brillantes salen en extremos opuestos de la "
        "copia. Sin cuarto oscuro, sin productos químicos, sin impresora.",
        "Una app de cianotipia para iPhone. Ejecuta la química del proceso de impresión al sol de "
        "1842 en vez de teñir la imagen de azul: el papel es ciego al rojo y al verde, así que dos "
        "colores que la cámara registró igual de brillantes salen en extremos opuestos de la "
        "copia. Sin cuarto oscuro, sin químicos, sin impresora.",
        "Une app de cyanotype pour iPhone. Elle calcule la chimie du procédé d'insolation de 1842 "
        "au lieu de teinter l'image en bleu : le papier est aveugle au rouge et au vert, si bien "
        "que deux couleurs qu'un appareil a enregistrées aussi claires l'une que l'autre "
        "ressortent aux extrémités opposées du tirage. Sans chambre noire, sans produits "
        "chimiques, sans imprimante.",
        "Un'app di cianotipia per iPhone. Esegue la chimica del procedimento di stampa al sole del "
        "1842 invece di tingere di blu l'immagine: la carta è cieca al rosso e al verde, quindi "
        "due colori che una fotocamera ha registrato ugualmente luminosi escono agli estremi "
        "opposti della stampa. Niente camera oscura, niente prodotti chimici, niente stampante.",
        "iPhone 用のサイアノタイプアプリ。写真を青く染めるのではなく、1842 年の日光写真の化学"
        "そのものを計算します。この紙は赤と緑に対して盲目なので、カメラが同じ明るさとして記録した"
        "二つの色が、プリントの上では正反対の端に出ます。暗室も薬品もプリンターも要りません。",
        "iPhone용 사이아노타입 앱. 사진을 파랗게 물들이는 대신 1842년 태양광 인화 공정의 화학을 "
        "그대로 계산합니다. 이 종이는 빨강과 초록에 눈이 멀어서, 카메라가 똑같은 밝기로 기록한 두 "
        "색이 인화지 위에서는 정반대 끝에 놓입니다. 암실도, 약품도, 프린터도 필요 없습니다.",
        "Een cyanotypie-app voor iPhone. Hij rekent de chemie van het zonnedrukproces uit 1842 "
        "door in plaats van het beeld blauw te kleuren: het papier is blind voor rood en groen, "
        "dus twee kleuren die een camera even helder vastlegde komen aan tegenovergestelde kanten "
        "van de afdruk uit. Geen donkere kamer, geen chemicaliën, geen printer.",
        "Um app de cianotipia para iPhone. Ele roda a química do processo de impressão ao sol de "
        "1842 em vez de tingir a imagem de azul: o papel é cego ao vermelho e ao verde, então duas "
        "cores que a câmera registrou igualmente claras saem em extremos opostos da cópia. Sem "
        "câmara escura, sem produtos químicos, sem impressora.",
        "一款 iPhone 上的蓝晒应用。它跑的是 1842 年日光晒印工艺的化学，而不是把画面染成蓝色："
        "这种纸对红色和绿色是盲的，所以相机记录为同样明亮的两种颜色，在成品上会落到两个相反的"
        "极端。不需要暗房、不需要药水、不需要打印机。"),
    "On the App Store soon": (
        "Bald im App Store", "Pronto en la App Store", "Pronto en la App Store",
        "Bientôt sur l'App Store", "Presto sull'App Store", "まもなく App Store に登場",
        "곧 App Store에 출시", "Binnenkort in de App Store", "Em breve na App Store",
        "即将上架 App Store"),
    "A colour harmony and design tool for iPhone and iPad.": (
        "Ein Werkzeug für Farbharmonie und Gestaltung für iPhone und iPad.",
        "Una herramienta de armonía de color y diseño para iPhone y iPad.",
        "Una herramienta de armonía de color y diseño para iPhone y iPad.",
        "Un outil d'harmonie colorée et de design pour iPhone et iPad.",
        "Uno strumento di armonia cromatica e design per iPhone e iPad.",
        "iPhone と iPad のための配色とデザインのツール。",
        "iPhone과 iPad를 위한 색 조화와 디자인 도구.",
        "Een tool voor kleurharmonie en ontwerp voor iPhone en iPad.",
        "Uma ferramenta de harmonia de cor e design para iPhone e iPad.",
        "一款面向 iPhone 和 iPad 的配色与设计工具。"),
    "An art project about the line where human imagination meets machine generation. Generated\n"
    "          visuals, experimental tools, and a print shop.": (
        "Ein Kunstprojekt über die Linie, an der menschliche Vorstellungskraft auf maschinelle "
        "Erzeugung trifft. Generierte Bilder, experimentelle Werkzeuge und ein Druckshop.",
        "Un proyecto artístico sobre la línea donde la imaginación humana se encuentra con la "
        "generación por máquina. Imágenes generadas, herramientas experimentales y una tienda de "
        "impresiones.",
        "Un proyecto artístico sobre la línea donde la imaginación humana se encuentra con la "
        "generación por máquina. Imágenes generadas, herramientas experimentales y una tienda de "
        "impresiones.",
        "Un projet artistique sur la ligne où l'imagination humaine rencontre la génération par "
        "machine. Visuels générés, outils expérimentaux et une boutique de tirages.",
        "Un progetto artistico sulla linea dove l'immaginazione umana incontra la generazione "
        "meccanica. Immagini generate, strumenti sperimentali e una bottega di stampe.",
        "人間の想像力と機械による生成が接する線についてのアートプロジェクト。生成されたビジュアル、"
        "実験的なツール、そしてプリントショップ。",
        "인간의 상상력과 기계의 생성이 만나는 경계에 관한 아트 프로젝트. 생성된 비주얼, 실험적인 "
        "도구, 그리고 프린트 숍.",
        "Een kunstproject over de lijn waar menselijke verbeelding machinale generatie ontmoet. "
        "Gegenereerde beelden, experimentele tools en een printshop.",
        "Um projeto de arte sobre a linha onde a imaginação humana encontra a geração por máquina. "
        "Visuais gerados, ferramentas experimentais e uma loja de impressões.",
        "一个关于人的想象力与机器生成交界之处的艺术项目。生成的视觉、实验性的工具，以及一间版画店。"),
    "Art": ("Kunst", "Arte", "Arte", "Art", "Arte", "アート", "아트", "Kunst", "Arte", "艺术"),
    "Prints": ("Drucke", "Impresiones", "Impresiones", "Tirages", "Stampe", "プリント", "프린트",
               "Prints", "Impressões", "版画"),
    "Elsewhere": ("Anderswo", "En otros sitios", "En otros lados", "Ailleurs", "Altrove",
                  "そのほか", "다른 곳", "Elders", "Em outros lugares", "别处"),
    "Contact": ("Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "連絡先", "연락처",
                "Contact", "Contato", "联系"),
    "Email": ("E-Mail", "Correo", "Correo", "E-mail", "Email", "メール", "이메일", "E-mail",
              "E-mail", "邮件"),
    ". That reaches me directly.": (
        ". Das erreicht mich direkt.", ". Eso me llega directamente.",
        ". Eso me llega directamente.", ". Cela me parvient directement.",
        ". Arriva direttamente a me.", "。直接わたしに届きます。", ". 저에게 바로 갑니다.",
        ". Dat komt rechtstreeks bij mij aan.", ". Isso chega direto para mim.",
        "。会直接到我这里。"),
    "Levi Foster is an independent iPhone app developer and artist based in Fort Worth, Texas. He "
    "builds photography and design tools including FRMT, MODUL8, CYANO and Harmony Palette, and "
    "runs the art project Merge With The Machine.": (
        "Levi Foster ist unabhängiger iPhone-App-Entwickler und Künstler mit Sitz in Fort Worth, "
        "Texas. Er baut Foto- und Gestaltungswerkzeuge, darunter FRMT, MODUL8, CYANO und Harmony "
        "Palette, und betreibt das Kunstprojekt Merge With The Machine.",
        "Levi Foster es desarrollador independiente de apps para iPhone y artista, con base en "
        "Fort Worth, Texas. Construye herramientas de fotografía y diseño como FRMT, MODUL8, CYANO "
        "y Harmony Palette, y lleva el proyecto artístico Merge With The Machine.",
        "Levi Foster es desarrollador independiente de apps para iPhone y artista, con base en "
        "Fort Worth, Texas. Construye herramientas de fotografía y diseño como FRMT, MODUL8, CYANO "
        "y Harmony Palette, y lleva el proyecto artístico Merge With The Machine.",
        "Levi Foster est développeur indépendant d'apps iPhone et artiste, établi à Fort Worth, au "
        "Texas. Il construit des outils de photographie et de design dont FRMT, MODUL8, CYANO et "
        "Harmony Palette, et mène le projet artistique Merge With The Machine.",
        "Levi Foster è sviluppatore indipendente di app per iPhone e artista, con base a Fort "
        "Worth, Texas. Costruisce strumenti di fotografia e design fra cui FRMT, MODUL8, CYANO e "
        "Harmony Palette, e porta avanti il progetto artistico Merge With The Machine.",
        "Levi Foster はテキサス州フォートワースを拠点とする独立系の iPhone アプリ開発者であり、"
        "アーティストです。FRMT、MODUL8、CYANO、Harmony Palette をはじめとする写真とデザインの"
        "ツールをつくり、アートプロジェクト Merge With The Machine を運営しています。",
        "Levi Foster는 텍사스주 포트워스를 기반으로 활동하는 독립 iPhone 앱 개발자이자 "
        "아티스트입니다. FRMT, MODUL8, CYANO, Harmony Palette를 비롯한 사진과 디자인 도구를 "
        "만들고, 아트 프로젝트 Merge With The Machine을 운영합니다.",
        "Levi Foster is een onafhankelijke iPhone-app-ontwikkelaar en kunstenaar, gevestigd in "
        "Fort Worth, Texas. Hij bouwt foto- en ontwerptools waaronder FRMT, MODUL8, CYANO en "
        "Harmony Palette, en runt het kunstproject Merge With The Machine.",
        "Levi Foster é desenvolvedor independente de apps para iPhone e artista, baseado em Fort "
        "Worth, Texas. Ele constrói ferramentas de fotografia e design como FRMT, MODUL8, CYANO e "
        "Harmony Palette, e toca o projeto de arte Merge With The Machine.",
        "Levi Foster 是一位独立 iPhone 应用开发者与艺术家，常驻美国得州沃斯堡。他打造 FRMT、"
        "MODUL8、CYANO、Harmony Palette 等摄影与设计工具，并经营艺术项目 "
        "Merge With The Machine。"),
    "A film simulation camera for iPhone that simulates the photographic process rather than "
    "applying a colour filter.": (
        "Eine Filmsimulationskamera für iPhone, die den fotografischen Prozess simuliert, statt "
        "einen Farbfilter anzuwenden.",
        "Una cámara de simulación de película para iPhone que simula el proceso fotográfico en vez "
        "de aplicar un filtro de color.",
        "Una cámara de simulación de película para iPhone que simula el proceso fotográfico en vez "
        "de aplicar un filtro de color.",
        "Un appareil photo à simulation argentique pour iPhone qui simule le procédé "
        "photographique au lieu d'appliquer un filtre coloré.",
        "Una fotocamera a simulazione di pellicola per iPhone che simula il processo fotografico "
        "invece di applicare un filtro colore.",
        "カラーフィルターをかけるのではなく、写真の工程そのものを再現する iPhone 用フィルム"
        "シミュレーションカメラ。",
        "컬러 필터를 씌우는 대신 사진의 공정 자체를 시뮬레이션하는 iPhone용 필름 시뮬레이션 "
        "카메라.",
        "Een filmsimulatiecamera voor iPhone die het fotografische proces simuleert in plaats van "
        "een kleurfilter toe te passen.",
        "Uma câmera de simulação de filme para iPhone que simula o processo fotográfico em vez de "
        "aplicar um filtro de cor.",
        "一款 iPhone 胶片模拟相机，模拟的是摄影工序本身，而不是套一层颜色滤镜。"),
    "A glitch art app for iPhone with 19 stackable effects, each modelled on a specific way real "
    "hardware used to fail.": (
        "Eine Glitch-Art-App für iPhone mit 19 stapelbaren Effekten, jeder einer bestimmten Art "
        "nachgebildet, auf die echte Hardware früher versagte.",
        "Una app de glitch art para iPhone con 19 efectos apilables, cada uno modelado sobre una "
        "forma concreta en que fallaba el hardware real.",
        "Una app de glitch art para iPhone con 19 efectos apilables, cada uno modelado sobre una "
        "forma concreta en que fallaba el hardware real.",
        "Une app de glitch art pour iPhone avec 19 effets empilables, chacun modélisé sur une "
        "façon précise dont le matériel tombait en panne.",
        "Un'app di glitch art per iPhone con 19 effetti impilabili, ognuno modellato su un modo "
        "preciso in cui l'hardware vero si guastava.",
        "実在のハードウェアが壊れたときの特定の壊れ方を再現した、積み重ね可能な 19 の"
        "エフェクトを備えた iPhone 用グリッチアートアプリ。",
        "실제 하드웨어가 고장 나던 특정한 방식을 각각 모델링한, 쌓아 올릴 수 있는 19가지 효과의 "
        "iPhone용 글리치 아트 앱.",
        "Een glitch-art-app voor iPhone met 19 stapelbare effecten, elk gemodelleerd op een "
        "specifieke manier waarop echte hardware kapotging.",
        "Um app de glitch art para iPhone com 19 efeitos empilháveis, cada um modelado sobre um "
        "jeito específico pelo qual o hardware de verdade falhava.",
        "一款 iPhone 故障艺术应用，19 种可叠加效果，每一种都对应真实硬件当年出错的某种具体方式。"),
    "A cyanotype app for iPhone that simulates the chemistry of the 1842 sunprint process rather "
    "than tinting a photograph blue.": (
        "Eine Cyanotypie-App für iPhone, die die Chemie des Sonnendruckverfahrens von 1842 "
        "simuliert, statt ein Foto blau einzufärben.",
        "Una app de cianotipia para iPhone que simula la química del proceso de impresión al sol "
        "de 1842 en vez de teñir una foto de azul.",
        "Una app de cianotipia para iPhone que simula la química del proceso de impresión al sol "
        "de 1842 en vez de teñir una foto de azul.",
        "Une app de cyanotype pour iPhone qui simule la chimie du procédé d'insolation de 1842 au "
        "lieu de teinter une photo en bleu.",
        "Un'app di cianotipia per iPhone che simula la chimica del procedimento di stampa al sole "
        "del 1842 invece di tingere di blu una foto.",
        "写真を青く染めるのではなく、1842 年の日光写真の化学を再現する iPhone 用サイアノタイプ"
        "アプリ。",
        "사진을 파랗게 물들이는 대신 1842년 태양광 인화 공정의 화학을 시뮬레이션하는 iPhone용 "
        "사이아노타입 앱.",
        "Een cyanotypie-app voor iPhone die de chemie van het zonnedrukproces uit 1842 simuleert "
        "in plaats van een foto blauw te kleuren.",
        "Um app de cianotipia para iPhone que simula a química do processo de impressão ao sol de "
        "1842 em vez de tingir uma foto de azul.",
        "一款 iPhone 蓝晒应用，模拟 1842 年日光晒印工艺的化学，而不是把照片染成蓝色。"),
    "Apps and projects by Levi Foster": (
        "Apps und Projekte von Levi Foster", "Apps y proyectos de Levi Foster",
        "Apps y proyectos de Levi Foster", "Apps et projets de Levi Foster",
        "App e progetti di Levi Foster", "Levi Foster のアプリとプロジェクト",
        "Levi Foster의 앱과 프로젝트", "Apps en projecten van Levi Foster",
        "Apps e projetos de Levi Foster", "Levi Foster 的应用与项目"),
}

# The link label used to be "CYANO &mdash; Cyanotype Photos", which the parser saw as two text
# nodes either side of the entity. With a colon it is one node, so it needs its own entry.
T["CYANO: Cyanotype Photos"] = tuple("CYANO: " + v for v in T["Cyanotype Photos"])
