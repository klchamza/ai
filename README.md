# CyberWordAI — Hamza Hack Team

> Siber güvenlik, etik hacking, python ve daha fazlası için geliştirilmiş yapay zeka terminal arayüzü.

🌐 **Canlı Site:** [cyberwordai.netlify.app](https://cyberwordai.netlify.app)

---

## Ne Bu Proje?

Bu proje iki şekilde çalışan, Groq API üzerinden Llama-3.3-70B modelini kullanan bir yapay zeka asistanı. Terminalde de çalışıyor, tarayıcıda da. İkisi de aynı mantıkla çalışıyor, sadece arayüz farklı.

4 tane AI modu var, her biri farklı bir konu için:

| Mod | Ne Yapar |
|---|---|
| 🟢 **CyberWordAI** | Siber güvenlik, etik hacking, ağ güvenliği, penetrasyon testi |
| 🔵 **EnglishWordAI** | İngilizce öğretmeni, dil pratiği, gramer soruları |
| 🟣 **PyWordAI** | Python kodu yazar, hata ayıklar, öğretir |
| 🔴 **ChatWordAI** | Sohbet, şaka, muhabbet, bilmece |

---

## Dosyalar

```
├── cyberwordai.html   → Tarayıcıda çalışan web arayüzü
├── ai.py              → Terminalde çalışan Python versiyonu
└── README.md          → Bu dosya
```

---

## Nasıl Kullanılır?

### Groq API Key Alma

Her iki versiyonda da Groq API key gerekiyor. Ücretsiz alabilirsin:

1. [console.groq.com](https://console.groq.com) adresine gir
2. Hesap aç, API Keys sekmesinden yeni key oluştur
3. Key'i kopyala

---

### Python Versiyonu (ai.py)

**Gereksinim:**
```bash
pip install groq
```

**API key'i ekle:**

`ai.py` dosyasını aç, en üstteki şu satırı bul:
```python
API_KEY = "buraya_kendi_key_ini_yaz"
```
Tırnak işaretleri arasındaki değeri kendi key'inle değiştir.

**Çalıştır:**
```bash
python ai.py
```

Terminalde hangi modla konuşmak istediğini seçiyorsun (1/2/3/4), sonra direkt sorularını yazıyorsun.

---

### Web Versiyonu (cyberwordai.html)

Dosyayı doğrudan tarayıcıda açabilirsin, ya da Netlify, GitHub Pages gibi bir yere deploy edebilirsin.

**API key'i ekle:**

`cyberwordai.html` dosyasını bir editörde aç, `Ctrl+F` ile şunu ara:
```
MODE CONFIG
```

Bu yorum satırının hemen altında şu satırı göreceksin:
```javascript
const API_KEY = 'buraya_kendi_key_ini_yaz';
```
Kendi key'ini buraya yaz, kaydet, bitti.

---

## AI Karakterlerini Özelleştirme

Her modun davranışını değiştirmek istersen yine `Ctrl+F` ile **`MODE CONFIG`** yaz. Hem HTML'de hem de Python'da bu bölümü kolayca bulursun.

**HTML'de** bu şekilde gözükür, her modun `system:` satırı onun kişiliğini belirliyor:

```javascript
const MODES = {
  cyber: {
    system: "Sen CyberWordAI'sın. Hamza Hack Team tarafından geliştirildin...",
    // bu metni değiştirerek AI'ın nasıl davranacağını belirleyebilirsin
  },
  english: {
    system: "...",
  },
  // ...
}
```

**Python'da** her fonksiyonun içindeki `history` listesinin ilk elemanı aynı işi yapıyor:

```python
history = [{"role": "system", "content": "Burası AI'ın kişiliği..."}]
```

İstediğin gibi düzenle, kendi adını koy, konusunu değiştir, tarzını ayarla.

---

## Önemli Not

Groq API key'ini **public bir repoya koyma.** Eğer GitHub'a yükleyeceksen key'i boş bırak ya da `.env` dosyası kullan, key'i oraya yaz ve `.gitignore`'a ekle.

---

## Geliştirici

**klchamza** — Hamza Hack Team  
Model: `llama-3.3-70b-versatile` via [Groq](https://groq.com)
