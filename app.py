# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample JSON response
    data = {
        "message": "Hello, World!",
        "status": "success",
        "data": {"id": 1, "name": "Sample Item"}
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)  # Use Gunicorn in production
