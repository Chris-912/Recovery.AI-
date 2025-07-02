# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_helper import get_ai_response
import os

app = Flask(__name__)
CORS(app)


@app.route('/check', methods=['POST'])
def check():
    symptoms = request.json.get('symptoms')
    if not symptoms:
        return jsonify({'error': 'No symptoms provided'}), 400
    try:
        result = get_ai_response(symptoms)
        return jsonify({'analysis': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

fetch('http://127.0.0.1:5000/check', { ... })




