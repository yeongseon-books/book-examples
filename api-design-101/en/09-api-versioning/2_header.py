# 2_header.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/users/<int:uid>")
def user(uid):
    v = request.headers.get("X-API-Version", "1")
    return jsonify(id=uid, name="Y") if v == "1" else jsonify(id=uid, full_name="Y")
