"""lf.wtf/kippu/privacy, in ten languages.

Order of every tuple: de, es, es-MX, fr, it, ja, ko, nl, pt-BR, zh-Hans.

Kippu's policy has one thing the other apps' do not: iCloud. Progress is kept in the reader's
own private CloudKit database, which Apple holds and the developer cannot read, and every
language says exactly that, with no hedge that would turn "cannot" into "does not normally".
"""

KEEP = {"Kippu", "lf.wtf", "L@LF.WTF", "Apple", "App Store", "iPhone", "iPad", "iCloud",
        "In-App Purchase", "Kippu Plus"}

T = {
    "Kippu Privacy Policy": (
        "Kippu Datenschutzerklärung",
        "Política de privacidad de Kippu",
        "Política de privacidad de Kippu",
        "Politique de confidentialité de Kippu",
        "Informativa sulla privacy di Kippu",
        "Kippu プライバシーポリシー",
        "Kippu 개인정보 처리방침",
        "Privacybeleid van Kippu",
        "Política de privacidade do Kippu",
        "Kippu 隐私政策"),

    "Kippu collects nothing. There is no account, no analytics and no advertising. Your progress stays on your device and, if you use iCloud, in your own private iCloud database, which Apple holds and the developer cannot read.": (
        "Kippu erfasst nichts. Es gibt kein Konto, keine Analyse und keine Werbung. Dein Fortschritt bleibt auf deinem Gerät und, wenn du iCloud nutzt, in deiner eigenen privaten iCloud-Datenbank, die Apple verwahrt und die der Entwickler nicht lesen kann.",
        "Kippu no recopila nada. No hay cuenta, ni analítica, ni publicidad. Tu progreso se queda en tu dispositivo y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que el desarrollador no puede leer.",
        "Kippu no recopila nada. No hay cuenta, ni analítica, ni publicidad. Tu progreso se queda en tu dispositivo y, si usas iCloud, en tu propia base de datos privada de iCloud, que guarda Apple y que el desarrollador no puede leer.",
        "Kippu ne collecte rien. Pas de compte, pas d'analyse d'audience, pas de publicité. Votre progression reste sur votre appareil et, si vous utilisez iCloud, dans votre propre base de données iCloud privée, qu'Apple héberge et que le développeur ne peut pas lire.",
        "Kippu non raccoglie nulla. Nessun account, nessuna analisi, nessuna pubblicità. I tuoi progressi restano sul tuo dispositivo e, se usi iCloud, nel tuo database iCloud privato, che Apple custodisce e che lo sviluppatore non può leggere.",
        "Kippu は何も収集しません。アカウントも、解析も、広告もありません。学習の進み具合はお使いの端末に保存され、iCloud を使っている場合はあなた自身のプライベートな iCloud データベースにも保存されます。それは Apple が保管し、開発者には読めません。",
        "Kippu는 아무것도 수집하지 않습니다. 계정도, 분석도, 광고도 없습니다. 진행 상황은 기기에 남고, iCloud를 쓰면 본인의 비공개 iCloud 데이터베이스에도 저장됩니다. 그 데이터베이스는 Apple이 보관하며 개발자는 읽을 수 없습니다.",
        "Kippu verzamelt niets. Geen account, geen analytics, geen advertenties. Je voortgang blijft op je apparaat en, als je iCloud gebruikt, in je eigen privé-iCloud-database, die Apple bewaart en die de ontwikkelaar niet kan lezen.",
        "O Kippu não coleta nada. Não há conta, nem análise, nem publicidade. Seu progresso fica no seu aparelho e, se você usa o iCloud, no seu próprio banco de dados privado do iCloud, que a Apple guarda e que o desenvolvedor não consegue ler.",
        "Kippu 不收集任何数据。没有账户，没有分析，没有广告。你的学习进度保存在你的设备上；如果你使用 iCloud，也会保存在你自己的私有 iCloud 数据库中，由 Apple 保管，开发者无法读取。"),

    "Privacy policy": (
        "Datenschutzerklärung", "Política de privacidad", "Política de privacidad",
        "Politique de confidentialité", "Informativa sulla privacy", "プライバシーポリシー",
        "개인정보 처리방침", "Privacybeleid", "Política de privacidade", "隐私政策"),

    "Last updated 21 September 2026": (
        "Zuletzt aktualisiert am 21. September 2026", "Última actualización: 21 de septiembre de 2026",
        "Última actualización: 21 de septiembre de 2026", "Dernière mise à jour le 21 septembre 2026",
        "Ultimo aggiornamento: 21 settembre 2026", "最終更新日：2026年9月21日", "최종 업데이트: 2026년 9월 21일",
        "Laatst bijgewerkt op 21 september 2026", "Última atualização: 21 de setembro de 2026", "最后更新：2026年9月21日"),

    "Kippu does not collect any data.": (
        "Kippu erfasst keinerlei Daten.", "Kippu no recopila ningún dato.", "Kippu no recopila ningún dato.",
        "Kippu ne collecte aucune donnée.", "Kippu non raccoglie alcun dato.", "Kippu はいかなるデータも収集しません。",
        "Kippu는 어떤 데이터도 수집하지 않습니다.", "Kippu verzamelt geen enkele gegevens.",
        "O Kippu não coleta nenhum dado.", "Kippu 不收集任何数据。"),

    "There is no account to create, no analytics, no advertising, no tracking, and no third-party code of any kind in the app. This is not a policy about how carefully your information is handled. There is no information on this side to handle.": (
        "Es gibt kein Konto anzulegen, keine Analyse, keine Werbung, kein Tracking und keinerlei Code von Dritten in der App. Dies ist keine Erklärung darüber, wie sorgfältig mit deinen Informationen umgegangen wird. Auf dieser Seite gibt es keine Informationen, mit denen umzugehen wäre.",
        "No hay ninguna cuenta que crear, ni analítica, ni publicidad, ni rastreo, ni código de terceros de ningún tipo en la aplicación. Esto no es una política sobre el cuidado con el que se maneja tu información. De este lado no hay información que manejar.",
        "No hay ninguna cuenta que crear, ni analítica, ni publicidad, ni rastreo, ni código de terceros de ningún tipo en la aplicación. Esto no es una política sobre el cuidado con el que se maneja tu información. De este lado no hay información que manejar.",
        "Il n'y a aucun compte à créer, pas d'analyse d'audience, pas de publicité, pas de pistage, et aucun code tiers d'aucune sorte dans l'application. Ce n'est pas une politique sur le soin apporté à vos informations. De ce côté-ci, il n'y a aucune information à traiter.",
        "Non c'è nessun account da creare, nessuna analisi, nessuna pubblicità, nessun tracciamento e nessun codice di terze parti di alcun tipo nell'app. Questa non è un'informativa su quanta cura si presta alle tue informazioni. Da questa parte non c'è alcuna informazione da trattare.",
        "作成するアカウントはなく、解析も、広告も、トラッキングも、第三者のコードも一切アプリに含まれていません。これは、あなたの情報をどれだけ慎重に扱うかについての方針ではありません。こちら側には扱う情報そのものがありません。",
        "만들 계정도 없고, 분석도, 광고도, 추적도, 어떤 종류의 제3자 코드도 앱에 없습니다. 이 문서는 당신의 정보를 얼마나 조심스럽게 다루는지에 관한 방침이 아닙니다. 이쪽에는 다룰 정보 자체가 없습니다.",
        "Er is geen account om aan te maken, geen analytics, geen advertenties, geen tracking en geen enkele code van derden in de app. Dit is geen beleid over hoe zorgvuldig er met je gegevens wordt omgegaan. Aan deze kant zijn er geen gegevens om mee om te gaan.",
        "Não há conta para criar, nem análise, nem publicidade, nem rastreamento, nem código de terceiros de qualquer tipo no app. Isto não é uma política sobre o cuidado com que suas informações são tratadas. Deste lado não há informação nenhuma para tratar.",
        "没有需要创建的账户，没有分析，没有广告，没有追踪，应用中也没有任何第三方代码。这不是一份关于如何谨慎处理你信息的政策。这一边根本没有信息可处理。"),

    "What leaves your device": (
        "Was dein Gerät verlässt", "Qué sale de tu dispositivo", "Qué sale de tu dispositivo",
        "Ce qui quitte votre appareil", "Cosa lascia il tuo dispositivo", "端末の外に出るもの",
        "기기 밖으로 나가는 것", "Wat je apparaat verlaat", "O que sai do seu aparelho", "什么会离开你的设备"),

    "Nothing that reaches me.": (
        "Nichts, das mich erreicht.", "Nada que me llegue a mí.", "Nada que me llegue a mí.",
        "Rien qui me parvienne.", "Niente che arrivi a me.", "私に届くものは何もありません。",
        "제게 닿는 것은 아무것도 없습니다.", "Niets dat bij mij terechtkomt.", "Nada que chegue até mim.", "没有任何东西会到我这里。"),

    "The app has no server. The only network traffic it makes is with Apple: syncing your progress to your own iCloud account if you have one, and checking your purchase with the App Store. Every lesson, every recording and every game is inside the app, so it works exactly the same with the phone in airplane mode.": (
        "Die App hat keinen Server. Der einzige Netzwerkverkehr läuft mit Apple: der Abgleich deines Fortschritts mit deinem eigenen iCloud-Konto, falls du eines hast, und die Prüfung deines Kaufs beim App Store. Jede Lektion, jede Aufnahme und jedes Spiel steckt in der App, sie funktioniert im Flugmodus also genau gleich.",
        "La aplicación no tiene servidor. El único tráfico de red que genera es con Apple: sincronizar tu progreso con tu propia cuenta de iCloud si tienes una, y comprobar tu compra con el App Store. Cada lección, cada grabación y cada juego están dentro de la aplicación, así que funciona exactamente igual con el teléfono en modo avión.",
        "La aplicación no tiene servidor. El único tráfico de red que genera es con Apple: sincronizar tu progreso con tu propia cuenta de iCloud si tienes una, y comprobar tu compra con el App Store. Cada lección, cada grabación y cada juego están dentro de la aplicación, así que funciona exactamente igual con el teléfono en modo avión.",
        "L'application n'a pas de serveur. Le seul trafic réseau qu'elle génère se fait avec Apple : la synchronisation de votre progression avec votre propre compte iCloud si vous en avez un, et la vérification de votre achat auprès de l'App Store. Chaque leçon, chaque enregistrement et chaque jeu sont dans l'application, elle fonctionne donc exactement pareil en mode avion.",
        "L'app non ha un server. L'unico traffico di rete che genera è con Apple: la sincronizzazione dei tuoi progressi con il tuo account iCloud, se ne hai uno, e la verifica del tuo acquisto con l'App Store. Ogni lezione, ogni registrazione e ogni gioco sono dentro l'app, quindi funziona esattamente allo stesso modo con il telefono in modalità aereo.",
        "このアプリにサーバーはありません。通信を行う相手は Apple だけです。iCloud アカウントをお持ちならそこへの進み具合の同期、そして App Store での購入確認です。すべてのレッスン、すべての音声、すべてのゲームはアプリの中にあるので、機内モードでもまったく同じように動きます。",
        "이 앱에는 서버가 없습니다. 네트워크 통신 상대는 Apple뿐입니다. iCloud 계정이 있다면 그곳으로 진행 상황을 동기화하고, App Store에서 구매를 확인하는 것이 전부입니다. 모든 수업, 모든 녹음, 모든 게임이 앱 안에 있어서 비행기 모드에서도 똑같이 동작합니다.",
        "De app heeft geen server. Het enige netwerkverkeer is met Apple: je voortgang synchroniseren met je eigen iCloud-account als je er een hebt, en je aankoop controleren bij de App Store. Elke les, elke opname en elk spel zit in de app, dus hij werkt precies hetzelfde met de telefoon in vliegtuigmodus.",
        "O app não tem servidor. O único tráfego de rede que ele faz é com a Apple: sincronizar seu progresso com a sua própria conta do iCloud, se você tiver uma, e conferir sua compra com a App Store. Cada lição, cada gravação e cada jogo estão dentro do app, então ele funciona exatamente igual com o celular em modo avião.",
        "这个应用没有服务器。它唯一的网络通信对象是 Apple：如果你有 iCloud 账户，就把进度同步到你自己的账户；以及向 App Store 核对你的购买。每一课、每一段录音、每一个游戏都在应用里，所以手机开飞行模式时它也完全一样地运行。"),

    "Your progress, and where it lives": (
        "Dein Fortschritt, und wo er liegt", "Tu progreso, y dónde vive", "Tu progreso, y dónde vive",
        "Votre progression, et où elle se trouve", "I tuoi progressi, e dove stanno", "学習の進み具合と、その保存先",
        "진행 상황, 그리고 그것이 있는 곳", "Je voortgang, en waar die staat", "Seu progresso, e onde ele fica", "你的进度，以及它存在哪里"),

    "Which lessons you have done, what you answered, your streak, your level, your game scores, the path you chose, your trip date if you set one, and your settings are stored on the device. If your device is signed in to iCloud, the same records are kept in": (
        "Welche Lektionen du gemacht hast, was du geantwortet hast, deine Serie, dein Level, deine Spielergebnisse, der gewählte Pfad, dein Reisedatum, falls du eines gesetzt hast, und deine Einstellungen werden auf dem Gerät gespeichert. Ist dein Gerät bei iCloud angemeldet, liegen dieselben Einträge in",
        "Qué lecciones has hecho, qué respondiste, tu racha, tu nivel, tus puntuaciones en los juegos, la ruta que elegiste, la fecha de tu viaje si la pusiste y tus ajustes se guardan en el dispositivo. Si tu dispositivo tiene sesión iniciada en iCloud, los mismos registros se guardan en",
        "Qué lecciones has hecho, qué respondiste, tu racha, tu nivel, tus puntuaciones en los juegos, la ruta que elegiste, la fecha de tu viaje si la pusiste y tus ajustes se guardan en el dispositivo. Si tu dispositivo tiene sesión iniciada en iCloud, los mismos registros se guardan en",
        "Les leçons que vous avez faites, vos réponses, votre série, votre niveau, vos scores aux jeux, le parcours choisi, votre date de voyage si vous en avez fixé une, et vos réglages sont stockés sur l'appareil. Si votre appareil est connecté à iCloud, les mêmes enregistrements sont conservés dans",
        "Quali lezioni hai fatto, cosa hai risposto, la tua serie, il tuo livello, i punteggi dei giochi, il percorso che hai scelto, la data del viaggio se l'hai impostata e le tue impostazioni sono salvati sul dispositivo. Se il dispositivo ha effettuato l'accesso a iCloud, gli stessi dati sono conservati nel",
        "どのレッスンを終えたか、何と答えたか、連続記録、レベル、ゲームのスコア、選んだコース、設定していれば旅行の日付、そして各種設定は、端末に保存されます。端末が iCloud にサインインしていれば、同じ記録は",
        "어떤 수업을 마쳤는지, 무엇이라고 답했는지, 연속 기록, 레벨, 게임 점수, 고른 코스, 설정했다면 여행 날짜, 그리고 설정값은 기기에 저장됩니다. 기기가 iCloud에 로그인되어 있으면 같은 기록이",
        "Welke lessen je hebt gedaan, wat je hebt geantwoord, je reeks, je level, je spelscores, het pad dat je koos, je reisdatum als je die hebt ingesteld en je instellingen worden op het apparaat opgeslagen. Als je apparaat is ingelogd bij iCloud, staan dezelfde gegevens ook in",
        "Quais lições você fez, o que respondeu, sua sequência, seu nível, suas pontuações nos jogos, a trilha que escolheu, a data da viagem se você a definiu e seus ajustes ficam guardados no aparelho. Se o aparelho estiver conectado ao iCloud, os mesmos registros ficam no",
        "你完成了哪些课、答了什么、连续打卡、等级、游戏分数、选的路线、设置过的旅行日期，以及各项设置，都保存在设备上。如果设备已登录 iCloud，同样的记录也会保存在"),

    "your own private iCloud database": (
        "deiner eigenen privaten iCloud-Datenbank", "tu propia base de datos privada de iCloud",
        "tu propia base de datos privada de iCloud", "votre propre base de données iCloud privée",
        "tuo database iCloud privato", "あなた自身のプライベートな iCloud データベース",
        "본인의 비공개 iCloud 데이터베이스", "je eigen privé-iCloud-database",
        "seu próprio banco de dados privado do iCloud", "你自己的私有 iCloud 数据库"),

    ", so a second iPhone or an iPad picks up where you left off. That database belongs to your Apple account.": (
        ", damit ein zweites iPhone oder ein iPad dort weitermacht, wo du aufgehört hast. Diese Datenbank gehört zu deinem Apple-Konto.",
        ", para que un segundo iPhone o un iPad continúe donde lo dejaste. Esa base de datos pertenece a tu cuenta de Apple.",
        ", para que un segundo iPhone o un iPad continúe donde lo dejaste. Esa base de datos pertenece a tu cuenta de Apple.",
        ", pour qu'un second iPhone ou un iPad reprenne là où vous vous êtes arrêté. Cette base de données appartient à votre compte Apple.",
        ", così un secondo iPhone o un iPad riprende da dove avevi lasciato. Quel database appartiene al tuo account Apple.",
        "にも保存され、2台目の iPhone や iPad が続きから始められます。そのデータベースはあなたの Apple アカウントのものです。",
        "에도 보관되어 두 번째 iPhone이나 iPad가 이어서 시작할 수 있습니다. 그 데이터베이스는 당신의 Apple 계정에 속합니다.",
        ", zodat een tweede iPhone of een iPad verdergaat waar je gebleven was. Die database hoort bij je Apple-account.",
        ", para que um segundo iPhone ou um iPad continue de onde você parou. Esse banco de dados pertence à sua conta Apple.",
        "，这样第二台 iPhone 或 iPad 可以从你停下的地方继续。那个数据库属于你的 Apple 账户。"),

    "Apple holds it, and I have no way to read it.": (
        "Apple verwahrt sie, und ich habe keine Möglichkeit, sie zu lesen.",
        "La guarda Apple, y yo no tengo forma de leerla.", "La guarda Apple, y yo no tengo forma de leerla.",
        "Apple l'héberge, et je n'ai aucun moyen de la lire.", "La custodisce Apple, e io non ho modo di leggerlo.",
        "それを保管しているのは Apple で、私には読む手段がありません。", "Apple이 보관하며, 저는 읽을 방법이 없습니다.",
        "Apple bewaart hem, en ik kan hem op geen enkele manier lezen.", "A Apple o guarda, e eu não tenho como lê-lo.",
        "它由 Apple 保管，我没有任何办法读取。"),

    "Turning off iCloud for Kippu in Settings stops the syncing; deleting the app and its iCloud data removes everything.": (
        "Wenn du iCloud für Kippu in den Einstellungen ausschaltest, endet der Abgleich; das Löschen der App und ihrer iCloud-Daten entfernt alles.",
        "Desactivar iCloud para Kippu en Ajustes detiene la sincronización; borrar la aplicación y sus datos de iCloud elimina todo.",
        "Desactivar iCloud para Kippu en Configuración detiene la sincronización; borrar la aplicación y sus datos de iCloud elimina todo.",
        "Désactiver iCloud pour Kippu dans les Réglages arrête la synchronisation ; supprimer l'application et ses données iCloud efface tout.",
        "Disattivare iCloud per Kippu nelle Impostazioni ferma la sincronizzazione; eliminare l'app e i suoi dati iCloud rimuove tutto.",
        "設定で Kippu の iCloud をオフにすると同期は止まります。アプリとその iCloud データを削除すれば、すべてが消えます。",
        "설정에서 Kippu의 iCloud를 끄면 동기화가 멈춥니다. 앱과 iCloud 데이터를 삭제하면 모든 것이 지워집니다.",
        "iCloud voor Kippu uitzetten in Instellingen stopt het synchroniseren; de app en zijn iCloud-gegevens verwijderen wist alles.",
        "Desligar o iCloud para o Kippu nos Ajustes interrompe a sincronização; apagar o app e seus dados do iCloud remove tudo.",
        "在设置里关闭 Kippu 的 iCloud 就会停止同步；删除应用及其 iCloud 数据就会清除一切。"),

    "The evening reminder": (
        "Die abendliche Erinnerung", "El recordatorio nocturno", "El recordatorio nocturno",
        "Le rappel du soir", "Il promemoria serale", "夜のリマインダー", "저녁 알림",
        "De avondherinnering", "O lembrete noturno", "晚间提醒"),

    "If you turn on the reminder, the app schedules a notification on the device itself for the time you chose.": (
        "Wenn du die Erinnerung einschaltest, plant die App eine Mitteilung auf dem Gerät selbst für die gewählte Uhrzeit.",
        "Si activas el recordatorio, la aplicación programa una notificación en el propio dispositivo para la hora que elegiste.",
        "Si activas el recordatorio, la aplicación programa una notificación en el propio dispositivo para la hora que elegiste.",
        "Si vous activez le rappel, l'application programme une notification sur l'appareil lui-même à l'heure que vous avez choisie.",
        "Se attivi il promemoria, l'app programma una notifica sul dispositivo stesso per l'ora che hai scelto.",
        "リマインダーをオンにすると、アプリは選んだ時刻の通知を端末そのものに登録します。",
        "알림을 켜면 앱은 당신이 고른 시각에 맞춰 기기 자체에 알림을 예약합니다.",
        "Als je de herinnering aanzet, plant de app een melding op het apparaat zelf voor de tijd die je koos.",
        "Se você ativar o lembrete, o app agenda uma notificação no próprio aparelho para a hora que você escolheu.",
        "如果你打开提醒，应用会在设备本身上按你选的时间安排一条通知。"),

    "It is a local notification: nothing is sent to a server, and no one knows whether you opened it.": (
        "Es ist eine lokale Mitteilung: Nichts wird an einen Server gesendet, und niemand erfährt, ob du sie geöffnet hast.",
        "Es una notificación local: no se envía nada a ningún servidor, y nadie sabe si la abriste.",
        "Es una notificación local: no se envía nada a ningún servidor, y nadie sabe si la abriste.",
        "C'est une notification locale : rien n'est envoyé à un serveur, et personne ne sait si vous l'avez ouverte.",
        "È una notifica locale: niente viene inviato a un server, e nessuno sa se l'hai aperta.",
        "これはローカル通知です。サーバーには何も送られず、あなたが開いたかどうかは誰にもわかりません。",
        "이것은 로컬 알림입니다. 서버로 보내는 것은 없고, 당신이 열었는지는 아무도 모릅니다.",
        "Het is een lokale melding: er wordt niets naar een server gestuurd, en niemand weet of je hem hebt geopend.",
        "É uma notificação local: nada é enviado a um servidor, e ninguém sabe se você a abriu.",
        "这是本地通知：不会向任何服务器发送任何东西，也没有人知道你是否打开了它。"),

    "Turning it off in the app or in Settings removes it.": (
        "Schaltest du sie in der App oder in den Einstellungen aus, ist sie weg.",
        "Desactivarla en la aplicación o en Ajustes la elimina.", "Desactivarla en la aplicación o en Configuración la elimina.",
        "La désactiver dans l'application ou dans les Réglages la supprime.", "Disattivarlo nell'app o nelle Impostazioni lo rimuove.",
        "アプリ内または設定でオフにすれば、通知はなくなります。", "앱이나 설정에서 끄면 사라집니다.",
        "Uitzetten in de app of in Instellingen verwijdert hem.", "Desativá-lo no app ou nos Ajustes o remove.",
        "在应用里或设置里关闭它，它就会被移除。"),

    "Purchases": (
        "Käufe", "Compras", "Compras", "Achats", "Acquisti", "購入", "구매", "Aankopen", "Compras", "购买"),

    "Kippu Plus is sold through Apple's In-App Purchase system as a subscription. Apple takes the payment, manages the free week and the renewals, and tells the app whether the subscription is active.": (
        "Kippu Plus wird über Apples In-App-Kauf-System als Abonnement verkauft. Apple nimmt die Zahlung entgegen, verwaltet die kostenlose Woche und die Verlängerungen und teilt der App mit, ob das Abonnement aktiv ist.",
        "Kippu Plus se vende a través del sistema de compras dentro de la aplicación de Apple como suscripción. Apple cobra el pago, gestiona la semana gratuita y las renovaciones, y le dice a la aplicación si la suscripción está activa.",
        "Kippu Plus se vende a través del sistema de compras dentro de la aplicación de Apple como suscripción. Apple cobra el pago, gestiona la semana gratuita y las renovaciones, y le dice a la aplicación si la suscripción está activa.",
        "Kippu Plus est vendu via le système d'achats intégrés d'Apple sous forme d'abonnement. Apple encaisse le paiement, gère la semaine gratuite et les renouvellements, et indique à l'application si l'abonnement est actif.",
        "Kippu Plus è venduto tramite il sistema di acquisti in-app di Apple come abbonamento. Apple incassa il pagamento, gestisce la settimana gratuita e i rinnovi, e dice all'app se l'abbonamento è attivo.",
        "Kippu Plus は Apple のアプリ内課金の仕組みを通じて、サブスクリプションとして販売されます。支払いを受け取り、無料の1週間と更新を管理し、サブスクリプションが有効かどうかをアプリに伝えるのは Apple です。",
        "Kippu Plus는 Apple의 앱 내 구입 시스템을 통해 구독으로 판매됩니다. 결제를 받고, 무료 일주일과 갱신을 관리하고, 구독이 유효한지 앱에 알려주는 것은 Apple입니다.",
        "Kippu Plus wordt verkocht via Apples systeem voor in-app-aankopen, als abonnement. Apple neemt de betaling aan, beheert de gratis week en de verlengingen, en vertelt de app of het abonnement actief is.",
        "O Kippu Plus é vendido pelo sistema de compras dentro do app da Apple, como assinatura. A Apple recebe o pagamento, administra a semana grátis e as renovações, e informa ao app se a assinatura está ativa.",
        "Kippu Plus 通过 Apple 的应用内购买系统以订阅方式出售。Apple 负责收款、管理免费的一周和续订，并告知应用订阅是否有效。"),

    "Your payment details, your name and your email address are never seen on this side.": (
        "Deine Zahlungsdaten, dein Name und deine E-Mail-Adresse sind auf dieser Seite nie zu sehen.",
        "Tus datos de pago, tu nombre y tu correo electrónico nunca se ven de este lado.",
        "Tus datos de pago, tu nombre y tu correo electrónico nunca se ven de este lado.",
        "Vos données de paiement, votre nom et votre adresse e-mail ne sont jamais visibles de ce côté-ci.",
        "I tuoi dati di pagamento, il tuo nome e il tuo indirizzo email non si vedono mai da questa parte.",
        "あなたの支払い情報、名前、メールアドレスがこちら側に見えることは決してありません。",
        "당신의 결제 정보, 이름, 이메일 주소는 이쪽에서 결코 볼 수 없습니다.",
        "Je betaalgegevens, je naam en je e-mailadres zijn aan deze kant nooit te zien.",
        "Seus dados de pagamento, seu nome e seu e-mail nunca são vistos deste lado.",
        "你的付款信息、姓名和电子邮件地址，这一边从来看不到。"),

    "Restoring a purchase asks Apple, not me, and cancelling is done in your Apple account.": (
        "Das Wiederherstellen eines Kaufs fragt Apple, nicht mich, und gekündigt wird in deinem Apple-Konto.",
        "Restaurar una compra se lo pregunta a Apple, no a mí, y cancelar se hace en tu cuenta de Apple.",
        "Restaurar una compra se lo pregunta a Apple, no a mí, y cancelar se hace en tu cuenta de Apple.",
        "Restaurer un achat interroge Apple, pas moi, et la résiliation se fait dans votre compte Apple.",
        "Il ripristino di un acquisto lo chiede ad Apple, non a me, e la disdetta si fa nel tuo account Apple.",
        "購入の復元は私ではなく Apple に問い合わせ、解約はあなたの Apple アカウントで行います。",
        "구매 복원은 제가 아니라 Apple에 묻고, 해지는 당신의 Apple 계정에서 합니다.",
        "Een aankoop herstellen vraagt het aan Apple, niet aan mij, en opzeggen doe je in je Apple-account.",
        "Restaurar uma compra pergunta à Apple, não a mim, e o cancelamento é feito na sua conta Apple.",
        "恢复购买问的是 Apple，不是我；取消在你的 Apple 账户里进行。"),

    "Children": (
        "Kinder", "Menores", "Menores", "Enfants", "Minori", "お子様について", "어린이", "Kinderen", "Crianças", "儿童"),

    "The app is rated 4+ and is safe for any age, for the plain reason that it collects nothing from anybody. There is no chat, no user content, no links to anywhere except this website and the App Store, and nothing that asks for a name.": (
        "Die App ist ab 4 Jahren freigegeben und für jedes Alter sicher, aus dem einfachen Grund, dass sie von niemandem etwas erfasst. Es gibt keinen Chat, keine Nutzerinhalte, keine Links außer zu dieser Website und zum App Store und nichts, das nach einem Namen fragt.",
        "La aplicación está clasificada para mayores de 4 años y es segura para cualquier edad, por la sencilla razón de que no recopila nada de nadie. No hay chat, ni contenido de usuarios, ni enlaces a ningún sitio salvo esta web y el App Store, ni nada que pida un nombre.",
        "La aplicación está clasificada para mayores de 4 años y es segura para cualquier edad, por la sencilla razón de que no recopila nada de nadie. No hay chat, ni contenido de usuarios, ni enlaces a ningún sitio salvo este sitio web y el App Store, ni nada que pida un nombre.",
        "L'application est classée 4+ et convient à tout âge, pour la simple raison qu'elle ne collecte rien de personne. Pas de chat, pas de contenu d'utilisateurs, aucun lien vers ailleurs que ce site et l'App Store, et rien qui demande un nom.",
        "L'app è classificata 4+ ed è sicura per qualsiasi età, per il semplice motivo che non raccoglie nulla da nessuno. Non c'è chat, nessun contenuto degli utenti, nessun collegamento se non a questo sito e all'App Store, e niente che chieda un nome.",
        "このアプリは 4+ に分類され、誰からも何も収集しないという単純な理由で、どの年齢にも安全です。チャットも、ユーザー投稿も、このサイトと App Store 以外へのリンクも、名前を尋ねるものも、何もありません。",
        "이 앱은 4+ 등급이며, 누구에게서도 아무것도 수집하지 않는다는 단순한 이유로 모든 나이에 안전합니다. 채팅도, 사용자 콘텐츠도, 이 웹사이트와 App Store 외의 링크도, 이름을 묻는 것도 없습니다.",
        "De app heeft een leeftijdsclassificatie van 4+ en is veilig voor elke leeftijd, om de simpele reden dat hij van niemand iets verzamelt. Er is geen chat, geen gebruikersinhoud, geen link naar iets anders dan deze website en de App Store, en niets dat om een naam vraagt.",
        "O app é classificado como 4+ e é seguro para qualquer idade, pela simples razão de que não coleta nada de ninguém. Não há chat, nem conteúdo de usuários, nem links para lugar nenhum além deste site e da App Store, nem nada que peça um nome.",
        "这个应用的分级是 4+，对任何年龄都安全，原因很简单：它不从任何人那里收集任何东西。没有聊天，没有用户内容，除了这个网站和 App Store 之外没有任何链接，也没有任何要你填名字的地方。"),

    "Changes": (
        "Änderungen", "Cambios", "Cambios", "Modifications", "Modifiche", "変更について", "변경", "Wijzigingen", "Alterações", "变更"),

    "If this ever changes, the change will appear here with a new date, and any version of the app that collects something will say so on its App Store page before you install it.": (
        "Sollte sich das jemals ändern, erscheint die Änderung hier mit neuem Datum, und jede Version der App, die etwas erfasst, sagt das auf ihrer App-Store-Seite, bevor du sie installierst.",
        "Si esto cambia alguna vez, el cambio aparecerá aquí con una nueva fecha, y cualquier versión de la aplicación que recopile algo lo dirá en su página del App Store antes de que la instales.",
        "Si esto cambia alguna vez, el cambio aparecerá aquí con una nueva fecha, y cualquier versión de la aplicación que recopile algo lo dirá en su página del App Store antes de que la instales.",
        "Si cela devait changer un jour, la modification apparaîtrait ici avec une nouvelle date, et toute version de l'application qui collecte quelque chose le dirait sur sa page App Store avant que vous ne l'installiez.",
        "Se mai dovesse cambiare, la modifica comparirà qui con una nuova data, e qualsiasi versione dell'app che raccolga qualcosa lo dirà sulla sua pagina dell'App Store prima che tu la installi.",
        "もし変わることがあれば、その変更は新しい日付とともにここに表示され、何かを収集するバージョンのアプリは、インストールする前に App Store のページでそう明記します。",
        "만약 바뀐다면 그 변경은 새 날짜와 함께 여기에 표시되고, 무언가를 수집하는 앱 버전은 설치하기 전에 App Store 페이지에서 그렇게 밝힙니다.",
        "Als dit ooit verandert, verschijnt de wijziging hier met een nieuwe datum, en elke versie van de app die iets verzamelt, zegt dat op zijn App Store-pagina voordat je hem installeert.",
        "Se isso um dia mudar, a mudança aparecerá aqui com uma nova data, e qualquer versão do app que colete algo dirá isso na sua página da App Store antes de você instalar.",
        "如果这一点有朝一日改变，变更会以新的日期出现在这里，任何会收集数据的应用版本都会在你安装之前在它的 App Store 页面上说明。"),

    "Getting in touch": (
        "Kontakt", "Contacto", "Contacto", "Contact", "Contatti", "お問い合わせ", "연락처", "Contact", "Contato", "联系方式"),

    "Questions go to": (
        "Fragen gehen an", "Las preguntas van a", "Las preguntas van a", "Les questions vont à",
        "Le domande vanno a", "質問は", "질문은", "Vragen gaan naar", "Perguntas vão para", "有问题请发到"),

    ", which reaches me directly. An email sent there is an email, and is handled like one: read, replied to, and not fed into anything.": (
        ", das mich direkt erreicht. Eine E-Mail dorthin ist eine E-Mail und wird auch so behandelt: gelesen, beantwortet und in nichts eingespeist.",
        ", que me llega directamente. Un correo enviado ahí es un correo, y se trata como tal: se lee, se responde y no se mete en nada.",
        ", que me llega directamente. Un correo enviado ahí es un correo, y se trata como tal: se lee, se responde y no se mete en nada.",
        ", qui me parvient directement. Un e-mail envoyé là est un e-mail, et traité comme tel : lu, répondu, et versé dans rien.",
        ", che mi arriva direttamente. Un'email inviata lì è un'email, e viene trattata come tale: letta, risposta e non inserita in nulla.",
        "へ。私に直接届きます。そこに送られたメールはメールとして扱われます。読んで、返事をして、他の何かに流し込むことはありません。",
        "으로 보내 주세요. 제게 직접 닿습니다. 그곳으로 보낸 이메일은 이메일로 다뤄집니다. 읽고, 답장하고, 다른 어디에도 넣지 않습니다.",
        ", dat mij rechtstreeks bereikt. Een e-mail daarheen is een e-mail en wordt zo behandeld: gelezen, beantwoord en nergens in gestopt.",
        ", que chega direto a mim. Um e-mail enviado para lá é um e-mail, e é tratado como tal: lido, respondido e não jogado em nada.",
        "，它直接到我这里。发到那里的邮件就是一封邮件，也按邮件处理：阅读、回复，不会被喂进任何系统。"),

    "Built in Fort Worth, Texas": (
        "Gebaut in Fort Worth, Texas", "Hecho en Fort Worth, Texas", "Hecho en Fort Worth, Texas",
        "Conçu à Fort Worth, Texas", "Costruito a Fort Worth, Texas", "テキサス州フォートワースにて制作",
        "텍사스 포트워스에서 만듦", "Gemaakt in Fort Worth, Texas", "Feito em Fort Worth, Texas", "于德克萨斯州沃斯堡制作"),
}

KEEP |= {"Discord"}  # the community server, a name in every language
