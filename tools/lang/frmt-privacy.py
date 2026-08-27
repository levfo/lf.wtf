"""lf.wtf/frmt/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

A privacy policy is a document someone may rely on, so this is translated closely rather than
rewritten. The claims are specific and load-bearing (add-only library access, no networking code at
all, both folders excluded from iCloud) and each one has to survive intact.

The date is left in English form on purpose: it is a fact, not copy, and every locale renders it
unambiguously as written.
"""

KEEP = {"FRMT", "iPhone", "lf.wtf", "App Store", "https://lf.wtf/frmt",
        "Last updated: 4 August 2026"}

T = {
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보", "Privacy", "Privacidade", "隐私"),
    "Privacy Policy": ("Datenschutzerklärung", "Política de privacidad",
                       "Política de privacidad", "Politique de confidentialité",
                       "Informativa sulla privacy", "プライバシーポリシー",
                       "개인정보 처리방침", "Privacybeleid", "Política de privacidade",
                       "隐私政策"),
    "FRMT collects nothing and has no way to. There is no account, no analytics and no server.": (
        "FRMT sammelt nichts und hat auch keine Möglichkeit dazu. Es gibt kein Konto, keine "
        "Analyse und keinen Server.",
        "FRMT no recoge nada y no tiene forma de hacerlo. No hay cuenta, ni analíticas, ni "
        "servidor.",
        "FRMT no recoge nada y no tiene forma de hacerlo. No hay cuenta, ni analíticas, ni "
        "servidor.",
        "FRMT ne collecte rien et n'a aucun moyen de le faire. Il n'y a pas de compte, pas "
        "d'analytique et pas de serveur.",
        "FRMT non raccoglie niente e non ha modo di farlo. Non c'è account, non ci sono analisi e "
        "non c'è server.",
        "FRMT は何も収集しませんし、収集する手段も持っていません。アカウントも、解析も、"
        "サーバーもありません。",
        "FRMT는 아무것도 수집하지 않으며, 수집할 방법도 없습니다. 계정도, 분석도, 서버도 없습니다.",
        "FRMT verzamelt niets en heeft er ook geen manier toe. Er is geen account, geen analytics "
        "en geen server.",
        "O FRMT não coleta nada e não tem como coletar. Não há conta, não há análises e não há "
        "servidor.",
        "FRMT 不收集任何东西，也没有办法收集。没有账号、没有分析，也没有服务器。"),
    "The short version": ("Die Kurzfassung", "La versión corta", "La versión corta",
                          "La version courte", "La versione breve", "短く言うと",
                          "짧게 말하면", "De korte versie", "A versão curta", "简短版本"),
    "FRMT does not collect anything about you, and it has no way to. There is no account, no "
    "analytics, no advertising and no server. The app contains no networking code at all.": (
        "FRMT sammelt nichts über dich und hat auch keine Möglichkeit dazu. Es gibt kein Konto, "
        "keine Analyse, keine Werbung und keinen Server. Die App enthält überhaupt keinen "
        "Netzwerkcode.",
        "FRMT no recoge nada sobre ti, y no tiene forma de hacerlo. No hay cuenta, ni analíticas, "
        "ni publicidad, ni servidor. La app no contiene nada de código de red.",
        "FRMT no recoge nada sobre ti, y no tiene forma de hacerlo. No hay cuenta, ni analíticas, "
        "ni publicidad, ni servidor. La app no contiene nada de código de red.",
        "FRMT ne collecte rien à votre sujet, et n'a aucun moyen de le faire. Il n'y a pas de "
        "compte, pas d'analytique, pas de publicité et pas de serveur. L'app ne contient aucun code "
        "réseau.",
        "FRMT non raccoglie niente su di te, e non ha modo di farlo. Non c'è account, non ci sono "
        "analisi, non c'è pubblicità e non c'è server. L'app non contiene proprio codice di rete.",
        "FRMT はあなたについて何も収集しませんし、収集する手段も持っていません。アカウントも、"
        "解析も、広告も、サーバーもありません。アプリには通信のコードそのものが入っていません。",
        "FRMT는 당신에 대해 아무것도 수집하지 않으며, 수집할 방법도 없습니다. 계정도, 분석도, "
        "광고도, 서버도 없습니다. 앱에는 네트워크 코드 자체가 들어 있지 않습니다.",
        "FRMT verzamelt niets over jou en heeft er ook geen manier toe. Er is geen account, geen "
        "analytics, geen advertenties en geen server. De app bevat helemaal geen netwerkcode.",
        "O FRMT não coleta nada sobre você, e não tem como. Não há conta, não há análises, não há "
        "publicidade e não há servidor. O app não contém nenhum código de rede.",
        "FRMT 不收集任何关于你的信息，也没有办法收集。没有账号、没有分析、没有广告，也没有服务器。"
        "这个应用里根本没有联网代码。"),
    "What the app stores, and where": (
        "Was die App speichert, und wo", "Qué guarda la app, y dónde", "Qué guarda la app, y dónde",
        "Ce que l'app stocke, et où", "Cosa memorizza l'app, e dove", "アプリが保存するもの、"
        "そしてその場所", "앱이 저장하는 것과 그 위치", "Wat de app opslaat, en waar",
        "O que o app armazena, e onde", "应用保存什么，保存在哪里"),
    "Everything stays on your iPhone.": (
        "Alles bleibt auf deinem iPhone.", "Todo se queda en tu iPhone.",
        "Todo se queda en tu iPhone.", "Tout reste sur votre iPhone.",
        "Resta tutto sul tuo iPhone.", "すべては iPhone のなかに留まります。",
        "모든 것이 당신의 iPhone 안에 남습니다.", "Alles blijft op je iPhone.",
        "Tudo fica no seu iPhone.", "一切都留在你的 iPhone 上。"),
    "Photographs.": ("Fotos.", "Fotografías.", "Fotografías.", "Photographies.", "Fotografie.",
                     "写真。", "사진.", "Foto's.", "Fotografias.", "照片。"),
    "When you press the shutter, a RAW negative is written to a working folder inside the app. "
    "When it finishes developing, the photograph is saved to your photo library and a copy is kept "
    "in the app so you can look at it without leaving. The negative is then deleted. You can delete "
    "photographs from the app at any time, and deleting one there does not touch the copy in your "
    "photo library.": (
        "Wenn du den Auslöser drückst, wird ein RAW-Negativ in einen Arbeitsordner innerhalb der "
        "App geschrieben. Ist das Entwickeln fertig, wird das Foto in deiner Mediathek gesichert "
        "und eine Kopie bleibt in der App, damit du es ansehen kannst, ohne sie zu verlassen. Das "
        "Negativ wird danach gelöscht. Du kannst Fotos jederzeit aus der App löschen, und das "
        "berührt die Kopie in deiner Mediathek nicht.",
        "Cuando pulsas el disparador, se escribe un negativo RAW en una carpeta de trabajo dentro "
        "de la app. Cuando termina de revelarse, la fotografía se guarda en tu fototeca y se "
        "conserva una copia en la app para que puedas verla sin salir. El negativo se elimina "
        "después. Puedes borrar fotografías de la app en cualquier momento, y hacerlo no toca la "
        "copia de tu fototeca.",
        "Cuando presionas el disparador, se escribe un negativo RAW en una carpeta de trabajo "
        "dentro de la app. Cuando termina de revelarse, la fotografía se guarda en tu fototeca y se "
        "conserva una copia en la app para que puedas verla sin salir. El negativo se elimina "
        "después. Puedes borrar fotografías de la app en cualquier momento, y hacerlo no toca la "
        "copia de tu fototeca.",
        "Quand vous appuyez sur le déclencheur, un négatif RAW est écrit dans un dossier de travail "
        "à l'intérieur de l'app. Une fois le développement terminé, la photographie est enregistrée "
        "dans votre photothèque et une copie reste dans l'app pour que vous puissiez la regarder "
        "sans en sortir. Le négatif est ensuite supprimé. Vous pouvez supprimer des photographies "
        "de l'app à tout moment, et cela ne touche pas la copie de votre photothèque.",
        "Quando premi lo scatto, un negativo RAW viene scritto in una cartella di lavoro dentro "
        "l'app. Quando lo sviluppo finisce, la fotografia viene salvata nella tua libreria e una "
        "copia resta nell'app così puoi guardarla senza uscire. Il negativo viene poi eliminato. "
        "Puoi eliminare fotografie dall'app in qualsiasi momento, e farlo non tocca la copia nella "
        "tua libreria.",
        "シャッターを押すと、RAW ネガがアプリ内の作業用フォルダに書き込まれます。現像が終わると、"
        "写真は写真ライブラリに保存され、アプリの中にも控えが残るので、外に出ずに見返せます。"
        "ネガはそのあと削除されます。アプリ内の写真はいつでも削除でき、そこで削除しても"
        "写真ライブラリ側の控えには手を触れません。",
        "셔터를 누르면 RAW 네거티브가 앱 안의 작업 폴더에 기록됩니다. 현상이 끝나면 사진은 사진 "
        "보관함에 저장되고, 앱 안에도 사본이 남아 앱을 나가지 않고 볼 수 있습니다. 네거티브는 그 "
        "뒤에 삭제됩니다. 앱 안의 사진은 언제든 지울 수 있고, 그렇게 지워도 사진 보관함의 사본은 "
        "건드리지 않습니다.",
        "Als je afdrukt, wordt er een RAW-negatief weggeschreven naar een werkmap binnen de app. "
        "Zodra het ontwikkelen klaar is, wordt de foto in je fotobibliotheek bewaard en blijft er "
        "een kopie in de app zodat je hem kunt bekijken zonder hem te verlaten. Het negatief wordt "
        "daarna verwijderd. Je kunt foto's op elk moment uit de app verwijderen, en dat raakt de "
        "kopie in je fotobibliotheek niet.",
        "Quando você aperta o disparador, um negativo RAW é gravado numa pasta de trabalho dentro "
        "do app. Quando termina de revelar, a fotografia é salva na sua fototeca e uma cópia fica "
        "no app para você poder olhar sem sair. O negativo é apagado em seguida. Você pode apagar "
        "fotografias do app a qualquer momento, e isso não mexe na cópia da sua fototeca.",
        "当你按下快门，一张 RAW 底片会写入应用内部的工作文件夹。显影完成后，"
        "照片会保存到你的照片图库，应用内也会留一份副本，方便你不离开就能查看。底片随后会被删除。"
        "你可以随时从应用里删除照片，这样做不会影响你照片图库里的那一份。"),
    "Settings.": ("Einstellungen.", "Ajustes.", "Ajustes.", "Réglages.", "Impostazioni.",
                  "設定。", "설정.", "Instellingen.", "Ajustes.", "设置。"),
    "Which film is loaded, capture size, when developing runs, and whether you have seen the "
    "introduction. These live in the app's own preferences and are read by nothing else.": (
        "Welcher Film eingelegt ist, die Aufnahmegröße, wann entwickelt wird, und ob du die "
        "Einführung gesehen hast. Das liegt in den eigenen Einstellungen der App und wird von "
        "nichts anderem gelesen.",
        "Qué película está cargada, el tamaño de captura, cuándo se revela, y si has visto la "
        "introducción. Viven en las preferencias de la propia app y no las lee nada más.",
        "Qué película está cargada, el tamaño de captura, cuándo se revela, y si has visto la "
        "introducción. Viven en las preferencias de la propia app y no las lee nada más.",
        "Quelle pellicule est chargée, la taille de capture, le moment du développement, et si "
        "vous avez vu l'introduction. Cela vit dans les préférences propres à l'app et rien "
        "d'autre ne les lit.",
        "Quale pellicola è caricata, la dimensione dello scatto, quando si sviluppa, e se hai "
        "visto l'introduzione. Stanno nelle preferenze dell'app e non le legge nient'altro.",
        "どのフィルムが装填されているか、撮影サイズ、現像するタイミング、そしてはじめにを見たか"
        "どうか。これらはアプリ自身の設定のなかにあり、ほかの何かが読むことはありません。",
        "어떤 필름이 장전되어 있는지, 촬영 크기, 언제 현상할지, 그리고 소개를 보았는지 여부. 이것들은 "
        "앱 자체의 설정 안에 있고, 다른 무엇도 읽지 않습니다.",
        "Welke film geladen is, het opnameformaat, wanneer er ontwikkeld wordt, en of je de "
        "introductie hebt gezien. Dat staat in de eigen voorkeuren van de app en wordt door niets "
        "anders gelezen.",
        "Qual filme está carregado, o tamanho de captura, quando revelar, e se você já viu a "
        "introdução. Isso fica nas preferências do próprio app e nada mais lê.",
        "装入的是哪款胶片、拍摄尺寸、什么时候显影，以及你是否看过介绍。"
        "这些存放在应用自己的偏好设置里，没有别的东西会读取。"),
    "None of this is backed up to iCloud: both folders are marked excluded, because they are a "
    "working copy of pictures that are already in your photo library.": (
        "Nichts davon wird in iCloud gesichert: Beide Ordner sind als ausgeschlossen markiert, "
        "weil sie eine Arbeitskopie von Bildern sind, die bereits in deiner Mediathek liegen.",
        "Nada de esto se respalda en iCloud: ambas carpetas están marcadas como excluidas, porque "
        "son una copia de trabajo de imágenes que ya están en tu fototeca.",
        "Nada de esto se respalda en iCloud: ambas carpetas están marcadas como excluidas, porque "
        "son una copia de trabajo de imágenes que ya están en tu fototeca.",
        "Rien de tout cela n'est sauvegardé sur iCloud : les deux dossiers sont marqués comme "
        "exclus, parce qu'ils sont une copie de travail d'images déjà présentes dans votre "
        "photothèque.",
        "Niente di tutto questo viene salvato su iCloud: entrambe le cartelle sono contrassegnate "
        "come escluse, perché sono una copia di lavoro di immagini già presenti nella tua libreria.",
        "これらはいずれも iCloud にバックアップされません。どちらのフォルダも除外の印が付いて"
        "います。すでに写真ライブラリにある画像の作業用の控えだからです。",
        "이 가운데 어느 것도 iCloud에 백업되지 않습니다. 두 폴더 모두 제외 표시가 되어 있는데, 이미 "
        "사진 보관함에 있는 이미지의 작업용 사본이기 때문입니다.",
        "Niets hiervan wordt naar iCloud geback-upt: beide mappen zijn als uitgesloten gemarkeerd, "
        "omdat ze een werkkopie zijn van beelden die al in je fotobibliotheek staan.",
        "Nada disso é salvo no iCloud: as duas pastas estão marcadas como excluídas, porque são uma "
        "cópia de trabalho de imagens que já estão na sua fototeca.",
        "这些都不会备份到 iCloud：两个文件夹都被标记为排除，"
        "因为它们只是你照片图库里已有图像的工作副本。"),
    "Permissions the app asks for": (
        "Berechtigungen, die die App anfragt", "Permisos que pide la app",
        "Permisos que pide la app", "Les autorisations que l'app demande",
        "I permessi che l'app chiede", "アプリが求める許可",
        "앱이 요청하는 권한", "Toestemmingen die de app vraagt",
        "Permissões que o app pede", "应用请求的权限"),
    "Camera.": ("Kamera.", "Cámara.", "Cámara.", "Appareil photo.", "Fotocamera.", "カメラ。",
                "카메라.", "Camera.", "Câmera.", "相机。"),
    "To take photographs. Refusing it leaves the rest of the app working, including developing "
    "anything already on the roll.": (
        "Um Fotos aufzunehmen. Verweigerst du sie, funktioniert der Rest der App weiter, "
        "einschließlich des Entwickelns von allem, was bereits auf dem Film liegt.",
        "Para hacer fotografías. Si lo rechazas, el resto de la app sigue funcionando, incluido "
        "revelar lo que ya haya en el carrete.",
        "Para tomar fotografías. Si lo rechazas, el resto de la app sigue funcionando, incluido "
        "revelar lo que ya haya en el rollo.",
        "Pour prendre des photographies. Le refuser laisse le reste de l'app fonctionner, y "
        "compris le développement de ce qui est déjà sur la pellicule.",
        "Per scattare fotografie. Se lo rifiuti, il resto dell'app continua a funzionare, compreso "
        "lo sviluppo di quello che è già sul rullino.",
        "写真を撮るためです。拒否しても、すでにフィルムに乗っている分の現像を含め、"
        "アプリのそのほかの部分は動き続けます。",
        "사진을 찍기 위해서입니다. 거부해도 이미 롤에 올라와 있는 것을 현상하는 일을 포함해, 앱의 "
        "나머지 부분은 계속 동작합니다.",
        "Om foto's te maken. Weiger je het, dan blijft de rest van de app werken, inclusief het "
        "ontwikkelen van wat al op het rolletje staat.",
        "Para tirar fotografias. Se você recusar, o resto do app continua funcionando, inclusive "
        "revelar o que já está no rolo.",
        "用来拍照。拒绝之后，应用其余部分仍然可用，包括显影已经在胶卷上的画面。"),
    "Adding to your photo library.": (
        "Hinzufügen zu deiner Mediathek.", "Añadir a tu fototeca.", "Agregar a tu fototeca.",
        "Ajouter à votre photothèque.", "Aggiungere alla tua libreria foto.",
        "写真ライブラリへの追加。", "사진 보관함에 추가.", "Toevoegen aan je fotobibliotheek.",
        "Adicionar à sua fototeca.", "添加到你的照片图库。"),
    "To save finished photographs. This is add-only access: the app can put photographs into your "
    "library and cannot read what is already there. That is also why it keeps its own copy. A "
    "gallery built on your library would have to ask for the whole library in order to show you a "
    "corner of it.": (
        "Um fertige Fotos zu sichern. Das ist reiner Hinzufügen-Zugriff: Die App kann Fotos in "
        "deine Mediathek legen und kann nicht lesen, was schon darin ist. Deshalb behält sie auch "
        "eine eigene Kopie. Eine Galerie, die auf deiner Mediathek aufbaut, müsste die ganze "
        "Mediathek anfragen, nur um dir eine Ecke davon zu zeigen.",
        "Para guardar las fotografías terminadas. Es acceso solo de adición: la app puede meter "
        "fotografías en tu fototeca y no puede leer lo que ya hay. Por eso también conserva su "
        "propia copia. Una galería construida sobre tu fototeca tendría que pedir la fototeca "
        "entera para enseñarte un rincón de ella.",
        "Para guardar las fotografías terminadas. Es acceso solo de adición: la app puede meter "
        "fotografías en tu fototeca y no puede leer lo que ya hay. Por eso también conserva su "
        "propia copia. Una galería construida sobre tu fototeca tendría que pedir la fototeca "
        "entera para enseñarte un rincón de ella.",
        "Pour enregistrer les photographies terminées. C'est un accès en ajout seul : l'app peut "
        "mettre des photographies dans votre photothèque et ne peut pas lire ce qui s'y trouve "
        "déjà. C'est aussi pourquoi elle garde sa propre copie. Une galerie bâtie sur votre "
        "photothèque devrait demander la photothèque entière pour vous en montrer un coin.",
        "Per salvare le fotografie finite. È un accesso di sola aggiunta: l'app può mettere "
        "fotografie nella tua libreria e non può leggere quello che c'è già. È anche per questo che "
        "tiene una copia propria. Una galleria costruita sulla tua libreria dovrebbe chiedere "
        "l'intera libreria per mostrartene un angolo.",
        "仕上がった写真を保存するためです。これは追加専用のアクセスで、アプリは写真ライブラリに"
        "写真を入れることはできますが、すでにそこにあるものを読むことはできません。アプリが自分の"
        "控えを持っているのもそのためです。写真ライブラリの上に組んだギャラリーは、"
        "その片隅を見せるだけのためにライブラリ全体を要求することになってしまいます。",
        "완성된 사진을 저장하기 위해서입니다. 이것은 추가 전용 접근으로, 앱은 사진 보관함에 사진을 "
        "넣을 수는 있지만 이미 그곳에 있는 것을 읽을 수는 없습니다. 앱이 자체 사본을 두는 이유이기도 "
        "합니다. 사진 보관함 위에 얹은 갤러리라면, 그 한 귀퉁이를 보여 주기 위해 보관함 전체를 "
        "요구해야 했을 것입니다.",
        "Om afgeronde foto's te bewaren. Dit is alleen-toevoegen-toegang: de app kan foto's in je "
        "bibliotheek zetten en kan niet lezen wat er al staat. Daarom houdt hij ook een eigen "
        "kopie. Een galerij die op je bibliotheek is gebouwd zou de hele bibliotheek moeten vragen "
        "om je er een hoekje van te laten zien.",
        "Para salvar as fotografias prontas. É um acesso somente de adição: o app pode colocar "
        "fotografias na sua fototeca e não pode ler o que já está lá. É também por isso que ele "
        "guarda a própria cópia. Uma galeria construída sobre a sua fototeca teria de pedir a "
        "fototeca inteira para mostrar um canto dela.",
        "用来保存完成的照片。这是\"仅添加\"权限：应用可以把照片放进你的图库，"
        "却读不到里面已经有的东西。这也是它自己另存一份的原因。"
        "一个建立在你图库之上的相册，为了给你看其中一角，就得申请整个图库。"),
    "Importing.": ("Importieren.", "Importar.", "Importar.", "Importation.", "Importazione.",
                   "読み込み。", "가져오기.", "Importeren.", "Importar.", "导入。"),
    "The Import button uses Apple's system photo picker, which runs outside the app. FRMT receives "
    "only the files you choose and never gains access to the rest.": (
        "Die Import-Taste benutzt Apples System-Fotoauswahl, die außerhalb der App läuft. FRMT "
        "erhält nur die Dateien, die du auswählst, und bekommt nie Zugriff auf den Rest.",
        "El botón Importar usa el selector de fotos del sistema de Apple, que se ejecuta fuera de "
        "la app. FRMT recibe solo los archivos que elijas y nunca obtiene acceso al resto.",
        "El botón Importar usa el selector de fotos del sistema de Apple, que se ejecuta fuera de "
        "la app. FRMT recibe solo los archivos que elijas y nunca obtiene acceso al resto.",
        "Le bouton Importer utilise le sélecteur de photos du système Apple, qui tourne en dehors "
        "de l'app. FRMT ne reçoit que les fichiers que vous choisissez et n'obtient jamais l'accès "
        "au reste.",
        "Il pulsante Importa usa il selettore foto di sistema di Apple, che gira fuori dall'app. "
        "FRMT riceve solo i file che scegli e non ottiene mai accesso al resto.",
        "読み込みボタンは Apple のシステムの写真ピッカーを使っており、これはアプリの外で動きます。"
        "FRMT が受け取るのは、あなたが選んだファイルだけで、それ以外にアクセスすることは"
        "ありません。",
        "가져오기 버튼은 Apple의 시스템 사진 선택기를 사용하며, 이것은 앱 바깥에서 동작합니다. "
        "FRMT가 받는 것은 당신이 고른 파일뿐이고, 나머지에는 결코 접근하지 못합니다.",
        "De knop Importeren gebruikt de systeemfotokiezer van Apple, die buiten de app draait. FRMT "
        "ontvangt alleen de bestanden die je kiest en krijgt nooit toegang tot de rest.",
        "O botão Importar usa o seletor de fotos do sistema da Apple, que roda fora do app. O FRMT "
        "recebe apenas os arquivos que você escolher e nunca ganha acesso ao resto.",
        "导入按钮使用的是 Apple 的系统照片选择器，它在应用之外运行。"
        "FRMT 只会收到你选中的文件，永远不会获得其余内容的访问权。"),
    "What is sent off the device": (
        "Was das Gerät verlässt", "Qué se envía fuera del dispositivo",
        "Qué se envía fuera del dispositivo", "Ce qui quitte l'appareil",
        "Cosa esce dal dispositivo", "端末の外へ送られるもの", "기기 밖으로 나가는 것",
        "Wat het toestel verlaat", "O que é enviado para fora do aparelho", "有什么会离开设备"),
    "Nothing.": ("Nichts.", "Nada.", "Nada.", "Rien.", "Niente.", "何もありません。",
                 "아무것도 없습니다.", "Niets.", "Nada.", "什么都没有。"),
    "Photographs are developed on your iPhone's GPU. There is no cloud processing, no telemetry, no "
    "crash reporting service and no third-party code of any kind linked into the app.": (
        "Fotos werden auf der GPU deines iPhone entwickelt. Es gibt keine Cloud-Verarbeitung, "
        "keine Telemetrie, keinen Absturzberichtsdienst und keinerlei Code von Dritten, der in die "
        "App eingebunden wäre.",
        "Las fotografías se revelan en la GPU de tu iPhone. No hay procesado en la nube, ni "
        "telemetría, ni servicio de informes de fallos, ni código de terceros de ningún tipo "
        "enlazado en la app.",
        "Las fotografías se revelan en la GPU de tu iPhone. No hay procesamiento en la nube, ni "
        "telemetría, ni servicio de informes de fallas, ni código de terceros de ningún tipo "
        "enlazado en la app.",
        "Les photographies sont développées sur le GPU de votre iPhone. Il n'y a pas de traitement "
        "dans le cloud, pas de télémétrie, pas de service de rapport de plantage et aucun code "
        "tiers d'aucune sorte lié à l'app.",
        "Le fotografie vengono sviluppate sulla GPU del tuo iPhone. Non c'è elaborazione nel "
        "cloud, non c'è telemetria, non c'è servizio di segnalazione crash e non c'è codice di "
        "terze parti di alcun tipo collegato all'app.",
        "写真はあなたの iPhone の GPU で現像されます。クラウド処理も、テレメトリも、"
        "クラッシュ報告サービスも、いかなる第三者のコードもアプリには組み込まれていません。",
        "사진은 당신의 iPhone GPU에서 현상됩니다. 클라우드 처리도, 텔레메트리도, 크래시 리포트 "
        "서비스도, 어떤 종류의 서드파티 코드도 앱에 연결되어 있지 않습니다.",
        "Foto's worden ontwikkeld op de GPU van je iPhone. Er is geen cloudverwerking, geen "
        "telemetrie, geen crashrapportagedienst en geen code van derden van welke aard dan ook in "
        "de app gelinkt.",
        "As fotografias são reveladas na GPU do seu iPhone. Não há processamento em nuvem, não há "
        "telemetria, não há serviço de relatório de falhas e não há código de terceiros de "
        "nenhum tipo ligado ao app.",
        "照片在你 iPhone 的 GPU 上完成显影。没有云端处理、没有遥测、没有崩溃报告服务，"
        "应用里也没有链接任何第三方代码。"),
    "If you use the share button on a photograph, iOS sends it wherever you choose. That is your "
    "action and your destination, and it is governed by whatever you shared it to.": (
        "Wenn du bei einem Foto die Teilen-Taste benutzt, schickt iOS es dorthin, wohin du "
        "wählst. Das ist deine Handlung und dein Ziel, und es richtet sich danach, wohin du "
        "geteilt hast.",
        "Si usas el botón de compartir en una fotografía, iOS la envía a donde tú elijas. Esa es "
        "tu acción y tu destino, y se rige por aquello a lo que la hayas compartido.",
        "Si usas el botón de compartir en una fotografía, iOS la envía a donde tú elijas. Esa es "
        "tu acción y tu destino, y se rige por aquello a lo que la hayas compartido.",
        "Si vous utilisez le bouton de partage sur une photographie, iOS l'envoie là où vous "
        "choisissez. C'est votre action et votre destination, et cela relève de ce vers quoi vous "
        "avez partagé.",
        "Se usi il pulsante di condivisione su una fotografia, iOS la manda dove scegli tu. È una "
        "tua azione verso una tua destinazione, e vale quello che dice il servizio a cui l'hai "
        "condivisa.",
        "写真で共有ボタンを使うと、iOS があなたの選んだ先へそれを送ります。それはあなたの操作と"
        "あなたの宛先であり、共有した先の規約に従います。",
        "사진에서 공유 버튼을 쓰면, iOS가 당신이 고른 곳으로 그것을 보냅니다. 그것은 당신의 동작과 "
        "당신의 목적지이고, 공유한 대상의 방침을 따릅니다.",
        "Als je bij een foto de deelknop gebruikt, stuurt iOS hem waarheen je kiest. Dat is jouw "
        "handeling en jouw bestemming, en het valt onder waar je het naartoe hebt gedeeld.",
        "Se você usar o botão de compartilhar numa fotografia, o iOS a envia para onde você "
        "escolher. Essa é a sua ação e o seu destino, e vale o que disser o serviço para onde você "
        "compartilhou.",
        "如果你对一张照片使用分享按钮，iOS 会把它发送到你选择的地方。"
        "那是你的操作和你的目的地，受你分享到的那一方的条款约束。"),
    "Children": ("Kinder", "Menores", "Menores", "Enfants", "Minori", "お子さまについて",
                 "어린이", "Kinderen", "Crianças", "儿童"),
    "FRMT is rated 4+ and collects no data from anyone, of any age.": (
        "FRMT ist mit 4+ eingestuft und sammelt von niemandem Daten, in keinem Alter.",
        "FRMT tiene clasificación 4+ y no recoge datos de nadie, de ninguna edad.",
        "FRMT tiene clasificación 4+ y no recoge datos de nadie, de ninguna edad.",
        "FRMT est classé 4+ et ne collecte aucune donnée de qui que ce soit, à tout âge.",
        "FRMT è classificato 4+ e non raccoglie dati da nessuno, di qualunque età.",
        "FRMT のレーティングは 4+ で、年齢を問わず誰からもデータを収集しません。",
        "FRMT는 4+ 등급이며, 나이에 관계없이 누구에게서도 데이터를 수집하지 않습니다.",
        "FRMT heeft een 4+-classificatie en verzamelt van niemand gegevens, ongeacht leeftijd.",
        "O FRMT tem classificação 4+ e não coleta dados de ninguém, de qualquer idade.",
        "FRMT 的分级为 4+，不会从任何年龄的任何人那里收集数据。"),
    "Changes": ("Änderungen", "Cambios", "Cambios", "Modifications", "Modifiche", "変更について",
                "변경", "Wijzigingen", "Alterações", "变更"),
    "If this policy ever changes, the date at the top changes with it. Since the app collects "
    "nothing, any change would be a clarification rather than a new use of your data.": (
        "Sollte sich diese Erklärung je ändern, ändert sich das Datum oben mit ihr. Da die App "
        "nichts sammelt, wäre jede Änderung eine Klarstellung und keine neue Nutzung deiner Daten.",
        "Si esta política cambia alguna vez, la fecha de arriba cambia con ella. Como la app no "
        "recoge nada, cualquier cambio sería una aclaración y no un uso nuevo de tus datos.",
        "Si esta política cambia alguna vez, la fecha de arriba cambia con ella. Como la app no "
        "recoge nada, cualquier cambio sería una aclaración y no un uso nuevo de tus datos.",
        "Si cette politique change un jour, la date en haut change avec elle. Comme l'app ne "
        "collecte rien, tout changement serait une clarification et non un nouvel usage de vos "
        "données.",
        "Se questa informativa dovesse cambiare, la data in alto cambia con essa. Dato che l'app "
        "non raccoglie niente, qualsiasi modifica sarebbe un chiarimento e non un nuovo uso dei "
        "tuoi dati.",
        "この方針が変わることがあれば、上部の日付も一緒に変わります。アプリは何も収集していない"
        "ので、変更があるとすれば、それはあなたのデータの新しい利用ではなく、説明の明確化です。",
        "이 방침이 바뀌면 맨 위의 날짜도 함께 바뀝니다. 앱이 아무것도 수집하지 않으므로, 어떤 "
        "변경이든 당신의 데이터를 새로 쓰는 것이 아니라 설명을 분명히 하는 일이 될 것입니다.",
        "Mocht dit beleid ooit veranderen, dan verandert de datum bovenaan mee. Omdat de app niets "
        "verzamelt, zou elke wijziging een verduidelijking zijn en geen nieuw gebruik van je "
        "gegevens.",
        "Se esta política mudar algum dia, a data no topo muda junto. Como o app não coleta nada, "
        "qualquer mudança seria um esclarecimento e não um novo uso dos seus dados.",
        "如果这份政策有变，顶部的日期也会随之更改。由于这个应用什么都不收集，"
        "任何变更都只会是措辞上的澄清，而不是对你数据的新用途。"),
    "Contact": ("Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "連絡先", "연락처",
                "Contact", "Contato", "联系"),
    "Questions about this policy or the app:": (
        "Fragen zu dieser Erklärung oder zur App:",
        "Preguntas sobre esta política o sobre la app:",
        "Preguntas sobre esta política o sobre la app:",
        "Questions sur cette politique ou sur l'app :",
        "Domande su questa informativa o sull'app:",
        "この方針やアプリについてのお問い合わせ：",
        "이 방침이나 앱에 대한 문의:",
        "Vragen over dit beleid of over de app:",
        "Dúvidas sobre esta política ou sobre o app:",
        "关于这份政策或这个应用的问题："),
}

# Was "Privacy &mdash; FRMT". Rewritten rather than repunctuated: every language puts the words in
# its own order, and leading with the product is the better title anyway.
T["FRMT Privacy Policy"] = (
    "Datenschutzerklärung für FRMT", "Política de privacidad de FRMT",
    "Política de privacidad de FRMT", "Politique de confidentialité de FRMT",
    "Informativa sulla privacy di FRMT", "FRMT プライバシーポリシー", "FRMT 개인정보 처리방침",
    "Privacybeleid van FRMT", "Política de privacidade do FRMT", "FRMT 隐私政策")
