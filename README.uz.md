[Follow this link for English](README.md)

# Futsuga 🧠✨

**Futsuga** — Telegram botlar yaratish uchun mo‘ljallangan sodda dasturlash tili. U yordamida dasturlashdan yiroq foydalanuvchilar ham kuchli botlar yaratishga qodir.

---

## ✨ Futsuga kimlar uchun?

### Dasturchi bo'lmaganlar uchun
- 💵 Botni ishlab chiqish mutlaqo **bepul**
- ✅ **Sodda tuzilish** — dasturlash tajribasi shart emas
- 📱 **Smartfon**da bot tuzish. **Telegram botimiz, mini-ilovamiz** yoki **veb-saytimizda** bot yarating
- 💸 **Kam obunachili** botingizda ham **reklama**ni yoqib, **pul ishlang**
- 🧠 **No-code / low-code** - Kod yozish shart emas! Faqat **oling** va **qo'ying**. Istasangiz, kod yozing
- 🔐 **Mualliflik himoyasi** (read-only, run-only, imzo, shifrlash)
- 🤖 Bot yozishda **yordam beruvchi** qurilmangizda ~~internet orqali~~ (internetsiz) ishlaydigan sodda va yengil **bot** (kompyuterda). **Telefon** uchun [telegram bot](https://t.me/futsugabot)

### Dasturchilar uchun
- 📚 **GUI + CLI + Veb UI**'ga ega **Paket va loyiha menejeri** orqali **paket** va **loyihalar**ingizni **oson** va **tartibli** boshqaring
- 🛠️ **Python, shell (sodda botlar uchun) va Rust**ga o'giring yoki Rust orqali **kompilyatsiya qiling**
- 📅 **JSON** orqali telegram bot tuzing
- 📝 Fustuga ichida **Python** va **PHP** kodlaridan foydalaning
- 🌍 **O'zbek** va **ingliz** tillaridagi interfeys, ogohlantirish va xatoliklar
- ⛓️‍💥 Oson **debugging**.
- 💻 **GUI + CLI + Veb UI**'ga ega Desktop ilova, paket va loyiha menejeri

---

## Kelajakdagi rejalar
- ⚒️ Bir bosish bilan **deploy**
- 💫 Rust / C++ orqali **yuqori tezlik** va **kamroq resurs sarfi**
- 💵 Pulli, tasdiqlangan, bepul, ochiq **kutubxonalar**

---
## 📜 Litsenziya

Ushbu loyiha **Futsuga License v1.0** ostida litsenziyalangan.

- ✅ Shaxsiy, ta'lim va ichki notijorat, tijorat (futsuga'ning aynan nusxasi bo'lmagan) maqsadlarda foydalanish uchun bepul.
- ❌ Futsuga'ga o'xshash platformalar yaratish uchun foydalanish mumkin emas.

📬 Biznes savollar uchun: kamronbekqochqorov1@gmail.com
---

## Manba havolalar
| Asosiy | O'rganish | Blog |
|---------|----------|------|
| [Veb-sayt](https://futsuga.uz) | [Qo'lanma & kitoblar](https://futsuga.uz/guide) | [Telegram](https://t.me/futsuga) |
| [Yuklab olish](https://futsuga.uz/download) | [Dasturchi bo'lmaganlar uchun](https://futsuga.uz/guide/for-scratch) | [Youtube](https://www.youtube.com/@futsuga) |
| [FSGX paket menejeri](https://futsuga.uz/fsgx) | [Dasturchilar uchun](https://futsuga.uz/guide/for-coders) | [Instagram](https://www.instagram.com) |

[VS Code uchun Extention'lar]()

---

## ⚙️ O'rnatish

### 🐧 Linux (Debian/Ubuntu oilasi uchun)
```bash
sudo apt install futsuga
```

### Boshqa tizimlar
| Tizim | Havola | Video |
|-|-|-|
| Windows | [havola](https://futsuga.uz/download/windows) |[video]() |
| Mac OS | [havola](https://futsuga.uz/download/macos) | [video]() |

### Rasmlar
(None)

---

## 🖼️ Futsuga'dan rasmlar
### Muharrir
- CLI (qurilma terminalidagi interfeys) kodni ishga tushiruvchi
- GUI (foydalanuvchining grafik interfeysi)ga ega IDLE (Integrallashgan o'rganish va dasturlash muhiti)
- Veb UI IDLE (localhost orqali)

### Paket va loyiha menejeri
- CLI (fsgx)
- GUI'ga ega Desktop paket va loyiha menejeri (fsg)
- Veb UI paket menejeri (localhost orqali)

### VS Code uchun Futsuga extention'lari

### Kod yozish jarayoni

### JSON orqali bot yozish

---

## 📦 Futsuga fayl formatlari

| Kengaytma | Turi           | Tavsif                              |
| --------- | -------------- | ----------------------------------- |
| `.futs`    | Manba          | Ochiq matnli skript                 |
| `.luts`    | Kutubxona      | Modul yoki funksiya to‘plami        |
| `.fsgz`   | Shifrlangan    | GZip + shifrlangan versiya          |
| `.fexe`    | Run-only       | Faqat bajarish uchun                |
| `.fsconf` | Konfiguratsiya | Tokenlar, ID’lar, maxfiy sozlamalar |

---

## 🔑 Himoya tizimi (DRM-like)

Futsuga sizga `PDF` fayllardagi kabi mualliflik nazoratini beradi:

- `readonly` – kodni ko‘rish mumkin, lekin o‘zgartirib bo‘lmaydi
- `viewonly` – faqat ko‘rish mumkin, bajarib bo‘lmaydi
- `runonly` – faqat ishlatish mumkin, kod yashirin
- `signed` – RSA imzo bilan himoyalangan fayl

---

## ⚙️ Misol: Oddiy `.futs` fayl

```futsuga
commands:
    /start: "Assalomu alaykum, botga xush kelibsiz!"
```

---

## Takliflar
Agar takliflaringiz bo'lsa, ularni [/invites](/invites) katalogiga *pull request* sifatida .pdf, .docx yoki .txt formatida yo'llashingiz mumkin. Faqat iltimos, fayl nomida til nomi `en` yoki `uz` ko'rinishida bo'lishi ishni osonlashtirgan bo'lar edi. Masalan, invites_1828_uz.docx. Shuningdek, [/Examples](/Examples/) katalogiga ham misol tariqasidagi takliflarni yuborishingiz mumkin.

Tushunganingiz uchun rahmat.

---

## "Futsuga"ning ma'nosi nima?
Ochiq yozaman: hech narsa. Shunchaki, "**Fustuga**" (Boshqa nomlar band ekan).
Ushbu nom Yapon yoki Xitoy tiliga aloqador emas.

---

## Hissa qo'shish
Agar loyiha sizga yoqqan bo'lsa, unga ijtimoiy tarmoqlardagi sahifalarimizga obuna bo'lish va yulduzcha bosish orqali loyiha rivojiga hissa qo'shishingiz mumkin. Ayniqsa, telegram guruhimiz o'zbek va ingliz tillarida faoliyat yuritadi. Ingliz tilidagi ma'lumotni o'qish uchun [telegramdagi ommaviy guruhimiz](https://t.me/futsuga)dagi "(en)" so'zi bor bo'lgan ixtiyoriy mavzuga kiring. Qolganlari o'zbek tilida.