# singleton_resource.py
from flask import Flask, jsonify

app = Flask(__name__)
USERS = {42: {"name": "Yeongseon", "bio": "Engineer", "avatar": "/img/ys.png"}}


@app.get("/users/<int:uid>/profile")
def get_profile(uid):
    """Singleton: 사용자당 프로필은 하나뿐"""
    user = USERS.get(uid)
    return jsonify({"bio": user["bio"], "avatar": user["avatar"]})
