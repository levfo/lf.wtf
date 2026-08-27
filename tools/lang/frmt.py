"""lf.wtf/frmt, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The title and description are written for search, not translated literally: each leads with the
phrase that language's photographers type. Filmsimulation, simulation argentique, simulazione
pellicola, フィルムシミュレーション, 필름 시뮬레이션, 胶片模拟.

The FAQ answers matter more than their length suggests. They are the part an answer engine quotes
back when somebody asks "is FRMT a subscription" in their own language, and the page carries FAQPage
structured data over exactly this text, so the two have to stay in step.

Terminology follows the app and the store listing, so a visitor who reads the page and then opens
the App Store sees the same words. No em-dashes, per house style.
"""

KEEP = {
    "← lf.wtf", "FRMT", "iPhone", "Cinnabar 50", "Galena 100", "Baryta 100", "Flint 64",
    "Levi Foster", "App Store", "MODUL8", "CYANO", "FRMT - Film Simulation",
}

T = {
    "FRMT: Film Simulation App for iPhone": (
        "FRMT: Filmsimulation-App für iPhone",
        "FRMT: app de simulación de película para iPhone",
        "FRMT: app de simulación de película para iPhone",
        "FRMT : app de simulation argentique pour iPhone",
        "FRMT: app di simulazione pellicola per iPhone",
        "FRMT｜iPhone 用フィルムシミュレーションアプリ",
        "FRMT｜iPhone 필름 시뮬레이션 앱",
        "FRMT: filmsimulatie-app voor iPhone",
        "FRMT: app de simulação de filme para iPhone",
        "FRMT｜iPhone 胶片模拟应用"),
    "FRMT is a film simulation app for iPhone that models the film itself, not a colour filter: "
    "halation, interimage effects and density-based grain, developed from RAW on device.": (
        "FRMT ist eine Filmsimulations-App für iPhone, die den Film selbst nachbildet statt einen "
        "Farbfilter: Lichthofbildung, Interimage-Effekte und dichteabhängiges Korn, auf dem Gerät "
        "aus RAW entwickelt.",
        "FRMT es una app de simulación de película para iPhone que modela la película en sí, no un "
        "filtro de color: halación, efectos interimagen y grano según la densidad, revelado desde "
        "RAW en el dispositivo.",
        "FRMT es una app de simulación de película para iPhone que modela la película en sí, no un "
        "filtro de color: halación, efectos interimagen y grano según la densidad, revelado desde "
        "RAW en el dispositivo.",
        "FRMT est une app de simulation argentique pour iPhone qui modélise la pellicule "
        "elle-même, pas un filtre coloré : halo, effets inter-image et grain lié à la densité, "
        "développés depuis le RAW sur l'appareil.",
        "FRMT è un'app di simulazione pellicola per iPhone che modella la pellicola stessa, non un "
        "filtro colore: alone, effetti interimmagine e grana legata alla densità, sviluppati dal "
        "RAW sul dispositivo.",
        "FRMT は、カラーフィルターではなくフィルムそのものを再現する iPhone 用フィルム"
        "シミュレーションアプリです。ハレーション、インターイメージ効果、濃度に応じた粒子を、"
        "端末上で RAW から現像します。",
        "FRMT는 컬러 필터가 아니라 필름 자체를 모델링하는 iPhone용 필름 시뮬레이션 앱입니다. "
        "헐레이션, 인터이미지 효과, 농도에 따른 입자를 기기 안에서 RAW로부터 현상합니다.",
        "FRMT is een filmsimulatie-app voor iPhone die de film zelf modelleert, geen kleurfilter: "
        "lichthof, interimage-effecten en korrel op basis van dichtheid, op het toestel ontwikkeld "
        "vanuit RAW.",
        "O FRMT é um app de simulação de filme para iPhone que modela o filme em si, não um filtro "
        "de cor: halação, efeitos interimagem e grão conforme a densidade, revelados a partir do "
        "RAW no aparelho.",
        "FRMT 是一款 iPhone 胶片模拟应用，它模拟的是胶片本身，而不是颜色滤镜：光晕、层间效应、"
        "随密度变化的颗粒，全部在设备上从 RAW 完成显影。"),
    "Every other film app is a colour filter. FRMT simulates the film itself: halation, interimage "
    "effects and density-based grain, developed from RAW on your iPhone.": (
        "Jede andere Film-App ist ein Farbfilter. FRMT simuliert den Film selbst: "
        "Lichthofbildung, Interimage-Effekte und dichteabhängiges Korn, auf deinem iPhone aus RAW "
        "entwickelt.",
        "Las demás apps de película son filtros de color. FRMT simula la película en sí: halación, "
        "efectos interimagen y grano según la densidad, revelado desde RAW en tu iPhone.",
        "Las demás apps de película son filtros de color. FRMT simula la película en sí: halación, "
        "efectos interimagen y grano según la densidad, revelado desde RAW en tu iPhone.",
        "Toutes les autres apps de film sont des filtres colorés. FRMT simule la pellicule "
        "elle-même : halo, effets inter-image et grain lié à la densité, développés depuis le RAW "
        "sur votre iPhone.",
        "Tutte le altre app di pellicola sono filtri colore. FRMT simula la pellicola stessa: "
        "alone, effetti interimmagine e grana legata alla densità, sviluppati dal RAW sul tuo "
        "iPhone.",
        "ほかのフィルムアプリはどれもカラーフィルターです。FRMT はフィルムそのものを再現します。"
        "ハレーション、インターイメージ効果、濃度に応じた粒子を、あなたの iPhone の上で RAW から"
        "現像します。",
        "다른 필름 앱은 모두 컬러 필터입니다. FRMT는 필름 자체를 시뮬레이션합니다. 헐레이션, "
        "인터이미지 효과, 농도에 따른 입자를 당신의 iPhone 안에서 RAW로부터 현상합니다.",
        "Elke andere film-app is een kleurfilter. FRMT simuleert de film zelf: lichthof, "
        "interimage-effecten en korrel op basis van dichtheid, op je iPhone ontwikkeld vanuit RAW.",
        "Todos os outros apps de filme são filtros de cor. O FRMT simula o filme em si: halação, "
        "efeitos interimagem e grão conforme a densidade, revelados a partir do RAW no seu iPhone.",
        "其他所有胶片应用都是颜色滤镜。FRMT 模拟的是胶片本身：光晕、层间效应、随密度变化的颗粒，"
        "在你的 iPhone 上从 RAW 完成显影。"),
    "A castle keep at dusk developed through the FRMT film simulation.": (
        "Ein Burgfried in der Dämmerung, entwickelt durch die FRMT-Filmsimulation.",
        "Una torre del homenaje al anochecer, revelada con la simulación de película de FRMT.",
        "Una torre del homenaje al anochecer, revelada con la simulación de película de FRMT.",
        "Un donjon au crépuscule, développé par la simulation argentique de FRMT.",
        "Un mastio al crepuscolo, sviluppato con la simulazione di pellicola di FRMT.",
        "夕暮れの天守を FRMT のフィルムシミュレーションで現像した一枚。",
        "해질 무렵의 성채를 FRMT 필름 시뮬레이션으로 현상한 사진.",
        "Een donjon in de schemering, ontwikkeld met de filmsimulatie van FRMT.",
        "Uma torre de menagem ao anoitecer, revelada com a simulação de filme do FRMT.",
        "黄昏时分的城堡主楼，用 FRMT 胶片模拟显影而成。"),
    "FRMT app icon": ("FRMT App-Symbol", "Icono de la app FRMT", "Icono de la app FRMT",
                      "Icône de l'app FRMT", "Icona dell'app FRMT", "FRMT のアプリアイコン",
                      "FRMT 앱 아이콘", "FRMT-app-icoon", "Ícone do app FRMT", "FRMT 应用图标"),
    "Film Simulation for iPhone": (
        "Filmsimulation für iPhone", "Simulación de película para iPhone",
        "Simulación de película para iPhone", "Simulation argentique pour iPhone",
        "Simulazione di pellicola per iPhone", "iPhone のためのフィルムシミュレーション",
        "iPhone을 위한 필름 시뮬레이션", "Filmsimulatie voor iPhone",
        "Simulação de filme para iPhone", "为 iPhone 打造的胶片模拟"),
    "Not a filter.": ("Kein Filter.", "No es un filtro.", "No es un filtro.", "Pas un filtre.",
                      "Non un filtro.", "フィルターではない。", "필터가 아닙니다.",
                      "Geen filter.", "Não é um filtro.", "不是滤镜。"),
    "A film.": ("Ein Film.", "Es película.", "Es película.", "Une pellicule.", "Una pellicola.",
                "フィルムだ。", "필름입니다.", "Film.", "É filme.", "是胶片。"),
    "Every other film app on your phone is a colour filter. A list of what each colour should\n"
    "      become, applied to a photo that has already been taken.": (
        "Jede andere Film-App auf deinem Telefon ist ein Farbfilter. Eine Liste davon, was aus "
        "jeder Farbe werden soll, angewendet auf ein Foto, das längst aufgenommen ist.",
        "Las demás apps de película de tu móvil son filtros de color. Una lista de en qué debe "
        "convertirse cada color, aplicada a una foto que ya está hecha.",
        "Las demás apps de película de tu celular son filtros de color. Una lista de en qué debe "
        "convertirse cada color, aplicada a una foto que ya está tomada.",
        "Toutes les autres apps de film sur votre téléphone sont des filtres colorés. Une liste de "
        "ce que chaque couleur doit devenir, appliquée à une photo déjà prise.",
        "Tutte le altre app di pellicola sul tuo telefono sono filtri colore. Un elenco di cosa "
        "deve diventare ogni colore, applicato a una foto già scattata.",
        "スマートフォンに入っているほかのフィルムアプリは、どれもカラーフィルターです。"
        "どの色を何に変えるかを並べた一覧を、撮り終わった写真にあてているだけです。",
        "휴대폰에 있는 다른 필름 앱은 모두 컬러 필터입니다. 어떤 색을 무엇으로 바꿀지 적어 둔 "
        "목록을, 이미 찍힌 사진에 씌우는 것뿐입니다.",
        "Elke andere film-app op je telefoon is een kleurfilter. Een lijst van wat elke kleur moet "
        "worden, toegepast op een foto die al gemaakt is.",
        "Todos os outros apps de filme no seu telefone são filtros de cor. Uma lista do que cada "
        "cor deve virar, aplicada a uma foto que já foi tirada.",
        "你手机上其他所有胶片应用都是颜色滤镜：一张写明每种颜色该变成什么的清单，套在一张已经"
        "拍好的照片上。"),
    "FRMT simulates the film instead.": (
        "FRMT simuliert stattdessen den Film.", "FRMT simula la película en su lugar.",
        "FRMT simula la película en su lugar.", "FRMT simule la pellicule à la place.",
        "FRMT simula invece la pellicola.", "FRMT はその代わりにフィルムを再現します。",
        "FRMT는 대신 필름을 시뮬레이션합니다.", "FRMT simuleert in plaats daarvan de film.",
        "O FRMT simula o filme, em vez disso.", "FRMT 做的是模拟胶片本身。"),
    "The light scattering sideways through the\n      emulsion. The dye layers chemically holding "
    "each other back. The grain forming only where\n      light actually landed. Your iPhone runs "
    "the chemistry, one frame at a time, from a RAW\n      negative.": (
        "Das Licht, das seitwärts durch die Emulsion streut. Die Farbschichten, die einander "
        "chemisch zurückhalten. Das Korn, das nur dort entsteht, wo Licht tatsächlich gelandet "
        "ist. Dein iPhone rechnet die Chemie durch, Bild für Bild, aus einem RAW-Negativ.",
        "La luz dispersándose de lado por la emulsión. Las capas de colorante frenándose entre sí "
        "químicamente. El grano formándose solo donde la luz llegó de verdad. Tu iPhone ejecuta la "
        "química, un fotograma cada vez, desde un negativo RAW.",
        "La luz dispersándose de lado por la emulsión. Las capas de colorante frenándose entre sí "
        "químicamente. El grano formándose solo donde la luz llegó de verdad. Tu iPhone ejecuta la "
        "química, un cuadro a la vez, desde un negativo RAW.",
        "La lumière qui diffuse latéralement dans l'émulsion. Les couches de colorant qui se "
        "retiennent chimiquement. Le grain qui ne se forme que là où la lumière est réellement "
        "tombée. Votre iPhone calcule la chimie, image par image, depuis un négatif RAW.",
        "La luce che diffonde di lato nell'emulsione. Gli strati di colorante che si trattengono a "
        "vicenda per via chimica. La grana che si forma solo dove la luce è davvero arrivata. Il "
        "tuo iPhone esegue la chimica, un fotogramma alla volta, da un negativo RAW.",
        "乳剤の中を横へ散乱していく光。互いを化学的に抑え合う色素層。光が実際に落ちた場所にだけ"
        "生まれる粒子。あなたの iPhone が、RAW ネガから一枚ずつ、この化学を計算します。",
        "유제 안을 옆으로 산란해 가는 빛. 서로를 화학적으로 붙잡는 염료층. 빛이 실제로 닿은 "
        "자리에만 생기는 입자. 당신의 iPhone이 RAW 네거티브로부터 한 장씩 이 화학을 계산합니다.",
        "Het licht dat zijwaarts door de emulsie verstrooit. De kleurlagen die elkaar chemisch "
        "tegenhouden. De korrel die alleen ontstaat waar licht echt is geland. Je iPhone rekent de "
        "chemie door, beeld voor beeld, vanuit een RAW-negatief.",
        "A luz se espalhando de lado pela emulsão. As camadas de corante segurando umas às outras "
        "quimicamente. O grão se formando só onde a luz de fato caiu. Seu iPhone roda a química, "
        "um quadro por vez, a partir de um negativo RAW.",
        "光在乳剂中向侧面散射。染料层在化学上彼此拖住。颗粒只生成在光真正落下的地方。"
        "你的 iPhone 从一张 RAW 底片出发，一次一张地把这套化学跑完。"),
    "Download on the App Store": (
        "Im App Store laden", "Descargar en la App Store", "Descargar en la App Store",
        "Télécharger dans l'App Store", "Scarica dall'App Store", "App Store でダウンロード",
        "App Store에서 다운로드", "Downloaden in de App Store", "Baixar na App Store",
        "在 App Store 下载"),
    "$14.99 once": ("14,99 $ einmalig", "14,99 $ una vez", "14,99 $ una vez", "14,99 $ une fois",
                    "14,99 $ una volta", "14.99 ドル買い切り", "14.99달러 한 번",
                    "$14,99 eenmalig", "US$ 14,99 uma vez", "14.99 美元买断"),
    "No subscription · No account · Nothing leaves your phone": (
        "Kein Abo · Kein Konto · Nichts verlässt dein Telefon",
        "Sin suscripción · Sin cuenta · Nada sale de tu móvil",
        "Sin suscripción · Sin cuenta · Nada sale de tu celular",
        "Sans abonnement · Sans compte · Rien ne quitte votre téléphone",
        "Nessun abbonamento · Nessun account · Niente esce dal telefono",
        "定額課金なし · アカウント不要 · 端末の外には出ない",
        "구독 없음 · 계정 없음 · 휴대폰 밖으로 나가지 않음",
        "Geen abonnement · Geen account · Er gaat niets van je telefoon af",
        "Sem assinatura · Sem conta · Nada sai do seu telefone",
        "无订阅 · 无账号 · 什么都不会离开你的手机"),
    "A lit castle keep above a moat at dusk, as the iPhone renders it.": (
        "Ein beleuchteter Burgfried über einem Wassergraben in der Dämmerung, so wie das iPhone "
        "ihn wiedergibt.",
        "Una torre del homenaje iluminada sobre un foso al anochecer, tal como la representa el "
        "iPhone.",
        "Una torre del homenaje iluminada sobre un foso al anochecer, tal como la representa el "
        "iPhone.",
        "Un donjon éclairé au-dessus de douves au crépuscule, tel que l'iPhone le restitue.",
        "Un mastio illuminato sopra un fossato al crepuscolo, come lo restituisce l'iPhone.",
        "夕暮れの堀の上に浮かぶ、ライトアップされた天守。iPhone が描いたそのまま。",
        "해질 무렵 해자 위로 불이 켜진 성채. iPhone이 그려 낸 그대로.",
        "Een verlichte donjon boven een slotgracht in de schemering, zoals de iPhone hem weergeeft.",
        "Uma torre de menagem iluminada sobre um fosso ao anoitecer, como o iPhone a representa.",
        "黄昏中护城河上灯火通明的城堡主楼，iPhone 直出的样子。"),
    "The same frame developed through the Cinnabar 50 profile: the lit walls and the towers bloom "
    "into the dark around them.": (
        "Dasselbe Bild, entwickelt über das Profil Cinnabar 50: Die beleuchteten Mauern und die "
        "Türme blühen in das Dunkel um sie herum.",
        "El mismo fotograma revelado con el perfil Cinnabar 50: los muros iluminados y las torres "
        "florecen hacia la oscuridad que los rodea.",
        "El mismo cuadro revelado con el perfil Cinnabar 50: los muros iluminados y las torres "
        "florecen hacia la oscuridad que los rodea.",
        "La même image développée avec le profil Cinnabar 50 : les murs éclairés et les tours "
        "rayonnent dans l'obscurité autour d'eux.",
        "Lo stesso fotogramma sviluppato con il profilo Cinnabar 50: i muri illuminati e le torri "
        "fioriscono nel buio attorno.",
        "同じ一枚を Cinnabar 50 のプロファイルで現像したもの。光が当たった壁と櫓が、"
        "まわりの闇へにじんでいく。",
        "같은 프레임을 Cinnabar 50 프로파일로 현상한 것. 빛을 받은 성벽과 망루가 주변의 어둠 "
        "속으로 번져 나갑니다.",
        "Hetzelfde beeld ontwikkeld met het profiel Cinnabar 50: de verlichte muren en de torens "
        "bloeien open in het donker eromheen.",
        "O mesmo quadro revelado com o perfil Cinnabar 50: os muros iluminados e as torres "
        "florescem para o escuro em volta.",
        "同一张画面用 Cinnabar 50 描述文件显影：被照亮的城墙和塔楼向四周的黑暗晕开。"),
    "Same frame, same exposure. Drag it.": (
        "Gleiches Bild, gleiche Belichtung. Zieh daran.",
        "Mismo fotograma, misma exposición. Arrastra.",
        "Mismo cuadro, misma exposición. Arrastra.",
        "Même image, même exposition. Faites glisser.",
        "Stesso fotogramma, stessa esposizione. Trascina.",
        "同じ一枚、同じ露出。ドラッグしてみてください。",
        "같은 프레임, 같은 노출. 끌어 보세요.",
        "Zelfde beeld, zelfde belichting. Sleep maar.",
        "Mesmo quadro, mesma exposição. Arraste.",
        "同一张画面，同样的曝光。拖动看看。"),
    "The difference": ("Der Unterschied", "La diferencia", "La diferencia", "La différence",
                       "La differenza", "違い", "차이", "Het verschil", "A diferença", "差别"),
    "A filter is a list. Film is a reaction.": (
        "Ein Filter ist eine Liste. Film ist eine Reaktion.",
        "Un filtro es una lista. La película es una reacción.",
        "Un filtro es una lista. La película es una reacción.",
        "Un filtre est une liste. La pellicule est une réaction.",
        "Un filtro è un elenco. La pellicola è una reazione.",
        "フィルターは一覧表。フィルムは反応。",
        "필터는 목록입니다. 필름은 반응입니다.",
        "Een filter is een lijst. Film is een reactie.",
        "Um filtro é uma lista. O filme é uma reação.",
        "滤镜是一张清单。胶片是一场反应。"),
    "A filter works by lookup. Somebody decided in advance what every colour should turn into, and\n"
    "      the app swaps them one pixel at a time. Feed it the same blue twice and you get the "
    "same\n      answer twice, whether that blue was an inch of evening sky or the highlight on a "
    "chrome\n      bumper.": (
        "Ein Filter arbeitet per Nachschlagen. Jemand hat vorab entschieden, was aus jeder Farbe "
        "werden soll, und die App tauscht sie Pixel für Pixel aus. Gib ihr zweimal dasselbe Blau, "
        "und du bekommst zweimal dieselbe Antwort, ob dieses Blau nun ein Stück Abendhimmel war "
        "oder das Glanzlicht auf einer Chromstoßstange.",
        "Un filtro funciona por consulta. Alguien decidió de antemano en qué debe convertirse cada "
        "color, y la app los cambia píxel a píxel. Dale dos veces el mismo azul y obtienes dos "
        "veces la misma respuesta, tanto si ese azul era un trozo de cielo al atardecer como el "
        "brillo en un parachoques cromado.",
        "Un filtro funciona por consulta. Alguien decidió de antemano en qué debe convertirse cada "
        "color, y la app los cambia píxel a píxel. Dale dos veces el mismo azul y obtienes dos "
        "veces la misma respuesta, ya fuera ese azul un trozo de cielo al atardecer o el brillo en "
        "una defensa cromada.",
        "Un filtre fonctionne par consultation. Quelqu'un a décidé à l'avance ce que chaque "
        "couleur doit devenir, et l'app les échange pixel par pixel. Donnez-lui deux fois le même "
        "bleu et vous obtenez deux fois la même réponse, que ce bleu ait été un morceau de ciel du "
        "soir ou le reflet sur un pare-chocs chromé.",
        "Un filtro funziona per consultazione. Qualcuno ha deciso in anticipo cosa deve diventare "
        "ogni colore, e l'app li scambia un pixel alla volta. Dagli due volte lo stesso blu e "
        "ottieni due volte la stessa risposta, che quel blu fosse un pezzo di cielo della sera o "
        "il riflesso su un paraurti cromato.",
        "フィルターは参照表で動きます。どの色が何になるかを誰かが前もって決めていて、アプリは"
        "それを一画素ずつ置き換えるだけ。同じ青を二度入れれば、答えも二度とも同じです。"
        "その青が夕空の一片であっても、クロームのバンパーのハイライトであっても。",
        "필터는 조회로 동작합니다. 어떤 색이 무엇이 될지 누군가 미리 정해 두었고, 앱은 그것을 한 "
        "픽셀씩 바꿔치울 뿐입니다. 같은 파랑을 두 번 넣으면 답도 두 번 다 같습니다. 그 파랑이 "
        "저녁 하늘 한 조각이든, 크롬 범퍼 위의 하이라이트든.",
        "Een filter werkt via opzoeken. Iemand heeft vooraf besloten wat elke kleur moet worden, "
        "en de app wisselt ze pixel voor pixel om. Geef het twee keer hetzelfde blauw en je krijgt "
        "twee keer hetzelfde antwoord, of dat blauw nu een stuk avondlucht was of de schittering "
        "op een chromen bumper.",
        "Um filtro funciona por consulta. Alguém decidiu de antemão no que cada cor deve virar, e "
        "o app troca uma a uma, pixel por pixel. Dê a ele o mesmo azul duas vezes e você recebe a "
        "mesma resposta duas vezes, fosse esse azul um pedaço de céu de fim de tarde ou o brilho "
        "num para-choque cromado.",
        "滤镜靠查表工作。有人事先决定了每种颜色该变成什么，应用再一个像素一个像素地替换。"
        "同一种蓝色喂进去两次，得到的答案也是两次一样，无论那片蓝是一小块傍晚的天空，"
        "还是镀铬保险杠上的高光。"),
    "Film has no list to consult. It has chemistry, and chemistry pays attention to its\n"
    "      surroundings. Light that hits a bright edge keeps going, bounces off the back of the "
    "film and\n      comes back to expose the grains beside it. Dye forming in one layer releases a "
    "chemical that\n      stops the layer next to it forming as strongly. Grain appears where "
    "enough photons happened to\n      land, which is not the same place in the shadows as in the "
    "midtones.": (
        "Film hat keine Liste zum Nachschlagen. Er hat Chemie, und Chemie achtet auf ihre "
        "Umgebung. Licht, das auf eine helle Kante trifft, läuft weiter, wird von der Rückseite "
        "des Films zurückgeworfen und belichtet die Körner daneben. Farbstoff, der in einer "
        "Schicht entsteht, setzt eine Chemikalie frei, die verhindert, dass die Schicht daneben "
        "ebenso stark entsteht. Korn erscheint dort, wo genug Photonen gelandet sind, und das ist "
        "in den Schatten ein anderer Ort als in den Mitteltönen.",
        "La película no tiene lista que consultar. Tiene química, y la química presta atención a "
        "lo que la rodea. La luz que da en un borde brillante sigue adelante, rebota en el dorso "
        "de la película y vuelve para exponer los granos de al lado. El colorante que se forma en "
        "una capa libera una sustancia que impide que la capa vecina se forme con la misma fuerza. "
        "El grano aparece donde han caído suficientes fotones, y ese no es el mismo sitio en las "
        "sombras que en los medios tonos.",
        "La película no tiene lista que consultar. Tiene química, y la química presta atención a "
        "lo que la rodea. La luz que da en un borde brillante sigue adelante, rebota en el dorso "
        "de la película y vuelve para exponer los granos de al lado. El colorante que se forma en "
        "una capa libera una sustancia que impide que la capa vecina se forme con la misma fuerza. "
        "El grano aparece donde cayeron suficientes fotones, y ese no es el mismo sitio en las "
        "sombras que en los medios tonos.",
        "La pellicule n'a pas de liste à consulter. Elle a de la chimie, et la chimie fait "
        "attention à ce qui l'entoure. La lumière qui frappe un bord clair continue, rebondit sur "
        "le dos du film et revient exposer les grains d'à côté. Le colorant qui se forme dans une "
        "couche libère un composé qui empêche la couche voisine de se former aussi fort. Le grain "
        "apparaît là où assez de photons sont tombés, et ce n'est pas le même endroit dans les "
        "ombres que dans les tons moyens.",
        "La pellicola non ha un elenco da consultare. Ha chimica, e la chimica bada a ciò che le "
        "sta intorno. La luce che colpisce un bordo chiaro prosegue, rimbalza sul retro della "
        "pellicola e torna a esporre i grani accanto. Il colorante che si forma in uno strato "
        "libera una sostanza che impedisce allo strato vicino di formarsi altrettanto forte. La "
        "grana compare dove sono caduti abbastanza fotoni, e nelle ombre non è lo stesso posto che "
        "nei mezzitoni.",
        "フィルムには参照する表がありません。あるのは化学で、化学はまわりの様子に反応します。"
        "明るい輪郭に当たった光はそのまま進み、フィルムの裏面で跳ね返って、隣の粒子を感光させに"
        "戻ってきます。ある層で色素ができると化学物質が放たれ、隣の層が同じだけ濃くなるのを"
        "妨げます。粒子は十分な光子が落ちた場所に現れますが、その場所は影と中間調とでは同じでは"
        "ありません。",
        "필름에는 찾아볼 목록이 없습니다. 있는 것은 화학이고, 화학은 주변을 살핍니다. 밝은 "
        "가장자리에 닿은 빛은 그대로 나아가 필름 뒷면에서 튕겨 나와, 옆에 있는 입자를 노광시키러 "
        "돌아옵니다. 한 층에서 염료가 생기면 화학 물질이 나와, 옆 층이 그만큼 진해지는 것을 "
        "막습니다. 입자는 충분한 광자가 떨어진 자리에 나타나는데, 그 자리는 그림자와 중간톤에서 "
        "서로 다릅니다.",
        "Film heeft geen lijst om te raadplegen. Hij heeft chemie, en chemie let op zijn omgeving. "
        "Licht dat een lichte rand raakt gaat door, kaatst terug van de achterkant van de film en "
        "komt terug om de korrels ernaast te belichten. Kleurstof die in de ene laag ontstaat laat "
        "een stof vrij die voorkomt dat de laag ernaast even sterk ontstaat. Korrel verschijnt "
        "waar genoeg fotonen zijn geland, en dat is in de schaduwen niet dezelfde plek als in de "
        "middentonen.",
        "O filme não tem lista para consultar. Tem química, e química presta atenção ao que está "
        "em volta. A luz que bate numa borda clara segue adiante, ricocheteia no verso do filme e "
        "volta para expor os grãos ao lado. O corante que se forma numa camada libera uma "
        "substância que impede a camada vizinha de se formar com a mesma força. O grão aparece "
        "onde caíram fótons suficientes, e nas sombras esse não é o mesmo lugar que nos meios-tons.",
        "胶片没有清单可查。它有的是化学，而化学会理会周围发生了什么。打在明亮边缘上的光会继续前行，"
        "在片基背面反弹，再回来曝光旁边的颗粒。某一层生成染料时会释放一种化学物质，"
        "阻止相邻的层生成得同样浓。颗粒出现在落下了足够多光子的地方，而在暗部和中间调里，"
        "那并不是同一个地方。"),
    "None of that can be written down as a list, because the answer depends on what else is in\n"
    "      the frame.": (
        "Nichts davon lässt sich als Liste aufschreiben, weil die Antwort davon abhängt, was sonst "
        "im Bild ist.",
        "Nada de eso se puede escribir como una lista, porque la respuesta depende de qué más hay "
        "en el encuadre.",
        "Nada de eso se puede escribir como una lista, porque la respuesta depende de qué más hay "
        "en el encuadre.",
        "Rien de tout cela ne peut s'écrire sous forme de liste, parce que la réponse dépend de ce "
        "qu'il y a d'autre dans le cadre.",
        "Niente di tutto questo si può scrivere come un elenco, perché la risposta dipende da cosa "
        "altro c'è nell'inquadratura.",
        "こうしたことはどれも一覧表には書き下せません。答えが、その画面のほかに何が写っているかに"
        "左右されるからです。",
        "이 가운데 어느 것도 목록으로 적어 둘 수 없습니다. 답이 그 화면 안에 무엇이 함께 있는지에 "
        "달려 있기 때문입니다.",
        "Niets daarvan valt als lijst op te schrijven, omdat het antwoord afhangt van wat er "
        "verder in beeld is.",
        "Nada disso pode ser escrito como uma lista, porque a resposta depende do que mais está no "
        "enquadramento.",
        "这些都没法写成一张清单，因为答案取决于画面里还有什么。"),
    "That is the whole reason a neon sign on film glows into the dark around it, why reds stay\n"
    "      separate from greens instead of turning to mud, and why grain sits heaviest in the "
    "midtones\n      and vanishes in deep shadow. It is what people are pointing at when they say a "
    "photograph\n      looks like film. A lookup table cannot get there, no matter how carefully it "
    "was made.": (
        "Genau darum leuchtet eine Neonreklame auf Film in das Dunkel um sie herum, darum bleiben "
        "Rottöne von Grüntönen getrennt, statt zu Matsch zu werden, und darum liegt das Korn am "
        "schwersten in den Mitteltönen und verschwindet im tiefen Schatten. Darauf zeigen die "
        "Leute, wenn sie sagen, ein Foto sehe nach Film aus. Eine Nachschlagetabelle kommt da "
        "nicht hin, so sorgfältig sie auch gemacht wurde.",
        "Esa es toda la razón de que un letrero de neón en película brille hacia la oscuridad que "
        "lo rodea, de que los rojos se mantengan separados de los verdes en vez de volverse barro, "
        "y de que el grano pese más en los medios tonos y desaparezca en las sombras profundas. Es "
        "lo que señala la gente cuando dice que una foto parece película. Una tabla de consulta no "
        "llega ahí, por cuidadosamente que se haya hecho.",
        "Esa es toda la razón de que un letrero de neón en película brille hacia la oscuridad que "
        "lo rodea, de que los rojos se mantengan separados de los verdes en vez de volverse lodo, "
        "y de que el grano pese más en los medios tonos y desaparezca en las sombras profundas. Es "
        "lo que señala la gente cuando dice que una foto parece película. Una tabla de consulta no "
        "llega ahí, por cuidadosamente que se haya hecho.",
        "C'est toute la raison pour laquelle une enseigne au néon sur pellicule rayonne dans "
        "l'obscurité autour d'elle, pour laquelle les rouges restent distincts des verts au lieu "
        "de tourner à la boue, et pour laquelle le grain pèse le plus dans les tons moyens et "
        "disparaît dans les ombres profondes. C'est ce que les gens désignent quand ils disent "
        "qu'une photo fait argentique. Une table de conversion n'y arrive pas, aussi soigneusement "
        "qu'elle ait été faite.",
        "È tutta qui la ragione per cui un'insegna al neon su pellicola brilla nel buio attorno a "
        "sé, per cui i rossi restano distinti dai verdi invece di virare al fango, e per cui la "
        "grana pesa di più nei mezzitoni e sparisce nelle ombre profonde. È quello che la gente "
        "indica quando dice che una foto sembra pellicola. Una tabella di consultazione non ci "
        "arriva, per quanto accuratamente sia stata fatta.",
        "フィルムのネオンサインがまわりの闇へにじんで光るのも、赤が緑と混ざって濁らずに"
        "別々のままでいるのも、粒子が中間調で最も重く、深い影ではほとんど消えるのも、"
        "理由はすべてここにあります。「フィルムっぽい写真」と言うとき、人が指しているのはこれです。"
        "参照表がどれほど丁寧につくられていても、そこには届きません。",
        "필름에 찍힌 네온사인이 주변의 어둠 속으로 번지며 빛나는 것도, 빨강이 초록과 섞여 "
        "탁해지지 않고 따로 남는 것도, 입자가 중간톤에서 가장 무겁고 깊은 그림자에서 사라지는 "
        "것도, 이유는 전부 여기에 있습니다. 사람들이 \"필름 같다\"고 말할 때 가리키는 것이 바로 "
        "이것입니다. 룩업 테이블은 아무리 정성껏 만들어도 거기에 닿지 못합니다.",
        "Dat is de hele reden dat een neonreclame op film de duisternis eromheen in gloeit, dat "
        "rood en groen gescheiden blijven in plaats van tot modder te worden, en dat korrel het "
        "zwaarst ligt in de middentonen en verdwijnt in diepe schaduw. Het is waar mensen naar "
        "wijzen als ze zeggen dat een foto er als film uitziet. Een opzoektabel komt daar niet, "
        "hoe zorgvuldig hij ook is gemaakt.",
        "É essa toda a razão de um letreiro de neon em filme brilhar para o escuro em volta, de os "
        "vermelhos ficarem separados dos verdes em vez de virar lama, e de o grão pesar mais nos "
        "meios-tons e sumir nas sombras profundas. É para isso que as pessoas apontam quando dizem "
        "que uma foto parece filme. Uma tabela de consulta não chega lá, por mais caprichada que "
        "seja.",
        "胶片上的霓虹招牌之所以会向周围的黑暗里发光，红色之所以不会和绿色混成一团烂泥，"
        "颗粒之所以在中间调最重、在深暗部几乎消失，原因全在这里。人们说一张照片\"有胶片味\"时，"
        "指的就是这个。查找表再怎么用心去做，也到不了这里。"),
    "The proof": ("Der Beweis", "La prueba", "La prueba", "La preuve", "La prova", "証拠", "증거",
                  "Het bewijs", "A prova", "证据"),
    "We built the filter, then beat it.": (
        "Wir haben den Filter gebaut und ihn dann geschlagen.",
        "Construimos el filtro y luego lo superamos.",
        "Construimos el filtro y luego lo superamos.",
        "Nous avons construit le filtre, puis nous l'avons battu.",
        "Abbiamo costruito il filtro, poi lo abbiamo battuto.",
        "そのフィルターを自分たちでつくり、そのうえで超えました。",
        "그 필터를 우리가 직접 만들고, 그다음 넘어섰습니다.",
        "We hebben het filter gebouwd en het daarna verslagen.",
        "Construímos o filtro e depois o superamos.",
        "我们先把这个滤镜做出来，然后超过它。"),
    "One photograph, developed twice. On the left, the best possible colour filter of this exact\n"
    "      film stock, built from the same measurements we built the model from. On the right, the "
    "full\n      simulation. This is a 1:1 crop, so you are looking at real pixels rather than a "
    "resized\n      version of them.": (
        "Ein Foto, zweimal entwickelt. Links der bestmögliche Farbfilter genau dieses Films, "
        "gebaut aus denselben Messungen, aus denen wir das Modell gebaut haben. Rechts die volle "
        "Simulation. Das ist ein 1:1-Ausschnitt, du siehst also echte Pixel und nicht eine "
        "skalierte Fassung davon.",
        "Una fotografía, revelada dos veces. A la izquierda, el mejor filtro de color posible de "
        "esta misma película, construido a partir de las mismas mediciones con las que "
        "construimos el modelo. A la derecha, la simulación completa. Es un recorte 1:1, así que "
        "estás viendo píxeles reales y no una versión redimensionada de ellos.",
        "Una fotografía, revelada dos veces. A la izquierda, el mejor filtro de color posible de "
        "esta misma película, construido a partir de las mismas mediciones con las que "
        "construimos el modelo. A la derecha, la simulación completa. Es un recorte 1:1, así que "
        "estás viendo píxeles reales y no una versión redimensionada de ellos.",
        "Une photographie, développée deux fois. À gauche, le meilleur filtre coloré possible de "
        "cette pellicule précise, construit à partir des mêmes mesures que le modèle. À droite, la "
        "simulation complète. C'est un recadrage 1:1, vous regardez donc de vrais pixels et non "
        "une version redimensionnée.",
        "Una fotografia, sviluppata due volte. A sinistra, il miglior filtro colore possibile di "
        "questa stessa pellicola, costruito dalle stesse misure con cui abbiamo costruito il "
        "modello. A destra, la simulazione completa. È un ritaglio 1:1, quindi stai guardando "
        "pixel veri e non una loro versione ridimensionata.",
        "一枚の写真を、二通りに現像しました。左は、この同じフィルムから作れる最良のカラー"
        "フィルター。モデルを組んだのと同じ実測値から作っています。右は完全なシミュレーション。"
        "これは 1:1 の切り出しなので、縮小された画像ではなく実際の画素を見ていることになります。",
        "사진 한 장을 두 번 현상했습니다. 왼쪽은 바로 이 필름으로 만들 수 있는 최선의 컬러 "
        "필터로, 모델을 만든 것과 똑같은 실측값에서 만들었습니다. 오른쪽은 완전한 시뮬레이션. "
        "1:1 크롭이라, 축소된 이미지가 아니라 실제 픽셀을 보고 계십니다.",
        "Eén foto, twee keer ontwikkeld. Links het best mogelijke kleurfilter van precies deze "
        "film, gebouwd op dezelfde metingen waarop we het model bouwden. Rechts de volledige "
        "simulatie. Dit is een 1:1-uitsnede, dus je kijkt naar echte pixels en niet naar een "
        "verkleinde versie ervan.",
        "Uma fotografia, revelada duas vezes. À esquerda, o melhor filtro de cor possível deste "
        "mesmo filme, construído a partir das mesmas medições com que construímos o modelo. À "
        "direita, a simulação completa. É um recorte 1:1, então você está vendo pixels reais e não "
        "uma versão redimensionada deles.",
        "同一张照片，显影两次。左边是用这款胶片能做出的最好的颜色滤镜，"
        "它和我们的模型来自同一批实测数据。右边是完整的模拟。这是 1:1 裁切，"
        "所以你看到的是真实像素，而不是缩放过的版本。"),
    "A 1:1 crop of bright sky seen through dark autumn branches, developed through a colour lookup "
    "table: clean, smooth, edges cut hard against the sky.": (
        "Ein 1:1-Ausschnitt von hellem Himmel durch dunkle Herbstzweige, entwickelt über eine "
        "Farbnachschlagetabelle: sauber, glatt, Kanten hart gegen den Himmel geschnitten.",
        "Un recorte 1:1 de cielo brillante visto entre ramas oscuras de otoño, revelado con una "
        "tabla de color: limpio, suave, con los bordes cortados en seco contra el cielo.",
        "Un recorte 1:1 de cielo brillante visto entre ramas oscuras de otoño, revelado con una "
        "tabla de color: limpio, suave, con los bordes cortados en seco contra el cielo.",
        "Un recadrage 1:1 de ciel clair vu à travers des branches d'automne sombres, développé "
        "avec une table de conversion : propre, lisse, les bords coupés net contre le ciel.",
        "Un ritaglio 1:1 di cielo chiaro visto attraverso rami autunnali scuri, sviluppato con una "
        "tabella colore: pulito, liscio, bordi tagliati netti contro il cielo.",
        "暗い秋の枝越しに見える明るい空の 1:1 切り出し。カラー参照表で現像したもので、清潔で、"
        "滑らかで、輪郭は空に対してくっきり切れている。",
        "어두운 가을 나뭇가지 사이로 보이는 밝은 하늘의 1:1 크롭. 컬러 룩업 테이블로 현상해 "
        "깨끗하고 매끈하며, 가장자리가 하늘을 배경으로 딱 잘려 있습니다.",
        "Een 1:1-uitsnede van heldere lucht gezien door donkere herfsttakken, ontwikkeld met een "
        "kleuropzoektabel: schoon, glad, randen hard afgesneden tegen de lucht.",
        "Um recorte 1:1 de céu claro visto por entre galhos escuros de outono, revelado com uma "
        "tabela de cores: limpo, liso, bordas cortadas secas contra o céu.",
        "透过深色秋枝看到的明亮天空，1:1 裁切，用颜色查找表显影：干净、平滑，边缘对着天空硬生生"
        "切断。"),
    "The identical crop through the full FRMT simulation: grain across the sky, and the bright sky "
    "blooming into every dark branch and leaf.": (
        "Derselbe Ausschnitt durch die volle FRMT-Simulation: Korn über den ganzen Himmel, und der "
        "helle Himmel blüht in jeden dunklen Zweig und jedes Blatt.",
        "El mismo recorte a través de la simulación completa de FRMT: grano por todo el cielo, y "
        "el cielo brillante floreciendo hacia cada rama y cada hoja oscura.",
        "El mismo recorte a través de la simulación completa de FRMT: grano por todo el cielo, y "
        "el cielo brillante floreciendo hacia cada rama y cada hoja oscura.",
        "Le même recadrage à travers la simulation complète de FRMT : du grain sur tout le ciel, "
        "et le ciel clair qui rayonne dans chaque branche et chaque feuille sombre.",
        "Lo stesso ritaglio attraverso la simulazione completa di FRMT: grana su tutto il cielo, e "
        "il cielo chiaro che fiorisce dentro ogni ramo e ogni foglia scura.",
        "同じ切り出しを FRMT の完全なシミュレーションで現像したもの。空一面に粒子が乗り、"
        "明るい空が暗い枝と葉のひとつひとつへにじんでいく。",
        "같은 크롭을 FRMT의 완전한 시뮬레이션으로 현상한 것. 하늘 전체에 입자가 얹히고, 밝은 "
        "하늘이 어두운 가지와 잎 하나하나로 번져 들어갑니다.",
        "Dezelfde uitsnede door de volledige FRMT-simulatie: korrel over de hele lucht, en de "
        "heldere lucht die in elke donkere tak en elk blad openbloeit.",
        "O mesmo recorte pela simulação completa do FRMT: grão por todo o céu, e o céu claro "
        "florescendo para dentro de cada galho e cada folha escura.",
        "同一处裁切经过 FRMT 完整模拟：整片天空带上颗粒，明亮的天空向每一根深色枝条和叶片里晕开。"),
    "Filter": ("Filter", "Filtro", "Filtro", "Filtre", "Filtro", "フィルター", "필터", "Filter",
               "Filtro", "滤镜"),
    "Drag it. The sky picks up grain, and every dark branch gets eaten into by the light behind\n"
    "        it. The filter cuts hard against the sky because a filter has no way to move light "
    "sideways.\n        Flint 64.": (
        "Zieh daran. Der Himmel bekommt Korn, und jeder dunkle Zweig wird vom Licht dahinter "
        "angefressen. Der Filter schneidet hart gegen den Himmel, weil ein Filter Licht nicht "
        "seitwärts bewegen kann. Flint 64.",
        "Arrastra. El cielo coge grano, y a cada rama oscura se la va comiendo la luz que hay "
        "detrás. El filtro corta en seco contra el cielo porque un filtro no tiene manera de mover "
        "la luz de lado. Flint 64.",
        "Arrastra. El cielo agarra grano, y a cada rama oscura se la va comiendo la luz que hay "
        "detrás. El filtro corta en seco contra el cielo porque un filtro no tiene manera de mover "
        "la luz de lado. Flint 64.",
        "Faites glisser. Le ciel prend du grain, et chaque branche sombre se fait grignoter par la "
        "lumière derrière elle. Le filtre coupe net contre le ciel parce qu'un filtre n'a aucun "
        "moyen de déplacer la lumière latéralement. Flint 64.",
        "Trascina. Il cielo prende grana, e ogni ramo scuro viene mangiato dalla luce che gli sta "
        "dietro. Il filtro taglia netto contro il cielo perché un filtro non ha modo di spostare "
        "la luce di lato. Flint 64.",
        "ドラッグしてみてください。空に粒子が乗り、暗い枝は背後の光に食い込まれていきます。"
        "フィルターが空に対してくっきり切れてしまうのは、光を横へ動かす手段を持たないからです。"
        "Flint 64。",
        "끌어 보세요. 하늘에 입자가 얹히고, 어두운 가지마다 뒤쪽의 빛이 파고듭니다. 필터가 하늘을 "
        "배경으로 딱 잘리는 것은, 필터에는 빛을 옆으로 옮길 방법이 없기 때문입니다. Flint 64.",
        "Sleep maar. De lucht krijgt korrel, en elke donkere tak wordt aangevreten door het licht "
        "erachter. Het filter snijdt hard af tegen de lucht, omdat een filter licht niet zijwaarts "
        "kan verplaatsen. Flint 64.",
        "Arraste. O céu ganha grão, e cada galho escuro vai sendo comido pela luz atrás dele. O "
        "filtro corta seco contra o céu porque um filtro não tem como mover a luz de lado. "
        "Flint 64.",
        "拖动看看。天空带上颗粒，每一根深色枝条都被它背后的光啃进去。滤镜之所以对着天空硬生生切断，"
        "是因为滤镜没有任何办法让光向侧面移动。Flint 64。"),
    "Zoom back out and it is everywhere. Here is every place the two versions disagree across the\n"
    "      whole frame, amplified and shown on its own. This is the light a filter cannot produce,\n"
    "      because producing it means moving light across the frame rather than recolouring it in "
    "place.": (
        "Zoom wieder heraus, und es ist überall. Hier ist jede Stelle, an der die beiden Fassungen "
        "über das ganze Bild hinweg voneinander abweichen, verstärkt und für sich gezeigt. Das ist "
        "das Licht, das ein Filter nicht erzeugen kann, weil es zu erzeugen bedeutet, Licht über "
        "das Bild zu bewegen, statt es an Ort und Stelle umzufärben.",
        "Aleja el zoom y está por todas partes. Aquí está cada punto en el que las dos versiones "
        "discrepan a lo largo de todo el fotograma, amplificado y mostrado por separado. Esta es "
        "la luz que un filtro no puede producir, porque producirla significa mover luz por el "
        "encuadre en vez de recolorearla en el sitio.",
        "Aleja el zoom y está por todas partes. Aquí está cada punto en el que las dos versiones "
        "discrepan a lo largo de todo el cuadro, amplificado y mostrado por separado. Esta es la "
        "luz que un filtro no puede producir, porque producirla significa mover luz por el "
        "encuadre en vez de recolorearla en el sitio.",
        "Dézoomez et c'est partout. Voici chaque endroit où les deux versions divergent sur toute "
        "l'image, amplifié et montré seul. C'est la lumière qu'un filtre ne peut pas produire, "
        "parce que la produire suppose de déplacer de la lumière à travers l'image plutôt que de "
        "la recolorer sur place.",
        "Allarga di nuovo ed è ovunque. Ecco ogni punto in cui le due versioni non vanno d'accordo "
        "su tutto il fotogramma, amplificato e mostrato da solo. È la luce che un filtro non può "
        "produrre, perché produrla significa spostare luce attraverso l'inquadratura invece di "
        "ricolorarla sul posto.",
        "引きで見ると、それは画面じゅうにあります。ここに出しているのは、二つの版が食い違って"
        "いる場所を一枚ぶんすべて拾い、強調して単独で示したものです。これは、フィルターには"
        "つくれない光です。つくるには、その場で色を塗り替えるのではなく、光を画面の上で"
        "動かさなければならないからです。",
        "다시 축소해 보면 그것은 화면 전체에 있습니다. 여기 있는 것은 두 버전이 어긋나는 모든 "
        "자리를 한 프레임 전체에서 모아, 강조해 따로 보여 준 것입니다. 이것이 필터로는 만들 수 "
        "없는 빛입니다. 만들려면 제자리에서 색을 다시 칠하는 게 아니라, 화면을 가로질러 빛을 "
        "옮겨야 하기 때문입니다.",
        "Zoom weer uit en het zit overal. Hier is elke plek waar de twee versies over het hele "
        "beeld van elkaar verschillen, versterkt en apart getoond. Dit is het licht dat een filter "
        "niet kan maken, want het maken betekent licht over het beeld verplaatsen in plaats van "
        "het ter plekke te verkleuren.",
        "Afaste o zoom e está em todo lugar. Aqui está cada ponto em que as duas versões discordam "
        "ao longo do quadro inteiro, amplificado e mostrado sozinho. Esta é a luz que um filtro "
        "não consegue produzir, porque produzi-la significa mover luz pelo enquadramento em vez de "
        "recolori-la no lugar.",
        "把画面拉回来看，它到处都是。这里呈现的是整张画面上两个版本不一致的每一处，"
        "放大后单独显示。这就是滤镜做不出的光，因为要做出它，就得让光在画面上移动，"
        "而不是就地重新上色。"),
    "A dark field showing only the difference between the two versions: warm light tracing every "
    "lit leaf, branch and edge in the frame.": (
        "Ein dunkles Feld, das nur den Unterschied zwischen den beiden Fassungen zeigt: warmes "
        "Licht, das jedes beleuchtete Blatt, jeden Zweig und jede Kante im Bild nachzeichnet.",
        "Un campo oscuro que muestra solo la diferencia entre las dos versiones: luz cálida "
        "trazando cada hoja, rama y borde iluminado del encuadre.",
        "Un campo oscuro que muestra solo la diferencia entre las dos versiones: luz cálida "
        "trazando cada hoja, rama y borde iluminado del encuadre.",
        "Un champ sombre montrant seulement la différence entre les deux versions : une lumière "
        "chaude qui trace chaque feuille, branche et arête éclairée de l'image.",
        "Un campo scuro che mostra solo la differenza fra le due versioni: luce calda che traccia "
        "ogni foglia, ramo e bordo illuminato dell'inquadratura.",
        "二つの版の差だけを示した暗い画面。画面のなかで光を受けた葉、枝、輪郭のひとつひとつを、"
        "暖かい光がなぞっている。",
        "두 버전의 차이만 보여 주는 어두운 화면. 화면 안에서 빛을 받은 잎과 가지와 가장자리 "
        "하나하나를 따뜻한 빛이 따라 그리고 있습니다.",
        "Een donker veld dat alleen het verschil tussen de twee versies toont: warm licht dat elk "
        "verlicht blad, elke tak en elke rand in beeld natrekt.",
        "Um campo escuro mostrando só a diferença entre as duas versões: luz quente traçando cada "
        "folha, galho e borda iluminada do quadro.",
        "一片黑色画面，只显示两个版本之间的差异：暖色的光勾勒出画面中每一片受光的叶子、枝条和边缘。"),
    "The gap between a filter and a film, isolated. One real frame.": (
        "Der Abstand zwischen Filter und Film, isoliert. Ein echtes Bild.",
        "La distancia entre un filtro y una película, aislada. Un fotograma real.",
        "La distancia entre un filtro y una película, aislada. Un cuadro real.",
        "L'écart entre un filtre et une pellicule, isolé. Une image réelle.",
        "La distanza fra un filtro e una pellicola, isolata. Un fotogramma vero.",
        "フィルターとフィルムのあいだの隔たりだけを取り出したもの。実際の一枚から。",
        "필터와 필름 사이의 간극만 떼어 낸 것. 실제 한 프레임에서.",
        "De kloof tussen een filter en een film, geïsoleerd. Eén echt beeld.",
        "A distância entre um filtro e um filme, isolada. Um quadro real.",
        "把滤镜与胶片之间的落差单独提取出来。取自真实的一张。"),
}

