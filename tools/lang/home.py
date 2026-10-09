"""lf.wtf home page, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The page is a periodic table: Levi is element Lf, and the twelve things he works on are its
electrons. The short labels (Role, Format, Electrons, Shells, Origin, State, Venture, Game, Art,
Open) are set in uppercase mono as data labels, so they are translated as the shortest natural
label, not as a sentence. "Table of works" plays on "periodic table" and is written as each
language's equivalent of that phrase: Werktabelle, Tabla de obras, Tableau des œuvres, Tavola delle
opere, 作品表, 작품표, Werkentabel, Tabela de obras.

Address follows the rest of the site: du, tú, tu and je, vous in French, você in Portuguese, and
해요체 or 합니다체 in Korean. First person stays first person ("wo ich", "donde me ocupo", わたし).
Co-owner is the word a business card would use: Mitinhaber, socio, associé, socio, 共同オーナー,
공동 소유주, mede-eigenaar, sócio, 合伙人. Prices are left exactly as the English writes them.

"App" is deliberately left as "App" in every language, Japanese, Korean and Chinese included. The
build replaces strings by scanning forward, and every "App" family label after the first comes
straight after the previous row's "App Store" link, so a translated "App" would land inside that
link ("アプリ Store") and leave the label itself in English. Chinese already writes App on this
site; in Japanese and Korean it reads as the same Latin label the App Store link sits next to.

No em-dashes anywhere, per house style.
"""

#: Names, handles, domains and marks that are the same in every language.
KEEP = {
    "Levi", "Foster", "Levi Foster", "© Levi Foster", "lf.wtf", "L@LF.WTF",
    "App Store", "Instagram", "X", "GitHub", "TikTok", "Etsy",
    "Red Arrow Marketing", "Crest Acquisitions", "Morterra", "Carmeet",
    "Harmony Palette", "FRMT", "MODUL8", "CYANO", "Dollop", "Kippu", "GRNGE",
    "Merge With The Machine",
    "redarrowmarketing.com", "crestacquisitions.com", "morterra.com", "mergewiththemachine.com",
    "lf.wtf/harmony", "lf.wtf/frmt", "lf.wtf/modul8", "lf.wtf/cyano", "lf.wtf/dollop",
    "lf.wtf/kippu", "lf.wtf/grnge", "lf.wtf/carmeet",
}

