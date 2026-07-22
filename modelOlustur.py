import pandas as pd # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import joblib # type: ignore


data = pd.read_csv('spamYorum2str.csv')  


X = data[' İÇERİK']
y = data[' SINIF']


vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)


accuracy = model.score(X_test, y_test)
print(f"Model doğruluğu: {accuracy * 100:.2f}%")


joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