# ---------------------------------------------------------------- mechanisms, stocks, FAQ
T.update({
    "Three things a filter cannot do": (
        "Drei Dinge, die ein Filter nicht kann", "Tres cosas que un filtro no puede hacer",
        "Tres cosas que un filtro no puede hacer", "Trois choses qu'un filtre ne sait pas faire",
        "Tre cose che un filtro non può fare", "フィルターにできない三つのこと",
        "필터가 할 수 없는 세 가지", "Drie dingen die een filter niet kan",
        "Três coisas que um filtro não consegue fazer", "滤镜做不到的三件事"),
    "What your phone is actually calculating.": (
        "Was dein Telefon tatsächlich rechnet.", "Lo que tu móvil está calculando de verdad.",
        "Lo que tu celular está calculando de verdad.",
        "Ce que votre téléphone calcule vraiment.", "Cosa sta calcolando davvero il tuo telefono.",
        "あなたの端末が実際に計算していること。", "당신의 휴대폰이 실제로 계산하고 있는 것.",
        "Wat je telefoon werkelijk berekent.", "O que o seu telefone está de fato calculando.",
        "你的手机实际上在算什么。"),
    "Every photograph goes through these in order, the same order a negative goes through them,\n"
    "      on the graphics processor in your phone.": (
        "Jedes Foto durchläuft diese der Reihe nach, in derselben Reihenfolge wie ein Negativ, auf "
        "dem Grafikprozessor in deinem Telefon.",
        "Cada fotografía pasa por estos en orden, el mismo orden por el que pasa un negativo, en "
        "el procesador gráfico de tu móvil.",
        "Cada fotografía pasa por estos en orden, el mismo orden por el que pasa un negativo, en "
        "el procesador gráfico de tu celular.",
        "Chaque photographie les traverse dans l'ordre, le même ordre qu'un négatif, sur le "
        "processeur graphique de votre téléphone.",
        "Ogni fotografia li attraversa in ordine, lo stesso ordine di un negativo, sul processore "
        "grafico del tuo telefono.",
        "どの写真も、ネガがたどるのと同じ順番でこれらを通っていきます。あなたの端末の"
        "グラフィックスプロセッサの上で。",
        "모든 사진이 네거티브가 거치는 것과 같은 순서로 이 과정을 지나갑니다. 당신 휴대폰의 그래픽 "
        "프로세서 위에서.",
        "Elke foto gaat hier in volgorde doorheen, dezelfde volgorde als een negatief, op de "
        "grafische processor in je telefoon.",
        "Cada fotografia passa por estes em ordem, a mesma ordem por que passa um negativo, no "
        "processador gráfico do seu telefone.",
        "每一张照片都会按顺序走完这些步骤，和一张底片经历的顺序一样，就在你手机的图形处理器上。"),
    "01 · Halation": ("01 · Lichthofbildung", "01 · Halación", "01 · Halación", "01 · Halo",
                      "01 · Alone", "01 · ハレーション", "01 · 헐레이션", "01 · Lichthof",
                      "01 · Halação", "01 · 光晕"),
    "Light goes in, and comes back out beside itself.": (
        "Licht geht hinein und kommt daneben wieder heraus.",
        "La luz entra y vuelve a salir al lado de sí misma.",
        "La luz entra y vuelve a salir al lado de sí misma.",
        "La lumière entre et ressort à côté d'elle-même.",
        "La luce entra ed esce di nuovo accanto a se stessa.",
        "光は入っていき、自分のすぐ隣から出てくる。",
        "빛은 들어갔다가 자기 바로 옆으로 다시 나옵니다.",
        "Licht gaat erin en komt er naast zichzelf weer uit.",
        "A luz entra e volta a sair ao lado de si mesma.",
        "光进去，又从紧挨着自己的地方回来。"),
    "Some light passes clean through the emulsion, reflects off the base underneath, and\n"
    "          exposes the film a second time next to where it entered. Bright things do not stop "
    "at\n          their edges. They bleed into what surrounds them.": (
        "Ein Teil des Lichts geht glatt durch die Emulsion, wird von der Trägerschicht darunter "
        "reflektiert und belichtet den Film ein zweites Mal neben der Stelle, an der es eintrat. "
        "Helle Dinge hören an ihren Kanten nicht auf. Sie bluten in das aus, was sie umgibt.",
        "Parte de la luz atraviesa limpiamente la emulsión, se refleja en el soporte de debajo y "
        "expone la película una segunda vez junto a donde entró. Las cosas brillantes no se paran "
        "en sus bordes. Se derraman en lo que las rodea.",
        "Parte de la luz atraviesa limpiamente la emulsión, se refleja en el soporte de debajo y "
        "expone la película una segunda vez junto a donde entró. Las cosas brillantes no se paran "
        "en sus bordes. Se derraman en lo que las rodea.",
        "Une partie de la lumière traverse franchement l'émulsion, se réfléchit sur le support en "
        "dessous et expose la pellicule une seconde fois à côté de son point d'entrée. Les choses "
        "claires ne s'arrêtent pas à leurs bords. Elles débordent sur ce qui les entoure.",
        "Una parte della luce attraversa netta l'emulsione, si riflette sul supporto sotto ed "
        "espone la pellicola una seconda volta accanto a dove è entrata. Le cose luminose non si "
        "fermano ai loro bordi. Sbordano in ciò che le circonda.",
        "光の一部は乳剤をまっすぐ通り抜け、その下のベースで反射して、入ってきた場所のすぐ隣で"
        "フィルムをもう一度感光させます。明るいものは自分の輪郭で止まりません。"
        "まわりのものへにじみ出します。",
        "빛의 일부는 유제를 그대로 통과해 아래 베이스에서 반사되고, 들어온 자리 바로 옆에서 필름을 "
        "한 번 더 노광시킵니다. 밝은 것들은 자기 가장자리에서 멈추지 않습니다. 주변으로 번져 "
        "나갑니다.",
        "Een deel van het licht gaat schoon door de emulsie heen, weerkaatst op de drager eronder "
        "en belicht de film een tweede keer naast de plek waar het binnenkwam. Heldere dingen "
        "stoppen niet bij hun randen. Ze lopen door in wat hen omringt.",
        "Parte da luz atravessa limpa a emulsão, reflete na base embaixo e expõe o filme uma "
        "segunda vez ao lado de onde entrou. Coisas claras não param nas suas bordas. Elas vazam "
        "para o que está em volta.",
        "一部分光会干净利落地穿过乳剂，在下面的片基上反射，再在它进入处的旁边把胶片第二次曝光。"
        "明亮的东西不会停在自己的边缘上。它们会渗进周围。"),
    "You notice it in: neon, streetlights, windows, sun through leaves.": (
        "Du siehst es bei: Neon, Straßenlaternen, Fenstern, Sonne durch Blätter.",
        "Se nota en: neón, farolas, ventanas, sol entre las hojas.",
        "Se nota en: neón, luminarias, ventanas, sol entre las hojas.",
        "On le remarque sur : le néon, les lampadaires, les fenêtres, le soleil à travers les "
        "feuilles.",
        "Si nota su: neon, lampioni, finestre, sole fra le foglie.",
        "気づきやすいのは、ネオン、街灯、窓、木漏れ日。",
        "네온, 가로등, 창문, 나뭇잎 사이로 드는 햇빛에서 눈에 띕니다.",
        "Je ziet het bij: neon, straatlantaarns, ramen, zon door bladeren.",
        "Dá para notar em: neon, postes de luz, janelas, sol entre as folhas.",
        "在这些地方最容易看到：霓虹、路灯、窗户、穿过树叶的阳光。"),
    "02 · Interimage effects": (
        "02 · Interimage-Effekte", "02 · Efectos interimagen", "02 · Efectos interimagen",
        "02 · Effets inter-image", "02 · Effetti interimmagine", "02 · インターイメージ効果",
        "02 · 인터이미지 효과", "02 · Interimage-effecten", "02 · Efeitos interimagem",
        "02 · 层间效应"),
    "The colour layers argue with each other.": (
        "Die Farbschichten streiten miteinander.", "Las capas de color discuten entre sí.",
        "Las capas de color discuten entre sí.", "Les couches de couleur se disputent.",
        "Gli strati di colore litigano fra loro.", "色の層どうしが言い合いをする。",
        "색 층들이 서로 다툽니다.", "De kleurlagen ruziën met elkaar.",
        "As camadas de cor discutem entre si.", "各个色层彼此争执。"),
    "As dye develops in one layer it releases a chemical that drifts sideways and holds back\n"
    "          its neighbours. This is most of what gives a stock its colour signature, and it is "
    "why a\n          red stays red when it sits against a green instead of both sliding toward "
    "brown.": (
        "Während in einer Schicht Farbstoff entsteht, setzt sie eine Chemikalie frei, die "
        "seitwärts wandert und ihre Nachbarn zurückhält. Das macht den größten Teil der "
        "Farbsignatur eines Films aus, und es ist der Grund, warum ein Rot rot bleibt, wenn es "
        "neben einem Grün liegt, statt dass beide ins Braune rutschen.",
        "Mientras el colorante se revela en una capa, libera una sustancia que se desplaza de lado "
        "y frena a sus vecinas. Eso es la mayor parte de lo que da a una película su firma de "
        "color, y es la razón de que un rojo siga siendo rojo cuando está junto a un verde en vez "
        "de deslizarse los dos hacia el marrón.",
        "Mientras el colorante se revela en una capa, libera una sustancia que se desplaza de lado "
        "y frena a sus vecinas. Eso es la mayor parte de lo que da a una película su firma de "
        "color, y es la razón de que un rojo siga siendo rojo cuando está junto a un verde en vez "
        "de deslizarse los dos hacia el café.",
        "Pendant que le colorant se développe dans une couche, il libère un composé qui migre "
        "latéralement et retient ses voisines. C'est l'essentiel de ce qui donne sa signature "
        "colorée à une pellicule, et la raison pour laquelle un rouge reste rouge quand il jouxte "
        "un vert, au lieu que les deux glissent vers le brun.",
        "Mentre il colorante si sviluppa in uno strato, libera una sostanza che migra di lato e "
        "trattiene i vicini. È gran parte di ciò che dà a una pellicola la sua firma cromatica, ed "
        "è il motivo per cui un rosso resta rosso quando sta accanto a un verde invece di scivolare "
        "entrambi verso il marrone.",
        "ある層で色素が現像されるとき、化学物質が放たれ、それが横へ拡がって隣の層を抑えます。"
        "フィルムの色の個性の大半はここで決まり、赤が緑と隣り合っても両方が茶色へ寄っていかず、"
        "赤のままでいられるのもこのためです。",
        "한 층에서 염료가 현상되는 동안 화학 물질이 나와 옆으로 퍼지며 이웃한 층을 붙잡습니다. "
        "필름의 색 개성은 대부분 여기서 나오고, 빨강이 초록 옆에 놓여도 둘 다 갈색으로 흘러가지 "
        "않고 빨강으로 남는 이유이기도 합니다.",
        "Terwijl kleurstof in de ene laag ontstaat, laat die een stof vrij die zijwaarts wegdrijft "
        "en zijn buren tegenhoudt. Dit is het grootste deel van wat een film zijn kleursignatuur "
        "geeft, en waarom een rood rood blijft naast een groen in plaats van dat beide naar bruin "
        "wegglijden.",
        "Enquanto o corante se revela numa camada, ele libera uma substância que migra de lado e "
        "segura as vizinhas. Isso é a maior parte do que dá a um filme sua assinatura de cor, e é "
        "o motivo de um vermelho continuar vermelho ao lado de um verde em vez de ambos "
        "escorregarem para o marrom.",
        "当某一层显出染料时，它会释放一种化学物质，向侧面扩散，拖住相邻的层。"
        "一款胶片的色彩个性大半由此而来，也正因为如此，红色挨着绿色时仍然是红色，"
        "而不是两者一起滑向褐色。"),
    "You notice it in: foliage, skin against colour, anything saturated.": (
        "Du siehst es bei: Laub, Haut neben Farbe, allem Gesättigten.",
        "Se nota en: follaje, piel junto a color, cualquier cosa saturada.",
        "Se nota en: follaje, piel junto a color, cualquier cosa saturada.",
        "On le remarque sur : le feuillage, la peau à côté d'une couleur, tout ce qui est saturé.",
        "Si nota su: fogliame, pelle accanto al colore, qualsiasi cosa satura.",
        "気づきやすいのは、木々、色と隣り合う肌、彩度の高いものすべて。",
        "나뭇잎, 색 옆에 놓인 피부, 채도가 높은 모든 것에서 눈에 띕니다.",
        "Je ziet het bij: gebladerte, huid naast kleur, alles wat verzadigd is.",
        "Dá para notar em: folhagem, pele ao lado de cor, qualquer coisa saturada.",
        "在这些地方最容易看到：树叶、与色彩相邻的肤色、任何高饱和的东西。"),
    "03 · Grain": ("03 · Korn", "03 · Grano", "03 · Grano", "03 · Grain", "03 · Grana",
                   "03 · 粒子", "03 · 입자", "03 · Korrel", "03 · Grão", "03 · 颗粒"),
    "Not a texture laid on top.": (
        "Keine Textur, die obendrauf gelegt wird.", "No es una textura puesta encima.",
        "No es una textura puesta encima.", "Pas une texture posée par-dessus.",
        "Non una texture messa sopra.", "上に乗せたテクスチャではない。",
        "위에 얹은 질감이 아닙니다.", "Geen textuur die er bovenop ligt.",
        "Não é uma textura posta por cima.", "不是盖在上面的一层纹理。"),
    "Grain here is the actual variation in how much dye formed, spot by spot, so it follows\n"
    "          the tones instead of sitting over them. Strongest through the midtones, almost gone "
    "in\n          deep shadow, and it moves when your exposure moves.": (
        "Korn ist hier die tatsächliche Schwankung darin, wie viel Farbstoff entstanden ist, "
        "Stelle für Stelle, es folgt also den Tönen, statt über ihnen zu liegen. Am stärksten "
        "durch die Mitteltöne, im tiefen Schatten fast weg, und es wandert mit, wenn sich deine "
        "Belichtung ändert.",
        "Aquí el grano es la variación real de cuánto colorante llegó a formarse, punto a punto, "
        "así que sigue a los tonos en vez de posarse sobre ellos. Más fuerte por los medios tonos, "
        "casi ausente en las sombras profundas, y se mueve cuando se mueve tu exposición.",
        "Aquí el grano es la variación real de cuánto colorante llegó a formarse, punto a punto, "
        "así que sigue a los tonos en vez de posarse sobre ellos. Más fuerte por los medios tonos, "
        "casi ausente en las sombras profundas, y se mueve cuando se mueve tu exposición.",
        "Ici, le grain est la variation réelle de la quantité de colorant formée, point par point, "
        "il suit donc les tonalités au lieu de se poser dessus. Le plus fort dans les tons moyens, "
        "presque absent dans les ombres profondes, et il bouge quand votre exposition bouge.",
        "Qui la grana è la variazione reale di quanto colorante si è formato, punto per punto, "
        "quindi segue i toni invece di stare sopra di essi. Più forte nei mezzitoni, quasi sparita "
        "nelle ombre profonde, e si sposta quando si sposta la tua esposizione.",
        "ここでの粒子は、色素が実際にどれだけできたかの場所ごとのばらつきそのものです。"
        "だから階調の上に乗るのではなく、階調に従います。中間調で最も強く、深い影ではほとんど"
        "消え、露出を動かせば粒子も動きます。",
        "여기서 입자는 염료가 실제로 얼마나 만들어졌는지의 자리별 편차 그 자체입니다. 그래서 계조 "
        "위에 얹히는 대신 계조를 따라갑니다. 중간톤에서 가장 강하고 깊은 그림자에서는 거의 "
        "사라지며, 노출을 옮기면 입자도 옮겨 갑니다.",
        "Korrel is hier de werkelijke variatie in hoeveel kleurstof zich vormde, plek voor plek, "
        "dus hij volgt de tonen in plaats van erop te liggen. Het sterkst door de middentonen, "
        "bijna weg in diepe schaduw, en hij beweegt mee als je belichting beweegt.",
        "Aqui o grão é a variação real de quanto corante se formou, ponto a ponto, então ele segue "
        "os tons em vez de ficar por cima deles. Mais forte pelos meios-tons, quase ausente nas "
        "sombras profundas, e se move quando a sua exposição se move.",
        "这里的颗粒就是染料实际生成量在一处处之间的起伏本身，所以它跟着影调走，而不是压在影调上。"
        "在中间调最强，在深暗部几乎消失，你的曝光一动，它也跟着动。"),
    "You notice it in: skies, skin, flat walls, anywhere a fake grain layer looks pasted on.": (
        "Du siehst es bei: Himmeln, Haut, glatten Wänden, überall dort, wo eine falsche Kornebene "
        "aufgeklebt wirkt.",
        "Se nota en: cielos, piel, paredes lisas, en cualquier sitio donde una capa de grano falso "
        "parece pegada encima.",
        "Se nota en: cielos, piel, paredes lisas, en cualquier lugar donde una capa de grano falso "
        "parece pegada encima.",
        "On le remarque sur : les ciels, la peau, les murs lisses, partout où une fausse couche de "
        "grain a l'air collée.",
        "Si nota su: cieli, pelle, muri lisci, ovunque uno strato di grana finta sembri incollato "
        "sopra.",
        "気づきやすいのは、空、肌、平らな壁。偽の粒子レイヤーが貼りつけたように見える場所すべて。",
        "하늘, 피부, 평평한 벽처럼 가짜 입자 레이어가 붙여 놓은 것처럼 보이는 모든 곳에서 눈에 "
        "띕니다.",
        "Je ziet het bij: luchten, huid, vlakke muren, overal waar een nep-korrellaag erop geplakt "
        "lijkt.",
        "Dá para notar em: céus, pele, paredes lisas, em qualquer lugar onde uma camada de grão "
        "falso parece colada por cima.",
        "在这些地方最容易看到：天空、皮肤、平整的墙面，以及任何假颗粒图层看起来像贴上去的地方。"),
    "Halation, on its own": (
        "Lichthofbildung, für sich", "La halación, por sí sola", "La halación, por sí sola",
        "Le halo, seul", "L'alone, da solo", "ハレーションだけを取り出して",
        "헐레이션만 따로", "Lichthof, op zichzelf", "A halação, sozinha", "单看光晕"),
    "This is real, and it is in every frame.": (
        "Das ist echt, und es steckt in jedem Bild.",
        "Esto es real, y está en cada fotograma.", "Esto es real, y está en cada cuadro.",
        "C'est réel, et c'est dans chaque image.", "Questo è reale, ed è in ogni fotogramma.",
        "これは実在していて、どの一枚にも入っています。",
        "이것은 실재하고, 모든 프레임에 들어 있습니다.",
        "Dit is echt, en het zit in elk beeld.", "Isto é real, e está em cada quadro.",
        "这是真实存在的，而且每一张里都有。"),
    "The returning light from a single photograph, pulled out and amplified so you can see it.\n"
    "      Nothing here was painted on. It is what the model produced from the negative.": (
        "Das zurückkehrende Licht aus einem einzigen Foto, herausgezogen und verstärkt, damit du "
        "es sehen kannst. Nichts davon wurde aufgemalt. Es ist das, was das Modell aus dem Negativ "
        "erzeugt hat.",
        "La luz que vuelve, de una sola fotografía, extraída y amplificada para que puedas verla. "
        "Aquí no se ha pintado nada. Es lo que el modelo produjo a partir del negativo.",
        "La luz que regresa, de una sola fotografía, extraída y amplificada para que puedas verla. "
        "Aquí no se pintó nada. Es lo que el modelo produjo a partir del negativo.",
        "La lumière de retour d'une seule photographie, extraite et amplifiée pour que vous la "
        "voyiez. Rien n'a été peint ici. C'est ce que le modèle a produit à partir du négatif.",
        "La luce di ritorno da una sola fotografia, estratta e amplificata perché tu la veda. Qui "
        "non è stato dipinto niente. È ciò che il modello ha prodotto dal negativo.",
        "一枚の写真から戻ってきた光だけを取り出し、見えるように強調したものです。"
        "描き足したものは何もありません。モデルがネガから生み出したそのままです。",
        "사진 한 장에서 되돌아온 빛만 뽑아내어, 보이도록 강조한 것입니다. 여기에 덧그린 것은 "
        "없습니다. 모델이 네거티브로부터 만들어 낸 그대로입니다.",
        "Het terugkerende licht uit één enkele foto, eruit gehaald en versterkt zodat je het kunt "
        "zien. Hier is niets op geschilderd. Het is wat het model uit het negatief heeft "
        "voortgebracht.",
        "A luz que volta, de uma única fotografia, extraída e amplificada para você poder ver. "
        "Nada aqui foi pintado. É o que o modelo produziu a partir do negativo.",
        "从一张照片里提取出来、并加以放大的回返光，好让你看得见。这里没有任何东西是画上去的。"
        "这是模型从底片算出来的结果。"),
    "A false-colour field showing only the returning light in one photograph: warm outlines "
    "tracing every bright edge of a castle at night.": (
        "Ein Falschfarbenfeld, das nur das zurückkehrende Licht in einem Foto zeigt: warme "
        "Umrisse, die jede helle Kante einer Burg bei Nacht nachzeichnen.",
        "Un campo en falso color que muestra solo la luz que vuelve en una fotografía: contornos "
        "cálidos trazando cada borde iluminado de un castillo de noche.",
        "Un campo en falso color que muestra solo la luz que regresa en una fotografía: contornos "
        "cálidos trazando cada borde iluminado de un castillo de noche.",
        "Un champ en fausses couleurs montrant seulement la lumière de retour dans une "
        "photographie : des contours chauds qui tracent chaque arête éclairée d'un château la nuit.",
        "Un campo in falsi colori che mostra solo la luce di ritorno in una fotografia: contorni "
        "caldi che tracciano ogni bordo illuminato di un castello di notte.",
        "一枚の写真のなかの戻ってきた光だけを疑似カラーで示した画面。夜の城の明るい輪郭を、"
        "暖かい線がひとつひとつなぞっている。",
        "사진 한 장 안에서 되돌아온 빛만 의사 색으로 보여 주는 화면. 밤의 성에서 밝은 가장자리 "
        "하나하나를 따뜻한 윤곽선이 따라 그리고 있습니다.",
        "Een veld in valse kleuren dat alleen het terugkerende licht in één foto toont: warme "
        "contouren die elke lichte rand van een kasteel bij nacht natrekken.",
        "Um campo em falsa cor mostrando só a luz que volta numa fotografia: contornos quentes "
        "traçando cada borda iluminada de um castelo à noite.",
        "一张伪彩色画面，只显示一张照片中回返的光：暖色的轮廓线勾出夜色中城堡每一道明亮的边缘。"),
    "Four stocks": ("Vier Filme", "Cuatro películas", "Cuatro películas", "Quatre pellicules",
                    "Quattro pellicole", "フィルム四種", "필름 네 가지", "Vier films",
                    "Quatro filmes", "四款胶片"),
    "Measured, not styled.": (
        "Gemessen, nicht gestylt.", "Medidas, no estilizadas.", "Medidas, no estilizadas.",
        "Mesurées, pas stylisées.", "Misurate, non stilizzate.", "演出ではなく、実測。",
        "연출이 아니라 측정입니다.", "Gemeten, niet gestyled.", "Medidos, não estilizados.",
        "是测出来的，不是调出来的。"),
    "The numbers behind each one come off its manufacturer's own published datasheet: the response\n"
    "      curves, the spectral sensitivity, the grain figures. Nobody sat down and eyeballed a "
    "preset\n      until it looked about right.": (
        "Die Zahlen hinter jedem stammen vom veröffentlichten Datenblatt des jeweiligen "
        "Herstellers: die Kennlinien, die spektrale Empfindlichkeit, die Kornwerte. Niemand hat "
        "sich hingesetzt und ein Preset nach Augenmaß justiert, bis es ungefähr passte.",
        "Los números detrás de cada una salen de la hoja de datos publicada por su propio "
        "fabricante: las curvas de respuesta, la sensibilidad espectral, las cifras de grano. "
        "Nadie se sentó a ajustar un preajuste a ojo hasta que quedó más o menos bien.",
        "Los números detrás de cada una salen de la hoja de datos publicada por su propio "
        "fabricante: las curvas de respuesta, la sensibilidad espectral, las cifras de grano. "
        "Nadie se sentó a ajustar una predefinición a ojo hasta que quedó más o menos bien.",
        "Les nombres derrière chacune viennent de la fiche technique publiée par son propre "
        "fabricant : les courbes de réponse, la sensibilité spectrale, les chiffres de grain. "
        "Personne ne s'est assis pour régler un préréglage à l'oeil jusqu'à ce que ça paraisse à "
        "peu près juste.",
        "I numeri dietro a ciascuna vengono dalla scheda tecnica pubblicata dal suo stesso "
        "produttore: le curve di risposta, la sensibilità spettrale, i dati di grana. Nessuno si è "
        "seduto a regolare un preset a occhio finché non sembrava più o meno giusto.",
        "それぞれの背後にある数値は、そのメーカー自身が公開したデータシートから取っています。"
        "応答曲線、分光感度、粒状性の数値。誰かが座って、それらしく見えるまで目分量でプリセットを"
        "いじった、ということはありません。",
        "각각의 뒤에 있는 수치는 그 제조사가 직접 공개한 데이터시트에서 가져온 것입니다. 응답 "
        "곡선, 분광 감도, 입상성 수치. 누군가 앉아서 그럴듯해 보일 때까지 눈대중으로 프리셋을 "
        "만진 것이 아닙니다.",
        "De getallen achter elk ervan komen van het gepubliceerde datasheet van de fabrikant zelf: "
        "de responscurves, de spectrale gevoeligheid, de korrelcijfers. Niemand is gaan zitten om "
        "op het oog een preset bij te stellen tot het er ongeveer goed uitzag.",
        "Os números por trás de cada um saem da ficha técnica publicada pelo próprio fabricante: "
        "as curvas de resposta, a sensibilidade espectral, os dados de grão. Ninguém sentou para "
        "ajustar uma predefinição no olho até ficar mais ou menos certo.",
        "每一款背后的数值都来自其厂商自己公开的数据表：响应曲线、光谱感光度、颗粒数据。"
        "没有谁坐下来凭眼睛去调一个预设，调到看着差不多为止。"),
    "You load one at a time, the way you load a roll. There is no look picker on the capture "
    "screen\n      and there are no sliders, and none of the four is a variation on another.": (
        "Du legst einen nach dem anderen ein, so wie man einen Film einlegt. Auf dem "
        "Aufnahmebildschirm gibt es keine Auswahl von Looks und keine Regler, und keiner der vier "
        "ist eine Variante eines anderen.",
        "Cargas una cada vez, como se carga un carrete. No hay selector de estilos en la pantalla "
        "de captura ni hay controles deslizantes, y ninguna de las cuatro es una variación de otra.",
        "Cargas una a la vez, como se carga un rollo. No hay selector de estilos en la pantalla de "
        "captura ni hay controles deslizantes, y ninguna de las cuatro es una variación de otra.",
        "Vous en chargez une à la fois, comme on charge une pellicule. Il n'y a pas de sélecteur "
        "de rendu sur l'écran de prise de vue ni de curseurs, et aucune des quatre n'est une "
        "variante d'une autre.",
        "Ne carichi una alla volta, come si carica un rullino. Sulla schermata di scatto non c'è "
        "un selettore di look e non ci sono cursori, e nessuna delle quattro è una variante di "
        "un'altra.",
        "ロールと同じで、一度に一本だけ装填します。撮影画面にはルックの一覧もスライダーもなく、"
        "四種のどれかがほかの派生ということもありません。",
        "롤을 넣듯이 한 번에 하나씩 장전합니다. 촬영 화면에는 룩 목록도 슬라이더도 없고, 네 가지 "
        "중 어느 하나도 다른 것의 변형이 아닙니다.",
        "Je laadt er één tegelijk, zoals je een rolletje laadt. Op het opnamescherm zit geen "
        "lookkiezer en er zijn geen schuifjes, en geen van de vier is een variatie op een andere.",
        "Você carrega um de cada vez, do jeito que se carrega um rolo. Não há seletor de visual na "
        "tela de captura nem controles deslizantes, e nenhum dos quatro é uma variação de outro.",
        "像装胶卷一样，一次只装一款。拍摄界面上没有风格列表，也没有滑块，"
        "而且四款之中没有哪一款是另一款的变体。"),
    "Punchy and saturated. Landscape, foliage, sunsets.": (
        "Kräftig und gesättigt. Landschaft, Laub, Sonnenuntergänge.",
        "Intensa y saturada. Paisaje, follaje, puestas de sol.",
        "Intensa y saturada. Paisaje, follaje, atardeceres.",
        "Punchy et saturée. Paysage, feuillage, couchers de soleil.",
        "Decisa e satura. Paesaggio, fogliame, tramonti.",
        "力強く彩度が高い。風景、木々、夕景。",
        "강하고 채도가 높습니다. 풍경, 나뭇잎, 노을.",
        "Krachtig en verzadigd. Landschap, gebladerte, zonsondergangen.",
        "Intenso e saturado. Paisagem, folhagem, pôr do sol.",
        "浓郁饱和。风景、树叶、日落。"),
    "Neutral and even. Travel, streets, mixed light.": (
        "Neutral und ausgeglichen. Reisen, Straßen, gemischtes Licht.",
        "Neutra y pareja. Viajes, calles, luz mixta.",
        "Neutra y pareja. Viajes, calles, luz mixta.",
        "Neutre et régulière. Voyage, rue, lumière mixte.",
        "Neutra e uniforme. Viaggi, strade, luce mista.",
        "ニュートラルで素直。旅、街、混合光。",
        "중립적이고 고릅니다. 여행, 거리, 혼합광.",
        "Neutraal en gelijkmatig. Reizen, straten, gemengd licht.",
        "Neutro e parelho. Viagem, ruas, luz mista.",
        "中性均衡。旅行、街道、混合光。"),
    "Soft and fine-grained. People, portraits, overcast days.": (
        "Weich und feinkörnig. Menschen, Porträts, bedeckte Tage.",
        "Suave y de grano fino. Personas, retratos, días nublados.",
        "Suave y de grano fino. Personas, retratos, días nublados.",
        "Douce et à grain fin. Les gens, le portrait, les jours couverts.",
        "Morbida e a grana fine. Persone, ritratti, giornate coperte.",
        "軟らかく粒子が細かい。人、ポートレート、曇りの日。",
        "부드럽고 입자가 곱습니다. 인물, 초상, 흐린 날.",
        "Zacht en fijnkorrelig. Mensen, portretten, bewolkte dagen.",
        "Suave e de grão fino. Pessoas, retratos, dias nublados.",
        "柔和、颗粒细。人、人像、阴天。"),
    "Grainy and warm with cool shadows. Street, hard light, neon.": (
        "Körnig und warm mit kühlen Schatten. Straße, hartes Licht, Neon.",
        "Con grano y cálida, con sombras frías. Calle, luz dura, neón.",
        "Con grano y cálida, con sombras frías. Calle, luz dura, neón.",
        "Granuleuse et chaude avec des ombres froides. Rue, lumière dure, néon.",
        "Granulosa e calda con ombre fredde. Strada, luce dura, neon.",
        "粒子が粗く暖かい、影は冷たい。街、硬い光、ネオン。",
        "입자가 굵고 따뜻하며 그림자는 차갑습니다. 거리, 강한 빛, 네온.",
        "Korrelig en warm met koele schaduwen. Straat, hard licht, neon.",
        "Granulado e quente com sombras frias. Rua, luz dura, neon.",
        "颗粒粗、色调暖，暗部偏冷。街头、硬光、霓虹。"),
})

