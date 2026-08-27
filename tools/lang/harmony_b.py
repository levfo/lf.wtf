"""Harmony Palette page, part B: the two wheels, the eight harmonies, accessibility.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The harmony names are the terms colour theory actually uses in each language, not calques of the
English. Where a language has a settled Bauhaus-era vocabulary it wins over a literal reading.
"""

T = {
    "two wheels, because": (
        "zwei Kreise, weil", "dos ruedas, porque", "dos ruedas, porque", "deux roues, parce que",
        "due ruote, perché", "ホイールが二つあるのは", "색상환이 둘인 이유는",
        "twee wielen, omdat", "duas rodas, porque", "两个色轮，因为"),
    "they disagree": (
        "sie sich widersprechen", "no se ponen de acuerdo", "no se ponen de acuerdo",
        "elles ne sont pas d'accord", "non sono d'accordo", "答えが食い違うから",
        "서로 답이 다르기 때문", "ze het oneens zijn", "elas discordam", "它们意见不合"),
    "Ask a screen what the opposite of red is and it says cyan. Ask a painter and they say green.\n      Both are right, and they are answering different questions: one is how light mixes, the other\n      is the wheel taught in art schools and refined by Johannes Itten at the Bauhaus.": (
        "Fragen Sie einen Bildschirm, was das Gegenteil von Rot ist, sagt er Cyan. Fragen Sie eine "
        "Malerin, sagt sie Grün. Beide haben recht und beantworten verschiedene Fragen: das eine "
        "ist, wie Licht sich mischt, das andere ist der Kreis, der an Kunsthochschulen gelehrt und "
        "von Johannes Itten am Bauhaus verfeinert wurde.",
        "Pregúntale a una pantalla cuál es el opuesto del rojo y dirá cian. Pregúntale a un pintor "
        "y dirá verde. Los dos tienen razón y están respondiendo a preguntas distintas: una es "
        "cómo se mezcla la luz, la otra es la rueda que se enseña en las escuelas de arte y que "
        "Johannes Itten refinó en la Bauhaus.",
        "Pregúntale a una pantalla cuál es el opuesto del rojo y dirá cian. Pregúntale a un pintor "
        "y dirá verde. Los dos tienen razón y están respondiendo a preguntas distintas: una es "
        "cómo se mezcla la luz, la otra es la rueda que se enseña en las escuelas de arte y que "
        "Johannes Itten refinó en la Bauhaus.",
        "Demandez à un écran quel est le contraire du rouge et il répond cyan. Demandez-le à un "
        "peintre et il répond vert. Les deux ont raison et répondent à des questions différentes : "
        "l'une porte sur la façon dont la lumière se mélange, l'autre est la roue enseignée dans "
        "les écoles d'art et affinée par Johannes Itten au Bauhaus.",
        "Chiedi a uno schermo qual è l'opposto del rosso e risponde ciano. Chiedilo a un pittore e "
        "risponde verde. Hanno ragione entrambi e stanno rispondendo a domande diverse: una "
        "riguarda come si mescola la luce, l'altra è la ruota insegnata nelle scuole d'arte e "
        "affinata da Johannes Itten al Bauhaus.",
        "画面に赤の反対は何かと尋ねればシアンと答え、画家に尋ねれば緑と答えます。どちらも正しく、"
        "答えている問いが違うのです。一方は光がどう混ざるかであり、もう一方は美術学校で教えられ、"
        "Bauhaus で Johannes Itten が磨き上げたホイールです。",
        "화면에 빨강의 반대가 무엇이냐고 물으면 사이언이라 답하고, 화가에게 물으면 초록이라 "
        "답합니다. 둘 다 맞고, 서로 다른 질문에 답하고 있을 뿐입니다. 하나는 빛이 섞이는 방식이고, "
        "다른 하나는 미술학교에서 가르치고 Johannes Itten이 Bauhaus에서 다듬은 색상환입니다.",
        "Vraag een scherm wat het tegenovergestelde van rood is en het zegt cyaan. Vraag het een "
        "schilder en die zegt groen. Beiden hebben gelijk en beantwoorden verschillende vragen: de "
        "een gaat over hoe licht mengt, de ander is het wiel dat op kunstacademies wordt "
        "onderwezen en door Johannes Itten aan het Bauhaus is verfijnd.",
        "Pergunte a uma tela qual é o oposto do vermelho e ela diz ciano. Pergunte a um pintor e "
        "ele diz verde. Os dois estão certos e estão respondendo a perguntas diferentes: uma é "
        "como a luz se mistura, a outra é a roda ensinada nas escolas de arte e refinada por "
        "Johannes Itten na Bauhaus.",
        "问屏幕红色的对面是什么，它说青色；问画家，画家说绿色。两者都对，只是在回答不同的问题："
        "一个说的是光如何相加，另一个是美术院校教授、由 Johannes Itten 在 Bauhaus 精炼过的色轮。"),
    "This matters more than it sounds. A triad that looks evenly weighted on the RGB wheel can\n      come out lopsided in RYB, and a palette built for print behaves differently from one built for\n      a screen. Harmony Palette gives you both models and lets you flip between them on the same\n      color, so you can see the disagreement instead of picking a side by accident.": (
        "Das ist wichtiger, als es klingt. Eine Triade, die auf dem RGB-Kreis gleichmäßig "
        "gewichtet aussieht, kann in RYB schief herauskommen, und eine Palette für den Druck "
        "verhält sich anders als eine für den Bildschirm. Harmony Palette gibt Ihnen beide Modelle "
        "und lässt Sie bei derselben Farbe zwischen ihnen umschalten, damit Sie den Widerspruch "
        "sehen, statt sich versehentlich für eine Seite zu entscheiden.",
        "Esto importa más de lo que parece. Una tríada que se ve equilibrada en la rueda RGB puede "
        "salir desequilibrada en RYB, y una paleta pensada para imprenta se comporta de otro modo "
        "que una pensada para pantalla. Harmony Palette te da los dos modelos y te deja alternar "
        "entre ellos sobre el mismo color, para que veas el desacuerdo en vez de elegir bando sin "
        "querer.",
        "Esto importa más de lo que parece. Una tríada que se ve equilibrada en la rueda RGB puede "
        "salir desequilibrada en RYB, y una paleta pensada para imprenta se comporta distinto que "
        "una pensada para pantalla. Harmony Palette te da los dos modelos y te deja alternar entre "
        "ellos sobre el mismo color, para que veas el desacuerdo en vez de elegir bando sin "
        "querer.",
        "Cela compte plus qu'il n'y paraît. Une triade qui semble équilibrée sur la roue RVB peut "
        "sortir bancale en RJB, et une palette conçue pour l'impression se comporte autrement "
        "qu'une palette conçue pour l'écran. Harmony Palette vous donne les deux modèles et vous "
        "laisse basculer de l'un à l'autre sur la même couleur, pour que vous voyiez le désaccord "
        "au lieu de choisir un camp par accident.",
        "Conta più di quanto sembri. Una triade che sulla ruota RGB appare equilibrata può "
        "risultare sbilanciata in RYB, e una palette pensata per la stampa si comporta diversamente "
        "da una pensata per lo schermo. Harmony Palette ti dà entrambi i modelli e ti lascia "
        "passare dall'uno all'altro sullo stesso colore, così vedi il disaccordo invece di "
        "scegliere una parte per caso.",
        "これは聞こえる以上に重要です。RGB のホイールでは均等に見える三色配色が RYB では偏って"
        "出ることがあり、印刷向けに組んだパレットは画面向けのものとは違うふるまいをします。"
        "Harmony Palette は両方のモデルを用意し、同じ色のまま切り替えられるようにしています。"
        "うっかりどちらかに肩入れするのではなく、食い違いそのものを見られます。",
        "이는 들리는 것보다 중요합니다. RGB 색상환에서 고르게 보이던 3색 배색이 RYB에서는 한쪽으로 "
        "쏠려 나올 수 있고, 인쇄를 염두에 두고 짠 팔레트는 화면용과 다르게 움직입니다. Harmony "
        "Palette는 두 모델을 모두 주고 같은 색에서 서로 오갈 수 있게 합니다. 얼떨결에 한쪽 편을 "
        "드는 대신 그 불일치를 직접 볼 수 있습니다.",
        "Dit doet er meer toe dan het klinkt. Een triade die op het RGB-wiel gelijk verdeeld lijkt, "
        "kan in RYB scheef uitpakken, en een palet voor druk gedraagt zich anders dan een palet "
        "voor het scherm. Harmony Palette geeft je beide modellen en laat je er bij dezelfde kleur "
        "tussen wisselen, zodat je het meningsverschil ziet in plaats van per ongeluk partij te "
        "kiezen.",
        "Isso importa mais do que parece. Uma tríade que na roda RGB parece equilibrada pode sair "
        "torta em RYB, e uma paleta feita para impressão se comporta de outro jeito que uma feita "
        "para tela. O Harmony Palette te dá os dois modelos e deixa você alternar entre eles na "
        "mesma cor, para você ver a discordância em vez de escolher um lado sem querer.",
        "这比听上去更要紧。在 RGB 色轮上看着分量均等的三色配色，到了 RYB 可能就偏了；"
        "为印刷配的色和为屏幕配的色表现并不一样。Harmony Palette 把两个模型都给你，"
        "并允许在同一个颜色上来回切换，"
        "这样你看到的是二者的分歧，而不是稀里糊涂站了队。"),
    "Complementary": (
        "Komplementär", "Complementario", "Complementario", "Complémentaire", "Complementare",
        "補色", "보색", "Complementair", "Complementar", "互补"),
    "Two colors facing each other. The strongest contrast available, and the easiest to overdo.": (
        "Zwei Farben, die sich gegenüberstehen. Der stärkste verfügbare Kontrast, und der am "
        "leichtesten übertriebene.",
        "Dos colores enfrentados. El contraste más fuerte que hay, y el más fácil de pasarse.",
        "Dos colores enfrentados. El contraste más fuerte que hay, y el más fácil de pasarse.",
        "Deux couleurs qui se font face. Le contraste le plus fort qui soit, et le plus facile à "
        "pousser trop loin.",
        "Due colori uno di fronte all'altro. Il contrasto più forte disponibile, e il più facile "
        "da esagerare.",
        "向かい合う二色。もっとも強いコントラストであり、もっともやりすぎやすいものでもあります。",
        "서로 마주 보는 두 색. 쓸 수 있는 가장 강한 대비이자, 가장 과해지기 쉬운 대비입니다.",
        "Twee kleuren tegenover elkaar. Het sterkste contrast dat er is, en het makkelijkst te "
        "overdrijven.",
        "Duas cores de frente uma para a outra. O contraste mais forte que existe, e o mais fácil "
        "de exagerar.",
        "彼此正对的两个颜色。可用的最强对比，也是最容易用过头的一种。"),
    "Analogous": (
        "Analog", "Análogo", "Análogo", "Analogue", "Analogo", "類似色", "유사색",
        "Analoog", "Análogo", "邻近"),
    "Three neighbours. Quiet and cohesive, which is why so much brand work lives here.": (
        "Drei Nachbarn. Ruhig und geschlossen, weshalb so viel Markenarbeit hier wohnt.",
        "Tres vecinos. Tranquilo y cohesionado, que es por lo que tanto trabajo de marca vive "
        "aquí.",
        "Tres vecinos. Tranquilo y cohesionado, que es por lo que tanto trabajo de marca vive "
        "aquí.",
        "Trois voisines. Calme et cohérent, ce qui explique que tant de travail de marque habite "
        "ici.",
        "Tre vicini. Quieto e coeso, ed è per questo che tanto lavoro di marca abita qui.",
        "隣り合う三色。静かでまとまりがあり、だからこそ多くのブランド仕事がここに住んでいます。",
        "이웃한 세 색. 조용하고 짜임새가 있어서, 그토록 많은 브랜드 작업이 여기에 삽니다.",
        "Drie buren. Rustig en samenhangend, en daarom woont zoveel merkwerk hier.",
        "Três vizinhos. Calmo e coeso, e é por isso que tanto trabalho de marca mora aqui.",
        "相邻的三个颜色。安静而整体，所以许多品牌工作都住在这里。"),
    "Monochromatic": (
        "Monochrom", "Monocromático", "Monocromático", "Monochrome", "Monocromatico",
        "単色", "단색", "Monochroom", "Monocromático", "单色"),
    "One hue, worked through its shades and tints. Hard to get wrong.": (
        "Ein Farbton, durch seine Abdunklungen und Aufhellungen durchgearbeitet. Schwer falsch zu "
        "machen.",
        "Un solo tono, trabajado a través de sus sombras y sus claros. Difícil de equivocar.",
        "Un solo tono, trabajado a través de sus sombras y sus claros. Difícil de equivocar.",
        "Une seule teinte, travaillée à travers ses nuances sombres et claires. Difficile à rater.",
        "Una sola tinta, lavorata attraverso le sue ombre e le sue schiariture. Difficile "
        "sbagliare.",
        "一つの色相を、その陰影と明度で通して扱います。外しにくい配色です。",
        "하나의 색상을 그 음영과 밝기로 끝까지 밀고 갑니다. 틀리기 어렵습니다.",
        "Eén kleurtoon, uitgewerkt in zijn schaduwen en tinten. Moeilijk fout te doen.",
        "Um só matiz, trabalhado através de seus tons escuros e claros. Difícil de errar.",
        "一个色相，贯穿它的深浅明暗。很难做错。"),
    "Triadic": (
        "Triadisch", "Triádico", "Triádico", "Triadique", "Triadico", "三色", "삼색",
        "Triadisch", "Triádico", "三等分"),
    "Three evenly spaced. Vivid and balanced at the same time, which is a rare combination.": (
        "Drei gleichmäßig verteilt. Kräftig und ausgewogen zugleich, was eine seltene Kombination "
        "ist.",
        "Tres a distancias iguales. Vivo y equilibrado a la vez, que es una combinación rara.",
        "Tres a distancias iguales. Vivo y equilibrado a la vez, que es una combinación rara.",
        "Trois à intervalles égaux. Vif et équilibré à la fois, ce qui est une combinaison rare.",
        "Tre a distanze uguali. Vivace ed equilibrato allo stesso tempo, che è una combinazione "
        "rara.",
        "等間隔の三色。鮮やかでありながら釣り合っている、まれな組み合わせです。",
        "같은 간격의 세 색. 선명하면서 동시에 균형이 잡히는, 드문 조합입니다.",
        "Drie op gelijke afstand. Levendig en in balans tegelijk, en dat is een zeldzame "
        "combinatie.",
        "Três em distâncias iguais. Vivo e equilibrado ao mesmo tempo, o que é uma combinação "
        "rara.",
        "等距的三个颜色。既鲜明又平衡，这是难得的组合。"),
    "Split-complementary": (
        "Geteilt komplementär", "Complementario dividido", "Complementario dividido",
        "Complémentaire divisé", "Complementare diviso", "分裂補色", "분할 보색",
        "Gesplitst complementair", "Complementar dividido", "分裂互补"),
    "A base plus the two neighbours of its opposite. Nearly the same punch, far less tension.": (
        "Eine Basis plus die beiden Nachbarn ihres Gegenübers. Fast dieselbe Wucht, viel weniger "
        "Spannung.",
        "Una base más los dos vecinos de su opuesto. Casi la misma fuerza, mucha menos tensión.",
        "Una base más los dos vecinos de su opuesto. Casi la misma fuerza, mucha menos tensión.",
        "Une base plus les deux voisines de son opposée. Presque la même force, bien moins de "
        "tension.",
        "Una base più i due vicini del suo opposto. Quasi la stessa forza, molta meno tensione.",
        "基準色に、その補色の両隣を足したもの。力はほぼ同じで、緊張はずっと少なくなります。",
        "기준색에 그 보색의 양옆 두 색을 더한 것. 힘은 거의 같고 긴장은 훨씬 덜합니다.",
        "Een basis plus de twee buren van haar tegenhanger. Bijna dezelfde kracht, veel minder "
        "spanning.",
        "Uma base mais os dois vizinhos do seu oposto. Quase a mesma força, bem menos tensão.",
        "一个基色，加上它对面颜色的两个邻居。冲击力几乎不变，张力小得多。"),
    "Square": (
        "Quadratisch", "Cuadrado", "Cuadrado", "Carré", "Quadrato", "矩形", "사각",
        "Vierkant", "Quadrado", "正方"),
    "rectangular": (
        "rechteckig", "rectangular", "rectangular", "rectangulaire", "rettangolare",
        "長方形", "직사각", "rechthoekig", "retangular", "矩形"),
    "Four colors, evenly or in pairs. Enough range for a whole system.": (
        "Vier Farben, gleichmäßig oder paarweise. Genug Spielraum für ein ganzes System.",
        "Cuatro colores, a distancias iguales o por parejas. Rango suficiente para un sistema "
        "entero.",
        "Cuatro colores, a distancias iguales o por parejas. Rango suficiente para un sistema "
        "entero.",
        "Quatre couleurs, à intervalles égaux ou par paires. Assez d'amplitude pour tout un "
        "système.",
        "Quattro colori, a distanze uguali o a coppie. Abbastanza ampiezza per un intero sistema.",
        "四色を、等間隔または二組で。ひとつのシステムを組むのに十分な幅があります。",
        "네 가지 색을, 같은 간격으로 또는 두 쌍으로. 체계 하나를 짜기에 충분한 폭입니다.",
        "Vier kleuren, gelijkmatig of in paren. Genoeg bereik voor een heel systeem.",
        "Quatro cores, em distâncias iguais ou aos pares. Amplitude suficiente para um sistema "
        "inteiro.",
        "四个颜色，等距或成对。够撑起一整套系统。"),
    "Compound": (
        "Zusammengesetzt", "Compuesto", "Compuesto", "Composé", "Composto", "複合", "복합",
        "Samengesteld", "Composto", "复合"),
    "Complementary and analogous relationships braided together. Complex, and worth the trouble.": (
        "Komplementäre und analoge Beziehungen ineinander geflochten. Komplex, und die Mühe wert.",
        "Relaciones complementarias y análogas trenzadas entre sí. Complejo, y merece el esfuerzo.",
        "Relaciones complementarias y análogas trenzadas entre sí. Complejo, y vale el esfuerzo.",
        "Des rapports complémentaires et analogues tressés ensemble. Complexe, et qui vaut la "
        "peine.",
        "Rapporti complementari e analoghi intrecciati insieme. Complesso, e vale la fatica.",
        "補色の関係と類似色の関係を編み合わせたもの。複雑ですが、その手間に見合います。",
        "보색 관계와 유사색 관계를 함께 엮은 것. 복잡하지만 그만한 값을 합니다.",
        "Complementaire en analoge verhoudingen door elkaar gevlochten. Complex, en de moeite "
        "waard.",
        "Relações complementares e análogas trançadas juntas. Complexo, e vale o trabalho.",
        "把互补关系与邻近关系编织在一起。复杂，但值得这份麻烦。"),
    "Eight in total": (
        "Acht insgesamt", "Ocho en total", "Ocho en total", "Huit en tout", "Otto in totale",
        "全部で 8 種類", "모두 8가지", "Acht in totaal", "Oito no total", "共 8 种"),
    "Four in the free version. The other four, and the curated library, come with Pro.": (
        "Vier in der kostenlosen Version. Die anderen vier und die kuratierte Bibliothek kommen "
        "mit Pro.",
        "Cuatro en la versión gratuita. Los otros cuatro, y la biblioteca seleccionada, vienen con "
        "Pro.",
        "Cuatro en la versión gratuita. Los otros cuatro, y la biblioteca seleccionada, vienen con "
        "Pro.",
        "Quatre dans la version gratuite. Les quatre autres, et la bibliothèque sélectionnée, "
        "viennent avec Pro.",
        "Quattro nella versione gratuita. Gli altri quattro, e la libreria selezionata, arrivano "
        "con Pro.",
        "無料版に 4 種類。残りの 4 種類と厳選ライブラリは Pro に付いてきます。",
        "무료 버전에 4가지. 나머지 4가지와 엄선된 라이브러리는 Pro와 함께 옵니다.",
        "Vier in de gratis versie. De andere vier, en de samengestelde bibliotheek, horen bij Pro.",
        "Quatro na versão gratuita. Os outros quatro, e a biblioteca selecionada, vêm com o Pro.",
        "免费版里有 4 种。另外 4 种和精选库随 Pro 提供。"),
    "the accessibility part": (
        "der Teil zur Barrierefreiheit,", "la parte de accesibilidad", "la parte de accesibilidad",
        "la partie accessibilité", "la parte sull'accessibilità", "飛ばすつもりだった",
        "그냥 건너뛰려던", "het toegankelijkheidsdeel", "a parte de acessibilidade",
        "你本打算跳过的"),
    "you were going to skip": (
        "den Sie überspringen wollten", "que ibas a saltarte", "que ibas a saltarte",
        "que vous alliez sauter", "che stavi per saltare", "アクセシビリティの話",
        "접근성 이야기", "dat je zou overslaan", "que você ia pular", "无障碍部分"),
    "Contrast checking usually lives in a separate browser tab, gets done at the end,\n      and gets skipped when the deadline moves. It is in here, next to the colors, while you are\n      still choosing them.": (
        "Kontrastprüfung wohnt sonst in einem eigenen Browser-Tab, wird am Ende erledigt und fällt "
        "aus, wenn der Termin sich verschiebt. Hier ist sie drin, direkt neben den Farben, während "
        "Sie sie noch auswählen.",
        "La comprobación de contraste suele vivir en una pestaña aparte del navegador, se hace al "
        "final y se salta cuando la fecha de entrega se mueve. Aquí está dentro, junto a los "
        "colores, mientras todavía los estás eligiendo.",
        "La verificación de contraste suele vivir en una pestaña aparte del navegador, se hace al "
        "final y se salta cuando la fecha de entrega se mueve. Aquí está dentro, junto a los "
        "colores, mientras todavía los estás eligiendo.",
        "La vérification du contraste vit d'habitude dans un onglet de navigateur à part, se fait "
        "à la fin, et saute quand la date de rendu bouge. Ici elle est à l'intérieur, à côté des "
        "couleurs, pendant que vous êtes encore en train de les choisir.",
        "Il controllo del contrasto di solito vive in una scheda del browser a parte, si fa alla "
        "fine e salta quando la scadenza si sposta. Qui è dentro, accanto ai colori, mentre li "
        "stai ancora scegliendo.",
        "コントラストの確認は普通、別のブラウザタブに住んでいて、最後に回され、締め切りが動くと"
        "省かれます。これはこの中にあります。色のすぐ隣に、まだ色を選んでいる最中に。",
        "명도 대비 확인은 보통 브라우저의 다른 탭에 살면서 맨 마지막에 하고, 마감이 밀리면 "
        "생략됩니다. 이건 안에 있습니다. 색 바로 옆에, 아직 색을 고르는 동안에.",
        "Contrast controleren woont meestal in een apart browsertabblad, gebeurt op het eind en "
        "valt weg als de deadline schuift. Hier zit het erin, naast de kleuren, terwijl je ze nog "
        "aan het kiezen bent.",
        "A verificação de contraste costuma morar numa aba separada do navegador, é feita no fim e "
        "é pulada quando o prazo se mexe. Aqui ela está dentro, ao lado das cores, enquanto você "
        "ainda está escolhendo.",
        "对比度检查通常住在浏览器的另一个标签页里，留到最后才做，一旦排期变动就被跳过。"
        "在这里它就在里面，紧挨着颜色，就在你还在挑色的时候。"),
    "Harmony Palette reports the WCAG 2.1 contrast ratio for any foreground and background pair\n      and grades it AA and AAA, separately for normal and large text, because the thresholds are\n      different: 4.5:1 and 3:1. When a pair falls short it can adjust the last color you touched\n      until it clears the bar, so the fix takes a tap instead of a spreadsheet.": (
        "Harmony Palette nennt für jedes Paar aus Vorder- und Hintergrund das WCAG 2.1 "
        "Kontrastverhältnis und bewertet es mit AA und AAA, getrennt für normalen und großen Text, "
        "weil die Schwellen verschieden sind: 4.5:1 und 3:1. Reicht ein Paar nicht, kann die App "
        "die zuletzt angefasste Farbe nachziehen, bis die Grenze erreicht ist. Die Korrektur ist "
        "ein Tippen statt einer Tabelle.",
        "Harmony Palette da la relación de contraste WCAG 2.1 de cualquier par de primer plano y "
        "fondo y la califica AA y AAA, por separado para texto normal y texto grande, porque los "
        "umbrales son distintos: 4.5:1 y 3:1. Si un par se queda corto, puede ajustar el último "
        "color que tocaste hasta que pase el listón, de modo que arreglarlo es un toque y no una "
        "hoja de cálculo.",
        "Harmony Palette da la relación de contraste WCAG 2.1 de cualquier par de primer plano y "
        "fondo y la califica AA y AAA, por separado para texto normal y texto grande, porque los "
        "umbrales son distintos: 4.5:1 y 3:1. Si un par se queda corto, puede ajustar el último "
        "color que tocaste hasta que pase el listón, así que arreglarlo es un toque y no una hoja "
        "de cálculo.",
        "Harmony Palette donne le rapport de contraste WCAG 2.1 de n'importe quel couple premier "
        "plan et arrière-plan et le note AA et AAA, séparément pour le texte normal et le grand "
        "texte, parce que les seuils diffèrent : 4.5:1 et 3:1. Quand un couple est insuffisant, "
        "l'application peut ajuster la dernière couleur touchée jusqu'à ce qu'elle passe la barre, "
        "si bien que la correction tient en une pression plutôt qu'en un tableur.",
        "Harmony Palette indica il rapporto di contrasto WCAG 2.1 di qualsiasi coppia di primo "
        "piano e sfondo e lo valuta AA e AAA, separatamente per il testo normale e quello grande, "
        "perché le soglie sono diverse: 4.5:1 e 3:1. Quando una coppia non basta, può regolare "
        "l'ultimo colore che hai toccato finché non supera l'asticella, così la correzione è un "
        "tocco invece di un foglio di calcolo.",
        "Harmony Palette は前景と背景のどの組み合わせについても WCAG 2.1 のコントラスト比を示し、"
        "通常の文字と大きな文字とで別々に AA と AAA を判定します。基準が 4.5:1 と 3:1 で違うから"
        "です。基準に届かない組み合わせがあれば、最後に触った色を基準を満たすところまで調整でき"
        "ます。修正は表計算ではなく一度のタップで済みます。",
        "Harmony Palette는 전경과 배경의 어떤 조합에 대해서도 WCAG 2.1 명도 대비를 알려주고, 일반 "
        "텍스트와 큰 텍스트를 나눠 AA와 AAA로 매깁니다. 기준이 4.5:1과 3:1로 다르기 때문입니다. "
        "기준에 못 미치는 조합이 있으면 마지막에 만진 색을 기준을 넘을 때까지 조정할 수 있습니다. "
        "고치는 데 스프레드시트가 아니라 한 번의 탭이면 됩니다.",
        "Harmony Palette geeft de WCAG 2.1 contrastverhouding van elk voorgrond- en achtergrondpaar "
        "en beoordeelt die met AA en AAA, apart voor gewone en grote tekst, want de drempels "
        "verschillen: 4.5:1 en 3:1. Schiet een paar tekort, dan kan de app de laatst aangeraakte "
        "kleur bijstellen tot die de lat haalt, zodat de correctie één tik kost in plaats van een "
        "spreadsheet.",
        "O Harmony Palette informa a relação de contraste WCAG 2.1 de qualquer par de primeiro "
        "plano e fundo e a classifica em AA e AAA, separadamente para texto normal e texto grande, "
        "porque os limiares são diferentes: 4.5:1 e 3:1. Quando um par não alcança, ele pode "
        "ajustar a última cor que você tocou até passar da marca, de modo que a correção é um "
        "toque em vez de uma planilha.",
        "对任意一组前景色与背景色，Harmony Palette 都会给出 WCAG 2.1 的对比度，"
        "并按正文和大字分别评定 AA 与 AAA，因为两者的门槛不同：4.5:1 和 3:1。"
        "若某一组不达标，它可以把你最后碰过的那个颜色调到过线为止，"
        "于是修正只需点一下，而不是打开一张表格。"),
    "It also shows you the palette as someone else sees it. Protanopia, deuteranopia, tritanopia\n      and achromatopsia, applied to a single color or to a whole saved palette, so you find out that\n      your success green and your error red are the same swatch to a large number of people before\n      you ship it rather than after.": (
        "Sie sehen die Palette außerdem so, wie andere sie sehen. Protanopie, Deuteranopie, "
        "Tritanopie und Achromatopsie, auf eine einzelne Farbe oder auf eine ganze gespeicherte "
        "Palette angewandt. So merken Sie vor dem Ausliefern und nicht danach, dass Ihr "
        "Erfolgs-Grün und Ihr Fehler-Rot für sehr viele Menschen dasselbe Feld sind.",
        "También te enseña la paleta como la ve otra persona. Protanopia, deuteranopia, tritanopia "
        "y acromatopsia, aplicadas a un solo color o a una paleta guardada entera, para que "
        "descubras que tu verde de acierto y tu rojo de error son la misma muestra para muchísima "
        "gente antes de publicarlo y no después.",
        "También te enseña la paleta como la ve otra persona. Protanopia, deuteranopia, tritanopia "
        "y acromatopsia, aplicadas a un solo color o a una paleta guardada entera, para que "
        "descubras que tu verde de acierto y tu rojo de error son la misma muestra para muchísima "
        "gente antes de publicarlo y no después.",
        "Elle vous montre aussi la palette telle que quelqu'un d'autre la voit. Protanopie, "
        "deutéranopie, tritanopie et achromatopsie, appliquées à une seule couleur ou à toute une "
        "palette enregistrée, pour que vous découvriez que votre vert de succès et votre rouge "
        "d'erreur sont le même échantillon pour énormément de gens avant de livrer plutôt "
        "qu'après.",
        "Ti mostra anche la palette come la vede qualcun altro. Protanopia, deuteranopia, "
        "tritanopia e acromatopsia, applicate a un singolo colore o a un'intera palette salvata, "
        "così scopri che il tuo verde di successo e il tuo rosso di errore sono lo stesso campione "
        "per moltissime persone prima di pubblicare invece che dopo.",
        "そのパレットが他の人にどう見えるかも示します。1 型色覚、2 型色覚、3 型色覚、全色盲を、"
        "単一の色にも保存済みのパレット全体にも適用できます。成功を示す緑とエラーを示す赤が、"
        "非常に多くの人にとって同じ色に見えることを、出してからではなく出す前に知れます。",
        "그 팔레트가 다른 사람에게 어떻게 보이는지도 보여줍니다. 적색맹, 녹색맹, 청색맹, 전색맹을 "
        "색 하나에도, 저장한 팔레트 전체에도 적용할 수 있습니다. 성공을 뜻하는 초록과 오류를 뜻하는 "
        "빨강이 아주 많은 사람에게 같은 색이라는 사실을, 내보낸 뒤가 아니라 내보내기 전에 알게 "
        "됩니다.",
        "Het laat je het palet ook zien zoals iemand anders het ziet. Protanopie, deuteranopie, "
        "tritanopie en achromatopsie, toegepast op één kleur of op een heel bewaard palet, zodat "
        "je erachter komt dat je succesgroen en je foutrood voor heel veel mensen hetzelfde staal "
        "zijn vóór je het uitbrengt in plaats van erna.",
        "Ele também mostra a paleta como outra pessoa a vê. Protanopia, deuteranopia, tritanopia e "
        "acromatopsia, aplicadas a uma única cor ou a uma paleta salva inteira, para você "
        "descobrir que o seu verde de sucesso e o seu vermelho de erro são a mesma amostra para "
        "muitíssima gente antes de publicar e não depois.",
        "它还会让你看到别人眼中的这套调色板。红色盲、绿色盲、蓝色盲和全色盲，"
        "可以作用于单个颜色，也可以作用于整套已保存的调色板。"
        "于是你会在发布之前、而不是之后，"
        "发现你用来表示成功的绿和表示错误的红，对相当多的人来说是同一个颜色。"),
}
