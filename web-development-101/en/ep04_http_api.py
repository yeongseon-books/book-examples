"""Web Development 101 - Episode 4: Http api."""

from flask import Flask, jsonify, request


def run():
    """Create Flask app with REST CRUD endpoints."""
    app = Flask(__name__)
    items: dict[int, dict] = {}
    next_id = [1]

    @app.route("/api/v1/items", methods=["GET"])
    def list_items():
        """List all items."""
        return jsonify(list(items.values()))

    @app.route("/api/v1/items", methods=["POST"])
    def create_item():
        """Create a new item."""
        data = request.get_json()
        item_id = next_id[0]
        next_id[0] += 1
        item = {"id": item_id, "name": data["name"]}
        items[item_id] = item
        return jsonify(item), 201

    @app.route("/api/v1/items/<int:item_id>", methods=["PUT"])
    def update_item(item_id):
        """Update an existing item."""
        data = request.get_json()
        items[item_id]["name"] = data["name"]
        return jsonify(items[item_id])

    @app.route("/api/v1/items/<int:item_id>", methods=["DELETE"])
    def delete_item(item_id):
        """Delete an item."""
        items.pop(item_id, None)
        return "", 204

    return app