# ---------------------------------------------------------------- workflow, price, FAQ, JSON-LD
#
# The FAQ answers appear twice: once as visible copy and once inside FAQPage structured data. Both
# are translated from the same entries here, so they cannot drift apart. Google requires the
# structured data to match what a visitor can read, and an answer engine quoting one while the page
# shows the other is exactly the failure to avoid.
T.update({
    "How it works": ("Wie es abläuft", "Cómo funciona", "Cómo funciona", "Comment ça marche",
                     "Come funziona", "使い方", "어떻게 작동하나", "Hoe het werkt",
                     "Como funciona", "怎么用"),
    "A camera, not a control panel.": (
        "Eine Kamera, kein Schaltpult.", "Una cámara, no un panel de control.",
        "Una cámara, no un panel de control.", "Un appareil photo, pas un tableau de bord.",
        "Una fotocamera, non un pannello di controllo.", "カメラであって、操作パネルではない。",
        "카메라이지 제어판이 아닙니다.", "Een camera, geen bedieningspaneel.",
        "Uma câmera, não um painel de controle.", "是相机，不是控制面板。"),
    "Press the shutter.": ("Drück den Auslöser.", "Pulsa el disparador.", "Presiona el disparador.",
                           "Appuyez sur le déclencheur.", "Premi lo scatto.", "シャッターを押す。",
                           "셔터를 누릅니다.", "Druk af.", "Aperte o disparador.", "按下快门。"),
    "A RAW negative is written immediately. The shutter never waits on processing, so the app "
    "stays as fast as the stock camera.": (
        "Ein RAW-Negativ wird sofort geschrieben. Der Auslöser wartet nie auf die Verarbeitung, "
        "die App bleibt also so schnell wie die eingebaute Kamera.",
        "Se escribe un negativo RAW al instante. El disparador nunca espera al procesado, así que "
        "la app sigue siendo tan rápida como la cámara de serie.",
        "Se escribe un negativo RAW al instante. El disparador nunca espera al procesamiento, así "
        "que la app sigue siendo tan rápida como la cámara de fábrica.",
        "Un négatif RAW est écrit immédiatement. Le déclencheur n'attend jamais le traitement, "
        "l'app reste donc aussi rapide que l'appareil photo d'origine.",
        "Un negativo RAW viene scritto subito. Lo scatto non aspetta mai l'elaborazione, quindi "
        "l'app resta veloce come la fotocamera di sistema.",
        "RAW ネガがその場で書き込まれます。シャッターが処理を待つことはないので、"
        "標準カメラと同じ速さのまま使えます。",
        "RAW 네거티브가 즉시 기록됩니다. 셔터가 처리를 기다리는 일이 없어서, 앱은 기본 카메라만큼 "
        "빠릅니다.",
        "Er wordt meteen een RAW-negatief weggeschreven. De sluiter wacht nooit op verwerking, dus "
        "de app blijft net zo snel als de standaardcamera.",
        "Um negativo RAW é gravado na hora. O disparador nunca espera pelo processamento, então o "
        "app continua tão rápido quanto a câmera de fábrica.",
        "一张 RAW 底片立刻写入。快门永远不会等处理，所以这个应用和系统相机一样快。"),
    "It goes on the roll.": ("Es kommt auf den Film.", "Va al carrete.", "Va al rollo.",
                             "Elle passe sur la pellicule.", "Va sul rullino.",
                             "フィルムの上に並ぶ。", "롤에 올라갑니다.",
                             "Het gaat op het rolletje.", "Vai para o rolo.", "它进入胶卷。"),
    "Frames queue up exactly like exposures on a roll of film. Keep shooting. You can also set "
    "developing to hold until you are plugged in.": (
        "Bilder reihen sich genau wie Aufnahmen auf einem Film. Fotografiere weiter. Du kannst das "
        "Entwickeln auch warten lassen, bis du am Strom hängst.",
        "Los fotogramas hacen cola exactamente como las exposiciones en un carrete. Sigue "
        "disparando. También puedes hacer que el revelado espere a que estés enchufado.",
        "Los cuadros hacen fila exactamente como las exposiciones en un rollo. Sigue disparando. "
        "También puedes hacer que el revelado espere a que estés conectado a la corriente.",
        "Les images font la queue exactement comme des poses sur une pellicule. Continuez à "
        "photographier. Vous pouvez aussi faire attendre le développement jusqu'au branchement.",
        "I fotogrammi si mettono in coda esattamente come le pose su un rullino. Continua a "
        "scattare. Puoi anche far aspettare lo sviluppo finché non sei sotto carica.",
        "一枚ずつが、フィルムのコマとまったく同じように並んで待ちます。そのまま撮り続けてください。"
        "電源につないでいるときだけ現像するように設定することもできます。",
        "프레임이 필름의 컷처럼 그대로 줄을 서서 기다립니다. 계속 찍으세요. 충전 중일 때만 "
        "현상하도록 설정할 수도 있습니다.",
        "Beelden staan in de rij precies zoals opnamen op een rolletje. Blijf fotograferen. Je "
        "kunt het ontwikkelen ook laten wachten tot je aan de lader ligt.",
        "Os quadros entram na fila exatamente como poses num rolo de filme. Continue fotografando. "
        "Você também pode fazer a revelação esperar até estar na tomada.",
        "画面会像胶卷上的一格格底片那样排队等待。继续拍就好。你也可以设置成接上电源后再显影。"),
    "It develops.": ("Es wird entwickelt.", "Se revela.", "Se revela.", "Elle se développe.",
                     "Si sviluppa.", "現像される。", "현상됩니다.", "Het ontwikkelt.",
                     "Ele revela.", "开始显影。"),
    "About a minute a frame, on your phone, running the full model from negative to print. You "
    "watch the timer, not a progress bar pretending to be one.": (
        "Etwa eine Minute pro Bild, auf deinem Telefon, mit dem vollen Modell vom Negativ bis zum "
        "Abzug. Du siehst eine echte Uhr, keinen Fortschrittsbalken, der so tut als ob.",
        "Alrededor de un minuto por fotograma, en tu móvil, ejecutando el modelo completo del "
        "negativo a la copia. Miras un cronómetro, no una barra de progreso que finge serlo.",
        "Alrededor de un minuto por cuadro, en tu celular, ejecutando el modelo completo del "
        "negativo a la copia. Miras un cronómetro, no una barra de progreso que finge serlo.",
        "Environ une minute par image, sur votre téléphone, avec le modèle complet du négatif au "
        "tirage. Vous regardez un chronomètre, pas une barre de progression qui fait semblant.",
        "Circa un minuto per fotogramma, sul tuo telefono, con il modello completo dal negativo "
        "alla stampa. Guardi un cronometro, non una barra di avanzamento che finge di esserlo.",
        "一枚におよそ一分。あなたの端末の上で、ネガからプリントまでモデルを丸ごと走らせます。"
        "表示されるのは本物の時計で、それらしく見せかけた進捗バーではありません。",
        "한 장에 약 1분, 당신의 휴대폰 위에서, 네거티브부터 인화까지 모델을 통째로 돌립니다. "
        "보이는 것은 실제 타이머이지, 그런 척하는 진행 막대가 아닙니다.",
        "Ongeveer een minuut per beeld, op je telefoon, met het volledige model van negatief tot "
        "afdruk. Je kijkt naar een echte teller, niet naar een voortgangsbalk die er een nadoet.",
        "Cerca de um minuto por quadro, no seu telefone, rodando o modelo completo do negativo à "
        "cópia. Você olha um cronômetro, não uma barra de progresso fingindo ser um.",
        "每张大约一分钟，就在你的手机上，把从底片到成片的完整模型跑完。你看到的是真正的计时，"
        "而不是一根假装在走的进度条。"),
    "You get it back.": ("Du bekommst es zurück.", "Lo recuperas.", "Lo recuperas.",
                         "Vous la récupérez.", "Te lo ritrovi.", "受け取る。", "돌려받습니다.",
                         "Je krijgt het terug.", "Você o recebe de volta.", "你把它取回来。"),
    "Finished photographs save to your photo library and stay in the app, so you can look through "
    "them without leaving. Shot something on another camera? Import the RAW and develop that too.": (
        "Fertige Fotos werden in deiner Mediathek gesichert und bleiben in der App, du kannst sie "
        "also durchsehen, ohne sie zu verlassen. Etwas mit einer anderen Kamera aufgenommen? "
        "Importiere das RAW und entwickle es genauso.",
        "Las fotos terminadas se guardan en tu fototeca y se quedan en la app, así que puedes "
        "repasarlas sin salir. ¿Has hecho algo con otra cámara? Importa el RAW y revélalo también.",
        "Las fotos terminadas se guardan en tu fototeca y se quedan en la app, así que puedes "
        "repasarlas sin salir. ¿Tomaste algo con otra cámara? Importa el RAW y revélalo también.",
        "Les photos terminées sont enregistrées dans votre photothèque et restent dans "
        "l'application, vous pouvez donc les parcourir sans en sortir. Vous avez photographié avec "
        "un autre appareil ? Importez le RAW et développez-le aussi.",
        "Le foto finite vengono salvate nella tua libreria e restano nell'app, così puoi "
        "sfogliarle senza uscire. Hai scattato con un'altra fotocamera? Importa il RAW e sviluppa "
        "anche quello.",
        "仕上がった写真は写真ライブラリに保存され、アプリのなかにも残るので、外に出ずに見返せます。"
        "ほかのカメラで撮ったものがありますか。その RAW を読み込めば、同じように現像できます。",
        "완성된 사진은 사진 보관함에 저장되고 앱 안에도 남아서, 앱을 나가지 않고 훑어볼 수 "
        "있습니다. 다른 카메라로 찍은 것이 있나요? 그 RAW를 가져오면 똑같이 현상할 수 있습니다.",
        "Klare foto's worden in je fotobibliotheek bewaard en blijven in de app, dus je kunt ze "
        "doornemen zonder hem te verlaten. Iets met een andere camera geschoten? Importeer de RAW "
        "en ontwikkel die ook.",
        "As fotos prontas são salvas na sua fototeca e continuam no app, então você pode olhar "
        "todas sem sair. Fotografou com outra câmera? Importe o RAW e revele também.",
        "完成的照片会保存到你的照片图库，并留在应用里，不用离开就能翻看。用别的相机拍了东西？"
        "把 RAW 导进来，一样可以显影。"),
    "A developed photograph of a bird on a rock above turquoise water.": (
        "Ein entwickeltes Foto von einem Vogel auf einem Felsen über türkisfarbenem Wasser.",
        "Una fotografía revelada de un pájaro sobre una roca por encima de agua turquesa.",
        "Una fotografía revelada de un pájaro sobre una roca por encima de agua turquesa.",
        "Une photographie développée d'un oiseau sur un rocher au-dessus d'une eau turquoise.",
        "Una fotografia sviluppata di un uccello su uno scoglio sopra acqua turchese.",
        "ターコイズ色の水の上、岩にとまる鳥を現像した写真。",
        "청록빛 물 위 바위에 앉은 새를 현상한 사진.",
        "Een ontwikkelde foto van een vogel op een rots boven turkooizen water.",
        "Uma fotografia revelada de um pássaro numa rocha acima de água turquesa.",
        "一张显影完成的照片：绿松石色水面上方，一只鸟停在岩石上。"),
    "A filter and film comparison of backlit leaves, magnified.": (
        "Ein Vergleich von Filter und Film an hinterleuchteten Blättern, vergrößert.",
        "Una comparación entre filtro y película de hojas a contraluz, ampliada.",
        "Una comparación entre filtro y película de hojas a contraluz, ampliada.",
        "Une comparaison filtre et pellicule de feuilles à contre-jour, agrandie.",
        "Un confronto fra filtro e pellicola di foglie in controluce, ingrandito.",
        "逆光の葉における、フィルターとフィルムの比較を拡大したもの。",
        "역광의 잎에서 필터와 필름을 비교한 것, 확대.",
        "Een vergelijking van filter en film bij tegenlicht door bladeren, vergroot.",
        "Uma comparação entre filtro e filme de folhas em contraluz, ampliada.",
        "逆光树叶上滤镜与胶片的对比，放大显示。"),
    "One scene developed through all four film stocks.": (
        "Eine Szene, durch alle vier Filme entwickelt.",
        "Una escena revelada con las cuatro películas.",
        "Una escena revelada con las cuatro películas.",
        "Une scène développée avec les quatre pellicules.",
        "Una scena sviluppata con tutte e quattro le pellicole.",
        "ひとつの場面を四種すべてのフィルムで現像したもの。",
        "한 장면을 네 가지 필름 모두로 현상한 것.",
        "Eén scène ontwikkeld met alle vier de films.",
        "Uma cena revelada com os quatro filmes.",
        "同一个场景，用四款胶片分别显影。"),
    "The capture screen: viewfinder, exposure and zoom wheels, shutter.": (
        "Der Aufnahmebildschirm: Sucher, Räder für Belichtung und Zoom, Auslöser.",
        "La pantalla de captura: visor, ruedas de exposición y zoom, disparador.",
        "La pantalla de captura: visor, ruedas de exposición y zoom, disparador.",
        "L'écran de prise de vue : viseur, molettes d'exposition et de zoom, déclencheur.",
        "La schermata di scatto: mirino, ghiere di esposizione e zoom, pulsante di scatto.",
        "撮影画面。ファインダー、露出とズームのダイヤル、シャッター。",
        "촬영 화면. 뷰파인더, 노출과 줌 다이얼, 셔터.",
        "Het opnamescherm: zoeker, wielen voor belichting en zoom, sluiter.",
        "A tela de captura: visor, discos de exposição e zoom, disparador.",
        "拍摄界面：取景器、曝光与变焦拨盘、快门。"),
    "The roll: frames waiting to develop above a grid of finished photographs.": (
        "Der Film: Bilder, die auf die Entwicklung warten, über einem Raster fertiger Fotos.",
        "El carrete: fotogramas esperando revelado sobre una cuadrícula de fotos terminadas.",
        "El rollo: cuadros esperando revelado sobre una cuadrícula de fotos terminadas.",
        "La pellicule : des images en attente de développement au-dessus d'une grille de photos "
        "terminées.",
        "Il rullino: fotogrammi in attesa di sviluppo sopra una griglia di foto finite.",
        "フィルムロール。現像を待つ一枚たちと、その下に仕上がった写真のグリッド。",
        "필름 롤. 현상을 기다리는 프레임들과 그 아래 완성된 사진 그리드.",
        "Het rolletje: beelden die op ontwikkeling wachten boven een raster met klare foto's.",
        "O rolo: quadros esperando revelação acima de uma grade de fotos prontas.",
        "胶卷：等待显影的画面，下面是已完成照片的网格。"),
    "Honestly": ("Ehrlich gesagt", "Con franqueza", "Con franqueza", "Honnêtement",
                 "Sinceramente", "正直なところ", "솔직히", "Eerlijk gezegd", "Sinceramente",
                 "说实话"),
    "It is slow, and that is the trade.": (
        "Es ist langsam, und das ist der Handel.", "Es lento, y ese es el trato.",
        "Es lento, y ese es el trato.", "C'est lent, et c'est le marché.",
        "È lento, e questo è il compromesso.", "遅い。それが引き換えです。",
        "느립니다. 그것이 맞바꾼 것입니다.", "Het is traag, en dat is de ruil.",
        "É lento, e essa é a troca.", "它很慢，这就是代价。"),
    "A minute of your phone's graphics processor per photograph is an absurd amount of computation\n"
    "      to spend on one image, and it is the reason nobody else does this. A filter is one "
    "lookup per\n      pixel and it is done before you lift your thumb. We think the minute buys "
    "something a lookup\n      never will.": (
        "Eine Minute Grafikprozessor deines Telefons pro Foto ist ein absurder Rechenaufwand für "
        "ein einziges Bild, und genau darum macht das sonst niemand. Ein Filter ist eine "
        "Nachschlagung pro Pixel und fertig, bevor du den Daumen hebst. Wir glauben, diese Minute "
        "kauft etwas, das eine Nachschlagung nie kaufen wird.",
        "Un minuto del procesador gráfico de tu móvil por fotografía es una cantidad de cálculo "
        "absurda para una sola imagen, y es la razón por la que nadie más hace esto. Un filtro es "
        "una consulta por píxel y está hecho antes de que levantes el pulgar. Creemos que ese "
        "minuto compra algo que una consulta nunca comprará.",
        "Un minuto del procesador gráfico de tu celular por fotografía es una cantidad de cálculo "
        "absurda para una sola imagen, y es la razón por la que nadie más hace esto. Un filtro es "
        "una consulta por píxel y está hecho antes de que levantes el pulgar. Creemos que ese "
        "minuto compra algo que una consulta nunca comprará.",
        "Une minute du processeur graphique de votre téléphone par photographie, c'est une "
        "quantité de calcul absurde pour une seule image, et c'est la raison pour laquelle "
        "personne d'autre ne le fait. Un filtre, c'est une consultation par pixel, et c'est fini "
        "avant que vous ne leviez le pouce. Nous pensons que cette minute achète quelque chose "
        "qu'une consultation n'achètera jamais.",
        "Un minuto del processore grafico del tuo telefono per fotografia è una quantità di "
        "calcolo assurda da spendere su una sola immagine, ed è il motivo per cui nessun altro lo "
        "fa. Un filtro è una consultazione per pixel ed è finito prima che tu alzi il pollice. "
        "Pensiamo che quel minuto compri qualcosa che una consultazione non comprerà mai.",
        "写真一枚につき端末のグラフィックスプロセッサを一分使うというのは、一枚の画像に費やす"
        "計算量としてはばかげています。ほかの誰もやらないのはそのためです。フィルターなら一画素"
        "あたり一回の参照で、あなたが親指を離す前に終わっています。それでもこの一分は、"
        "参照では決して買えないものを買っていると考えています。",
        "사진 한 장에 휴대폰 그래픽 프로세서를 1분 쓰는 것은, 이미지 한 장에 들이는 연산량으로는 "
        "터무니없습니다. 아무도 이렇게 하지 않는 이유가 그것입니다. 필터라면 픽셀당 조회 한 "
        "번이고, 당신이 엄지를 떼기도 전에 끝납니다. 그래도 이 1분은 조회로는 결코 살 수 없는 "
        "것을 산다고 생각합니다.",
        "Een minuut van de grafische processor van je telefoon per foto is een absurde hoeveelheid "
        "rekenwerk voor één beeld, en het is de reden dat niemand anders dit doet. Een filter is "
        "één opzoeking per pixel en is klaar voor je je duim optilt. Wij denken dat die minuut "
        "iets koopt wat een opzoeking nooit zal kopen.",
        "Um minuto do processador gráfico do seu telefone por fotografia é uma quantidade absurda "
        "de cálculo para uma única imagem, e é a razão de mais ninguém fazer isso. Um filtro é uma "
        "consulta por pixel e termina antes de você levantar o polegar. Achamos que esse minuto "
        "compra algo que uma consulta nunca vai comprar.",
        "每张照片占用你手机图形处理器一分钟，对一张图像来说是荒谬的计算量，"
        "这也正是别人都不这么做的原因。滤镜只是每个像素查一次表，在你抬起拇指之前就结束了。"
        "我们认为这一分钟买到的，是查表永远买不到的东西。"),
    "The viewfinder shows you the scene, not the film. Grading a live preview means guessing at "
    "the\n      answer before the work is done, and a preview that guesses wrong is worse than one "
    "that is\n      honest. Use the exposure dial to place your highlights.": (
        "Der Sucher zeigt dir die Szene, nicht den Film. Eine Live-Vorschau zu graden heißt, die "
        "Antwort zu raten, bevor die Arbeit getan ist, und eine Vorschau, die falsch rät, ist "
        "schlimmer als eine ehrliche. Setze deine Lichter mit dem Belichtungsrad.",
        "El visor te muestra la escena, no la película. Etalonar una vista previa en directo "
        "significa adivinar la respuesta antes de que el trabajo esté hecho, y una vista previa "
        "que adivina mal es peor que una honesta. Usa la rueda de exposición para colocar tus "
        "altas luces.",
        "El visor te muestra la escena, no la película. Etalonar una vista previa en vivo "
        "significa adivinar la respuesta antes de que el trabajo esté hecho, y una vista previa "
        "que adivina mal es peor que una honesta. Usa la rueda de exposición para colocar tus "
        "altas luces.",
        "Le viseur vous montre la scène, pas la pellicule. Étalonner un aperçu en direct revient à "
        "deviner la réponse avant que le travail soit fait, et un aperçu qui devine mal est pire "
        "qu'un aperçu honnête. Servez-vous de la molette d'exposition pour placer vos hautes "
        "lumières.",
        "Il mirino ti mostra la scena, non la pellicola. Correggere un'anteprima dal vivo vuol "
        "dire tirare a indovinare la risposta prima che il lavoro sia fatto, e un'anteprima che "
        "indovina male è peggio di una onesta. Usa la ghiera dell'esposizione per sistemare le "
        "alte luci.",
        "ファインダーに映るのは被写体であって、フィルムではありません。ライブプレビューに色を"
        "当てることは、作業が終わる前に答えを推測することであり、外れる推測をするプレビューは、"
        "正直なプレビューより質が悪い。露出ダイヤルでハイライトを置いてください。",
        "뷰파인더는 장면을 보여 주지 필름을 보여 주지 않습니다. 라이브 미리보기에 색을 입히는 "
        "것은 작업이 끝나기 전에 답을 추측하는 일이고, 틀리게 추측하는 미리보기는 정직한 것보다 "
        "나쁩니다. 노출 다이얼로 하이라이트를 잡으세요.",
        "De zoeker toont je het tafereel, niet de film. Een live voorbeeld graden betekent het "
        "antwoord raden voordat het werk gedaan is, en een voorbeeld dat verkeerd raadt is erger "
        "dan een eerlijk voorbeeld. Gebruik het belichtingswiel om je hoge lichten te plaatsen.",
        "O visor mostra a cena, não o filme. Corrigir uma prévia ao vivo significa chutar a "
        "resposta antes de o trabalho estar feito, e uma prévia que chuta errado é pior do que uma "
        "honesta. Use o disco de exposição para posicionar suas altas luzes.",
        "取景器给你看的是场景，不是胶片。给实时预览调色，等于在工作完成之前就去猜结果，"
        "而猜错的预览比诚实的预览更糟。请用曝光拨盘来安排你的高光。"),
    "This is slide film. There is not much room above the highlights. That is faithful rather "
    "than\n      accidental, and it is the part that will change how you shoot.": (
        "Das hier ist Diafilm. Über den Lichtern ist nicht viel Luft. Das ist originalgetreu und "
        "nicht zufällig, und es ist der Teil, der ändern wird, wie du fotografierst.",
        "Esto es película de diapositiva. No hay mucho margen por encima de las altas luces. Eso "
        "es fidelidad y no un accidente, y es la parte que cambiará cómo disparas.",
        "Esto es película de diapositiva. No hay mucho margen por encima de las altas luces. Eso "
        "es fidelidad y no un accidente, y es la parte que cambiará cómo disparas.",
        "C'est un film inversible. Il n'y a pas beaucoup de marge au-dessus des hautes lumières. "
        "C'est fidèle et non accidentel, et c'est la part qui changera votre façon de "
        "photographier.",
        "Questa è pellicola diapositiva. Sopra le alte luci non c'è molto margine. È fedeltà e non "
        "un caso, ed è la parte che cambierà il tuo modo di scattare.",
        "これはリバーサルフィルムです。ハイライトの上に残された余裕は多くありません。"
        "それは偶然ではなく忠実さであり、あなたの撮り方を変えることになる部分です。",
        "이것은 슬라이드 필름입니다. 하이라이트 위로 남은 여유가 많지 않습니다. 그것은 우연이 "
        "아니라 충실함이고, 당신이 찍는 방식을 바꾸게 될 부분입니다.",
        "Dit is omkeerfilm. Boven de hoge lichten zit niet veel ruimte. Dat is getrouw en niet per "
        "ongeluk, en het is het deel dat verandert hoe je fotografeert.",
        "Este é filme slide. Não há muita margem acima das altas luzes. Isso é fidelidade e não "
        "acidente, e é a parte que vai mudar o jeito como você fotografa.",
        "这是反转片。高光之上留的余地并不多。这是忠实，而不是意外，"
        "而且正是这一点会改变你拍摄的方式。"),
    "One price, once": ("Ein Preis, einmal", "Un precio, una vez", "Un precio, una vez",
                        "Un prix, une fois", "Un prezzo, una volta", "価格はひとつ、一度きり",
                        "가격은 하나, 한 번", "Eén prijs, één keer", "Um preço, uma vez",
                        "一个价格，只付一次"),
    "$14.99. That is the whole business model.": (
        "14,99 $. Das ist das ganze Geschäftsmodell.",
        "14,99 $. Ese es todo el modelo de negocio.",
        "14,99 $. Ese es todo el modelo de negocio.",
        "14,99 $. C'est tout le modèle économique.",
        "14,99 $. È tutto qui il modello di business.",
        "14.99 ドル。ビジネスモデルはこれだけです。",
        "14.99달러. 비즈니스 모델은 이게 전부입니다.",
        "$14,99. Dat is het hele verdienmodel.",
        "US$ 14,99. Esse é todo o modelo de negócio.",
        "14.99 美元。整个商业模式就这一句。"),
    "No subscription, no account, no cloud, no ads, no watermark, no in app purchases, no upsell "
    "to\n      unlock the good stocks. Your photographs never leave your phone, because the app has "
    "no\n      networking code in it at all.": (
        "Kein Abo, kein Konto, keine Cloud, keine Werbung, kein Wasserzeichen, keine "
        "In-App-Käufe, kein Aufpreis, um die guten Filme freizuschalten. Deine Fotos verlassen "
        "dein Telefon nie, weil in der App überhaupt kein Netzwerkcode steckt.",
        "Sin suscripción, sin cuenta, sin nube, sin anuncios, sin marca de agua, sin compras "
        "dentro de la app, sin pagar más para desbloquear las películas buenas. Tus fotografías "
        "nunca salen de tu móvil, porque la app no lleva nada de código de red.",
        "Sin suscripción, sin cuenta, sin nube, sin anuncios, sin marca de agua, sin compras "
        "dentro de la app, sin pagar más para desbloquear las películas buenas. Tus fotografías "
        "nunca salen de tu celular, porque la app no lleva nada de código de red.",
        "Sans abonnement, sans compte, sans cloud, sans publicité, sans filigrane, sans achat "
        "intégré, sans supplément pour débloquer les bonnes pellicules. Vos photographies ne "
        "quittent jamais votre téléphone, parce que l'app ne contient aucun code réseau.",
        "Nessun abbonamento, nessun account, nessun cloud, nessuna pubblicità, nessuna filigrana, "
        "nessun acquisto in-app, nessun sovrapprezzo per sbloccare le pellicole buone. Le tue "
        "fotografie non lasciano mai il telefono, perché nell'app non c'è proprio codice di rete.",
        "定額課金なし、アカウントなし、クラウドなし、広告なし、透かしなし、アプリ内課金なし、"
        "「良いフィルム」を解放するための追加料金もなし。あなたの写真が端末の外に出ることは"
        "ありません。アプリには通信のコードそのものが入っていないからです。",
        "구독 없음, 계정 없음, 클라우드 없음, 광고 없음, 워터마크 없음, 인앱 결제 없음, 좋은 "
        "필름을 풀기 위한 추가 결제도 없음. 당신의 사진은 절대 휴대폰을 떠나지 않습니다. 앱에 "
        "네트워크 코드 자체가 들어 있지 않기 때문입니다.",
        "Geen abonnement, geen account, geen cloud, geen advertenties, geen watermerk, geen "
        "in-app-aankopen, geen bijbetaling om de goede films vrij te spelen. Je foto's verlaten je "
        "telefoon nooit, want er zit helemaal geen netwerkcode in de app.",
        "Sem assinatura, sem conta, sem nuvem, sem anúncios, sem marca d'água, sem compras dentro "
        "do app, sem pagar mais para liberar os filmes bons. Suas fotografias nunca saem do seu "
        "telefone, porque o app não tem nenhum código de rede.",
        "无订阅、无账号、无云端、无广告、无水印、无应用内购买，也不会让你再花钱去解锁\"好胶片\"。"
        "你的照片永远不会离开你的手机，因为这个应用里根本没有联网代码。"),
    "Requires an iPhone that can capture Apple ProRAW.": (
        "Erfordert ein iPhone, das Apple ProRAW aufnehmen kann.",
        "Requiere un iPhone capaz de capturar Apple ProRAW.",
        "Requiere un iPhone capaz de capturar Apple ProRAW.",
        "Nécessite un iPhone capable de photographier en Apple ProRAW.",
        "Richiede un iPhone in grado di scattare in Apple ProRAW.",
        "Apple ProRAW で撮影できる iPhone が必要です。",
        "Apple ProRAW로 촬영할 수 있는 iPhone이 필요합니다.",
        "Vereist een iPhone die Apple ProRAW kan vastleggen.",
        "Requer um iPhone capaz de capturar Apple ProRAW.",
        "需要一台能够拍摄 Apple ProRAW 的 iPhone。"),
    "Questions": ("Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問",
                  "질문", "Vragen", "Perguntas", "常见问题"),
    "The things people ask first.": (
        "Was zuerst gefragt wird.", "Lo que la gente pregunta primero.",
        "Lo que la gente pregunta primero.", "Ce que les gens demandent en premier.",
        "Le cose che chiedono per prime.", "最初に聞かれること。",
        "사람들이 가장 먼저 묻는 것들.", "Wat mensen als eerste vragen.",
        "O que as pessoas perguntam primeiro.", "大家最先问的问题。"),
    "Levi Foster": ("Levi Foster",) * 10,
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "Support": ("Support", "Soporte", "Soporte", "Assistance", "Assistenza", "サポート", "지원",
                "Ondersteuning", "Suporte", "支持"),
    "FRMT is built by Levi Foster in Fort Worth, Texas": (
        "FRMT wird von Levi Foster in Fort Worth, Texas gebaut",
        "FRMT lo hace Levi Foster en Fort Worth, Texas",
        "FRMT lo hace Levi Foster en Fort Worth, Texas",
        "FRMT est fait par Levi Foster à Fort Worth, Texas",
        "FRMT è fatto da Levi Foster a Fort Worth, Texas",
        "FRMT はテキサス州フォートワースの Levi Foster がつくっています",
        "FRMT는 텍사스주 포트워스의 Levi Foster가 만듭니다",
        "FRMT wordt gemaakt door Levi Foster in Fort Worth, Texas",
        "O FRMT é feito por Levi Foster em Fort Worth, Texas",
        "FRMT 由 Levi Foster 在美国得州沃斯堡打造"),
})

