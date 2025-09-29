from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # We'll keep this for the POST request

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    # This block will manually handle the OPTIONS preflight request
    if request.method == 'OPTIONS':
        return '', 200

    # This block handles the actual POST request with the calculation
    data = request.get_json()
    if 'expression' not in data:
        return jsonify({'error': 'Expression not provided'}), 400

    expression = data['expression']
    try:
        result = eval(expression)
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'Invalid Expression'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)