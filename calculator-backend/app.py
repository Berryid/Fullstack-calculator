# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS to allow the React frontend to make requests
CORS(app)

# Define the /calculate endpoint that accepts POST requests
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if 'expression' not in data:
        return jsonify({'error': 'Expression not provided'}), 400

    expression = data['expression']

    try:
        # WARNING: Using eval() is a security risk in production.
        # It's okay for this personal project, but for a real app,
        # you should use a safer expression parsing library.
        result = eval(expression)
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'Invalid Expression'}), 400

# This allows the script to be run directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)