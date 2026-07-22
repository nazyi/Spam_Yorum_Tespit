from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Modeli yükleme
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')  # TfidfVectorizer için kaydedilmiş dosya

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    yorum = request.form['yorum']  # HTML formundan gelen veri
    yorum_vec = vectorizer.transform([yorum])
    prediction = model.predict(yorum_vec)
    sonuc = "Spam" if prediction[0] == 1 else "Spam değil"
    return jsonify({'sonuc': sonuc})

if __name__ == '__main__':
    app.run(debug=True)
