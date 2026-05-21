# 1_offset.py
from flask import Flask, jsonify, request

app = Flask(__name__)
ITEMS = list(range(1000))

@app.get("/items")
def items():
    offset = int(request.args.get("offset", 0))
    limit = min(int(request.args.get("limit", 20)), 100)
    return jsonify(items=ITEMS[offset:offset+limit], total=len(ITEMS))
