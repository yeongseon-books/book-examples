"""Web Development 101 - Episode 6: Auth sessions."""

from flask import Flask, jsonify, request, session


def run():
    """Create Flask app with session-based auth."""
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    users = {"alice": "pw123"}

    @app.route("/login", methods=["POST"])
    def login():
        """Authenticate user and create session."""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if users.get(username) == password:
            session["user"] = username
            return jsonify({"status": "ok"})
        return jsonify({"error": "invalid credentials"}), 401

    @app.route("/logout", methods=["POST"])
    def logout():
        """Clear session."""
        session.clear()
        return jsonify({"status": "ok"})

    @app.route("/protected")
    def protected():
        """Protected endpoint requiring auth."""
        if "user" not in session:
            return jsonify({"error": "unauthorized"}), 401
        return jsonify({"message": f"Hello {session['user']}"})

    return app
