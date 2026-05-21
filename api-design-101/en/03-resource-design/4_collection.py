# 4_collection.py
from flask import Flask, jsonify

app = Flask(__name__)

USERS = {42: {"name": "Yeongseon"}}

@app.get("/users")
def list_users(): return jsonify(list(USERS.values()))

@app.get("/users/<int:uid>")
def get_user(uid): return jsonify(USERS[uid])
