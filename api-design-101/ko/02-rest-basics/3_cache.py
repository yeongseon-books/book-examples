# 3_cache.py
from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.get("/articles/<int:article_id>")
def get_article(article_id):
    article = {"id": article_id, "title": "REST Basics", "author": "Alice"}
    resp = make_response(jsonify(article))
    # 이 응답은 60초간 캐시 가능
    resp.headers["Cache-Control"] = "public, max-age=60"
    resp.headers["ETag"] = f'"{article_id}-v1"'
    return resp

@app.post("/articles")
def create_article():
    # POST 응답은 캐시하지 않음
    resp = make_response(jsonify(id=99, title="New"), 201)
    resp.headers["Cache-Control"] = "no-store"
    return resp
