# Spam Yorum Tespit Sistemi

**Spam Yorum Tespit Sistemi**, kullanıcı yorumlarını doğal dil işleme (NLP) teknikleri ile analiz ederek **Spam** ya da **Spam Değil** olarak sınıflandıran bir makine öğrenmesi uygulamasıdır. Metinler TF-IDF ile vektörleştirilir, bir **Random Forest** sınıflandırıcısı ile eğitilir ve basit bir Flask arayüzü üzerinden gerçek zamanlı tahmin sunulur.

## Projenin Amacı

İnternet üzerindeki kullanıcı yorumlarının artmasıyla birlikte spam içeriklerin tespit edilmesi önemli bir ihtiyaç haline gelmiştir. Bu proje, yorumların otomatik olarak analiz edilmesini sağlayarak spam içeriklerin hızlı ve doğru bir şekilde belirlenmesine yardımcı olur.

##  Özellikler

- 📝 Kullanıcının girdiği yorumun anlık olarak analiz edilmesi
- 🔤 TF-IDF tabanlı metin vektörleştirme
- 🌲 Random Forest sınıflandırıcı ile spam tahmini
- ⚡ Flask ile hafif ve hızlı web arayüzü
- 🔌 JSON tabanlı `/predict` API uç noktası

  
## 🗃️ Veri Seti
 
Model, yorum metni ve etiket (`1`: spam, `0`: spam değil) içeren `spamYorum2str.csv` dosyasıyla eğitilmiştir. Veri seti yalnızca eğitim/deneme amaçlıdır.
