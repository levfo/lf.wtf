"""lf.wtf/modul8/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

This page was held back from the first localisation pass because it still described Google AdMob as
current. MODUL8 2.0, released on 24 September 2026, has no ads and no AdMob, so the page now
describes 2.0 and keeps a short section for 1.2 and earlier, which served AdMob ads in the free
tier and may still be installed on some phones. That version boundary is the thing a translation
must not blur.

**It claims no more than the App Store does.** The listing says no ads, everything processed on the
device, nothing uploaded, and its privacy label reads Data Not Collected. That label is quoted in
Apple's own localised words, taken from each storefront's app page (Keine Daten erfasst, Données non
collectées, データの収集なし, 未收集数据 and so on), so a reader can find the same phrase there.

**The iOS Settings path uses Apple's own words**, not a translation of them. Someone following
"Settings > Privacy & Security > Tracking" has to find those exact items on their own device, so
German gets Datenschutz & Sicherheit, Japanese gets プライバシー / セキュリティ / トラッキング, and
so on. Getting this wrong sends people hunting through a menu that does not say what the page says.

The fragments either side of the link and the menu separators are one sentence in the markup and
cannot be reordered, so each is written to read correctly once assembled.
"""

KEEP = {"MODUL8", "L@LF.WTF", "App Store", "MODUL8 · Levi Foster ·",
        }

