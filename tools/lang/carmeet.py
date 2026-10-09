"""lf.wtf/carmeet, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

This page sells a free game to car people, so it talks the way a car meet talks. Every language
uses the informal address a game site would (du, tú, tu, je, você), French included, and Japanese
and Korean use the casual-polite register (です/ます and 해요체) with plain verbs in the headlines.
The four headlines stay four short verbs: Schrauben / Cruisen / Parken / Knipsen, 組む / 流す /
停める / 撮る, 改起来 / 开起来 / 停下来 / 拍下来.

The scene's own words are used rather than dictionary ones. A car meet is a Car-Meet in German, a
quedada in Spain, a car meet in Mexico, a rassemblement in France, a raduno in Italy, カーミート,
카밋, an autotreffen, an encontro de carros and a 车聚. Tuning a car is schrauben, tunear, armar,
préparer, elaborare, 組む, 튜닝, bouwen, montar and 改. Mexican Spanish has its own garage: carro,
cofre, rines, polarizado, celular, manejar, curva de torque. Vinyls are バイナル and 拉花, the body
kit is エアロパーツ, tint is スモーク and 틴팅, and cruising in Brazil is dar um rolê.

Need for Speed, Underground 2, Electronic Arts, EA, PlayStation 2, PS2 and Quest are names and
are never translated, not even into the titles the game was sold under in Japan and China. The
disclaimer keeps all three of its verbs in every language (affiliated, endorsed, sponsored), and
names Electronic Arts again rather than leaning on a pronoun. In the "How it was made" steps,
terms engineers keep in English stay in English (triangle strip, vector unit, grain, streaming,
WebSockets); the `code` lines keep their notation and translate only the words. Numbers take the
local separator: 2.000 in German, 2 000 in French, 2,000 in Mexico, Japan, Korea and China.
"""

KEEP = {
    "Carmeet", "lf.wtf", "Levi Foster",
    # The MIME type of the trailer's <source>, and the keycaps.
    "video/mp4", "W", "A", "S", "D", "E", "G", "P", "T",
}

NB = " "   # French thousands separator, so 2 000 never breaks across a line.

