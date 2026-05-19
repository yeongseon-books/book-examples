"""Web Development 101 - Episode 8: Deployment."""

import os

from flask import Flask, jsonify


def readiness_check() -> dict:
    """Check deployment readiness."""
    return {"port_set": bool(os.environ.get("PORT"))}


def gunicorn_fixture_text() -> str:
    """Return sample gunicorn config text."""
    return "bind = '0.0.0.0:8000'\nworkers = 4\ntimeout = 120\n"


def app_factory():
    """Create Flask app with health endpoint."""
    app = Flask(__name__)

    @app.route("/health")
    def health():
        """Health check endpoint."""
        return jsonify({"status": "ok", "port": os.environ.get("PORT")})

    return app
