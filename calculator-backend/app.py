# 1. Import Libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

# 2. Initialize the App
app = Flask(__name__)

# 3. Set up CORS to allow requests from your live sites
CORS(app, origins=["https://simplecalculatorarithmetic.netlify.app", "http://localhost:3001"])

# 4. Define the API endpoint
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    if 'expression' not in data:
        return jsonify({'error': 'Expression not provided'}), 400

    expression = data['expression']
    try:
        # WARNING: Using eval() is a security risk in production.
        result = eval(expression)
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'Invalid Expression'}), 400

# 5. Run the App
if __name__ == '__main__':
    app.run(debug=True, port=5000)