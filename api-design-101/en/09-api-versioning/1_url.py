# 1_url.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/v1/users/<int:uid>")
def v1(uid): return jsonify(id=uid, name="Y")

@app.get("/v2/users/<int:uid>")
def v2(uid): return jsonify(id=uid, full_name="Y", username="y")
