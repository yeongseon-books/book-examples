# resource_operations.py
from flask import Flask, abort, jsonify, request

app = Flask(__name__)

USERS = {
    42: {"id": 42, "name": "Yeongseon", "email": "ys@example.com"},
}
ORDERS = {
    42: [  # user_id -> orders
        {"id": 9, "product": "Clean Code", "status": "shipped"},
        {"id": 10, "product": "DDD", "status": "pending"},
    ]
}


@app.get("/users")
def list_users():
    """Collection: 사용자 목록 반환"""
    return jsonify(list(USERS.values()))


@app.get("/users/<int:uid>")
def get_user(uid):
    """Item: 단일 사용자 반환"""
    if uid not in USERS:
        abort(404)
    return jsonify(USERS[uid])


@app.get("/users/<int:uid>/orders")
def list_user_orders(uid):
    """Sub-collection: 특정 사용자의 주문 목록"""
    if uid not in USERS:
        abort(404)
    return jsonify(ORDERS.get(uid, []))


@app.get("/users/<int:uid>/orders/<int:oid>")
def get_user_order(uid, oid):
    """Sub-item: 특정 사용자의 특정 주문"""
    orders = ORDERS.get(uid, [])
    order = next((o for o in orders if o["id"] == oid), None)
    if order is None:
        abort(404)
    return jsonify(order)
