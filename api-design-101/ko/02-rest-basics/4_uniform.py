# 4_uniform.py
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {1: {"id": 1, "name": "Alice"}, 2: {"id": 2, "name": "Bob"}}

@app.get("/users/<int:uid>")
def get_user(uid):
    """같은 리소스 URI, GET = 조회"""
    if uid not in users:
        return jsonify(error="not_found"), 404
    return jsonify(users[uid])

@app.put("/users/<int:uid>")
def replace_user(uid):
    """같은 리소스 URI, PUT = 전체 교체"""
    users[uid] = request.json
    users[uid]["id"] = uid
    return jsonify(users[uid])

@app.delete("/users/<int:uid>")
def delete_user(uid):
    """같은 리소스 URI, DELETE = 삭제"""
    users.pop(uid, None)
    return "", 204