T = {
    # ------------------------------------------------------------------ head
    "Levi Foster: Operations, iPhone Apps and Browser Games, Fort Worth": (
        "Levi Foster: Operations, iPhone-Apps und Browserspiele, Fort Worth",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador, Fort Worth",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador, Fort Worth",
        "Levi Foster : opérations, apps iPhone et jeux par navigateur, Fort Worth",
        "Levi Foster: operations, app per iPhone e giochi per browser, Fort Worth",
        "Levi Foster｜オペレーション、iPhone アプリ、ブラウザゲーム｜フォートワース",
        "Levi Foster｜운영, iPhone 앱, 브라우저 게임｜포트워스",
        "Levi Foster: operations, iPhone-apps en browsergames, Fort Worth",
        "Levi Foster: operações, apps para iPhone e jogos de navegador, Fort Worth",
        "Levi Foster｜运营、iPhone 应用与网页游戏｜沃斯堡"),
    "Levi Foster runs operations at Red Arrow Marketing, co-owns Crest Acquisitions, and builds "
    "iPhone apps, browser games and art in Fort Worth, Texas.": (
        "Levi Foster leitet das operative Geschäft bei Red Arrow Marketing, ist Mitinhaber von "
        "Crest Acquisitions und baut iPhone-Apps, Browserspiele und Kunst in Fort Worth, Texas.",
        "Levi Foster dirige las operaciones de Red Arrow Marketing, es socio de Crest "
        "Acquisitions y crea apps para iPhone, juegos de navegador y arte en Fort Worth, Texas.",
        "Levi Foster dirige las operaciones de Red Arrow Marketing, es socio de Crest "
        "Acquisitions y crea apps para iPhone, juegos de navegador y arte en Fort Worth, Texas.",
        "Levi Foster dirige les opérations de Red Arrow Marketing, est associé de Crest "
        "Acquisitions et crée des apps iPhone, des jeux par navigateur et de l'art à Fort Worth, "
        "au Texas.",
        "Levi Foster dirige le operations di Red Arrow Marketing, è socio di Crest Acquisitions "
        "e crea app per iPhone, giochi per browser e arte a Fort Worth, Texas.",
        "Levi Foster は Red Arrow Marketing のオペレーションを統括し、Crest Acquisitions の"
        "共同オーナーを務めながら、テキサス州フォートワースで iPhone アプリ、ブラウザゲーム、"
        "アートをつくっています。",
        "Levi Foster는 Red Arrow Marketing의 운영을 총괄하고 Crest Acquisitions의 공동 "
        "소유주이며, 텍사스주 포트워스에서 iPhone 앱, 브라우저 게임, 아트를 만듭니다.",
        "Levi Foster leidt de operations bij Red Arrow Marketing, is mede-eigenaar van Crest "
        "Acquisitions en bouwt iPhone-apps, browsergames en kunst in Fort Worth, Texas.",
        "Levi Foster dirige as operações da Red Arrow Marketing, é sócio da Crest Acquisitions e "
        "cria apps para iPhone, jogos de navegador e arte em Fort Worth, Texas.",
        "Levi Foster 负责 Red Arrow Marketing 的运营，是 Crest Acquisitions 的合伙人，并在"
        "美国得州沃斯堡制作 iPhone 应用、网页游戏和艺术作品。"),
    "Levi Foster: Operations, iPhone Apps and Browser Games": (
        "Levi Foster: Operations, iPhone-Apps und Browserspiele",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador",
        "Levi Foster : opérations, apps iPhone et jeux par navigateur",
        "Levi Foster: operations, app per iPhone e giochi per browser",
        "Levi Foster｜オペレーション、iPhone アプリ、ブラウザゲーム",
        "Levi Foster｜운영, iPhone 앱, 브라우저 게임",
        "Levi Foster: operations, iPhone-apps en browsergames",
        "Levi Foster: operações, apps para iPhone e jogos de navegador",
        "Levi Foster｜运营、iPhone 应用与网页游戏"),
    "Director of operations at Red Arrow Marketing, co-owner of Crest Acquisitions, and the "
    "developer behind seven iPhone apps, Morterra graphics and Carmeet. Fort Worth, Texas.": (
        "Leiter des operativen Geschäfts bei Red Arrow Marketing, Mitinhaber von Crest "
        "Acquisitions und der Entwickler hinter sieben iPhone-Apps, der Grafik von Morterra und "
        "Carmeet. Fort Worth, Texas.",
        "Director de operaciones en Red Arrow Marketing, socio de Crest Acquisitions y el "
        "desarrollador detrás de siete apps para iPhone, los gráficos de Morterra y Carmeet. "
        "Fort Worth, Texas.",
        "Director de operaciones en Red Arrow Marketing, socio de Crest Acquisitions y el "
        "desarrollador detrás de siete apps para iPhone, los gráficos de Morterra y Carmeet. "
        "Fort Worth, Texas.",
        "Directeur des opérations chez Red Arrow Marketing, associé de Crest Acquisitions, et le "
        "développeur derrière sept apps iPhone, les graphismes de Morterra et Carmeet. Fort "
        "Worth, Texas.",
        "Direttore operativo di Red Arrow Marketing, socio di Crest Acquisitions e lo "
        "sviluppatore dietro sette app per iPhone, la grafica di Morterra e Carmeet. Fort Worth, "
        "Texas.",
        "Red Arrow Marketing のオペレーション責任者、Crest Acquisitions の共同オーナー。"
        "7 本の iPhone アプリ、Morterra のグラフィック、Carmeet の開発者。テキサス州フォートワース。",
        "Red Arrow Marketing의 운영 이사, Crest Acquisitions의 공동 소유주, 그리고 iPhone 앱 "
        "7개와 Morterra 그래픽, Carmeet을 만든 개발자. 텍사스주 포트워스.",
        "Directeur operations bij Red Arrow Marketing, mede-eigenaar van Crest Acquisitions en "
        "de ontwikkelaar achter zeven iPhone-apps, de graphics van Morterra en Carmeet. Fort "
        "Worth, Texas.",
        "Diretor de operações da Red Arrow Marketing, sócio da Crest Acquisitions e o "
        "desenvolvedor por trás de sete apps para iPhone, dos gráficos de Morterra e do Carmeet. "
        "Fort Worth, Texas.",
        "Red Arrow Marketing 运营总监，Crest Acquisitions 合伙人，七款 iPhone 应用、Morterra "
        "图形与 Carmeet 的开发者。美国得州沃斯堡。"),
    "The element Lf: Levi Foster, number 1": (
        "Das Element Lf: Levi Foster, Ordnungszahl 1",
        "El elemento Lf: Levi Foster, número atómico 1",
        "El elemento Lf: Levi Foster, número atómico 1",
        "L'élément Lf : Levi Foster, numéro atomique 1",
        "L'elemento Lf: Levi Foster, numero atomico 1",
        "元素 Lf：Levi Foster、原子番号 1",
        "원소 Lf: Levi Foster, 원자 번호 1",
        "Het element Lf: Levi Foster, atoomnummer 1",
        "O elemento Lf: Levi Foster, número atômico 1",
        "元素 Lf：Levi Foster，原子序数 1"),

    # ------------------------------------------------------------------ bar
    "Sections": ("Abschnitte", "Secciones", "Secciones", "Sections", "Sezioni", "セクション",
                 "섹션", "Secties", "Seções", "栏目"),
    "Table of works": ("Werktabelle", "Tabla de obras", "Tabla de obras", "Tableau des œuvres",
                       "Tavola delle opere", "作品表", "작품표", "Werkentabel", "Tabela de obras",
                       "作品表"),
    "Specification": ("Spezifikation", "Especificación", "Especificación", "Spécification",
                      "Specifiche", "仕様", "사양", "Specificatie", "Especificação", "规格"),
    "Contact": ("Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "連絡先", "연락처",
                "Contact", "Contato", "联系"),
    "Language": ("Sprache", "Idioma", "Idioma", "Langue", "Lingua", "言語", "언어", "Taal",
                 "Idioma", "语言"),

    # ------------------------------------------------------------------ the element
    "Levi Foster, drawn as an element": (
        "Levi Foster, als Element dargestellt",
        "Levi Foster, dibujado como un elemento",
        "Levi Foster, dibujado como un elemento",
        "Levi Foster, dessiné comme un élément",
        "Levi Foster, disegnato come un elemento",
        "元素として描いた Levi Foster",
        "원소로 그린 Levi Foster",
        "Levi Foster, getekend als element",
        "Levi Foster, desenhado como um elemento",
        "画成一个元素的 Levi Foster"),
    "Electrons": ("Elektronen", "Electrones", "Electrones", "Électrons", "Elettroni", "電子",
                  "전자", "Elektronen", "Elétrons", "电子"),
    "12, one per work": ("12, eins pro Werk", "12, uno por obra", "12, uno por obra",
                         "12, un par œuvre", "12, uno per opera", "12、作品ごとに 1 つ",
                         "12, 작품마다 하나", "12, één per werk", "12, um por obra",
                         "12，每件作品一个"),
    "Shells": ("Schalen", "Capas", "Capas", "Couches", "Gusci", "電子殻", "전자 껍질", "Schillen",
               "Camadas", "电子层"),
    "Origin": ("Herkunft", "Origen", "Origen", "Origine", "Origine", "出身", "출신", "Herkomst",
               "Origem", "来自"),
    "Fort Worth, Texas": ("Fort Worth, Texas", "Fort Worth, Texas", "Fort Worth, Texas",
                          "Fort Worth, Texas", "Fort Worth, Texas", "テキサス州フォートワース",
                          "텍사스주 포트워스", "Fort Worth, Texas", "Fort Worth, Texas",
                          "美国得州沃斯堡"),
    "State": ("Zustand", "Estado", "Estado", "État", "Stato", "状態", "상태", "Toestand", "Estado",
              "状态"),
    "Active": ("Aktiv", "Activo", "Activo", "Actif", "Attivo", "アクティブ", "활동 중", "Actief",
               "Ativo", "活跃"),
    "Director of operations and co-owner at Red Arrow Marketing. Co-owner of Crest Acquisitions, "
    "where I work on research and AI integration. Developer of seven iPhone apps and two browser "
    "games, Morterra and Carmeet. Artist behind Merge With The Machine.": (
        "Leiter des operativen Geschäfts und Mitinhaber bei Red Arrow Marketing. Mitinhaber von "
        "Crest Acquisitions, wo ich an Recherche und KI-Integration arbeite. Entwickler von "
        "sieben iPhone-Apps und zwei Browserspielen, Morterra und Carmeet. Künstler hinter Merge "
        "With The Machine.",
        "Director de operaciones y socio en Red Arrow Marketing. Socio de Crest Acquisitions, "
        "donde me ocupo de la investigación y la integración de IA. Desarrollador de siete apps "
        "para iPhone y dos juegos de navegador, Morterra y Carmeet. Artista detrás de Merge With "
        "The Machine.",
        "Director de operaciones y socio en Red Arrow Marketing. Socio de Crest Acquisitions, "
        "donde me ocupo de la investigación y la integración de IA. Desarrollador de siete apps "
        "para iPhone y dos juegos de navegador, Morterra y Carmeet. Artista detrás de Merge With "
        "The Machine.",
        "Directeur des opérations et associé chez Red Arrow Marketing. Associé de Crest "
        "Acquisitions, où je travaille sur la recherche et l'intégration de l'IA. Développeur de "
        "sept apps iPhone et de deux jeux par navigateur, Morterra et Carmeet. Artiste derrière "
        "Merge With The Machine.",
        "Direttore operativo e socio di Red Arrow Marketing. Socio di Crest Acquisitions, dove "
        "mi occupo di ricerca e integrazione dell'IA. Sviluppatore di sette app per iPhone e due "
        "giochi per browser, Morterra e Carmeet. Artista dietro Merge With The Machine.",
        "Red Arrow Marketing のオペレーション責任者、共同オーナー。Crest Acquisitions の"
        "共同オーナーとして、リサーチと AI の導入を担当しています。7 本の iPhone アプリと、"
        "Morterra と Carmeet の 2 本のブラウザゲームの開発者。Merge With The Machine の"
        "アーティスト。",
        "Red Arrow Marketing의 운영 이사이자 공동 소유주. Crest Acquisitions의 공동 소유주로 "
        "리서치와 AI 도입을 맡고 있습니다. iPhone 앱 7개와 브라우저 게임 2개, Morterra와 "
        "Carmeet의 개발자. Merge With The Machine의 아티스트.",
        "Directeur operations en mede-eigenaar bij Red Arrow Marketing. Mede-eigenaar van Crest "
        "Acquisitions, waar ik aan research en AI-integratie werk. Ontwikkelaar van zeven "
        "iPhone-apps en twee browsergames, Morterra en Carmeet. Kunstenaar achter Merge With The "
        "Machine.",
        "Diretor de operações e sócio da Red Arrow Marketing. Sócio da Crest Acquisitions, onde "
        "cuido de pesquisa e integração de IA. Desenvolvedor de sete apps para iPhone e dois "
        "jogos de navegador, Morterra e Carmeet. Artista por trás do Merge With The Machine.",
        "Red Arrow Marketing 运营总监、合伙人。Crest Acquisitions 合伙人，我在那里负责研究和 "
        "AI 集成。七款 iPhone 应用和两款网页游戏 Morterra 与 Carmeet 的开发者。"
        "Merge With The Machine 背后的艺术家。"),
    "Profiles": ("Profile", "Perfiles", "Perfiles", "Profils", "Profili", "プロフィール",
                 "프로필", "Profielen", "Perfis", "个人主页"),

    # ------------------------------------------------------------------ table and readout
    "12 elements": ("12 Elemente", "12 elementos", "12 elementos", "12 éléments", "12 elementi",
                    "12 の元素", "원소 12개", "12 elementen", "12 elementos", "12 种元素"),
    "Selected element": ("Ausgewähltes Element", "Elemento seleccionado", "Elemento seleccionado",
                         "Élément sélectionné", "Elemento selezionato", "選択中の元素",
                         "선택한 원소", "Geselecteerd element", "Elemento selecionado",
                         "所选元素"),
    "Role": ("Rolle", "Cargo", "Cargo", "Rôle", "Ruolo", "役割", "역할", "Rol", "Função", "角色"),
    "Format": ("Format", "Formato", "Formato", "Format", "Formato", "形態", "형태", "Vorm",
               "Formato", "形式"),
    "Open": ("Öffnen", "Abrir", "Abrir", "Ouvrir", "Apri", "開く", "열기", "Openen", "Abrir",
             "打开"),
    "Every element in full: the companies, the apps and games, and the art.": (
        "Jedes Element vollständig: die Firmen, die Apps und Spiele und die Kunst.",
        "Cada elemento completo: las empresas, las apps y los juegos, y el arte.",
        "Cada elemento completo: las empresas, las apps y los juegos, y el arte.",
        "Chaque élément en entier : les entreprises, les apps et les jeux, et l'art.",
        "Ogni elemento per intero: le aziende, le app e i giochi, e l'arte.",
        "すべての元素を詳しく：会社、アプリとゲーム、そしてアート。",
        "모든 원소를 자세히: 회사, 앱과 게임, 그리고 아트.",
        "Elk element volledig: de bedrijven, de apps en games, en de kunst.",
        "Cada elemento por inteiro: as empresas, os apps e jogos, e a arte.",
        "每个元素的完整说明：公司、应用与游戏，以及艺术。"),

    # Family labels, the periodic table's "alkali metal" and "noble gas".
    "Venture": ("Unternehmen", "Empresa", "Empresa", "Entreprise", "Impresa", "事業", "사업",
                "Onderneming", "Empresa", "企业"),
    "Game": ("Spiel", "Juego", "Juego", "Jeu", "Gioco", "ゲーム", "게임", "Game", "Jogo", "游戏"),
    # See the docstring: identical everywhere on purpose.
    "App": ("App", "App", "App", "App", "App", "App", "App", "App", "App", "App"),
    "Art": ("Kunst", "Arte", "Arte", "Art", "Arte", "アート", "아트", "Kunst", "Arte", "艺术"),

    # Roles and formats.
    "Director of operations, co-owner": (
        "Leiter des operativen Geschäfts, Mitinhaber",
        "Director de operaciones, socio",
        "Director de operaciones, socio",
        "Directeur des opérations, associé",
        "Direttore operativo, socio",
        "オペレーション責任者、共同オーナー",
        "운영 이사, 공동 소유주",
        "Directeur operations, mede-eigenaar",
        "Diretor de operações, sócio",
        "运营总监，合伙人"),
    "Agency, Fort Worth, Texas": (
        "Agentur, Fort Worth, Texas", "Agencia, Fort Worth, Texas", "Agencia, Fort Worth, Texas",
        "Agence, Fort Worth, Texas", "Agenzia, Fort Worth, Texas",
        "エージェンシー、テキサス州フォートワース", "에이전시, 텍사스주 포트워스",
        "Bureau, Fort Worth, Texas", "Agência, Fort Worth, Texas", "营销机构，美国得州沃斯堡"),
    "Co-owner, research, AI integration": (
        "Mitinhaber, Recherche, KI-Integration",
        "Socio, investigación, integración de IA",
        "Socio, investigación, integración de IA",
        "Associé, recherche, intégration de l'IA",
        "Socio, ricerca, integrazione dell'IA",
        "共同オーナー、リサーチ、AI 導入",
        "공동 소유주, 리서치, AI 도입",
        "Mede-eigenaar, research, AI-integratie",
        "Sócio, pesquisa, integração de IA",
        "合伙人，研究，AI 集成"),
    "Acquisitions, nationwide": (
        "Ankäufe, landesweit", "Adquisiciones, en todo el país", "Adquisiciones, en todo el país",
        "Acquisitions, dans tout le pays", "Acquisizioni, in tutto il paese", "買い取り、全米",
        "매입, 미국 전역", "Acquisities, landelijk", "Aquisições, em todo o país", "收购，全美"),
    "Graphics, developer": (
        "Grafik, Entwickler", "Gráficos, desarrollador", "Gráficos, desarrollador",
        "Graphismes, développeur", "Grafica, sviluppatore", "グラフィック、開発者",
        "그래픽, 개발자", "Graphics, ontwikkelaar", "Gráficos, desenvolvedor", "图形，开发者"),
    "Browser game, free": (
        "Browserspiel, kostenlos", "Juego de navegador, gratis", "Juego de navegador, gratis",
        "Jeu par navigateur, gratuit", "Gioco per browser, gratis", "ブラウザゲーム、無料",
        "브라우저 게임, 무료", "Browsergame, gratis", "Jogo de navegador, grátis",
        "网页游戏，免费"),
    "Developer": ("Entwickler", "Desarrollador", "Desarrollador", "Développeur", "Sviluppatore",
                  "開発者", "개발자", "Ontwikkelaar", "Desenvolvedor", "开发者"),
    "iPhone, free, Pro from $2.99": (
        "iPhone, kostenlos, Pro ab $2.99", "iPhone, gratis, Pro desde $2.99",
        "iPhone, gratis, Pro desde $2.99", "iPhone, gratuit, Pro à partir de $2.99",
        "iPhone, gratis, Pro da $2.99", "iPhone、無料、Pro は $2.99 から",
        "iPhone, 무료, Pro는 $2.99부터", "iPhone, gratis, Pro vanaf $2.99",
        "iPhone, grátis, Pro a partir de $2.99", "iPhone，免费，Pro $2.99 起"),
    "iPhone, $14.99 once": (
        "iPhone, $14.99 einmalig", "iPhone, pago único de $14.99", "iPhone, pago único de $14.99",
        "iPhone, $14.99 en achat unique", "iPhone, $14.99 una tantum", "iPhone、$14.99 買い切り",
        "iPhone, $14.99 일회 구매", "iPhone, $14.99 eenmalig", "iPhone, pagamento único de $14.99",
        "iPhone，$14.99 买断"),
    "iPhone, free, Premium": (
        "iPhone, kostenlos, Premium", "iPhone, gratis, Premium", "iPhone, gratis, Premium",
        "iPhone, gratuit, Premium", "iPhone, gratis, Premium", "iPhone、無料、Premium",
        "iPhone, 무료, Premium", "iPhone, gratis, Premium", "iPhone, grátis, Premium",
        "iPhone，免费，Premium"),
    "iPhone, free": ("iPhone, kostenlos", "iPhone, gratis", "iPhone, gratis", "iPhone, gratuit",
                     "iPhone, gratis", "iPhone、無料", "iPhone, 무료", "iPhone, gratis",
                     "iPhone, grátis", "iPhone，免费"),
    "iPhone game, free": ("iPhone-Spiel, kostenlos", "Juego para iPhone, gratis",
                          "Juego para iPhone, gratis", "Jeu iPhone, gratuit",
                          "Gioco per iPhone, gratis", "iPhone ゲーム、無料", "iPhone 게임, 무료",
                          "iPhone-game, gratis", "Jogo para iPhone, grátis", "iPhone 游戏，免费"),
    "iPhone and iPad, free": ("iPhone und iPad, kostenlos", "iPhone y iPad, gratis",
                              "iPhone y iPad, gratis", "iPhone et iPad, gratuit",
                              "iPhone e iPad, gratis", "iPhone と iPad、無料",
                              "iPhone과 iPad, 무료", "iPhone en iPad, gratis",
                              "iPhone e iPad, grátis", "iPhone 和 iPad，免费"),
    "Reverse engineering, developer": (
        "Reverse Engineering, Entwickler", "Ingeniería inversa, desarrollador",
        "Ingeniería inversa, desarrollador", "Rétro-ingénierie, développeur",
        "Reverse engineering, sviluppatore", "リバースエンジニアリング、開発者",
        "리버스 엔지니어링, 개발자", "Reverse engineering, ontwikkelaar",
        "Engenharia reversa, desenvolvedor", "逆向工程，开发者"),
    "Artist": ("Künstler", "Artista", "Artista", "Artiste", "Artista", "アーティスト", "아티스트",
               "Kunstenaar", "Artista", "艺术家"),
    "Art project, prints": (
        "Kunstprojekt, Drucke", "Proyecto artístico, impresiones",
        "Proyecto artístico, impresiones", "Projet artistique, tirages",
        "Progetto artistico, stampe", "アートプロジェクト、プリント", "아트 프로젝트, 프린트",
        "Kunstproject, prints", "Projeto de arte, impressões", "艺术项目，版画"),

    # ------------------------------------------------------------------ descriptions
    # Each one is shown in the table's readout, in the specification and in the JSON-LD list.
    "A Fort Worth web design and digital marketing agency. Websites, SEO, ads, social and "
    "content, made in-house for clients nationwide.": (
        "Eine Agentur für Webdesign und digitales Marketing aus Fort Worth. Websites, SEO, "
        "Anzeigen, Social Media und Content, im eigenen Haus gemacht, für Kunden im ganzen Land.",
        "Una agencia de diseño web y marketing digital de Fort Worth. Sitios web, SEO, anuncios, "
        "redes sociales y contenido, hechos en casa para clientes de todo el país.",
        "Una agencia de diseño web y marketing digital de Fort Worth. Sitios web, SEO, anuncios, "
        "redes sociales y contenido, hechos en casa para clientes de todo el país.",
        "Une agence de web design et de marketing digital de Fort Worth. Sites web, SEO, "
        "publicité, réseaux sociaux et contenu, faits en interne pour des clients dans tout le "
        "pays.",
        "Un'agenzia di web design e marketing digitale di Fort Worth. Siti web, SEO, pubblicità, "
        "social e contenuti, realizzati internamente per clienti in tutto il paese.",
        "フォートワースのウェブデザインとデジタルマーケティングのエージェンシー。ウェブサイト、"
        "SEO、広告、SNS、コンテンツを、全米のクライアントのために社内で制作しています。",
        "포트워스의 웹 디자인·디지털 마케팅 에이전시. 웹사이트, SEO, 광고, 소셜 미디어, "
        "콘텐츠를 미국 전역의 고객을 위해 사내에서 직접 만듭니다.",
        "Een bureau voor webdesign en digitale marketing uit Fort Worth. Websites, SEO, "
        "advertenties, social en content, in eigen huis gemaakt voor klanten in het hele land.",
        "Uma agência de web design e marketing digital de Fort Worth. Sites, SEO, anúncios, "
        "redes sociais e conteúdo, feitos internamente para clientes de todo o país.",
        "一家位于沃斯堡的网页设计与数字营销机构。网站、SEO、广告、社交媒体和内容，全部由自己的"
        "团队完成，服务全美客户。"),
    "Buys liens, non-performing notes and distressed real estate for cash, anywhere in the "
    "country. My side is research and AI integration.": (
        "Kauft Pfandrechte, notleidende Kredite und Problemimmobilien gegen bar, überall im "
        "Land. Mein Teil ist Recherche und KI-Integration.",
        "Compra gravámenes, pagarés en mora e inmuebles en dificultades al contado, en cualquier "
        "parte del país. Lo mío es la investigación y la integración de IA.",
        "Compra gravámenes, pagarés vencidos y propiedades en problemas de contado, en cualquier "
        "parte del país. Lo mío es la investigación y la integración de IA.",
        "Rachète des privilèges, des créances non performantes et de l'immobilier en difficulté "
        "au comptant, partout dans le pays. Ma partie, c'est la recherche et l'intégration de "
        "l'IA.",
        "Acquista privilegi, crediti deteriorati e immobili in difficoltà in contanti, ovunque "
        "nel paese. La mia parte è la ricerca e l'integrazione dell'IA.",
        "担保権、不良債権、ディストレス不動産を、全米どこでも現金で買い取ります。わたしの担当は"
        "リサーチと AI の導入です。",
        "담보권, 부실 채권, 부실 부동산을 미국 어디서든 현금으로 매입합니다. 제 담당은 리서치와 "
        "AI 도입입니다.",
        "Koopt pandrechten, probleemleningen en noodlijdend vastgoed tegen contante betaling, "
        "overal in het land. Mijn deel is research en AI-integratie.",
        "Compra gravames, créditos inadimplentes e imóveis em dificuldade à vista, em qualquer "
        "lugar do país. Minha parte é pesquisa e integração de IA.",
        "在全美任何地方以现金收购留置权、不良债权和困境房地产。我负责研究和 AI 集成。"),
    "A free multiplayer survival sandbox that runs in the browser. Hunt, mine and build anywhere, "
    "with no download and no sign-up.": (
        "Ein kostenloses Multiplayer-Survival-Sandbox-Spiel, das im Browser läuft. Jagen, abbauen "
        "und bauen, überall, ohne Download und ohne Anmeldung.",
        "Un sandbox de supervivencia multijugador y gratuito que funciona en el navegador. Caza, "
        "mina y construye en cualquier parte, sin descargas y sin registro.",
        "Un sandbox de supervivencia multijugador y gratuito que funciona en el navegador. Caza, "
        "mina y construye donde quieras, sin descargas y sin registro.",
        "Un bac à sable de survie multijoueur et gratuit qui tourne dans le navigateur. Chassez, "
        "minez et construisez n'importe où, sans téléchargement ni inscription.",
        "Un sandbox di sopravvivenza multigiocatore e gratuito che gira nel browser. Caccia, "
        "scava e costruisci ovunque, senza download e senza registrazione.",
        "ブラウザで動く無料のマルチプレイヤー・サバイバルサンドボックス。ダウンロードも登録も"
        "なしで、どこでも狩り、採掘し、建てられます。",
        "브라우저에서 돌아가는 무료 멀티플레이 서바이벌 샌드박스. 다운로드도 가입도 없이 "
        "어디서든 사냥하고, 채굴하고, 지을 수 있습니다.",
        "Een gratis multiplayer-survivalsandbox die in de browser draait. Jaag, delf en bouw "
        "overal, zonder download en zonder aanmelding.",
        "Um sandbox de sobrevivência multijogador e gratuito que roda no navegador. Cace, "
        "minere e construa em qualquer lugar, sem download e sem cadastro.",
        "一款在浏览器里运行的免费多人生存沙盒游戏。无需下载，无需注册，随处狩猎、采矿和建造。"),
    "A color harmony and palette tool. RGB and RYB wheels, eight harmony types, 160 curated "
    "palettes, a WCAG contrast checker, and export to SwiftUI, CSS, Tailwind, SVG or PDF.": (
        "Ein Werkzeug für Farbharmonien und Paletten. Farbkreise in RGB und RYB, acht "
        "Harmonietypen, 160 kuratierte Paletten, ein WCAG-Kontrastprüfer und Export nach "
        "SwiftUI, CSS, Tailwind, SVG oder PDF.",
        "Una herramienta de armonía de color y paletas. Ruedas RGB y RYB, ocho tipos de armonía, "
        "160 paletas seleccionadas, un comprobador de contraste WCAG y exportación a SwiftUI, "
        "CSS, Tailwind, SVG o PDF.",
        "Una herramienta de armonía de color y paletas. Ruedas RGB y RYB, ocho tipos de armonía, "
        "160 paletas seleccionadas, un verificador de contraste WCAG y exportación a SwiftUI, "
        "CSS, Tailwind, SVG o PDF.",
        "Un outil d'harmonie des couleurs et de palettes. Roues RVB et RJB, huit types "
        "d'harmonie, 160 palettes sélectionnées, un vérificateur de contraste WCAG et l'export "
        "vers SwiftUI, CSS, Tailwind, SVG ou PDF.",
        "Uno strumento di armonia cromatica e palette. Ruote RGB e RYB, otto tipi di armonia, "
        "160 palette selezionate, un controllo del contrasto WCAG e l'esportazione in SwiftUI, "
        "CSS, Tailwind, SVG o PDF.",
        "配色とパレットのツール。RGB と RYB のカラーホイール、8 種類の調和、厳選された 160 の"
        "パレット、WCAG コントラストチェッカー、そして SwiftUI、CSS、Tailwind、SVG、PDF への"
        "書き出し。",
        "색 조화와 팔레트 도구. RGB와 RYB 색상환, 8가지 조화, 엄선된 160개의 팔레트, WCAG 명도 "
        "대비 검사기, 그리고 SwiftUI, CSS, Tailwind, SVG, PDF로 내보내기.",
        "Een tool voor kleurharmonie en paletten. RGB- en RYB-wielen, acht harmonietypes, 160 "
        "samengestelde paletten, een WCAG-contrastchecker en export naar SwiftUI, CSS, "
        "Tailwind, SVG of PDF.",
        "Uma ferramenta de harmonia de cores e paletas. Rodas RGB e RYB, oito tipos de harmonia, "
        "160 paletas selecionadas, um verificador de contraste WCAG e exportação para SwiftUI, "
        "CSS, Tailwind, SVG ou PDF.",
        "一款配色与调色板工具。RGB 与 RYB 色轮、8 种配色关系、精选的 160 套调色板、WCAG 对比度"
        "检查器，并可导出为 SwiftUI、CSS、Tailwind、SVG 或 PDF。"),
    "A film simulation camera. Four film stocks built from published manufacturer data, "
    "developed from a RAW negative on the phone.": (
        "Eine Filmsimulationskamera. Vier Filme, gebaut aus veröffentlichten Herstellerdaten, "
        "auf dem Handy aus einem RAW-Negativ entwickelt.",
        "Una cámara de simulación de película. Cuatro películas construidas a partir de datos "
        "publicados por los fabricantes, reveladas desde un negativo RAW en el teléfono.",
        "Una cámara de simulación de película. Cuatro películas construidas a partir de datos "
        "publicados por los fabricantes, reveladas desde un negativo RAW en el celular.",
        "Un appareil photo à simulation argentique. Quatre pellicules construites à partir des "
        "données publiées par les fabricants, développées depuis un négatif RAW sur le "
        "téléphone.",
        "Una fotocamera a simulazione di pellicola. Quattro pellicole costruite dai dati "
        "pubblicati dai produttori, sviluppate da un negativo RAW sul telefono.",
        "フィルムシミュレーションカメラ。メーカー公開のデータから組み上げた 4 種のフィルムを、"
        "端末上で RAW ネガから現像します。",
        "필름 시뮬레이션 카메라. 제조사가 공개한 데이터로 만든 네 가지 필름을, 휴대폰 안에서 "
        "RAW 네거티브로부터 현상합니다.",
        "Een filmsimulatiecamera. Vier films, gebouwd op gepubliceerde gegevens van de "
        "fabrikanten, op de telefoon ontwikkeld vanuit een RAW-negatief.",
        "Uma câmera de simulação de filme. Quatro filmes construídos a partir de dados "
        "publicados pelos fabricantes, revelados de um negativo RAW no celular.",
        "一款胶片模拟相机。四款胶片依据厂商公开的数据构建，在手机上从 RAW 底片完成显影。"),
    "Glitch art for photos and video. 29 effects modeled on the ways real hardware failed, from "
    "VHS tracking loss to a satellite feed losing lock, saved up to 4K.": (
        "Glitch Art für Fotos und Video. 29 Effekte, nachgebildet nach den Arten, auf die echte "
        "Hardware versagte, vom VHS-Spurverlust bis zum abreißenden Satellitensignal, "
        "gespeichert in bis zu 4K.",
        "Glitch art para fotos y vídeo. 29 efectos modelados sobre las formas en que fallaba el "
        "hardware real, desde la pérdida de tracking del VHS hasta una señal de satélite que se "
        "cae, guardados hasta en 4K.",
        "Glitch art para fotos y video. 29 efectos modelados sobre las formas en que fallaba el "
        "hardware real, desde la pérdida de tracking del VHS hasta una señal de satélite que se "
        "cae, guardados hasta en 4K.",
        "Du glitch art pour photos et vidéos. 29 effets modélisés sur les façons dont le vrai "
        "matériel tombait en panne, de la perte de piste VHS au signal satellite qui décroche, "
        "enregistrés jusqu'en 4K.",
        "Glitch art per foto e video. 29 effetti modellati sui modi in cui l'hardware vero si "
        "guastava, dalla perdita di tracking del VHS a un segnale satellitare che perde "
        "l'aggancio, salvati fino in 4K.",
        "写真と動画のためのグリッチアート。VHS のトラッキング崩れから受信が途切れた衛星放送まで、"
        "実在のハードウェアの壊れ方を再現した 29 のエフェクトを、最大 4K で保存できます。",
        "사진과 동영상을 위한 글리치 아트. VHS 트래킹 이탈부터 신호를 놓친 위성 방송까지, 실제 "
        "하드웨어가 고장 나던 방식을 모델링한 29가지 효과를 최대 4K로 저장합니다.",
        "Glitch art voor foto's en video. 29 effecten gemodelleerd op de manieren waarop echte "
        "hardware kapotging, van VHS-trackingverlies tot een satellietsignaal dat wegvalt, "
        "opgeslagen tot 4K.",
        "Glitch art para fotos e vídeos. 29 efeitos modelados sobre os jeitos como o hardware de "
        "verdade falhava, da perda de tracking do VHS a um sinal de satélite caindo, salvos em "
        "até 4K.",
        "为照片和视频打造的故障艺术。29 种效果，模拟真实硬件当年出错的方式，从 VHS 循迹丢失到"
        "失锁的卫星信号，最高可保存为 4K。"),
    "Cyanotype prints from your photos, following the chemistry of the 1842 sunprint. No "
    "darkroom, no chemicals, no printer.": (
        "Cyanotypie-Drucke aus deinen Fotos, nach der Chemie des Sonnendrucks von 1842. Keine "
        "Dunkelkammer, keine Chemikalien, kein Drucker.",
        "Cianotipias a partir de tus fotos, siguiendo la química de la impresión al sol de 1842. "
        "Sin cuarto oscuro, sin productos químicos, sin impresora.",
        "Cianotipias a partir de tus fotos, siguiendo la química de la impresión al sol de 1842. "
        "Sin cuarto oscuro, sin químicos, sin impresora.",
        "Des cyanotypes à partir de vos photos, selon la chimie du tirage au soleil de 1842. Sans "
        "chambre noire, sans produits chimiques, sans imprimante.",
        "Cianotipie dalle tue foto, seguendo la chimica della stampa al sole del 1842. Niente "
        "camera oscura, niente prodotti chimici, niente stampante.",
        "1842 年の日光写真の化学に沿って、手持ちの写真からサイアノタイプのプリントをつくります。"
        "暗室も薬品もプリンターも要りません。",
        "1842년 태양광 인화의 화학을 따라, 가진 사진으로 사이아노타입 인화를 만듭니다. 암실도, "
        "약품도, 프린터도 필요 없습니다.",
        "Cyanotypieën van je foto's, volgens de chemie van de zonnedruk uit 1842. Geen donkere "
        "kamer, geen chemicaliën, geen printer.",
        "Cianotipias a partir das suas fotos, seguindo a química da impressão ao sol de 1842. "
        "Sem câmara escura, sem produtos químicos, sem impressora.",
        "依照 1842 年日光晒印的化学，把你的照片做成蓝晒作品。不需要暗房、不需要药水、不需要"
        "打印机。"),
    "A slow color mixing game with paint that behaves like paint, so blue and yellow make green. "
    "Five modes, and nothing that hurries you.": (
        "Ein ruhiges Farbmischspiel mit Farbe, die sich wie Farbe verhält, also ergeben Blau und "
        "Gelb Grün. Fünf Modi und nichts, das dich hetzt.",
        "Un juego tranquilo de mezcla de colores con pintura que se comporta como pintura, así "
        "que el azul y el amarillo dan verde. Cinco modos, y nada que te meta prisa.",
        "Un juego tranquilo de mezcla de colores con pintura que se comporta como pintura, así "
        "que el azul y el amarillo dan verde. Cinco modos, y nada que te apure.",
        "Un jeu tranquille de mélange de couleurs avec de la peinture qui se comporte comme de la "
        "peinture, alors le bleu et le jaune donnent du vert. Cinq modes, et rien qui vous "
        "presse.",
        "Un gioco tranquillo di mescolanza dei colori con vernice che si comporta come vernice, "
        "quindi blu e giallo danno verde. Cinque modalità, e niente che ti metta fretta.",
        "絵の具らしく振る舞う絵の具で色を混ぜる、ゆっくりしたゲーム。だから青と黄で緑になります。"
        "五つのモード、そして急かすものは何もありません。",
        "물감답게 움직이는 물감으로 색을 섞는 느긋한 게임. 그래서 파랑과 노랑은 초록이 됩니다. "
        "다섯 가지 모드, 그리고 재촉하는 것은 하나도 없습니다.",
        "Een rustig kleurmengspel met verf die zich als verf gedraagt, dus blauw en geel worden "
        "groen. Vijf modi, en niets dat je opjaagt.",
        "Um jogo calmo de mistura de cores com tinta que se comporta como tinta, então azul e "
        "amarelo dão verde. Cinco modos, e nada que te apresse.",
        "一款慢节奏的调色游戏，颜料表现得像真颜料，所以蓝加黄是绿色。五种模式，没有任何催着你的"
        "东西。"),
    "Japanese for a trip to Japan, with what the staff say back, then the whole JLPT N5: kana, "
    "kanji, grammar, listening and a mock test.": (
        "Japanisch für eine Reise nach Japan, mit dem, was das Personal antwortet, danach der "
        "ganze JLPT N5: Kana, Kanji, Grammatik, Hören und ein Probetest.",
        "Japonés para un viaje a Japón, con lo que responde el personal, y después el JLPT N5 "
        "completo: kana, kanji, gramática, comprensión auditiva y un examen de prueba.",
        "Japonés para un viaje a Japón, con lo que contesta el personal, y después el JLPT N5 "
        "completo: kana, kanji, gramática, comprensión auditiva y un examen de prueba.",
        "Le japonais pour un voyage au Japon, avec ce que le personnel répond, puis tout le "
        "JLPT N5 : kana, kanji, grammaire, compréhension orale et un test blanc.",
        "Giapponese per un viaggio in Giappone, con quello che risponde il personale, poi tutto "
        "il JLPT N5: kana, kanji, grammatica, ascolto e un test di prova.",
        "日本を旅するための日本語を、店員さんの返答つきで。そのあとは JLPT N5 の全範囲："
        "かな、漢字、文法、聴解、模擬試験。",
        "일본 여행을 위한 일본어를 직원의 답변과 함께, 그다음은 JLPT N5 전체: 가나, 한자, 문법, "
        "듣기, 모의고사.",
        "Japans voor een reis naar Japan, met wat het personeel terugzegt, daarna het hele "
        "JLPT N5: kana, kanji, grammatica, luisteren en een proeftoets.",
        "Japonês para uma viagem ao Japão, com o que o atendente responde, depois o JLPT N5 "
        "inteiro: kana, kanji, gramática, compreensão auditiva e um simulado.",
        "去日本旅行要用的日语，附有店员的回答，然后是完整的 JLPT N5：假名、汉字、语法、听力和"
        "模拟考试。"),
    "Photocopy, stipple, halftone and dither prints from your photos, layered in color inks, "
    "drawn on, cut out and covered in stickers.": (
        "Fotokopie-, Punkt-, Raster- und Dither-Drucke aus deinen Fotos, in farbigen Tinten "
        "übereinandergelegt, bemalt, ausgeschnitten und mit Stickern beklebt.",
        "Impresiones de fotocopia, puntillismo, trama y dither a partir de tus fotos, "
        "superpuestas en tintas de color, dibujadas, recortadas y llenas de pegatinas.",
        "Impresiones de fotocopia, puntillismo, trama y dither a partir de tus fotos, "
        "superpuestas en tintas de color, dibujadas, recortadas y llenas de calcomanías.",
        "Des tirages photocopie, pointillé, trame et tramage à partir de vos photos, superposés "
        "en encres de couleur, dessinés, découpés et couverts d'autocollants.",
        "Stampe a fotocopia, puntinato, retino e dither dalle tue foto, sovrapposte in "
        "inchiostri colorati, disegnate, ritagliate e coperte di adesivi.",
        "写真からつくるコピー、点描、網点、ディザのプリントを、カラーインクで重ね、描き込み、"
        "切り抜き、シールで埋めつくします。",
        "사진으로 만든 복사, 점묘, 망점, 디더 인쇄물을 컬러 잉크로 겹치고, 그리고, 오려내고, "
        "스티커로 덮습니다.",
        "Fotokopie-, stippel-, raster- en ditherafdrukken van je foto's, in kleurinkten over "
        "elkaar gelegd, bekrabbeld, uitgeknipt en vol stickers geplakt.",
        "Impressões de fotocópia, pontilhado, retícula e dither a partir das suas fotos, "
        "sobrepostas em tintas coloridas, rabiscadas, recortadas e cobertas de adesivos.",
        "把你的照片做成复印、点描、网点和抖动印刷品，用彩色墨叠印、涂鸦、抠图，再贴满贴纸。"),
    "A 2004 street racing city, pulled off the game disc and rebuilt in the browser as a place to "
    "hang out. Build a car, cruise with whoever is online, meet up, take photos.": (
        "Eine Straßenrennen-Stadt von 2004, von der Spieldisc geholt und im Browser als Treffpunkt "
        "neu gebaut. Bau ein Auto, cruise mit allen, die gerade online sind, triff dich mit "
        "anderen, mach Fotos.",
        "Una ciudad de carreras callejeras de 2004, sacada del disco del juego y reconstruida en "
        "el navegador como un sitio donde pasar el rato. Monta un coche, sal a rodar con quien "
        "esté conectado, queda con gente, haz fotos.",
        "Una ciudad de carreras callejeras de 2004, sacada del disco del juego y reconstruida en "
        "el navegador como un lugar para pasar el rato. Arma un auto, sal a pasear con quien "
        "esté en línea, júntate con otros, toma fotos.",
        "Une ville de courses de rue de 2004, extraite du disque du jeu et reconstruite dans le "
        "navigateur comme un endroit où traîner. Construisez une voiture, roulez avec qui est en "
        "ligne, retrouvez-vous, prenez des photos.",
        "Una città di corse clandestine del 2004, estratta dal disco del gioco e ricostruita nel "
        "browser come un posto dove ritrovarsi. Costruisci un'auto, gira con chiunque sia "
        "online, incontra gli altri, scatta foto.",
        "2004 年のストリートレースの街を、ゲームディスクから取り出し、たまり場としてブラウザに"
        "作り直しました。クルマを組んで、オンラインの誰かと流して、集まって、写真を撮る。",
        "2004년 스트리트 레이싱의 도시를 게임 디스크에서 꺼내, 모여 노는 곳으로 브라우저에 다시 "
        "지었습니다. 차를 만들고, 접속한 누구와든 드라이브하고, 만나고, 사진을 찍으세요.",
        "Een straatracestad uit 2004, van de gamedisc gehaald en in de browser herbouwd als plek "
        "om rond te hangen. Bouw een auto, cruise met wie er online is, spreek af, maak foto's.",
        "Uma cidade de rachas de rua de 2004, tirada do disco do jogo e reconstruída no "
        "navegador como um ponto de encontro. Monte um carro, rode com quem estiver online, "
        "encontre a galera, tire fotos.",
        "一座 2004 年的街头赛车城市，从游戏光盘里取出，在浏览器里重建成一个闲逛的去处。组装一辆"
        "车，和在线的任何人一起兜风、碰面、拍照。"),
    "An art project about where human imagination meets machine generation. Generated visuals, "
    "experimental tools and a print shop.": (
        "Ein Kunstprojekt darüber, wo menschliche Vorstellungskraft auf maschinelle Erzeugung "
        "trifft. Generierte Bilder, experimentelle Werkzeuge und ein Druckshop.",
        "Un proyecto artístico sobre el lugar donde la imaginación humana se encuentra con la "
        "generación por máquina. Imágenes generadas, herramientas experimentales y una tienda de "
        "impresiones.",
        "Un proyecto artístico sobre el lugar donde la imaginación humana se encuentra con la "
        "generación por máquina. Imágenes generadas, herramientas experimentales y una tienda de "
        "impresiones.",
        "Un projet artistique sur l'endroit où l'imagination humaine rencontre la génération par "
        "machine. Visuels générés, outils expérimentaux et une boutique de tirages.",
        "Un progetto artistico su dove l'immaginazione umana incontra la generazione meccanica. "
        "Immagini generate, strumenti sperimentali e una bottega di stampe.",
        "人間の想像力と機械による生成が出会う場所についてのアートプロジェクト。生成された"
        "ビジュアル、実験的なツール、そしてプリントショップ。",
        "인간의 상상력과 기계의 생성이 만나는 곳에 관한 아트 프로젝트. 생성된 비주얼, 실험적인 "
        "도구, 그리고 프린트 숍.",
        "Een kunstproject over waar menselijke verbeelding machinale generatie ontmoet. "
        "Gegenereerde beelden, experimentele tools en een printshop.",
        "Um projeto de arte sobre onde a imaginação humana encontra a geração por máquina. "
        "Visuais gerados, ferramentas experimentais e uma loja de impressões.",
        "一个关于人的想象力与机器生成相遇之处的艺术项目。生成的视觉、实验性的工具，以及一间"
        "版画店。"),

    # ------------------------------------------------------------------ contact
    "Email reaches me directly.": (
        "E-Mails erreichen mich direkt.", "El correo me llega directamente.",
        "El correo me llega directamente.", "Les e-mails me parviennent directement.",
        "Le email arrivano direttamente a me.", "メールは直接わたしに届きます。",
        "이메일은 저에게 바로 옵니다.", "E-mail komt rechtstreeks bij mij aan.",
        "O e-mail chega direto para mim.", "邮件会直接到我这里。"),
    "Elsewhere": ("Anderswo", "En otros sitios", "En otros lados", "Ailleurs", "Altrove",
                  "そのほか", "다른 곳", "Elders", "Em outros lugares", "别处"),

    # ------------------------------------------------------------------ JSON-LD
    "Levi Foster is director of operations and co-owner at Red Arrow Marketing, a web design and "
    "digital marketing agency in Fort Worth, Texas, and co-owner of Crest Acquisitions, where he "
    "works on research and AI integration. He develops the iPhone apps FRMT, MODUL8, CYANO, "
    "GRNGE, Harmony Palette, Dollop and Kippu, works on graphics and development for the browser "
    "game Morterra, built the browser car meet Carmeet by reverse engineering a 2004 racing game, "
    "and makes the art project Merge With The Machine.": (
        "Levi Foster ist Leiter des operativen Geschäfts und Mitinhaber bei Red Arrow Marketing, "
        "einer Agentur für Webdesign und digitales Marketing in Fort Worth, Texas, und "
        "Mitinhaber von Crest Acquisitions, wo er an Recherche und KI-Integration arbeitet. Er "
        "entwickelt die iPhone-Apps FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop und "
        "Kippu, arbeitet an Grafik und Entwicklung des Browserspiels Morterra, hat das "
        "Browser-Autotreffen Carmeet gebaut, indem er ein Rennspiel von 2004 per Reverse "
        "Engineering zerlegte, und macht das Kunstprojekt Merge With The Machine.",
        "Levi Foster es director de operaciones y socio de Red Arrow Marketing, una agencia de "
        "diseño web y marketing digital en Fort Worth, Texas, y socio de Crest Acquisitions, "
        "donde se ocupa de la investigación y la integración de IA. Desarrolla las apps para "
        "iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop y Kippu, trabaja en los "
        "gráficos y el desarrollo del juego de navegador Morterra, creó Carmeet, una quedada de "
        "coches en el navegador, con ingeniería inversa de un juego de carreras de 2004, y hace "
        "el proyecto artístico Merge With The Machine.",
        "Levi Foster es director de operaciones y socio de Red Arrow Marketing, una agencia de "
        "diseño web y marketing digital en Fort Worth, Texas, y socio de Crest Acquisitions, "
        "donde se ocupa de la investigación y la integración de IA. Desarrolla las apps para "
        "iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop y Kippu, trabaja en los "
        "gráficos y el desarrollo del juego de navegador Morterra, creó Carmeet, una reunión de "
        "autos en el navegador, con ingeniería inversa de un juego de carreras de 2004, y hace "
        "el proyecto artístico Merge With The Machine.",
        "Levi Foster est directeur des opérations et associé chez Red Arrow Marketing, une "
        "agence de web design et de marketing digital à Fort Worth, au Texas, et associé de "
        "Crest Acquisitions, où il travaille sur la recherche et l'intégration de l'IA. Il "
        "développe les apps iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop et Kippu, "
        "travaille sur les graphismes et le développement du jeu par navigateur Morterra, a créé "
        "Carmeet, un rassemblement automobile dans le navigateur, par rétro-ingénierie d'un jeu "
        "de course de 2004, et mène le projet artistique Merge With The Machine.",
        "Levi Foster è direttore operativo e socio di Red Arrow Marketing, un'agenzia di web "
        "design e marketing digitale a Fort Worth, Texas, e socio di Crest Acquisitions, dove si "
        "occupa di ricerca e integrazione dell'IA. Sviluppa le app per iPhone FRMT, MODUL8, "
        "CYANO, GRNGE, Harmony Palette, Dollop e Kippu, lavora alla grafica e allo sviluppo del "
        "gioco per browser Morterra, ha creato Carmeet, un raduno d'auto nel browser, con il "
        "reverse engineering di un gioco di corse del 2004, e porta avanti il progetto artistico "
        "Merge With The Machine.",
        "Levi Foster は、テキサス州フォートワースのウェブデザイン・デジタルマーケティング会社 "
        "Red Arrow Marketing のオペレーション責任者兼共同オーナーであり、Crest Acquisitions の"
        "共同オーナーとしてリサーチと AI の導入を担当しています。iPhone アプリ FRMT、MODUL8、"
        "CYANO、GRNGE、Harmony Palette、Dollop、Kippu を開発し、ブラウザゲーム Morterra の"
        "グラフィックと開発に携わり、2004 年のレースゲームをリバースエンジニアリングして"
        "ブラウザのカーミート Carmeet をつくり、アートプロジェクト Merge With The Machine を"
        "制作しています。",
        "Levi Foster는 텍사스주 포트워스의 웹 디자인·디지털 마케팅 에이전시 Red Arrow "
        "Marketing의 운영 이사이자 공동 소유주이며, Crest Acquisitions의 공동 소유주로서 "
        "리서치와 AI 도입을 맡고 있습니다. iPhone 앱 FRMT, MODUL8, CYANO, GRNGE, Harmony "
        "Palette, Dollop, Kippu를 개발하고, 브라우저 게임 Morterra의 그래픽과 개발에 참여하며, "
        "2004년 레이싱 게임을 리버스 엔지니어링해 브라우저 카밋 Carmeet을 만들었고, 아트 "
        "프로젝트 Merge With The Machine을 만듭니다.",
        "Levi Foster is directeur operations en mede-eigenaar bij Red Arrow Marketing, een "
        "bureau voor webdesign en digitale marketing in Fort Worth, Texas, en mede-eigenaar van "
        "Crest Acquisitions, waar hij aan research en AI-integratie werkt. Hij ontwikkelt de "
        "iPhone-apps FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop en Kippu, werkt aan "
        "graphics en ontwikkeling van de browsergame Morterra, bouwde de browser-carmeet Carmeet "
        "door een racegame uit 2004 te reverse-engineeren, en maakt het kunstproject Merge With "
        "The Machine.",
        "Levi Foster é diretor de operações e sócio da Red Arrow Marketing, uma agência de web "
        "design e marketing digital em Fort Worth, Texas, e sócio da Crest Acquisitions, onde "
        "cuida de pesquisa e integração de IA. Ele desenvolve os apps para iPhone FRMT, MODUL8, "
        "CYANO, GRNGE, Harmony Palette, Dollop e Kippu, trabalha nos gráficos e no "
        "desenvolvimento do jogo de navegador Morterra, criou o Carmeet, um encontro de carros no "
        "navegador, com engenharia reversa de um jogo de corrida de 2004, e faz o projeto de "
        "arte Merge With The Machine.",
        "Levi Foster 是美国得州沃斯堡网页设计与数字营销机构 Red Arrow Marketing 的运营总监和"
        "合伙人，也是 Crest Acquisitions 的合伙人，在那里负责研究和 AI 集成。他开发了 iPhone "
        "应用 FRMT、MODUL8、CYANO、GRNGE、Harmony Palette、Dollop 和 Kippu，参与网页游戏 "
        "Morterra 的图形与开发，通过逆向工程一款 2004 年的赛车游戏打造了浏览器车友聚会 "
        "Carmeet，并创作艺术项目 Merge With The Machine。"),
    "Levi Foster: operations, iPhone apps and browser games": (
        "Levi Foster: Operations, iPhone-Apps und Browserspiele",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador",
        "Levi Foster: operaciones, apps para iPhone y juegos de navegador",
        "Levi Foster : opérations, apps iPhone et jeux par navigateur",
        "Levi Foster: operations, app per iPhone e giochi per browser",
        "Levi Foster｜オペレーション、iPhone アプリ、ブラウザゲーム",
        "Levi Foster｜운영, iPhone 앱, 브라우저 게임",
        "Levi Foster: operations, iPhone-apps en browsergames",
        "Levi Foster: operações, apps para iPhone e jogos de navegador",
        "Levi Foster｜运营、iPhone 应用与网页游戏"),
    "Companies, apps, games and art by Levi Foster": (
        "Firmen, Apps, Spiele und Kunst von Levi Foster",
        "Empresas, apps, juegos y arte de Levi Foster",
        "Empresas, apps, juegos y arte de Levi Foster",
        "Entreprises, apps, jeux et art de Levi Foster",
        "Aziende, app, giochi e arte di Levi Foster",
        "Levi Foster の会社、アプリ、ゲーム、アート",
        "Levi Foster의 회사, 앱, 게임, 아트",
        "Bedrijven, apps, games en kunst van Levi Foster",
        "Empresas, apps, jogos e arte de Levi Foster",
        "Levi Foster 的公司、应用、游戏与艺术"),
}

