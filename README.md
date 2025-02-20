# 📱 Instagram Follower Tracker
Üniversiteye yeni mi başladınız ? Ve tüm kızlara istek atmak zor mu geliyor... Ahh evet işte tam işinize yarayacak bir depo.

## 🚀 Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/yourusername/FollowApp.git
cd FollowApp
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun ve Instagram bilgilerinizi ekleyin:
```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

## ⚙️ Yapılandırma

`app/config.py` dosyasında aşağıdaki ayarları özelleştirebilirsiniz:

- `CHECK_USERNAME`: Takip edilecek hesap
- `SCRAPE_COUNT`: Her seferde çekilecek takipçi sayısı
- `DURATION`: İstekler arası bekleme süresi (ms)

## 📂 Proje Yapısı

```
FollowApp/
├── app/
│   ├── core/
│   │   └── instagram_client.py
│   ├── utils/
│   ├── config.py
│   └── __main__.py
├── .env
├── requirements.txt
├── session.json
└── README.md
```

## 🎮 Kullanım

Uygulamayı başlatmak için:

```bash
python -m app
```

## 📝 Çıktı Dosyaları

- `session.json`: Oturum bilgilerini saklar
- `basarili_istekler.txt`: Başarılı takip isteklerinin kaydını tutar
- `isimler.txt`: Takip edilen kullanıcıların listesi

## ⚠️ Güvenlik Notları

- Instagram kimlik bilgilerinizi her zaman `.env` dosyasında saklayın
- `.env` dosyasını asla git reposuna eklemeyin
- Instagram'ın kullanım koşullarına uygun kullanın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
