from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Zero-Downtime E-Commerce Platform",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop",
            "price": 55000
        },
        {
            "id": 2,
            "name": "Keyboard",
            "price": 1500
        },
        {
            "id": 3,
            "name": "Mouse",
            "price": 800
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