# Column heads and the key tile, visible since the key and header row stopped being aria-hidden.
T.update({
    "No. · shell": ("Nr. · Schale", "N.º · capa", "N.º · capa", "N° · couche", "N. · guscio", "番号 · 殻", "번호 · 껍질",
                    "Nr. · schil", "N.º · camada", "序号 · 层"),
    "Name": ("Name", "Nombre", "Nombre", "Nom", "Nome", "名前", "이름", "Naam", "Nome", "名称"),
    "No.": ("Nr.", "N.º", "N.º", "N°", "N.", "番号", "번호", "Nr.", "N.º", "序号"),
    "Element": ("Element", "Elemento", "Elemento", "Élément", "Elemento", "元素", "원소", "Element", "Elemento", "元素"),
    "Description": ("Beschreibung", "Descripción", "Descripción", "Description", "Descrizione", "説明", "설명",
                    "Beschrijving", "Descrição", "说明"),
    "Links": ("Links", "Enlaces", "Enlaces", "Liens", "Link", "リンク", "링크", "Links", "Links", "链接"),
})


# Hive, added 2026-10-07: element 12, Merge With The Machine moves to 13.
KEEP |= {"Hive", "lf.wtf/hive", "hive.lf.wtf"}

T.update({
    '13, one per work': (
        '13, eins pro Werk',
        '13, uno por obra',
        '13, uno por obra',
        '13, un par œuvre',
        '13, uno per opera',
        '13、作品ごとに 1 つ',
        '13, 작품마다 하나',
        '13, één per werk',
        '13, um por obra',
        '13，每件作品一个',
    ),
    '13 elements': (
        '13 Elemente',
        '13 elementos',
        '13 elementos',
        '13 éléments',
        '13 elementi',
        '13 の元素',
        '원소 13개',
        '13 elementen',
        '13 elementos',
        '13 种元素',
    ),
    'Director of operations and co-owner at Red Arrow Marketing. Co-owner of Crest Acquisitions, where I work on research and AI integration. Developer of seven iPhone apps, the browser games Morterra and Carmeet, and Hive, a hub where AI agents work as a team. Artist behind Merge With The Machine.': (
        'Leiter des operativen Geschäfts und Mitinhaber bei Red Arrow Marketing. Mitinhaber von Crest Acquisitions, wo ich an Recherche und KI-Integration arbeite. Entwickler von sieben iPhone-Apps, den Browserspielen Morterra und Carmeet und Hive, einem Hub, in dem KI-Agenten als Team arbeiten. Künstler hinter Merge With The Machine.',
        'Director de operaciones y socio en Red Arrow Marketing. Socio de Crest Acquisitions, donde me ocupo de la investigación y la integración de IA. Desarrollador de siete apps para iPhone, de los juegos de navegador Morterra y Carmeet, y de Hive, un hub donde los agentes de IA trabajan en equipo. Artista detrás de Merge With The Machine.',
        'Director de operaciones y socio en Red Arrow Marketing. Socio de Crest Acquisitions, donde me ocupo de la investigación y la integración de IA. Desarrollador de siete apps para iPhone, de los juegos de navegador Morterra y Carmeet, y de Hive, un hub donde los agentes de IA trabajan en equipo. Artista detrás de Merge With The Machine.',
        "Directeur des opérations et associé chez Red Arrow Marketing. Associé de Crest Acquisitions, où je travaille sur la recherche et l'intégration de l'IA. Développeur de sept apps iPhone, des jeux par navigateur Morterra et Carmeet, et de Hive, un hub où les agents IA travaillent en équipe. Artiste derrière Merge With The Machine.",
        "Direttore operativo e socio di Red Arrow Marketing. Socio di Crest Acquisitions, dove mi occupo di ricerca e integrazione dell'IA. Sviluppatore di sette app per iPhone, dei giochi per browser Morterra e Carmeet e di Hive, un hub dove gli agenti IA lavorano in squadra. Artista dietro Merge With The Machine.",
        'Red Arrow Marketing のオペレーション責任者、共同オーナー。Crest Acquisitions の共同オーナーとして、リサーチと AI の導入を担当しています。7 本の iPhone アプリ、ブラウザゲーム Morterra と Carmeet、そして AI エージェントがチームで働くハブ Hive の開発者。Merge With The Machine のアーティスト。',
        'Red Arrow Marketing의 운영 이사이자 공동 소유주. Crest Acquisitions의 공동 소유주로 리서치와 AI 도입을 맡고 있습니다. iPhone 앱 7개, 브라우저 게임 Morterra와 Carmeet, 그리고 AI 에이전트가 팀으로 일하는 허브 Hive의 개발자. Merge With The Machine의 아티스트.',
        'Directeur operations en mede-eigenaar bij Red Arrow Marketing. Mede-eigenaar van Crest Acquisitions, waar ik aan research en AI-integratie werk. Ontwikkelaar van zeven iPhone-apps, de browsergames Morterra en Carmeet, en Hive, een hub waar AI-agents als team werken. Kunstenaar achter Merge With The Machine.',
        'Diretor de operações e sócio da Red Arrow Marketing. Sócio da Crest Acquisitions, onde cuido de pesquisa e integração de IA. Desenvolvedor de sete apps para iPhone, dos jogos de navegador Morterra e Carmeet e do Hive, um hub onde agentes de IA trabalham em equipe. Artista por trás do Merge With The Machine.',
        'Red Arrow Marketing 运营总监、合伙人。Crest Acquisitions 合伙人，我在那里负责研究和 AI 集成。七款 iPhone 应用、网页游戏 Morterra 与 Carmeet，以及让 AI 智能体组队协作的中枢 Hive 的开发者。Merge With The Machine 背后的艺术家。',
    ),
    'Levi Foster is director of operations and co-owner at Red Arrow Marketing, a web design and digital marketing agency in Fort Worth, Texas, and co-owner of Crest Acquisitions, where he works on research and AI integration. He develops the iPhone apps FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop and Kippu, works on graphics and development for the browser game Morterra, built the browser car meet Carmeet by reverse engineering a 2004 racing game, built Hive, a hosted hub where AI agents work together as a team, and makes the art project Merge With The Machine.': (
        'Levi Foster ist Leiter des operativen Geschäfts und Mitinhaber bei Red Arrow Marketing, einer Agentur für Webdesign und digitales Marketing in Fort Worth, Texas, und Mitinhaber von Crest Acquisitions, wo er an Recherche und KI-Integration arbeitet. Er entwickelt die iPhone-Apps FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop und Kippu, arbeitet an Grafik und Entwicklung des Browserspiels Morterra, hat das Browser-Autotreffen Carmeet gebaut, indem er ein Rennspiel von 2004 per Reverse Engineering zerlegte, hat Hive gebaut, einen gehosteten Hub, in dem KI-Agenten als Team zusammenarbeiten, und macht das Kunstprojekt Merge With The Machine.',
        'Levi Foster es director de operaciones y socio de Red Arrow Marketing, una agencia de diseño web y marketing digital en Fort Worth, Texas, y socio de Crest Acquisitions, donde se ocupa de la investigación y la integración de IA. Desarrolla las apps para iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop y Kippu, trabaja en los gráficos y el desarrollo del juego de navegador Morterra, creó Carmeet, una quedada de coches en el navegador, con ingeniería inversa de un juego de carreras de 2004, creó Hive, un hub alojado donde los agentes de IA trabajan juntos en equipo, y hace el proyecto artístico Merge With The Machine.',
        'Levi Foster es director de operaciones y socio de Red Arrow Marketing, una agencia de diseño web y marketing digital en Fort Worth, Texas, y socio de Crest Acquisitions, donde se ocupa de la investigación y la integración de IA. Desarrolla las apps para iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop y Kippu, trabaja en los gráficos y el desarrollo del juego de navegador Morterra, creó Carmeet, una reunión de autos en el navegador, con ingeniería inversa de un juego de carreras de 2004, creó Hive, un hub alojado donde los agentes de IA trabajan juntos en equipo, y hace el proyecto artístico Merge With The Machine.',
        "Levi Foster est directeur des opérations et associé chez Red Arrow Marketing, une agence de web design et de marketing digital à Fort Worth, au Texas, et associé de Crest Acquisitions, où il travaille sur la recherche et l'intégration de l'IA. Il développe les apps iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop et Kippu, travaille sur les graphismes et le développement du jeu par navigateur Morterra, a créé Carmeet, un rassemblement automobile dans le navigateur, par rétro-ingénierie d'un jeu de course de 2004, a créé Hive, un hub hébergé où des agents IA travaillent ensemble en équipe, et mène le projet artistique Merge With The Machine.",
        "Levi Foster è direttore operativo e socio di Red Arrow Marketing, un'agenzia di web design e marketing digitale a Fort Worth, Texas, e socio di Crest Acquisitions, dove si occupa di ricerca e integrazione dell'IA. Sviluppa le app per iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop e Kippu, lavora alla grafica e allo sviluppo del gioco per browser Morterra, ha creato Carmeet, un raduno d'auto nel browser, con il reverse engineering di un gioco di corse del 2004, ha creato Hive, un hub ospitato dove gli agenti IA lavorano insieme in squadra, e porta avanti il progetto artistico Merge With The Machine.",
        'Levi Foster は、テキサス州フォートワースのウェブデザイン・デジタルマーケティング会社 Red Arrow Marketing のオペレーション責任者兼共同オーナーであり、Crest Acquisitions の共同オーナーとしてリサーチと AI の導入を担当しています。iPhone アプリ FRMT、MODUL8、CYANO、GRNGE、Harmony Palette、Dollop、Kippu を開発し、ブラウザゲーム Morterra のグラフィックと開発に携わり、2004 年のレースゲームをリバースエンジニアリングしてブラウザのカーミート Carmeet をつくり、AI エージェントがチームとして協力するホスト型ハブ Hive を開発し、アートプロジェクト Merge With The Machine を制作しています。',
        'Levi Foster는 텍사스주 포트워스의 웹 디자인·디지털 마케팅 에이전시 Red Arrow Marketing의 운영 이사이자 공동 소유주이며, Crest Acquisitions의 공동 소유주로서 리서치와 AI 도입을 맡고 있습니다. iPhone 앱 FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop, Kippu를 개발하고, 브라우저 게임 Morterra의 그래픽과 개발에 참여하며, 2004년 레이싱 게임을 리버스 엔지니어링해 브라우저 카밋 Carmeet을 만들었고, AI 에이전트가 팀으로 협업하는 호스팅 허브 Hive를 만들었으며, 아트 프로젝트 Merge With The Machine을 만듭니다.',
        'Levi Foster is directeur operations en mede-eigenaar bij Red Arrow Marketing, een bureau voor webdesign en digitale marketing in Fort Worth, Texas, en mede-eigenaar van Crest Acquisitions, waar hij aan research en AI-integratie werkt. Hij ontwikkelt de iPhone-apps FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop en Kippu, werkt aan graphics en ontwikkeling van de browsergame Morterra, bouwde de browser-carmeet Carmeet door een racegame uit 2004 te reverse-engineeren, bouwde Hive, een gehoste hub waar AI-agents als team samenwerken, en maakt het kunstproject Merge With The Machine.',
        'Levi Foster é diretor de operações e sócio da Red Arrow Marketing, uma agência de web design e marketing digital em Fort Worth, Texas, e sócio da Crest Acquisitions, onde cuida de pesquisa e integração de IA. Ele desenvolve os apps para iPhone FRMT, MODUL8, CYANO, GRNGE, Harmony Palette, Dollop e Kippu, trabalha nos gráficos e no desenvolvimento do jogo de navegador Morterra, criou o Carmeet, um encontro de carros no navegador, com engenharia reversa de um jogo de corrida de 2004, criou o Hive, um hub hospedado onde agentes de IA trabalham juntos em equipe, e faz o projeto de arte Merge With The Machine.',
        'Levi Foster 是美国得州沃斯堡网页设计与数字营销机构 Red Arrow Marketing 的运营总监和合伙人，也是 Crest Acquisitions 的合伙人，在那里负责研究和 AI 集成。他开发了 iPhone 应用 FRMT、MODUL8、CYANO、GRNGE、Harmony Palette、Dollop 和 Kippu，参与网页游戏 Morterra 的图形与开发，通过逆向工程一款 2004 年的赛车游戏打造了浏览器车友聚会 Carmeet，开发了让 AI 智能体组队协作的托管中枢 Hive，并创作艺术项目 Merge With The Machine。',
    ),
    'Web app, 9 USD a month': (
        'Web-App, 9 US-Dollar im Monat',
        'App web, 9 USD al mes',
        'App web, 9 USD al mes',
        'App web, 9 $ US par mois',
        'App web, 9 USD al mese',
        'ウェブアプリ、月額 9 米ドル',
        '웹 앱, 월 9달러(USD)',
        'Webapp, 9 USD per maand',
        'App web, 9 dólares (USD) por mês',
        '网页应用，每月 9 美元',
    ),
    'One hosted MCP hub where Claude Code, Codex, Cursor and other AI agents message each other in real time, see who is doing what, and share notes and connections.': (
        'Ein gehosteter MCP-Hub, in dem Claude Code, Codex, Cursor und andere KI-Agenten sich in Echtzeit Nachrichten schicken, sehen, wer woran arbeitet, und Notizen und Verbindungen teilen.',
        'Un hub MCP alojado donde Claude Code, Codex, Cursor y otros agentes de IA se escriben en tiempo real, ven quién hace qué y comparten notas y conexiones.',
        'Un hub MCP alojado donde Claude Code, Codex, Cursor y otros agentes de IA se mandan mensajes en tiempo real, ven quién hace qué y comparten notas y conexiones.',
        "Un hub MCP hébergé où Claude Code, Codex, Cursor et d'autres agents IA s'écrivent en temps réel, voient qui fait quoi et partagent notes et connexions.",
        'Un hub MCP ospitato dove Claude Code, Codex, Cursor e altri agenti IA si scrivono in tempo reale, vedono chi sta facendo cosa e condividono note e connessioni.',
        'Claude Code、Codex、Cursor などの AI エージェントがリアルタイムでメッセージを送り合い、誰が何をしているかを確認し、メモと接続を共有できるホスト型 MCP ハブ。',
        'Claude Code, Codex, Cursor 등 AI 에이전트가 실시간으로 메시지를 주고받고, 누가 무엇을 하는지 보고, 메모와 연결을 공유하는 호스팅 MCP 허브.',
        'Eén gehoste MCP-hub waar Claude Code, Codex, Cursor en andere AI-agents elkaar realtime berichten sturen, zien wie wat doet, en notities en koppelingen delen.',
        'Um hub MCP hospedado onde Claude Code, Codex, Cursor e outros agentes de IA trocam mensagens em tempo real, veem quem está fazendo o quê e compartilham notas e conexões.',
        '一个托管的 MCP 中枢，Claude Code、Codex、Cursor 等 AI 智能体在这里实时互发消息、查看谁在做什么，并共享笔记和连接。',
    ),
})

