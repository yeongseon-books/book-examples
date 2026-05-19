"""Web Development 101 - Episode 9: Performance caching."""

import hashlib
from functools import lru_cache

from flask import Flask, jsonify, request


@lru_cache(maxsize=128)
def slow_square(n: int) -> int:
    """Simulate expensive computation with caching."""
    return n * n


def app_factory():
    """Create Flask app with ETag caching."""
    app = Flask(__name__)
    resource_data = {"value": "cached content"}

    @app.route("/resource")
    def resource():
        """Serve resource with ETag support."""
        body = jsonify(resource_data).get_data(as_text=True)
        etag = hashlib.md5(body.encode()).hexdigest()  # noqa: S324
        if request.headers.get("If-None-Match") == etag:
            return "", 304
        resp = jsonify(resource_data)
        resp.headers["ETag"] = etag
        return resp

    return app
