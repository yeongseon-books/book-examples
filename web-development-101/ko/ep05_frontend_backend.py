"""Web Development 101 - Episode 5: Frontend backend."""

from flask import Flask, jsonify


def run():
    """Create Flask app demonstrating API contract."""
    app = Flask(__name__)

    @app.route("/api/data")
    def api_data():
        """Return structured API response."""
        return jsonify({"message": "Hello from backend", "version": "1.0.0"})

    return app
