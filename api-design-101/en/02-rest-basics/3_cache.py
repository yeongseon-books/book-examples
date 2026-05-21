# 3_cache.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/articles/1")
def article():
    resp = jsonify(id=1, title="REST Basics")
    resp.headers["Cache-Control"] = "public, max-age=60"
    return resp
