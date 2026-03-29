from flask import Flask, render_template, request, jsonify
from structural_engine import StructuralAnalyzer
import pickle
import os
import re
import numpy as np

app = Flask(__name__)
analyzer = StructuralAnalyzer()

MODEL_PATH = os.path.expanduser("~/CD_Lab_Project/data/processed/model.pkl")
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

def extract_signal(text):
    # 1. Lexical Signal
    for char in ['@', '$', '`', '#']:
        if char in text:
            return f"stray '{char}' in program"

    # 2. Syntax Signal
    if "return" in text and "0" in text and ";" not in text:
        return "expected ';' before 'return'"

    # 3. Cleaning
    text = re.sub(r'^.*?:\d+:\d+:?\s*', '', text) 
    text = re.sub(r'^(error|warning|note):\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r"'.*?'", "'ID'", text) 
    text = re.sub(r'\d+', 'NUM', text)
    
    return text.strip().lower()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    raw_input = request.form.get('error_message', '').strip()
    if not raw_input:
        return jsonify({'error': 'No input'})

    structural_nodes = analyzer.extract_features(raw_input)
    signal = extract_signal(raw_input)
    
    prediction = model.predict([signal])[0]
    probs = model.predict_proba([signal])[0]
    confidence = np.max(probs) * 100

    if "@" in raw_input:
        prediction = "lexical"
        confidence = 100.0

    return jsonify({
        'category': prediction.upper(),
        'confidence': f"{confidence:.2f}%",
        'structural_nodes': structural_nodes
    })

if __name__ == '__main__':
    print("🚀 WEEK 9 ENGINE ACTIVE: http://127.0.0.1:5001")
    app.run(debug=True, port=5001)
