"""lf.wtf/dollop, part B: the creature, the feel of it, privacy, the FAQ, the live demonstration.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

The FAQ answers here are the ones the page shows *and* the ones the FAQ schema carries, so each is
translated once and reused in both places. Anything that promises the app collects nothing says so
flatly in every language: no "grundsätzlich", no "en principe", nothing that turns a statement into
a tendency.

The last block is the copy the mixing demonstration says while you play. It lives in the markup of
the page rather than in its script, because the extractor deliberately refuses to read inside a
<script> and a string hidden there would have shipped in English to ten languages.
"""

T = {
    # ---------------------------------------------------------------- the pet

    "Something hatches out of it": (
        "Daraus schlüpft etwas",
        "De ahí sale algo",
        "De ahí sale algo",
        "Quelque chose en éclot",
        "Da lì nasce qualcosa",
        "そこから何かが孵ります",
        "거기서 무언가 부화합니다",
        "Er komt iets uit",
        "Dali nasce uma coisa",
        "会从里面孵出点什么"),

    "The first color you match becomes a small creature, in that color. Everything you mix after\n"
    "    that feeds it, and its DNA is the strip of every color it has ever eaten, in order. It "
    "grows\n    slowly. It sleeps while you are gone. Leave it a month and it dries out, which one "
    "round undoes.\n    Nothing here can die, and nothing will notify you to say it misses you.": (
        "Der erste Farbton, den du triffst, wird zu einem kleinen Wesen in genau dieser Farbe. "
        "Alles, was du danach mischst, füttert es, und seine DNA ist der Streifen aller Farben, die "
        "es je gefressen hat, der Reihe nach. Es wächst langsam. Es schläft, während du weg bist. "
        "Lass es einen Monat allein, dann trocknet es aus, was eine einzige Runde wieder rückgängig "
        "macht. Hier kann nichts sterben, und nichts schickt dir eine Mitteilung, dass es dich "
        "vermisst.",
        "El primer color que aciertas se convierte en una criatura pequeña, de ese color. Todo lo "
        "que mezclas después la alimenta, y su ADN es la tira de todos los colores que se ha "
        "comido, en orden. Crece despacio. Duerme mientras no estás. Déjala un mes y se reseca, "
        "cosa que una sola partida deshace. Aquí nada puede morir, y nada te avisa de que te echa "
        "de menos.",
        "El primer color que aciertas se convierte en una criatura pequeña, de ese color. Todo lo "
        "que mezclas después la alimenta, y su ADN es la tira de todos los colores que se ha "
        "comido, en orden. Crece despacio. Duerme mientras no estás. Déjala un mes y se reseca, "
        "cosa que una sola partida deshace. Aquí nada puede morir, y nada te avisa de que te "
        "extraña.",
        "La première couleur que vous réussissez devient une petite créature, de cette couleur "
        "exactement. Tout ce que vous mélangez ensuite la nourrit, et son ADN est la bande de "
        "toutes les couleurs qu'elle a mangées, dans l'ordre. Elle grandit lentement. Elle dort "
        "pendant votre absence. Laissez-la un mois et elle se dessèche, ce qu'une seule partie "
        "défait. Ici rien ne peut mourir, et rien ne vous notifiera qu'on vous regrette.",
        "Il primo colore che indovini diventa una piccola creatura, di quel colore. Tutto quello "
        "che mescoli dopo la nutre, e il suo DNA è la striscia di ogni colore che ha mangiato, in "
        "ordine. Cresce piano. Dorme mentre sei via. Lasciala un mese e si secca, cosa che una sola "
        "partita annulla. Qui niente può morire, e niente ti manda una notifica per dirti che gli "
        "manchi.",
        "最初に合わせた色が、そのままの色の小さな生きものになります。そのあと混ぜたものはすべて"
        "餌になり、その DNA は食べてきた色を順番に並べた帯です。ゆっくり育ちます。いない間は"
        "眠っています。一か月ほうっておくと乾いてしまいますが、一回遊べば元に戻ります。ここでは"
        "何も死にません。寂しがっていると通知が来ることもありません。",
        "처음 맞춘 색이 그 색 그대로의 작은 생물이 됩니다. 그 뒤에 섞는 것은 모두 먹이가 되고, "
        "그 DNA는 지금까지 먹은 색을 순서대로 늘어놓은 띠입니다. 천천히 자랍니다. 당신이 없는 "
        "동안에는 잠을 잡니다. 한 달을 두면 말라 버리지만, 한 판이면 되돌아옵니다. 여기서는 "
        "아무것도 죽지 않고, 보고 싶다며 알림을 보내는 일도 없습니다.",
        "De eerste kleur die je raakt wordt een klein wezen, in precies die kleur. Alles wat je "
        "daarna mengt voedt het, en zijn DNA is de strook van elke kleur die het ooit heeft "
        "gegeten, op volgorde. Het groeit langzaam. Het slaapt terwijl je weg bent. Laat het een "
        "maand alleen en het droogt uit, wat één potje weer ongedaan maakt. Hier kan niets "
        "doodgaan, en niets stuurt je een melding dat het je mist.",
        "A primeira cor que você acerta vira uma criatura pequena, naquela cor. Tudo o que você "
        "mistura depois a alimenta, e o DNA dela é a tira de todas as cores que já comeu, em ordem. "
        "Cresce devagar. Dorme enquanto você está fora. Deixe um mês e ela resseca, o que uma "
        "partida desfaz. Aqui nada pode morrer, e nada te notifica dizendo que sente sua falta.",
        "你配对的第一个颜色，会变成一只那个颜色的小生物。之后你调出的每一个颜色都是它的食物，"
        "它的 DNA 就是它吃过的所有颜色按顺序排成的一条。它长得很慢。你不在的时候它就睡觉。"
        "一个月不理它就会干掉，但玩一局就恢复了。这里没有什么会死掉，也不会有通知跳出来说它想你。"),

    # ------------------------------------------------------------ sound and feel

    "Made to be quiet": (
        "Auf leise gebaut",
        "Hecho para estar en silencio",
        "Hecho para estar en silencio",
        "Fait pour rester discret",
        "Fatto per essere silenzioso",
        "静かであるようにつくりました",
        "조용하도록 만들었습니다",
        "Gemaakt om stil te zijn",
        "Feito para ser quieto",
        "为安静而做"),

    "Every sound is synthesized rather than sampled, and all of them sit in one pentatonic scale, "
    "so\n  however they land on top of each other they stay consonant. A drop parting from the tray "
    "rises in\n  pitch, the way a small amount of liquid pinching off does. A dollop sounds deeper "
    "as it grows.\n  Nothing is loud, nothing repeats exactly, and the audio mixes underneath "
    "whatever you were already\n  listening to instead of stopping it.": (
        "Jeder Ton wird synthetisiert statt gesampelt, und alle liegen in einer einzigen "
        "pentatonischen Tonleiter, sodass sie zusammenklingen, wie auch immer sie übereinander "
        "fallen. Ein Tropfen, der sich von der Palette löst, steigt in der Tonhöhe, so wie eine "
        "kleine Menge Flüssigkeit es tut, wenn sie abreißt. Ein Klecks klingt tiefer, je größer er "
        "wird. Nichts ist laut, nichts wiederholt sich exakt, und der Ton mischt sich unter das, "
        "was du ohnehin schon hörst, statt es abzubrechen.",
        "Cada sonido está sintetizado en vez de muestreado, y todos viven en una misma escala "
        "pentatónica, así que se apilen como se apilen siguen sonando consonantes. Una gota que se "
        "separa de la bandeja sube de tono, igual que hace una pequeña cantidad de líquido al "
        "desprenderse. Una gota suena más grave a medida que crece. Nada es fuerte, nada se repite "
        "exactamente, y el audio se mezcla por debajo de lo que ya estuvieras escuchando en vez de "
        "cortarlo.",
        "Cada sonido está sintetizado en vez de muestreado, y todos viven en una misma escala "
        "pentatónica, así que se apilen como se apilen siguen sonando consonantes. Una gota que se "
        "separa de la bandeja sube de tono, igual que hace una pequeña cantidad de líquido al "
        "desprenderse. Una gota suena más grave a medida que crece. Nada es fuerte, nada se repite "
        "exactamente, y el audio se mezcla por debajo de lo que ya estuvieras escuchando en vez de "
        "cortarlo.",
        "Chaque son est synthétisé plutôt qu'échantillonné, et tous tiennent dans une seule gamme "
        "pentatonique : quelle que soit la façon dont ils se superposent, ils restent consonants. "
        "Une goutte qui se détache du plateau monte en hauteur, comme le fait une petite quantité "
        "de liquide qui se pince. Une noisette sonne plus grave à mesure qu'elle grossit. Rien "
        "n'est fort, rien ne se répète à l'identique, et l'audio se glisse sous ce que vous "
        "écoutiez déjà au lieu de l'interrompre.",
        "Ogni suono è sintetizzato invece che campionato, e stanno tutti in un'unica scala "
        "pentatonica, così comunque si sovrappongano restano consonanti. Una goccia che si stacca "
        "dal vassoio sale di intonazione, come fa una piccola quantità di liquido che si stacca. Una "
        "goccia suona più grave man mano che cresce. Niente è forte, niente si ripete uguale, e "
        "l'audio si infila sotto quello che stavi già ascoltando invece di interromperlo.",
        "音はすべてサンプリングではなく合成で、しかも全部がひとつのペンタトニック音階の中に"
        "あります。どう重なっても濁りません。トレイから絵の具がちぎれるときは、少量の液体が"
        "切れるときのように音が上がります。かたまりは大きくなるほど低く鳴ります。大きな音は"
        "なく、まったく同じ音が繰り返されることもなく、すでに聴いているものを止めずにその下に"
        "混ざります。",
        "모든 소리는 샘플이 아니라 합성이고, 전부 하나의 5음 음계 안에 있어서 어떻게 겹쳐도 "
        "어울립니다. 트레이에서 물감이 떨어져 나올 때는 적은 양의 액체가 끊길 때처럼 음이 "
        "올라갑니다. 덩어리는 커질수록 더 낮게 울립니다. 큰 소리는 없고, 똑같이 반복되는 소리도 "
        "없으며, 이미 듣고 있던 것을 끊지 않고 그 아래에 섞입니다.",
        "Elk geluid is gesynthetiseerd in plaats van gesampled, en ze zitten allemaal in één "
        "pentatonische toonladder, dus hoe ze ook over elkaar heen vallen, ze blijven consonant. "
        "Een druppel die van het palet loskomt gaat omhoog in toonhoogte, zoals een kleine "
        "hoeveelheid vloeistof doet als ze afknijpt. Een klodder klinkt lager naarmate hij groeit. "
        "Niets is luid, niets herhaalt zich precies, en het geluid mengt zich onder waar je al naar "
        "luisterde in plaats van het te onderbreken.",
        "Todo som é sintetizado em vez de amostrado, e todos ficam numa mesma escala pentatônica, "
        "então, de qualquer jeito que se empilhem, continuam consoantes. Um pingo que se solta da "
        "bandeja sobe de altura, como faz uma pequena quantidade de líquido ao se desprender. Um "
        "pingo soa mais grave conforme cresce. Nada é alto, nada se repete igual, e o áudio se "
        "mistura por baixo do que você já estava ouvindo em vez de interromper.",
        "所有声音都是合成的，不是采样的，而且全都落在同一个五声音阶里，无论怎样叠在一起都不会"
        "刺耳。一滴颜料从盘子上被拉断时，音高会往上走，就像少量液体断开时那样。一团颜料越大，"
        "声音越低。没有响的地方，也没有一模一样的重复，声音会垫在你原本在听的东西下面，"
        "而不是把它掐掉。"),

    "The paint is drawn as a real wet surface and shaded so that the flat top of a dollop is "
    "exactly\n  the color you mixed rather than a lighter version of it. That sounds like a small "
    "thing. It is the\n  difference between judging your mix and judging a highlight.": (
        "Die Farbe ist als echte nasse Oberfläche gezeichnet und so schattiert, dass die flache "
        "Oberseite eines Kleckses genau der Farbton ist, den du gemischt hast, und nicht eine "
        "hellere Fassung davon. Das klingt nach einer Kleinigkeit. Es ist der Unterschied zwischen "
        "der Beurteilung deiner Mischung und der Beurteilung eines Glanzlichts.",
        "La pintura está dibujada como una superficie mojada de verdad y sombreada para que la "
        "parte plana de arriba de una gota sea exactamente el color que mezclaste y no una versión "
        "más clara. Suena a detalle menor. Es la diferencia entre juzgar tu mezcla y juzgar un "
        "brillo.",
        "La pintura está dibujada como una superficie mojada de verdad y sombreada para que la "
        "parte plana de arriba de una gota sea exactamente el color que mezclaste y no una versión "
        "más clara. Suena a detalle menor. Es la diferencia entre juzgar tu mezcla y juzgar un "
        "brillo.",
        "La peinture est dessinée comme une vraie surface mouillée et ombrée de sorte que le dessus "
        "plat d'une noisette soit exactement la couleur que vous avez mélangée, et non une version "
        "plus claire. Cela paraît un détail. C'est la différence entre juger votre mélange et juger "
        "un reflet.",
        "La vernice è disegnata come una vera superficie bagnata e ombreggiata in modo che la parte "
        "piatta in cima a una goccia sia esattamente il colore che hai mescolato e non una sua "
        "versione più chiara. Sembra una piccolezza. È la differenza tra giudicare la tua mescola e "
        "giudicare un riflesso.",
        "絵の具は本物の濡れた面として描かれ、かたまりの平らな上面が、混ぜた色そのものになるよう"
        "陰影がつけてあります。明るくなった色ではありません。ささいなことに聞こえますが、"
        "自分の混ぜた色を見ているのか、ハイライトを見ているのかの違いです。",
        "물감은 진짜 젖은 표면으로 그려지고, 덩어리의 평평한 윗면이 당신이 섞은 바로 그 색이 "
        "되도록 음영이 들어갑니다. 더 밝아진 색이 아닙니다. 사소해 보이지만, 자기 색을 보는 것과 "
        "하이라이트를 보는 것의 차이입니다.",
        "De verf is getekend als een echt nat oppervlak en zo geschaduwd dat de vlakke bovenkant "
        "van een klodder precies de kleur is die je mengde, en niet een lichtere versie ervan. Dat "
        "klinkt als een kleinigheid. Het is het verschil tussen je mengsel beoordelen en een "
        "lichtvlek beoordelen.",
        "A tinta é desenhada como uma superfície molhada de verdade e sombreada de modo que o topo "
        "plano de um pingo seja exatamente a cor que você misturou, e não uma versão mais clara "
        "dela. Parece detalhe pequeno. É a diferença entre julgar a sua mistura e julgar um brilho.",
        "颜料是按真正的湿表面画出来的，并且做了明暗处理，让一团颜料平的顶面正好是你调出来的那个"
        "颜色，而不是它更浅的版本。听上去是小事。可这决定了你看的到底是自己的颜色，还是一块高光。"),

    "It reads in eleven languages, every control is labeled for VoiceOver, and the type scales "
    "with\n  the rest of your phone. Because the distance to the target is shown as a number, a "
    "color blind\n  player can close in on a match by reading rather than by comparing.": (
        "Es liest sich in elf Sprachen, jedes Bedienelement ist für VoiceOver beschriftet, und die "
        "Schrift skaliert mit dem Rest deines Telefons. Weil der Abstand zum Ziel als Zahl "
        "angezeigt wird, kann sich auch eine farbenblinde Spielerin lesend an einen Treffer "
        "herantasten statt vergleichend.",
        "Se lee en once idiomas, cada control está etiquetado para VoiceOver y la tipografía escala "
        "con el resto de tu teléfono. Como la distancia al objetivo se muestra como un número, "
        "quien no distingue los colores puede acercarse al acierto leyendo en vez de comparando.",
        "Se lee en once idiomas, cada control está etiquetado para VoiceOver y la tipografía escala "
        "con el resto de tu teléfono. Como la distancia al objetivo se muestra como un número, "
        "quien no distingue los colores puede acercarse al acierto leyendo en vez de comparando.",
        "Il se lit en onze langues, chaque commande est étiquetée pour VoiceOver, et la typographie "
        "suit la taille de texte du reste de votre téléphone. Comme la distance à la cible est "
        "affichée sous forme de nombre, une joueuse daltonienne peut se rapprocher d'une "
        "correspondance en lisant plutôt qu'en comparant.",
        "Si legge in undici lingue, ogni comando è etichettato per VoiceOver e il carattere scala "
        "con il resto del telefono. Poiché la distanza dall'obiettivo è mostrata come numero, chi "
        "non distingue i colori può avvicinarsi a un abbinamento leggendo invece che confrontando.",
        "十一の言語で読めます。すべての操作に VoiceOver 用のラベルがあり、文字は端末の設定に"
        "合わせて大きくなります。目標との差が数字で出るので、色の見分けがつきにくい人でも、"
        "見比べるのではなく読むことで正解に近づけます。",
        "열한 개 언어로 읽을 수 있고, 모든 조작에는 VoiceOver 레이블이 있으며, 글자는 기기 설정에 "
        "따라 커집니다. 목표와의 거리가 숫자로 나오기 때문에, 색을 구분하기 어려운 사람도 "
        "비교하는 대신 읽으면서 정답에 다가갈 수 있습니다.",
        "Het leest in elf talen, elke bediening heeft een VoiceOver-label, en de letters schalen "
        "mee met de rest van je telefoon. Doordat de afstand tot het doel als getal wordt getoond, "
        "kan een kleurenblinde speler een match benaderen door te lezen in plaats van te "
        "vergelijken.",
        "Ele lê em onze idiomas, cada controle tem rótulo para o VoiceOver e o texto acompanha o "
        "tamanho do resto do seu telefone. Como a distância até o alvo aparece como número, quem "
        "não distingue cores pode chegar ao acerto lendo em vez de comparando.",
        "它有十一种语言，每一个控件都为 VoiceOver 标好了名字，字号也跟着手机的设置一起变大。"
        "因为与目标的差距是用数字显示的，色觉障碍的玩家可以靠读数字逼近答案，而不必去比对颜色。"),

    # ------------------------------------------------------------------ privacy

    "What it does not do": (
        "Was es nicht tut",
        "Lo que no hace",
        "Lo que no hace",
        "Ce qu'il ne fait pas",
        "Cosa non fa",
        "しないこと",
        "하지 않는 것",
        "Wat het niet doet",
        "O que ele não faz",
        "它不做的事"),

    "No account. No sign in. No analytics, no advertising, no tracking, and no networking code in "
    "the\n  app at all. The daily color is computed rather than downloaded. Photographs used in "
    "From Life are\n  read on your phone and never leave it. Nothing you do in Dollop is collected, "
    "because there is\n  nothing in it that could collect anything.": (
        "Kein Konto. Keine Anmeldung. Keine Analyse, keine Werbung, kein Tracking und überhaupt "
        "kein Netzwerkcode in der App. Die Tagesfarbe wird berechnet, nicht heruntergeladen. Fotos, "
        "die du für Nach der Natur verwendest, werden auf deinem Telefon gelesen und verlassen es "
        "nie. Nichts von dem, was du in Dollop tust, wird erfasst, weil nichts darin etwas erfassen "
        "könnte.",
        "Sin cuenta. Sin inicio de sesión. Sin analítica, sin publicidad, sin seguimiento y sin "
        "nada de código de red en la app. El color del día se calcula, no se descarga. Las fotos "
        "que uses en Del natural se leen en tu teléfono y nunca salen de él. Nada de lo que haces "
        "en Dollop se recopila, porque no hay nada dentro que pudiera recopilarlo.",
        "Sin cuenta. Sin inicio de sesión. Sin analítica, sin publicidad, sin rastreo y sin nada de "
        "código de red en la app. El color del día se calcula, no se descarga. Las fotos que uses "
        "en Del natural se leen en tu teléfono y nunca salen de él. Nada de lo que haces en Dollop "
        "se recopila, porque no hay nada dentro que pudiera recopilarlo.",
        "Pas de compte. Pas de connexion. Pas d'analytique, pas de publicité, pas de pistage, et "
        "aucun code réseau dans l'app. La couleur du jour est calculée, pas téléchargée. Les photos "
        "utilisées dans D'après nature sont lues sur votre téléphone et n'en sortent jamais. Rien "
        "de ce que vous faites dans Dollop n'est collecté, parce qu'il n'y a rien dedans qui "
        "pourrait collecter quoi que ce soit.",
        "Nessun account. Nessun accesso. Nessuna analitica, nessuna pubblicità, nessun "
        "tracciamento e nessun codice di rete nell'app. Il colore del giorno è calcolato, non "
        "scaricato. Le foto usate in Dal vero vengono lette sul telefono e non lo lasciano mai. "
        "Niente di quello che fai in Dollop viene raccolto, perché non c'è nulla dentro che "
        "potrebbe raccogliere qualcosa.",
        "アカウントなし。サインインなし。解析も広告もトラッキングもなく、そもそも通信の"
        "コードがアプリの中にありません。その日の色はダウンロードではなく計算されます。実物から"
        "で使った写真は端末の中で読まれ、外に出ることはありません。Dollop での行動は何も"
        "収集されません。収集できるものが中にないからです。",
        "계정 없음. 로그인 없음. 분석도 광고도 추적도 없고, 애초에 앱 안에 네트워크 코드가 "
        "없습니다. 오늘의 색은 내려받는 것이 아니라 계산됩니다. 실물에서 모드에서 쓴 사진은 "
        "기기 안에서 읽히고 밖으로 나가지 않습니다. Dollop에서 하는 어떤 것도 수집되지 않습니다. "
        "수집할 수 있는 것이 안에 없기 때문입니다.",
        "Geen account. Geen inloggen. Geen analytics, geen advertenties, geen tracking, en "
        "überhaupt geen netwerkcode in de app. De kleur van de dag wordt berekend, niet gedownload. "
        "Foto's die je in Naar de natuur gebruikt worden op je telefoon gelezen en verlaten hem "
        "nooit. Niets van wat je in Dollop doet wordt verzameld, want er zit niets in dat iets zou "
        "kunnen verzamelen.",
        "Sem conta. Sem login. Sem analytics, sem publicidade, sem rastreamento e sem nenhum código "
        "de rede no app. A cor do dia é calculada, não baixada. As fotos usadas no Do natural são "
        "lidas no seu telefone e nunca saem dele. Nada do que você faz no Dollop é coletado, porque "
        "não há nada nele que pudesse coletar qualquer coisa.",
        "没有账号。不用登录。没有统计分析，没有广告，没有追踪，App 里根本就没有联网代码。"
        "每日的颜色是算出来的，不是下载的。写生模式里用到的照片在你手机上读取，从不离开手机。"
        "你在 Dollop 里做的任何事都不会被收集，因为它里面没有任何能收集东西的部分。"),

    "The privacy policy": (
        "Die Datenschutzerklärung",
        "La política de privacidad",
        "La política de privacidad",
        "La politique de confidentialité",
        "L'informativa sulla privacy",
        "プライバシーポリシー",
        "개인정보 처리방침",
        "Het privacybeleid",
        "A política de privacidade",
        "隐私政策"),

    "says the same at greater length, and says\n  nothing else.": (
        "sagt dasselbe ausführlicher, und sonst nichts.",
        "dice lo mismo más largo, y no dice nada más.",
        "dice lo mismo más largo, y no dice nada más.",
        "dit la même chose en plus long, et ne dit rien d'autre.",
        "dice lo stesso più per esteso, e non dice altro.",
        "は同じことをもう少し長く述べているだけで、それ以外は何も書いていません。",
        "은 같은 이야기를 조금 더 길게 할 뿐, 그 밖의 내용은 없습니다.",
        "zegt hetzelfde wat uitgebreider, en verder niets.",
        "diz o mesmo com mais palavras, e não diz mais nada.",
        "把同样的话说得长一些，除此之外没有别的内容。"),

    # ---------------------------------------------------------------------- FAQ

    "Questions": (
        "Fragen", "Preguntas", "Preguntas", "Questions", "Domande",
        "よくある質問", "질문", "Vragen", "Perguntas", "常见问题"),

    "Why do blue and yellow make green in paint but gray on a screen?": (
        "Warum ergeben Blau und Gelb in Farbe Grün, auf einem Bildschirm aber Grau?",
        "¿Por qué el azul y el amarillo dan verde en pintura pero gris en una pantalla?",
        "¿Por qué el azul y el amarillo dan verde en pintura pero gris en una pantalla?",
        "Pourquoi le bleu et le jaune donnent-ils du vert en peinture mais du gris sur un écran ?",
        "Perché blu e giallo danno verde nella vernice ma grigio su uno schermo?",
        "絵の具では青と黄が緑になるのに、画面では灰色になるのはなぜですか。",
        "물감에서는 파랑과 노랑이 초록이 되는데, 화면에서는 왜 회색이 되나요?",
        "Waarom worden blauw en geel groen in verf maar grijs op een scherm?",
        "Por que azul e amarelo dão verde na tinta mas cinza numa tela?",
        "为什么颜料里蓝加黄是绿色，屏幕上却是灰色？"),

    "Because they are two different kinds of mixing. A screen adds light: red, green and blue\n"
    "  emitters sum, so blue light plus yellow light gives something pale. Paint subtracts light. "
    "Blue\n  pigment absorbs most of the red end of the spectrum, yellow pigment absorbs most of "
    "the blue end,\n  and what survives both is the middle, which is green. Dollop mixes the second "
    "way, which is why it\n  gives a real green.": (
        "Weil das zwei verschiedene Arten des Mischens sind. Ein Bildschirm addiert Licht: rote, "
        "grüne und blaue Emitter summieren sich, also ergibt blaues Licht plus gelbes Licht etwas "
        "Blasses. Farbe subtrahiert Licht. Blaues Pigment schluckt den größten Teil des roten "
        "Spektrumendes, gelbes Pigment den größten Teil des blauen Endes, und was beides überlebt, "
        "ist die Mitte, also Grün. Dollop mischt auf die zweite Art, und deshalb kommt ein echtes "
        "Grün heraus.",
        "Porque son dos tipos de mezcla distintos. Una pantalla suma luz: los emisores rojo, verde "
        "y azul se suman, así que luz azul más luz amarilla da algo pálido. La pintura resta luz. "
        "El pigmento azul absorbe casi todo el extremo rojo del espectro, el amarillo absorbe casi "
        "todo el extremo azul, y lo que sobrevive a ambos es el centro, que es verde. Dollop mezcla "
        "de la segunda manera, y por eso da un verde de verdad.",
        "Porque son dos tipos de mezcla distintos. Una pantalla suma luz: los emisores rojo, verde "
        "y azul se suman, así que luz azul más luz amarilla da algo pálido. La pintura resta luz. "
        "El pigmento azul absorbe casi todo el extremo rojo del espectro, el amarillo absorbe casi "
        "todo el extremo azul, y lo que sobrevive a ambos es el centro, que es verde. Dollop mezcla "
        "de la segunda manera, y por eso da un verde de verdad.",
        "Parce que ce sont deux façons de mélanger différentes. Un écran ajoute de la lumière : les "
        "émetteurs rouge, vert et bleu s'additionnent, donc lumière bleue plus lumière jaune donne "
        "quelque chose de pâle. La peinture soustrait de la lumière. Le pigment bleu absorbe "
        "l'essentiel de l'extrémité rouge du spectre, le pigment jaune l'essentiel de l'extrémité "
        "bleue, et ce qui survit aux deux, c'est le milieu, c'est-à-dire le vert. Dollop mélange de "
        "la seconde façon, et c'est pour cela qu'il donne un vrai vert.",
        "Perché sono due tipi di mescolanza diversi. Uno schermo somma luce: gli emettitori rosso, "
        "verde e blu si sommano, quindi luce blu più luce gialla dà qualcosa di pallido. La vernice "
        "sottrae luce. Il pigmento blu assorbe quasi tutto l'estremo rosso dello spettro, quello "
        "giallo quasi tutto l'estremo blu, e ciò che sopravvive a entrambi è il centro, cioè il "
        "verde. Dollop mescola nel secondo modo, ed è per questo che dà un verde vero.",
        "混ぜ方が二種類あるからです。画面は光を足します。赤・緑・青の発光が足し合わさるので、"
        "青い光と黄色い光を足すと淡い色になります。絵の具は光を引きます。青い顔料はスペクトルの"
        "赤側の大半を、黄色い顔料は青側の大半を吸い、両方を生き延びるのは真ん中、つまり緑です。"
        "Dollop は後者のやり方で混ぜます。だから本物の緑になります。",
        "섞는 방식이 두 가지이기 때문입니다. 화면은 빛을 더합니다. 빨강, 초록, 파랑 발광이 "
        "더해지므로 파란빛에 노란빛을 더하면 창백한 색이 됩니다. 물감은 빛을 뺍니다. 파란 안료는 "
        "스펙트럼의 빨강 쪽 대부분을, 노란 안료는 파랑 쪽 대부분을 흡수하고, 둘 다에서 살아남는 "
        "것은 가운데, 곧 초록입니다. Dollop은 두 번째 방식으로 섞습니다. 그래서 진짜 초록이 "
        "나옵니다.",
        "Omdat het twee verschillende soorten mengen zijn. Een scherm telt licht op: rode, groene "
        "en blauwe emitters tellen bij elkaar op, dus blauw licht plus geel licht geeft iets "
        "bleeks. Verf trekt licht af. Blauw pigment slikt het grootste deel van het rode uiteinde "
        "van het spectrum, geel pigment het grootste deel van het blauwe, en wat allebei overleeft "
        "is het midden, en dat is groen. Dollop mengt op de tweede manier, en daarom komt er een "
        "echt groen uit.",
        "Porque são dois tipos de mistura diferentes. Uma tela soma luz: os emissores vermelho, "
        "verde e azul se somam, então luz azul mais luz amarela dá algo pálido. A tinta subtrai "
        "luz. O pigmento azul absorve quase toda a ponta vermelha do espectro, o amarelo absorve "
        "quase toda a ponta azul, e o que sobrevive aos dois é o meio, que é verde. O Dollop "
        "mistura do segundo jeito, e por isso dá um verde de verdade.",
        "因为这是两种不同的混合。屏幕做的是加法：红、绿、蓝三种发光叠加，所以蓝光加黄光会得到"
        "发白的颜色。颜料做的是减法。蓝颜料吸掉光谱里红的那一端的大部分，黄颜料吸掉蓝的那一端的"
        "大部分，两者都留下的是中间，也就是绿色。Dollop 用的是后一种混合，所以它给出的是真正的"
        "绿色。"),

    "What is subtractive color mixing?": (
        "Was ist subtraktive Farbmischung?",
        "¿Qué es la mezcla sustractiva de color?",
        "¿Qué es la mezcla sustractiva de color?",
        "Qu'est-ce que la synthèse soustractive des couleurs ?",
        "Che cos'è la mescolanza sottrattiva dei colori?",
        "減法混色とは何ですか。",
        "감산 혼합이란 무엇인가요?",
        "Wat is subtractieve kleurmenging?",
        "O que é mistura subtrativa de cores?",
        "什么是减法混色？"),

    "Subtractive mixing is what happens when colorants are combined: each one removes part of the\n"
    "  spectrum, and you see only the light that nothing absorbed. It is how paint, ink and dye "
    "behave.\n  Additive mixing is the opposite and describes light itself, which is what a screen "
    "or a stage lamp\n  does. Dollop models the subtractive case with Kubelka-Munk theory, the "
    "approximation the paint\n  industry uses to predict a batch before anyone stirs it.": (
        "Subtraktive Mischung ist das, was passiert, wenn Farbmittel zusammenkommen: jedes entfernt "
        "einen Teil des Spektrums, und du siehst nur das Licht, das nichts geschluckt hat. So "
        "verhalten sich Farbe, Tinte und Farbstoff. Additive Mischung ist das Gegenteil und "
        "beschreibt das Licht selbst, also das, was ein Bildschirm oder ein Bühnenscheinwerfer tut. "
        "Dollop modelliert den subtraktiven Fall mit der Kubelka-Munk-Theorie, der Näherung, mit "
        "der die Farbenindustrie eine Charge vorhersagt, bevor jemand rührt.",
        "La mezcla sustractiva es lo que ocurre cuando se combinan colorantes: cada uno quita una "
        "parte del espectro y solo ves la luz que nada absorbió. Es como se comportan la pintura, "
        "la tinta y el tinte. La mezcla aditiva es lo contrario y describe la luz misma, que es lo "
        "que hace una pantalla o un foco de escenario. Dollop modela el caso sustractivo con la "
        "teoría de Kubelka-Munk, la aproximación que usa la industria de la pintura para predecir "
        "un lote antes de que nadie lo remueva.",
        "La mezcla sustractiva es lo que ocurre cuando se combinan colorantes: cada uno quita una "
        "parte del espectro y solo ves la luz que nada absorbió. Es como se comportan la pintura, "
        "la tinta y el tinte. La mezcla aditiva es lo contrario y describe la luz misma, que es lo "
        "que hace una pantalla o un foco de escenario. Dollop modela el caso sustractivo con la "
        "teoría de Kubelka-Munk, la aproximación que usa la industria de la pintura para predecir "
        "un lote antes de que alguien lo revuelva.",
        "La synthèse soustractive, c'est ce qui se produit quand on combine des colorants : chacun "
        "retire une partie du spectre, et vous ne voyez que la lumière que rien n'a absorbée. C'est "
        "ainsi que se comportent la peinture, l'encre et la teinture. La synthèse additive est "
        "l'inverse et décrit la lumière elle-même, ce que fait un écran ou un projecteur de scène. "
        "Dollop modélise le cas soustractif avec la théorie de Kubelka-Munk, l'approximation dont "
        "l'industrie de la peinture se sert pour prévoir un lot avant que quiconque ne remue.",
        "La mescolanza sottrattiva è ciò che accade quando si combinano coloranti: ciascuno toglie "
        "una parte dello spettro, e vedi soltanto la luce che nulla ha assorbito. È così che si "
        "comportano vernice, inchiostro e tintura. La mescolanza additiva è l'opposto e descrive la "
        "luce stessa, cioè quello che fa uno schermo o un faro da palco. Dollop modella il caso "
        "sottrattivo con la teoria di Kubelka-Munk, l'approssimazione che l'industria della vernice "
        "usa per prevedere una partita prima che qualcuno la mescoli.",
        "減法混色とは、色材を混ぜたときに起きることです。それぞれがスペクトルの一部を取り去り、"
        "何にも吸われなかった光だけが見えます。絵の具もインクも染料もこう振る舞います。加法混色"
        "はその逆で、光そのものの話です。画面や舞台照明がしているのがそれです。Dollop は減法の"
        "側を、クベルカ・ムンク理論でモデル化しています。塗料の業界が、実際にかき混ぜる前に"
        "仕上がりを予測するのに使っている近似です。",
        "감산 혼합은 색료를 합쳤을 때 일어나는 일입니다. 각각이 스펙트럼의 일부를 덜어내고, "
        "아무것도 흡수하지 않은 빛만 보입니다. 물감과 잉크와 염료가 이렇게 움직입니다. 가산 "
        "혼합은 그 반대이고 빛 자체를 설명합니다. 화면이나 무대 조명이 하는 일이 그것입니다. "
        "Dollop은 감산 쪽을 쿠벨카-뭉크 이론으로 모델링합니다. 페인트 업계가 실제로 젓기 전에 "
        "결과를 예측할 때 쓰는 근사입니다.",
        "Subtractief mengen is wat er gebeurt als kleurstoffen worden gecombineerd: elk haalt een "
        "deel van het spectrum weg, en je ziet alleen het licht dat niets heeft opgeslokt. Zo "
        "gedragen verf, inkt en kleurstof zich. Additief mengen is het omgekeerde en beschrijft het "
        "licht zelf, wat een scherm of een toneellamp doet. Dollop modelleert het subtractieve "
        "geval met de Kubelka-Munk-theorie, de benadering waarmee de verfindustrie een charge "
        "voorspelt voordat iemand roert.",
        "Mistura subtrativa é o que acontece quando corantes são combinados: cada um remove uma "
        "parte do espectro, e você vê só a luz que nada absorveu. É assim que tinta, tinta de "
        "impressão e corante se comportam. A mistura aditiva é o oposto e descreve a luz em si, que "
        "é o que uma tela ou um refletor de palco faz. O Dollop modela o caso subtrativo com a "
        "teoria de Kubelka-Munk, a aproximação que a indústria de tintas usa para prever um lote "
        "antes de alguém mexer.",
        "减法混色，指的是色料被混在一起时发生的事：每一种都减去光谱里的一段，你看到的只有没被"
        "任何东西吸收掉的光。颜料、油墨和染料都是这样。加法混色正好相反，说的是光本身，"
        "屏幕和舞台灯做的就是这件事。Dollop 用库贝尔卡-蒙克理论来建模减法这一侧，"
        "那正是涂料行业在真正搅拌之前用来预测一批漆的近似方法。"),

    "Is Dollop free?": (
        "Ist Dollop kostenlos?",
        "¿Dollop es gratis?",
        "¿Dollop es gratis?",
        "Dollop est-il gratuit ?",
        "Dollop è gratis?",
        "Dollop は無料ですか。",
        "Dollop은 무료인가요?",
        "Is Dollop gratis?",
        "O Dollop é grátis?",
        "Dollop 免费吗？"),

    "Yes. Zen and Daily are free forever and are whole modes rather than a demonstration. One\n"
    "  purchase of 4.99 US dollars, paid once and never again, unlocks Blind, Precise and From "
    "Life.\n  There is no subscription, no advertising, and no lives or energy to wait for.": (
        "Ja. Zen und Täglich sind für immer kostenlos und sind vollständige Modi, keine Demo. Ein "
        "einziger Kauf von 4,99 US-Dollar, einmal bezahlt und nie wieder, schaltet Blind, Präzise "
        "und Nach der Natur frei. Es gibt kein Abo, keine Werbung und keine Leben oder Energie, auf "
        "die man warten müsste.",
        "Sí. Zen y Diario son gratis para siempre y son modos completos, no una demostración. Una "
        "sola compra de 4,99 dólares, pagada una vez y nunca más, desbloquea A ciegas, Preciso y "
        "Del natural. No hay suscripción, ni publicidad, ni vidas o energía que haya que esperar.",
        "Sí. Zen y Diario son gratis para siempre y son modos completos, no una demostración. Una "
        "sola compra de 4.99 dólares, pagada una vez y nunca más, desbloquea A ciegas, Preciso y "
        "Del natural. No hay suscripción, ni publicidad, ni vidas o energía que haya que esperar.",
        "Oui. Zen et Quotidien sont gratuits pour toujours et sont des modes entiers, pas une "
        "démonstration. Un seul achat de 4,99 dollars, payé une fois et plus jamais, déverrouille À "
        "l'aveugle, Précis et D'après nature. Il n'y a pas d'abonnement, pas de publicité, ni vies "
        "ni énergie à attendre.",
        "Sì. Zen e Quotidiano sono gratis per sempre e sono modalità intere, non una dimostrazione. "
        "Un solo acquisto di 4,99 dollari, pagato una volta e mai più, sblocca Alla cieca, Preciso "
        "e Dal vero. Non c'è abbonamento, non c'è pubblicità, e non ci sono vite o energia da "
        "aspettare.",
        "はい。禅とデイリーはずっと無料で、体験版ではなく丸ごとひとつのモードです。4.99 米ドルの"
        "買い切りを一度だけ支払えば、ブラインド・精密・実物からが開きます。二度目はありません。"
        "サブスクリプションも広告もなく、回復を待つライフやエネルギーもありません。",
        "예. 젠과 데일리는 영원히 무료이고, 체험판이 아니라 온전한 모드입니다. 4.99 미국 달러를 "
        "한 번만 결제하면 블라인드, 정밀, 실물에서가 열립니다. 구독도 광고도 없고, 회복을 "
        "기다려야 하는 라이프나 에너지도 없습니다.",
        "Ja. Zen en Dagelijks zijn voor altijd gratis en zijn hele modi, geen demonstratie. Eén "
        "aankoop van 4,99 Amerikaanse dollar, één keer betaald en nooit meer, ontgrendelt Blind, "
        "Precies en Naar de natuur. Er is geen abonnement, geen reclame, en geen levens of energie "
        "om op te wachten.",
        "Sim. Zen e Diário são grátis para sempre e são modos inteiros, não uma demonstração. Uma "
        "compra de 4,99 dólares, paga uma vez e nunca mais, desbloqueia Às cegas, Preciso e Do "
        "natural. Não há assinatura, não há publicidade, e não há vidas ou energia para esperar.",
        "免费。禅和每日永远免费，而且是完整的模式，不是演示。一次 4.99 美元的买断，付一次就够了，"
        "解锁盲配、精准和写生。没有订阅，没有广告，也没有需要等待回复的生命值或体力。"),

    "What does Delta E mean?": (
        "Was bedeutet Delta E?",
        "¿Qué significa Delta E?",
        "¿Qué significa Delta E?",
        "Que signifie Delta E ?",
        "Che cosa significa Delta E?",
        "Delta E とは何ですか。",
        "Delta E는 무슨 뜻인가요?",
        "Wat betekent Delta E?",
        "O que significa Delta E?",
        "Delta E 是什么意思？"),

    "Delta E is the distance between two colors in a space built so that equal distances look "
    "about\n  equally different to a person. A Delta E of 1 is roughly the smallest difference a "
    "trained eye\n  catches side by side, and 3 is close enough that most people would call it a "
    "match. Dollop shows it\n  while you mix: Zen, Daily and Blind accept anything under 3, and "
    "Precise wants under 1.": (
        "Delta E ist der Abstand zwischen zwei Farben in einem Raum, der so gebaut ist, dass "
        "gleiche Abstände für einen Menschen ungefähr gleich unterschiedlich aussehen. Ein Delta E "
        "von 1 ist ungefähr der kleinste Unterschied, den ein geübtes Auge im direkten Vergleich "
        "bemerkt, und 3 ist nah genug, dass die meisten es einen Treffer nennen würden. Dollop "
        "zeigt es beim Mischen an: Zen, Täglich und Blind akzeptieren alles unter 3, Präzise will "
        "unter 1.",
        "Delta E es la distancia entre dos colores en un espacio construido para que distancias "
        "iguales se vean más o menos igual de distintas para una persona. Un Delta E de 1 es "
        "aproximadamente la diferencia más pequeña que un ojo entrenado detecta lado a lado, y 3 "
        "está lo bastante cerca como para que la mayoría lo llame un acierto. Dollop lo muestra "
        "mientras mezclas: Zen, Diario y A ciegas aceptan cualquier cosa por debajo de 3, y Preciso "
        "quiere por debajo de 1.",
        "Delta E es la distancia entre dos colores en un espacio construido para que distancias "
        "iguales se vean más o menos igual de distintas para una persona. Un Delta E de 1 es "
        "aproximadamente la diferencia más pequeña que un ojo entrenado detecta lado a lado, y 3 "
        "está lo bastante cerca como para que la mayoría lo llame un acierto. Dollop lo muestra "
        "mientras mezclas: Zen, Diario y A ciegas aceptan cualquier cosa por debajo de 3, y Preciso "
        "quiere por debajo de 1.",
        "Delta E est la distance entre deux couleurs dans un espace construit pour que des "
        "distances égales paraissent à peu près également différentes à un être humain. Un Delta E "
        "de 1, c'est à peu près la plus petite différence qu'un œil exercé repère côte à côte, et 3 "
        "est assez proche pour que la plupart des gens parlent d'une correspondance. Dollop "
        "l'affiche pendant que vous mélangez : Zen, Quotidien et À l'aveugle acceptent tout ce qui "
        "est sous 3, et Précis veut sous 1.",
        "Delta E è la distanza tra due colori in uno spazio costruito perché distanze uguali "
        "sembrino a una persona più o meno ugualmente diverse. Un Delta E di 1 è all'incirca la più "
        "piccola differenza che un occhio allenato coglie affiancando i due colori, e 3 è abbastanza "
        "vicino perché la maggior parte delle persone lo chiami un abbinamento. Dollop lo mostra "
        "mentre mescoli: Zen, Quotidiano e Alla cieca accettano qualsiasi cosa sotto 3, e Preciso "
        "vuole sotto 1.",
        "Delta E は、同じ距離が人にとってほぼ同じだけ違って見えるように作られた空間での、"
        "二色のあいだの距離です。Delta E が 1 なら、訓練された目が並べてやっと気づく程度の差、"
        "3 なら、たいていの人が一致と呼ぶくらいの近さです。Dollop は混ぜているあいだそれを"
        "表示します。禅・デイリー・ブラインドは 3 未満で合格、精密は 1 未満を求めます。",
        "Delta E는 같은 거리가 사람에게 거의 같은 정도로 달라 보이도록 만든 공간에서 두 색 사이의 "
        "거리입니다. Delta E 1은 훈련된 눈이 나란히 놓고서야 겨우 알아채는 차이이고, 3이면 대부분 "
        "일치라고 부를 만큼 가깝습니다. Dollop은 섞는 동안 이 값을 보여 줍니다. 젠, 데일리, "
        "블라인드는 3 미만이면 통과하고, 정밀은 1 미만을 요구합니다.",
        "Delta E is de afstand tussen twee kleuren in een ruimte die zo gebouwd is dat gelijke "
        "afstanden voor een mens ongeveer even verschillend ogen. Een Delta E van 1 is ruwweg het "
        "kleinste verschil dat een geoefend oog naast elkaar oppikt, en 3 is dicht genoeg dat de "
        "meeste mensen het een match noemen. Dollop toont het terwijl je mengt: Zen, Dagelijks en "
        "Blind accepteren alles onder 3, en Precies wil onder 1.",
        "Delta E é a distância entre duas cores num espaço construído para que distâncias iguais "
        "pareçam mais ou menos igualmente diferentes para uma pessoa. Um Delta E de 1 é mais ou "
        "menos a menor diferença que um olho treinado percebe lado a lado, e 3 está perto o "
        "bastante para a maioria chamar de acerto. O Dollop mostra isso enquanto você mistura: Zen, "
        "Diário e Às cegas aceitam qualquer coisa abaixo de 3, e Preciso quer abaixo de 1.",
        "Delta E 是两个颜色之间的距离，所在的色彩空间被构造成：相等的距离，在人眼看来差别也大致"
        "相等。Delta E 为 1，差不多是训练过的眼睛并排比较才能察觉的最小差别；到了 3，"
        "大多数人就会说这是配上了。Dollop 会在你调色时把它显示出来：禅、每日和盲配接受 3 以内，"
        "精准要求 1 以内。"),

    "Does Dollop need an account or an internet connection?": (
        "Braucht Dollop ein Konto oder eine Internetverbindung?",
        "¿Dollop necesita una cuenta o conexión a internet?",
        "¿Dollop necesita una cuenta o conexión a internet?",
        "Dollop a-t-il besoin d'un compte ou d'une connexion internet ?",
        "Dollop ha bisogno di un account o di una connessione a internet?",
        "Dollop にアカウントやインターネット接続は必要ですか。",
        "Dollop에 계정이나 인터넷 연결이 필요한가요?",
        "Heeft Dollop een account of internetverbinding nodig?",
        "O Dollop precisa de conta ou de conexão com a internet?",
        "Dollop 需要账号或者联网吗？"),

    "Neither. There is no account, no sign in, and no networking code in the app at all. Even the\n"
    "  daily color is computed on the device from the date rather than fetched, so everyone gets "
    "the same\n  color each day without a server being involved. Nothing you do is collected or "
    "sent anywhere.": (
        "Weder noch. Es gibt kein Konto, keine Anmeldung und überhaupt keinen Netzwerkcode in der "
        "App. Selbst die Tagesfarbe wird auf dem Gerät aus dem Datum berechnet statt geholt, also "
        "bekommen alle jeden Tag dieselbe Farbe, ohne dass ein Server beteiligt wäre. Nichts, was "
        "du tust, wird erfasst oder irgendwohin geschickt.",
        "Ninguna de las dos. No hay cuenta, no hay inicio de sesión y no hay nada de código de red "
        "en la app. Incluso el color del día se calcula en el dispositivo a partir de la fecha en "
        "vez de descargarse, así que todo el mundo recibe el mismo color cada día sin que haya "
        "ningún servidor de por medio. Nada de lo que haces se recopila ni se envía a ninguna parte.",
        "Ninguna de las dos. No hay cuenta, no hay inicio de sesión y no hay nada de código de red "
        "en la app. Incluso el color del día se calcula en el dispositivo a partir de la fecha en "
        "vez de descargarse, así que todos reciben el mismo color cada día sin que haya ningún "
        "servidor de por medio. Nada de lo que haces se recopila ni se envía a ninguna parte.",
        "Ni l'un ni l'autre. Il n'y a pas de compte, pas de connexion, et aucun code réseau dans "
        "l'app. Même la couleur du jour est calculée sur l'appareil à partir de la date plutôt que "
        "récupérée : tout le monde a donc la même couleur chaque jour sans qu'aucun serveur soit "
        "impliqué. Rien de ce que vous faites n'est collecté ni envoyé nulle part.",
        "Nessuna delle due. Non c'è account, non c'è accesso e non c'è alcun codice di rete "
        "nell'app. Perfino il colore del giorno è calcolato sul dispositivo a partire dalla data "
        "invece di essere scaricato, così tutti ricevono lo stesso colore ogni giorno senza che sia "
        "coinvolto un server. Niente di quello che fai viene raccolto o mandato da qualche parte.",
        "どちらも要りません。アカウントもサインインもなく、通信のコードがアプリの中に"
        "ありません。その日の色さえ、取りに行くのではなく端末の中で日付から計算されるので、"
        "サーバーなしで全員が同じ色を受け取ります。あなたのしたことは何も収集されず、"
        "どこにも送られません。",
        "둘 다 필요 없습니다. 계정도 로그인도 없고, 앱 안에 네트워크 코드가 전혀 없습니다. 오늘의 "
        "색조차 받아 오는 것이 아니라 기기 안에서 날짜로부터 계산되기 때문에, 서버 없이도 모두가 "
        "매일 같은 색을 받습니다. 당신이 한 어떤 것도 수집되거나 어디론가 보내지지 않습니다.",
        "Geen van beide. Er is geen account, geen inloggen, en überhaupt geen netwerkcode in de "
        "app. Zelfs de kleur van de dag wordt op het toestel uit de datum berekend in plaats van "
        "opgehaald, dus iedereen krijgt elke dag dezelfde kleur zonder dat er een server aan te pas "
        "komt. Niets van wat je doet wordt verzameld of ergens heen gestuurd.",
        "Nenhum dos dois. Não há conta, não há login e não há nenhum código de rede no app. Até a "
        "cor do dia é calculada no aparelho a partir da data em vez de ser baixada, então todo "
        "mundo recebe a mesma cor por dia sem nenhum servidor envolvido. Nada do que você faz é "
        "coletado ou enviado a lugar nenhum.",
        "都不需要。没有账号，不用登录，App 里也完全没有联网代码。就连每日的颜色也是在设备上"
        "由日期算出来的，不是取回来的，所以不经过任何服务器，所有人每天拿到的都是同一个颜色。"
        "你做的任何事都不会被收集，也不会被发到任何地方。"),

    "Can I play Dollop if I am color blind?": (
        "Kann ich Dollop spielen, wenn ich farbenblind bin?",
        "¿Puedo jugar a Dollop si no distingo los colores?",
        "¿Puedo jugar Dollop si no distingo los colores?",
        "Puis-je jouer à Dollop si je suis daltonien ?",
        "Posso giocare a Dollop se sono daltonico?",
        "色覚に違いがあっても Dollop を遊べますか。",
        "색각 이상이 있어도 Dollop을 할 수 있나요?",
        "Kan ik Dollop spelen als ik kleurenblind ben?",
        "Posso jogar Dollop se eu for daltônico?",
        "色觉障碍还能玩 Dollop 吗？"),

    "Partly, and further than you might expect. The distance from the target is shown as a live\n"
    "  number, so a match can be closed in by reading it rather than by judging two colors against "
    "each\n  other. Blind mode, which hides the target on purpose, is the one that will not work.": (
        "Teilweise, und weiter, als du vielleicht erwartest. Der Abstand zum Ziel wird als "
        "laufende Zahl angezeigt, also lässt sich ein Treffer lesend einkreisen statt durch das "
        "Abwägen zweier Farben gegeneinander. Blind, wo das Ziel absichtlich verdeckt wird, ist der "
        "Modus, der nicht funktionieren wird.",
        "En parte, y más lejos de lo que esperarías. La distancia al objetivo se muestra como un "
        "número en vivo, así que puedes cerrar el acierto leyéndolo en vez de comparando dos "
        "colores entre sí. A ciegas, que oculta el objetivo a propósito, es el modo que no va a "
        "funcionar.",
        "En parte, y más lejos de lo que esperarías. La distancia al objetivo se muestra como un "
        "número en vivo, así que puedes cerrar el acierto leyéndolo en vez de comparando dos "
        "colores entre sí. A ciegas, que oculta el objetivo a propósito, es el modo que no va a "
        "funcionar.",
        "En partie, et plus loin que vous ne le pensez. La distance à la cible s'affiche sous forme "
        "de nombre en direct : on peut donc resserrer sur une correspondance en le lisant plutôt "
        "qu'en soupesant deux couleurs l'une contre l'autre. À l'aveugle, qui masque la cible "
        "exprès, est le mode qui ne marchera pas.",
        "In parte, e più in là di quanto ti aspetteresti. La distanza dall'obiettivo è mostrata "
        "come numero dal vivo, quindi un abbinamento si può stringere leggendolo invece che "
        "soppesando due colori l'uno contro l'altro. Alla cieca, che nasconde l'obiettivo di "
        "proposito, è la modalità che non funzionerà.",
        "ある程度は、しかも思っているより深くまで遊べます。目標との差が常に数字で出るので、"
        "二つの色を見比べるのではなく、その数字を読んで正解に寄せられます。うまくいかないのは、"
        "目標をわざと隠すブラインドです。",
        "어느 정도는, 그리고 생각보다 더 깊이 즐길 수 있습니다. 목표와의 거리가 실시간 숫자로 "
        "나오기 때문에, 두 색을 견주는 대신 그 숫자를 읽으며 정답에 좁혀 갈 수 있습니다. 목표를 "
        "일부러 가리는 블라인드만은 잘 되지 않습니다.",
        "Deels, en verder dan je zou verwachten. De afstand tot het doel wordt als een levend getal "
        "getoond, dus een match is dicht te krijgen door dat te lezen in plaats van twee kleuren "
        "tegen elkaar af te wegen. Blind, dat het doel met opzet verbergt, is de modus die niet zal "
        "werken.",
        "Em parte, e mais longe do que você imagina. A distância até o alvo aparece como um número "
        "ao vivo, então dá para fechar o acerto lendo esse número em vez de comparar duas cores "
        "entre si. Às cegas, que esconde o alvo de propósito, é o modo que não vai funcionar.",
        "可以玩相当一部分，而且比你想的走得更远。与目标的差距会以实时数字显示，所以你可以靠读"
        "这个数字去逼近答案，而不必把两个颜色放在一起比。唯一玩不了的是刻意把目标藏起来的盲配。"),

    "Which pigments are in the game?": (
        "Welche Pigmente sind im Spiel?",
        "¿Qué pigmentos hay en el juego?",
        "¿Qué pigmentos hay en el juego?",
        "Quels pigments y a-t-il dans le jeu ?",
        "Quali pigmenti ci sono nel gioco?",
        "ゲームにはどんな顔料が入っていますか。",
        "게임에는 어떤 안료가 들어 있나요?",
        "Welke pigmenten zitten er in het spel?",
        "Quais pigmentos estão no jogo?",
        "游戏里有哪些颜料？"),

    "Eight standing pigments: titanium white, cadmium yellow, cadmium red, quinacridone magenta,\n"
    "  ultramarine, phthalo blue, phthalo green and lamp black. Each round hands you six of them, "
    "chosen\n  so that the color you were given can actually be reached from what is on the tray.": (
        "Acht feste Pigmente: Titanweiß, Kadmiumgelb, Kadmiumrot, Chinacridonmagenta, Ultramarin, "
        "Phthaloblau, Phthalogrün und Lampenschwarz. Jede Runde gibt dir sechs davon, ausgewählt "
        "danach, dass der geforderte Farbton aus dem, was auf der Palette liegt, wirklich "
        "erreichbar ist.",
        "Ocho pigmentos fijos: blanco de titanio, amarillo de cadmio, rojo de cadmio, magenta de "
        "quinacridona, ultramar, azul ftalo, verde ftalo y negro humo. Cada ronda te da seis, "
        "elegidos de modo que el color pedido se pueda alcanzar de verdad con lo que hay en la "
        "bandeja.",
        "Ocho pigmentos fijos: blanco de titanio, amarillo de cadmio, rojo de cadmio, magenta de "
        "quinacridona, ultramar, azul ftalo, verde ftalo y negro humo. Cada ronda te da seis, "
        "elegidos de modo que el color pedido se pueda alcanzar de verdad con lo que hay en la "
        "bandeja.",
        "Huit pigments permanents : blanc de titane, jaune de cadmium, rouge de cadmium, magenta "
        "quinacridone, outremer, bleu phtalo, vert phtalo et noir de fumée. Chaque manche vous en "
        "donne six, choisis pour que la couleur demandée soit réellement atteignable avec ce qui "
        "est sur le plateau.",
        "Otto pigmenti fissi: bianco di titanio, giallo di cadmio, rosso di cadmio, magenta "
        "chinacridone, oltremare, blu ftalo, verde ftalo e nero fumo. Ogni round te ne dà sei, "
        "scelti in modo che il colore richiesto sia davvero raggiungibile con quello che c'è sul "
        "vassoio.",
        "顔料は八種類。チタンホワイト、カドミウムイエロー、カドミウムレッド、キナクリドン"
        "マゼンタ、ウルトラマリン、フタロブルー、フタログリーン、ランプブラックです。毎回その"
        "うち六つが渡され、示された色がトレイの上のもので本当に作れるように選ばれます。",
        "여덟 가지 상비 안료: 티타늄 화이트, 카드뮴 옐로, 카드뮴 레드, 퀴나크리돈 마젠타, "
        "울트라마린, 프탈로 블루, 프탈로 그린, 램프 블랙. 매 판마다 그중 여섯 개가 주어지고, "
        "주어진 색이 트레이 위의 것들로 실제로 만들어질 수 있도록 고릅니다.",
        "Acht vaste pigmenten: titaanwit, cadmiumgeel, cadmiumrood, quinacridonmagenta, "
        "ultramarijn, ftaloblauw, ftalogroen en lampenzwart. Elke ronde krijg je er zes, gekozen "
        "zodat de gevraagde kleur echt bereikbaar is met wat er op het palet ligt.",
        "Oito pigmentos fixos: branco de titânio, amarelo de cádmio, vermelho de cádmio, magenta "
        "de quinacridona, ultramar, azul ftalo, verde ftalo e preto de fumo. Cada rodada te dá "
        "seis, escolhidos de forma que a cor pedida seja de fato alcançável com o que está na "
        "bandeja.",
        "八种常备颜料：钛白、镉黄、镉红、喹吖啶酮品红、群青、酞菁蓝、酞菁绿和灯黑。每一局会给你"
        "其中六种，并且是挑过的，保证给出的那个颜色真的能用盘里的东西调出来。"),

    # ---------------------------------------------------------------- the footer

    "Privacy": (
        "Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
        "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),

    "Also here:": (
        "Ebenfalls hier:", "También aquí:", "También aquí:", "Également ici :", "Anche qui:",
        "こちらもどうぞ：", "여기에도 있습니다:", "Ook hier:", "Também aqui:", "这里还有："),

    ", which is about choosing colors\n  rather than making them.": (
        ", bei dem es ums Auswählen von Farben geht statt ums Herstellen.",
        ", que va de elegir colores en vez de fabricarlos.",
        ", que va de elegir colores en vez de fabricarlos.",
        ", qui parle de choisir les couleurs plutôt que de les fabriquer.",
        ", che parla di scegliere i colori invece di farli.",
        "。色をつくるのではなく、選ぶためのアプリです。",
        ". 색을 만드는 것이 아니라 고르는 쪽의 앱입니다.",
        ", dat over het kiezen van kleuren gaat in plaats van het maken ervan.",
        ", que é sobre escolher cores em vez de fabricá-las.",
        "，那是一款关于挑选颜色、而不是调出颜色的应用。"),

    # ------------------------------------------------- what the demonstration says

    "Matched. That is a real green, and it came out of the arithmetic.": (
        "Getroffen. Das ist ein echtes Grün, und es kommt aus der Arithmetik.",
        "Acertado. Ese es un verde de verdad, y salió de la aritmética.",
        "Acertado. Ese es un verde de verdad, y salió de la aritmética.",
        "Trouvé. C'est un vrai vert, et il sort de l'arithmétique.",
        "Trovato. Quello è un verde vero, ed è uscito dall'aritmetica.",
        "一致しました。これは本物の緑で、計算から出てきたものです。",
        "맞췄습니다. 이건 진짜 초록이고, 계산에서 나온 색입니다.",
        "Raak. Dat is een echt groen, en het komt uit de rekensom.",
        "Acertou. Esse é um verde de verdade, e saiu da aritmética.",
        "配上了。这是真正的绿色，是算出来的。"),

    "Close. One more dollop of something.": (
        "Nah dran. Noch ein Klecks von irgendetwas.",
        "Cerca. Una gota más de algo.",
        "Cerca. Una gota más de algo.",
        "Tout près. Encore une noisette de quelque chose.",
        "Vicino. Ancora una goccia di qualcosa.",
        "近いです。何かをもうひとつ。",
        "가깝습니다. 무언가를 한 덩이 더.",
        "Dichtbij. Nog één klodder van iets.",
        "Perto. Mais um pingo de alguma coisa.",
        "很接近了。再来一团什么。"),

    "Keep going.": (
        "Weitermachen.", "Sigue.", "Sigue.", "Continuez.", "Continua.",
        "そのまま続けて。", "계속 해 보세요.", "Ga door.", "Continue.", "接着调。"),

    "Scraped off. Start again.": (
        "Abgekratzt. Von vorn.",
        "Raspado. Empieza de nuevo.",
        "Raspado. Empieza de nuevo.",
        "Gratté. On recommence.",
        "Raschiato via. Ricomincia.",
        "こそげ落としました。はじめから。",
        "긁어냈습니다. 다시 시작하세요.",
        "Eraf geschraapt. Opnieuw.",
        "Raspado. Comece de novo.",
        "刮干净了。重新来。"),

    "A new color, mixable from what is on the tray.": (
        "Eine neue Farbe, mischbar aus dem, was auf der Palette liegt.",
        "Un color nuevo, mezclable con lo que hay en la bandeja.",
        "Un color nuevo, mezclable con lo que hay en la bandeja.",
        "Une nouvelle couleur, réalisable avec ce qui est sur le plateau.",
        "Un colore nuovo, ottenibile con quello che c'è sul vassoio.",
        "新しい色です。トレイの上のものだけで作れます。",
        "새로운 색입니다. 트레이 위의 것들만으로 만들 수 있습니다.",
        "Een nieuwe kleur, te mengen uit wat er op het palet ligt.",
        "Uma cor nova, possível com o que está na bandeja.",
        "换了个新颜色，用盘里的东西一定调得出来。"),

    "The board is full. Scrape it off and start again.": (
        "Das Brett ist voll. Kratz es ab und fang von vorn an.",
        "El tablero está lleno. Ráspalo y empieza de nuevo.",
        "El tablero está lleno. Ráspalo y empieza de nuevo.",
        "La planche est pleine. Grattez tout et recommencez.",
        "La tavola è piena. Raschia via e ricomincia.",
        "板がいっぱいです。こそげ落として、はじめからどうぞ。",
        "판이 가득 찼습니다. 긁어내고 다시 시작하세요.",
        "Het bord is vol. Schraap het eraf en begin opnieuw.",
        "O tabuleiro está cheio. Raspe tudo e comece de novo.",
        "板上满了。刮掉重来吧。"),

    "Add a dollop of this pigment": (
        "Einen Klecks von diesem Pigment hinzufügen",
        "Añadir una gota de este pigmento",
        "Agregar una gota de este pigmento",
        "Ajouter une noisette de ce pigment",
        "Aggiungi una goccia di questo pigmento",
        "この顔料をひとつ加える",
        "이 안료를 한 덩이 넣기",
        "Een klodder van dit pigment toevoegen",
        "Adicionar um pingo deste pigmento",
        "加一团这个颜料"),

    # ------------------------------------------------------ structured data only

    "A color mixing puzzle for iPhone in which paint mixes subtractively. Each pigment is held as "
    "sixteen reflectance readings from 400 to 700 nanometers and combined under Kubelka-Munk "
    "theory, so blue and yellow make green rather than gray. Five modes, a creature that hatches "
    "from the first color you match, and no account, advertising or networking of any kind.": (
        "Ein Farbmisch-Puzzle fürs iPhone, in dem Farbe subtraktiv mischt. Jedes Pigment wird als "
        "sechzehn Reflexionswerte von 400 bis 700 Nanometern gehalten und nach der "
        "Kubelka-Munk-Theorie kombiniert, sodass Blau und Gelb Grün ergeben statt Grau. Fünf Modi, "
        "ein Wesen, das aus dem ersten getroffenen Farbton schlüpft, und weder Konto noch Werbung "
        "noch irgendeine Netzwerkverbindung.",
        "Un puzle de mezcla de colores para iPhone en el que la pintura mezcla de forma "
        "sustractiva. Cada pigmento se guarda como dieciséis lecturas de reflectancia de 400 a 700 "
        "nanómetros y se combina con la teoría de Kubelka-Munk, así que el azul y el amarillo dan "
        "verde y no gris. Cinco modos, una criatura que nace del primer color que aciertas, y ni "
        "cuenta ni publicidad ni conexión de ningún tipo.",
        "Un juego de mezcla de colores para iPhone en el que la pintura mezcla de forma "
        "sustractiva. Cada pigmento se guarda como dieciséis lecturas de reflectancia de 400 a 700 "
        "nanómetros y se combina con la teoría de Kubelka-Munk, así que el azul y el amarillo dan "
        "verde y no gris. Cinco modos, una criatura que nace del primer color que aciertas, y ni "
        "cuenta ni publicidad ni conexión de ningún tipo.",
        "Un puzzle de mélange de couleurs pour iPhone où la peinture se mélange de façon "
        "soustractive. Chaque pigment est conservé sous forme de seize mesures de réflectance de "
        "400 à 700 nanomètres et combiné selon la théorie de Kubelka-Munk : le bleu et le jaune "
        "donnent donc du vert et non du gris. Cinq modes, une créature qui éclot de la première "
        "couleur réussie, et ni compte, ni publicité, ni réseau d'aucune sorte.",
        "Un puzzle di mescolanza dei colori per iPhone in cui la vernice si mescola in modo "
        "sottrattivo. Ogni pigmento è tenuto come sedici letture di riflettanza da 400 a 700 "
        "nanometri e combinato secondo la teoria di Kubelka-Munk, così blu e giallo danno verde e "
        "non grigio. Cinque modalità, una creatura che nasce dal primo colore indovinato, e nessun "
        "account, nessuna pubblicità e nessuna rete di alcun tipo.",
        "絵の具が減法で混ざる iPhone 用の色混ぜパズル。顔料はそれぞれ 400 から 700 ナノメートル"
        "までの十六個の反射率として保持され、クベルカ・ムンク理論で合成されるので、青と黄は"
        "灰色ではなく緑になります。五つのモード、最初に合わせた色から孵る生きもの、そして"
        "アカウントも広告も一切の通信もありません。",
        "물감이 감산으로 섞이는 iPhone용 색 혼합 퍼즐. 각 안료는 400에서 700나노미터까지 열여섯 "
        "개의 반사율로 보관되고 쿠벨카-뭉크 이론으로 합쳐지기 때문에, 파랑과 노랑이 회색이 아니라 "
        "초록이 됩니다. 다섯 가지 모드, 처음 맞춘 색에서 부화하는 생물, 그리고 계정도 광고도 "
        "어떤 종류의 통신도 없습니다.",
        "Een kleurmengpuzzel voor iPhone waarin verf subtractief mengt. Elk pigment wordt bewaard "
        "als zestien reflectiemetingen van 400 tot 700 nanometer en gecombineerd volgens de "
        "Kubelka-Munk-theorie, dus blauw en geel worden groen in plaats van grijs. Vijf modi, een "
        "wezen dat uit je eerste geraakte kleur komt, en geen account, geen advertenties en geen "
        "netwerk van welke aard dan ook.",
        "Um quebra-cabeça de mistura de cores para iPhone em que a tinta mistura de forma "
        "subtrativa. Cada pigmento é guardado como dezesseis leituras de refletância de 400 a 700 "
        "nanômetros e combinado pela teoria de Kubelka-Munk, então azul e amarelo dão verde e não "
        "cinza. Cinco modos, uma criatura que nasce da primeira cor que você acerta, e nenhuma "
        "conta, publicidade ou rede de qualquer tipo.",
        "一款 iPhone 上的调色解谜游戏，颜料按减法混合。每一种颜料都以从 400 到 700 纳米的十六个"
        "反射率读数保存，并按库贝尔卡-蒙克理论合成，所以蓝加黄是绿色，不是灰色。五种模式，"
        "一只从你配对的第一个颜色里孵出来的小生物，没有账号、没有广告，也没有任何联网。"),

    "Zen, an unhurried run of colors to mix": (
        "Zen, eine gemächliche Folge von Farben zum Mischen",
        "Zen, una tanda tranquila de colores para mezclar",
        "Zen, una tanda tranquila de colores para mezclar",
        "Zen, une suite tranquille de couleurs à mélanger",
        "Zen, una serie senza fretta di colori da mescolare",
        "禅：急かされずに色を混ぜ続けるモード",
        "젠: 서두르지 않고 색을 계속 섞는 모드",
        "Zen, een ongehaaste reeks kleuren om te mengen",
        "Zen, uma sequência sem pressa de cores para misturar",
        "禅：不赶时间，一个接一个地调色"),

    "Daily, one color a day worked out on the device from the date": (
        "Täglich, ein Farbton pro Tag, auf dem Gerät aus dem Datum errechnet",
        "Diario, un color al día calculado en el dispositivo a partir de la fecha",
        "Diario, un color al día calculado en el dispositivo a partir de la fecha",
        "Quotidien, une couleur par jour calculée sur l'appareil à partir de la date",
        "Quotidiano, un colore al giorno calcolato sul dispositivo a partire dalla data",
        "デイリー：日付から端末の中で計算される、一日にひとつの色",
        "데일리: 날짜로부터 기기 안에서 계산되는 하루 한 가지 색",
        "Dagelijks, één kleur per dag die op het toestel uit de datum wordt berekend",
        "Diário, uma cor por dia calculada no aparelho a partir da data",
        "每日：由日期在设备上算出的、每天一个的颜色"),

    "Blind, where the target is covered after a few seconds": (
        "Blind, wo das Ziel nach ein paar Sekunden abgedeckt wird",
        "A ciegas, donde el objetivo se tapa a los pocos segundos",
        "A ciegas, donde el objetivo se tapa a los pocos segundos",
        "À l'aveugle, où la cible est masquée au bout de quelques secondes",
        "Alla cieca, dove l'obiettivo viene coperto dopo pochi secondi",
        "ブラインド：数秒で目標が隠れるモード",
        "블라인드: 몇 초 뒤 목표가 가려지는 모드",
        "Blind, waarbij het doel na een paar seconden wordt afgedekt",
        "Às cegas, em que o alvo é coberto depois de alguns segundos",
        "盲配：几秒之后目标就会被盖住"),

    "Precise, which asks for a match closer than most eyes can resolve": (
        "Präzise, das einen Treffer verlangt, der feiner ist, als die meisten Augen auflösen",
        "Preciso, que pide un acierto más fino de lo que la mayoría de los ojos distingue",
        "Preciso, que pide un acierto más fino de lo que la mayoría de los ojos distingue",
        "Précis, qui demande une correspondance plus fine que ce que la plupart des yeux "
        "distinguent",
        "Preciso, che chiede un abbinamento più fine di quanto la maggior parte degli occhi "
        "distingua",
        "精密：ほとんどの目には見分けられない精度での一致を求めるモード",
        "정밀: 대부분의 눈으로는 구분할 수 없는 정확도를 요구하는 모드",
        "Precies, dat een match vraagt die fijner is dan de meeste ogen kunnen onderscheiden",
        "Preciso, que pede um acerto mais fino do que a maioria dos olhos distingue",
        "精准：要求的接近程度超出大多数眼睛能分辨的范围"),

    "From Life, which pulls a color out of a photograph you take": (
        "Nach der Natur, das einen Farbton aus einem Foto zieht, das du machst",
        "Del natural, que saca un color de una foto que tomas tú",
        "Del natural, que saca un color de una foto que tomas tú",
        "D'après nature, qui tire une couleur d'une photo que vous prenez",
        "Dal vero, che estrae un colore da una foto che scatti tu",
        "実物から：自分で撮った写真の中から色を取り出すモード",
        "실물에서: 직접 찍은 사진에서 색을 뽑아내는 모드",
        "Naar de natuur, dat een kleur uit een foto haalt die je zelf maakt",
        "Do natural, que tira uma cor de uma foto que você mesmo faz",
        "写生：从你自己拍的照片里取一个颜色"),

    "A creature that hatches from your first match and keeps the DNA of every color it has eaten": (
        "Ein Wesen, das aus deinem ersten Treffer schlüpft und die DNA jeder Farbe behält, die es "
        "gefressen hat",
        "Una criatura que nace de tu primer acierto y conserva el ADN de cada color que se ha "
        "comido",
        "Una criatura que nace de tu primer acierto y conserva el ADN de cada color que se ha "
        "comido",
        "Une créature qui éclot de votre première réussite et garde l'ADN de chaque couleur qu'elle "
        "a mangée",
        "Una creatura che nasce dal tuo primo abbinamento e conserva il DNA di ogni colore che ha "
        "mangiato",
        "最初に合わせた色から孵り、食べてきた色の DNA を保ち続ける生きもの",
        "처음 맞춘 색에서 부화해, 먹어 온 모든 색의 DNA를 간직하는 생물",
        "Een wezen dat uit je eerste treffer komt en het DNA bewaart van elke kleur die het heeft "
        "gegeten",
        "Uma criatura que nasce do seu primeiro acerto e guarda o DNA de cada cor que já comeu",
        "一只从你配对的第一个颜色里孵出来、并保留吃过的每一个颜色 DNA 的小生物"),

    "Synthesized sound in a single pentatonic scale, with nothing loud in it": (
        "Synthetisierter Klang in einer einzigen pentatonischen Tonleiter, ohne irgendetwas Lautes",
        "Sonido sintetizado en una sola escala pentatónica, sin nada fuerte dentro",
        "Sonido sintetizado en una sola escala pentatónica, sin nada fuerte dentro",
        "Un son synthétisé dans une seule gamme pentatonique, sans rien de fort dedans",
        "Suono sintetizzato in un'unica scala pentatonica, senza niente di forte dentro",
        "ひとつのペンタトニック音階でつくられた合成音。大きな音はありません",
        "하나의 5음 음계로 만든 합성음, 큰 소리는 하나도 없음",
        "Gesynthetiseerd geluid in één pentatonische toonladder, zonder iets luids erin",
        "Som sintetizado numa única escala pentatônica, sem nada alto dentro",
        "全部落在同一个五声音阶里的合成音，没有一处是响的"),

    "Eleven languages, VoiceOver labels and Dynamic Type": (
        "Elf Sprachen, VoiceOver-Beschriftungen und dynamische Schrift",
        "Once idiomas, etiquetas de VoiceOver y texto dinámico",
        "Once idiomas, etiquetas de VoiceOver y texto dinámico",
        "Onze langues, étiquettes VoiceOver et texte dynamique",
        "Undici lingue, etichette VoiceOver e testo dinamico",
        "十一言語、VoiceOver のラベル、Dynamic Type 対応",
        "열한 개 언어, VoiceOver 레이블, 동적 글자 크기",
        "Elf talen, VoiceOver-labels en dynamische tekst",
        "Onze idiomas, rótulos de VoiceOver e texto dinâmico",
        "十一种语言、VoiceOver 标签和动态字体"),

    "Free to play. One purchase of 4.99 US dollars unlocks Blind, Precise and From Life. There is "
    "no subscription.": (
        "Kostenlos spielbar. Ein einziger Kauf von 4,99 US-Dollar schaltet Blind, Präzise und Nach "
        "der Natur frei. Es gibt kein Abo.",
        "Se juega gratis. Una compra de 4,99 dólares desbloquea A ciegas, Preciso y Del natural. No "
        "hay suscripción.",
        "Se juega gratis. Una compra de 4.99 dólares desbloquea A ciegas, Preciso y Del natural. No "
        "hay suscripción.",
        "Jouable gratuitement. Un achat de 4,99 dollars déverrouille À l'aveugle, Précis et "
        "D'après nature. Il n'y a pas d'abonnement.",
        "Si gioca gratis. Un acquisto di 4,99 dollari sblocca Alla cieca, Preciso e Dal vero. Non "
        "c'è abbonamento.",
        "無料で遊べます。4.99 米ドルの購入ひとつでブラインド・精密・実物からが開きます。"
        "サブスクリプションはありません。",
        "무료로 즐길 수 있습니다. 4.99 미국 달러 한 번의 구매로 블라인드, 정밀, 실물에서가 "
        "열립니다. 구독은 없습니다.",
        "Gratis te spelen. Eén aankoop van 4,99 Amerikaanse dollar ontgrendelt Blind, Precies en "
        "Naar de natuur. Er is geen abonnement.",
        "Grátis para jogar. Uma compra de 4,99 dólares desbloqueia Às cegas, Preciso e Do natural. "
        "Não há assinatura.",
        "免费游玩。一次 4.99 美元的购买即可解锁盲配、精准和写生。没有订阅。"),
}

# ------------------------------------------------------- rewritten, September 2026
#
# The page led on the fidelity of the mixing model, which is the wrong claim for a game and is also
# FRMT's claim rather than this one's. These replace the sentences that boasted about the engine
# with sentences about playing it. The physics stays where it answers a question a player asks; it
# is gone from every place it was there to impress.

T.update({
    "A slow, calming color mixing puzzle for iPhone. Blue and yellow make green here, the way "
    "they do on a palette and not the way they do on a screen. Free, no account, no ads, no "
    "internet needed.": (
        "Ein ruhiges, entschleunigtes Farbmisch-Puzzle fürs iPhone. Blau und Gelb ergeben hier "
        "Grün, so wie auf einer Palette und nicht so wie auf einem Bildschirm. Kostenlos, ohne "
        "Konto, ohne Werbung, ohne Internet.",
        "Un puzle de mezcla de colores lento y relajante para iPhone. Aquí el azul y el amarillo "
        "dan verde, como en una paleta y no como en una pantalla. Gratis, sin cuenta, sin anuncios "
        "y sin internet.",
        "Un juego de mezcla de colores lento y relajante para iPhone. Aquí el azul y el amarillo "
        "dan verde, como en una paleta y no como en una pantalla. Gratis, sin cuenta, sin anuncios "
        "y sin internet.",
        "Un puzzle de mélange de couleurs lent et apaisant pour iPhone. Ici le bleu et le jaune "
        "donnent du vert, comme sur une palette et non comme sur un écran. Gratuit, sans compte, "
        "sans publicité, sans connexion.",
        "Un puzzle di mescolanza dei colori lento e rilassante per iPhone. Qui blu e giallo danno "
        "verde, come su una tavolozza e non come su uno schermo. Gratis, senza account, senza "
        "pubblicità, senza internet.",
        "iPhone のためのゆっくり静かな色混ぜパズル。ここでは青と黄で緑になります。画面の上では"
        "なく、パレットの上と同じように。無料、アカウント不要、広告なし、通信なし。",
        "iPhone을 위한 느리고 차분한 색 혼합 퍼즐. 여기서는 파랑과 노랑이 초록이 됩니다. 화면이 "
        "아니라 팔레트 위에서처럼. 무료, 계정 없음, 광고 없음, 인터넷 없이.",
        "Een traag, rustgevend kleurmengspel voor iPhone. Blauw en geel worden hier groen, zoals op "
        "een palet en niet zoals op een scherm. Gratis, zonder account, zonder advertenties, zonder "
        "internet.",
        "Um quebra-cabeça de mistura de cores lento e tranquilo para iPhone. Aqui azul e amarelo "
        "dão verde, como numa paleta e não como numa tela. Grátis, sem conta, sem anúncios e sem "
        "internet.",
        "一款慢节奏、让人平静的 iPhone 调色解谜游戏。在这里，蓝加黄会变成绿，就像在调色板上，"
        "而不是在屏幕上。免费，无需账号，没有广告，不联网。"),

    "A slow, calming paint puzzle for iPhone. You are given a color. You mix it.": (
        "Ein ruhiges, entschleunigtes Farbpuzzle fürs iPhone. Du bekommst einen Farbton. Du "
        "mischst ihn.",
        "Un puzle de pintura lento y relajante para iPhone. Te dan un color. Lo mezclas.",
        "Un juego de pintura lento y relajante para iPhone. Te dan un color. Lo mezclas.",
        "Un puzzle de peinture lent et apaisant pour iPhone. On vous donne une couleur. Vous la "
        "mélangez.",
        "Un puzzle di pittura lento e rilassante per iPhone. Ti viene dato un colore. Lo mescoli.",
        "iPhone のためのゆっくり静かな絵の具パズル。色がひとつ示されます。それを混ぜてつくります。",
        "iPhone을 위한 느리고 차분한 물감 퍼즐. 색이 하나 주어집니다. 그 색을 만듭니다.",
        "Een traag, rustgevend verfspel voor iPhone. Je krijgt een kleur. Die meng je.",
        "Um quebra-cabeça de tinta lento e tranquilo para iPhone. Você recebe uma cor. Você a "
        "mistura.",
        "一款慢节奏、让人平静的 iPhone 颜料解谜游戏。给你一个颜色，你把它调出来。"),

    "On a screen they make gray. Dollop is a puzzle about mixing paint, and the paint in\n  it "
    "behaves the way paint behaves. You are given a color. You mix it.": (
        "Auf einem Bildschirm ergeben sie Grau. Dollop ist ein Puzzle über das Mischen von Farbe, "
        "und diese Farbe verhält sich wie Farbe. Du bekommst einen Farbton. Du mischst ihn.",
        "En una pantalla dan gris. Dollop es un puzle sobre mezclar pintura, y esa pintura se "
        "comporta como se comporta la pintura. Te dan un color. Lo mezclas.",
        "En una pantalla dan gris. Dollop es un juego sobre mezclar pintura, y esa pintura se "
        "comporta como se comporta la pintura. Te dan un color. Lo mezclas.",
        "Sur un écran, ils donnent du gris. Dollop est un puzzle sur le mélange de la peinture, et "
        "cette peinture se comporte comme de la peinture. On vous donne une couleur. Vous la "
        "mélangez.",
        "Su uno schermo danno grigio. Dollop è un puzzle sul mescolare la vernice, e quella vernice "
        "si comporta come si comporta la vernice. Ti viene dato un colore. Lo mescoli.",
        "画面の上では灰色になります。Dollop は絵の具を混ぜるパズルで、その絵の具は絵の具の"
        "とおりに振る舞います。色がひとつ示されます。それを混ぜてつくります。",
        "화면에서는 회색이 됩니다. Dollop은 물감을 섞는 퍼즐이고, 그 물감은 실제 물감처럼 "
        "움직입니다. 색이 하나 주어집니다. 그 색을 만들면 됩니다.",
        "Op een scherm worden ze grijs. Dollop is een puzzel over het mengen van verf, en die verf "
        "gedraagt zich zoals verf zich gedraagt. Je krijgt een kleur. Die meng je.",
        "Numa tela eles dão cinza. Dollop é um quebra-cabeça sobre misturar tinta, e essa tinta se "
        "comporta como tinta se comporta. Você recebe uma cor. Você a mistura.",
        "在屏幕上它们只会变成灰色。Dollop 是一款关于调颜料的解谜游戏，而这里的颜料，表现得就像"
        "真的颜料。给你一个颜色，你把它调出来。"),

    "So the ratio matters and the order does not. Two parts blue to one part yellow lands "
    "somewhere\n  different from one to one, exactly as it would on a palette, and getting there "
    "is the game: a\n  little more yellow, a little more white, until the two halves of the screen "
    "stop being two\n  halves.": (
        "Also zählt das Verhältnis und die Reihenfolge nicht. Zwei Teile Blau auf einen Teil Gelb "
        "landen woanders als eins zu eins, genau wie auf einer Palette, und genau dorthin zu kommen "
        "ist das Spiel: ein wenig mehr Gelb, ein wenig mehr Weiß, bis die beiden Hälften des "
        "Bildschirms aufhören, zwei Hälften zu sein.",
        "Así que la proporción importa y el orden no. Dos partes de azul por una de amarillo caen "
        "en un sitio distinto que uno a uno, igual que en una paleta, y llegar ahí es el juego: un "
        "poco más de amarillo, un poco más de blanco, hasta que las dos mitades de la pantalla "
        "dejan de ser dos mitades.",
        "Así que la proporción importa y el orden no. Dos partes de azul por una de amarillo caen "
        "en un lugar distinto que uno a uno, igual que en una paleta, y llegar ahí es el juego: un "
        "poco más de amarillo, un poco más de blanco, hasta que las dos mitades de la pantalla "
        "dejan de ser dos mitades.",
        "Le rapport compte donc, et l'ordre non. Deux parts de bleu pour une de jaune n'arrivent "
        "pas au même endroit qu'une pour une, exactement comme sur une palette, et y arriver est "
        "tout le jeu : un peu plus de jaune, un peu plus de blanc, jusqu'à ce que les deux moitiés "
        "de l'écran cessent d'être deux moitiés.",
        "Quindi il rapporto conta e l'ordine no. Due parti di blu per una di giallo finiscono "
        "altrove rispetto a uno a uno, esattamente come su una tavolozza, e arrivarci è il gioco: "
        "un po' più di giallo, un po' più di bianco, finché le due metà dello schermo smettono di "
        "essere due metà.",
        "だから比率は効き、順序は効きません。青二に対して黄一は、一対一とは違うところに着地し"
        "ます。パレットの上とまったく同じです。そこへ寄せていくことがこのゲームです。黄色を少し"
        "足し、白を少し足し、画面の左右がふたつに見えなくなるまで。",
        "그래서 비율은 영향을 주고 순서는 주지 않습니다. 파랑 둘에 노랑 하나는 일 대 일과 다른 "
        "곳에 떨어집니다. 팔레트 위에서와 똑같이. 거기에 다가가는 것이 이 게임입니다. 노랑을 조금 "
        "더, 흰색을 조금 더, 화면의 두 쪽이 더 이상 둘로 보이지 않을 때까지.",
        "Dus de verhouding doet ertoe en de volgorde niet. Twee delen blauw op één deel geel komt "
        "ergens anders uit dan één op één, precies zoals op een palet, en daar komen is het spel: "
        "een beetje meer geel, een beetje meer wit, tot de twee helften van het scherm ophouden "
        "twee helften te zijn.",
        "Então a proporção importa e a ordem não. Duas partes de azul para uma de amarelo cai em "
        "outro lugar que não um para um, exatamente como numa paleta, e chegar lá é o jogo: um "
        "pouco mais de amarelo, um pouco mais de branco, até as duas metades da tela deixarem de "
        "ser duas metades.",
        "所以比例有影响，先后没有。两份蓝配一份黄，落点和一比一并不相同，和在调色板上完全一样。"
        "而把它调过去，就是这个游戏：多一点黄，多一点白，直到屏幕上的两半不再是两半。"),

    "Subtractive mixing is what happens when colorants are combined: each one removes part of the\n"
    "  spectrum, and you see only the light that nothing absorbed. It is how paint, ink and dye "
    "behave.\n  Additive mixing is the opposite and describes light itself, which is what a screen "
    "or a stage lamp\n  does. Dollop is the subtractive kind, which is why mixing in it feels like "
    "mixing paint.": (
        "Subtraktive Mischung ist das, was passiert, wenn Farbmittel zusammenkommen: jedes entfernt "
        "einen Teil des Spektrums, und du siehst nur das Licht, das nichts geschluckt hat. So "
        "verhalten sich Farbe, Tinte und Farbstoff. Additive Mischung ist das Gegenteil und "
        "beschreibt das Licht selbst, also das, was ein Bildschirm oder ein Bühnenscheinwerfer tut. "
        "Dollop ist die subtraktive Sorte, und deshalb fühlt sich Mischen darin an wie Farbe "
        "mischen.",
        "La mezcla sustractiva es lo que ocurre cuando se combinan colorantes: cada uno quita una "
        "parte del espectro y solo ves la luz que nada absorbió. Es como se comportan la pintura, "
        "la tinta y el tinte. La mezcla aditiva es lo contrario y describe la luz misma, que es lo "
        "que hace una pantalla o un foco de escenario. Dollop es de la clase sustractiva, y por eso "
        "mezclar en él se siente como mezclar pintura.",
        "La mezcla sustractiva es lo que ocurre cuando se combinan colorantes: cada uno quita una "
        "parte del espectro y solo ves la luz que nada absorbió. Es como se comportan la pintura, "
        "la tinta y el tinte. La mezcla aditiva es lo contrario y describe la luz misma, que es lo "
        "que hace una pantalla o un foco de escenario. Dollop es de la clase sustractiva, y por eso "
        "mezclar en él se siente como mezclar pintura.",
        "La synthèse soustractive, c'est ce qui se produit quand on combine des colorants : chacun "
        "retire une partie du spectre, et vous ne voyez que la lumière que rien n'a absorbée. C'est "
        "ainsi que se comportent la peinture, l'encre et la teinture. La synthèse additive est "
        "l'inverse et décrit la lumière elle-même, ce que fait un écran ou un projecteur de scène. "
        "Dollop est du côté soustractif, et c'est pour cela que mélanger dedans donne la sensation "
        "de mélanger de la peinture.",
        "La mescolanza sottrattiva è ciò che accade quando si combinano coloranti: ciascuno toglie "
        "una parte dello spettro, e vedi soltanto la luce che nulla ha assorbito. È così che si "
        "comportano vernice, inchiostro e tintura. La mescolanza additiva è l'opposto e descrive la "
        "luce stessa, cioè quello che fa uno schermo o un faro da palco. Dollop è del tipo "
        "sottrattivo, ed è per questo che mescolare al suo interno sembra mescolare vernice.",
        "減法混色とは、色材を混ぜたときに起きることです。それぞれがスペクトルの一部を取り去り、"
        "何にも吸われなかった光だけが見えます。絵の具もインクも染料もこう振る舞います。加法混色"
        "はその逆で、光そのものの話です。画面や舞台照明がしているのがそれです。Dollop は減法の"
        "側なので、混ぜている感じが絵の具を混ぜている感じになります。",
        "감산 혼합은 색료를 합쳤을 때 일어나는 일입니다. 각각이 스펙트럼의 일부를 덜어내고, "
        "아무것도 흡수하지 않은 빛만 보입니다. 물감과 잉크와 염료가 이렇게 움직입니다. 가산 "
        "혼합은 그 반대이고 빛 자체를 설명합니다. 화면이나 무대 조명이 하는 일이 그것입니다. "
        "Dollop은 감산 쪽이어서, 여기서 색을 섞으면 물감을 섞는 느낌이 납니다.",
        "Subtractief mengen is wat er gebeurt als kleurstoffen worden gecombineerd: elk haalt een "
        "deel van het spectrum weg, en je ziet alleen het licht dat niets heeft opgeslokt. Zo "
        "gedragen verf, inkt en kleurstof zich. Additief mengen is het omgekeerde en beschrijft het "
        "licht zelf, wat een scherm of een toneellamp doet. Dollop is de subtractieve soort, en "
        "daarom voelt mengen erin als verf mengen.",
        "Mistura subtrativa é o que acontece quando corantes são combinados: cada um remove uma "
        "parte do espectro, e você vê só a luz que nada absorveu. É assim que tinta, tinta de "
        "impressão e corante se comportam. A mistura aditiva é o oposto e descreve a luz em si, que "
        "é o que uma tela ou um refletor de palco faz. O Dollop é do tipo subtrativo, e é por isso "
        "que misturar nele parece misturar tinta.",
        "减法混色，指的是色料被混在一起时发生的事：每一种都减去光谱里的一段，你看到的只有没被"
        "任何东西吸收掉的光。颜料、油墨和染料都是这样。加法混色正好相反，说的是光本身，屏幕和"
        "舞台灯做的就是这件事。Dollop 属于减法这一侧，所以在里面调色，手感就像在调真的颜料。"),

    "A slow color mixing puzzle for iPhone. You are given a color and you mix it out of a tray of "
    "paint, where blue and yellow make green the way they do on a palette rather than gray the way "
    "they do on a screen. Five modes, a creature that hatches from the first color you match, and "
    "no account, advertising or networking of any kind.": (
        "Ein ruhiges Farbmisch-Puzzle fürs iPhone. Du bekommst einen Farbton und mischst ihn aus "
        "einer Palette, auf der Blau und Gelb Grün ergeben wie auf einer echten Palette und nicht "
        "Grau wie auf einem Bildschirm. Fünf Modi, ein Wesen, das aus dem ersten getroffenen "
        "Farbton schlüpft, und weder Konto noch Werbung noch irgendeine Netzwerkverbindung.",
        "Un puzle de mezcla de colores tranquilo para iPhone. Te dan un color y lo mezclas a partir "
        "de una bandeja de pintura, donde el azul y el amarillo dan verde como en una paleta y no "
        "gris como en una pantalla. Cinco modos, una criatura que nace del primer color que "
        "aciertas, y ni cuenta ni publicidad ni conexión de ningún tipo.",
        "Un juego de mezcla de colores tranquilo para iPhone. Te dan un color y lo mezclas a partir "
        "de una bandeja de pintura, donde el azul y el amarillo dan verde como en una paleta y no "
        "gris como en una pantalla. Cinco modos, una criatura que nace del primer color que "
        "aciertas, y ni cuenta ni publicidad ni conexión de ningún tipo.",
        "Un puzzle de mélange de couleurs tranquille pour iPhone. On vous donne une couleur et vous "
        "la mélangez à partir d'un plateau de peinture, où le bleu et le jaune donnent du vert "
        "comme sur une palette et non du gris comme sur un écran. Cinq modes, une créature qui "
        "éclot de la première couleur réussie, et ni compte, ni publicité, ni réseau d'aucune "
        "sorte.",
        "Un puzzle di mescolanza dei colori tranquillo per iPhone. Ti viene dato un colore e lo "
        "mescoli da un vassoio di vernice, dove blu e giallo danno verde come su una tavolozza e "
        "non grigio come su uno schermo. Cinque modalità, una creatura che nasce dal primo colore "
        "indovinato, e nessun account, nessuna pubblicità e nessuna rete di alcun tipo.",
        "iPhone のための静かな色混ぜパズル。示された色を、絵の具のトレイから混ぜてつくります。"
        "ここでは青と黄が、画面の上の灰色ではなく、パレットの上と同じ緑になります。五つのモード、"
        "最初に合わせた色から孵る生きもの、そしてアカウントも広告も一切の通信もありません。",
        "iPhone을 위한 차분한 색 혼합 퍼즐. 주어진 색을 물감 트레이에서 섞어 만듭니다. 여기서 "
        "파랑과 노랑은 화면에서처럼 회색이 아니라 팔레트에서처럼 초록이 됩니다. 다섯 가지 모드, "
        "처음 맞춘 색에서 부화하는 생물, 그리고 계정도 광고도 어떤 종류의 통신도 없습니다.",
        "Een rustig kleurmengspel voor iPhone. Je krijgt een kleur en mengt die uit een palet met "
        "verf, waar blauw en geel groen worden zoals op een palet en niet grijs zoals op een "
        "scherm. Vijf modi, een wezen dat uit je eerste geraakte kleur komt, en geen account, geen "
        "advertenties en geen netwerk van welke aard dan ook.",
        "Um quebra-cabeça de mistura de cores calmo para iPhone. Você recebe uma cor e a mistura a "
        "partir de uma bandeja de tinta, onde azul e amarelo dão verde como numa paleta e não cinza "
        "como numa tela. Cinco modos, uma criatura que nasce da primeira cor que você acerta, e "
        "nenhuma conta, publicidade ou rede de qualquer tipo.",
        "一款安静的 iPhone 调色解谜游戏。给你一个颜色，你从一盘颜料里把它调出来。在这里，"
        "蓝加黄得到的是调色板上的绿，而不是屏幕上的灰。五种模式，一只从你配对的第一个颜色里孵"
        "出来的小生物，没有账号、没有广告，也没有任何联网。"),
})