T = {
    "MODUL8 Privacy Policy": (
        "Datenschutzerklärung für MODUL8", "Política de privacidad de MODUL8",
        "Política de privacidad de MODUL8", "Politique de confidentialité de MODUL8",
        "Informativa sulla privacy di MODUL8", "MODUL8 プライバシーポリシー",
        "MODUL8 개인정보 처리방침", "Privacybeleid van MODUL8",
        "Política de privacidade do MODUL8", "MODUL8 隐私政策"),
    "MODUL8 app icon": ("MODUL8 App-Symbol", "Icono de la app MODUL8", "Icono de la app MODUL8",
                        "Icône de l'app MODUL8", "Icona dell'app MODUL8",
                        "MODUL8 のアプリアイコン", "MODUL8 앱 아이콘", "MODUL8-app-icoon",
                        "Ícone do app MODUL8", "MODUL8 应用图标"),
    "Back to MODUL8": ("Zurück zu MODUL8", "Volver a MODUL8", "Volver a MODUL8",
                       "Retour à MODUL8", "Torna a MODUL8", "MODUL8 に戻る", "MODUL8로 돌아가기",
                       "Terug naar MODUL8", "Voltar para o MODUL8", "返回 MODUL8"),
    "Privacy Policy": ("Datenschutzerklärung", "Política de privacidad", "Política de privacidad",
                       "Politique de confidentialité", "Informativa sulla privacy",
                       "プライバシーポリシー", "개인정보 처리방침", "Privacybeleid",
                       "Política de privacidade", "隐私政策"),
    "The short version.": ("Die Kurzfassung.", "La versión corta.", "La versión corta.",
                           "La version courte.", "La versione breve.", "短く言うと。",
                           "짧게 말하면.", "De korte versie.", "A versão curta.", "简短版本。"),
    "Which version this describes": (
        "Welche Version hier beschrieben wird", "Qué versión describe esto",
        "Qué versión describe esto", "Quelle version ceci décrit",
        "Quale versione descrive questo", "この文書が対象とするバージョン",
        "이 문서가 설명하는 버전", "Welke versie dit beschrijft",
        "Qual versão isto descreve", "本文所描述的版本"),
    "What the app does with your media": (
        "Was die App mit deinen Medien macht", "Qué hace la app con tus archivos",
        "Qué hace la app con tus archivos", "Ce que l'app fait de vos médias",
        "Cosa fa l'app con i tuoi file", "アプリがあなたのメディアに対してすること",
        "앱이 당신의 미디어로 하는 일", "Wat de app met je media doet",
        "O que o app faz com suas mídias", "应用如何处理你的素材"),
    "MODUL8 needs access to your photo library for two things: loading the images or videos you\n"
    "      choose, and saving the finished versions back. That is the whole of it.": (
        "MODUL8 braucht den Zugriff auf deine Mediathek für zwei Dinge: die Bilder oder Videos zu "
        "laden, die du auswählst, und die fertigen Fassungen zurückzusichern. Das ist alles.",
        "MODUL8 necesita acceso a tu fototeca para dos cosas: cargar las imágenes o vídeos que "
        "elijas, y guardar de vuelta las versiones terminadas. Eso es todo.",
        "MODUL8 necesita acceso a tu fototeca para dos cosas: cargar las imágenes o videos que "
        "elijas, y guardar de vuelta las versiones terminadas. Eso es todo.",
        "MODUL8 a besoin d'accéder à votre photothèque pour deux choses : charger les images ou "
        "vidéos que vous choisissez, et réenregistrer les versions terminées. C'est tout.",
        "MODUL8 ha bisogno di accedere alla tua libreria foto per due cose: caricare le immagini o "
        "i video che scegli, e risalvare le versioni finite. È tutto qui.",
        "MODUL8 が写真ライブラリへのアクセスを必要とするのは二つのことのためです。"
        "あなたが選んだ画像や動画を読み込むことと、仕上がったものを書き戻すこと。それだけです。",
        "MODUL8가 사진 보관함 접근을 필요로 하는 것은 두 가지 때문입니다. 당신이 고른 이미지나 "
        "영상을 불러오는 것과, 완성된 것을 다시 저장하는 것. 그게 전부입니다.",
        "MODUL8 heeft toegang tot je fotobibliotheek nodig voor twee dingen: het laden van de "
        "beelden of video's die je kiest, en het terugzetten van de afgeronde versies. Dat is alles.",
        "O MODUL8 precisa de acesso à sua fototeca para duas coisas: carregar as imagens ou vídeos "
        "que você escolher, e salvar de volta as versões prontas. É só isso.",
        "MODUL8 需要访问你的照片图库，只为两件事：载入你选择的图像或视频，"
        "以及把完成的版本存回去。仅此而已。"),
    "All image and video processing happens locally on your device. Your originals and your edits\n"
    "      are never uploaded to our servers or to any third-party server, and we have no access to "
    "the\n      contents of your library. This has been true in every version.": (
        "Die gesamte Bild- und Videoverarbeitung passiert lokal auf deinem Gerät. Deine Originale "
        "und deine Bearbeitungen werden nie auf unsere Server oder auf einen Server Dritter "
        "hochgeladen, und wir haben keinen Zugriff auf den Inhalt deiner Mediathek. Das galt in "
        "jeder Version.",
        "Todo el procesado de imagen y vídeo ocurre localmente en tu dispositivo. Tus originales y "
        "tus ediciones nunca se suben a nuestros servidores ni a ningún servidor de terceros, y no "
        "tenemos acceso al contenido de tu fototeca. Esto ha sido cierto en todas las versiones.",
        "Todo el procesamiento de imagen y video ocurre localmente en tu dispositivo. Tus "
        "originales y tus ediciones nunca se suben a nuestros servidores ni a ningún servidor de "
        "terceros, y no tenemos acceso al contenido de tu fototeca. Esto ha sido cierto en todas "
        "las versiones.",
        "Tout le traitement des images et des vidéos se fait localement sur votre appareil. Vos "
        "originaux et vos modifications ne sont jamais envoyés vers nos serveurs ni vers un serveur "
        "tiers, et nous n'avons aucun accès au contenu de votre photothèque. Cela a été vrai dans "
        "toutes les versions.",
        "Tutta l'elaborazione di immagini e video avviene in locale sul tuo dispositivo. I tuoi "
        "originali e le tue modifiche non vengono mai caricati sui nostri server né su server di "
        "terze parti, e non abbiamo accesso al contenuto della tua libreria. È stato vero in ogni "
        "versione.",
        "画像も動画も、処理はすべてあなたの端末の中で行われます。元のファイルも編集結果も、"
        "こちらのサーバーにも第三者のサーバーにもアップロードされることはなく、"
        "こちらがあなたのライブラリの中身にアクセスすることもありません。"
        "これはどのバージョンでも変わりません。",
        "이미지와 영상의 모든 처리는 당신의 기기 안에서 이루어집니다. 원본도 편집 결과도 우리 "
        "서버나 제3자의 서버로 업로드되지 않으며, 우리는 당신 보관함의 내용에 접근할 수 없습니다. "
        "이것은 모든 버전에서 그러했습니다.",
        "Alle beeld- en videoverwerking gebeurt lokaal op je toestel. Je originelen en je "
        "bewerkingen worden nooit naar onze servers of naar een server van derden geüpload, en wij "
        "hebben geen toegang tot de inhoud van je bibliotheek. Dit gold in elke versie.",
        "Todo o processamento de imagem e vídeo acontece localmente no seu aparelho. Seus originais "
        "e suas edições nunca são enviados para os nossos servidores nem para nenhum servidor de "
        "terceiros, e não temos acesso ao conteúdo da sua fototeca. Isso valeu em todas as versões.",
        "所有图像和视频的处理都在你的设备本地完成。你的原件和你的编辑结果永远不会被上传到我们的"
        "服务器或任何第三方服务器，我们也无法访问你图库中的内容。这在每一个版本中都是如此。"),
    "Version 1.2 and earlier: advertising": (
        "Version 1.2 und früher: Werbung", "Versión 1.2 y anteriores: publicidad",
        "Versión 1.2 y anteriores: publicidad", "Version 1.2 et antérieures : publicité",
        "Versione 1.2 e precedenti: pubblicità", "バージョン 1.2 以前：広告について",
        "1.2 버전과 그 이전: 광고", "Versie 1.2 en eerder: advertenties",
        "Versão 1.2 e anteriores: publicidade", "1.2 版及更早版本：广告"),
    "Device identifiers": ("Gerätekennungen", "Identificadores de dispositivo",
                           "Identificadores de dispositivo", "Identifiants d'appareil",
                           "Identificatori del dispositivo", "端末の識別子", "기기 식별자",
                           "Apparaat-identificaties", "Identificadores de dispositivo",
                           "设备标识符"),
    ": the Advertising Identifier (IDFA) on iOS, and only if\n      you allowed it at the App "
    "Tracking Transparency prompt.": (
        ": die Werbe-ID (IDFA) auf iOS, und nur, wenn du es bei Apples "
        "App-Tracking-Transparency-Abfrage erlaubt hast.",
        ": el Identificador de publicidad (IDFA) en iOS, y solo si lo permitiste en el aviso de App "
        "Tracking Transparency.",
        ": el Identificador de publicidad (IDFA) en iOS, y solo si lo permitiste en el aviso de App "
        "Tracking Transparency.",
        ": l'identifiant publicitaire (IDFA) sur iOS, et seulement si vous l'avez autorisé à "
        "l'invite App Tracking Transparency.",
        ": l'Identificatore per la pubblicità (IDFA) su iOS, e solo se lo hai consentito alla "
        "richiesta App Tracking Transparency.",
        "：iOS の広告識別子（IDFA）。ただし App Tracking Transparency の確認で許可した場合のみ。",
        ": iOS의 광고 식별자(IDFA), 그리고 App Tracking Transparency 안내에서 허용한 경우에만.",
        ": de reclame-identificatie (IDFA) op iOS, en alleen als je dat toestond bij de App "
        "Tracking Transparency-vraag.",
        ": o Identificador de Publicidade (IDFA) no iOS, e só se você permitiu no aviso de App "
        "Tracking Transparency.",
        "：iOS 上的广告标识符（IDFA），且仅在你于 App Tracking Transparency 提示中允许时。"),
    "Usage data": ("Nutzungsdaten", "Datos de uso", "Datos de uso", "Données d'utilisation",
                   "Dati di utilizzo", "利用データ", "사용 데이터", "Gebruiksgegevens",
                   "Dados de uso", "使用数据"),
    ": information about how you interacted with the ads, along with\n      device type, operating "
    "system and IP address.": (
        ": Informationen darüber, wie du mit der Werbung umgegangen bist, dazu Gerätetyp, "
        "Betriebssystem und IP-Adresse.",
        ": información sobre cómo interactuaste con los anuncios, junto con el tipo de dispositivo, "
        "el sistema operativo y la dirección IP.",
        ": información sobre cómo interactuaste con los anuncios, junto con el tipo de dispositivo, "
        "el sistema operativo y la dirección IP.",
        ": des informations sur la façon dont vous avez interagi avec les publicités, ainsi que le "
        "type d'appareil, le système d'exploitation et l'adresse IP.",
        ": informazioni su come hai interagito con la pubblicità, insieme al tipo di dispositivo, "
        "al sistema operativo e all'indirizzo IP.",
        "：広告にどう反応したかの情報。あわせて端末の種類、OS、IP アドレス。",
        ": 광고와 어떻게 상호작용했는지에 대한 정보, 그리고 기기 종류, 운영체제, IP 주소.",
        ": informatie over hoe je met de advertenties omging, samen met apparaattype, "
        "besturingssysteem en IP-adres.",
        ": informações sobre como você interagiu com os anúncios, junto com tipo de aparelho, "
        "sistema operacional e endereço IP.",
        "：你与广告互动方式的信息，以及设备类型、操作系统和 IP 地址。"),
    # This sentence runs: [A] Settings > [Privacy] & [Security] > [Tracking...] LINK [tail].
    # The menu items use Apple's own localised wording so they can actually be found on the device.
    "That was used to serve personalised ads and to measure how they performed. You can turn\n"
    "      personalised tracking off at any time in Settings": (
        "Das diente dazu, personalisierte Werbung auszuliefern und ihre Leistung zu messen. Du "
        "kannst personalisiertes Tracking jederzeit ausschalten unter Einstellungen",
        "Eso servía para mostrar anuncios personalizados y medir su rendimiento. Puedes desactivar "
        "el rastreo personalizado en cualquier momento en Ajustes",
        "Eso servía para mostrar anuncios personalizados y medir su rendimiento. Puedes desactivar "
        "el rastreo personalizado en cualquier momento en Ajustes",
        "Cela servait à diffuser des publicités personnalisées et à mesurer leurs performances. "
        "Vous pouvez désactiver le suivi personnalisé à tout moment dans Réglages",
        "Serviva a mostrare pubblicità personalizzata e a misurarne il rendimento. Puoi "
        "disattivare il tracciamento personalizzato in qualsiasi momento in Impostazioni",
        "これはパーソナライズされた広告を配信し、その成果を測るために使われていました。"
        "パーソナライズされたトラッキングは、いつでもオフにできます。設定",
        "이것은 맞춤형 광고를 보여 주고 그 성과를 측정하는 데 쓰였습니다. 맞춤형 추적은 언제든지 끌 "
        "수 있습니다. 설정",
        "Dat werd gebruikt om gepersonaliseerde advertenties te tonen en te meten hoe ze presteren. "
        "Je kunt gepersonaliseerde tracking op elk moment uitzetten in Instellingen",
        "Isso era usado para exibir anúncios personalizados e medir o desempenho deles. Você pode "
        "desativar o rastreamento personalizado a qualquer momento em Ajustes",
        "这用于投放个性化广告并衡量其效果。你可以随时关闭个性化追踪：设置"),
    "Privacy": ("Datenschutz", "Privacidad", "Privacidad", "Confidentialité", "Privacy",
                "プライバシー", "개인정보 보호", "Privacy", "Privacidade", "隐私"),
    "Security": ("Sicherheit", "seguridad", "seguridad", "sécurité", "sicurezza",
                 "セキュリティ", "보안", "beveiliging", "Segurança", "安全性"),
    "Tracking. For what Google collects and how long it keeps it, see the": (
        "Tracking. Was Google erhebt und wie lange es das aufbewahrt, steht in der",
        "Rastreo. Para saber qué recoge Google y cuánto tiempo lo conserva, consulta la",
        "Rastreo. Para saber qué recoge Google y cuánto tiempo lo conserva, consulta la",
        "Suivi. Pour ce que Google collecte et combien de temps il le conserve, voyez la",
        "Tracciamento. Per sapere cosa raccoglie Google e per quanto lo conserva, vedi l'",
        "トラッキング。Google が何を収集し、どれだけの期間保持するかについては、",
        "추적. Google이 무엇을 수집하고 얼마나 보관하는지는",
        "Tracking. Voor wat Google verzamelt en hoe lang het dat bewaart, zie het",
        "Rastreamento. Para o que o Google coleta e por quanto tempo guarda, veja a",
        "跟踪。关于 Google 收集什么以及保留多久，请参阅"),
    "Google Privacy Policy": (
        "Datenschutzerklärung von Google", "política de privacidad de Google",
        "política de privacidad de Google", "politique de confidentialité de Google",
        "informativa sulla privacy di Google", "Google のプライバシー ポリシー",
        "Google 개인정보처리방침", "privacybeleid van Google",
        "política de privacidade do Google", "《Google 隐私权政策》"),
    ". That data sits with\n      Google rather than with us, so a request to see or delete it goes "
    "to them.": (
        ". Diese Daten liegen bei Google und nicht bei uns, eine Anfrage auf Einsicht oder Löschung "
        "geht also an Google.",
        ". Esos datos están en manos de Google y no en las nuestras, así que una solicitud para "
        "verlos o borrarlos va dirigida a ellos.",
        ". Esos datos están en manos de Google y no en las nuestras, así que una solicitud para "
        "verlos o borrarlos va dirigida a ellos.",
        ". Ces données se trouvent chez Google et non chez nous, une demande de consultation ou de "
        "suppression s'adresse donc à eux.",
        ". Quei dati stanno da Google e non da noi, quindi una richiesta di accesso o cancellazione "
        "va rivolta a loro.",
        "をご覧ください。そのデータは当方ではなく Google の側にあるため、"
        "開示や削除の請求は Google に対して行うことになります。",
        "을 참고하세요. 그 데이터는 우리가 아니라 Google이 가지고 있으므로, 열람이나 삭제 요청은 "
        "Google에 하시면 됩니다.",
        ". Die gegevens liggen bij Google en niet bij ons, dus een verzoek om inzage of "
        "verwijdering gaat naar hen.",
        ". Esses dados ficam com o Google e não conosco, então um pedido para ver ou apagar vai "
        "para eles.",
        "。这些数据在 Google 那里，而不在我们这里，因此查阅或删除的请求应向他们提出。"),
    "Premium": ("Premium",) * 10,
    "Premium is handled entirely by Apple through the App Store. The app asks the system whether a\n"
    "      purchase is active and receives yes or no. It never sees your Apple Account, your name "
    "or any\n      payment detail, and no payment information is stored in the app or sent anywhere "
    "by it.\n      Apple's own handling of that transaction is covered by Apple's privacy policy, "
    "not this one.": (
        "Premium wird vollständig von Apple über den App Store abgewickelt. Die App fragt das "
        "System, ob ein Kauf aktiv ist, und erhält ja oder nein. Sie sieht nie deinen Apple "
        "Account, deinen Namen oder irgendein Zahlungsdetail, und in der App werden keine "
        "Zahlungsinformationen gespeichert oder von ihr irgendwohin gesendet. Wie Apple selbst mit "
        "dieser Transaktion umgeht, regelt Apples Datenschutzerklärung, nicht diese.",
        "Premium lo gestiona enteramente Apple a través de la App Store. La app pregunta al sistema "
        "si hay una compra activa y recibe sí o no. Nunca ve tu cuenta de Apple, tu nombre ni "
        "ningún dato de pago, y en la app no se guarda información de pago ni ella la envía a "
        "ninguna parte. Cómo trata Apple esa transacción se rige por la política de privacidad de "
        "Apple, no por esta.",
        "Premium lo gestiona enteramente Apple a través de la App Store. La app pregunta al sistema "
        "si hay una compra activa y recibe sí o no. Nunca ve tu cuenta de Apple, tu nombre ni "
        "ningún dato de pago, y en la app no se guarda información de pago ni ella la envía a "
        "ninguna parte. Cómo trata Apple esa transacción se rige por la política de privacidad de "
        "Apple, no por esta.",
        "Premium est entièrement géré par Apple via l'App Store. L'app demande au système si un "
        "achat est actif et reçoit oui ou non. Elle ne voit jamais votre compte Apple, votre nom ni "
        "aucun détail de paiement, et aucune information de paiement n'est stockée dans l'app ni "
        "envoyée où que ce soit par elle. La manière dont Apple traite cette transaction relève de "
        "la politique de confidentialité d'Apple, pas de celle-ci.",
        "Premium è gestito interamente da Apple tramite l'App Store. L'app chiede al sistema se un "
        "acquisto è attivo e riceve sì o no. Non vede mai il tuo Apple Account, il tuo nome o alcun "
        "dato di pagamento, e nell'app non viene memorizzata nessuna informazione di pagamento né "
        "viene inviata da nessuna parte. Il modo in cui Apple gestisce quella transazione è coperto "
        "dall'informativa sulla privacy di Apple, non da questa.",
        "Premium はすべて App Store を通じて Apple が処理します。アプリはシステムに購入が"
        "有効かどうかを尋ね、はい／いいえを受け取るだけです。あなたの Apple アカウントも、名前も、"
        "支払いの詳細も見ることはなく、支払い情報がアプリに保存されることも、"
        "アプリからどこかへ送られることもありません。その取引を Apple 自身がどう扱うかは、"
        "この方針ではなく Apple のプライバシーポリシーが定めます。",
        "Premium은 전부 App Store를 통해 Apple이 처리합니다. 앱은 시스템에 구매가 활성 상태인지를 "
        "묻고 예 또는 아니요를 받을 뿐입니다. 당신의 Apple 계정도, 이름도, 결제 정보도 결코 보지 "
        "못하며, 결제 정보가 앱에 저장되거나 앱이 그것을 어딘가로 보내는 일도 없습니다. 그 거래를 "
        "Apple이 어떻게 다루는지는 이 방침이 아니라 Apple의 개인정보 처리방침이 정합니다.",
        "Premium wordt volledig door Apple afgehandeld via de App Store. De app vraagt het systeem "
        "of een aankoop actief is en krijgt ja of nee. Hij ziet nooit je Apple Account, je naam of "
        "enig betaalgegeven, en er wordt geen betaalinformatie in de app opgeslagen of door de app "
        "ergens naartoe gestuurd. Hoe Apple die transactie zelf behandelt valt onder het "
        "privacybeleid van Apple, niet onder dit beleid.",
        "O Premium é tratado inteiramente pela Apple através da App Store. O app pergunta ao "
        "sistema se há uma compra ativa e recebe sim ou não. Ele nunca vê sua Conta Apple, seu nome "
        "ou qualquer dado de pagamento, e nenhuma informação de pagamento é guardada no app nem "
        "enviada por ele para lugar algum. Como a Apple trata essa transação é coberto pela "
        "política de privacidade da Apple, não por esta.",
        "Premium 完全由 Apple 通过 App Store 处理。应用只是向系统询问是否有生效的购买，"
        "并得到\"是\"或\"否\"。它永远看不到你的 Apple 账户、你的姓名或任何支付信息，"
        "应用里不会保存支付信息，也不会把它发往任何地方。Apple 自己如何处理这笔交易，"
        "由 Apple 的隐私政策规定，而不是这一份。"),
    "Children": ("Kinder", "Menores", "Menores", "Enfants", "Minori", "お子さまについて",
                 "어린이", "Kinderen", "Crianças", "儿童"),
    "Changes to this policy": ("Änderungen an dieser Erklärung", "Cambios en esta política",
                               "Cambios en esta política", "Modifications de cette politique",
                               "Modifiche a questa informativa", "この方針の変更について",
                               "이 방침의 변경", "Wijzigingen in dit beleid",
                               "Alterações nesta política", "本政策的变更"),
    "This policy may be updated from time to time. Any changes are posted on this page and take\n"
    "      effect once posted, and the date at the top changes with them.": (
        "Diese Erklärung kann von Zeit zu Zeit aktualisiert werden. Änderungen werden auf dieser "
        "Seite veröffentlicht und gelten ab der Veröffentlichung, und das Datum oben ändert sich "
        "mit ihnen.",
        "Esta política puede actualizarse de vez en cuando. Cualquier cambio se publica en esta "
        "página y entra en vigor una vez publicado, y la fecha de arriba cambia con él.",
        "Esta política puede actualizarse de vez en cuando. Cualquier cambio se publica en esta "
        "página y entra en vigor una vez publicado, y la fecha de arriba cambia con él.",
        "Cette politique peut être mise à jour de temps à autre. Toute modification est publiée sur "
        "cette page et prend effet dès sa publication, et la date en haut change avec elle.",
        "Questa informativa può essere aggiornata di tanto in tanto. Ogni modifica viene pubblicata "
        "su questa pagina ed entra in vigore una volta pubblicata, e la data in alto cambia con "
        "essa.",
        "この方針は随時更新されることがあります。変更はこのページに掲載され、掲載をもって"
        "効力を持ち、上部の日付も一緒に変わります。",
        "이 방침은 수시로 갱신될 수 있습니다. 변경 사항은 이 페이지에 게시되며 게시와 동시에 "
        "효력이 생기고, 맨 위의 날짜도 함께 바뀝니다.",
        "Dit beleid kan van tijd tot tijd worden bijgewerkt. Wijzigingen worden op deze pagina "
        "geplaatst en gaan in zodra ze geplaatst zijn, en de datum bovenaan verandert mee.",
        "Esta política pode ser atualizada de tempos em tempos. Qualquer alteração é publicada "
        "nesta página e passa a valer assim que publicada, e a data no topo muda junto.",
        "本政策可能会不时更新。任何变更都会发布在本页面上，并自发布之时起生效，"
        "顶部的日期也会随之更改。"),
    "Contact": ("Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "連絡先", "연락처",
                "Contact", "Contato", "联系"),
    "Questions about this policy or about the app:": (
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

# ---------------------------------------------------------------- 2.0
#
# The page describes 2.0, and the advertising boundary is 1.3: AdMob came out on 26 August 2026
# (Glitch App Opus 699a683), before the 1.3 build was uploaded, and the 1.3.1 tag has no ad code.
# A 30 September pass had moved the boundary to 2.0, which told 1.3 users they still had AdMob;
# corrected 6 October. Keys are written with their line wrapping collapsed; merge.py matches them.
T.update({
    "How MODUL8 handles your photos and your data. Photos and videos are processed on your device "
    "and never uploaded. From version 1.3 there is no advertising and no Google AdMob.": (
        "Wie MODUL8 mit deinen Fotos und deinen Daten umgeht. Fotos und Videos werden auf deinem "
        "Gerät verarbeitet und nie hochgeladen. Ab Version 1.3 gibt es keine Werbung und kein "
        "Google AdMob.",
        "Cómo trata MODUL8 tus fotos y tus datos. Las fotos y los vídeos se procesan en tu "
        "dispositivo y nunca se suben. Desde la versión 1.3 no hay publicidad ni Google AdMob.",
        "Cómo trata MODUL8 tus fotos y tus datos. Las fotos y los videos se procesan en tu "
        "dispositivo y nunca se suben. Desde la versión 1.3 no hay publicidad ni Google AdMob.",
        "Comment MODUL8 traite vos photos et vos données. Les photos et les vidéos sont traitées "
        "sur votre appareil et jamais envoyées. Depuis la version 1.3, il n'y a plus de publicité "
        "ni de Google AdMob.",
        "Come MODUL8 tratta le tue foto e i tuoi dati. Foto e video vengono elaborati sul tuo "
        "dispositivo e non vengono mai caricati. Dalla versione 1.3 non c'è pubblicità né Google "
        "AdMob.",
        "MODUL8 が写真とデータをどう扱うか。写真も動画も端末の上で処理され、アップロードされる"
        "ことはありません。バージョン 1.3 からは広告も Google AdMob もありません。",
        "MODUL8가 사진과 데이터를 어떻게 다루는지. 사진과 동영상은 기기 안에서 처리되고 절대 "
        "업로드되지 않습니다. 1.3 버전부터는 광고도 Google AdMob도 없습니다.",
        "Hoe MODUL8 met je foto's en je gegevens omgaat. Foto's en video's worden op je toestel "
        "verwerkt en nooit geüpload. Vanaf versie 1.3 zijn er geen advertenties en is er geen "
        "Google AdMob.",
        "Como o MODUL8 lida com suas fotos e seus dados. Fotos e vídeos são processados no seu "
        "aparelho e nunca enviados. A partir da versão 1.3 não há publicidade nem Google AdMob.",
        "MODUL8 如何处理你的照片和数据。照片和视频在你的设备上处理，永远不会上传。从 1.3 版起"
        "没有广告，也没有 Google AdMob。"),
    "Last updated 6 October 2026": (
        "Zuletzt aktualisiert am 6. Oktober 2026",
        "Última actualización: 6 de octubre de 2026",
        "Última actualización: 6 de octubre de 2026",
        "Dernière mise à jour : 6 octobre 2026", "Ultimo aggiornamento: 6 ottobre 2026",
        "最終更新：2026年10月6日", "최종 업데이트: 2026년 10월 6일",
        "Laatst bijgewerkt: 6 oktober 2026", "Última atualização: 6 de outubro de 2026",
        "最后更新：2026年10月6日"),
    "Your photos and videos are processed on your iPhone and are never uploaded anywhere. There "
    "is no image server.": (
        "Deine Fotos und Videos werden auf deinem iPhone verarbeitet und nirgendwohin "
        "hochgeladen. Es gibt keinen Bildserver.",
        "Tus fotos y vídeos se procesan en tu iPhone y no se suben a ninguna parte. No hay "
        "servidor de imágenes.",
        "Tus fotos y videos se procesan en tu iPhone y no se suben a ninguna parte. No hay "
        "servidor de imágenes.",
        "Vos photos et vidéos sont traitées sur votre iPhone et ne sont envoyées nulle part. Il "
        "n'y a pas de serveur d'images.",
        "Le tue foto e i tuoi video vengono elaborati sul tuo iPhone e non vengono caricati da "
        "nessuna parte. Non c'è nessun server di immagini.",
        "写真も動画も、あなたの iPhone の中で処理され、どこにもアップロードされません。"
        "画像サーバーもありません。",
        "사진과 영상은 당신의 iPhone 안에서 처리되고, 어디로도 업로드되지 않습니다. 이미지 "
        "서버도 없습니다.",
        "Je foto's en video's worden op je iPhone verwerkt en nergens naartoe geüpload. Er is "
        "geen beeldserver.",
        "Suas fotos e vídeos são processados no seu iPhone e nunca enviados para lugar nenhum. "
        "Não há servidor de imagens.",
        "你的照片和视频都在你的 iPhone 上处理，不会被上传到任何地方。也没有图像服务器。"),
    # Two sentences, the first in <strong>. The label is quoted in Apple's own words (see the
    # module docstring), so a reader can find the same phrase on the App Store page.
    "From version 1.3 there is no advertising and no Google AdMob.": (
        "Ab Version 1.3 gibt es keine Werbung und kein Google AdMob.",
        "Desde la versión 1.3 no hay publicidad ni Google AdMob.",
        "Desde la versión 1.3 no hay publicidad ni Google AdMob.",
        "Depuis la version 1.3, il n'y a plus de publicité ni de Google AdMob.",
        "Dalla versione 1.3 non c'è pubblicità né Google AdMob.",
        "バージョン 1.3 からは、広告も Google AdMob もありません。",
        "1.3 버전부터는 광고도 Google AdMob도 없습니다.",
        "Vanaf versie 1.3 zijn er geen advertenties en is er geen Google AdMob.",
        "A partir da versão 1.3 não há publicidade nem Google AdMob.",
        "从 1.3 版起没有广告，也没有 Google AdMob。"),
    "The App Store privacy label reads Data Not Collected. Version 1.2 and earlier showed ads in "
    "the free tier through Google AdMob, which is covered at the end for anyone still running an "
    "old copy.": (
        "Das Datenschutzetikett im App Store lautet „Keine Daten erfasst“. Version 1.2 und früher "
        "zeigten in der kostenlosen Stufe Werbung über Google AdMob; das steht am Ende, für alle, "
        "die noch eine alte Fassung benutzen.",
        "La etiqueta de privacidad de la App Store dice «No se recopilan datos». La versión 1.2 y "
        "anteriores mostraban anuncios en el nivel gratuito a través de Google AdMob, lo que se "
        "explica al final para quien siga usando una copia antigua.",
        "La etiqueta de privacidad de la App Store dice “No se recopilan datos”. La versión 1.2 y "
        "anteriores mostraban anuncios en el nivel gratuito a través de Google AdMob, lo que se "
        "explica al final para quien siga usando una copia antigua.",
        "L'étiquette de confidentialité de l'App Store indique « Données non collectées ». La "
        "version 1.2 et les précédentes affichaient des publicités dans l'offre gratuite via "
        "Google AdMob, ce qui est décrit à la fin pour ceux qui utilisent encore une ancienne "
        "copie.",
        "L'etichetta sulla privacy dell'App Store riporta «Dati non raccolti». La versione 1.2 e "
        "precedenti mostravano pubblicità nel livello gratuito tramite Google AdMob, di cui si "
        "parla alla fine per chi usa ancora una copia vecchia.",
        "App Store のプライバシーラベルは「データの収集なし」です。バージョン 1.2 以前は、"
        "無料版で Google AdMob による広告を表示していました。古いバージョンをまだ使っている方の"
        "ために、そのことは最後に説明します。",
        "App Store의 개인정보 보호 라벨은 ‘데이터가 수집되지 않음’입니다. 1.2 버전과 그 이전은 "
        "무료 등급에서 Google AdMob을 통해 광고를 표시했으며, 아직 예전 버전을 쓰는 분을 위해 "
        "끝부분에서 설명합니다.",
        "Het privacylabel in de App Store luidt ‘Er worden geen gegevens verzameld’. Versie 1.2 en "
        "eerder toonden advertenties in de gratis laag via Google AdMob; dat staat aan het einde "
        "beschreven, voor wie nog een oude versie gebruikt.",
        "O rótulo de privacidade da App Store diz “Dados não coletados”. A versão 1.2 e anteriores "
        "mostravam anúncios no nível gratuito através do Google AdMob, o que está explicado no fim "
        "para quem ainda usa uma cópia antiga.",
        "App Store 上的隐私标签写着“未收集数据”。1.2 版及更早版本曾在免费层通过 Google AdMob "
        "显示广告，文末会为仍在使用旧版本的人说明。"),
    "This policy describes MODUL8 2.0, released on 24 September 2026, and every version after it. "
    "Advertising was removed earlier, in version 1.3, so Google AdMob is not in the app. If you "
    "have not updated and are still running 1.2 or earlier, the section on advertising near the "
    "end applies to your copy.": (
        "Diese Erklärung beschreibt MODUL8 2.0, erschienen am 24. September 2026, und jede spätere "
        "Version. Die Werbung wurde schon früher entfernt, mit Version 1.3, daher ist Google AdMob "
        "nicht in der App. Wenn du nicht aktualisiert hast und noch 1.2 oder früher benutzt, gilt "
        "für deine Fassung der Abschnitt über Werbung gegen Ende.",
        "Esta política describe MODUL8 2.0, publicada el 24 de septiembre de 2026, y todas las "
        "versiones posteriores. La publicidad se eliminó antes, en la versión 1.3, así que Google "
        "AdMob no está en la app. Si no has actualizado y sigues usando la 1.2 o una anterior, la "
        "sección sobre publicidad del final se aplica a tu copia.",
        "Esta política describe MODUL8 2.0, publicada el 24 de septiembre de 2026, y todas las "
        "versiones posteriores. La publicidad se eliminó antes, en la versión 1.3, así que Google "
        "AdMob no está en la app. Si no has actualizado y sigues usando la 1.2 o una anterior, la "
        "sección sobre publicidad del final se aplica a tu copia.",
        "Cette politique décrit MODUL8 2.0, sortie le 24 septembre 2026, et toutes les versions "
        "suivantes. La publicité a été supprimée plus tôt, avec la version 1.3, donc Google AdMob "
        "n'est pas dans l'app. Si vous n'avez pas fait la mise à jour et utilisez encore la 1.2 ou "
        "une version antérieure, la section sur la publicité vers la fin s'applique à votre copie.",
        "Questa informativa descrive MODUL8 2.0, uscita il 24 settembre 2026, e ogni versione "
        "successiva. La pubblicità è stata tolta prima, con la versione 1.3, quindi Google AdMob "
        "non è nell'app. Se non hai aggiornato e usi ancora la 1.2 o una precedente, alla tua copia "
        "si applica la sezione sulla pubblicità verso la fine.",
        "このポリシーは、2026 年 9 月 24 日に公開された MODUL8 2.0 と、それ以降のすべての"
        "バージョンについて説明するものです。広告はそれより前のバージョン 1.3 で取り除かれており、"
        "Google AdMob はアプリに入っていません。まだアップデートしておらず 1.2 以前を使っている"
        "場合は、終わりのほうにある広告についての項目があなたのアプリに当てはまります。",
        "이 방침은 2026년 9월 24일에 출시된 MODUL8 2.0과 그 이후의 모든 버전을 설명합니다. 광고는 "
        "그보다 앞선 1.3 버전에서 없어졌으므로, Google AdMob은 앱에 들어 있지 않습니다. 아직 "
        "업데이트하지 않고 1.2 이하 버전을 쓰고 있다면, 끝부분의 광고 항목이 당신의 앱에 "
        "해당합니다.",
        "Dit beleid beschrijft MODUL8 2.0, uitgebracht op 24 september 2026, en elke versie "
        "daarna. Advertenties zijn al eerder weggehaald, in versie 1.3, dus Google AdMob zit niet in "
        "de app. Heb je niet bijgewerkt en gebruik je nog 1.2 of eerder, dan geldt het deel over "
        "advertenties tegen het einde voor jouw exemplaar.",
        "Esta política descreve o MODUL8 2.0, lançado em 24 de setembro de 2026, e todas as "
        "versões depois dele. A publicidade foi removida antes, na versão 1.3, então o Google AdMob "
        "não está no app. Se você não atualizou e ainda usa a 1.2 ou anterior, a seção sobre "
        "publicidade perto do fim vale para a sua cópia.",
        "本政策适用于 2026 年 9 月 24 日发布的 MODUL8 2.0 及之后的所有版本。广告在更早的 1.3 版"
        "中就已移除，因此应用里没有 Google AdMob。如果你还没有更新、仍在使用 1.2 或更早的版本，"
        "文末关于广告的部分适用于你手上的这一份。"),
    # New in October: the camera, masking and recents, each of which stays on the phone.
    "The camera is used only when you choose to shoot a photo in the app. Masking finds the "
    "subject of a picture with Apple's Vision framework, which runs on the phone, so that never "
    "leaves the device either. Your recent photo edits are kept in the app's own storage so you "
    "can reopen them, and are deleted with the app.": (
        "Die Kamera wird nur benutzt, wenn du in der App selbst ein Foto aufnimmst. Die Maskierung "
        "findet das Motiv eines Bildes mit Apples Vision-Framework, das auf dem iPhone läuft, also "
        "verlässt auch das nie das Gerät. Deine letzten Fotobearbeitungen liegen im eigenen "
        "Speicher der App, damit du sie wieder öffnen kannst, und werden mit der App gelöscht.",
        "La cámara solo se usa cuando eliges hacer una foto en la app. El enmascarado encuentra "
        "el motivo de una imagen con el framework Vision de Apple, que funciona en el teléfono, así "
        "que eso tampoco sale nunca del dispositivo. Tus ediciones de fotos recientes se guardan en "
        "el almacenamiento propio de la app para que puedas volver a abrirlas, y se borran con la "
        "app.",
        "La cámara solo se usa cuando eliges tomar una foto en la app. El enmascarado encuentra el "
        "motivo de una imagen con el framework Vision de Apple, que funciona en el teléfono, así "
        "que eso tampoco sale nunca del dispositivo. Tus ediciones de fotos recientes se guardan en "
        "el almacenamiento propio de la app para que puedas volver a abrirlas, y se borran con la "
        "app.",
        "L'appareil photo n'est utilisé que si vous choisissez de prendre une photo dans l'app. Le "
        "masquage trouve le sujet d'une image avec le framework Vision d'Apple, qui fonctionne sur "
        "le téléphone, donc cela non plus ne quitte jamais l'appareil. Vos retouches de photos "
        "récentes sont gardées dans le stockage propre de l'app pour que vous puissiez les rouvrir, "
        "et sont supprimées avec l'app.",
        "La fotocamera si usa solo quando scegli di scattare una foto nell'app. Il mascheramento "
        "trova il soggetto di un'immagine con il framework Vision di Apple, che funziona sul "
        "telefono, quindi anche questo non lascia mai il dispositivo. Le tue modifiche recenti alle "
        "foto restano nello spazio dell'app perché tu possa riaprirle, e vengono eliminate con "
        "l'app.",
        "カメラを使うのは、アプリの中で写真を撮ることを選んだときだけです。マスクは Apple の "
        "Vision フレームワークで被写体を見つけますが、これも端末の上で動くので、端末の外に出る"
        "ことはありません。最近の写真の編集は、開き直せるようにアプリ自身の保存領域に置かれ、"
        "アプリと一緒に削除されます。",
        "카메라는 앱에서 직접 사진을 찍기로 할 때만 쓰입니다. 마스킹은 Apple의 Vision 프레임워크로 "
        "사진의 피사체를 찾는데, 이것도 휴대폰에서 실행되므로 기기를 벗어나지 않습니다. 최근 사진 "
        "편집은 다시 열 수 있도록 앱 자체의 저장 공간에 보관되며, 앱과 함께 삭제됩니다.",
        "De camera wordt alleen gebruikt als je in de app zelf een foto maakt. Maskeren vindt het "
        "onderwerp van een beeld met Apples Vision-framework, dat op de telefoon draait, dus ook "
        "dat verlaat het toestel nooit. Je recente fotobewerkingen staan in de eigen opslag van de "
        "app zodat je ze opnieuw kunt openen, en worden met de app verwijderd.",
        "A câmera só é usada quando você escolhe tirar uma foto no app. O mascaramento encontra o "
        "tema de uma imagem com o framework Vision da Apple, que roda no telefone, então isso "
        "também nunca sai do aparelho. Suas edições de fotos recentes ficam no armazenamento do "
        "próprio app para que você possa reabri-las, e são apagadas junto com o app.",
        "只有在你选择在应用里拍照时才会使用相机。蒙版功能用 Apple 的 Vision 框架找出画面的主体，"
        "它同样在手机上运行，所以这部分也从不离开设备。你最近的照片编辑保存在应用自己的存储空间"
        "里，方便你重新打开，删除应用时会一并删除。"),
    "Version 1.3 onwards: no ads, no data collected": (
        "Ab Version 1.3: keine Werbung, keine Datenerfassung",
        "Desde la versión 1.3: sin anuncios, sin recopilación de datos",
        "Desde la versión 1.3: sin anuncios, sin recopilación de datos",
        "À partir de la version 1.3 : pas de publicité, aucune donnée collectée",
        "Dalla versione 1.3: niente pubblicità, nessun dato raccolto",
        "バージョン 1.3 以降：広告なし、データの収集なし",
        "1.3 버전부터: 광고 없음, 데이터 수집 없음",
        "Vanaf versie 1.3: geen advertenties, geen gegevens verzameld",
        "Da versão 1.3 em diante: sem anúncios, sem coleta de dados",
        "1.3 版起：没有广告，不收集数据"),
    "MODUL8 shows no ads and does not include Google AdMob or any other advertising SDK. Nothing "
    "you open in it is uploaded, and its App Store privacy label reads Data Not Collected: we do "
    "not collect data from the app, and nothing in it is used to track you across apps or "
    "websites.": (
        "MODUL8 zeigt keine Werbung und enthält weder Google AdMob noch ein anderes Werbe-SDK. "
        "Nichts, was du darin öffnest, wird hochgeladen, und das Datenschutzetikett im App Store "
        "lautet „Keine Daten erfasst“: Wir erfassen keine Daten aus der App, und nichts darin wird "
        "genutzt, um dich über Apps oder Websites hinweg zu verfolgen.",
        "MODUL8 no muestra anuncios y no incluye Google AdMob ni ningún otro SDK de publicidad. "
        "Nada de lo que abres en ella se sube, y su etiqueta de privacidad en la App Store dice "
        "«No se recopilan datos»: no recopilamos datos desde la app, y nada en ella se usa para "
        "seguirte entre apps o sitios web.",
        "MODUL8 no muestra anuncios y no incluye Google AdMob ni ningún otro SDK de publicidad. "
        "Nada de lo que abres en ella se sube, y su etiqueta de privacidad en la App Store dice "
        "“No se recopilan datos”: no recopilamos datos desde la app, y nada en ella se usa para "
        "rastrearte entre apps o sitios web.",
        "MODUL8 n'affiche aucune publicité et n'intègre ni Google AdMob ni aucun autre SDK "
        "publicitaire. Rien de ce que vous y ouvrez n'est envoyé, et son étiquette de "
        "confidentialité sur l'App Store indique « Données non collectées » : nous ne collectons "
        "aucune donnée depuis l'app, et rien en elle ne sert à vous suivre d'une app ou d'un site "
        "web à l'autre.",
        "MODUL8 non mostra pubblicità e non include Google AdMob né alcun altro SDK pubblicitario. "
        "Niente di quello che ci apri viene caricato, e la sua etichetta sulla privacy nell'App "
        "Store riporta «Dati non raccolti»: non raccogliamo dati dall'app, e niente al suo interno "
        "viene usato per tracciarti fra app o siti web.",
        "MODUL8 は広告を表示せず、Google AdMob もほかの広告 SDK も入っていません。開いたものが"
        "アップロードされることはなく、App Store のプライバシーラベルは「データの収集なし」です。"
        "私たちはアプリからデータを収集せず、アプリや Web サイトをまたいであなたを追跡するために"
        "使われるものも、アプリの中にはありません。",
        "MODUL8는 광고를 표시하지 않으며, Google AdMob이나 다른 어떤 광고 SDK도 들어 있지 "
        "않습니다. 앱에서 연 것은 무엇도 업로드되지 않고, App Store의 개인정보 보호 라벨은 "
        "‘데이터가 수집되지 않음’입니다. 저희는 앱에서 데이터를 수집하지 않으며, 앱 안의 어떤 것도 "
        "앱이나 웹사이트를 넘나들며 당신을 추적하는 데 쓰이지 않습니다.",
        "MODUL8 toont geen advertenties en bevat geen Google AdMob of enige andere "
        "advertentie-SDK. Niets wat je erin opent wordt geüpload, en het privacylabel in de App "
        "Store luidt ‘Er worden geen gegevens verzameld’: wij verzamelen geen gegevens uit de app, "
        "en niets erin wordt gebruikt om je over apps of websites heen te volgen.",
        "O MODUL8 não mostra anúncios e não inclui o Google AdMob nem nenhum outro SDK de "
        "publicidade. Nada do que você abre nele é enviado, e o rótulo de privacidade dele na App "
        "Store diz “Dados não coletados”: não coletamos dados pelo app, e nada nele é usado para "
        "rastrear você entre apps ou sites.",
        "MODUL8 不显示广告，也不包含 Google AdMob 或任何其他广告 SDK。你在里面打开的任何东西都"
        "不会被上传，它在 App Store 上的隐私标签写着“未收集数据”：我们不从应用中收集数据，"
        "应用里也没有任何东西被用来跨应用或跨网站追踪你。"),
    "Because we hold nothing, there is no data to request or delete. Deleting the app removes its "
    "settings with it.": (
        "Weil wir nichts haben, gibt es auch keine Daten, die du anfordern oder löschen lassen "
        "könntest. Löschst du die App, verschwinden ihre Einstellungen mit ihr.",
        "Como no guardamos nada, no hay datos que solicitar ni que borrar. Borrar la app se lleva "
        "sus ajustes con ella.",
        "Como no guardamos nada, no hay datos que solicitar ni que borrar. Borrar la app se lleva "
        "sus ajustes con ella.",
        "Comme nous ne détenons rien, il n'y a aucune donnée à demander ni à supprimer. Supprimer "
        "l'app emporte ses réglages avec elle.",
        "Poiché non conserviamo nulla, non ci sono dati da richiedere o cancellare. Eliminando "
        "l'app spariscono con essa le sue impostazioni.",
        "私たちは何も保持していないので、開示や削除を請求すべきデータもありません。アプリを"
        "削除すれば、その設定も一緒になくなります。",
        "저희가 가진 것이 없으므로, 열람이나 삭제를 요청할 데이터도 없습니다. 앱을 삭제하면 그 "
        "설정도 함께 사라집니다.",
        "Omdat wij niets bewaren, zijn er ook geen gegevens om op te vragen of te laten wissen. De "
        "app verwijderen neemt de instellingen mee.",
        "Como não guardamos nada, não há dados para solicitar ou apagar. Apagar o app leva as "
        "configurações dele junto.",
        "因为我们什么都没有保存，也就没有数据可以索取或删除。删除应用时，它的设置也会一并消失。"),
    "The free tier of version 1.2 and earlier showed ads through Google AdMob, the one part of "
    "those versions that involved a third party. Premium removed them, and updating to 1.3 "
    "removes AdMob altogether. In those versions AdMob could collect and use:": (
        "Die kostenlose Stufe von Version 1.2 und früher zeigte Werbung über Google AdMob, den "
        "einzigen Teil dieser Versionen, an dem ein Dritter beteiligt war. Premium entfernte sie, "
        "und das Update auf 1.3 entfernt AdMob ganz. In diesen Versionen konnte AdMob Folgendes "
        "erheben und nutzen:",
        "El nivel gratuito de la versión 1.2 y anteriores mostraba anuncios a través de Google "
        "AdMob, la única parte de esas versiones en la que intervenía un tercero. Premium los "
        "quitaba, y actualizar a la 1.3 elimina AdMob por completo. En esas versiones AdMob podía "
        "recopilar y usar:",
        "El nivel gratuito de la versión 1.2 y anteriores mostraba anuncios a través de Google "
        "AdMob, la única parte de esas versiones en la que intervenía un tercero. Premium los "
        "quitaba, y actualizar a la 1.3 elimina AdMob por completo. En esas versiones AdMob podía "
        "recopilar y usar:",
        "L'offre gratuite de la version 1.2 et des précédentes affichait des publicités via "
        "Google AdMob, la seule partie de ces versions qui faisait intervenir un tiers. Premium "
        "les supprimait, et la mise à jour vers la 1.3 retire complètement AdMob. Dans ces "
        "versions, AdMob pouvait collecter et utiliser :",
        "Il livello gratuito della versione 1.2 e precedenti mostrava pubblicità tramite Google "
        "AdMob, l'unica parte di quelle versioni che coinvolgeva una terza parte. Premium la "
        "toglieva, e aggiornare alla 1.3 elimina AdMob del tutto. In quelle versioni AdMob poteva "
        "raccogliere e usare:",
        "バージョン 1.2 以前の無料版は、Google AdMob を通じて広告を表示していました。それらの"
        "バージョンで第三者が関わる唯一の部分です。Premium では広告が消え、1.3 にアップデート"
        "すれば AdMob そのものがなくなります。それらのバージョンで AdMob が収集・利用できたのは"
        "次のものです。",
        "1.2 버전과 그 이전의 무료 등급은 Google AdMob을 통해 광고를 표시했으며, 그 버전들에서 "
        "제3자가 관여한 유일한 부분이었습니다. Premium은 광고를 없앴고, 1.3으로 업데이트하면 AdMob "
        "자체가 사라집니다. 그 버전들에서 AdMob은 다음을 수집하고 사용할 수 있었습니다.",
        "De gratis laag van versie 1.2 en eerder toonde advertenties via Google AdMob, het enige "
        "deel van die versies waar een derde partij bij betrokken was. Premium haalde ze weg, en "
        "bijwerken naar 1.3 haalt AdMob helemaal weg. In die versies kon AdMob het volgende "
        "verzamelen en gebruiken:",
        "O nível gratuito da versão 1.2 e anteriores mostrava anúncios através do Google AdMob, a "
        "única parte dessas versões que envolvia terceiros. O Premium os removia, e atualizar para "
        "a 1.3 remove o AdMob por completo. Nessas versões o AdMob podia coletar e usar:",
        "1.2 版及更早版本的免费层通过 Google AdMob 显示广告，这是那些版本中唯一涉及第三方的"
        "部分。Premium 会去掉广告，而更新到 1.3 则会彻底移除 AdMob。在那些版本中，AdMob 可能"
        "收集并使用："),
    "MODUL8 is not directed at anyone under 13, and we do not knowingly collect personally "
    "identifiable information from anyone under 13. From version 1.3 the app collects nothing "
    "from anybody, of any age. If you are a parent or guardian and believe your child gave us "
    "personal data through an earlier version, please get in touch and we will remove it.": (
        "MODUL8 richtet sich nicht an Personen unter 13 Jahren, und wir erheben wissentlich keine "
        "personenbezogenen Daten von Personen unter 13. Ab Version 1.3 sammelt die App von "
        "niemandem etwas, in keinem Alter. Wenn du Elternteil oder Erziehungsberechtigte bist und "
        "glaubst, dass dein Kind uns über eine frühere Version personenbezogene Daten gegeben hat, "
        "melde dich, und wir entfernen sie.",
        "MODUL8 no está dirigida a menores de 13 años, y no recogemos a sabiendas información "
        "personal identificable de menores de 13. Desde la versión 1.3 la app no recoge nada de "
        "nadie, de ninguna edad. Si eres madre, padre o tutor y crees que tu hijo nos dio datos "
        "personales a través de una versión anterior, ponte en contacto y los eliminaremos.",
        "MODUL8 no está dirigida a menores de 13 años, y no recogemos a sabiendas información "
        "personal identificable de menores de 13. Desde la versión 1.3 la app no recoge nada de "
        "nadie, de ninguna edad. Si eres madre, padre o tutor y crees que tu hijo nos dio datos "
        "personales a través de una versión anterior, ponte en contacto y los eliminaremos.",
        "MODUL8 ne s'adresse pas aux personnes de moins de 13 ans, et nous ne collectons pas "
        "sciemment d'informations personnelles identifiables auprès de personnes de moins de 13 "
        "ans. Depuis la version 1.3, l'app ne collecte rien de personne, à tout âge. Si vous êtes "
        "parent ou tuteur et pensez que votre enfant nous a donné des données personnelles via une "
        "version antérieure, contactez-nous et nous les supprimerons.",
        "MODUL8 non è rivolta a chi ha meno di 13 anni, e non raccogliamo consapevolmente "
        "informazioni personali identificabili da chi ha meno di 13 anni. Dalla versione 1.3 l'app "
        "non raccoglie niente da nessuno, di qualunque età. Se sei un genitore o un tutore e pensi "
        "che tuo figlio ci abbia dato dati personali tramite una versione precedente, scrivici e li "
        "rimuoveremo.",
        "MODUL8 は 13 歳未満の方を対象としておらず、13 歳未満の方から個人を特定できる情報を"
        "意図して収集することはありません。バージョン 1.3 以降、アプリは年齢を問わず誰からも"
        "何も収集しません。保護者の方で、以前のバージョンを通じてお子さまが個人データを"
        "渡したとお考えの場合は、ご連絡いただければ削除します。",
        "MODUL8는 13세 미만을 대상으로 하지 않으며, 13세 미만으로부터 개인 식별 정보를 알면서 "
        "수집하지 않습니다. 1.3 버전부터 앱은 나이에 관계없이 누구에게서도 아무것도 수집하지 "
        "않습니다. 보호자이시고 자녀가 이전 버전을 통해 개인 정보를 제공했다고 생각되시면, "
        "연락 주시면 삭제하겠습니다.",
        "MODUL8 richt zich niet op mensen onder de 13, en wij verzamelen niet bewust persoonlijk "
        "identificeerbare informatie van mensen onder de 13. Vanaf versie 1.3 verzamelt de app van "
        "niemand iets, ongeacht leeftijd. Ben je ouder of voogd en denk je dat je kind ons via een "
        "eerdere versie persoonsgegevens heeft gegeven, neem dan contact op en we verwijderen ze.",
        "O MODUL8 não é direcionado a menores de 13 anos, e não coletamos conscientemente "
        "informações pessoalmente identificáveis de menores de 13. A partir da versão 1.3 o app não "
        "coleta nada de ninguém, de qualquer idade. Se você é mãe, pai ou responsável e acredita "
        "que seu filho nos deu dados pessoais por uma versão anterior, entre em contato e nós "
        "removeremos.",
        "MODUL8 并非面向 13 岁以下人群，我们也不会有意收集 13 岁以下人群的个人身份信息。"
        "自 1.3 版起，应用不会从任何年龄的任何人那里收集任何东西。如果你是家长或监护人，"
        "并认为你的孩子通过更早的版本向我们提供了个人数据，请与我们联系，我们会将其删除。"),
})

KEEP |= {"Discord"}  # the community server, a name in every language
