|Line|Turi|Data|
|-|-|-|
|1|{}|@cpp|
|2|begin.init|init {|
|3|begin.ADMINS|ADMINS {|
|4|value|112029910|
|5|value|199020009|
|6|end.1|}|
|7|assign|INLINE: True|
|8|assign|ADMIN_WARNINGS: True|
|9|assign|TELEGRAM_LOG: True|
|10|begin.LOGS|LOGS {|
|11|value|"file.log"|
|12|value|'telegram'|
|13|call_value|ADMINS|
|14|end.2|}}|
|15|begin.imports|imports {|
|16|call_value|futsuga_ads|
|17|call_value|admin_panel|
|18|end.1|}|
|19|begin.InlineButtons|InlineButtons {|
|20|begin.menu_btns|menu_btns {|
|21|assign|link: url="https://t.me/InviProgUz" -> "Salom" /./ xayr: callback_data -> "Xayr"|
|22|assign|copy_button: '639' -> 'Nusxa olish'|
|23|assign|cancel: callback_data -> 'X'|
|24|end.1|}|
|25|begin.channels|channels {|
|26|assign_buttons|CHANNELS -> "$tr-kanal"|
|27|assign_buttons|verify -> "✅ Tasdiqlash ✅"|
|28|end.1|}|
|29|end.1|}|
|30|begin.KeyboardButtons|KeyboardButtons {|
|31|begin.KeyboardButton menu|KeyboardButton menu {|
|32|assign|buyurtma: "Buyurtma" /./ now: "Balans"|
|33|assign|yordam: "Yordam"|
|34|end.1|}|
|35|end.1|}|
|36|begin.commands|commands {|
|37|begin./start|/start {|
|38|do.reply|reply: "Salom, botga xush kelibsiz **$user.first_name**!/.//./1/.//./Siz menga $subcom.1ni yubordingiz."|
|39|begin.python|python {|
|40|unknown|tp, id = $subcom.split('-')|
|41|unknown|return tp, id|
|42|end.1|}|
|43|do.reply|reply: "$tp & $id"|
|44|end.1|}|
|45|assign|/help: "Bot yordamchi buyruqlari: /start, /help: #help"|
|46|begin./menu|/menu {|
|47|begin.reply|reply {|
|48|assign|"Tanlang:",|
|49|assign|buttons: menu|
|50|end.1|}|
|51|assign|set_reaction: "❤️‍🔥"|
|52|end.1|}|
|53|begin./photo|/photo {|
|54|assign|send_photo: "https://example.com/image.jpg"|
|55|end.1|}|
|56|begin./about_bot|/about_bot {|
|57|begin.reply|reply {|
|58|unknown|py.subprocess.getoutput "echo Hello"|
|59|end.1|}|
|60|end.1|}|
|61|end.1|}|
|62|begin.text|text {|
|63|begin.~"Xayr"|~"Xayr" {|
|64|value|"Sizga ham xayr.",|
|65|assign|buttons: menu_btns|
|66|end.1|}|
|67|assign|"Salom": "Va alaykum salom!"|
|68|end.1|}|
|69|begin.admin_panel|admin_panel {|
|70|unknown|pass|
|71|end.1|}|
|72|begin.files|files {|
|73|assign|file: reply: "Siz fayl yubordingiz"|
|74|assign|photo: "Siz rasm yubordingiz"|
|75|assign|document: forward: $this_content|
|76|assign|video: reply: 'Siz video yubordingiz'|
|77|end.1|}|
|78|begin.keyboard_buttons_handler|keyboard_buttons_handler {|
|79|assign|buyurtma: "Buyurtmani tanlash"|
|80|begin.yordam|yordam {|
|81|assign|"Admin manzili:"|
|82|begin.buttons|buttons {|
|83|value|"Admin"|
|84|assign|url: "https://t.me/inviprog"|
|85|end.1|}|
|86|end.1|}|
|87|end.1|}|
|88|begin.inline_buttons_handler|inline_buttons_handler {|
|89|assign|cancel: delete|
|90|assign|salom: "Salom"|
|91|begin.verify|verify {|
|92|assign|is_admin: 'Obuna bo\'lishingiz /* mcn */ shart emas!'|
|93|assign|is_subscriber: "Siz obuna bo'lgansiz"|
|94|begin.if,not is_subscriber|not is_subscriber {|
|95|value|"Iltimos, majburiy kanallarga obuna bo'ling /*abc*/"|
|96|assign|buttons: channels|
|97|end.1|}|
|98|end.1|}|
|99|assign|xayr: show_alert: "Sizga ham xayr"|
|100|end.1|}|
