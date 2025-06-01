# 📘 Proje Adı: Scrabble Oyuncu Derecesi Tahmin Modeli

## 🎯 Proje Amacı:
Bu proje, Kaggle üzerindeki "Scrabble Player Rating" yarışması kapsamında geliştirilmiştir. Amaç, bir Scrabble oyuncusunun yalnızca tek bir maç performansı kullanılarak oyun öncesi derecesini (rating) tahmin etmektir.

## 📦 Veri Seti:
Veri seti Woogles.io platformundan alınan yaklaşık 73.000 oyunu içermektedir. Her oyun iki oyuncunun:
- Skor bilgisi
- Nickname (bot veya insan)
- Rating değeri
- Game ID (eşleşme kimliği)

verilerini içermektedir. Ayrıca hamle düzeyinde ek veri olan `turns.csv` dosyası da bulunmaktadır.

## ⚙️ Kullanılan Yöntem:
- Veri ön işleme (negatif skor temizliği, bot kontrolü)
- Özellik mühendisliği (skor farkı, kazanan durumu, bot karşılaşması)
- Geniş veri formatında oyuncu eşleşmeleri oluşturuldu
- Model olarak `RandomForestRegressor` kullanıldı
- Performans metriği olarak RMSE: **215.77**

## 💡 Model Girdileri (Streamlit için):
- Player 1 Skoru
- Player 2 Skoru
- Player 1 Kazandı mı?
- Rakip Bot mu?

Bu bilgilerle model, `Player 1`'ın tahmini rating'ini üretir.

## 🧪 Örnek Girdi:
```json
{
  "player1_score": 420,
  "player2_score": 390,
  "player1_is_winner": true,
  "player1_vs_bot": false
}



📁 Çıktılar:
model.pkl: Eğitilmiş model

app.py: Streamlit arayüzü

requirements.txt: Gerekli kütüphaneler

sample_input.json: Örnek test girdisi

README.md: GitHub + Hugging Face dokümantasyonu



🚀 Geliştirme Fırsatları:
turns.csv kullanılarak hamle bazlı özellik mühendisliği yapılabilir

Model doğruluğu arttırmak için LightGBM veya XGBoost ile karşılaştırma yapılabilir

Oyunculara özel geçmiş bilgileriyle rating tahmini iyileştirilebilir