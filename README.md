# Spam Yorum Tespit Sistemi

Makine öğrenmesi tabanlı bu proje, kullanıcı yorumlarını analiz ederek **spam** veya **normal** yorum olarak sınıflandırmayı amaçlamaktadır. Metin ön işleme teknikleri ve doğal dil işleme (NLP) yöntemleri kullanılarak yorumların içeriği analiz edilir ve eğitilmiş model yardımıyla tahmin gerçekleştirilir.

## Projenin Amacı

İnternet üzerindeki kullanıcı yorumlarının artmasıyla birlikte spam içeriklerin tespit edilmesi önemli bir ihtiyaç haline gelmiştir. Bu proje, yorumların otomatik olarak analiz edilmesini sağlayarak spam içeriklerin hızlı ve doğru bir şekilde belirlenmesine yardımcı olur.

## Özellikler

- Kullanıcı yorumlarının analiz edilmesi
- Metin ön işleme (Text Preprocessing)
- Spam / Normal yorum sınıflandırması
- Makine öğrenmesi tabanlı tahmin sistemi
- Kullanıcı dostu arayüz

## Kullanılan Teknolojiler

- Python
- Django
- HTML / CSS
- Scikit-learn
- Pandas
- NumPy
- Natural Language Processing (NLP)

## Çalışma Mantığı

1. Kullanıcı yorumunu sisteme girer.
2. Yorum metni ön işleme adımlarından geçirilir.
3. Eğitilmiş makine öğrenmesi modeli yorumu analiz eder.
4. Sistem yorumun **Spam** veya **Normal** olduğunu tahmin eder.
5. Sonuç kullanıcıya gösterilir.

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
