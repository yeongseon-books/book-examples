"""Portfolio Project 101 - Episode 4: Flask demo."""

from __future__ import annotations

from flask import Flask, jsonify, request


def create_app() -> Flask:
    """Create app."""
    app = Flask(__name__)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        """Health."""
        return {"status": "ok"}, 200

    @app.post("/api/echo")
    def api_echo():
        """Api echo."""
        payload = request.get_json(silent=True) or {}
        return jsonify({"echo": payload}), 200

    return app