# ---------------------------------------------------------------- FAQ and structured data
T.update({
    "How is FRMT different from a film filter or a LUT?": (
        "Wie unterscheidet sich FRMT von einem Filmfilter oder einer LUT?",
        "¿En qué se diferencia FRMT de un filtro de película o una LUT?",
        "¿En qué se diferencia FRMT de un filtro de película o una LUT?",
        "En quoi FRMT diffère-t-il d'un filtre argentique ou d'une LUT ?",
        "In cosa differisce FRMT da un filtro pellicola o da una LUT?",
        "FRMT はフィルム風フィルターや LUT と何が違うのですか。",
        "FRMT는 필름 필터나 LUT와 무엇이 다른가요?",
        "Waarin verschilt FRMT van een filmfilter of een LUT?",
        "Como o FRMT é diferente de um filtro de filme ou de uma LUT?",
        "FRMT 和胶片滤镜或 LUT 有什么不同？"),
    "A filter is a lookup table. Somebody decided in advance what every colour becomes, and the\n"
    "        same input always gives the same output. FRMT simulates the process instead, so what "
    "happens\n        to a pixel depends on what surrounds it: light spreads sideways into "
    "neighbouring areas, dye\n        layers hold each other back, and grain forms according to how "
    "much light actually landed.": (
        "Ein Filter ist eine Nachschlagetabelle. Jemand hat vorab entschieden, was aus jeder Farbe "
        "wird, und dieselbe Eingabe liefert immer dieselbe Ausgabe. FRMT simuliert stattdessen den "
        "Prozess, also hängt das, was mit einem Pixel geschieht, davon ab, was es umgibt: Licht "
        "breitet sich seitwärts in benachbarte Bereiche aus, Farbschichten halten einander zurück, "
        "und Korn entsteht danach, wie viel Licht tatsächlich gelandet ist.",
        "Un filtro es una tabla de consulta. Alguien decidió de antemano en qué se convierte cada "
        "color, y la misma entrada da siempre la misma salida. FRMT simula el proceso en su lugar, "
        "así que lo que le pasa a un píxel depende de lo que lo rodea: la luz se extiende de lado "
        "hacia las zonas vecinas, las capas de colorante se frenan entre sí y el grano se forma "
        "según cuánta luz llegó de verdad.",
        "Un filtro es una tabla de consulta. Alguien decidió de antemano en qué se convierte cada "
        "color, y la misma entrada da siempre la misma salida. FRMT simula el proceso en su lugar, "
        "así que lo que le pasa a un píxel depende de lo que lo rodea: la luz se extiende de lado "
        "hacia las zonas vecinas, las capas de colorante se frenan entre sí y el grano se forma "
        "según cuánta luz llegó de verdad.",
        "Un filtre est une table de conversion. Quelqu'un a décidé à l'avance ce que devient "
        "chaque couleur, et la même entrée donne toujours la même sortie. FRMT simule le procédé à "
        "la place, si bien que ce qui arrive à un pixel dépend de ce qui l'entoure : la lumière "
        "s'étend latéralement vers les zones voisines, les couches de colorant se retiennent, et "
        "le grain se forme selon la quantité de lumière réellement tombée.",
        "Un filtro è una tabella di consultazione. Qualcuno ha deciso in anticipo cosa diventa "
        "ogni colore, e lo stesso ingresso dà sempre la stessa uscita. FRMT simula invece il "
        "processo, quindi quello che succede a un pixel dipende da ciò che lo circonda: la luce si "
        "allarga di lato verso le zone vicine, gli strati di colorante si trattengono a vicenda, e "
        "la grana si forma in base a quanta luce è davvero arrivata.",
        "フィルターはルックアップテーブルです。どの色が何になるかを誰かが前もって決めていて、"
        "同じ入力からは必ず同じ出力が出ます。FRMT はその代わりに工程そのものを再現するので、"
        "ある画素に何が起きるかは、そのまわりに何があるかで決まります。光は隣接する領域へ横に"
        "広がり、色素層は互いを抑え合い、粒子は実際に落ちた光の量に応じて生まれます。",
        "필터는 룩업 테이블입니다. 어떤 색이 무엇이 될지 누군가 미리 정해 두었고, 같은 입력은 "
        "언제나 같은 출력을 냅니다. FRMT는 대신 공정 자체를 시뮬레이션하므로, 한 픽셀에 무슨 일이 "
        "일어날지는 그 주변에 무엇이 있는지에 달려 있습니다. 빛은 이웃한 영역으로 옆으로 퍼지고, "
        "염료층은 서로를 붙잡고, 입자는 실제로 닿은 빛의 양에 따라 생깁니다.",
        "Een filter is een opzoektabel. Iemand heeft vooraf besloten wat elke kleur wordt, en "
        "dezelfde invoer geeft altijd dezelfde uitvoer. FRMT simuleert in plaats daarvan het "
        "proces, dus wat er met een pixel gebeurt hangt af van wat eromheen zit: licht spreidt "
        "zijwaarts naar naburige gebieden, kleurlagen houden elkaar tegen, en korrel ontstaat naar "
        "gelang hoeveel licht er werkelijk is geland.",
        "Um filtro é uma tabela de consulta. Alguém decidiu de antemão no que cada cor vira, e a "
        "mesma entrada dá sempre a mesma saída. O FRMT simula o processo em vez disso, então o que "
        "acontece com um pixel depende do que está em volta dele: a luz se espalha de lado para as "
        "áreas vizinhas, as camadas de corante seguram umas às outras, e o grão se forma conforme "
        "quanta luz de fato caiu.",
        "滤镜是一张查找表。有人事先决定了每种颜色会变成什么，同样的输入永远给出同样的输出。"
        "FRMT 做的是模拟这道工序，因此一个像素会发生什么，取决于它周围有什么："
        "光会向侧面扩散到相邻区域，染料层彼此拖住，颗粒则按照实际落下的光量生成。"),
    "Which film stocks are included?": (
        "Welche Filme sind enthalten?", "¿Qué películas incluye?", "¿Qué películas incluye?",
        "Quelles pellicules sont incluses ?", "Quali pellicole sono incluse?",
        "どのフィルムが入っていますか。", "어떤 필름이 들어 있나요?",
        "Welke films zitten erin?", "Quais filmes estão incluídos?", "包含哪几款胶片？"),
    "Four, each built from its manufacturer's published characteristic curves and spectral\n"
    "        sensitivity data rather than eyeballed from somebody's scans.": (
        "Vier, jeder gebaut aus den veröffentlichten Kennlinien und spektralen Empfindlichkeiten "
        "seines Herstellers statt nach Augenmaß aus irgendwelchen Scans.",
        "Cuatro, cada una construida a partir de las curvas características y los datos de "
        "sensibilidad espectral publicados por su fabricante, no calculada a ojo desde los "
        "escaneos de alguien.",
        "Cuatro, cada una construida a partir de las curvas características y los datos de "
        "sensibilidad espectral publicados por su fabricante, no calculada a ojo desde los "
        "escaneos de alguien.",
        "Quatre, chacune construite à partir des courbes caractéristiques et des données de "
        "sensibilité spectrale publiées par son fabricant, et non estimée à l'oeil depuis les "
        "scans de quelqu'un.",
        "Quattro, ognuna costruita dalle curve caratteristiche e dai dati di sensibilità spettrale "
        "pubblicati dal suo produttore, non ricavata a occhio dalle scansioni di qualcuno.",
        "四種です。いずれも、そのメーカーが公開した特性曲線と分光感度のデータから組み上げて"
        "います。誰かのスキャンを見ながら目分量で合わせたものではありません。",
        "네 가지입니다. 각각 그 제조사가 공개한 특성곡선과 분광 감도 데이터로 만들었고, 누군가의 "
        "스캔을 보며 눈대중으로 맞춘 것이 아닙니다.",
        "Vier, elk gebouwd op de gepubliceerde karakteristieke krommen en spectrale "
        "gevoeligheidsdata van de fabrikant, en niet op het oog afgekeken van iemands scans.",
        "Quatro, cada um construído a partir das curvas características e dos dados de "
        "sensibilidade espectral publicados pelo fabricante, e não estimado no olho a partir dos "
        "scans de alguém.",
        "四款。每一款都建立在其厂商公开的特性曲线和光谱感光度数据之上，而不是照着谁的扫描件"
        "凭眼睛凑出来的。"),
    "Is it a subscription?": (
        "Ist das ein Abo?", "¿Es una suscripción?", "¿Es una suscripción?",
        "Est-ce un abonnement ?", "È un abbonamento?", "定額課金ですか。", "구독인가요?",
        "Is het een abonnement?", "É uma assinatura?", "这是订阅制吗？"),
    "No. One purchase of $14.99. No subscription, no account, no advertising, no in app purchases.": (
        "Nein. Ein Kauf für 14,99 $. Kein Abo, kein Konto, keine Werbung, keine In-App-Käufe.",
        "No. Una compra de 14,99 $. Sin suscripción, sin cuenta, sin publicidad, sin compras "
        "dentro de la app.",
        "No. Una compra de 14,99 $. Sin suscripción, sin cuenta, sin publicidad, sin compras "
        "dentro de la app.",
        "Non. Un achat de 14,99 $. Sans abonnement, sans compte, sans publicité, sans achat "
        "intégré.",
        "No. Un acquisto da 14,99 $. Nessun abbonamento, nessun account, nessuna pubblicità, "
        "nessun acquisto in-app.",
        "いいえ。14.99 ドルの買い切りです。定額課金も、アカウントも、広告も、アプリ内課金も"
        "ありません。",
        "아니요. 14.99달러 한 번의 구매입니다. 구독도, 계정도, 광고도, 인앱 결제도 없습니다.",
        "Nee. Eén aankoop van $14,99. Geen abonnement, geen account, geen advertenties, geen "
        "in-app-aankopen.",
        "Não. Uma compra de US$ 14,99. Sem assinatura, sem conta, sem publicidade, sem compras "
        "dentro do app.",
        "不是。一次性购买 14.99 美元。没有订阅、没有账号、没有广告、没有应用内购买。"),
    "Do my photos leave my iPhone?": (
        "Verlassen meine Fotos mein iPhone?", "¿Mis fotos salen de mi iPhone?",
        "¿Mis fotos salen de mi iPhone?", "Mes photos quittent-elles mon iPhone ?",
        "Le mie foto escono dal mio iPhone?", "写真が iPhone の外に出ることはありますか。",
        "제 사진이 iPhone 밖으로 나가나요?", "Verlaten mijn foto's mijn iPhone?",
        "Minhas fotos saem do meu iPhone?", "我的照片会离开 iPhone 吗？"),
    "No. Every frame is developed on the iPhone's own GPU. The app contains no networking code at\n"
    "        all, so there is nothing to upload and no server holding a copy.": (
        "Nein. Jedes Bild wird auf der GPU des iPhone selbst entwickelt. Die App enthält "
        "überhaupt keinen Netzwerkcode, es gibt also nichts hochzuladen und keinen Server, der "
        "eine Kopie hält.",
        "No. Cada fotograma se revela en la propia GPU del iPhone. La app no contiene nada de "
        "código de red, así que no hay nada que subir ni servidor alguno guardando una copia.",
        "No. Cada cuadro se revela en la propia GPU del iPhone. La app no contiene nada de código "
        "de red, así que no hay nada que subir ni servidor alguno guardando una copia.",
        "Non. Chaque image est développée sur le GPU de l'iPhone lui-même. L'app ne contient aucun "
        "code réseau, il n'y a donc rien à envoyer et aucun serveur qui en garde une copie.",
        "No. Ogni fotogramma viene sviluppato sulla GPU dell'iPhone stesso. L'app non contiene "
        "proprio codice di rete, quindi non c'è niente da caricare e nessun server che ne tenga "
        "una copia.",
        "いいえ。どの一枚も iPhone 自身の GPU で現像されます。アプリには通信のコードそのものが"
        "入っていないので、送るものも、控えを持つサーバーもありません。",
        "아니요. 모든 프레임이 iPhone 자체의 GPU에서 현상됩니다. 앱에는 네트워크 코드 자체가 들어 "
        "있지 않아서, 올릴 것도 없고 사본을 가진 서버도 없습니다.",
        "Nee. Elk beeld wordt ontwikkeld op de eigen GPU van de iPhone. De app bevat helemaal geen "
        "netwerkcode, dus er valt niets te uploaden en er is geen server met een kopie.",
        "Não. Cada quadro é revelado na própria GPU do iPhone. O app não contém nenhum código de "
        "rede, então não há nada para enviar e nenhum servidor guardando uma cópia.",
        "不会。每一张都在 iPhone 自己的 GPU 上完成显影。应用里根本没有联网代码，"
        "所以没有东西可上传，也没有服务器留副本。"),
    "Why does developing take so long?": (
        "Warum dauert das Entwickeln so lange?", "¿Por qué tarda tanto el revelado?",
        "¿Por qué tarda tanto el revelado?", "Pourquoi le développement est-il si long ?",
        "Perché lo sviluppo ci mette così tanto?", "現像にどうしてそんなに時間がかかるのですか。",
        "현상이 왜 이렇게 오래 걸리나요?", "Waarom duurt het ontwikkelen zo lang?",
        "Por que a revelação demora tanto?", "为什么显影要这么久？"),
    "Because it runs the chemistry rather than looking up an answer. Light transport through the\n"
    "        emulsion, the interaction between dye layers and grain formation are all computed for "
    "every\n        frame, and that costs real time on a phone.": (
        "Weil es die Chemie durchrechnet, statt eine Antwort nachzuschlagen. Lichttransport durch "
        "die Emulsion, das Zusammenspiel der Farbschichten und die Kornbildung werden für jedes "
        "Bild berechnet, und das kostet auf einem Telefon echte Zeit.",
        "Porque ejecuta la química en vez de consultar una respuesta. El transporte de luz por la "
        "emulsión, la interacción entre capas de colorante y la formación del grano se calculan "
        "para cada fotograma, y eso cuesta tiempo real en un móvil.",
        "Porque ejecuta la química en vez de consultar una respuesta. El transporte de luz por la "
        "emulsión, la interacción entre capas de colorante y la formación del grano se calculan "
        "para cada cuadro, y eso cuesta tiempo real en un celular.",
        "Parce qu'il calcule la chimie au lieu de consulter une réponse. Le transport de la "
        "lumière dans l'émulsion, l'interaction entre les couches de colorant et la formation du "
        "grain sont calculés pour chaque image, et cela coûte du temps réel sur un téléphone.",
        "Perché esegue la chimica invece di consultare una risposta. Il trasporto della luce "
        "nell'emulsione, l'interazione fra strati di colorante e la formazione della grana vengono "
        "calcolati per ogni fotogramma, e su un telefono questo costa tempo vero.",
        "答えを調べるのではなく、化学を計算しているからです。乳剤のなかの光の伝わり方、"
        "色素層どうしの相互作用、粒子の生成が、どの一枚についても計算されます。"
        "端末の上でそれをやれば、実際に時間がかかります。",
        "답을 찾아보는 대신 화학을 계산하기 때문입니다. 유제 안에서의 빛의 이동, 염료층 사이의 "
        "상호작용, 입자의 형성이 모든 프레임마다 계산되고, 휴대폰에서 그것은 실제 시간을 "
        "잡아먹습니다.",
        "Omdat hij de chemie doorrekent in plaats van een antwoord op te zoeken. Lichttransport "
        "door de emulsie, de wisselwerking tussen kleurlagen en korrelvorming worden voor elk "
        "beeld berekend, en dat kost op een telefoon echte tijd.",
        "Porque ele roda a química em vez de consultar uma resposta. O transporte de luz pela "
        "emulsão, a interação entre camadas de corante e a formação do grão são calculados para "
        "cada quadro, e isso custa tempo real num telefone.",
        "因为它是在跑化学，而不是查一个答案。光在乳剂中的传输、染料层之间的相互作用、"
        "颗粒的生成，都要为每一张单独算过，而这在手机上要花掉实实在在的时间。"),
    "Which iPhones does it work on?": (
        "Auf welchen iPhones läuft es?", "¿En qué iPhones funciona?", "¿En qué iPhones funciona?",
        "Sur quels iPhone fonctionne-t-il ?", "Su quali iPhone funziona?",
        "どの iPhone で使えますか。", "어떤 iPhone에서 쓸 수 있나요?",
        "Op welke iPhones werkt het?", "Em quais iPhones funciona?", "支持哪些 iPhone？"),
    "Any iPhone that can capture Apple ProRAW, running iOS 26 or later.": (
        "Jedes iPhone, das Apple ProRAW aufnehmen kann, mit iOS 26 oder neuer.",
        "Cualquier iPhone capaz de capturar Apple ProRAW, con iOS 26 o posterior.",
        "Cualquier iPhone capaz de capturar Apple ProRAW, con iOS 26 o posterior.",
        "Tout iPhone capable de photographier en Apple ProRAW, sous iOS 26 ou version ultérieure.",
        "Qualsiasi iPhone in grado di scattare in Apple ProRAW, con iOS 26 o successivo.",
        "Apple ProRAW で撮影でき、iOS 26 以降が動作している iPhone。",
        "Apple ProRAW로 촬영할 수 있고 iOS 26 이상이 설치된 iPhone.",
        "Elke iPhone die Apple ProRAW kan vastleggen, met iOS 26 of nieuwer.",
        "Qualquer iPhone capaz de capturar Apple ProRAW, com iOS 26 ou posterior.",
        "任何能够拍摄 Apple ProRAW 且运行 iOS 26 或更高版本的 iPhone。"),

    # --- JSON-LD. Same claims, phrased for a machine reading the graph rather than a visitor.
    "A film simulation camera for iPhone that models the photographic process itself rather than "
    "applying a colour filter: halation, interimage coupler effects and density-based grain, "
    "developed from a RAW negative on device.": (
        "Eine Filmsimulationskamera für iPhone, die den fotografischen Prozess selbst nachbildet "
        "statt einen Farbfilter anzuwenden: Lichthofbildung, Interimage-Couplereffekte und "
        "dichteabhängiges Korn, auf dem Gerät aus einem RAW-Negativ entwickelt.",
        "Una cámara de simulación de película para iPhone que modela el proceso fotográfico en sí "
        "en vez de aplicar un filtro de color: halación, efectos de copulantes interimagen y grano "
        "según la densidad, revelado en el dispositivo desde un negativo RAW.",
        "Una cámara de simulación de película para iPhone que modela el proceso fotográfico en sí "
        "en vez de aplicar un filtro de color: halación, efectos de copulantes interimagen y grano "
        "según la densidad, revelado en el dispositivo desde un negativo RAW.",
        "Un appareil photo à simulation argentique pour iPhone qui modélise le procédé "
        "photographique lui-même au lieu d'appliquer un filtre coloré : halo, effets de coupleurs "
        "inter-image et grain lié à la densité, développés sur l'appareil depuis un négatif RAW.",
        "Una fotocamera a simulazione di pellicola per iPhone che modella il processo fotografico "
        "in sé invece di applicare un filtro colore: alone, effetti dei copulanti interimmagine e "
        "grana legata alla densità, sviluppati sul dispositivo da un negativo RAW.",
        "カラーフィルターをかけるのではなく、写真という工程そのものを再現する iPhone 用フィルム"
        "シミュレーションカメラ。ハレーション、インターイメージのカプラー効果、濃度に応じた粒子を、"
        "端末上で RAW ネガから現像します。",
        "컬러 필터를 씌우는 대신 사진이라는 공정 자체를 모델링하는 iPhone용 필름 시뮬레이션 "
        "카메라. 헐레이션, 인터이미지 커플러 효과, 농도에 따른 입자를 기기 안에서 RAW "
        "네거티브로부터 현상합니다.",
        "Een filmsimulatiecamera voor iPhone die het fotografische proces zelf modelleert in "
        "plaats van een kleurfilter toe te passen: lichthof, interimage-couplereffecten en korrel "
        "op basis van dichtheid, op het toestel ontwikkeld vanuit een RAW-negatief.",
        "Uma câmera de simulação de filme para iPhone que modela o próprio processo fotográfico em "
        "vez de aplicar um filtro de cor: halação, efeitos de copulantes interimagem e grão "
        "conforme a densidade, revelados no aparelho a partir de um negativo RAW.",
        "一款 iPhone 胶片模拟相机，模拟的是摄影工序本身，而不是套一层颜色滤镜：光晕、"
        "层间成色剂效应、随密度变化的颗粒，在设备上从 RAW 底片完成显影。"),
    "Halation modelled from the light that scatters through the emulsion": (
        "Lichthofbildung, nachgebildet aus dem Licht, das durch die Emulsion streut",
        "Halación modelada a partir de la luz que se dispersa por la emulsión",
        "Halación modelada a partir de la luz que se dispersa por la emulsión",
        "Halo modélisé à partir de la lumière qui diffuse dans l'émulsion",
        "Alone modellato dalla luce che diffonde nell'emulsione",
        "乳剤のなかを散乱する光から再現したハレーション",
        "유제 안에서 산란하는 빛으로부터 모델링한 헐레이션",
        "Lichthof gemodelleerd op het licht dat door de emulsie verstrooit",
        "Halação modelada a partir da luz que se espalha pela emulsão",
        "根据在乳剂中散射的光建模的光晕"),
    "Interimage coupler effects between dye layers": (
        "Interimage-Couplereffekte zwischen den Farbschichten",
        "Efectos de copulantes interimagen entre capas de colorante",
        "Efectos de copulantes interimagen entre capas de colorante",
        "Effets de coupleurs inter-image entre couches de colorant",
        "Effetti dei copulanti interimmagine fra gli strati di colorante",
        "色素層のあいだのインターイメージ・カプラー効果",
        "염료층 사이의 인터이미지 커플러 효과",
        "Interimage-couplereffecten tussen kleurlagen",
        "Efeitos de copulantes interimagem entre camadas de corante",
        "染料层之间的层间成色剂效应"),
    "Density-based grain that forms where light actually landed": (
        "Dichteabhängiges Korn, das dort entsteht, wo Licht tatsächlich gelandet ist",
        "Grano según la densidad, que se forma donde la luz llegó de verdad",
        "Grano según la densidad, que se forma donde la luz llegó de verdad",
        "Grain lié à la densité, qui se forme là où la lumière est réellement tombée",
        "Grana legata alla densità, che si forma dove la luce è davvero arrivata",
        "光が実際に落ちた場所に生まれる、濃度に応じた粒子",
        "빛이 실제로 닿은 자리에 생기는, 농도에 따른 입자",
        "Korrel op basis van dichtheid, die ontstaat waar licht echt is geland",
        "Grão conforme a densidade, que se forma onde a luz de fato caiu",
        "随密度变化、生成在光真正落下之处的颗粒"),
    "Four film stocks built from published manufacturer measurements": (
        "Vier Filme, gebaut aus veröffentlichten Herstellermessungen",
        "Cuatro películas construidas a partir de mediciones publicadas por los fabricantes",
        "Cuatro películas construidas a partir de mediciones publicadas por los fabricantes",
        "Quatre pellicules construites à partir de mesures publiées par les fabricants",
        "Quattro pellicole costruite da misure pubblicate dai produttori",
        "メーカー公開の実測値から組み上げた四種のフィルム",
        "제조사가 공개한 실측값으로 만든 네 가지 필름",
        "Vier films gebouwd op gepubliceerde metingen van de fabrikanten",
        "Quatro filmes construídos a partir de medições publicadas pelos fabricantes",
        "依据厂商公开实测数据构建的四款胶片"),
    "ProRAW capture developed on device": (
        "ProRAW-Aufnahme, auf dem Gerät entwickelt",
        "Captura ProRAW revelada en el dispositivo",
        "Captura ProRAW revelada en el dispositivo",
        "Prise de vue ProRAW développée sur l'appareil",
        "Scatto ProRAW sviluppato sul dispositivo",
        "端末上で現像される ProRAW 撮影",
        "기기 안에서 현상되는 ProRAW 촬영",
        "ProRAW-opname op het toestel ontwikkeld",
        "Captura ProRAW revelada no aparelho",
        "在设备上完成显影的 ProRAW 拍摄"),
    "No account, no server, no subscription": (
        "Kein Konto, kein Server, kein Abo", "Sin cuenta, sin servidor, sin suscripción",
        "Sin cuenta, sin servidor, sin suscripción", "Sans compte, sans serveur, sans abonnement",
        "Nessun account, nessun server, nessun abbonamento",
        "アカウントなし、サーバーなし、定額課金なし", "계정 없음, 서버 없음, 구독 없음",
        "Geen account, geen server, geen abonnement", "Sem conta, sem servidor, sem assinatura",
        "无账号、无服务器、无订阅"),
    "A filter is a lookup table: somebody decided in advance what every colour becomes, and the "
    "same input colour always gives the same output. FRMT simulates the photographic process "
    "instead, so what happens to a pixel depends on what surrounds it. Light spreads sideways into "
    "neighbouring areas, dye layers hold each other back, and grain forms according to how much "
    "light actually landed.": (
        "Ein Filter ist eine Nachschlagetabelle: Jemand hat vorab entschieden, was aus jeder Farbe "
        "wird, und dieselbe Eingangsfarbe liefert immer dieselbe Ausgabe. FRMT simuliert "
        "stattdessen den fotografischen Prozess, also hängt das, was mit einem Pixel geschieht, "
        "davon ab, was es umgibt. Licht breitet sich seitwärts in benachbarte Bereiche aus, "
        "Farbschichten halten einander zurück, und Korn entsteht danach, wie viel Licht "
        "tatsächlich gelandet ist.",
        "Un filtro es una tabla de consulta: alguien decidió de antemano en qué se convierte cada "
        "color, y el mismo color de entrada da siempre la misma salida. FRMT simula el proceso "
        "fotográfico en su lugar, así que lo que le pasa a un píxel depende de lo que lo rodea. La "
        "luz se extiende de lado hacia las zonas vecinas, las capas de colorante se frenan entre "
        "sí y el grano se forma según cuánta luz llegó de verdad.",
        "Un filtro es una tabla de consulta: alguien decidió de antemano en qué se convierte cada "
        "color, y el mismo color de entrada da siempre la misma salida. FRMT simula el proceso "
        "fotográfico en su lugar, así que lo que le pasa a un píxel depende de lo que lo rodea. La "
        "luz se extiende de lado hacia las zonas vecinas, las capas de colorante se frenan entre "
        "sí y el grano se forma según cuánta luz llegó de verdad.",
        "Un filtre est une table de conversion : quelqu'un a décidé à l'avance ce que devient "
        "chaque couleur, et la même couleur en entrée donne toujours la même sortie. FRMT simule à "
        "la place le procédé photographique, si bien que ce qui arrive à un pixel dépend de ce qui "
        "l'entoure. La lumière s'étend latéralement vers les zones voisines, les couches de "
        "colorant se retiennent, et le grain se forme selon la quantité de lumière réellement "
        "tombée.",
        "Un filtro è una tabella di consultazione: qualcuno ha deciso in anticipo cosa diventa "
        "ogni colore, e lo stesso colore in ingresso dà sempre la stessa uscita. FRMT simula "
        "invece il processo fotografico, quindi quello che succede a un pixel dipende da ciò che "
        "lo circonda. La luce si allarga di lato verso le zone vicine, gli strati di colorante si "
        "trattengono a vicenda, e la grana si forma in base a quanta luce è davvero arrivata.",
        "フィルターはルックアップテーブルです。どの色が何になるかを誰かが前もって決めていて、"
        "同じ入力色からは必ず同じ出力が出ます。FRMT はその代わりに写真の工程を再現するので、"
        "ある画素に何が起きるかは、そのまわりに何があるかで決まります。光は隣接する領域へ横に"
        "広がり、色素層は互いを抑え合い、粒子は実際に落ちた光の量に応じて生まれます。",
        "필터는 룩업 테이블입니다. 어떤 색이 무엇이 될지 누군가 미리 정해 두었고, 같은 입력 색은 "
        "언제나 같은 출력을 냅니다. FRMT는 대신 사진의 공정을 시뮬레이션하므로, 한 픽셀에 무슨 "
        "일이 일어날지는 그 주변에 무엇이 있는지에 달려 있습니다. 빛은 이웃한 영역으로 옆으로 "
        "퍼지고, 염료층은 서로를 붙잡고, 입자는 실제로 닿은 빛의 양에 따라 생깁니다.",
        "Een filter is een opzoektabel: iemand heeft vooraf besloten wat elke kleur wordt, en "
        "dezelfde invoerkleur geeft altijd dezelfde uitvoer. FRMT simuleert in plaats daarvan het "
        "fotografische proces, dus wat er met een pixel gebeurt hangt af van wat eromheen zit. "
        "Licht spreidt zijwaarts naar naburige gebieden, kleurlagen houden elkaar tegen, en korrel "
        "ontstaat naar gelang hoeveel licht er werkelijk is geland.",
        "Um filtro é uma tabela de consulta: alguém decidiu de antemão no que cada cor vira, e a "
        "mesma cor de entrada dá sempre a mesma saída. O FRMT simula o processo fotográfico em vez "
        "disso, então o que acontece com um pixel depende do que está em volta dele. A luz se "
        "espalha de lado para as áreas vizinhas, as camadas de corante seguram umas às outras, e o "
        "grão se forma conforme quanta luz de fato caiu.",
        "滤镜是一张查找表：有人事先决定了每种颜色会变成什么，同一个输入色永远给出同样的输出。"
        "FRMT 做的是模拟摄影工序，因此一个像素会发生什么，取决于它周围有什么。"
        "光会向侧面扩散到相邻区域，染料层彼此拖住，颗粒则按照实际落下的光量生成。"),
    "Four stocks, each built from its manufacturer's published characteristic curves and spectral "
    "sensitivity data rather than eyeballed from scans.": (
        "Vier Filme, jeder gebaut aus den veröffentlichten Kennlinien und spektralen "
        "Empfindlichkeiten seines Herstellers statt nach Augenmaß aus Scans.",
        "Cuatro películas, cada una construida a partir de las curvas características y los datos "
        "de sensibilidad espectral publicados por su fabricante, no calculadas a ojo desde "
        "escaneos.",
        "Cuatro películas, cada una construida a partir de las curvas características y los datos "
        "de sensibilidad espectral publicados por su fabricante, no calculadas a ojo desde "
        "escaneos.",
        "Quatre pellicules, chacune construite à partir des courbes caractéristiques et des "
        "données de sensibilité spectrale publiées par son fabricant, et non estimées à l'oeil "
        "depuis des scans.",
        "Quattro pellicole, ognuna costruita dalle curve caratteristiche e dai dati di sensibilità "
        "spettrale pubblicati dal suo produttore, non ricavate a occhio da scansioni.",
        "四種のフィルム。いずれも、そのメーカーが公開した特性曲線と分光感度のデータから"
        "組み上げたもので、スキャンを見ながら目分量で合わせたものではありません。",
        "네 가지 필름. 각각 그 제조사가 공개한 특성곡선과 분광 감도 데이터로 만들었고, 스캔을 보며 "
        "눈대중으로 맞춘 것이 아닙니다.",
        "Vier films, elk gebouwd op de gepubliceerde karakteristieke krommen en spectrale "
        "gevoeligheidsdata van de fabrikant, en niet op het oog afgekeken van scans.",
        "Quatro filmes, cada um construído a partir das curvas características e dos dados de "
        "sensibilidade espectral publicados pelo fabricante, e não estimados no olho a partir de "
        "scans.",
        "四款胶片，每一款都建立在其厂商公开的特性曲线和光谱感光度数据之上，"
        "而不是照着扫描件凭眼睛凑出来的。"),
    "Which film stocks does FRMT include?": (
        "Welche Filme enthält FRMT?", "¿Qué películas incluye FRMT?",
        "¿Qué películas incluye FRMT?", "Quelles pellicules FRMT inclut-il ?",
        "Quali pellicole include FRMT?", "FRMT にはどのフィルムが入っていますか。",
        "FRMT에는 어떤 필름이 들어 있나요?", "Welke films bevat FRMT?",
        "Quais filmes o FRMT inclui?", "FRMT 包含哪几款胶片？"),
    "No. FRMT is a single 14.99 US dollar purchase. There is no subscription, no account and no "
    "advertising.": (
        "Nein. FRMT ist ein einmaliger Kauf für 14,99 US-Dollar. Es gibt kein Abo, kein Konto und "
        "keine Werbung.",
        "No. FRMT es una única compra de 14,99 dólares estadounidenses. No hay suscripción, ni "
        "cuenta, ni publicidad.",
        "No. FRMT es una única compra de 14,99 dólares estadounidenses. No hay suscripción, ni "
        "cuenta, ni publicidad.",
        "Non. FRMT est un achat unique de 14,99 dollars américains. Il n'y a pas d'abonnement, pas "
        "de compte et pas de publicité.",
        "No. FRMT è un acquisto unico da 14,99 dollari statunitensi. Non c'è abbonamento, non c'è "
        "account e non c'è pubblicità.",
        "いいえ。FRMT は 14.99 米ドルの一度きりの購入です。定額課金も、アカウントも、"
        "広告もありません。",
        "아니요. FRMT는 14.99 미국 달러 한 번의 구매입니다. 구독도, 계정도, 광고도 없습니다.",
        "Nee. FRMT is een eenmalige aankoop van 14,99 Amerikaanse dollar. Er is geen abonnement, "
        "geen account en geen advertenties.",
        "Não. O FRMT é uma compra única de 14,99 dólares americanos. Não há assinatura, não há "
        "conta e não há publicidade.",
        "不是。FRMT 是一次性购买，14.99 美元。没有订阅、没有账号，也没有广告。"),
    "Is FRMT a subscription?": (
        "Ist FRMT ein Abo?", "¿FRMT es una suscripción?", "¿FRMT es una suscripción?",
        "FRMT est-il un abonnement ?", "FRMT è un abbonamento?", "FRMT は定額課金ですか。",
        "FRMT는 구독인가요?", "Is FRMT een abonnement?", "O FRMT é uma assinatura?",
        "FRMT 是订阅制吗？"),
    "No. Every frame is developed on the iPhone's own GPU. The app contains no networking code at "
    "all, so there is nothing to upload and no server holding a copy.": (
        "Nein. Jedes Bild wird auf der GPU des iPhone selbst entwickelt. Die App enthält überhaupt "
        "keinen Netzwerkcode, es gibt also nichts hochzuladen und keinen Server, der eine Kopie "
        "hält.",
        "No. Cada fotograma se revela en la propia GPU del iPhone. La app no contiene nada de "
        "código de red, así que no hay nada que subir ni servidor alguno guardando una copia.",
        "No. Cada cuadro se revela en la propia GPU del iPhone. La app no contiene nada de código "
        "de red, así que no hay nada que subir ni servidor alguno guardando una copia.",
        "Non. Chaque image est développée sur le GPU de l'iPhone lui-même. L'app ne contient aucun "
        "code réseau, il n'y a donc rien à envoyer et aucun serveur qui en garde une copie.",
        "No. Ogni fotogramma viene sviluppato sulla GPU dell'iPhone stesso. L'app non contiene "
        "proprio codice di rete, quindi non c'è niente da caricare e nessun server che ne tenga "
        "una copia.",
        "いいえ。どの一枚も iPhone 自身の GPU で現像されます。アプリには通信のコードそのものが"
        "入っていないので、送るものも、控えを持つサーバーもありません。",
        "아니요. 모든 프레임이 iPhone 자체의 GPU에서 현상됩니다. 앱에는 네트워크 코드 자체가 들어 "
        "있지 않아서, 올릴 것도 없고 사본을 가진 서버도 없습니다.",
        "Nee. Elk beeld wordt ontwikkeld op de eigen GPU van de iPhone. De app bevat helemaal geen "
        "netwerkcode, dus er valt niets te uploaden en er is geen server met een kopie.",
        "Não. Cada quadro é revelado na própria GPU do iPhone. O app não contém nenhum código de "
        "rede, então não há nada para enviar e nenhum servidor guardando uma cópia.",
        "不会。每一张都在 iPhone 自己的 GPU 上完成显影。应用里根本没有联网代码，"
        "所以没有东西可上传，也没有服务器留副本。"),
    "Because the simulation runs the chemistry rather than looking up an answer. Light transport "
    "through the emulsion, the interaction between dye layers and grain formation are all computed "
    "per frame, which takes real time on a phone.": (
        "Weil die Simulation die Chemie durchrechnet, statt eine Antwort nachzuschlagen. "
        "Lichttransport durch die Emulsion, das Zusammenspiel der Farbschichten und die "
        "Kornbildung werden pro Bild berechnet, und das braucht auf einem Telefon echte Zeit.",
        "Porque la simulación ejecuta la química en vez de consultar una respuesta. El transporte "
        "de luz por la emulsión, la interacción entre capas de colorante y la formación del grano "
        "se calculan por fotograma, y eso lleva tiempo real en un móvil.",
        "Porque la simulación ejecuta la química en vez de consultar una respuesta. El transporte "
        "de luz por la emulsión, la interacción entre capas de colorante y la formación del grano "
        "se calculan por cuadro, y eso lleva tiempo real en un celular.",
        "Parce que la simulation calcule la chimie au lieu de consulter une réponse. Le transport "
        "de la lumière dans l'émulsion, l'interaction entre les couches de colorant et la "
        "formation du grain sont calculés image par image, ce qui prend du temps réel sur un "
        "téléphone.",
        "Perché la simulazione esegue la chimica invece di consultare una risposta. Il trasporto "
        "della luce nell'emulsione, l'interazione fra strati di colorante e la formazione della "
        "grana vengono calcolati per fotogramma, e su un telefono questo richiede tempo vero.",
        "シミュレーションが答えを調べるのではなく、化学を計算しているからです。乳剤のなかの光の"
        "伝わり方、色素層どうしの相互作用、粒子の生成が一枚ごとに計算され、端末の上ではそれに"
        "実際の時間がかかります。",
        "시뮬레이션이 답을 찾아보는 대신 화학을 계산하기 때문입니다. 유제 안에서의 빛의 이동, "
        "염료층 사이의 상호작용, 입자의 형성이 프레임마다 계산되고, 휴대폰에서 그것은 실제 시간을 "
        "잡아먹습니다.",
        "Omdat de simulatie de chemie doorrekent in plaats van een antwoord op te zoeken. "
        "Lichttransport door de emulsie, de wisselwerking tussen kleurlagen en korrelvorming "
        "worden per beeld berekend, en dat kost op een telefoon echte tijd.",
        "Porque a simulação roda a química em vez de consultar uma resposta. O transporte de luz "
        "pela emulsão, a interação entre camadas de corante e a formação do grão são calculados "
        "por quadro, o que leva tempo real num telefone.",
        "因为这套模拟是在跑化学，而不是查一个答案。光在乳剂中的传输、染料层之间的相互作用、"
        "颗粒的生成，都要逐张计算，而这在手机上要花掉实实在在的时间。"),
    "Why does developing a photo take so long?": (
        "Warum dauert das Entwickeln eines Fotos so lange?",
        "¿Por qué tarda tanto en revelarse una foto?",
        "¿Por qué tarda tanto en revelarse una foto?",
        "Pourquoi le développement d'une photo prend-il si longtemps ?",
        "Perché sviluppare una foto ci mette così tanto?",
        "写真の現像にどうしてそんなに時間がかかるのですか。",
        "사진 한 장 현상이 왜 이렇게 오래 걸리나요?",
        "Waarom duurt het ontwikkelen van een foto zo lang?",
        "Por que revelar uma foto demora tanto?", "显影一张照片为什么要这么久？"),
})
