"""Web Development 101 - Episode 10: Small web app."""

import sqlite3

from flask import Flask, g, jsonify, request, session


def run(db_path: str):
    """Create a todo app with auth and REST API."""
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    users = {"alice": "pw123"}

    def get_db():
        """Get database connection."""
        if "db" not in g:
            g.db = sqlite3.connect(db_path)
            g.db.row_factory = sqlite3.Row
            g.db.execute(
                "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT)"
            )
            g.db.commit()
        return g.db

    @app.teardown_appcontext
    def close_db(exception):
        """Close database."""
        db = g.pop("db", None)
        if db is not None:
            db.close()

    @app.route("/login", methods=["POST"])
    def login():
        """Authenticate user."""
        data = request.get_json()
        if users.get(data.get("username")) == data.get("password"):
            session["user"] = data["username"]
            return jsonify({"status": "ok"})
        return jsonify({"error": "invalid"}), 401

    @app.route("/api/v1/todos", methods=["GET"])
    def list_todos():
        """List todos (requires auth)."""
        if "user" not in session:
            return jsonify({"error": "unauthorized"}), 401
        db = get_db()
        rows = db.execute("SELECT id, title FROM todos").fetchall()
        return jsonify([{"id": r["id"], "title": r["title"]} for r in rows])

    @app.route("/api/v1/todos", methods=["POST"])
    def create_todo():
        """Create todo (requires auth)."""
        if "user" not in session:
            return jsonify({"error": "unauthorized"}), 401
        db = get_db()
        data = request.get_json()
        cursor = db.execute("INSERT INTO todos (title) VALUES (?)", (data["title"],))
        db.commit()
        return jsonify({"id": cursor.lastrowid, "title": data["title"]}), 201

    return app