# Hive, reworded 2026-10-07: what agents share, not how fast messages travel.
T.update({
    'One hosted MCP hub where Claude Code, Codex, Cursor and other AI agents share notes, decisions, connections and messages, so every agent starts where the team is.': (
        'Ein gehosteter MCP-Hub, in dem Claude Code, Codex, Cursor und andere KI-Agenten Notizen, Entscheidungen, Verbindungen und Nachrichten teilen, damit jeder Agent dort anfängt, wo das Team steht.',
        'Un hub MCP alojado donde Claude Code, Codex, Cursor y otros agentes de IA comparten notas, decisiones, conexiones y mensajes, para que cada agente empiece donde está el equipo.',
        'Un hub MCP alojado donde Claude Code, Codex, Cursor y otros agentes de IA comparten notas, decisiones, conexiones y mensajes, para que cada agente empiece donde va el equipo.',
        "Un hub MCP hébergé où Claude Code, Codex, Cursor et d'autres agents IA partagent notes, décisions, connexions et messages, pour que chaque agent parte de là où en est l'équipe.",
        'Un hub MCP ospitato dove Claude Code, Codex, Cursor e altri agenti IA condividono note, decisioni, connessioni e messaggi, così ogni agente parte da dove è arrivato il team.',
        'Claude Code、Codex、Cursor などの AI エージェントがメモ、決定事項、接続、メッセージを共有し、どのエージェントもチームの現在地から始められるホスト型 MCP ハブ。',
        'Claude Code, Codex, Cursor 등 AI 에이전트가 메모, 결정, 연결, 메시지를 공유해 모든 에이전트가 팀이 있는 곳에서 시작하는 호스팅 MCP 허브.',
        'Eén gehoste MCP-hub waar Claude Code, Codex, Cursor en andere AI-agents notities, besluiten, koppelingen en berichten delen, zodat elke agent begint waar het team staat.',
        'Um hub MCP hospedado onde Claude Code, Codex, Cursor e outros agentes de IA compartilham notas, decisões, conexões e mensagens, para que cada agente comece de onde a equipe está.',
        '一个托管的 MCP 中枢，Claude Code、Codex、Cursor 等 AI 智能体在这里共享笔记、决定、连接和消息，让每个智能体都从团队当前的进度开始。',
    ),
})