T = {
    # ------------------------------------------------------------------ head

    "Carmeet: Need for Speed Underground 2's City, Rebuilt as a Browser Car Meet": (
        "Carmeet: Die Stadt aus Need for Speed Underground 2, neu gebaut als Car-Meet im Browser",
        "Carmeet: la ciudad de Need for Speed Underground 2, reconstruida como quedada de coches en el navegador",
        "Carmeet: la ciudad de Need for Speed Underground 2, reconstruida como car meet en el navegador",
        "Carmeet : la ville de Need for Speed Underground 2, reconstruite en rassemblement auto dans le navigateur",
        "Carmeet: la città di Need for Speed Underground 2, ricostruita come raduno d'auto nel browser",
        "Carmeet：Need for Speed Underground 2 の街を、ブラウザのカーミートとして再構築",
        "Carmeet: Need for Speed Underground 2의 도시, 브라우저 카밋으로 재탄생",
        "Carmeet: de stad uit Need for Speed Underground 2, herbouwd als autotreffen in je browser",
        "Carmeet: a cidade de Need for Speed Underground 2, reconstruída como encontro de carros no navegador",
        "Carmeet：Need for Speed Underground 2 的城市，重建为浏览器里的车聚"),

    "Carmeet is a free multiplayer car meet in your browser. The city and 29 cars were reverse engineered from the PS2 disc of Need for Speed: Underground 2 and rebuilt for hanging out: build a car, cruise, meet people.": (
        "Carmeet ist ein kostenloses Multiplayer-Car-Meet in deinem Browser. Die Stadt und 29 Autos wurden per Reverse Engineering von der PS2-Disc von Need for Speed: Underground 2 geholt und zum Abhängen neu gebaut: Auto aufbauen, cruisen, Leute treffen.",
        "Carmeet es una quedada de coches multijugador y gratis en tu navegador. La ciudad y 29 coches se sacaron con ingeniería inversa del disco de PS2 de Need for Speed: Underground 2 y se reconstruyeron para pasar el rato: tunea un coche, sal a rodar, conoce gente.",
        "Carmeet es un car meet multijugador y gratis en tu navegador. La ciudad y 29 carros se sacaron con ingeniería inversa del disco de PS2 de Need for Speed: Underground 2 y se reconstruyeron para pasar el rato: arma un carro, sal a rodar, conoce gente.",
        "Carmeet est un rassemblement auto multijoueur et gratuit dans ton navigateur. La ville et 29 voitures ont été extraites par rétro-ingénierie du disque PS2 de Need for Speed: Underground 2, puis reconstruites pour traîner ensemble : prépare une voiture, balade-toi, rencontre du monde.",
        "Carmeet è un raduno d'auto multigiocatore e gratuito nel tuo browser. La città e 29 auto sono state ricavate con il reverse engineering dal disco PS2 di Need for Speed: Underground 2 e ricostruite per stare insieme: elabora un'auto, fatti un giro, conosci gente.",
        "Carmeet はブラウザで遊べる無料のマルチプレイ・カーミート。Need for Speed: Underground 2 の PS2 ディスクから街と 29 台の車をリバースエンジニアリングで取り出し、たまり場として作り直しました。車を組んで、流して、みんなと会おう。",
        "Carmeet은 브라우저에서 즐기는 무료 멀티플레이 카밋이에요. Need for Speed: Underground 2의 PS2 디스크에서 도시와 차 29대를 리버스 엔지니어링으로 꺼내, 함께 어울리는 공간으로 다시 만들었어요. 차를 튜닝하고, 달리고, 사람들을 만나요.",
        "Carmeet is een gratis multiplayer-autotreffen in je browser. De stad en 29 auto's zijn met reverse engineering van de PS2-disc van Need for Speed: Underground 2 gehaald en herbouwd om samen te chillen: bouw een auto, ga toeren, ontmoet mensen.",
        "Carmeet é um encontro de carros multiplayer e grátis no seu navegador. A cidade e 29 carros foram extraídos por engenharia reversa do disco de PS2 de Need for Speed: Underground 2 e reconstruídos para curtir junto: monte um carro, dê um rolê, conheça gente.",
        "Carmeet 是一个在浏览器里免费玩的多人车聚。城市和 29 辆车是从 Need for Speed: Underground 2 的 PS2 光盘里逆向工程出来的，重建成一个可以一起闲逛的地方：改一辆车，兜兜风，认识新朋友。"),

    "Carmeet: a free car meet in your browser": (
        "Carmeet: ein kostenloses Car-Meet in deinem Browser",
        "Carmeet: una quedada de coches gratis en tu navegador",
        "Carmeet: un car meet gratis en tu navegador",
        "Carmeet : un rassemblement auto gratuit dans ton navigateur",
        "Carmeet: un raduno d'auto gratuito nel tuo browser",
        "Carmeet：ブラウザで遊べる無料のカーミート",
        "Carmeet: 브라우저에서 즐기는 무료 카밋",
        "Carmeet: een gratis autotreffen in je browser",
        "Carmeet: um encontro de carros grátis no seu navegador",
        "Carmeet：浏览器里的免费车聚"),

    "Underground 2's city and cars, reverse engineered from the PS2 disc and rebuilt as a place to hang out. Build a car, cruise one shared city, meet everyone online.": (
        "Die Stadt und die Autos aus Underground 2, per Reverse Engineering von der PS2-Disc geholt und als Treffpunkt neu gebaut. Bau dir ein Auto, cruise durch eine gemeinsame Stadt, triff alle, die online sind.",
        "La ciudad y los coches de Underground 2, sacados del disco de PS2 con ingeniería inversa y reconstruidos como un sitio para pasar el rato. Tunea un coche, rueda por una ciudad compartida y encuéntrate con todos los que están conectados.",
        "La ciudad y los carros de Underground 2, sacados del disco de PS2 con ingeniería inversa y reconstruidos como un lugar para pasar el rato. Arma un carro, rueda por una ciudad compartida y encuéntrate con todos los que están en línea.",
        "La ville et les voitures d'Underground 2, extraites du disque PS2 par rétro-ingénierie et reconstruites comme un lieu où traîner. Prépare une voiture, balade-toi dans une ville partagée, retrouve tous ceux qui sont en ligne.",
        "La città e le auto di Underground 2, ricavate dal disco PS2 con il reverse engineering e ricostruite come posto dove ritrovarsi. Elabora un'auto, gira per un'unica città condivisa, incontra tutti quelli online.",
        "Underground 2 の街と車を PS2 ディスクからリバースエンジニアリングで取り出し、たまり場として作り直しました。車を組んで、みんなで一つの街を流して、オンラインの全員と会おう。",
        "Underground 2의 도시와 차들을 PS2 디스크에서 리버스 엔지니어링으로 꺼내 어울려 노는 공간으로 다시 만들었어요. 차를 튜닝하고, 모두가 함께 쓰는 도시를 달리고, 접속한 모두를 만나요.",
        "De stad en auto's uit Underground 2, met reverse engineering van de PS2-disc gehaald en herbouwd als plek om te chillen. Bouw een auto, toer door één gedeelde stad en ontmoet iedereen die online is.",
        "A cidade e os carros de Underground 2, extraídos do disco de PS2 por engenharia reversa e reconstruídos como um lugar para curtir. Monte um carro, dê um rolê por uma cidade compartilhada e encontre todo mundo que está online.",
        "Underground 2 的城市和车辆，从 PS2 光盘逆向工程而来，重建成一个可以闲逛的地方。改一辆车，在同一座共享城市里兜风，和所有在线的人碰面。"),

    "A car driving through the Carmeet city at night, under the Carmeet wordmark": (
        "Ein Auto fährt nachts durch die Stadt von Carmeet, darüber der Carmeet-Schriftzug",
        "Un coche circulando de noche por la ciudad de Carmeet, bajo el logotipo de Carmeet",
        "Un carro circulando de noche por la ciudad de Carmeet, bajo el logotipo de Carmeet",
        "Une voiture qui roule de nuit dans la ville de Carmeet, sous le logo Carmeet",
        "Un'auto che attraversa di notte la città di Carmeet, sotto il logo Carmeet",
        "Carmeet のロゴの下、夜の Carmeet の街を走る車",
        "Carmeet 로고 아래, 밤의 Carmeet 도시를 달리는 차",
        "Een auto die 's nachts door de stad van Carmeet rijdt, onder het Carmeet-woordmerk",
        "Um carro rodando à noite pela cidade do Carmeet, sob o logotipo do Carmeet",
        "夜晚在 Carmeet 城市中行驶的一辆车，上方是 Carmeet 字标"),

    # ------------------------------------------------------------------ header

    "Sections": (
        "Abschnitte", "Secciones", "Secciones", "Sections", "Sezioni", "セクション", "섹션",
        "Secties", "Seções", "栏目"),

    "What it is": (
        "Was es ist", "Qué es", "Qué es", "C'est quoi", "Cos'è", "Carmeet とは", "Carmeet이란",
        "Wat het is", "O que é", "这是什么"),

    "How it was made": (
        "So entstand es", "Cómo se hizo", "Cómo se hizo", "Comment c'est fait",
        "Come è stato fatto", "制作の裏側", "제작 과정", "Hoe het gemaakt is", "Como foi feito",
        "制作过程"),

    "Play": (
        "Spielen", "Jugar", "Jugar", "Jouer", "Gioca", "プレイ", "플레이", "Spelen", "Jogar",
        "开玩"),

    # ------------------------------------------------------------------ hero

    "Build your car. Cruise one shared city.": (
        "Bau dein Auto. Cruise durch eine gemeinsame Stadt.",
        "Tunea tu coche. Rueda por una ciudad compartida.",
        "Arma tu carro. Rueda por una ciudad compartida.",
        "Prépare ta caisse. Balade-toi dans une ville partagée.",
        "Elabora la tua auto. Gira per un'unica città condivisa.",
        "車を組んで、ひとつの街を流す。",
        "차를 튜닝하고, 하나의 도시를 함께 달려요.",
        "Bouw je auto. Toer door één gedeelde stad.",
        "Monte seu carro. Dê um rolê por uma cidade compartilhada.",
        "改好你的车，在同一座城市里兜风。"),

    "Meet everyone online.": (
        "Triff alle, die online sind.",
        "Encuéntrate con todos los conectados.",
        "Encuéntrate con todos en línea.",
        "Retrouve tout le monde en ligne.",
        "Incontra tutti quelli online.",
        "オンラインのみんなと会おう。",
        "접속한 모두를 만나요.",
        "Ontmoet iedereen online.",
        "Encontre todo mundo online.",
        "和所有在线玩家碰面。"),

    "Carmeet is a free multiplayer car meet that runs in your browser. The city, the 29 cars and the garage come from the PlayStation 2 disc of Need for Speed: Underground 2, taken apart file by file and rebuilt for the web. The racing is gone. What is left is the part everyone remembers: building a car and rolling up to show it off.": (
        "Carmeet ist ein kostenloses Multiplayer-Car-Meet, das in deinem Browser läuft. Die Stadt, die 29 Autos und die Garage stammen von der Disc von Need for Speed: Underground 2 für die PlayStation 2, Datei für Datei zerlegt und fürs Web neu gebaut. Die Rennen sind weg. Geblieben ist der Teil, an den sich alle erinnern: ein Auto aufbauen und damit vorfahren, um es herzuzeigen.",
        "Carmeet es una quedada de coches multijugador y gratis que funciona en tu navegador. La ciudad, los 29 coches y el garaje salen del disco de PlayStation 2 de Need for Speed: Underground 2, desmontado archivo por archivo y reconstruido para la web. Las carreras ya no están. Queda la parte que todos recuerdan: tunear un coche y llegar con él para lucirlo.",
        "Carmeet es un car meet multijugador y gratis que funciona en tu navegador. La ciudad, los 29 carros y el garaje salen del disco de PlayStation 2 de Need for Speed: Underground 2, desarmado archivo por archivo y reconstruido para la web. Las carreras ya no están. Queda la parte que todos recuerdan: armar un carro y llegar con él para presumirlo.",
        "Carmeet est un rassemblement auto multijoueur et gratuit qui tourne dans ton navigateur. La ville, les 29 voitures et le garage viennent du disque PlayStation 2 de Need for Speed: Underground 2, démonté fichier par fichier et reconstruit pour le web. Les courses ont disparu. Il reste ce dont tout le monde se souvient : préparer une voiture et débarquer avec pour la montrer.",
        "Carmeet è un raduno d'auto multigiocatore e gratuito che gira nel tuo browser. La città, le 29 auto e il garage vengono dal disco PlayStation 2 di Need for Speed: Underground 2, smontato file per file e ricostruito per il web. Le gare non ci sono più. Resta la parte che tutti ricordano: elaborare un'auto e presentarsi al raduno per farla vedere.",
        "Carmeet はブラウザで動く無料のマルチプレイ・カーミート。街も、29 台の車も、ガレージも、Need for Speed: Underground 2 の PlayStation 2 ディスクから来ています。ファイルを一つずつバラして、Web 向けに組み直しました。レースはありません。残ったのは、みんなが覚えているあの部分。車を組んで、見せびらかしに乗りつけることです。",
        "Carmeet은 브라우저에서 돌아가는 무료 멀티플레이 카밋이에요. 도시, 29대의 차, 그리고 차고는 모두 Need for Speed: Underground 2의 PlayStation 2 디스크에서 왔어요. 파일 하나하나 뜯어서 웹용으로 다시 만들었죠. 레이스는 빠졌어요. 남은 건 모두가 기억하는 그 부분, 차를 튜닝해서 자랑하러 몰고 가는 거예요.",
        "Carmeet is een gratis multiplayer-autotreffen dat in je browser draait. De stad, de 29 auto's en de garage komen van de PlayStation 2-disc van Need for Speed: Underground 2, bestand voor bestand uit elkaar gehaald en herbouwd voor het web. Het racen is eruit. Wat overblijft is het deel dat iedereen zich herinnert: een auto opbouwen en ermee komen aanrijden om hem te laten zien.",
        "Carmeet é um encontro de carros multiplayer e grátis que roda no seu navegador. A cidade, os 29 carros e a garagem vêm do disco de PlayStation 2 de Need for Speed: Underground 2, desmontado arquivo por arquivo e reconstruído para a web. As corridas saíram. Ficou a parte de que todo mundo lembra: montar um carro e chegar com ele para exibir.",
        "Carmeet 是一个在浏览器里运行的免费多人车聚。城市、29 辆车和车库都来自 Need for Speed: Underground 2 的 PlayStation 2 光盘，被一个文件一个文件地拆开，再为网页重建。比赛没有了。留下的是大家都记得的那部分：改一辆车，开过去秀一秀。"),

    "Play free in your browser": (
        "Kostenlos im Browser spielen", "Juega gratis en tu navegador",
        "Juega gratis en tu navegador", "Joue gratuitement dans ton navigateur",
        "Gioca gratis nel browser", "ブラウザで無料プレイ", "브라우저에서 무료로 플레이",
        "Speel gratis in je browser", "Jogue grátis no navegador", "在浏览器里免费玩"),

    "Free roam · one shared city · everyone online": (
        "Free Roam · eine gemeinsame Stadt · alle online",
        "Exploración libre · una ciudad compartida · todos conectados",
        "Exploración libre · una ciudad compartida · todos en línea",
        "Balade libre · une ville partagée · tout le monde en ligne",
        "Free roam · un'unica città condivisa · tutti online",
        "フリーラン · みんなで一つの街 · 全員オンライン",
        "프리 로밍 · 하나의 공유 도시 · 모두 온라인",
        "Free roam · één gedeelde stad · iedereen online",
        "Free roam · uma cidade compartilhada · todo mundo online",
        "自由漫游 · 一座共享城市 · 所有人在线"),

    "cars to build": (
        "Autos zum Aufbauen", "coches para tunear", "carros para armar", "voitures à préparer",
        "auto da elaborare", "カスタムできる車", "튜닝 가능한 차", "auto's om te bouwen",
        "carros para montar", "可改装车辆"),

    "shared city": (
        "gemeinsame Stadt", "ciudad compartida", "ciudad compartida", "ville partagée",
        "città condivisa", "共有の街", "공유 도시", "gedeelde stad",
        "cidade compartilhada", "共享城市"),

    "players per server": (
        "Spieler pro Server", "jugadores por servidor", "jugadores por servidor",
        "joueurs par serveur", "giocatori per server", "サーバーあたりの人数", "서버당 플레이어",
        "spelers per server", "jogadores por servidor", "每台服务器玩家数"),

    "downloads": (
        "Downloads", "descargas", "descargas", "téléchargement", "download", "ダウンロード",
        "다운로드", "downloads", "downloads", "下载"),

    "Carmeet trailer: a convoy through the city, building cars, the meet, and the phone camera": (
        "Carmeet-Trailer: ein Konvoi durch die Stadt, Autos aufbauen, das Treffen und die Handykamera",
        "Tráiler de Carmeet: un convoy por la ciudad, tuneando coches, la quedada y la cámara del móvil",
        "Tráiler de Carmeet: un convoy por la ciudad, armando carros, el car meet y la cámara del celular",
        "Bande-annonce de Carmeet : un convoi dans la ville, la prépa des voitures, le rassemblement et l'appareil photo du téléphone",
        "Trailer di Carmeet: un convoglio in città, auto da elaborare, il raduno e la fotocamera del telefono",
        "Carmeet のトレーラー：街を走る車列、車のカスタム、ミート、スマホのカメラ",
        "Carmeet 트레일러: 도시를 달리는 차량 행렬, 차 튜닝, 카밋, 그리고 폰 카메라",
        "Carmeet-trailer: een konvooi door de stad, auto's bouwen, het treffen en de telefooncamera",
        "Trailer do Carmeet: um comboio pela cidade, montando carros, o encontro e a câmera do celular",
        "Carmeet 预告片：穿城而过的车队、改装车辆、车聚现场和手机相机"),

    "Sound": (
        "Ton", "Sonido", "Sonido", "Son", "Audio", "サウンド", "소리", "Geluid", "Som", "声音"),

    "Trailer, captured in the game": (
        "Trailer, im Spiel aufgenommen", "Tráiler, grabado dentro del juego",
        "Tráiler, grabado dentro del juego", "Bande-annonce, capturée dans le jeu",
        "Trailer, registrato nel gioco", "トレーラー、ゲーム内で撮影", "트레일러, 게임 안에서 녹화",
        "Trailer, opgenomen in de game", "Trailer, gravado dentro do jogo", "预告片，于游戏内录制"),

    # ------------------------------------------------------------------ what it is

    "The Carmeet garage: a silver Nissan 350Z on the turntable, with the Customize menu open": (
        "Die Garage von Carmeet: ein silberner Nissan 350Z auf der Drehscheibe, das Customize-Menü geöffnet",
        "El garaje de Carmeet: un Nissan 350Z plateado en la plataforma giratoria, con el menú Customize abierto",
        "El garaje de Carmeet: un Nissan 350Z plateado en la plataforma giratoria, con el menú Customize abierto",
        "Le garage de Carmeet : une Nissan 350Z argentée sur le plateau tournant, avec le menu Customize ouvert",
        "Il garage di Carmeet: una Nissan 350Z argento sulla pedana girevole, con il menu Customize aperto",
        "Carmeet のガレージ：ターンテーブルに載ったシルバーの Nissan 350Z と、開いた Customize メニュー",
        "Carmeet 차고: 턴테이블 위의 은색 Nissan 350Z와 열린 Customize 메뉴",
        "De garage van Carmeet: een zilveren Nissan 350Z op de draaischijf, met het Customize-menu open",
        "A garagem do Carmeet: um Nissan 350Z prata na plataforma giratória, com o menu Customize aberto",
        "Carmeet 车库：转台上的一辆银色 Nissan 350Z，Customize 菜单已打开"),

    "01 · Garage": (
        "01 · Garage", "01 · Garaje", "01 · Garaje", "01 · Garage", "01 · Garage",
        "01 · ガレージ", "01 · 차고", "01 · Garage", "01 · Garagem", "01 · 车库"),

    "Build it": (
        "Schrauben", "Tunéalo", "Ármalo", "Prépare-la", "Elaborala", "組む", "튜닝해요",
        "Bouw 'm", "Monte o seu", "改起来"),

    "Pick one of 29 cars from the game and work through the original garage. The menu icons, the italic menu font and the gauges are decoded from the disc too, so it looks the way it did in 2004.": (
        "Such dir eines von 29 Autos aus dem Spiel aus und arbeite dich durch die Original-Garage. Auch die Menüsymbole, die kursive Menüschrift und die Anzeigen sind von der Disc dekodiert, damit alles so aussieht wie 2004.",
        "Elige uno de los 29 coches del juego y pásalo por el garaje original. Los iconos del menú, la tipografía cursiva y los indicadores también se han decodificado del disco, así que todo se ve como en 2004.",
        "Elige uno de los 29 carros del juego y pásalo por el garaje original. Los íconos del menú, la tipografía cursiva y los indicadores también se decodificaron del disco, así que todo se ve como en 2004.",
        "Choisis l'une des 29 voitures du jeu et passe-la dans le garage d'origine. Les icônes des menus, la police italique et les compteurs sont eux aussi décodés depuis le disque : tout a l'air comme en 2004.",
        "Scegli una delle 29 auto del gioco e passala nel garage originale. Anche le icone del menu, il font corsivo e gli strumenti sono decodificati dal disco, così è tutto come nel 2004.",
        "ゲームに登場する 29 台から 1 台を選んで、オリジナルのガレージでいじろう。メニューのアイコンも、斜体のメニューフォントも、メーターもディスクからデコードしたもの。見た目は 2004 年のままです。",
        "게임 속 29대 중 한 대를 골라 오리지널 차고에서 손봐요. 메뉴 아이콘, 기울어진 메뉴 폰트, 계기판도 디스크에서 디코딩해서 2004년 그 모습 그대로예요.",
        "Kies een van de 29 auto's uit de game en werk hem af in de originele garage. Ook de menu-iconen, het cursieve menulettertype en de meters zijn van de disc gedecodeerd, dus het ziet eruit zoals in 2004.",
        "Escolha um dos 29 carros do jogo e trabalhe nele na garagem original. Os ícones do menu, a fonte itálica do menu e os medidores também foram decodificados do disco, então tudo fica igualzinho a 2004.",
        "从游戏里的 29 辆车中挑一辆，在原版车库里一项项改。菜单图标、斜体菜单字体和仪表也都是从光盘里解码出来的，所以看起来就和 2004 年一样。"),

    "Body kits": (
        "Bodykits", "Kits de carrocería", "Kits de carrocería", "Kits carrosserie", "Body kit",
        "エアロパーツ", "바디킷", "Bodykits", "Body kits", "车身套件"),

    "Hoods and wings": (
        "Hauben und Heckflügel", "Capós y alerones", "Cofres y alerones", "Capots et ailerons",
        "Cofani e alettoni", "ボンネットとウイング", "보닛과 윙", "Motorkappen en spoilers",
        "Capôs e aerofólios", "引擎盖和尾翼"),

    "Paint": (
        "Lack", "Pintura", "Pintura", "Peinture", "Vernice", "塗装", "도색", "Lak", "Pintura",
        "喷漆"),

    "Vinyls": (
        "Vinyls", "Vinilos", "Viniles", "Vinyles", "Vinili", "バイナル", "비닐", "Vinyls", "Vinis",
        "拉花"),

    "Wheels": (
        "Felgen", "Llantas", "Rines", "Jantes", "Cerchi", "ホイール", "휠", "Velgen", "Rodas",
        "轮毂"),

    "Tint": (
        "Scheibentönung", "Lunas tintadas", "Polarizado", "Vitres teintées", "Vetri oscurati",
        "スモーク", "틴팅", "Getinte ramen", "Vidros fumê", "车窗贴膜"),

    "Neon": (
        "Neon", "Neón", "Neón", "Néons", "Neon", "ネオン", "네온", "Neon", "Neon", "霓虹灯"),

    "Driving through the city at night with the speedometer, map and chat on screen": (
        "Nachts durch die Stadt fahren, mit Tacho, Karte und Chat auf dem Bildschirm",
        "Conduciendo de noche por la ciudad con el velocímetro, el mapa y el chat en pantalla",
        "Manejando de noche por la ciudad con el velocímetro, el mapa y el chat en pantalla",
        "Conduite de nuit dans la ville, avec le compteur, la carte et le chat à l'écran",
        "Alla guida di notte in città, con tachimetro, mappa e chat sullo schermo",
        "スピードメーター、マップ、チャットを表示したまま夜の街を走る",
        "속도계, 지도, 채팅이 떠 있는 화면으로 밤의 도시를 달리는 모습",
        "'s Nachts door de stad rijden, met de snelheidsmeter, kaart en chat in beeld",
        "Dirigindo à noite pela cidade com o velocímetro, o mapa e o chat na tela",
        "夜里在城中驾驶，屏幕上显示着速度表、地图和聊天"),

    "02 · Streets": (
        "02 · Straße", "02 · Calles", "02 · Calles", "02 · La rue", "02 · Strade",
        "02 · ストリート", "02 · 거리", "02 · Straat", "02 · Ruas", "02 · 街头"),

    "Cruise it": (
        "Cruisen", "Sácalo a rodar", "Sácalo a rodar", "Balade-la", "Portala in giro", "流す",
        "달려요", "Toer ermee", "Dê um rolê", "开起来"),

    "Everyone who opens the link lands in the same city. Each car drives on its own torque curve and gearing from the game's data. Talk over proximity voice, type in the chat, and read the name plates to see who is who.": (
        "Alle, die den Link öffnen, landen in derselben Stadt. Jedes Auto fährt mit seiner eigenen Drehmomentkurve und Übersetzung aus den Spieldaten. Sprich per Proximity-Voice-Chat, schreib im Chat und lies die Namensschilder, um zu sehen, wer wer ist.",
        "Todos los que abren el enlace aparecen en la misma ciudad. Cada coche va con su propia curva de par y sus desarrollos, sacados de los datos del juego. Habla por voz de proximidad, escribe en el chat y lee las etiquetas de nombre para saber quién es quién.",
        "Todos los que abren el link llegan a la misma ciudad. Cada carro anda con su propia curva de torque y sus relaciones de transmisión, sacadas de los datos del juego. Habla por voz de proximidad, escribe en el chat y lee las etiquetas de nombre para saber quién es quién.",
        "Tous ceux qui ouvrent le lien arrivent dans la même ville. Chaque voiture roule avec sa propre courbe de couple et son étagement de boîte, tirés des données du jeu. Parle en vocal de proximité, écris dans le chat et lis les pseudos au-dessus des têtes pour savoir qui est qui.",
        "Chi apre il link finisce nella stessa città. Ogni auto va con la sua curva di coppia e i suoi rapporti del cambio, presi dai dati del gioco. Parla con la chat vocale di prossimità, scrivi in chat e leggi le targhette con i nomi per capire chi è chi.",
        "リンクを開いた人はみんな同じ街に降り立ちます。各車はゲームのデータにあるトルクカーブとギア比で走ります。近くの人とボイスで話して、チャットに打ち込んで、ネームプレートで誰が誰かをチェック。",
        "링크를 연 사람은 모두 같은 도시에 도착해요. 차마다 게임 데이터에 있는 고유한 토크 커브와 기어비로 달려요. 근거리 보이스로 대화하고, 채팅을 치고, 네임 플레이트로 누가 누군지 확인해요.",
        "Iedereen die de link opent, komt in dezelfde stad terecht. Elke auto rijdt met zijn eigen koppelkromme en overbrengingen uit de gamedata. Praat via proximity voice, typ in de chat en lees de naambordjes om te zien wie wie is.",
        "Todo mundo que abre o link cai na mesma cidade. Cada carro anda com sua própria curva de torque e relação de marchas, tiradas dos dados do jogo. Fale por voz de proximidade, digite no chat e leia as plaquinhas de nome para saber quem é quem.",
        "所有打开链接的人都会进入同一座城市。每辆车都按游戏数据里自己的扭矩曲线和齿比来跑。用近距离语音聊天，在聊天框里打字，看名牌就知道谁是谁。"),

    "A player out of the car, dancing next to a parked 350Z on a city street": (
        "Ein Spieler ist ausgestiegen und tanzt neben einem geparkten 350Z auf einer Straße der Stadt",
        "Un jugador fuera del coche, bailando junto a un 350Z aparcado en una calle de la ciudad",
        "Un jugador fuera del carro, bailando junto a un 350Z estacionado en una calle de la ciudad",
        "Un joueur descendu de sa voiture, qui danse à côté d'une 350Z garée dans une rue de la ville",
        "Un giocatore sceso dall'auto che balla accanto a una 350Z parcheggiata in una strada della città",
        "車を降りたプレイヤーが、街の通りに停めた 350Z の横で踊っている",
        "차에서 내린 플레이어가 도시 거리에 세워진 350Z 옆에서 춤추는 모습",
        "Een speler buiten zijn auto, dansend naast een geparkeerde 350Z in een straat in de stad",
        "Um jogador fora do carro, dançando ao lado de um 350Z estacionado numa rua da cidade",
        "一名下了车的玩家，在城市街道上一辆停着的 350Z 旁跳舞"),

    "03 · The meet": (
        "03 · Das Treffen", "03 · La quedada", "03 · El car meet", "03 · Le rasso",
        "03 · Il raduno", "03 · ミート", "03 · 카밋", "03 · Het treffen", "03 · O encontro",
        "03 · 车聚"),

    "Park it": (
        "Parken", "Apárcalo", "Estaciónalo", "Gare-la", "Parcheggiala", "停める", "세워요",
        "Parkeer 'm", "Estacione", "停下来"),

    "Stop anywhere, get out and walk. Sprint over to someone's car, then wave, cheer, point, dance or sit. Your driver is yours to dress, and they follow you onto the street.": (
        "Halt irgendwo an, steig aus und lauf los. Sprinte zum Auto von jemand anderem, dann wink, jubel, zeig, tanz oder setz dich. Deine Fahrerfigur stylst du selbst, und sie kommt mit dir auf die Straße.",
        "Para donde quieras, bájate y camina. Corre hasta el coche de alguien y saluda, anima, señala, baila o siéntate. A tu piloto lo vistes tú, y te acompaña a la calle.",
        "Detente donde quieras, bájate y camina. Corre hasta el carro de alguien y saluda, echa porras, señala, baila o siéntate. A tu piloto lo vistes tú, y sale contigo a la calle.",
        "Arrête-toi n'importe où, descends et marche. Pique un sprint jusqu'à la voiture de quelqu'un, puis salue, acclame, pointe du doigt, danse ou assieds-toi. Ton pilote, tu l'habilles comme tu veux, et il te suit dans la rue.",
        "Fermati dove vuoi, scendi e cammina. Corri fino all'auto di qualcuno, poi saluta, esulta, indica, balla o siediti. Il tuo pilota lo vesti come vuoi tu, e ti segue in strada.",
        "どこでも停めて、降りて歩こう。誰かの車までダッシュして、手を振ったり、盛り上がったり、指さしたり、踊ったり、座ったり。ドライバーの服は自由に選べて、そのまま一緒にストリートへ出てきます。",
        "아무 데나 세우고 내려서 걸어요. 다른 사람 차까지 달려가서 손 흔들고, 환호하고, 가리키고, 춤추고, 앉아요. 드라이버 옷은 마음대로 입힐 수 있고, 그대로 거리까지 따라 나와요.",
        "Stop waar je wilt, stap uit en loop. Sprint naar iemands auto en zwaai, juich, wijs, dans of ga zitten. Je bestuurder kleed je zelf aan, en die loopt met je mee de straat op.",
        "Pare em qualquer lugar, desça e ande. Corra até o carro de alguém e acene, comemore, aponte, dance ou sente. Seu piloto você veste do seu jeito, e ele te acompanha pela rua.",
        "随便在哪儿停下，下车走走。冲到别人的车旁，然后挥手、欢呼、指一指、跳舞或者坐下。你的车手穿什么由你定，车手也会跟着你走上街头。"),

    "A photo taken with the in-game phone: players cheering between rows of parked cars": (
        "Ein Foto mit dem Handy im Spiel: Spieler jubeln zwischen Reihen geparkter Autos",
        "Una foto hecha con el móvil del juego: jugadores animando entre filas de coches aparcados",
        "Una foto tomada con el celular del juego: jugadores echando porras entre filas de carros estacionados",
        "Une photo prise avec le téléphone du jeu : des joueurs qui acclament entre des rangées de voitures garées",
        "Una foto scattata con il telefono del gioco: giocatori che esultano tra file di auto parcheggiate",
        "ゲーム内のスマホで撮った写真：並んで停まった車の間で盛り上がるプレイヤーたち",
        "게임 속 폰으로 찍은 사진: 줄지어 세워진 차들 사이에서 환호하는 플레이어들",
        "Een foto gemaakt met de telefoon in de game: spelers die juichen tussen rijen geparkeerde auto's",
        "Uma foto tirada com o celular do jogo: jogadores comemorando entre fileiras de carros estacionados",
        "用游戏内手机拍的照片：玩家们在一排排停着的车之间欢呼"),

    "A selfie taken with the in-game phone's front camera at the meet": (
        "Ein Selfie mit der Frontkamera des Handys im Spiel, aufgenommen beim Treffen",
        "Un selfi hecho con la cámara frontal del móvil del juego en la quedada",
        "Una selfie tomada con la cámara frontal del celular del juego en el car meet",
        "Un selfie pris avec la caméra avant du téléphone du jeu, au rassemblement",
        "Un selfie scattato con la fotocamera frontale del telefono del gioco al raduno",
        "ミートでゲーム内スマホのインカメラを使って撮った自撮り",
        "카밋에서 게임 속 폰 전면 카메라로 찍은 셀카",
        "Een selfie gemaakt met de voorcamera van de telefoon in de game, op het treffen",
        "Uma selfie tirada com a câmera frontal do celular do jogo no encontro",
        "在车聚上用游戏内手机前置摄像头拍的自拍"),

    "Both photos were taken with the phone in the game.": (
        "Beide Fotos wurden mit dem Handy im Spiel gemacht.",
        "Las dos fotos se hicieron con el móvil del juego.",
        "Las dos fotos se tomaron con el celular del juego.",
        "Les deux photos ont été prises avec le téléphone du jeu.",
        "Entrambe le foto sono state scattate con il telefono del gioco.",
        "どちらの写真もゲーム内のスマホで撮影しました。",
        "두 사진 모두 게임 속 폰으로 찍었어요.",
        "Beide foto's zijn gemaakt met de telefoon in de game.",
        "As duas fotos foram tiradas com o celular do jogo.",
        "两张照片都是用游戏里的手机拍的。"),

    "04 · Phone": (
        "04 · Handy", "04 · Móvil", "04 · Celular", "04 · Téléphone", "04 · Telefono",
        "04 · スマホ", "04 · 폰", "04 · Telefoon", "04 · Celular", "04 · 手机"),

    "Shoot it": (
        "Knipsen", "Sácale fotos", "Tómale fotos", "Mitraille", "Scatta", "撮る", "찍어요",
        "Schiet plaatjes", "Fotografe", "拍下来"),

    "Take out your phone and shoot the meet, back camera or selfie. Every photo gets a film grain and grade, is saved in your browser, and shows up in the garage.": (
        "Zück dein Handy und fotografier das Treffen, mit der Rückkamera oder als Selfie. Jedes Foto bekommt Filmkorn und ein Color Grading, wird in deinem Browser gespeichert und taucht in der Garage auf.",
        "Saca el móvil y fotografía la quedada, con la cámara trasera o en selfi. Cada foto lleva grano de película y etalonaje, se guarda en tu navegador y aparece en el garaje.",
        "Saca el celular y tómale fotos al car meet, con la cámara trasera o en selfie. Cada foto lleva grano de película y corrección de color, se guarda en tu navegador y aparece en el garaje.",
        "Sors ton téléphone et mitraille le rassemblement, caméra arrière ou selfie. Chaque photo reçoit un grain et un étalonnage façon film, est enregistrée dans ton navigateur et apparaît dans le garage.",
        "Tira fuori il telefono e fotografa il raduno, con la fotocamera posteriore o in selfie. Ogni foto riceve grana e color grading da pellicola, viene salvata nel browser e compare nel garage.",
        "スマホを取り出して、ミートを撮ろう。アウトカメラでも自撮りでも。どの写真にもフィルムの粒子とカラーグレーディングがかかり、ブラウザに保存されて、ガレージに表示されます。",
        "폰을 꺼내 카밋을 찍어요. 후면 카메라든 셀카든 상관없어요. 모든 사진에 필름 그레인과 색보정이 들어가고, 브라우저에 저장되어 차고에 나타나요.",
        "Pak je telefoon en schiet plaatjes van het treffen, met de achtercamera of als selfie. Elke foto krijgt filmkorrel en een color grade, wordt in je browser bewaard en verschijnt in de garage.",
        "Pegue o celular e fotografe o encontro, com a câmera traseira ou de selfie. Cada foto ganha granulação e tratamento de cor de filme, fica salva no navegador e aparece na garagem.",
        "掏出手机拍下车聚，后置摄像头或自拍都行。每张照片都会加上胶片颗粒和调色，保存在你的浏览器里，并出现在车库中。"),

    # ------------------------------------------------------------------ reel

    "Frames from the trailer": (
        "Standbilder aus dem Trailer", "Fotogramas del tráiler", "Fotogramas del tráiler",
        "Images de la bande-annonce", "Fotogrammi dal trailer", "トレーラーからのカット",
        "트레일러 장면들", "Beelden uit de trailer", "Quadros do trailer", "预告片截帧"),

    "A blue car with a wing on the garage turntable": (
        "Ein blaues Auto mit Heckflügel auf der Drehscheibe in der Garage",
        "Un coche azul con alerón en la plataforma giratoria del garaje",
        "Un carro azul con alerón en la plataforma giratoria del garaje",
        "Une voiture bleue avec aileron sur le plateau tournant du garage",
        "Un'auto blu con alettone sulla pedana girevole del garage",
        "ガレージのターンテーブルに載った、ウイング付きの青い車",
        "차고 턴테이블 위, 윙을 단 파란 차",
        "Een blauwe auto met spoiler op de draaischijf in de garage",
        "Um carro azul com aerofólio na plataforma giratória da garagem",
        "车库转台上一辆装着尾翼的蓝色车"),

    "A red car with a web vinyl in the garage": (
        "Ein rotes Auto mit Spinnennetz-Vinyl in der Garage",
        "Un coche rojo con un vinilo de telaraña en el garaje",
        "Un carro rojo con un vinil de telaraña en el garaje",
        "Une voiture rouge avec un vinyle toile d'araignée dans le garage",
        "Un'auto rossa con un vinile a ragnatela nel garage",
        "ガレージにある、クモの巣バイナルの赤い車",
        "차고 안, 거미줄 비닐을 입힌 빨간 차",
        "Een rode auto met een spinnenweb-vinyl in de garage",
        "Um carro vermelho com um vinil de teia de aranha na garagem",
        "车库里一辆贴着蛛网拉花的红色车"),

    "Players gathered between parked cars at the meet": (
        "Spieler versammelt zwischen geparkten Autos beim Treffen",
        "Jugadores reunidos entre coches aparcados en la quedada",
        "Jugadores reunidos entre carros estacionados en el car meet",
        "Des joueurs réunis entre les voitures garées au rassemblement",
        "Giocatori riuniti tra le auto parcheggiate al raduno",
        "ミートで停めた車の間に集まるプレイヤーたち",
        "카밋에서 세워진 차들 사이에 모인 플레이어들",
        "Spelers verzameld tussen geparkeerde auto's op het treffen",
        "Jogadores reunidos entre carros estacionados no encontro",
        "车聚上聚在停放车辆之间的玩家们"),

    "A player cheering beside a white car with neon underglow": (
        "Ein Spieler jubelt neben einem weißen Auto mit Neon-Unterbodenbeleuchtung",
        "Un jugador animando junto a un coche blanco con neón en los bajos",
        "Un jugador echando porras junto a un carro blanco con luces de neón por debajo",
        "Un joueur qui acclame à côté d'une voiture blanche avec néons sous caisse",
        "Un giocatore che esulta accanto a un'auto bianca con neon sottoscocca",
        "アンダーネオンを光らせた白い車の横で盛り上がるプレイヤー",
        "언더글로우 네온을 단 흰 차 옆에서 환호하는 플레이어",
        "Een speler die juicht naast een witte auto met neon-underglow",
        "Um jogador comemorando ao lado de um carro branco com neon embaixo",
        "一名玩家在装着底盘霓虹灯的白色车旁欢呼"),

    "The in-game phone raised to photograph the crowd": (
        "Das Handy im Spiel, hochgehalten, um die Menge zu fotografieren",
        "El móvil del juego en alto para fotografiar a la gente",
        "El celular del juego en alto para tomarle foto a la gente",
        "Le téléphone du jeu levé pour photographier la foule",
        "Il telefono del gioco alzato per fotografare la folla",
        "人だかりを撮ろうと掲げたゲーム内のスマホ",
        "사람들을 찍으려고 들어 올린 게임 속 폰",
        "De telefoon in de game omhooggehouden om de menigte te fotograferen",
        "O celular do jogo erguido para fotografar a galera",
        "举起游戏内手机拍摄人群"),

    "The city from above, with a convoy on the road between towers": (
        "Die Stadt von oben, ein Konvoi auf der Straße zwischen Hochhäusern",
        "La ciudad desde arriba, con un convoy en la carretera entre rascacielos",
        "La ciudad desde arriba, con un convoy en la carretera entre rascacielos",
        "La ville vue d'en haut, avec un convoi sur la route entre les tours",
        "La città dall'alto, con un convoglio sulla strada tra i grattacieli",
        "上から見た街と、ビルの間の道を走る車列",
        "위에서 본 도시, 빌딩 사이 도로를 달리는 차량 행렬",
        "De stad van bovenaf, met een konvooi op de weg tussen torens",
        "A cidade vista de cima, com um comboio na pista entre os prédios",
        "俯瞰城市，高楼之间的道路上有一支车队"),

    "The meet from directly above: rows of customized cars": (
        "Das Treffen direkt von oben: Reihen getunter Autos",
        "La quedada vista desde arriba: filas de coches tuneados",
        "El car meet visto desde arriba: filas de carros tuneados",
        "Le rassemblement vu du dessus : des rangées de voitures préparées",
        "Il raduno visto dall'alto: file di auto elaborate",
        "真上から見たミート：カスタムカーがずらりと並ぶ",
        "바로 위에서 본 카밋: 줄지어 선 튜닝카들",
        "Het treffen recht van bovenaf: rijen getunede auto's",
        "O encontro visto de cima: fileiras de carros tunados",
        "正上方俯瞰车聚：一排排改装车"),

    "Frames from the trailer. Scroll sideways for more.": (
        "Standbilder aus dem Trailer. Seitlich scrollen für mehr.",
        "Fotogramas del tráiler. Desliza hacia el lado para ver más.",
        "Fotogramas del tráiler. Desliza hacia el lado para ver más.",
        "Images de la bande-annonce. Fais défiler sur le côté pour en voir plus.",
        "Fotogrammi dal trailer. Scorri di lato per vederne altri.",
        "トレーラーからのカット。横にスクロールするともっと見られます。",
        "트레일러 장면들. 옆으로 스크롤하면 더 볼 수 있어요.",
        "Beelden uit de trailer. Scrol opzij voor meer.",
        "Quadros do trailer. Role para o lado para ver mais.",
        "预告片截帧。横向滚动查看更多。"),

    # ------------------------------------------------------------------ how it was made

    "Underground 2 came out in 2004. Its city was never meant to leave the console, so every step of getting it into a browser had to be worked out from the bytes on the disc.": (
        "Underground 2 erschien 2004. Seine Stadt sollte die Konsole nie verlassen, also musste jeder Schritt in den Browser aus den Bytes auf der Disc erarbeitet werden.",
        "Underground 2 salió en 2004. Su ciudad nunca estuvo pensada para salir de la consola, así que cada paso para llevarla a un navegador hubo que descifrarlo a partir de los bytes del disco.",
        "Underground 2 salió en 2004. Su ciudad nunca estuvo pensada para salir de la consola, así que cada paso para llevarla a un navegador se tuvo que descifrar a partir de los bytes del disco.",
        "Underground 2 est sorti en 2004. Sa ville n'était pas censée quitter la console : chaque étape pour l'amener dans un navigateur a dû être reconstituée à partir des octets du disque.",
        "Underground 2 è uscito nel 2004. La sua città non doveva mai lasciare la console, quindi ogni passaggio per portarla in un browser è stato ricavato dai byte del disco.",
        "Underground 2 の発売は 2004 年。その街はコンソールの外に出ることを想定していなかったので、ブラウザに持ち込むまでのすべての工程を、ディスク上のバイトから解き明かす必要がありました。",
        "Underground 2는 2004년에 나왔어요. 그 도시는 콘솔 밖으로 나올 일이 없었기 때문에, 브라우저로 옮기는 모든 단계를 디스크의 바이트에서부터 하나하나 알아내야 했어요.",
        "Underground 2 kwam uit in 2004. De stad was nooit bedoeld om de console te verlaten, dus elke stap richting browser moest worden uitgezocht vanuit de bytes op de disc.",
        "Underground 2 saiu em 2004. A cidade nunca foi feita para sair do console, então cada passo para levá-la ao navegador teve que ser desvendado a partir dos bytes do disco.",
        "Underground 2 发行于 2004 年。它的城市本来就没打算离开游戏机，所以把它搬进浏览器的每一步，都得从光盘上的字节一点点弄明白。"),

    "Read the disc": (
        "Die Disc auslesen", "Leer el disco", "Leer el disco", "Lire le disque",
        "Leggere il disco", "ディスクを読む", "디스크 읽기", "De disc uitlezen", "Ler o disco",
        "读取光盘"),

    "The disc image is only ever read, never changed. Its files sit inside packed archives, indexed by hashed names. Rebuilding the hash function recovered the names of 1,381 of its 1,392 files.": (
        "Das Disc-Image wird nur gelesen, nie verändert. Die Dateien liegen in gepackten Archiven, indiziert über gehashte Namen. Durch den Nachbau der Hashfunktion kamen die Namen von 1.381 der 1.392 Dateien zurück.",
        "La imagen del disco solo se lee, nunca se modifica. Sus archivos están dentro de contenedores empaquetados, indexados por nombres convertidos en hash. Al reconstruir la función hash se recuperaron los nombres de 1.381 de sus 1.392 archivos.",
        "La imagen del disco solo se lee, nunca se modifica. Sus archivos están dentro de contenedores empaquetados, indexados por nombres convertidos en hash. Al reconstruir la función hash se recuperaron los nombres de 1,381 de sus 1,392 archivos.",
        f"L'image disque est seulement lue, jamais modifiée. Ses fichiers sont rangés dans des archives compactées, indexées par des noms hachés. Reconstruire la fonction de hachage a permis de retrouver les noms de 1{NB}381 de ses 1{NB}392 fichiers.",
        "L'immagine del disco viene solo letta, mai modificata. I suoi file stanno dentro archivi impacchettati, indicizzati per nomi sottoposti a hash. Ricostruire la funzione di hash ha permesso di recuperare i nomi di 1.381 dei suoi 1.392 file.",
        "ディスクイメージは読むだけで、一切変更しません。ファイルはパックされたアーカイブの中にあり、ハッシュ化された名前でインデックスされています。ハッシュ関数を再構築したことで、1,392 個のファイルのうち 1,381 個の名前を復元できました。",
        "디스크 이미지는 읽기만 하고 절대 수정하지 않아요. 파일들은 패킹된 아카이브 안에 해시된 이름으로 인덱싱되어 있어요. 해시 함수를 재구현해서 1,392개 파일 중 1,381개의 이름을 복구했어요.",
        "Het disc-image wordt alleen gelezen, nooit aangepast. De bestanden zitten in gepackte archieven, geïndexeerd op gehashte namen. Door de hashfunctie na te bouwen kwamen de namen van 1.381 van de 1.392 bestanden terug.",
        "A imagem do disco só é lida, nunca alterada. Os arquivos ficam dentro de pacotes compactados, indexados por nomes com hash. Reconstruir a função de hash recuperou os nomes de 1.381 dos 1.392 arquivos.",
        "光盘镜像只读取，从不修改。里面的文件放在打包的归档中，以哈希后的文件名建立索引。重建哈希函数之后，1,392 个文件中有 1,381 个找回了名字。"),

    "ZDIR index · 24-byte records · h = 33 × h + c": (
        "ZDIR-Index · 24-Byte-Einträge · h = 33 × h + c",
        "Índice ZDIR · registros de 24 bytes · h = 33 × h + c",
        "Índice ZDIR · registros de 24 bytes · h = 33 × h + c",
        "Index ZDIR · enregistrements de 24 octets · h = 33 × h + c",
        "Indice ZDIR · record da 24 byte · h = 33 × h + c",
        "ZDIR インデックス · 24 バイトのレコード · h = 33 × h + c",
        "ZDIR 인덱스 · 24바이트 레코드 · h = 33 × h + c",
        "ZDIR-index · records van 24 bytes · h = 33 × h + c",
        "Índice ZDIR · registros de 24 bytes · h = 33 × h + c",
        "ZDIR 索引 · 24 字节记录 · h = 33 × h + c"),

    "Decode the geometry": (
        "Die Geometrie dekodieren", "Decodificar la geometría", "Decodificar la geometría",
        "Décoder la géométrie", "Decodificare la geometria", "ジオメトリをデコードする",
        "지오메트리 디코딩", "De geometrie decoderen", "Decodificar a geometria", "解码几何数据"),

    "EA stored its models as PlayStation 2 vector unit packets with compressed positions. Where a triangle strip breaks is decided by the vector unit's random number generator, so that generator was rebuilt too. It matches all 140,493 strips it was checked against.": (
        "EA hat die Modelle als Pakete für die Vector Units der PlayStation 2 gespeichert, mit komprimierten Positionen. Wo ein Triangle Strip abbricht, entscheidet der Zufallszahlengenerator der Vector Unit, also wurde auch dieser Generator nachgebaut. Er stimmt bei allen 140.493 Strips überein, gegen die er geprüft wurde.",
        "EA guardó sus modelos como paquetes para las unidades vectoriales (VU) de la PlayStation 2, con posiciones comprimidas. Dónde se corta una tira de triángulos lo decide el generador de números aleatorios de la unidad vectorial, así que ese generador también se reconstruyó. Coincide en las 140.493 tiras con las que se comprobó.",
        "EA guardó sus modelos como paquetes para las unidades vectoriales (VU) del PlayStation 2, con posiciones comprimidas. Dónde se corta una tira de triángulos lo decide el generador de números aleatorios de la unidad vectorial, así que ese generador también se reconstruyó. Coincide en las 140,493 tiras con las que se comprobó.",
        f"EA stockait ses modèles sous forme de paquets pour les unités vectorielles (VU) de la PlayStation 2, avec des positions compressées. L'endroit où une bande de triangles (triangle strip) s'interrompt est décidé par le générateur de nombres aléatoires de l'unité vectorielle : ce générateur a donc lui aussi été reconstruit. Il concorde sur les 140{NB}493 bandes sur lesquelles il a été vérifié.",
        "EA salvava i suoi modelli come pacchetti per le vector unit della PlayStation 2, con posizioni compresse. Il punto in cui una triangle strip si interrompe lo decide il generatore di numeri casuali della vector unit, quindi è stato ricostruito anche quel generatore. Corrisponde su tutte le 140.493 strip su cui è stato verificato.",
        "EA はモデルを、座標を圧縮した PlayStation 2 のベクターユニット用パケットとして格納していました。トライアングルストリップがどこで切れるかはベクターユニットの乱数生成器が決めているので、その乱数生成器も再現しました。検証した 140,493 本のストリップすべてで一致しています。",
        "EA는 모델을 위치값을 압축한 PlayStation 2 벡터 유닛 패킷으로 저장했어요. 트라이앵글 스트립이 어디서 끊기는지는 벡터 유닛의 난수 생성기가 정하기 때문에, 그 생성기도 재구현했어요. 검증한 140,493개 스트립 전부와 일치해요.",
        "EA sloeg de modellen op als vector unit-pakketten voor de PlayStation 2, met gecomprimeerde posities. Waar een triangle strip breekt, wordt bepaald door de random number generator van de vector unit, dus ook die generator is nagebouwd. Hij klopt bij alle 140.493 strips waartegen hij is getest.",
        "A EA guardava os modelos como pacotes para as unidades vetoriais (VU) do PlayStation 2, com posições comprimidas. Onde uma triangle strip se quebra é decidido pelo gerador de números aleatórios da unidade vetorial, então esse gerador também foi reconstruído. Ele bate com todas as 140.493 strips em que foi testado.",
        "EA 把模型存成 PlayStation 2 向量单元（VU）的数据包，顶点位置经过压缩。三角形条带在哪里断开，是由向量单元的随机数生成器决定的，所以连这个生成器也一起重建了。在检验过的全部 140,493 条条带上，结果都一致。"),

    "VIF packets · VU1 random number generator · 140,493 strips": (
        "VIF-Pakete · VU1-Zufallszahlengenerator · 140.493 Strips",
        "Paquetes VIF · generador de números aleatorios de la VU1 · 140.493 tiras",
        "Paquetes VIF · generador de números aleatorios de la VU1 · 140,493 tiras",
        f"Paquets VIF · générateur de nombres aléatoires de la VU1 · 140{NB}493 bandes",
        "Pacchetti VIF · generatore di numeri casuali della VU1 · 140.493 strip",
        "VIF パケット · VU1 乱数生成器 · 140,493 ストリップ",
        "VIF 패킷 · VU1 난수 생성기 · 스트립 140,493개",
        "VIF-pakketten · VU1-random number generator · 140.493 strips",
        "Pacotes VIF · gerador de números aleatórios da VU1 · 140.493 strips",
        "VIF 数据包 · VU1 随机数生成器 · 140,493 条条带"),

    "Rebuild the city": (
        "Die Stadt neu aufbauen", "Reconstruir la ciudad", "Reconstruir la ciudad",
        "Reconstruire la ville", "Ricostruire la città", "街を組み直す", "도시 재구성",
        "De stad herbouwen", "Reconstruir a cidade", "重建城市"),

    "Scenery placement records, texture archives and palettes were decoded and turned into web-ready models. The city streams in around you, cell by cell, so it runs on a phone.": (
        "Platzierungsdaten der Umgebung, Texturarchive und Paletten wurden dekodiert und in webtaugliche Modelle umgewandelt. Die Stadt wird Zelle für Zelle um dich herum gestreamt, deshalb läuft sie auch auf dem Handy.",
        "Se decodificaron los registros de colocación del escenario, los contenedores de texturas y las paletas, y se convirtieron en modelos listos para la web. La ciudad se carga por streaming a tu alrededor, celda a celda, así que funciona en un móvil.",
        "Se decodificaron los registros de colocación del escenario, los contenedores de texturas y las paletas, y se convirtieron en modelos listos para la web. La ciudad se carga por streaming a tu alrededor, celda por celda, así que funciona en un celular.",
        "Les données de placement du décor, les archives de textures et les palettes ont été décodées et transformées en modèles prêts pour le web. La ville se charge en streaming autour de toi, cellule par cellule : elle tourne donc sur un téléphone.",
        "I dati di posizionamento dello scenario, gli archivi delle texture e le palette sono stati decodificati e trasformati in modelli pronti per il web. La città viene caricata in streaming intorno a te, cella dopo cella, così gira anche su un telefono.",
        "背景オブジェクトの配置レコード、テクスチャアーカイブ、パレットをデコードして、Web で使えるモデルに変換しました。街はあなたの周りにセル単位でストリーミングされるので、スマホでも動きます。",
        "배경 오브젝트 배치 레코드, 텍스처 아카이브, 팔레트를 디코딩해서 웹용 모델로 바꿨어요. 도시는 내 주변에 셀 단위로 스트리밍되기 때문에 폰에서도 돌아가요.",
        "Plaatsingsrecords van de omgeving, textuurarchieven en paletten zijn gedecodeerd en omgezet in webklare modellen. De stad streamt cel voor cel om je heen in, dus hij draait ook op een telefoon.",
        "Registros de posicionamento do cenário, pacotes de texturas e paletas foram decodificados e transformados em modelos prontos para a web. A cidade é carregada por streaming ao seu redor, célula por célula, então roda até no celular.",
        "场景摆放记录、贴图归档和调色板都被解码，并转成了适合网页的模型。城市会围绕你一格一格地流式加载，所以手机上也能跑。"),

    "TPK textures · 4 and 8-bit palettes · streamed cells": (
        "TPK-Texturen · 4- und 8-Bit-Paletten · gestreamte Zellen",
        "Texturas TPK · paletas de 4 y 8 bits · celdas en streaming",
        "Texturas TPK · paletas de 4 y 8 bits · celdas en streaming",
        "Textures TPK · palettes 4 et 8 bits · cellules en streaming",
        "Texture TPK · palette a 4 e 8 bit · celle in streaming",
        "TPK テクスチャ · 4/8 ビットパレット · ストリーミングセル",
        "TPK 텍스처 · 4비트·8비트 팔레트 · 스트리밍 셀",
        "TPK-texturen · 4- en 8-bits paletten · gestreamde cellen",
        "Texturas TPK · paletas de 4 e 8 bits · células em streaming",
        "TPK 贴图 · 4 位和 8 位调色板 · 流式加载的格子"),

    "Restore the garage": (
        "Die Garage wiederherstellen", "Restaurar el garaje", "Restaurar el garaje",
        "Restaurer le garage", "Ripristinare il garage", "ガレージを復元する", "차고 복원",
        "De garage herstellen", "Restaurar a garagem", "还原车库"),

    "The 29 player cars come with their body kits, paint, vinyls and wheels. The original garage, the menu icons, the font and the custom gauges are the game's own, decoded and used as they are.": (
        "Die 29 spielbaren Autos kommen mit ihren Bodykits, Lackierungen, Vinyls und Felgen. Die Original-Garage, die Menüsymbole, die Schrift und die eigens gestalteten Anzeigen stammen aus dem Spiel selbst, dekodiert und unverändert verwendet.",
        "Los 29 coches jugables vienen con sus kits de carrocería, pintura, vinilos y llantas. El garaje original, los iconos del menú, la tipografía y los indicadores personalizados son los del propio juego, decodificados y usados tal cual.",
        "Los 29 carros jugables vienen con sus kits de carrocería, pintura, viniles y rines. El garaje original, los íconos del menú, la tipografía y los indicadores personalizados son los del propio juego, decodificados y usados tal cual.",
        "Les 29 voitures jouables arrivent avec leurs kits carrosserie, peintures, vinyles et jantes. Le garage d'origine, les icônes des menus, la police et les compteurs personnalisés sont ceux du jeu, décodés et utilisés tels quels.",
        "Le 29 auto giocabili arrivano con i loro body kit, vernici, vinili e cerchi. Il garage originale, le icone del menu, il font e gli strumenti personalizzati sono quelli del gioco, decodificati e usati così come sono.",
        "プレイヤーが乗れる 29 台には、エアロパーツ、塗装、バイナル、ホイールも揃っています。オリジナルのガレージ、メニューアイコン、フォント、専用メーターはすべてゲームそのもの。デコードして、そのまま使っています。",
        "플레이어용 차 29대는 바디킷, 도색, 비닐, 휠까지 그대로 들어 있어요. 오리지널 차고, 메뉴 아이콘, 폰트, 전용 계기판은 모두 게임의 것을 디코딩해서 그대로 썼어요.",
        "De 29 speelbare auto's komen met hun bodykits, lak, vinyls en velgen. De originele garage, de menu-iconen, het lettertype en de eigen meters zijn die van de game zelf, gedecodeerd en ongewijzigd gebruikt.",
        "Os 29 carros jogáveis vêm com seus body kits, pinturas, vinis e rodas. A garagem original, os ícones do menu, a fonte e os medidores personalizados são do próprio jogo, decodificados e usados do jeito que são.",
        "29 辆可玩车辆都带着各自的车身套件、喷漆、拉花和轮毂。原版车库、菜单图标、字体和定制仪表都是游戏自己的，解码后原样使用。"),

    "29 cars · original garage · 496 menu textures · 7 fonts": (
        "29 Autos · Original-Garage · 496 Menütexturen · 7 Schriften",
        "29 coches · garaje original · 496 texturas de menú · 7 fuentes",
        "29 carros · garaje original · 496 texturas de menú · 7 fuentes",
        "29 voitures · garage d'origine · 496 textures de menu · 7 polices",
        "29 auto · garage originale · 496 texture di menu · 7 font",
        "29 台 · オリジナルガレージ · メニューテクスチャ 496 枚 · フォント 7 種",
        "차 29대 · 오리지널 차고 · 메뉴 텍스처 496개 · 폰트 7종",
        "29 auto's · originele garage · 496 menutexturen · 7 lettertypen",
        "29 carros · garagem original · 496 texturas de menu · 7 fontes",
        "29 辆车 · 原版车库 · 496 张菜单贴图 · 7 种字体"),

    "Recover the sound": (
        "Den Sound zurückholen", "Recuperar el sonido", "Recuperar el sonido",
        "Récupérer le son", "Recuperare il suono", "サウンドを取り戻す", "사운드 복구",
        "Het geluid terughalen", "Recuperar o som", "找回声音"),

    "Engine sounds are decoded from the game's own recordings, one grain per engine cycle, and played through each car's rev range.": (
        "Die Motorsounds werden aus den Originalaufnahmen des Spiels dekodiert, ein Grain pro Motorzyklus, und über das gesamte Drehzahlband jedes Autos abgespielt.",
        "Los sonidos del motor se decodifican de las grabaciones del propio juego, un grain por ciclo de motor, y se reproducen a lo largo del rango de revoluciones de cada coche.",
        "Los sonidos del motor se decodifican de las grabaciones del propio juego, un grain por ciclo de motor, y se reproducen a lo largo del rango de revoluciones de cada carro.",
        "Les sons moteur sont décodés à partir des enregistrements du jeu, un grain par cycle moteur, et joués sur toute la plage de régime de chaque voiture.",
        "I suoni dei motori sono decodificati dalle registrazioni originali del gioco, un grain per ciclo motore, e riprodotti lungo tutto l'arco di giri di ogni auto.",
        "エンジン音はゲーム自身の録音からデコードしたもの。エンジン 1 サイクルにつき 1 グレインで、各車の回転域に合わせて鳴らしています。",
        "엔진 사운드는 게임에 들어 있는 녹음에서 디코딩했어요. 엔진 한 사이클당 그레인 하나씩, 차마다의 회전 영역에 맞춰 재생해요.",
        "Motorgeluiden worden gedecodeerd uit de eigen opnames van de game, één grain per motorcyclus, en afgespeeld over het toerenbereik van elke auto.",
        "Os sons de motor são decodificados das gravações do próprio jogo, um grain por ciclo do motor, e tocados ao longo da faixa de giro de cada carro.",
        "引擎声是从游戏自带的录音里解码出来的，每个发动机循环一个颗粒（grain），并按每辆车的转速范围播放。"),

    "Engine sweeps · idle loops · torque curves": (
        "Drehzahl-Sweeps · Leerlauf-Loops · Drehmomentkurven",
        "Barridos de motor · loops de ralentí · curvas de par",
        "Barridos de motor · loops de marcha mínima · curvas de torque",
        "Balayages moteur · boucles de ralenti · courbes de couple",
        "Sweep del motore · loop del minimo · curve di coppia",
        "エンジンスイープ · アイドルループ · トルクカーブ",
        "엔진 스윕 · 아이들 루프 · 토크 커브",
        "Motorsweeps · stationair-loops · koppelkrommes",
        "Varreduras de motor · loops de marcha lenta · curvas de torque",
        "引擎扫频 · 怠速循环 · 扭矩曲线"),

    "Add the people": (
        "Die Leute dazuholen", "Añadir a la gente", "Agregar a la gente", "Ajouter les gens",
        "Aggiungere le persone", "人を呼び込む", "사람 더하기", "De mensen toevoegen",
        "Adicionar as pessoas", "加入玩家"),

    "None of the social side is on the disc. The walking characters, emotes, phone camera, chat, proximity voice and name plates are new. One server holds up to 2,000 players in the same city, and each player is only sent the people near them.": (
        "Nichts vom sozialen Teil ist auf der Disc. Die laufenden Figuren, Emotes, Handykamera, Chat, Proximity-Voice-Chat und Namensschilder sind neu. Ein Server fasst bis zu 2.000 Spieler in derselben Stadt, und jeder Spieler bekommt nur die Leute in seiner Nähe übertragen.",
        "Nada de la parte social está en el disco. Los personajes que caminan, los gestos, la cámara del móvil, el chat, la voz de proximidad y las etiquetas de nombre son nuevos. Un servidor aguanta hasta 2.000 jugadores en la misma ciudad, y a cada jugador solo se le envía la gente que tiene cerca.",
        "Nada de la parte social está en el disco. Los personajes que caminan, los emotes, la cámara del celular, el chat, la voz de proximidad y las etiquetas de nombre son nuevos. Un servidor aguanta hasta 2,000 jugadores en la misma ciudad, y a cada jugador solo se le envía la gente que tiene cerca.",
        f"Rien de la partie sociale n'est sur le disque. Les personnages qui marchent, les emotes, l'appareil photo du téléphone, le chat, le vocal de proximité et les pseudos sont nouveaux. Un serveur accueille jusqu'à 2{NB}000 joueurs dans la même ville, et chaque joueur ne reçoit que les gens proches de lui.",
        "Niente della parte social è sul disco. I personaggi che camminano, le emote, la fotocamera del telefono, la chat, la voce di prossimità e le targhette con i nomi sono nuovi. Un server regge fino a 2.000 giocatori nella stessa città, e a ogni giocatore vengono inviate solo le persone vicine.",
        "ソーシャルな要素はどれもディスクには入っていません。歩くキャラクター、エモート、スマホのカメラ、チャット、近接ボイス、ネームプレートは新しく作ったもの。1 台のサーバーに同じ街で最大 2,000 人が入れて、各プレイヤーには近くにいる人のデータだけが送られます。",
        "소셜 요소는 디스크에 하나도 없어요. 걸어 다니는 캐릭터, 이모트, 폰 카메라, 채팅, 근거리 보이스, 네임 플레이트는 새로 만들었어요. 서버 하나에 같은 도시에서 최대 2,000명이 들어갈 수 있고, 각 플레이어에게는 근처에 있는 사람들만 전송돼요.",
        "Niets van het sociale deel staat op de disc. De lopende personages, emotes, telefooncamera, chat, proximity voice en naambordjes zijn nieuw. Eén server biedt plaats aan maximaal 2.000 spelers in dezelfde stad, en elke speler krijgt alleen de mensen in zijn buurt doorgestuurd.",
        "Nada da parte social está no disco. Os personagens que andam, os emotes, a câmera do celular, o chat, a voz de proximidade e as plaquinhas de nome são novos. Um servidor aguenta até 2.000 jogadores na mesma cidade, e cada jogador só recebe as pessoas perto dele.",
        "社交部分光盘里一样都没有。能走动的角色、表情动作、手机相机、聊天、近距离语音和名牌都是新做的。一台服务器最多容纳 2,000 名玩家在同一座城市里，每个玩家只会收到自己附近的人的数据。"),

    "WebSockets · WebRTC voice · 2,000 players per server": (
        "WebSockets · WebRTC-Voice · 2.000 Spieler pro Server",
        "WebSockets · voz por WebRTC · 2.000 jugadores por servidor",
        "WebSockets · voz por WebRTC · 2,000 jugadores por servidor",
        f"WebSockets · vocal WebRTC · 2{NB}000 joueurs par serveur",
        "WebSockets · voce WebRTC · 2.000 giocatori per server",
        "WebSockets · WebRTC ボイス · 1 サーバー 2,000 人",
        "WebSockets · WebRTC 보이스 · 서버당 2,000명",
        "WebSockets · WebRTC-voice · 2.000 spelers per server",
        "WebSockets · voz via WebRTC · 2.000 jogadores por servidor",
        "WebSockets · WebRTC 语音 · 每台服务器 2,000 名玩家"),

    "Carmeet started as a way to walk around the city in a Quest headset and take photographs. The driving came next, and then other people.": (
        "Carmeet begann als Möglichkeit, mit einem Quest-Headset durch die Stadt zu laufen und Fotos zu machen. Dann kam das Fahren dazu, und danach andere Leute.",
        "Carmeet empezó como una forma de pasear por la ciudad con un visor Quest y hacer fotos. Luego llegó la conducción, y después, más gente.",
        "Carmeet empezó como una forma de pasear por la ciudad con un visor Quest y tomar fotos. Luego llegó el manejo, y después, más gente.",
        "Carmeet a commencé comme un moyen de se promener dans la ville avec un casque Quest et de prendre des photos. La conduite est venue ensuite, puis les autres.",
        "Carmeet è nato come un modo per girare a piedi per la città con un visore Quest e scattare foto. Poi è arrivata la guida, e poi le altre persone.",
        "Carmeet は、Quest のヘッドセットで街を歩き回って写真を撮るためのものとして始まりました。次に運転が加わり、それから他の人たちがやってきました。",
        "Carmeet은 Quest 헤드셋을 쓰고 도시를 걸어 다니며 사진을 찍으려고 시작됐어요. 그다음에 운전이 들어왔고, 그다음엔 다른 사람들이 왔어요.",
        "Carmeet begon als een manier om met een Quest-headset door de stad te lopen en foto's te maken. Daarna kwam het rijden, en toen andere mensen.",
        "Carmeet começou como um jeito de andar pela cidade com um headset Quest e tirar fotos. Depois veio a direção, e então outras pessoas.",
        "Carmeet 最初只是为了戴着 Quest 头显在城里走走、拍拍照。后来加上了开车，再后来，有了其他人。"),

    # ------------------------------------------------------------------ play

    "Open the link, build your car and drive. There is nothing to install. The server asks for an email the first time you join, and other players never see it.": (
        "Link öffnen, Auto aufbauen, losfahren. Es gibt nichts zu installieren. Beim ersten Beitritt fragt der Server nach einer E-Mail-Adresse, und andere Spieler sehen sie nie.",
        "Abre el enlace, tunea tu coche y conduce. No hay nada que instalar. La primera vez que entras, el servidor te pide un correo, y los demás jugadores nunca lo ven.",
        "Abre el link, arma tu carro y maneja. No hay nada que instalar. La primera vez que entras, el servidor te pide un correo, y los demás jugadores nunca lo ven.",
        "Ouvre le lien, prépare ta voiture et roule. Il n'y a rien à installer. Le serveur te demande un e-mail la première fois que tu te connectes, et les autres joueurs ne le voient jamais.",
        "Apri il link, elabora la tua auto e guida. Non c'è niente da installare. La prima volta che entri il server ti chiede un'email, e gli altri giocatori non la vedono mai.",
        "リンクを開いて、車を組んで、走り出そう。インストールは不要です。初めて参加するときにサーバーがメールアドレスを聞きますが、他のプレイヤーに見られることはありません。",
        "링크를 열고, 차를 튜닝하고, 달리면 돼요. 설치할 건 없어요. 처음 접속할 때 서버가 이메일을 물어보지만, 다른 플레이어에게는 절대 보이지 않아요.",
        "Open de link, bouw je auto en rijden maar. Er valt niets te installeren. De server vraagt de eerste keer dat je meedoet om een e-mailadres, en andere spelers zien het nooit.",
        "Abra o link, monte seu carro e dirija. Não tem nada para instalar. O servidor pede um e-mail na primeira vez que você entra, e os outros jogadores nunca veem.",
        "打开链接，改好车，开就完了。无需安装任何东西。第一次加入时服务器会要一个邮箱地址，其他玩家永远看不到。"),

    "Keyboard": (
        "Tastatur", "Teclado", "Teclado", "Clavier", "Tastiera", "キーボード", "키보드",
        "Toetsenbord", "Teclado", "键盘"),

    "drive": (
        "fahren", "conducir", "manejar", "conduire", "guidare", "運転", "운전", "rijden",
        "dirigir", "驾驶"),

    # The name printed on the key, not a word to explain it.
    "Space": (
        "Leertaste", "Espacio", "Espacio", "Espace", "Spazio", "スペース", "스페이스", "Spatie",
        "Espaço", "空格"),

    "handbrake": (
        "Handbremse", "freno de mano", "freno de mano", "frein à main", "freno a mano",
        "サイドブレーキ", "사이드 브레이크", "handrem", "freio de mão", "手刹"),

    "get out": (
        "aussteigen", "bajarse", "bajarse", "descendre", "scendere", "降りる", "내리기",
        "uitstappen", "descer", "下车"),

    "garage": (
        "Garage", "garaje", "garaje", "garage", "garage", "ガレージ", "차고", "garage", "garagem",
        "车库"),

    "phone": (
        "Handy", "móvil", "celular", "téléphone", "telefono", "スマホ", "폰", "telefoon",
        "celular", "手机"),

    "chat": (
        "Chat", "chat", "chat", "chat", "chat", "チャット", "채팅", "chat", "chat", "聊天"),

    "Gamepad": (
        "Gamepad", "Mando", "Control", "Manette", "Controller", "ゲームパッド", "게임패드",
        "Gamepad", "Controle", "手柄"),

    "Left stick steers or walks. Triggers are gas and brake. B gets out and back in.": (
        "Linker Stick lenkt oder läuft. Die Trigger sind Gas und Bremse. B zum Aus- und wieder Einsteigen.",
        "El stick izquierdo dirige o camina. Los gatillos son acelerador y freno. B para bajarte y volver a subir.",
        "El stick izquierdo dirige o camina. Los gatillos son acelerador y freno. B para bajarte y volver a subir.",
        "Le stick gauche dirige ou fait marcher. Les gâchettes, c'est l'accélérateur et le frein. B pour descendre et remonter.",
        "La levetta sinistra sterza o cammina. I grilletti sono gas e freno. B per scendere e risalire.",
        "左スティックでハンドル操作・歩行。トリガーがアクセルとブレーキ。B で乗り降り。",
        "왼쪽 스틱으로 조향하거나 걸어요. 트리거는 액셀과 브레이크. B로 내리고 다시 타요.",
        "Linkerstick stuurt of loopt. De triggers zijn gas en rem. B om uit en weer in te stappen.",
        "O analógico esquerdo vira ou anda. Os gatilhos são acelerador e freio. B para descer e entrar de novo.",
        "左摇杆转向或走路。扳机键是油门和刹车。按 B 下车、再上车。"),

    "Touch": (
        "Touch", "Táctil", "Táctil", "Tactile", "Touch", "タッチ", "터치", "Touch", "Toque",
        "触屏"),

    "A steering pad and pedals on screen, in portrait or landscape. The pad walks you when you are out of the car.": (
        "Ein Lenkpad und Pedale auf dem Bildschirm, im Hoch- oder Querformat. Wenn du ausgestiegen bist, läufst du mit dem Pad.",
        "Un pad de dirección y pedales en pantalla, en vertical u horizontal. Cuando estás fuera del coche, el pad te hace caminar.",
        "Un pad de dirección y pedales en pantalla, en vertical u horizontal. Cuando estás fuera del carro, el pad te hace caminar.",
        "Un pad de direction et des pédales à l'écran, en portrait ou en paysage. Quand tu es hors de la voiture, le pad te fait marcher.",
        "Un pad di sterzo e i pedali sullo schermo, in verticale o in orizzontale. Quando sei fuori dall'auto, il pad ti fa camminare.",
        "画面上にステアリングパッドとペダル。縦画面でも横画面でも OK。車を降りているときは、パッドで歩けます。",
        "화면에 조향 패드와 페달이 나와요. 세로든 가로든 돼요. 차에서 내렸을 때는 패드로 걸어요.",
        "Een stuurpad en pedalen op het scherm, staand of liggend. Ben je uitgestapt, dan loop je met het pad.",
        "Um pad de direção e pedais na tela, na vertical ou na horizontal. Fora do carro, o pad faz você andar.",
        "屏幕上有方向盘触控板和踏板，竖屏横屏都行。下车后，用触控板走路。"),

    "Carmeet on a phone, driving with the touch controls": (
        "Carmeet auf einem Handy, gefahren mit der Touch-Steuerung",
        "Carmeet en un móvil, conduciendo con los controles táctiles",
        "Carmeet en un celular, manejando con los controles táctiles",
        "Carmeet sur un téléphone, en conduite avec les commandes tactiles",
        "Carmeet su un telefono, alla guida con i controlli touch",
        "スマホで Carmeet。タッチ操作で運転中",
        "폰에서 터치 조작으로 운전 중인 Carmeet",
        "Carmeet op een telefoon, rijden met de touchbediening",
        "Carmeet no celular, dirigindo com os controles de toque",
        "手机上的 Carmeet，正用触屏操作驾驶"),

    "It works on phones too. Touch controls appear by themselves, and a friend on the same link shows up on your street.": (
        "Läuft auch auf dem Handy. Die Touch-Steuerung erscheint von selbst, und ein Freund mit demselben Link taucht in deiner Straße auf.",
        "También funciona en móviles. Los controles táctiles aparecen solos, y un amigo con el mismo enlace aparece en tu calle.",
        "También funciona en celulares. Los controles táctiles aparecen solos, y un amigo con el mismo link aparece en tu calle.",
        "Ça marche aussi sur téléphone. Les commandes tactiles apparaissent toutes seules, et un pote sur le même lien débarque dans ta rue.",
        "Funziona anche sui telefoni. I controlli touch compaiono da soli, e un amico con lo stesso link spunta nella tua strada.",
        "スマホでも遊べます。タッチ操作は自動で表示されて、同じリンクを開いた友だちがあなたの通りに現れます。",
        "폰에서도 돼요. 터치 조작은 알아서 나타나고, 같은 링크로 들어온 친구가 내 거리에 나타나요.",
        "Het werkt ook op telefoons. De touchbediening verschijnt vanzelf, en een vriend met dezelfde link duikt op in jouw straat.",
        "Funciona no celular também. Os controles de toque aparecem sozinhos, e um amigo com o mesmo link aparece na sua rua.",
        "手机上也能玩。触屏操作会自动出现，用同一个链接进来的朋友会出现在你的街上。"),

    # ------------------------------------------------------------------ questions

    "Questions": (
        "Fragen", "Preguntas", "Preguntas", "Questions", "Domande", "よくある質問",
        "자주 묻는 질문", "Vragen", "Perguntas", "常见问题"),

    "Is Carmeet free?": (
        "Ist Carmeet kostenlos?", "¿Carmeet es gratis?", "¿Carmeet es gratis?",
        "Carmeet est gratuit ?", "Carmeet è gratis?", "Carmeet は無料ですか？",
        "Carmeet은 무료인가요?", "Is Carmeet gratis?", "O Carmeet é grátis?", "Carmeet 免费吗？"),

    "Yes. It runs in the browser and costs nothing to play. There is nothing to download or install.": (
        "Ja. Es läuft im Browser und kostet nichts. Es gibt nichts herunterzuladen oder zu installieren.",
        "Sí. Funciona en el navegador y jugar no cuesta nada. No hay nada que descargar ni instalar.",
        "Sí. Funciona en el navegador y jugar no cuesta nada. No hay nada que descargar ni instalar.",
        "Oui. Il tourne dans le navigateur et y jouer ne coûte rien. Il n'y a rien à télécharger ni à installer.",
        "Sì. Gira nel browser e giocare non costa nulla. Non c'è niente da scaricare o installare.",
        "はい。ブラウザで動いて、プレイは無料。ダウンロードもインストールも必要ありません。",
        "네. 브라우저에서 돌아가고 플레이는 무료예요. 다운로드하거나 설치할 것도 없어요.",
        "Ja. Het draait in de browser en spelen kost niets. Er valt niets te downloaden of te installeren.",
        "Sim. Roda no navegador e não custa nada para jogar. Não tem nada para baixar nem instalar.",
        "是的。它在浏览器里运行，玩不花一分钱。不用下载，也不用安装。"),

    "Does it work on a phone?": (
        "Läuft es auf dem Handy?", "¿Funciona en el móvil?", "¿Funciona en el celular?",
        "Ça marche sur téléphone ?", "Funziona sul telefono?", "スマホでも遊べますか？",
        "폰에서도 되나요?", "Werkt het op een telefoon?", "Funciona no celular?",
        "手机上能玩吗？"),

    "Yes. Touch controls appear on phones and tablets, in portrait or landscape. Keyboards and gamepads work on a computer.": (
        "Ja. Auf Handys und Tablets erscheint eine Touch-Steuerung, im Hoch- oder Querformat. Am Computer funktionieren Tastatur und Gamepad.",
        "Sí. En móviles y tabletas aparecen controles táctiles, en vertical u horizontal. En el ordenador funcionan el teclado y el mando.",
        "Sí. En celulares y tablets aparecen controles táctiles, en vertical u horizontal. En la computadora funcionan el teclado y el control.",
        "Oui. Des commandes tactiles apparaissent sur téléphone et tablette, en portrait ou en paysage. Sur ordinateur, clavier et manette fonctionnent.",
        "Sì. Su telefoni e tablet compaiono i controlli touch, in verticale o in orizzontale. Sul computer funzionano tastiera e controller.",
        "はい。スマホやタブレットではタッチ操作が表示されます。縦でも横でも OK。パソコンではキーボードとゲームパッドが使えます。",
        "네. 폰과 태블릿에서는 세로든 가로든 터치 조작이 나타나요. 컴퓨터에서는 키보드와 게임패드를 쓸 수 있어요.",
        "Ja. Op telefoons en tablets verschijnt touchbediening, staand of liggend. Op een computer werken toetsenbord en gamepad.",
        "Sim. Em celulares e tablets aparecem controles de toque, na vertical ou na horizontal. No computador, teclado e controle funcionam.",
        "能。在手机和平板上会出现触屏操作，竖屏横屏都行。在电脑上可以用键盘和手柄。"),

    "Can you race?": (
        "Kann man Rennen fahren?", "¿Se pueden echar carreras?", "¿Se pueden echar carreras?",
        "On peut faire la course ?", "Si può gareggiare?", "レースはできますか？",
        "레이스할 수 있나요?", "Kun je racen?", "Dá para apostar corrida?", "能比赛吗？"),

    "There are no races. Carmeet is about building a car, cruising and meeting up.": (
        "Es gibt keine Rennen. Bei Carmeet geht es ums Aufbauen, Cruisen und Treffen.",
        "No hay carreras. Carmeet va de tunear un coche, salir a rodar y quedar.",
        "No hay carreras. Carmeet se trata de armar un carro, salir a rodar y juntarse.",
        "Il n'y a pas de courses. Carmeet, c'est préparer une voiture, se balader et se retrouver.",
        "Non ci sono gare. Carmeet è fatto per elaborare un'auto, girare e ritrovarsi.",
        "レースはありません。Carmeet は、車を組んで、流して、集まるためのものです。",
        "레이스는 없어요. Carmeet은 차를 튜닝하고, 달리고, 모이는 곳이에요.",
        "Er zijn geen races. Bij Carmeet draait het om een auto bouwen, toeren en samenkomen.",
        "Não tem corrida. Carmeet é sobre montar um carro, dar um rolê e se encontrar.",
        "没有比赛。Carmeet 就是改车、兜风、聚会。"),

    "Why does it ask for an email?": (
        "Warum wird nach einer E-Mail-Adresse gefragt?", "¿Por qué pide un correo?",
        "¿Por qué pide un correo?", "Pourquoi il demande un e-mail ?", "Perché chiede un'email?",
        "なぜメールアドレスが必要なんですか？", "왜 이메일을 물어보나요?",
        "Waarom vraagt het om een e-mailadres?", "Por que pede um e-mail?", "为什么要填邮箱？"),

    "The public server asks for an email once, before you join. It stays with the host, and other players never see it.": (
        "Der öffentliche Server fragt einmal nach einer E-Mail-Adresse, bevor du beitrittst. Sie bleibt beim Betreiber, und andere Spieler sehen sie nie.",
        "El servidor público pide un correo una sola vez, antes de entrar. Se queda con quien aloja el servidor, y los demás jugadores nunca lo ven.",
        "El servidor público pide un correo una sola vez, antes de entrar. Se queda con quien aloja el servidor, y los demás jugadores nunca lo ven.",
        "Le serveur public demande un e-mail une seule fois, avant que tu te connectes. Il reste chez l'hébergeur, et les autres joueurs ne le voient jamais.",
        "Il server pubblico chiede un'email una volta sola, prima di entrare. Resta a chi gestisce il server, e gli altri giocatori non la vedono mai.",
        "公開サーバーでは、参加する前に一度だけメールアドレスを聞かれます。アドレスはホスト側に保管され、他のプレイヤーに見られることはありません。",
        "공개 서버는 접속하기 전에 한 번 이메일을 물어봐요. 이메일은 호스트만 보관하고, 다른 플레이어는 절대 볼 수 없어요.",
        "De openbare server vraagt één keer om een e-mailadres, voordat je meedoet. Het blijft bij de host, en andere spelers zien het nooit.",
        "O servidor público pede um e-mail uma vez, antes de você entrar. Ele fica com quem hospeda o servidor, e os outros jogadores nunca veem.",
        "公共服务器会在你加入前要一次邮箱。邮箱只留在主机那边，其他玩家永远看不到。"),

    "Is Carmeet made by EA?": (
        "Ist Carmeet von EA?", "¿Carmeet es de EA?", "¿Carmeet es de EA?",
        "Carmeet est fait par EA ?", "Carmeet è fatto da EA?",
        "Carmeet は EA が作ったものですか？", "Carmeet은 EA가 만들었나요?",
        "Is Carmeet gemaakt door EA?", "O Carmeet é feito pela EA?", "Carmeet 是 EA 做的吗？"),

    # The disclaimer, here and in the footer: three verbs, Electronic Arts named each time.
    "No. Carmeet is an independent fan project by Levi Foster. It is not affiliated with, endorsed or sponsored by Electronic Arts.": (
        "Nein. Carmeet ist ein unabhängiges Fanprojekt von Levi Foster. Es steht in keiner Verbindung zu Electronic Arts und wird von Electronic Arts weder befürwortet noch gesponsert.",
        "No. Carmeet es un proyecto fan independiente de Levi Foster. No está afiliado a Electronic Arts, ni respaldado ni patrocinado por Electronic Arts.",
        "No. Carmeet es un proyecto fan independiente de Levi Foster. No está afiliado a Electronic Arts, ni respaldado ni patrocinado por Electronic Arts.",
        "Non. Carmeet est un projet de fan indépendant de Levi Foster. Il n'est ni affilié à Electronic Arts, ni approuvé ni sponsorisé par Electronic Arts.",
        "No. Carmeet è un fan project indipendente di Levi Foster. Non è affiliato a Electronic Arts, né approvato o sponsorizzato da Electronic Arts.",
        "いいえ。Carmeet は Levi Foster による独立したファンプロジェクトです。Electronic Arts とは提携関係になく、Electronic Arts の承認も後援も受けていません。",
        "아니요. Carmeet은 Levi Foster가 만든 독립 팬 프로젝트예요. Electronic Arts와 제휴 관계가 없으며, Electronic Arts의 승인이나 후원도 받지 않았어요.",
        "Nee. Carmeet is een onafhankelijk fanproject van Levi Foster. Het is niet gelieerd aan, goedgekeurd door of gesponsord door Electronic Arts.",
        "Não. Carmeet é um projeto de fã independente de Levi Foster. Não é afiliado à Electronic Arts, nem endossado ou patrocinado pela Electronic Arts.",
        "不是。Carmeet 是 Levi Foster 的独立粉丝项目，与 Electronic Arts 没有任何关联，也未获得 Electronic Arts 的认可或赞助。"),

    # ------------------------------------------------------------------ end of page

    "Play Carmeet": (
        "Carmeet spielen", "Jugar a Carmeet", "Jugar Carmeet", "Jouer à Carmeet",
        "Gioca a Carmeet", "Carmeet をプレイ", "Carmeet 플레이", "Carmeet spelen",
        "Jogar Carmeet", "开玩 Carmeet"),

    "The garage is open and the street is waiting.": (
        "Die Garage ist offen, und die Straße wartet.",
        "El garaje está abierto y la calle te espera.",
        "El garaje está abierto y la calle te espera.",
        "Le garage est ouvert et la rue t'attend.",
        "Il garage è aperto e la strada ti aspetta.",
        "ガレージはオープン。ストリートが待ってます。",
        "차고는 열려 있고, 거리가 기다리고 있어요.",
        "De garage is open en de straat wacht.",
        "A garagem está aberta e a rua está esperando.",
        "车库已开，街头在等你。"),

    # The footer is split around the link on the name, so the first half ends where the name
    # goes and the second picks up after it: "Carmeet は [Levi Foster] による…".
    "Carmeet is an independent fan project by": (
        "Carmeet ist ein unabhängiges Fanprojekt von",
        "Carmeet es un proyecto fan independiente de",
        "Carmeet es un proyecto fan independiente de",
        "Carmeet est un projet de fan indépendant de",
        "Carmeet è un fan project indipendente di",
        "Carmeet は",
        "Carmeet은",
        "Carmeet is een onafhankelijk fanproject van",
        "Carmeet é um projeto de fã independente de",
        "Carmeet 是"),

    ". It is not affiliated with, endorsed or sponsored by Electronic Arts. Need for Speed and Underground are trademarks of Electronic Arts Inc.": (
        ". Es steht in keiner Verbindung zu Electronic Arts und wird von Electronic Arts weder befürwortet noch gesponsert. Need for Speed und Underground sind Marken von Electronic Arts Inc.",
        ". No está afiliado a Electronic Arts, ni respaldado ni patrocinado por Electronic Arts. Need for Speed y Underground son marcas comerciales de Electronic Arts Inc.",
        ". No está afiliado a Electronic Arts, ni respaldado ni patrocinado por Electronic Arts. Need for Speed y Underground son marcas comerciales de Electronic Arts Inc.",
        ". Il n'est ni affilié à Electronic Arts, ni approuvé ni sponsorisé par Electronic Arts. Need for Speed et Underground sont des marques commerciales d'Electronic Arts Inc.",
        ". Non è affiliato a Electronic Arts, né approvato o sponsorizzato da Electronic Arts. Need for Speed e Underground sono marchi di Electronic Arts Inc.",
        " による独立したファンプロジェクトです。Electronic Arts とは提携関係になく、Electronic Arts の承認も後援も受けていません。Need for Speed および Underground は Electronic Arts Inc. の商標です。",
        "가 만든 독립 팬 프로젝트예요. Electronic Arts와 제휴 관계가 없으며, Electronic Arts의 승인이나 후원도 받지 않았어요. Need for Speed와 Underground는 Electronic Arts Inc.의 상표예요.",
        ". Het is niet gelieerd aan, goedgekeurd door of gesponsord door Electronic Arts. Need for Speed en Underground zijn handelsmerken van Electronic Arts Inc.",
        ". Não é afiliado à Electronic Arts, nem endossado ou patrocinado pela Electronic Arts. Need for Speed e Underground são marcas comerciais da Electronic Arts Inc.",
        " 的独立粉丝项目，与 Electronic Arts 没有任何关联，也未获得 Electronic Arts 的认可或赞助。Need for Speed 和 Underground 是 Electronic Arts Inc. 的商标。"),

    # ------------------------------------------------------------------ JSON-LD only

    "How Carmeet was made: the city and cars of Need for Speed: Underground 2, reverse engineered from the PS2 disc and rebuilt as a multiplayer car meet in the browser.": (
        "Wie Carmeet entstand: die Stadt und die Autos aus Need for Speed: Underground 2, per Reverse Engineering von der PS2-Disc geholt und als Multiplayer-Car-Meet im Browser neu gebaut.",
        "Cómo se hizo Carmeet: la ciudad y los coches de Need for Speed: Underground 2, sacados del disco de PS2 con ingeniería inversa y reconstruidos como una quedada de coches multijugador en el navegador.",
        "Cómo se hizo Carmeet: la ciudad y los carros de Need for Speed: Underground 2, sacados del disco de PS2 con ingeniería inversa y reconstruidos como un car meet multijugador en el navegador.",
        "Comment Carmeet a été fait : la ville et les voitures de Need for Speed: Underground 2, extraites du disque PS2 par rétro-ingénierie et reconstruites en rassemblement auto multijoueur dans le navigateur.",
        "Come è nato Carmeet: la città e le auto di Need for Speed: Underground 2, ricavate dal disco PS2 con il reverse engineering e ricostruite come raduno d'auto multigiocatore nel browser.",
        "Carmeet のつくりかた：Need for Speed: Underground 2 の街と車を PS2 ディスクからリバースエンジニアリングし、ブラウザで遊べるマルチプレイのカーミートとして再構築。",
        "Carmeet 제작기: Need for Speed: Underground 2의 도시와 차들을 PS2 디스크에서 리버스 엔지니어링해, 브라우저 멀티플레이 카밋으로 다시 만들었어요.",
        "Hoe Carmeet is gemaakt: de stad en auto's uit Need for Speed: Underground 2, met reverse engineering van de PS2-disc gehaald en herbouwd als multiplayer-autotreffen in de browser.",
        "Como o Carmeet foi feito: a cidade e os carros de Need for Speed: Underground 2, extraídos do disco de PS2 por engenharia reversa e reconstruídos como um encontro de carros multiplayer no navegador.",
        "Carmeet 是怎么做出来的：Need for Speed: Underground 2 的城市和车辆，从 PS2 光盘逆向工程而来，重建为浏览器里的多人车聚。"),

    "A free multiplayer car meet in the browser. Build a car from 29 cars in the original garage, cruise one shared city with everyone online, get out and walk, use emotes, voice and text chat, and take photos with an in-game phone.": (
        "Ein kostenloses Multiplayer-Car-Meet im Browser. Bau eines von 29 Autos in der Original-Garage auf, cruise mit allen, die online sind, durch eine gemeinsame Stadt, steig aus und lauf herum, nutz Emotes, Sprach- und Textchat und mach Fotos mit einem Handy im Spiel.",
        "Una quedada de coches multijugador y gratis en el navegador. Tunea uno de los 29 coches en el garaje original, rueda por una ciudad compartida con todos los conectados, bájate y camina, usa gestos, chat de voz y de texto, y haz fotos con un móvil dentro del juego.",
        "Un car meet multijugador y gratis en el navegador. Arma uno de los 29 carros en el garaje original, rueda por una ciudad compartida con todos los que están en línea, bájate y camina, usa emotes, chat de voz y de texto, y toma fotos con un celular dentro del juego.",
        "Un rassemblement auto multijoueur et gratuit dans le navigateur. Prépare l'une des 29 voitures dans le garage d'origine, balade-toi dans une ville partagée avec tout le monde en ligne, descends et marche, utilise des emotes, le chat vocal et écrit, et prends des photos avec un téléphone dans le jeu.",
        "Un raduno d'auto multigiocatore e gratuito nel browser. Elabora una delle 29 auto nel garage originale, gira per un'unica città condivisa con tutti quelli online, scendi e cammina, usa le emote, la chat vocale e testuale, e scatta foto con un telefono nel gioco.",
        "ブラウザで遊べる無料のマルチプレイ・カーミート。オリジナルのガレージで 29 台から車を組み、オンラインのみんなと一つの街を流し、車を降りて歩き、エモートやボイス・テキストチャットを使い、ゲーム内のスマホで写真を撮ろう。",
        "브라우저에서 즐기는 무료 멀티플레이 카밋. 오리지널 차고에서 29대 중 한 대를 튜닝하고, 접속한 모두와 하나의 도시를 달리고, 차에서 내려 걷고, 이모트와 음성·텍스트 채팅을 쓰고, 게임 속 폰으로 사진을 찍어요.",
        "Een gratis multiplayer-autotreffen in de browser. Bouw een van de 29 auto's op in de originele garage, toer met iedereen die online is door één gedeelde stad, stap uit en loop rond, gebruik emotes, voice- en tekstchat, en maak foto's met een telefoon in de game.",
        "Um encontro de carros multiplayer e grátis no navegador. Monte um dos 29 carros na garagem original, dê um rolê por uma cidade compartilhada com todo mundo online, desça e ande, use emotes, chat de voz e de texto, e tire fotos com um celular dentro do jogo.",
        "浏览器里的免费多人车聚。在原版车库里从 29 辆车中挑一辆来改，和所有在线的人一起在同一座城市里兜风，下车走走，用表情动作、语音和文字聊天，还能用游戏内的手机拍照。"),

    "Twenty-two seconds of Carmeet: a convoy through the city, building cars in the garage, the meet, the phone camera and the map from above.": (
        "Zweiundzwanzig Sekunden Carmeet: ein Konvoi durch die Stadt, Autos aufbauen in der Garage, das Treffen, die Handykamera und die Karte von oben.",
        "Veintidós segundos de Carmeet: un convoy por la ciudad, tuneando coches en el garaje, la quedada, la cámara del móvil y el mapa desde arriba.",
        "Veintidós segundos de Carmeet: un convoy por la ciudad, armando carros en el garaje, el car meet, la cámara del celular y el mapa desde arriba.",
        "Vingt-deux secondes de Carmeet : un convoi dans la ville, la prépa des voitures au garage, le rassemblement, l'appareil photo du téléphone et la carte vue d'en haut.",
        "Ventidue secondi di Carmeet: un convoglio in città, auto elaborate nel garage, il raduno, la fotocamera del telefono e la mappa dall'alto.",
        "22 秒の Carmeet：街を走る車列、ガレージでのカスタム、ミート、スマホのカメラ、そして上空からのマップ。",
        "22초짜리 Carmeet: 도시를 달리는 차량 행렬, 차고에서의 튜닝, 카밋, 폰 카메라, 그리고 위에서 본 지도.",
        "Tweeëntwintig seconden Carmeet: een konvooi door de stad, auto's bouwen in de garage, het treffen, de telefooncamera en de kaart van bovenaf.",
        "Vinte e dois segundos de Carmeet: um comboio pela cidade, montando carros na garagem, o encontro, a câmera do celular e o mapa visto de cima.",
        "22 秒的 Carmeet：穿城而过的车队、在车库里改车、车聚现场、手机相机，以及从上方俯瞰的地图。"),

    "Carmeet trailer": (
        "Carmeet-Trailer", "Tráiler de Carmeet", "Tráiler de Carmeet", "Bande-annonce de Carmeet",
        "Trailer di Carmeet", "Carmeet トレーラー", "Carmeet 트레일러", "Carmeet-trailer",
        "Trailer do Carmeet", "Carmeet 预告片"),
}

KEEP |= {"Discord", "X", "Instagram"}  # names, the same in every language
