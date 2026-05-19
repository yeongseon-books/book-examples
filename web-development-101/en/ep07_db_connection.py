"""Web Development 101 - Episode 7: Db connection."""

import sqlite3

from flask import Flask, g, jsonify, request


def run(db_path: str):
    """Create Flask app with SQLite CRUD."""
    app = Flask(__name__)
    app.config["DATABASE"] = db_path

    def get_db():
        """Get database connection for current request."""
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DATABASE"])
            g.db.row_factory = sqlite3.Row
            g.db.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"
            )
            g.db.commit()
        return g.db

    @app.teardown_appcontext
    def close_db(exception):
        """Close database connection."""
        db = g.pop("db", None)
        if db is not None:
            db.close()

    @app.route("/users", methods=["GET"])
    def list_users():
        """List all users."""
        db = get_db()
        rows = db.execute("SELECT id, name FROM users").fetchall()
        return jsonify([{"id": row["id"], "name": row["name"]} for row in rows])

    @app.route("/users", methods=["POST"])
    def create_user():
        """Create a new user."""
        db = get_db()
        data = request.get_json()
        cursor = db.execute("INSERT INTO users (name) VALUES (?)", (data["name"],))
        db.commit()
        return jsonify({"id": cursor.lastrowid, "name": data["name"]}), 201

    return app
