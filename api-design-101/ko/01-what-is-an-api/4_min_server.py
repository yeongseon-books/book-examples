# 4_min_server.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    """계약: GET /health → 200 + {"status": "ok"}"""
    return jsonify(status="ok")

@app.get("/users")
def list_users():
    """계약: GET /users → 200 + JSON array"""
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    return jsonify(users)

if __name__ == "__main__":
    app.run(port=8000)