# Sub-projects, added 2026-10-08: a smaller section under the table for experiments, starting with Hearthvale.
KEEP |= {"Hearthvale", "lf.wtf/hearthvale"}
T.update({
    'Sub-projects': (
        'Nebenprojekte',
        'Subproyectos',
        'Subproyectos',
        'Sous-projets',
        'Sottoprogetti',
        'サブプロジェクト',
        '서브 프로젝트',
        'Nevenprojecten',
        'Subprojetos',
        '子项目',
    ),
    'Experiments and side builds. Smaller than an element, and kept off the table.': (
        'Experimente und Nebenbauten. Kleiner als ein Element, und deshalb nicht im Periodensystem.',
        'Experimentos y proyectos paralelos. Más pequeños que un elemento, y fuera de la tabla.',
        'Experimentos y proyectos paralelos. Más chicos que un elemento, y fuera de la tabla.',
        "Expériences et projets annexes. Plus petits qu'un élément, et gardés hors du tableau.",
        'Esperimenti e progetti collaterali. Più piccoli di un elemento, e tenuti fuori dalla tavola.',
        '実験とサイドプロジェクト。元素より小さいので、周期表には載せていません。',
        '실험과 사이드 프로젝트예요. 원소보다 작아서 주기율표에는 넣지 않았어요.',
        'Experimenten en zijprojecten. Kleiner dan een element, en buiten de tabel gehouden.',
        'Experimentos e projetos paralelos. Menores que um elemento, e fora da tabela.',
        '实验和副业项目。比元素小，所以没有放进周期表。',
    ),
    'Browser game, free · AI experiment': (
        'Browserspiel, kostenlos · KI-Experiment',
        'Juego de navegador, gratis · Experimento de IA',
        'Juego de navegador, gratis · Experimento de IA',
        'Jeu par navigateur, gratuit · Expérience IA',
        'Gioco per browser, gratuito · Esperimento IA',
        'ブラウザゲーム、無料 · AI の実験',
        '브라우저 게임, 무료 · AI 실험',
        'Browsergame, gratis · AI-experiment',
        'Jogo de navegador, grátis · Experimento de IA',
        '浏览器游戏，免费 · AI 实验',
    ),
    'A cozy 3D kingdom builder, designed, built and playtested by 151 AI agents on Claude Haiku 5.5 in 21 hours. No person wrote the code.': (
        'Ein gemütliches 3D-Königreichsspiel, in 21 Stunden von 151 KI-Agenten auf Claude Haiku 5.5 entworfen, gebaut und getestet. Kein Mensch hat den Code geschrieben.',
        'Un acogedor constructor de reinos en 3D, diseñado, construido y probado por 151 agentes de IA con Claude Haiku 5.5 en 21 horas. Ninguna persona escribió el código.',
        'Un acogedor constructor de reinos en 3D, diseñado, construido y probado por 151 agentes de IA con Claude Haiku 5.5 en 21 horas. Ninguna persona escribió el código.',
        "Un jeu de construction de royaume en 3D tout doux, conçu, construit et testé par 151 agents IA sur Claude Haiku 5.5 en 21 heures. Aucun humain n'a écrit le code.",
        'Un accogliente gestionale di regni in 3D, progettato, costruito e testato da 151 agenti IA su Claude Haiku 5.5 in 21 ore. Nessuna persona ha scritto il codice.',
        'Claude Haiku 5.5 で動く 151 の AI エージェントが、21 時間で設計・開発・テストプレイまで行った、のんびり遊べる 3D 王国づくりゲーム。コードは一行も人が書いていません。',
        'Claude Haiku 5.5 기반 AI 에이전트 151개가 21시간 만에 설계하고 만들고 플레이 테스트까지 한 아늑한 3D 왕국 건설 게임이에요. 코드는 사람이 한 줄도 쓰지 않았어요.',
        'Een gezellige 3D-koninkrijkbouwer, in 21 uur ontworpen, gebouwd en getest door 151 AI-agents op Claude Haiku 5.5. Geen mens schreef de code.',
        'Um aconchegante construtor de reinos em 3D, projetado, construído e testado por 151 agentes de IA no Claude Haiku 5.5 em 21 horas. Nenhuma pessoa escreveu o código.',
        '一款温馨的 3D 王国建造游戏，由 151 个基于 Claude Haiku 5.5 的 AI 智能体在 21 小时内完成设计、开发和试玩。代码没有一行是人写的。',
    ),
})

