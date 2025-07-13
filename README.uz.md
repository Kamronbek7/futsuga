[Follow this link for English](README.md)

# Futsuga 🧠✨

**Futsuga** — bu Telegram botlar yaratish uchun mo‘ljallangan o‘ziga xos (DSL) domen-ga xos dasturlash tili. U dasturlashdan yiroq foydalanuvchilar uchun oddiy va tushunarli sintaksis orqali kuchli botlar yaratishga imkon beradi.

---

## ✨ Nega Futsuga?

- ✅ **Sodda sintaksis** — dasturlash tajribasisiz ham ishlatish mumkin
- 🧠 **No-code / low-code** imkoniyatlari
- 🔐 **Mualliflik himoyasi (read-only, run-only, imzo, shifrlash)**
- 🧩 **Telegram inline va reply tugmalarni** deklarativ e'lon qilish imkoniyati
- 🛠️ **Python yoki Rust backend’ga kompilyatsiya qilish mumkin**
- 🌐 **Web editor (drag & drop UI)** va Desktop uchun IDLE (customTkinter) ishlab chiqilmoqda

---

## 📦 Futsuga fayl formatlari

| Fayl turi | Tavsif |
|----------|--------|
| `.fsg` | Ochiq manba Futsuga script |
| `.fsgz` | GZip qilingan va shifrlangan script |
| `.fcr` | Faqat bajarish uchun mo‘ljallangan (run-only) fayl |
| `.fsconfig` | Maxfiy sozlamalar (TOKEN, ID, permissions) |

---

## 🔑 Himoya tizimi (DRM-like)

Futsuga sizga `PDF` fayllardagi kabi mualliflik nazoratini beradi:

- `readonly` – kodni ko‘rish mumkin, lekin o‘zgartirib bo‘lmaydi
- `viewonly` – faqat ko‘rish mumkin, bajarib bo‘lmaydi
- `runonly` – faqat ishlatish mumkin, kod yashirin
- `signed` – RSA imzo bilan himoyalangan fayl

---

## ⚙️ Misol: Oddiy .fsg fayl

```futsuga
TOKEN $ENV.TOKEN
INLINE=True

InlineButton main:
    "Boshlash" -> callback_data: start
    "Yordam" -> callback_data: help

/start:
    reply "Assalomu alaykum, botga xush kelibsiz!"
```