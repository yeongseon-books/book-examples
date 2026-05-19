from flask import Flask, jsonify, request


def create_app() -> Flask:
    app = Flask(__name__)

    @app.post("/api/order")
    def create_order():
        data = request.get_json(silent=True) or {}
        item = data.get("item")
        qty = data.get("qty")
        if not item or not isinstance(qty, int) or qty <= 0:
            return jsonify({"ok": False, "error": "invalid request"}), 400
        return jsonify({"ok": True, "order": {"item": item, "qty": qty}}), 201

    return app