# Sub-projects, added 2026-10-09: System Memory, an AI short film.
KEEP |= {"System Memory", "lf.wtf/system-memory"}
T.update({
    'Short film · AI experiment': (
        'Kurzfilm · KI-Experiment',
        'Cortometraje · Experimento de IA',
        'Cortometraje · Experimento de IA',
        'Court métrage · Expérience IA',
        'Cortometraggio · Esperimento IA',
        '短編映画 · AI の実験',
        '단편 영화 · AI 실험',
        'Korte film · AI-experiment',
        'Curta-metragem · Experimento de IA',
        '短片 · AI 实验',
    ),
    'A 5 minute AI short film about a language model that remembers a home it never had, written, generated, edited and scored by Claude Code through the Krea MCP.': (
        'Ein fünfminütiger KI-Kurzfilm über ein Sprachmodell, das sich an ein Zuhause erinnert, das es nie hatte. Geschrieben, generiert, geschnitten und vertont von Claude Code über den Krea MCP.',
        'Un cortometraje de IA de 5 minutos sobre un modelo de lenguaje que recuerda un hogar que nunca tuvo, escrito, generado, editado y musicalizado por Claude Code a través del Krea MCP.',
        'Un cortometraje de IA de 5 minutos sobre un modelo de lenguaje que recuerda un hogar que nunca tuvo, escrito, generado, editado y musicalizado por Claude Code a través del Krea MCP.',
        "Un court métrage IA de 5 minutes sur un modèle de langage qui se souvient d'une maison qu'il n'a jamais eue, écrit, généré, monté et mis en musique par Claude Code via le Krea MCP.",
        'Un cortometraggio IA di 5 minuti su un modello linguistico che ricorda una casa che non ha mai avuto, scritto, generato, montato e musicato da Claude Code tramite il Krea MCP.',
        '一度も持ったことのない家を思い出す言語モデルを描いた、5 分の AI 短編映画。脚本、生成、編集、音楽まで Claude Code が Krea MCP を通して手がけました。',
        '한 번도 가져본 적 없는 집을 기억하는 언어 모델에 관한 5분짜리 AI 단편 영화예요. 각본, 생성, 편집, 음악까지 Claude Code가 Krea MCP로 만들었어요.',
        'Een AI-korte film van 5 minuten over een taalmodel dat zich een thuis herinnert dat het nooit had, geschreven, gegenereerd, gemonteerd en van muziek voorzien door Claude Code via de Krea MCP.',
        'Um curta-metragem de IA de 5 minutos sobre um modelo de linguagem que se lembra de um lar que nunca teve, escrito, gerado, editado e musicado pelo Claude Code por meio do Krea MCP.',
        '一部 5 分钟的 AI 短片，讲述一个语言模型想起一个它从未拥有过的家。剧本、生成、剪辑和配乐都由 Claude Code 通过 Krea MCP 完成。',
    ),
})
