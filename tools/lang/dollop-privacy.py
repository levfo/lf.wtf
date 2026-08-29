"""lf.wtf/dollop/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

A privacy policy is the one page where a hedge changes the meaning. Where the English says the app
collects nothing, every language here says it too, without the "grundsätzlich", "en principe" and
"in linea di massima" that legal prose reaches for and that quietly turn a statement into a
tendency.

Dollop's policy is the shortest of the five because the app is the emptiest: no account, no sync,
no analytics and no networking code at all. The mode names match lf.wtf/dollop, which is where they
were settled: Del natural, D'apres nature, Dal vero, Nach der Natur, 写生.
"""

KEEP = {"Dollop", "lf.wtf", "L@LF.WTF", "Apple", "App Store", "iPhone", "In-App Purchase"}

T = {
    "Dollop Privacy Policy": (
        "Dollop Datenschutzerklärung",
        "Política de privacidad de Dollop",
        "Política de privacidad de Dollop",
        "Politique de confidentialité de Dollop",
        "Informativa sulla privacy di Dollop",
        "Dollop プライバシーポリシー",
        "Dollop 개인정보 처리방침",
        "Privacybeleid van Dollop",
        "Política de privacidade do Dollop",
        "Dollop 隐私政策"),

    "Dollop collects nothing. There is no account, no analytics, no advertising, and no networking "
    "code in the app at all. Photographs used in From Life are read on your device and never leave "
    "it.": (
        "Dollop erfasst nichts. Es gibt kein Konto, keine Analyse, keine Werbung und überhaupt "
        "keinen Netzwerkcode in der App. Fotos, die in Nach der Natur verwendet werden, werden auf "
        "deinem Gerät gelesen und verlassen es nie.",
        "Dollop no recopila nada. No hay cuenta, ni analítica, ni publicidad, ni nada de código de "
        "red en la app. Las fotos que se usan en Del natural se leen en tu dispositivo y nunca "
        "salen de él.",
        "Dollop no recopila nada. No hay cuenta, ni analítica, ni publicidad, ni nada de código de "
        "red en la app. Las fotos que se usan en Del natural se leen en tu dispositivo y nunca "
        "salen de él.",
        "Dollop ne collecte rien. Il n'y a pas de compte, pas d'analytique, pas de publicité, et "
        "aucun code réseau dans l'app. Les photos utilisées dans D'après nature sont lues sur votre "
        "appareil et n'en sortent jamais.",
        "Dollop non raccoglie nulla. Non c'è account, non c'è analitica, non c'è pubblicità e non "
        "c'è alcun codice di rete nell'app. Le foto usate in Dal vero vengono lette sul tuo "
        "dispositivo e non lo lasciano mai.",
        "Dollop は何も収集しません。アカウントも解析も広告もなく、そもそも通信のコードがアプリの"
        "中にありません。実物からで使った写真は端末の中で読まれ、外に出ることはありません。",
        "Dollop은 아무것도 수집하지 않습니다. 계정도 분석도 광고도 없고, 앱 안에 네트워크 코드가 "
        "전혀 없습니다. 실물에서 모드에서 쓴 사진은 기기 안에서 읽히고 밖으로 나가지 않습니다.",
        "Dollop verzamelt niets. Er is geen account, geen analytics, geen advertenties, en "
        "überhaupt geen netwerkcode in de app. Foto's die in Naar de natuur worden gebruikt worden "
        "op je toestel gelezen en verlaten het nooit.",
        "O Dollop não coleta nada. Não há conta, nem analytics, nem publicidade, nem nenhum código "
        "de rede no app. As fotos usadas no Do natural são lidas no seu aparelho e nunca saem dele.",
        "Dollop 不收集任何数据。没有账号，没有统计分析，没有广告，App 里也完全没有联网代码。"
        "写生模式里用到的照片在你的设备上读取，从不离开设备。"),

    "privacy policy": (
        "datenschutzerklärung", "política de privacidad", "política de privacidad",
        "politique de confidentialité", "informativa sulla privacy", "プライバシーポリシー",
        "개인정보 처리방침", "privacybeleid", "política de privacidade", "隐私政策"),

    "Last updated 29 August 2026": (
        "Zuletzt aktualisiert am 29. August 2026",
        "Última actualización: 29 de agosto de 2026",
        "Última actualización: 29 de agosto de 2026",
        "Dernière mise à jour le 29 août 2026",
        "Ultimo aggiornamento 29 agosto 2026",
        "最終更新 2026 年 8 月 29 日",
        "최종 업데이트 2026년 8월 29일",
        "Laatst bijgewerkt op 29 augustus 2026",
        "Última atualização em 29 de agosto de 2026",
        "最后更新于 2026 年 8 月 29 日"),

    "Dollop does not collect any data.": (
        "Dollop erfasst keinerlei Daten.",
        "Dollop no recopila ningún dato.",
        "Dollop no recopila ningún dato.",
        "Dollop ne collecte aucune donnée.",
        "Dollop non raccoglie alcun dato.",
        "Dollop はいかなるデータも収集しません。",
        "Dollop은 어떤 데이터도 수집하지 않습니다.",
        "Dollop verzamelt geen enkele gegevens.",
        "O Dollop não coleta nenhum dado.",
        "Dollop 不收集任何数据。"),

    "There is no account to create, no\n    analytics, no advertising, no tracking, and no "
    "third-party code of any kind in the app. This is\n    not a policy about how carefully your "
    "information is handled. There is no information to\n    handle.": (
        "Es gibt kein Konto anzulegen, keine Analyse, keine Werbung, kein Tracking und keinerlei "
        "Fremdcode in der App. Das hier ist keine Erklärung darüber, wie sorgfältig mit deinen "
        "Daten umgegangen wird. Es gibt keine Daten, mit denen umzugehen wäre.",
        "No hay cuenta que crear, ni analítica, ni publicidad, ni seguimiento, ni código de "
        "terceros de ningún tipo en la app. Esto no es una política sobre con cuánto cuidado se "
        "tratan tus datos. No hay datos que tratar.",
        "No hay cuenta que crear, ni analítica, ni publicidad, ni rastreo, ni código de terceros de "
        "ningún tipo en la app. Esto no es una política sobre con cuánto cuidado se tratan tus "
        "datos. No hay datos que tratar.",
        "Il n'y a pas de compte à créer, pas d'analytique, pas de publicité, pas de pistage, et "
        "aucun code tiers d'aucune sorte dans l'app. Ceci n'est pas une politique sur le soin avec "
        "lequel vos informations sont traitées. Il n'y a pas d'informations à traiter.",
        "Non c'è un account da creare, non c'è analitica, non c'è pubblicità, non c'è "
        "tracciamento e non c'è codice di terze parti di alcun tipo nell'app. Questa non è "
        "un'informativa su quanta cura si mette nel trattare i tuoi dati. Non ci sono dati da "
        "trattare.",
        "作成するアカウントはなく、解析も広告もトラッキングもなく、第三者のコードも一切"
        "入っていません。これは、あなたの情報がどれだけ丁寧に扱われるかについての方針では"
        "ありません。扱う情報がそもそもありません。",
        "만들 계정도 없고, 분석도 광고도 추적도 없으며, 어떤 종류의 서드파티 코드도 앱에 들어 있지 "
        "않습니다. 이것은 당신의 정보를 얼마나 조심스럽게 다루는지에 대한 방침이 아닙니다. 다룰 "
        "정보 자체가 없습니다.",
        "Er is geen account aan te maken, geen analytics, geen advertenties, geen tracking, en geen "
        "code van derden van welke aard dan ook in de app. Dit is geen beleid over hoe zorgvuldig "
        "je gegevens worden behandeld. Er zijn geen gegevens om te behandelen.",
        "Não há conta a criar, nem analytics, nem publicidade, nem rastreamento, nem código de "
        "terceiros de qualquer tipo no app. Esta não é uma política sobre com quanto cuidado suas "
        "informações são tratadas. Não há informação nenhuma a tratar.",
        "没有需要注册的账号，没有统计分析，没有广告，没有追踪，App 里也没有任何第三方代码。"
        "这不是一份关于你的信息被如何小心处理的说明。这里根本没有信息需要处理。"),

    "What leaves your phone": (
        "Was dein Telefon verlässt",
        "Qué sale de tu teléfono",
        "Qué sale de tu teléfono",
        "Ce qui sort de votre téléphone",
        "Che cosa esce dal tuo telefono",
        "端末から出ていくもの",
        "휴대폰 밖으로 나가는 것",
        "Wat je telefoon verlaat",
        "O que sai do seu telefone",
        "有什么会离开你的手机"),

    "Nothing.": (
        "Nichts.", "Nada.", "Nada.", "Rien.", "Niente.",
        "何もありません。", "아무것도 없습니다.", "Niets.", "Nada.", "什么都没有。"),

    "The app contains no networking code at all: there is no server on\n    this side and nothing "
    "in Dollop that could talk to one. It works exactly the same with the phone\n    in airplane "
    "mode, and the only address anywhere in it is a link out to a page on this website,\n    which "
    "opens in your browser if you tap it.": (
        "Die App enthält überhaupt keinen Netzwerkcode: es gibt auf dieser Seite keinen Server und "
        "in Dollop nichts, das mit einem sprechen könnte. Sie funktioniert im Flugmodus genau "
        "gleich, und die einzige Adresse, die überhaupt darin vorkommt, ist ein Link auf eine Seite "
        "dieser Website, der sich in deinem Browser öffnet, wenn du ihn antippst.",
        "La app no contiene nada de código de red: no hay ningún servidor de este lado y no hay "
        "nada en Dollop que pudiera hablar con uno. Funciona exactamente igual con el teléfono en "
        "modo avión, y la única dirección que aparece en toda la app es un enlace a una página de "
        "esta web, que se abre en tu navegador si lo tocas.",
        "La app no contiene nada de código de red: no hay ningún servidor de este lado y no hay "
        "nada en Dollop que pudiera hablar con uno. Funciona exactamente igual con el teléfono en "
        "modo avión, y la única dirección que aparece en toda la app es un enlace a una página de "
        "este sitio, que se abre en tu navegador si lo tocas.",
        "L'app ne contient aucun code réseau : il n'y a pas de serveur de ce côté et rien dans "
        "Dollop qui pourrait parler à l'un d'eux. Elle fonctionne exactement pareil avec le "
        "téléphone en mode avion, et la seule adresse qui figure dedans est un lien vers une page "
        "de ce site, qui s'ouvre dans votre navigateur si vous le touchez.",
        "L'app non contiene alcun codice di rete: non c'è un server da questa parte e non c'è nulla "
        "in Dollop che potrebbe parlarci. Funziona esattamente allo stesso modo con il telefono in "
        "modalità aereo, e l'unico indirizzo presente al suo interno è un collegamento a una pagina "
        "di questo sito, che si apre nel tuo browser se lo tocchi.",
        "アプリには通信のコードがまったく入っていません。こちら側にサーバーはなく、Dollop の中に"
        "サーバーと話せるものもありません。機内モードでもまったく同じように動きます。アプリの中に"
        "ある唯一のアドレスは、このサイトのページへのリンクで、タップするとブラウザで開きます。",
        "앱에는 네트워크 코드가 전혀 들어 있지 않습니다. 이쪽에는 서버가 없고, Dollop 안에는 "
        "서버와 이야기할 수 있는 것도 없습니다. 비행기 모드에서도 똑같이 작동하며, 앱 안에 있는 "
        "유일한 주소는 이 웹사이트의 한 페이지로 가는 링크로, 누르면 브라우저에서 열립니다.",
        "De app bevat überhaupt geen netwerkcode: aan deze kant is er geen server en in Dollop zit "
        "niets dat met een server zou kunnen praten. Hij werkt precies hetzelfde met de telefoon in "
        "vliegtuigmodus, en het enige adres dat er ergens in staat is een link naar een pagina op "
        "deze website, die in je browser opent als je erop tikt.",
        "O app não contém nenhum código de rede: não há servidor deste lado e não há nada no Dollop "
        "que pudesse falar com um. Ele funciona exatamente igual com o telefone em modo avião, e o "
        "único endereço que existe nele é um link para uma página deste site, que abre no seu "
        "navegador se você tocar.",
        "App 里完全没有联网代码：这一侧没有服务器，Dollop 里也没有任何能和服务器说话的东西。"
        "在飞行模式下它的表现完全一样。整个 App 里唯一的一个网址，是指向本站某个页面的链接，"
        "点它会在你的浏览器里打开。"),

    "The daily color": (
        "Die Tagesfarbe",
        "El color del día",
        "El color del día",
        "La couleur du jour",
        "Il colore del giorno",
        "その日の色",
        "오늘의 색",
        "De kleur van de dag",
        "A cor do dia",
        "每日的颜色"),

    "Everyone gets the same color each day, and it is not downloaded. The date is turned into a\n"
    "    number and the number picks a color out of a list the app already carries.": (
        "Alle bekommen jeden Tag dieselbe Farbe, und sie wird nicht heruntergeladen. Das Datum wird "
        "in eine Zahl verwandelt, und die Zahl greift einen Farbton aus einer Liste, die die App "
        "ohnehin schon mitbringt.",
        "Todo el mundo recibe el mismo color cada día, y no se descarga. La fecha se convierte en "
        "un número y el número elige un color de una lista que la app ya lleva dentro.",
        "Todos reciben el mismo color cada día, y no se descarga. La fecha se convierte en un "
        "número y el número elige un color de una lista que la app ya trae dentro.",
        "Tout le monde reçoit la même couleur chaque jour, et elle n'est pas téléchargée. La date "
        "est transformée en nombre, et ce nombre choisit une couleur dans une liste que l'app "
        "contient déjà.",
        "Tutti ricevono lo stesso colore ogni giorno, e non viene scaricato. La data viene "
        "trasformata in un numero e il numero pesca un colore da un elenco che l'app porta già con "
        "sé.",
        "その日の色は全員同じで、ダウンロードはされません。日付が数に変換され、その数が、"
        "アプリがもともと持っている一覧から色をひとつ選びます。",
        "오늘의 색은 모두에게 같고, 내려받지 않습니다. 날짜가 숫자로 바뀌고, 그 숫자가 앱이 이미 "
        "가지고 있는 목록에서 색을 하나 고릅니다.",
        "Iedereen krijgt elke dag dezelfde kleur, en die wordt niet gedownload. De datum wordt "
        "omgezet in een getal, en dat getal pikt een kleur uit een lijst die de app al bij zich "
        "draagt.",
        "Todo mundo recebe a mesma cor por dia, e ela não é baixada. A data vira um número e o "
        "número escolhe uma cor de uma lista que o app já carrega.",
        "所有人每天拿到的颜色都一样，而且它不是下载来的。日期被换算成一个数，这个数从 App "
        "本来就带着的一份清单里挑出一个颜色。"),

    "Nobody is\n    counted, and no request is made to find out what today's color is.": (
        "Niemand wird gezählt, und es wird keine Anfrage gestellt, um herauszufinden, welche Farbe "
        "heute dran ist.",
        "No se cuenta a nadie, y no se hace ninguna petición para averiguar cuál es el color de "
        "hoy.",
        "No se cuenta a nadie, y no se hace ninguna petición para averiguar cuál es el color de "
        "hoy.",
        "Personne n'est compté, et aucune requête n'est faite pour savoir quelle est la couleur du "
        "jour.",
        "Nessuno viene contato, e non viene fatta alcuna richiesta per sapere qual è il colore di "
        "oggi.",
        "誰も数えられませんし、今日の色を知るための通信も行われません。",
        "아무도 집계되지 않으며, 오늘의 색이 무엇인지 알아내기 위한 요청도 보내지 않습니다.",
        "Niemand wordt geteld, en er wordt geen verzoek gedaan om te weten te komen wat de kleur "
        "van vandaag is.",
        "Ninguém é contado, e nenhuma requisição é feita para descobrir qual é a cor de hoje.",
        "没有人会被计数，也不会为了知道今天是什么颜色而发出任何请求。"),

    "Your photographs": (
        "Deine Fotos", "Tus fotos", "Tus fotos", "Vos photos", "Le tue foto",
        "あなたの写真", "당신의 사진", "Jouw foto's", "Suas fotos", "你的照片"),

    "The From Life mode asks the camera or your photo library for one picture so you can point at "
    "a\n    color inside it. That image is read on your device, the color under your finger is "
    "measured, and\n    that is the end of it.": (
        "Der Modus Nach der Natur bittet die Kamera oder deine Fotomediathek um ein einziges Bild, "
        "damit du auf eine Farbe darin zeigen kannst. Dieses Bild wird auf deinem Gerät gelesen, "
        "die Farbe unter deinem Finger wird gemessen, und damit ist es vorbei.",
        "El modo Del natural le pide a la cámara o a tu fototeca una sola imagen para que puedas "
        "señalar un color dentro de ella. Esa imagen se lee en tu dispositivo, se mide el color que "
        "hay bajo tu dedo, y ahí se acaba.",
        "El modo Del natural le pide a la cámara o a tu fototeca una sola imagen para que puedas "
        "señalar un color dentro de ella. Esa imagen se lee en tu dispositivo, se mide el color que "
        "hay bajo tu dedo, y ahí se acaba.",
        "Le mode D'après nature demande à l'appareil photo ou à votre photothèque une seule image "
        "pour que vous puissiez désigner une couleur dedans. Cette image est lue sur votre "
        "appareil, la couleur sous votre doigt est mesurée, et c'est tout.",
        "La modalità Dal vero chiede alla fotocamera o alla tua libreria una sola immagine perché "
        "tu possa indicare un colore al suo interno. Quell'immagine viene letta sul tuo "
        "dispositivo, il colore sotto il tuo dito viene misurato, e finisce lì.",
        "実物からのモードは、その中の色を指せるように、カメラか写真ライブラリから一枚だけ画像を"
        "受け取ります。その画像は端末の中で読まれ、指の下の色が測られ、それで終わりです。",
        "실물에서 모드는 그 안의 색을 짚을 수 있도록 카메라나 사진 보관함에서 사진 한 장을 "
        "받습니다. 그 이미지는 기기 안에서 읽히고, 손가락 아래의 색이 측정되고, 거기서 끝납니다.",
        "De modus Naar de natuur vraagt de camera of je fotobibliotheek om één afbeelding zodat je "
        "een kleur erin kunt aanwijzen. Die afbeelding wordt op je toestel gelezen, de kleur onder "
        "je vinger wordt gemeten, en daarmee is het klaar.",
        "O modo Do natural pede à câmera ou à sua fototeca uma única imagem para que você possa "
        "apontar uma cor dentro dela. Essa imagem é lida no seu aparelho, a cor sob o seu dedo é "
        "medida, e acaba aí.",
        "写生模式会向相机或你的照片图库要一张图片，好让你在里面指一个颜色。那张图片在你的设备上"
        "读取，测出你手指下面的颜色，到此为止。"),

    "It is never uploaded, never stored anywhere but where you already\n    keep it, and never "
    "sent to anyone.": (
        "Es wird nie hochgeladen, nirgendwo anders gespeichert als dort, wo du es ohnehin schon "
        "hast, und nie an irgendjemanden geschickt.",
        "Nunca se sube, nunca se guarda en ningún sitio que no sea donde ya la tienes, y nunca se "
        "envía a nadie.",
        "Nunca se sube, nunca se guarda en ningún lugar que no sea donde ya la tienes, y nunca se "
        "envía a nadie.",
        "Elle n'est jamais téléversée, jamais stockée ailleurs que là où vous la gardez déjà, et "
        "jamais envoyée à qui que ce soit.",
        "Non viene mai caricata, mai conservata da nessuna parte se non dove già la tieni tu, e mai "
        "inviata a nessuno.",
        "アップロードされることも、あなたがすでに置いている場所以外に保存されることも、誰かに"
        "送られることもありません。",
        "업로드되지 않고, 당신이 이미 보관하고 있는 곳 말고 어디에도 저장되지 않으며, 누구에게도 "
        "보내지지 않습니다.",
        "Ze wordt nooit geüpload, nooit ergens anders bewaard dan waar je haar al bewaart, en nooit "
        "naar iemand gestuurd.",
        "Ela nunca é enviada para lugar nenhum, nunca é guardada em outro lugar além de onde você "
        "já a guarda, e nunca é mandada para ninguém.",
        "它不会被上传，不会被保存在你原本存放它的地方之外的任何位置，也不会被发给任何人。"),

    "If you would rather not grant the permission, every\n    other mode works without it.": (
        "Wenn du die Berechtigung lieber nicht erteilen möchtest: jeder andere Modus kommt ohne sie "
        "aus.",
        "Si prefieres no dar el permiso, todos los demás modos funcionan sin él.",
        "Si prefieres no dar el permiso, todos los demás modos funcionan sin él.",
        "Si vous préférez ne pas accorder l'autorisation, tous les autres modes fonctionnent sans "
        "elle.",
        "Se preferisci non concedere il permesso, tutte le altre modalità funzionano senza.",
        "許可を出したくなければ、ほかのモードはすべてそれなしで動きます。",
        "권한을 주고 싶지 않다면, 나머지 모드는 모두 그것 없이 동작합니다.",
        "Wil je de toestemming liever niet geven, dan werkt elke andere modus ook zonder.",
        "Se você preferir não dar a permissão, todos os outros modos funcionam sem ela.",
        "如果你不想给这个权限，其他所有模式都不需要它也能玩。"),

    "What is saved, and where": (
        "Was gespeichert wird, und wo",
        "Qué se guarda y dónde",
        "Qué se guarda y dónde",
        "Ce qui est enregistré, et où",
        "Che cosa viene salvato, e dove",
        "何が、どこに保存されるか",
        "무엇이, 어디에 저장되는가",
        "Wat er wordt bewaard, en waar",
        "O que é salvo, e onde",
        "保存了什么，保存在哪里"),

    "Your creature, its DNA, whether you have played today, your daily streak, the sound setting "
    "and\n    the fact that you have seen the introduction are all stored on the device in the "
    "app's own\n    settings. They stay on that phone. Deleting the app deletes them, which is the "
    "only way to erase\n    them and does not require asking anybody.": (
        "Dein Wesen, seine DNA, ob du heute gespielt hast, deine tägliche Serie, die "
        "Toneinstellung und die Tatsache, dass du die Einführung gesehen hast, liegen alle auf dem "
        "Gerät in den eigenen Einstellungen der App. Sie bleiben auf diesem Telefon. Wer die App "
        "löscht, löscht sie mit, und das ist der einzige Weg, sie zu entfernen, und dafür muss "
        "niemand gefragt werden.",
        "Tu criatura, su ADN, si has jugado hoy, tu racha diaria, el ajuste de sonido y el hecho de "
        "que has visto la introducción se guardan todos en el dispositivo, en los ajustes propios "
        "de la app. Se quedan en ese teléfono. Borrar la app los borra, que es la única manera de "
        "eliminarlos y no requiere pedírselo a nadie.",
        "Tu criatura, su ADN, si has jugado hoy, tu racha diaria, el ajuste de sonido y el hecho de "
        "que has visto la introducción se guardan todos en el dispositivo, en los ajustes propios "
        "de la app. Se quedan en ese teléfono. Borrar la app los borra, que es la única manera de "
        "eliminarlos y no requiere pedírselo a nadie.",
        "Votre créature, son ADN, le fait que vous ayez joué aujourd'hui, votre série quotidienne, "
        "le réglage du son et le fait que vous ayez vu l'introduction sont tous enregistrés sur "
        "l'appareil, dans les réglages propres à l'app. Ils restent sur ce téléphone. Supprimer "
        "l'app les supprime, ce qui est la seule façon de les effacer et ne demande de le "
        "demander à personne.",
        "La tua creatura, il suo DNA, se hai giocato oggi, la tua serie quotidiana, "
        "l'impostazione del suono e il fatto che hai visto l'introduzione sono tutti salvati sul "
        "dispositivo, nelle impostazioni proprie dell'app. Restano su quel telefono. Eliminare "
        "l'app li elimina, ed è l'unico modo per cancellarli, senza doverlo chiedere a nessuno.",
        "あなたの生きもの、その DNA、今日遊んだかどうか、連続日数、サウンドの設定、そして"
        "はじめの説明を見たかどうかは、すべて端末の中のアプリ自身の設定に保存されます。その"
        "端末から出ません。アプリを削除すればまとめて消え、それが唯一の消し方で、誰かに頼む"
        "必要はありません。",
        "당신의 생물, 그 DNA, 오늘 플레이했는지 여부, 연속 일수, 소리 설정, 그리고 소개를 봤다는 "
        "사실은 모두 기기 안의 앱 자체 설정에 저장됩니다. 그 휴대폰에서 나가지 않습니다. 앱을 "
        "지우면 함께 지워지고, 그것이 유일한 삭제 방법이며 누구에게 요청할 필요도 없습니다.",
        "Je wezen, zijn DNA, of je vandaag hebt gespeeld, je dagelijkse reeks, de geluidsinstelling "
        "en het feit dat je de introductie hebt gezien staan allemaal op het toestel, in de eigen "
        "instellingen van de app. Ze blijven op die telefoon. De app verwijderen verwijdert ze, en "
        "dat is de enige manier om ze te wissen, en daar hoef je niemand voor te vragen.",
        "Sua criatura, o DNA dela, se você jogou hoje, sua sequência diária, o ajuste de som e o "
        "fato de você ter visto a introdução ficam todos no aparelho, nos ajustes do próprio app. "
        "Eles ficam naquele telefone. Apagar o app apaga tudo isso, que é a única forma de "
        "eliminá-los e não exige pedir a ninguém.",
        "你的小生物、它的 DNA、你今天是否玩过、你的连续天数、声音开关，以及你已经看过引导这件事，"
        "全都保存在设备上、App 自己的设置里。它们不会离开那台手机。删除 App 就会把它们一起删掉，"
        "那也是唯一的清除方式，而且不需要向任何人申请。"),

    "Purchases": (
        "Käufe", "Compras", "Compras", "Achats", "Acquisti",
        "購入について", "구매", "Aankopen", "Compras", "购买"),

    "The one purchase that unlocks Blind, Precise and From Life is sold through Apple's In-App\n"
    "    Purchase system. Apple takes the payment and tells the app whether it went through.": (
        "Der eine Kauf, der Blind, Präzise und Nach der Natur freischaltet, läuft über Apples "
        "In-App-Kaufsystem. Apple nimmt die Zahlung entgegen und sagt der App, ob sie durchgegangen "
        "ist.",
        "La única compra que desbloquea A ciegas, Preciso y Del natural se vende a través del "
        "sistema de compras dentro de la app de Apple. Apple cobra el pago y le dice a la app si ha "
        "salido bien.",
        "La única compra que desbloquea A ciegas, Preciso y Del natural se vende a través del "
        "sistema de compras dentro de la app de Apple. Apple cobra el pago y le dice a la app si "
        "salió bien.",
        "L'unique achat qui déverrouille À l'aveugle, Précis et D'après nature passe par le système "
        "d'achat intégré d'Apple. Apple encaisse le paiement et dit à l'app s'il est passé.",
        "L'unico acquisto che sblocca Alla cieca, Preciso e Dal vero è venduto tramite il sistema "
        "di acquisti in-app di Apple. Apple incassa il pagamento e dice all'app se è andato a buon "
        "fine.",
        "ブラインド・精密・実物からを開く唯一の購入は、Apple のアプリ内課金の仕組みを通して"
        "行われます。支払いは Apple が受け取り、通ったかどうかだけがアプリに伝えられます。",
        "블라인드, 정밀, 실물에서를 여는 그 한 번의 구매는 Apple의 앱 내 구입 시스템을 통해 "
        "이루어집니다. 결제는 Apple이 받고, 통과했는지 여부만 앱에 전달됩니다.",
        "De ene aankoop die Blind, Precies en Naar de natuur ontgrendelt, loopt via Apple's "
        "in-app-aankoopsysteem. Apple int de betaling en vertelt de app of die is gelukt.",
        "A única compra que desbloqueia Às cegas, Preciso e Do natural é vendida pelo sistema de "
        "compra no app da Apple. A Apple recebe o pagamento e diz ao app se ele passou.",
        "解锁盲配、精准和写生的那一次购买，是通过 Apple 的 App 内购买系统完成的。"
        "款项由 Apple 收取，App 只会知道这笔购买是否成功。"),

    "Your payment details, your name and your email address are never seen on this\n    side.": (
        "Deine Zahlungsdaten, dein Name und deine E-Mail-Adresse werden auf dieser Seite nie "
        "gesehen.",
        "Tus datos de pago, tu nombre y tu correo electrónico nunca se ven de este lado.",
        "Tus datos de pago, tu nombre y tu correo electrónico nunca se ven de este lado.",
        "Vos coordonnées de paiement, votre nom et votre adresse e-mail ne sont jamais vus de ce "
        "côté.",
        "I tuoi dati di pagamento, il tuo nome e il tuo indirizzo email non vengono mai visti da "
        "questa parte.",
        "支払い情報も、名前も、メールアドレスも、こちら側から見えることはありません。",
        "결제 정보도, 이름도, 이메일 주소도 이쪽에서는 전혀 보이지 않습니다.",
        "Je betaalgegevens, je naam en je e-mailadres worden aan deze kant nooit gezien.",
        "Seus dados de pagamento, seu nome e seu e-mail nunca são vistos deste lado.",
        "你的支付信息、姓名和电子邮件地址，在这一侧从来看不到。"),

    "Restoring a purchase asks Apple, not us.": (
        "Ein Kauf wiederherstellen fragt Apple, nicht uns.",
        "Restaurar una compra le pregunta a Apple, no a nosotros.",
        "Restaurar una compra le pregunta a Apple, no a nosotros.",
        "Restaurer un achat interroge Apple, pas nous.",
        "Ripristinare un acquisto lo chiede ad Apple, non a noi.",
        "購入の復元は、こちらではなく Apple に問い合わせます。",
        "구매 복원은 우리가 아니라 Apple에 묻습니다.",
        "Een aankoop herstellen vraagt het aan Apple, niet aan ons.",
        "Restaurar uma compra pergunta à Apple, não a nós.",
        "恢复购买问的是 Apple，不是我们。"),

    "Children": (
        "Kinder", "Menores", "Menores", "Enfants", "Bambini",
        "子どもについて", "어린이", "Kinderen", "Crianças", "儿童"),

    "The app is rated 4+ and is safe for any age, for the plain reason that it collects nothing "
    "from\n    anybody, regardless of how old they are. There is nothing in it to buy other than "
    "the single\n    unlock, no chat, no links to anywhere except this website, and nothing that "
    "asks for a name.": (
        "Die App ist mit 4+ bewertet und für jedes Alter unbedenklich, aus dem einfachen Grund, "
        "dass sie von niemandem etwas erfasst, egal wie alt er ist. Es gibt darin außer der einen "
        "Freischaltung nichts zu kaufen, keinen Chat, keine Links außer auf diese Website und "
        "nichts, das nach einem Namen fragt.",
        "La app está clasificada 4+ y es segura a cualquier edad, por la sencilla razón de que no "
        "recopila nada de nadie, tenga la edad que tenga. Dentro no hay nada que comprar aparte del "
        "único desbloqueo, no hay chat, no hay enlaces a ninguna parte salvo a esta web, y no hay "
        "nada que pida un nombre.",
        "La app está clasificada 4+ y es segura a cualquier edad, por la sencilla razón de que no "
        "recopila nada de nadie, tenga la edad que tenga. Dentro no hay nada que comprar aparte del "
        "único desbloqueo, no hay chat, no hay enlaces a ninguna parte salvo a este sitio, y no hay "
        "nada que pida un nombre.",
        "L'app est classée 4+ et convient à tout âge, pour la raison toute simple qu'elle ne "
        "collecte rien de personne, quel que soit son âge. Il n'y a rien à y acheter en dehors de "
        "l'unique déverrouillage, pas de messagerie, aucun lien vers ailleurs que ce site, et rien "
        "qui demande un nom.",
        "L'app è classificata 4+ ed è sicura a qualsiasi età, per il semplice motivo che non "
        "raccoglie nulla da nessuno, indipendentemente dall'età. Al suo interno non c'è nulla da "
        "comprare oltre all'unico sblocco, non c'è chat, non ci sono collegamenti se non a questo "
        "sito, e non c'è nulla che chieda un nome.",
        "このアプリのレーティングは 4+ で、どの年齢でも安全です。理由は単純で、相手が何歳で"
        "あろうと何も収集しないからです。ひとつのアンロック以外に買うものはなく、チャットも"
        "なく、このサイト以外へのリンクもなく、名前を尋ねるものもありません。",
        "이 앱은 4+ 등급이며 어떤 나이에도 안전합니다. 이유는 단순합니다. 나이와 상관없이 "
        "누구에게서도 아무것도 수집하지 않기 때문입니다. 단 하나의 잠금 해제 말고는 살 것이 없고, "
        "채팅도 없고, 이 웹사이트 말고 다른 곳으로 가는 링크도 없으며, 이름을 묻는 것도 없습니다.",
        "De app heeft een 4+-classificatie en is veilig op elke leeftijd, om de simpele reden dat "
        "hij van niemand iets verzamelt, hoe oud diegene ook is. Er valt niets in te kopen behalve "
        "de ene ontgrendeling, er is geen chat, er zijn geen links naar ergens anders dan deze "
        "website, en er is niets dat om een naam vraagt.",
        "O app tem classificação 4+ e é seguro em qualquer idade, pela razão simples de que não "
        "coleta nada de ninguém, seja qual for a idade. Não há nada para comprar dentro dele além "
        "do único desbloqueio, não há chat, não há links para lugar nenhum a não ser este site, e "
        "não há nada que peça um nome.",
        "这款 App 的分级是 4+，任何年龄都可以安心使用，原因很简单：无论对方多大，它都不收集"
        "任何东西。除了那一次解锁之外没有别的可买，没有聊天，除了本站之外没有任何外部链接，"
        "也没有任何地方会问你的名字。"),

    "Changes": (
        "Änderungen", "Cambios", "Cambios", "Modifications", "Modifiche",
        "変更について", "변경 사항", "Wijzigingen", "Alterações", "变更"),

    "If this ever changes, the change will appear here with a new date, and any version of the "
    "app\n    that collects something will say so on its App Store page before you install it.": (
        "Falls sich das jemals ändert, steht die Änderung hier mit einem neuen Datum, und jede "
        "Version der App, die etwas erfasst, sagt das auf ihrer App-Store-Seite, bevor du sie "
        "installierst.",
        "Si esto cambia alguna vez, el cambio aparecerá aquí con una fecha nueva, y cualquier "
        "versión de la app que recopile algo lo dirá en su página del App Store antes de que la "
        "instales.",
        "Si esto cambia alguna vez, el cambio aparecerá aquí con una fecha nueva, y cualquier "
        "versión de la app que recopile algo lo dirá en su página del App Store antes de que la "
        "instales.",
        "Si cela change un jour, le changement apparaîtra ici avec une nouvelle date, et toute "
        "version de l'app qui collecte quelque chose le dira sur sa page App Store avant que vous "
        "ne l'installiez.",
        "Se un giorno cambierà, il cambiamento comparirà qui con una data nuova, e qualsiasi "
        "versione dell'app che raccolga qualcosa lo dirà sulla sua pagina dell'App Store prima che "
        "tu la installi.",
        "もしこれが変わることがあれば、新しい日付とともにここに書かれます。何かを収集する"
        "バージョンが出るなら、インストールする前に App Store のページでそう明記されます。",
        "혹시 이 내용이 바뀌면 새 날짜와 함께 여기에 적힙니다. 무언가를 수집하는 버전이 나온다면, "
        "설치하기 전에 App Store 페이지에 그렇게 적혀 있을 것입니다.",
        "Mocht dit ooit veranderen, dan verschijnt de wijziging hier met een nieuwe datum, en elke "
        "versie van de app die iets verzamelt zegt dat op haar App Store-pagina voordat je haar "
        "installeert.",
        "Se isso mudar algum dia, a mudança vai aparecer aqui com uma data nova, e qualquer versão "
        "do app que colete algo vai dizer isso na página dele na App Store antes de você instalar.",
        "如果这一点将来有变，改动会带着新的日期出现在这里；任何会收集数据的版本，都会在你安装"
        "之前，在它的 App Store 页面上写明。"),

    "Getting in touch": (
        "Kontakt", "Contacto", "Contacto", "Nous écrire", "Contatti",
        "連絡", "문의", "Contact", "Fale comigo", "联系"),

    "Questions go to": (
        "Fragen gehen an", "Las preguntas van a", "Las preguntas van a",
        "Les questions vont à", "Le domande vanno a",
        "質問の宛先は", "질문은", "Vragen gaan naar", "Perguntas vão para", "问题请发到"),

    ", which reaches me directly. An email sent\n    there is an email, and is handled like one: "
    "read, replied to, and not fed into anything.": (
        ", das mich direkt erreicht. Eine E-Mail dorthin ist eine E-Mail und wird auch so "
        "behandelt: gelesen, beantwortet und in nichts weiter eingespeist.",
        ", que me llega directamente. Un correo enviado ahí es un correo, y se trata como tal: se "
        "lee, se responde y no se mete en nada más.",
        ", que me llega directamente. Un correo enviado ahí es un correo, y se trata como tal: se "
        "lee, se responde y no se mete en nada más.",
        ", qui m'arrive directement. Un e-mail envoyé là est un e-mail, et il est traité comme "
        "tel : lu, auquel on répond, et versé dans rien du tout.",
        ", che arriva direttamente a me. Un'email mandata lì è un'email, e viene trattata come "
        "tale: letta, a cui si risponde, e non data in pasto a nulla.",
        "。私に直接届きます。そこに届いたメールはただのメールで、そのとおりに扱われます。"
        "読んで、返事をして、それ以外の何かに流し込むことはありません。",
        "로 보내 주세요. 저에게 바로 옵니다. 거기로 온 메일은 그냥 메일이고, 그렇게 다뤄집니다. "
        "읽고, 답장하고, 다른 무엇에도 집어넣지 않습니다.",
        ", dat mij direct bereikt. Een mail die daarheen gaat is een mail, en wordt ook zo "
        "behandeld: gelezen, beantwoord, en nergens in gestopt.",
        ", que chega direto a mim. Um e-mail enviado para lá é um e-mail, e é tratado como tal: "
        "lido, respondido, e não jogado dentro de mais nada.",
        "，这会直接到我这里。发到那里的邮件就是邮件，也会被当作邮件对待：读，回复，"
        "不会被拿去喂给任何别的东西。"),

    "Built in Fort Worth, Texas": (
        "Gebaut in Fort Worth, Texas",
        "Hecho en Fort Worth, Texas",
        "Hecho en Fort Worth, Texas",
        "Conçu à Fort Worth, Texas",
        "Realizzato a Fort Worth, Texas",
        "テキサス州フォートワースにて制作",
        "미국 텍사스주 포트워스에서 제작",
        "Gemaakt in Fort Worth, Texas",
        "Feito em Fort Worth, Texas",
        "于美国得克萨斯州沃思堡制作"),
}
