"""lf.wtf/modul8/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

This page was held back from the first localisation pass because it still described Google AdMob as
current, which 1.3 removes. It now states both positions with the version boundary explicit, and
that boundary is the thing a translation must not blur: 1.2 is what the App Store is serving while
1.3 is in review, so the advertising section still applies to most people reading it.

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
    "How MODUL8 handles your photos and your data. Photos are processed on your device and never "
    "uploaded. From version 1.3 there is no advertising and no networking code at all.": (
        "Wie MODUL8 mit deinen Fotos und deinen Daten umgeht. Fotos werden auf deinem Gerät "
        "verarbeitet und nie hochgeladen. Ab Version 1.3 gibt es keine Werbung und überhaupt "
        "keinen Netzwerkcode.",
        "Cómo trata MODUL8 tus fotos y tus datos. Las fotos se procesan en tu dispositivo y nunca "
        "se suben. Desde la versión 1.3 no hay publicidad ni nada de código de red.",
        "Cómo trata MODUL8 tus fotos y tus datos. Las fotos se procesan en tu dispositivo y nunca "
        "se suben. Desde la versión 1.3 no hay publicidad ni nada de código de red.",
        "Comment MODUL8 traite vos photos et vos données. Les photos sont traitées sur votre "
        "appareil et jamais envoyées. Depuis la version 1.3, il n'y a plus de publicité ni aucun "
        "code réseau.",
        "Come MODUL8 tratta le tue foto e i tuoi dati. Le foto vengono elaborate sul tuo "
        "dispositivo e non vengono mai caricate. Dalla versione 1.3 non c'è pubblicità né alcun "
        "codice di rete.",
        "MODUL8 が写真とデータをどう扱うか。写真は端末の上で処理され、アップロードされることは"
        "ありません。バージョン 1.3 からは広告がなく、通信のコードそのものもありません。",
        "MODUL8가 사진과 데이터를 어떻게 다루는지. 사진은 기기 안에서 처리되고 절대 업로드되지 "
        "않습니다. 1.3 버전부터는 광고도, 네트워크 코드도 전혀 없습니다.",
        "Hoe MODUL8 met je foto's en je gegevens omgaat. Foto's worden op je toestel verwerkt en "
        "nooit geüpload. Vanaf versie 1.3 is er geen advertentie en helemaal geen netwerkcode.",
        "Como o MODUL8 lida com suas fotos e seus dados. As fotos são processadas no seu aparelho e "
        "nunca enviadas. A partir da versão 1.3 não há publicidade nem nenhum código de rede.",
        "MODUL8 如何处理你的照片和数据。照片在你的设备上处理，永远不会上传。从 1.3 版起没有广告，"
        "也完全没有联网代码。"),
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
    "Your photos and videos are processed on your iPhone and\n      are never uploaded anywhere. "
    "There is no account and no image server.": (
        "Deine Fotos und Videos werden auf deinem iPhone verarbeitet und nirgendwohin hochgeladen. "
        "Es gibt kein Konto und keinen Bildserver.",
        "Tus fotos y vídeos se procesan en tu iPhone y no se suben a ninguna parte. No hay cuenta "
        "ni servidor de imágenes.",
        "Tus fotos y videos se procesan en tu iPhone y no se suben a ninguna parte. No hay cuenta "
        "ni servidor de imágenes.",
        "Vos photos et vidéos sont traitées sur votre iPhone et ne sont envoyées nulle part. Il n'y "
        "a pas de compte et pas de serveur d'images.",
        "Le tue foto e i tuoi video vengono elaborati sul tuo iPhone e non vengono caricati da "
        "nessuna parte. Non c'è account e non c'è server di immagini.",
        "写真も動画も、あなたの iPhone の中で処理され、どこにもアップロードされません。"
        "アカウントも、画像サーバーもありません。",
        "사진과 영상은 당신의 iPhone 안에서 처리되고, 어디로도 업로드되지 않습니다. 계정도, 이미지 "
        "서버도 없습니다.",
        "Je foto's en video's worden op je iPhone verwerkt en nergens naartoe geüpload. Er is geen "
        "account en geen beeldserver.",
        "Suas fotos e vídeos são processados no seu iPhone e nunca enviados para lugar nenhum. Não "
        "há conta nem servidor de imagens.",
        "你的照片和视频都在你的 iPhone 上处理，不会被上传到任何地方。没有账号，也没有图像服务器。"),
    # One sentence, split by <strong>. [A] then the rest.
    "From version 1.3 there is no advertising": (
        "Ab Version 1.3 gibt es keine Werbung", "Desde la versión 1.3 no hay publicidad",
        "Desde la versión 1.3 no hay publicidad", "Depuis la version 1.3, il n'y a plus de publicité",
        "Dalla versione 1.3 non c'è pubblicità", "バージョン 1.3 からは広告がありません",
        "1.3 버전부터는 광고가 없고", "Vanaf versie 1.3 is er geen advertentie",
        "A partir da versão 1.3 não há publicidade", "从 1.3 版起没有广告"),
    ", and the app contains no\n      networking code at all. Version 1.2 and earlier show ads in "
    "the free tier through Google\n      AdMob. Both are described below, because 1.2 is what is on "
    "the App Store while 1.3 is in\n      review.": (
        ", und die App enthält überhaupt keinen Netzwerkcode. Version 1.2 und früher zeigen in der "
        "kostenlosen Stufe Werbung über Google AdMob. Beides steht unten, weil 1.2 das ist, was im "
        "App Store liegt, solange 1.3 in Prüfung ist.",
        ", y la app no contiene nada de código de red. La versión 1.2 y anteriores muestran "
        "anuncios en el nivel gratuito a través de Google AdMob. Ambas se describen abajo, porque "
        "1.2 es lo que hay en la App Store mientras 1.3 está en revisión.",
        ", y la app no contiene nada de código de red. La versión 1.2 y anteriores muestran "
        "anuncios en el nivel gratuito a través de Google AdMob. Ambas se describen abajo, porque "
        "1.2 es lo que hay en la App Store mientras 1.3 está en revisión.",
        ", et l'app ne contient aucun code réseau. La version 1.2 et les précédentes affichent des "
        "publicités dans l'offre gratuite via Google AdMob. Les deux sont décrites ci-dessous, "
        "parce que 1.2 est ce qui se trouve sur l'App Store tant que 1.3 est en cours d'examen.",
        ", e l'app non contiene proprio codice di rete. La versione 1.2 e precedenti mostrano "
        "pubblicità nel livello gratuito tramite Google AdMob. Entrambe sono descritte sotto, "
        "perché 1.2 è quello che c'è sull'App Store finché 1.3 è in revisione.",
        "。アプリには通信のコードそのものが入っていません。バージョン 1.2 以前は、"
        "無料版で Google AdMob による広告を表示します。1.3 が審査中のあいだ App Store にあるのは "
        "1.2 なので、下では両方について説明します。",
        ", 앱에는 네트워크 코드 자체가 들어 있지 않습니다. 1.2 버전과 그 이전은 무료 등급에서 "
        "Google AdMob을 통해 광고를 표시합니다. 1.3이 심사 중인 동안 App Store에 올라와 있는 것은 "
        "1.2이므로, 아래에서 둘 다 설명합니다.",
        ", en de app bevat helemaal geen netwerkcode. Versie 1.2 en eerder tonen advertenties in de "
        "gratis laag via Google AdMob. Beide staan hieronder beschreven, omdat 1.2 is wat er in de "
        "App Store staat zolang 1.3 in beoordeling is.",
        ", e o app não contém nenhum código de rede. A versão 1.2 e anteriores mostram anúncios no "
        "nível gratuito através do Google AdMob. As duas estão descritas abaixo, porque 1.2 é o que "
        "está na App Store enquanto a 1.3 está em análise.",
        "，应用里也完全没有联网代码。1.2 版及更早版本会在免费层通过 Google AdMob 显示广告。"
        "下面两种情况都会说明，因为在 1.3 通过审核之前，App Store 上的仍然是 1.2。"),
    "Which version this describes": (
        "Welche Version hier beschrieben wird", "Qué versión describe esto",
        "Qué versión describe esto", "Quelle version ceci décrit",
        "Quale versione descrive questo", "この文書が対象とするバージョン",
        "이 문서가 설명하는 버전", "Welke versie dit beschrijft",
        "Qual versão isto descreve", "本文所描述的版本"),
    "MODUL8 1.3 removes advertising entirely. Google AdMob, the consent form it required in Europe\n"
    "      and Apple's App Tracking Transparency prompt are all gone from the app, and with them "
    "the only\n      code that ever talked to the network. Until 1.3 clears review, the App Store "
    "is still serving\n      1.2, so the section on advertising below still applies to the copy you "
    "are most likely to have.": (
        "MODUL8 1.3 entfernt die Werbung vollständig. Google AdMob, das Einwilligungsformular, das "
        "es in Europa verlangte, und Apples App-Tracking-Transparency-Abfrage sind alle aus der App "
        "verschwunden, und mit ihnen der einzige Code, der je mit dem Netz gesprochen hat. Bis 1.3 "
        "die Prüfung besteht, liefert der App Store weiterhin 1.2 aus, der Abschnitt zur Werbung "
        "unten gilt also weiterhin für die Fassung, die du am ehesten hast.",
        "MODUL8 1.3 elimina la publicidad por completo. Google AdMob, el formulario de "
        "consentimiento que exigía en Europa y el aviso de App Tracking Transparency de Apple han "
        "desaparecido de la app, y con ellos el único código que alguna vez habló con la red. Hasta "
        "que 1.3 pase la revisión, la App Store sigue sirviendo 1.2, así que la sección de "
        "publicidad de abajo sigue aplicándose a la copia que es más probable que tengas.",
        "MODUL8 1.3 elimina la publicidad por completo. Google AdMob, el formulario de "
        "consentimiento que exigía en Europa y el aviso de App Tracking Transparency de Apple "
        "desaparecieron de la app, y con ellos el único código que alguna vez habló con la red. "
        "Hasta que 1.3 pase la revisión, la App Store sigue sirviendo 1.2, así que la sección de "
        "publicidad de abajo sigue aplicándose a la copia que es más probable que tengas.",
        "MODUL8 1.3 supprime la publicité entièrement. Google AdMob, le formulaire de consentement "
        "qu'il imposait en Europe et l'invite App Tracking Transparency d'Apple ont tous disparu de "
        "l'app, et avec eux le seul code qui ait jamais parlé au réseau. Tant que 1.3 n'a pas passé "
        "l'examen, l'App Store sert encore 1.2, et la section sur la publicité ci-dessous "
        "s'applique donc toujours à la version que vous avez le plus probablement.",
        "MODUL8 1.3 rimuove del tutto la pubblicità. Google AdMob, il modulo di consenso che "
        "richiedeva in Europa e la richiesta App Tracking Transparency di Apple sono spariti "
        "dall'app, e con loro l'unico codice che abbia mai parlato con la rete. Finché 1.3 non "
        "supera la revisione, l'App Store serve ancora la 1.2, quindi la sezione sulla pubblicità "
        "qui sotto vale ancora per la copia che è più probabile tu abbia.",
        "MODUL8 1.3 は広告を完全になくします。Google AdMob も、それがヨーロッパで要求していた"
        "同意フォームも、Apple の App Tracking Transparency の確認も、すべてアプリから消え、"
        "同時に、これまでネットワークと話していた唯一のコードも消えました。1.3 が審査を通るまで "
        "App Store が配信しているのは 1.2 なので、下の広告に関する節は、"
        "あなたが持っている可能性が高いほうの版に今も当てはまります。",
        "MODUL8 1.3은 광고를 완전히 없앱니다. Google AdMob도, 그것이 유럽에서 요구하던 동의 "
        "양식도, Apple의 App Tracking Transparency 안내도 모두 앱에서 사라졌고, 그와 함께 지금까지 "
        "네트워크와 이야기하던 유일한 코드도 사라졌습니다. 1.3이 심사를 통과할 때까지 App Store가 "
        "제공하는 것은 1.2이므로, 아래 광고에 관한 절은 당신이 가지고 있을 가능성이 높은 쪽에 "
        "여전히 해당합니다.",
        "MODUL8 1.3 haalt de advertenties er helemaal uit. Google AdMob, het toestemmingsformulier "
        "dat het in Europa vereiste en Apples App Tracking Transparency-vraag zijn allemaal uit de "
        "app verdwenen, en daarmee de enige code die ooit met het netwerk sprak. Totdat 1.3 de "
        "beoordeling doorkomt, levert de App Store nog 1.2, dus het stuk over advertenties "
        "hieronder geldt nog steeds voor de versie die je het waarschijnlijkst hebt.",
        "O MODUL8 1.3 remove a publicidade por completo. O Google AdMob, o formulário de "
        "consentimento que ele exigia na Europa e o aviso de App Tracking Transparency da Apple "
        "sumiram todos do app, e com eles o único código que alguma vez falou com a rede. Até a 1.3 "
        "passar na análise, a App Store ainda serve a 1.2, então a seção sobre publicidade abaixo "
        "continua valendo para a cópia que você provavelmente tem.",
        "MODUL8 1.3 彻底移除了广告。Google AdMob、它在欧洲要求的同意表单，"
        "以及 Apple 的 App Tracking Transparency 提示，全部从应用中消失，"
        "随之消失的还有唯一曾与网络通信的代码。在 1.3 通过审核之前，App Store 提供的仍然是 1.2，"
        "所以下面关于广告的部分，依然适用于你手上最可能的那个版本。"),
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
    "Version 1.3 onwards: nothing is collected": (
        "Ab Version 1.3: Es wird nichts gesammelt",
        "Desde la versión 1.3: no se recoge nada", "Desde la versión 1.3: no se recoge nada",
        "À partir de la version 1.3 : rien n'est collecté",
        "Dalla versione 1.3: non si raccoglie niente",
        "バージョン 1.3 以降：何も収集しません", "1.3 버전부터: 아무것도 수집하지 않습니다",
        "Vanaf versie 1.3: er wordt niets verzameld",
        "Da versão 1.3 em diante: nada é coletado", "1.3 版起：什么都不收集"),
    "No analytics. No crash reporting. No advertising identifier. No third-party SDKs of any kind.\n"
    "      No tracking across apps or websites. The app contains no networking code, so there is "
    "nothing\n      to upload and no server holding a copy of anything.": (
        "Keine Analyse. Keine Absturzberichte. Keine Werbe-ID. Keinerlei SDKs von Dritten. Kein "
        "Tracking über Apps oder Websites hinweg. Die App enthält keinen Netzwerkcode, es gibt also "
        "nichts hochzuladen und keinen Server, der eine Kopie von irgendetwas hält.",
        "Sin analíticas. Sin informes de fallos. Sin identificador de publicidad. Sin SDK de "
        "terceros de ningún tipo. Sin seguimiento entre apps o sitios web. La app no contiene "
        "código de red, así que no hay nada que subir ni servidor alguno guardando una copia de "
        "nada.",
        "Sin analíticas. Sin informes de fallas. Sin identificador de publicidad. Sin SDK de "
        "terceros de ningún tipo. Sin seguimiento entre apps o sitios web. La app no contiene "
        "código de red, así que no hay nada que subir ni servidor alguno guardando una copia de "
        "nada.",
        "Pas d'analytique. Pas de rapport de plantage. Pas d'identifiant publicitaire. Aucun SDK "
        "tiers d'aucune sorte. Pas de suivi entre apps ou sites web. L'app ne contient aucun code "
        "réseau, il n'y a donc rien à envoyer et aucun serveur qui garde une copie de quoi que ce "
        "soit.",
        "Nessuna analisi. Nessuna segnalazione di crash. Nessun identificatore pubblicitario. "
        "Nessun SDK di terze parti di alcun tipo. Nessun tracciamento fra app o siti web. L'app non "
        "contiene codice di rete, quindi non c'è niente da caricare e nessun server che tenga una "
        "copia di niente.",
        "解析なし。クラッシュ報告なし。広告識別子なし。いかなる第三者 SDK もなし。アプリや"
        "ウェブサイトをまたぐトラッキングなし。アプリには通信のコードが入っていないので、"
        "送るものも、何かの控えを持つサーバーもありません。",
        "분석 없음. 크래시 리포트 없음. 광고 식별자 없음. 어떤 종류의 서드파티 SDK도 없음. 앱이나 "
        "웹사이트를 넘나드는 추적 없음. 앱에는 네트워크 코드가 없어서, 올릴 것도 없고 무언가의 "
        "사본을 가진 서버도 없습니다.",
        "Geen analytics. Geen crashrapportage. Geen advertentie-identificatie. Geen SDK's van "
        "derden van welke aard dan ook. Geen tracking over apps of websites heen. De app bevat geen "
        "netwerkcode, dus er valt niets te uploaden en er is geen server met een kopie van wat dan "
        "ook.",
        "Sem análises. Sem relatório de falhas. Sem identificador de publicidade. Sem SDKs de "
        "terceiros de nenhum tipo. Sem rastreamento entre apps ou sites. O app não contém código de "
        "rede, então não há nada para enviar e nenhum servidor guardando cópia de nada.",
        "没有分析。没有崩溃报告。没有广告标识符。没有任何第三方 SDK。没有跨应用或跨网站的追踪。"
        "应用里没有联网代码，所以没有东西可上传，也没有服务器留着任何副本。"),
    "Because none of this exists, there is also nothing to opt out of and no data to request or\n"
    "      delete. Deleting the app removes its settings with it.": (
        "Weil nichts davon existiert, gibt es auch nichts, wovon man sich abmelden könnte, und "
        "keine Daten, die man anfordern oder löschen könnte. Löschst du die App, verschwinden ihre "
        "Einstellungen mit ihr.",
        "Como nada de esto existe, tampoco hay nada de lo que darse de baja ni datos que solicitar "
        "o borrar. Borrar la app se lleva sus ajustes con ella.",
        "Como nada de esto existe, tampoco hay nada de lo que darse de baja ni datos que solicitar "
        "o borrar. Borrar la app se lleva sus ajustes con ella.",
        "Comme rien de tout cela n'existe, il n'y a rien dont se désinscrire ni de données à "
        "demander ou supprimer. Supprimer l'app emporte ses réglages avec elle.",
        "Dato che niente di tutto questo esiste, non c'è nemmeno niente da cui disiscriversi né "
        "dati da richiedere o cancellare. Eliminando l'app spariscono con essa le sue impostazioni.",
        "こうしたものがそもそも存在しないため、オプトアウトすべきものも、開示や削除を請求すべき"
        "データもありません。アプリを削除すれば、その設定も一緒になくなります。",
        "이런 것들이 애초에 존재하지 않으므로, 수신을 거부할 것도, 열람이나 삭제를 요청할 데이터도 "
        "없습니다. 앱을 삭제하면 그 설정도 함께 사라집니다.",
        "Omdat niets hiervan bestaat, valt er ook nergens uit te stappen en zijn er geen gegevens "
        "om op te vragen of te laten wissen. De app verwijderen neemt de instellingen mee.",
        "Como nada disso existe, também não há nada para recusar nem dados para solicitar ou "
        "apagar. Apagar o app leva as configurações dele junto.",
        "因为这些统统不存在，也就没有什么可以退出，没有数据可以索取或删除。"
        "删除应用时，它的设置也会一并消失。"),
    "Version 1.2 and earlier: advertising": (
        "Version 1.2 und früher: Werbung", "Versión 1.2 y anteriores: publicidad",
        "Versión 1.2 y anteriores: publicidad", "Version 1.2 et antérieures : publicité",
        "Versione 1.2 e precedenti: pubblicità", "バージョン 1.2 以前：広告について",
        "1.2 버전과 그 이전: 광고", "Versie 1.2 en eerder: advertenties",
        "Versão 1.2 e anteriores: publicidade", "1.2 版及更早版本：广告"),
    "The free version showed ads through Google AdMob, which was the one part of the app that\n"
    "      involved a third party. Premium removed them. AdMob could collect and use:": (
        "Die kostenlose Fassung zeigte Werbung über Google AdMob, und das war der eine Teil der "
        "App, an dem ein Dritter beteiligt war. Premium entfernte sie. AdMob konnte erheben und "
        "nutzen:",
        "La versión gratuita mostraba anuncios a través de Google AdMob, que era la única parte de "
        "la app en la que intervenía un tercero. Premium los quitaba. AdMob podía recoger y usar:",
        "La versión gratuita mostraba anuncios a través de Google AdMob, que era la única parte de "
        "la app en la que intervenía un tercero. Premium los quitaba. AdMob podía recoger y usar:",
        "La version gratuite affichait des publicités via Google AdMob, la seule partie de l'app "
        "impliquant un tiers. Premium les supprimait. AdMob pouvait collecter et utiliser :",
        "La versione gratuita mostrava pubblicità tramite Google AdMob, che era l'unica parte "
        "dell'app in cui interveniva un terzo. Premium le toglieva. AdMob poteva raccogliere e "
        "usare:",
        "無料版は Google AdMob を通じて広告を表示していました。第三者が関わるのは、"
        "アプリのなかでその部分だけでした。Premium にすると広告はなくなりました。"
        "AdMob が収集し利用しうるのは次のものです。",
        "무료 버전은 Google AdMob을 통해 광고를 표시했고, 제3자가 관여하는 부분은 앱에서 그것뿐이 "
        "었습니다. Premium은 광고를 없앴습니다. AdMob이 수집하고 사용할 수 있었던 것은 다음과 "
        "같습니다.",
        "De gratis versie toonde advertenties via Google AdMob, het enige deel van de app waar een "
        "derde partij bij betrokken was. Premium haalde ze weg. AdMob kon verzamelen en gebruiken:",
        "A versão gratuita mostrava anúncios através do Google AdMob, que era a única parte do app "
        "em que um terceiro entrava. O Premium os removia. O AdMob podia coletar e usar:",
        "免费版通过 Google AdMob 显示广告，那是应用中唯一涉及第三方的部分。Premium 会去掉它们。"
        "AdMob 可能收集并使用："),
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
    "MODUL8 is not directed at anyone under 13, and we do not knowingly collect personally\n"
    "      identifiable information from anyone under 13. From version 1.3 the app collects nothing "
    "from\n      anybody, of any age. If you are a parent or guardian and believe your child gave "
    "us personal\n      data through an earlier version, please get in touch and we will remove it.": (
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


T['Last updated 27 August 2026'] = ('Zuletzt aktualisiert am 27. August 2026', 'Última actualización: 27 de agosto de 2026', 'Última actualización: 27 de agosto de 2026', 'Dernière mise à jour : 27 août 2026', 'Ultimo aggiornamento: 27 agosto 2026', '最終更新：2026年8月27日', '최종 업데이트: 2026년 8월 27일', 'Laatst bijgewerkt: 27 augustus 2026', 'Última atualização: 27 de agosto de 2026', '最后更新：2026年8月27日')
