"""Web Development 101 - Episode 1: Http request response."""

from flask import Flask, jsonify, request


def run():
    """Create Flask app that inspects HTTP requests."""
    app = Flask(__name__)

    @app.route("/inspect")
    def inspect():
        """Return request metadata as JSON."""
        return jsonify(
            {
                "method": request.method,
                "path": request.path,
                "status": 200,
                "headers": dict(request.headers),
            }
        )

    return app
