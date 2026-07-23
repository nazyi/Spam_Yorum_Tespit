# Spam Yorum Tespit Sistemi

Makine öğrenmesi tabanlı bu proje, kullanıcı yorumlarını analiz ederek **spam** veya **normal** yorum olarak sınıflandırmayı amaçlamaktadır. Metin ön işleme teknikleri ve doğal dil işleme (NLP) yöntemleri kullanılarak yorumların içeriği analiz edilir ve eğitilmiş model yardımıyla tahmin gerçekleştirilir.

## Projenin Amacı

İnternet üzerindeki kullanıcı yorumlarının artmasıyla birlikte spam içeriklerin tespit edilmesi önemli bir ihtiyaç haline gelmiştir. Bu proje, yorumların otomatik olarak analiz edilmesini sağlayarak spam içeriklerin hızlı ve doğru bir şekilde belirlenmesine yardımcı olur.

## Proje Hakkında

Spam Yorum Tespit Sistemi, kullanıcı yorumlarını doğal dil işleme (NLP) teknikleri ile analiz ederek Spam ya da Spam Değil olarak sınıflandıran bir makine öğrenmesi uygulamasıdır. Metinler TF-IDF ile vektörleştirilir, bir Random Forest sınıflandırıcısı ile eğitilir ve basit bir Flask arayüzü üzerinden gerçek zamanlı tahmin sunulur.

##  Özellikler

📝 Kullanıcının girdiği yorumun anlık olarak analiz edilmesi
🔤 TF-IDF tabanlı metin vektörleştirme
🌲 Random Forest sınıflandırıcı ile spam tahmini
⚡ Flask ile hafif ve hızlı web arayüzü
🔌 JSON tabanlı /predict API uç noktası

## Kurulum

```bash
git clone https://github.com/nazyi/Spam_Yorum_Tespit.git
cd Spam_Yorum_Tespit

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver
```
