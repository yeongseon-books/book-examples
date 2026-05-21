# collection_vs_item.py
from flask import Flask, jsonify

app = Flask(__name__)
BOOKS = {
    "clean-code": {"title": "Clean Code", "author": "Robert C. Martin"},
    "ddd": {"title": "Domain-Driven Design", "author": "Eric Evans"},
}


@app.get("/books")              # Collection: 목록 반환
def list_books():
    return jsonify(list(BOOKS.values()))


@app.get("/books/<slug>")       # Item: 단일 리소스 반환
def get_book(slug):
    return jsonify(BOOKS[slug])
