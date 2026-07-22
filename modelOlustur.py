import pandas as pd # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import joblib # type: ignore

# CSV dosyasını yükleme
data = pd.read_csv('spamYorum2str.csv')  # CSV dosyanızın adını girin

# Veri önişleme
X = data[' İÇERİK']
y = data[' SINIF']

# TF-IDF ile metin vektörleştirme
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Eğitim ve test verilerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Modeli eğitme
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Modelin doğruluğunu kontrol etme
accuracy = model.score(X_test, y_test)
print(f"Model doğruluğu: {accuracy * 100:.2f}%")

# Model ve vectorizer'ı kaydetme
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
