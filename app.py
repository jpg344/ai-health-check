from flask import Flask, request, jsonify, render_template

import joblib
import numpy as np
from keras.models import load_model

app = Flask(__name__)

#Modell und Scaler laden
model = load_model(r'model\patient_severity_model.h5')
scaler = joblib.load(r'model\scalar_transform.pkl')

#Route für die Startseite
@app.route('/')
def home():
    return render_template('index.html')

#Funktion zur Vorhersage
@app.route('/predict', methods=['POST'])

def predict():
    data = request.json  #Erhalte die Daten als JSON
    vital_values = [
        data ['TEMP'],
        data ['PULSE'],
        data ['RESP'],
        data ['BPSYS'],
        data ['BPDIAS'],
        data ['POPCT']

    ]

    #Daten normalisieren
    scaled_values = scaler.transform([vital_values])

    #Vorhersage durchführen
    prediction = model.predict(scaled_values)

    #Klasse mit der höchsten Wahrscheinlichkeit bestimmen
    predict_class = np.argmax(prediction, axis=1)[0]

    #Vorhersage an die UI zurückgeben
    return jsonify({'Prediction': int(predict_class)})

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5005, debug=True)