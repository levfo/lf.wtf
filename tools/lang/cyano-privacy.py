"""lf.wtf/cyano/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Shares most of its shape with FRMT's policy but not its wording, and the differences are the part
that matters: CYANO reads a picture rather than capturing one, and it has a single in-app purchase
that FRMT does not. Both are translated as written rather than harmonised.
"""

KEEP = {"CYANO", "iPhone", "lf.wtf", "App Store", "https://lf.wtf/cyano",
        "Last updated: 16 August 2026"}

T = {
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "Privacy Policy": ("Datenschutzerklärung", "Política de privacidad",
                       "Política de privacidad", "Politique de confidentialité",
                       "Informativa sulla privacy", "プライバシーポリシー",
                       "개인정보 처리방침", "Privacybeleid", "Política de privacidade",
                       "隐私政策"),
    "CYANO collects nothing and has no way to. There is no account, no analytics and no server.": (
        "CYANO sammelt nichts und hat auch keine Möglichkeit dazu. Es gibt kein Konto, keine "
        "Analyse und keinen Server.",
        "CYANO no recoge nada y no tiene forma de hacerlo. No hay cuenta, ni analíticas, ni "
        "servidor.",
        "CYANO no recoge nada y no tiene forma de hacerlo. No hay cuenta, ni analíticas, ni "
        "servidor.",
        "CYANO ne collecte rien et n'a aucun moyen de le faire. Il n'y a pas de compte, pas "
        "d'analytique et pas de serveur.",
        "CYANO non raccoglie niente e non ha modo di farlo. Non c'è account, non ci sono analisi e "
        "non c'è server.",
        "CYANO は何も収集しませんし、収集する手段も持っていません。アカウントも、解析も、"
        "サーバーもありません。",
        "CYANO는 아무것도 수집하지 않으며, 수집할 방법도 없습니다. 계정도, 분석도, 서버도 없습니다.",
        "CYANO verzamelt niets en heeft er ook geen manier toe. Er is geen account, geen analytics "
        "en geen server.",
        "O CYANO não coleta nada e não tem como coletar. Não há conta, não há análises e não há "
        "servidor.",
        "CYANO 不收集任何东西，也没有办法收集。没有账号、没有分析，也没有服务器。"),
    "The short version": ("Die Kurzfassung", "La versión corta", "La versión corta",
                          "La version courte", "La versione breve", "短く言うと",
                          "짧게 말하면", "De korte versie", "A versão curta", "简短版本"),
    "CYANO does not collect anything about you, and it has no way to. There is no account, no "
    "analytics, no advertising and no server. The app contains no networking code of its own.": (
        "CYANO sammelt nichts über dich und hat auch keine Möglichkeit dazu. Es gibt kein Konto, "
        "keine Analyse, keine Werbung und keinen Server. Die App enthält keinen eigenen "
        "Netzwerkcode.",
        "CYANO no recoge nada sobre ti, y no tiene forma de hacerlo. No hay cuenta, ni analíticas, "
        "ni publicidad, ni servidor. La app no contiene código de red propio.",
        "CYANO no recoge nada sobre ti, y no tiene forma de hacerlo. No hay cuenta, ni analíticas, "
        "ni publicidad, ni servidor. La app no contiene código de red propio.",
        "CYANO ne collecte rien à votre sujet, et n'a aucun moyen de le faire. Il n'y a pas de "
        "compte, pas d'analytique, pas de publicité et pas de serveur. L'app ne contient aucun code "
        "réseau propre.",
        "CYANO non raccoglie niente su di te, e non ha modo di farlo. Non c'è account, non ci sono "
        "analisi, non c'è pubblicità e non c'è server. L'app non contiene codice di rete proprio.",
        "CYANO はあなたについて何も収集しませんし、収集する手段も持っていません。アカウントも、"
        "解析も、広告も、サーバーもありません。アプリは独自の通信コードを持っていません。",
        "CYANO는 당신에 대해 아무것도 수집하지 않으며, 수집할 방법도 없습니다. 계정도, 분석도, "
        "광고도, 서버도 없습니다. 앱은 자체 네트워크 코드를 갖고 있지 않습니다.",
        "CYANO verzamelt niets over jou en heeft er ook geen manier toe. Er is geen account, geen "
        "analytics, geen advertenties en geen server. De app bevat geen eigen netwerkcode.",
        "O CYANO não coleta nada sobre você, e não tem como. Não há conta, não há análises, não há "
        "publicidade e não há servidor. O app não contém código de rede próprio.",
        "CYANO 不收集任何关于你的信息，也没有办法收集。没有账号、没有分析、没有广告，也没有服务器。"
        "这个应用没有自己的联网代码。"),
    "What the app stores, and where": (
        "Was die App speichert, und wo", "Qué guarda la app, y dónde", "Qué guarda la app, y dónde",
        "Ce que l'app stocke, et où", "Cosa memorizza l'app, e dove",
        "アプリが保存するもの、そしてその場所", "앱이 저장하는 것과 그 위치",
        "Wat de app opslaat, en waar", "O que o app armazena, e onde", "应用保存什么，保存在哪里"),
    "Everything stays on your iPhone.": (
        "Alles bleibt auf deinem iPhone.", "Todo se queda en tu iPhone.",
        "Todo se queda en tu iPhone.", "Tout reste sur votre iPhone.",
        "Resta tutto sul tuo iPhone.", "すべては iPhone のなかに留まります。",
        "모든 것이 당신의 iPhone 안에 남습니다.", "Alles blijft op je iPhone.",
        "Tudo fica no seu iPhone.", "一切都留在你的 iPhone 上。"),
    "Photographs.": ("Fotos.", "Fotografías.", "Fotografías.", "Photographies.", "Fotografie.",
                     "写真。", "사진.", "Foto's.", "Fotografias.", "照片。"),
    "You choose a photograph from your library and the app turns it into a cyanotype. That happens "
    "entirely on the device, using its graphics hardware. The picture you chose is read, not "
    "copied: nothing is uploaded, and nothing is kept after you close the app. When you save or "
    "share a finished print, it goes to your photo library or to whichever app you picked in the "
    "share sheet, and that is the only copy that persists.": (
        "Du wählst ein Foto aus deiner Mediathek, und die App macht daraus eine Cyanotypie. Das "
        "geschieht vollständig auf dem Gerät, mit dessen Grafikhardware. Das gewählte Bild wird "
        "gelesen, nicht kopiert: Nichts wird hochgeladen, und nichts bleibt zurück, wenn du die "
        "App schließt. Sicherst oder teilst du einen fertigen Abzug, geht er in deine Mediathek "
        "oder in die App, die du im Teilen-Menü gewählt hast, und das ist die einzige Kopie, die "
        "bestehen bleibt.",
        "Eliges una fotografía de tu fototeca y la app la convierte en cianotipia. Eso ocurre "
        "enteramente en el dispositivo, usando su hardware gráfico. La imagen que elegiste se lee, "
        "no se copia: no se sube nada, y no queda nada al cerrar la app. Cuando guardas o compartes "
        "una copia terminada, va a tu fototeca o a la app que hayas elegido en la hoja de "
        "compartir, y esa es la única copia que persiste.",
        "Eliges una fotografía de tu fototeca y la app la convierte en cianotipia. Eso ocurre "
        "enteramente en el dispositivo, usando su hardware gráfico. La imagen que elegiste se lee, "
        "no se copia: no se sube nada, y no queda nada al cerrar la app. Cuando guardas o compartes "
        "una copia terminada, va a tu fototeca o a la app que hayas elegido en la hoja de "
        "compartir, y esa es la única copia que persiste.",
        "Vous choisissez une photographie dans votre photothèque et l'app la transforme en "
        "cyanotype. Cela se passe entièrement sur l'appareil, avec son matériel graphique. L'image "
        "choisie est lue, pas copiée : rien n'est envoyé, et rien n'est conservé après la fermeture "
        "de l'app. Quand vous enregistrez ou partagez un tirage terminé, il va dans votre "
        "photothèque ou vers l'app choisie dans la feuille de partage, et c'est la seule copie qui "
        "persiste.",
        "Scegli una fotografia dalla tua libreria e l'app la trasforma in cianotipia. Succede "
        "interamente sul dispositivo, usando il suo hardware grafico. L'immagine che hai scelto "
        "viene letta, non copiata: non viene caricato niente, e non resta niente dopo che chiudi "
        "l'app. Quando salvi o condividi una stampa finita, va nella tua libreria o nell'app che "
        "hai scelto nel foglio di condivisione, e quella è l'unica copia che rimane.",
        "あなたがライブラリから写真を選ぶと、アプリがそれをサイアノタイプにします。これはすべて"
        "端末の上で、そのグラフィックスハードウェアを使って行われます。選ばれた画像は読み取られる"
        "だけで、複製はされません。何もアップロードされず、アプリを閉じたあとに残るものも"
        "ありません。仕上がったプリントを保存または共有すると、それは写真ライブラリか、"
        "共有シートで選んだアプリへ渡り、残るのはその一部だけです。",
        "당신이 보관함에서 사진을 고르면 앱이 그것을 사이아노타입으로 만듭니다. 이 일은 전부 기기 "
        "위에서, 그 그래픽 하드웨어를 써서 일어납니다. 고른 이미지는 읽힐 뿐 복사되지 않습니다. "
        "아무것도 업로드되지 않고, 앱을 닫은 뒤에 남는 것도 없습니다. 완성된 인화지를 저장하거나 "
        "공유하면 사진 보관함이나 공유 시트에서 고른 앱으로 가고, 남는 사본은 그것뿐입니다.",
        "Je kiest een foto uit je bibliotheek en de app maakt er een cyanotypie van. Dat gebeurt "
        "volledig op het toestel, met de grafische hardware ervan. Het gekozen beeld wordt gelezen, "
        "niet gekopieerd: er wordt niets geüpload, en er blijft niets achter nadat je de app sluit. "
        "Als je een afgeronde afdruk bewaart of deelt, gaat die naar je fotobibliotheek of naar de "
        "app die je in het deelmenu koos, en dat is de enige kopie die blijft.",
        "Você escolhe uma fotografia da sua fototeca e o app a transforma numa cianotipia. Isso "
        "acontece inteiramente no aparelho, usando o hardware gráfico dele. A imagem que você "
        "escolheu é lida, não copiada: nada é enviado, e nada fica depois que você fecha o app. "
        "Quando você salva ou compartilha uma cópia pronta, ela vai para a sua fototeca ou para o "
        "app que você escolheu na folha de compartilhamento, e essa é a única cópia que permanece.",
        "你从图库里选一张照片，应用把它变成蓝晒。这一切完全在设备上、用它的图形硬件完成。"
        "你选中的图像只是被读取，并不会被复制：没有任何东西被上传，关闭应用后也不会留下什么。"
        "当你保存或分享一张完成的成品时，它会进入你的照片图库，或者你在分享面板里选的那个应用，"
        "而那是唯一会留下来的副本。"),
    "Settings.": ("Einstellungen.", "Ajustes.", "Ajustes.", "Réglages.", "Impostazioni.",
                  "設定。", "설정.", "Instellingen.", "Ajustes.", "设置。"),
    "Whether you have seen the introduction, how many prints you have saved, which version last "
    "asked you for a rating, and whether the in-app purchase has been unlocked. These live in the "
    "app's own preferences and are read by nothing else.": (
        "Ob du die Einführung gesehen hast, wie viele Abzüge du gesichert hast, welche Version "
        "dich zuletzt um eine Bewertung gebeten hat, und ob der In-App-Kauf freigeschaltet ist. "
        "Das liegt in den eigenen Einstellungen der App und wird von nichts anderem gelesen.",
        "Si has visto la introducción, cuántas copias has guardado, qué versión te pidió por "
        "última vez una valoración, y si la compra dentro de la app está desbloqueada. Viven en las "
        "preferencias de la propia app y no las lee nada más.",
        "Si has visto la introducción, cuántas copias has guardado, qué versión te pidió por "
        "última vez una calificación, y si la compra dentro de la app está desbloqueada. Viven en "
        "las preferencias de la propia app y no las lee nada más.",
        "Si vous avez vu l'introduction, combien de tirages vous avez enregistrés, quelle version "
        "vous a demandé une note en dernier, et si l'achat intégré a été débloqué. Cela vit dans "
        "les préférences propres à l'app et rien d'autre ne les lit.",
        "Se hai visto l'introduzione, quante stampe hai salvato, quale versione ti ha chiesto per "
        "ultima una valutazione, e se l'acquisto in-app è stato sbloccato. Stanno nelle preferenze "
        "dell'app e non le legge nient'altro.",
        "はじめにを見たかどうか、何枚のプリントを保存したか、最後に評価を求めたのはどのバージョン"
        "か、そしてアプリ内課金が解放されているかどうか。これらはアプリ自身の設定のなかにあり、"
        "ほかの何かが読むことはありません。",
        "소개를 보았는지 여부, 인화지를 몇 장 저장했는지, 어떤 버전이 마지막으로 평가를 요청했는지, "
        "그리고 인앱 결제가 열려 있는지. 이것들은 앱 자체의 설정 안에 있고, 다른 무엇도 읽지 "
        "않습니다.",
        "Of je de introductie hebt gezien, hoeveel afdrukken je hebt bewaard, welke versie je het "
        "laatst om een beoordeling vroeg, en of de in-app-aankoop is ontgrendeld. Dat staat in de "
        "eigen voorkeuren van de app en wordt door niets anders gelezen.",
        "Se você já viu a introdução, quantas cópias salvou, qual versão pediu por último uma "
        "avaliação, e se a compra dentro do app foi liberada. Isso fica nas preferências do próprio "
        "app e nada mais lê.",
        "你是否看过介绍、保存过多少张成品、上一次请你评分的是哪个版本，"
        "以及应用内购买是否已解锁。这些存放在应用自己的偏好设置里，没有别的东西会读取。"),
    "Permissions the app asks for": (
        "Berechtigungen, die die App anfragt", "Permisos que pide la app",
        "Permisos que pide la app", "Les autorisations que l'app demande",
        "I permessi che l'app chiede", "アプリが求める許可", "앱이 요청하는 권한",
        "Toestemmingen die de app vraagt", "Permissões que o app pede", "应用请求的权限"),
    "Photo library, to add.": (
        "Mediathek, zum Hinzufügen.", "Fototeca, para añadir.", "Fototeca, para agregar.",
        "Photothèque, pour ajouter.", "Libreria foto, per aggiungere.",
        "写真ライブラリ、追加のため。", "사진 보관함, 추가를 위해.",
        "Fotobibliotheek, om toe te voegen.", "Fototeca, para adicionar.", "照片图库，用于添加。"),
    "So a finished print can be saved. The app asks only for permission to add, not to read your "
    "whole library.": (
        "Damit ein fertiger Abzug gesichert werden kann. Die App fragt nur um die Erlaubnis zum "
        "Hinzufügen, nicht zum Lesen deiner ganzen Mediathek.",
        "Para que se pueda guardar una copia terminada. La app pide solo permiso para añadir, no "
        "para leer toda tu fototeca.",
        "Para que se pueda guardar una copia terminada. La app pide solo permiso para agregar, no "
        "para leer toda tu fototeca.",
        "Pour qu'un tirage terminé puisse être enregistré. L'app demande seulement l'autorisation "
        "d'ajouter, pas de lire toute votre photothèque.",
        "Perché una stampa finita possa essere salvata. L'app chiede solo il permesso di "
        "aggiungere, non di leggere tutta la tua libreria.",
        "仕上がったプリントを保存できるようにするためです。アプリが求めるのは追加の許可だけで、"
        "ライブラリ全体を読む許可ではありません。",
        "완성된 인화지를 저장할 수 있게 하기 위해서입니다. 앱이 요청하는 것은 추가 권한뿐이고, "
        "보관함 전체를 읽는 권한이 아닙니다.",
        "Zodat een afgeronde afdruk kan worden bewaard. De app vraagt alleen toestemming om toe te "
        "voegen, niet om je hele bibliotheek te lezen.",
        "Para que uma cópia pronta possa ser salva. O app pede apenas permissão para adicionar, não "
        "para ler toda a sua fototeca.",
        "以便保存完成的成品。应用只请求添加权限，而不是读取你整个图库的权限。"),
    "Choosing a photograph": ("Ein Foto auswählen", "Elegir una fotografía",
                              "Elegir una fotografía", "Choisir une photographie",
                              "Scegliere una fotografia", "写真を選ぶこと", "사진을 고르는 것",
                              "Een foto kiezen", "Escolher uma fotografia", "选一张照片"),
    "does not need a permission at all. The picker is run by iOS, and the app receives only the "
    "single picture you select. It never sees the rest of your library.": (
        "braucht überhaupt keine Berechtigung. Die Auswahl wird von iOS ausgeführt, und die App "
        "erhält nur das eine Bild, das du auswählst. Den Rest deiner Mediathek sieht sie nie.",
        "no necesita permiso alguno. El selector lo ejecuta iOS, y la app recibe solo la única "
        "imagen que selecciones. Nunca ve el resto de tu fototeca.",
        "no necesita permiso alguno. El selector lo ejecuta iOS, y la app recibe solo la única "
        "imagen que selecciones. Nunca ve el resto de tu fototeca.",
        "ne demande aucune autorisation. Le sélecteur est exécuté par iOS, et l'app ne reçoit que "
        "la seule image que vous sélectionnez. Elle ne voit jamais le reste de votre photothèque.",
        "non richiede alcun permesso. Il selettore lo esegue iOS, e l'app riceve solo la singola "
        "immagine che selezioni. Il resto della tua libreria non lo vede mai.",
        "には、そもそも許可が要りません。ピッカーを動かすのは iOS であり、アプリが受け取るのは"
        "あなたが選んだ一枚だけです。ライブラリのそれ以外を見ることはありません。",
        "에는 애초에 권한이 필요 없습니다. 선택기는 iOS가 실행하고, 앱이 받는 것은 당신이 고른 한 "
        "장뿐입니다. 보관함의 나머지는 결코 보지 못합니다.",
        "heeft helemaal geen toestemming nodig. De kiezer wordt door iOS uitgevoerd, en de app "
        "ontvangt alleen het ene beeld dat je selecteert. De rest van je bibliotheek ziet hij nooit.",
        "não precisa de permissão nenhuma. O seletor é executado pelo iOS, e o app recebe apenas a "
        "única imagem que você selecionar. Ele nunca vê o resto da sua fototeca.",
        "根本不需要任何权限。选择器由 iOS 运行，应用只会收到你选中的那一张图像。"
        "它永远看不到你图库里的其余内容。"),
    "The in-app purchase": ("Der In-App-Kauf", "La compra dentro de la app",
                            "La compra dentro de la app", "L'achat intégré",
                            "L'acquisto in-app", "アプリ内課金について", "인앱 결제",
                            "De in-app-aankoop", "A compra dentro do app", "关于应用内购买"),
    "CYANO is free, and one optional purchase unlocks the toning baths, the remaining papers and "
    "the second sensitiser formula. That purchase is handled entirely by Apple through the App "
    "Store. The app asks the system whether the purchase has been made and receives yes or no. It "
    "never sees your Apple Account, your name or any payment detail, and no payment information is "
    "stored in the app or sent anywhere by it.": (
        "CYANO ist kostenlos, und ein optionaler Kauf schaltet die Tonbäder, die übrigen Papiere "
        "und die zweite Sensibilisatorformel frei. Dieser Kauf wird vollständig von Apple über den "
        "App Store abgewickelt. Die App fragt das System, ob der Kauf getätigt wurde, und erhält "
        "ja oder nein. Sie sieht nie deinen Apple Account, deinen Namen oder irgendein "
        "Zahlungsdetail, und in der App werden keine Zahlungsinformationen gespeichert oder von ihr "
        "irgendwohin gesendet.",
        "CYANO es gratis, y una compra opcional desbloquea los baños de virado, los papeles "
        "restantes y la segunda fórmula de sensibilizador. Esa compra la gestiona enteramente "
        "Apple a través de la App Store. La app pregunta al sistema si la compra se ha hecho y "
        "recibe sí o no. Nunca ve tu cuenta de Apple, tu nombre ni ningún dato de pago, y en la app "
        "no se guarda información de pago ni ella la envía a ninguna parte.",
        "CYANO es gratis, y una compra opcional desbloquea los baños de virado, los papeles "
        "restantes y la segunda fórmula de sensibilizador. Esa compra la gestiona enteramente "
        "Apple a través de la App Store. La app pregunta al sistema si la compra se hizo y recibe "
        "sí o no. Nunca ve tu cuenta de Apple, tu nombre ni ningún dato de pago, y en la app no se "
        "guarda información de pago ni ella la envía a ninguna parte.",
        "CYANO est gratuit, et un achat facultatif débloque les bains de virage, les papiers "
        "restants et la seconde formule de sensibilisateur. Cet achat est entièrement géré par "
        "Apple via l'App Store. L'app demande au système si l'achat a été fait et reçoit oui ou "
        "non. Elle ne voit jamais votre compte Apple, votre nom ni aucun détail de paiement, et "
        "aucune information de paiement n'est stockée dans l'app ni envoyée où que ce soit par elle.",
        "CYANO è gratis, e un acquisto facoltativo sblocca i bagni di viraggio, le carte rimanenti "
        "e la seconda formula di sensibilizzante. Quell'acquisto è gestito interamente da Apple "
        "tramite l'App Store. L'app chiede al sistema se l'acquisto è stato fatto e riceve sì o no. "
        "Non vede mai il tuo Apple Account, il tuo nome o alcun dato di pagamento, e nell'app non "
        "viene memorizzata nessuna informazione di pagamento né viene inviata da nessuna parte.",
        "CYANO は無料で、任意の購入によって調色浴、残りの紙、そして二つめの増感剤処方が"
        "使えるようになります。この購入はすべて App Store を通じて Apple が処理します。"
        "アプリはシステムに購入済みかどうかを尋ね、はい／いいえを受け取るだけです。"
        "あなたの Apple アカウントも、名前も、支払いの詳細も見ることはなく、"
        "支払い情報がアプリに保存されることも、アプリからどこかへ送られることもありません。",
        "CYANO는 무료이고, 선택 구매 한 번으로 조색액, 남은 종이들, 두 번째 감광제 조성이 열립니다. "
        "그 결제는 전부 App Store를 통해 Apple이 처리합니다. 앱은 시스템에 구매가 되었는지를 묻고 "
        "예 또는 아니요를 받을 뿐입니다. 당신의 Apple 계정도, 이름도, 결제 정보도 결코 보지 못하며, "
        "결제 정보가 앱에 저장되거나 앱이 그것을 어딘가로 보내는 일도 없습니다.",
        "CYANO is gratis, en één optionele aankoop ontgrendelt de toningbaden, de overige papieren "
        "en de tweede sensibilisatorformule. Die aankoop wordt volledig door Apple afgehandeld via "
        "de App Store. De app vraagt het systeem of de aankoop is gedaan en krijgt ja of nee. Hij "
        "ziet nooit je Apple Account, je naam of enig betaalgegeven, en er wordt geen "
        "betaalinformatie in de app opgeslagen of door de app ergens naartoe gestuurd.",
        "O CYANO é grátis, e uma compra opcional libera os banhos de viragem, os papéis restantes e "
        "a segunda fórmula de sensibilizador. Essa compra é tratada inteiramente pela Apple através "
        "da App Store. O app pergunta ao sistema se a compra foi feita e recebe sim ou não. Ele "
        "nunca vê sua Conta Apple, seu nome ou qualquer dado de pagamento, e nenhuma informação de "
        "pagamento é guardada no app nem enviada por ele para lugar algum.",
        "CYANO 是免费的，一次可选的购买会解锁调色液、其余的纸，以及第二种感光剂配方。"
        "这笔购买完全由 Apple 通过 App Store 处理。应用只是向系统询问是否已购买，"
        "并得到\"是\"或\"否\"。它永远看不到你的 Apple 账户、你的姓名或任何支付信息，"
        "应用里不会保存支付信息，也不会把它发往任何地方。"),
    "Apple's own handling of that transaction is covered by Apple's privacy policy, not this one.": (
        "Wie Apple selbst mit dieser Transaktion umgeht, regelt Apples Datenschutzerklärung, nicht "
        "diese.",
        "Cómo trata Apple esa transacción se rige por la política de privacidad de Apple, no por "
        "esta.",
        "Cómo trata Apple esa transacción se rige por la política de privacidad de Apple, no por "
        "esta.",
        "La manière dont Apple traite cette transaction relève de la politique de confidentialité "
        "d'Apple, pas de celle-ci.",
        "Il modo in cui Apple gestisce quella transazione è coperto dall'informativa sulla privacy "
        "di Apple, non da questa.",
        "その取引を Apple 自身がどう扱うかは、この方針ではなく Apple のプライバシーポリシーが"
        "定めます。",
        "그 거래를 Apple이 어떻게 다루는지는 이 방침이 아니라 Apple의 개인정보 처리방침이 "
        "정합니다.",
        "Hoe Apple die transactie zelf behandelt valt onder het privacybeleid van Apple, niet onder "
        "dit beleid.",
        "Como a Apple trata essa transação é coberto pela política de privacidade da Apple, não por "
        "esta.",
        "Apple 自己如何处理这笔交易，由 Apple 的隐私政策规定，而不是这一份。"),
    "What is not here": ("Was hier nicht ist", "Lo que no hay aquí", "Lo que no hay aquí",
                         "Ce qui n'est pas là", "Cosa non c'è", "ここにないもの",
                         "여기에 없는 것", "Wat hier niet is", "O que não há aqui",
                         "这里没有的东西"),
    "No analytics. No crash reporting. No advertising identifier. No third-party SDKs of any kind. "
    "No tracking across apps or websites. No mailing list. No cookies, because there is no website "
    "inside the app.": (
        "Keine Analyse. Keine Absturzberichte. Keine Werbe-ID. Keinerlei SDKs von Dritten. Kein "
        "Tracking über Apps oder Websites hinweg. Kein Newsletter. Keine Cookies, weil es in der "
        "App keine Website gibt.",
        "Sin analíticas. Sin informes de fallos. Sin identificador de publicidad. Sin SDK de "
        "terceros de ningún tipo. Sin seguimiento entre apps o sitios web. Sin lista de correo. Sin "
        "cookies, porque dentro de la app no hay ningún sitio web.",
        "Sin analíticas. Sin informes de fallas. Sin identificador de publicidad. Sin SDK de "
        "terceros de ningún tipo. Sin seguimiento entre apps o sitios web. Sin lista de correo. Sin "
        "cookies, porque dentro de la app no hay ningún sitio web.",
        "Pas d'analytique. Pas de rapport de plantage. Pas d'identifiant publicitaire. Aucun SDK "
        "tiers d'aucune sorte. Pas de suivi entre apps ou sites web. Pas de liste de diffusion. Pas "
        "de cookies, parce qu'il n'y a pas de site web dans l'app.",
        "Nessuna analisi. Nessuna segnalazione di crash. Nessun identificatore pubblicitario. "
        "Nessun SDK di terze parti di alcun tipo. Nessun tracciamento fra app o siti web. Nessuna "
        "mailing list. Nessun cookie, perché dentro l'app non c'è nessun sito web.",
        "解析なし。クラッシュ報告なし。広告識別子なし。いかなる第三者 SDK もなし。アプリや"
        "ウェブサイトをまたぐトラッキングなし。メーリングリストなし。クッキーもありません。"
        "アプリの中にウェブサイトが存在しないからです。",
        "분석 없음. 크래시 리포트 없음. 광고 식별자 없음. 어떤 종류의 서드파티 SDK도 없음. 앱이나 "
        "웹사이트를 넘나드는 추적 없음. 메일링 리스트 없음. 쿠키도 없습니다. 앱 안에 웹사이트가 "
        "없기 때문입니다.",
        "Geen analytics. Geen crashrapportage. Geen advertentie-identificatie. Geen SDK's van "
        "derden van welke aard dan ook. Geen tracking over apps of websites heen. Geen mailinglijst. "
        "Geen cookies, want er zit geen website in de app.",
        "Sem análises. Sem relatório de falhas. Sem identificador de publicidade. Sem SDKs de "
        "terceiros de nenhum tipo. Sem rastreamento entre apps ou sites. Sem lista de e-mails. Sem "
        "cookies, porque não há nenhum site dentro do app.",
        "没有分析。没有崩溃报告。没有广告标识符。没有任何第三方 SDK。"
        "没有跨应用或跨网站的追踪。没有邮件列表。也没有 Cookie，因为应用里根本没有网页。"),
    "Because none of this exists, there is also nothing to opt out of and no data to request or "
    "delete. Deleting the app removes its preferences with it.": (
        "Weil nichts davon existiert, gibt es auch nichts, wovon man sich abmelden könnte, und "
        "keine Daten, die man anfordern oder löschen könnte. Löschst du die App, verschwinden ihre "
        "Einstellungen mit ihr.",
        "Como nada de esto existe, tampoco hay nada de lo que darse de baja ni datos que solicitar "
        "o borrar. Borrar la app se lleva sus preferencias con ella.",
        "Como nada de esto existe, tampoco hay nada de lo que darse de baja ni datos que solicitar "
        "o borrar. Borrar la app se lleva sus preferencias con ella.",
        "Comme rien de tout cela n'existe, il n'y a rien dont se désinscrire ni de données à "
        "demander ou supprimer. Supprimer l'app emporte ses préférences avec elle.",
        "Dato che niente di tutto questo esiste, non c'è nemmeno niente da cui disiscriversi né "
        "dati da richiedere o cancellare. Eliminando l'app spariscono con essa le sue preferenze.",
        "こうしたものがそもそも存在しないため、オプトアウトすべきものも、開示や削除を請求すべき"
        "データもありません。アプリを削除すれば、その設定も一緒になくなります。",
        "이런 것들이 애초에 존재하지 않으므로, 수신을 거부할 것도, 열람이나 삭제를 요청할 데이터도 "
        "없습니다. 앱을 삭제하면 그 설정도 함께 사라집니다.",
        "Omdat niets hiervan bestaat, valt er ook nergens uit te stappen en zijn er geen gegevens "
        "om op te vragen of te laten wissen. De app verwijderen neemt de voorkeuren mee.",
        "Como nada disso existe, também não há nada para recusar nem dados para solicitar ou "
        "apagar. Apagar o app leva as preferências dele junto.",
        "因为这些统统不存在，也就没有什么可以退出，没有数据可以索取或删除。"
        "删除应用时，它的偏好设置也会一并消失。"),
    "Children": ("Kinder", "Menores", "Menores", "Enfants", "Minori", "お子さまについて",
                 "어린이", "Kinderen", "Crianças", "儿童"),
    "CYANO is rated 4+ and is safe for any age. It collects nothing from anybody, children "
    "included.": (
        "CYANO ist mit 4+ eingestuft und für jedes Alter unbedenklich. Es sammelt von niemandem "
        "etwas, Kinder eingeschlossen.",
        "CYANO tiene clasificación 4+ y es seguro para cualquier edad. No recoge nada de nadie, "
        "menores incluidos.",
        "CYANO tiene clasificación 4+ y es seguro para cualquier edad. No recoge nada de nadie, "
        "menores incluidos.",
        "CYANO est classé 4+ et convient à tout âge. Il ne collecte rien de personne, enfants "
        "compris.",
        "CYANO è classificato 4+ ed è sicuro a qualsiasi età. Non raccoglie niente da nessuno, "
        "bambini compresi.",
        "CYANO のレーティングは 4+ で、どの年齢の方にも安全です。お子さまを含め、"
        "誰からも何も収集しません。",
        "CYANO는 4+ 등급이며 어떤 연령에게도 안전합니다. 어린이를 포함해 누구에게서도 아무것도 "
        "수집하지 않습니다.",
        "CYANO heeft een 4+-classificatie en is veilig voor elke leeftijd. Het verzamelt van "
        "niemand iets, kinderen inbegrepen.",
        "O CYANO tem classificação 4+ e é seguro para qualquer idade. Ele não coleta nada de "
        "ninguém, inclusive crianças.",
        "CYANO 的分级为 4+，适合任何年龄。它不会从任何人那里收集任何东西，儿童也一样。"),
    "Changes": ("Änderungen", "Cambios", "Cambios", "Modifications", "Modifiche", "変更について",
                "변경", "Wijzigingen", "Alterações", "变更"),
    "If this policy ever changes, the date at the top of this page changes with it. Since the app "
    "collects nothing, any change would be a matter of wording rather than of practice.": (
        "Sollte sich diese Erklärung je ändern, ändert sich das Datum oben auf dieser Seite mit "
        "ihr. Da die App nichts sammelt, wäre jede Änderung eine Frage der Formulierung und nicht "
        "der Praxis.",
        "Si esta política cambia alguna vez, la fecha de la parte superior de esta página cambia "
        "con ella. Como la app no recoge nada, cualquier cambio sería una cuestión de redacción y "
        "no de práctica.",
        "Si esta política cambia alguna vez, la fecha de la parte superior de esta página cambia "
        "con ella. Como la app no recoge nada, cualquier cambio sería una cuestión de redacción y "
        "no de práctica.",
        "Si cette politique change un jour, la date en haut de cette page change avec elle. Comme "
        "l'app ne collecte rien, tout changement relèverait de la formulation et non de la "
        "pratique.",
        "Se questa informativa dovesse cambiare, la data in cima a questa pagina cambia con essa. "
        "Dato che l'app non raccoglie niente, qualsiasi modifica sarebbe una questione di parole e "
        "non di pratica.",
        "この方針が変わることがあれば、このページ上部の日付も一緒に変わります。アプリは何も"
        "収集していないので、変更があるとすれば、それは運用ではなく言い回しの問題です。",
        "이 방침이 바뀌면 이 페이지 맨 위의 날짜도 함께 바뀝니다. 앱이 아무것도 수집하지 않으므로, "
        "어떤 변경이든 실제 관행이 아니라 표현의 문제일 것입니다.",
        "Mocht dit beleid ooit veranderen, dan verandert de datum boven aan deze pagina mee. Omdat "
        "de app niets verzamelt, zou elke wijziging een kwestie van formulering zijn en niet van "
        "praktijk.",
        "Se esta política mudar algum dia, a data no topo desta página muda junto. Como o app não "
        "coleta nada, qualquer mudança seria uma questão de redação e não de prática.",
        "如果这份政策有变，本页顶部的日期也会随之更改。由于这个应用什么都不收集，"
        "任何变更都只关乎措辞，而不关乎做法。"),
    "Contact": ("Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "連絡先", "연락처",
                "Contact", "Contato", "联系"),
    "Questions about this policy:": (
        "Fragen zu dieser Erklärung:", "Preguntas sobre esta política:",
        "Preguntas sobre esta política:", "Questions sur cette politique :",
        "Domande su questa informativa:", "この方針についてのお問い合わせ：",
        "이 방침에 대한 문의:", "Vragen over dit beleid:", "Dúvidas sobre esta política:",
        "关于这份政策的问题："),
}
