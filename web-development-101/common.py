"""Shared utilities and domain models for Web Development 101."""

import functools
import hashlib
import json
import os
import sqlite3
import time
from html.parser import HTMLParser
from pathlib import Path

from flask import Flask, g, jsonify, make_response, request, session

ROOT = Path(__file__).parent


def ep01_http_demo():
    """Ep01 http demo."""
    app = Flask(__name__)

    @app.route("/inspect", methods=["GET", "POST"])
    def inspect():
        """Inspect."""
        return jsonify(
            {
                "method": request.method,
                "path": request.path,
                "status": 200,
                "headers": {
                    "Host": request.host,
                    "User-Agent": request.headers.get("User-Agent", ""),
                },
            }
        )

    return app


class MetaValidator(HTMLParser):
    """Meta validator."""

    def __init__(self):
        super().__init__()
        self.h1_count = 0
        self.has_charset = False
        self.has_viewport = False

    def handle_starttag(self, tag, attrs):
        """Handle starttag."""
        attr = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        charset = str(attr.get("charset", "")).lower()
        meta_name = str(attr.get("name", "")).lower()
        if tag == "meta" and charset == "utf-8":
            self.has_charset = True
        if tag == "meta" and meta_name == "viewport":
            self.has_viewport = True


def validate_fixture_html(path: str):
    """Validate fixture html."""
    parser = MetaValidator()
    parser.feed(Path(path).read_text(encoding="utf-8"))
    return {
        "h1_count": parser.h1_count,
        "has_charset": parser.has_charset,
        "has_viewport": parser.has_viewport,
    }


class DOMNode:
    """DOM node."""

    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []


class DOMBuilder(HTMLParser):
    """DOM builder."""

    def __init__(self):
        super().__init__()
        self.root = DOMNode("document", [])
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        """Handle starttag."""
        node = DOMNode(tag, attrs)
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        """Handle endtag."""
        if len(self.stack) > 1:
            self.stack.pop()


def query_by_tag(node, tag):
    """Query by tag."""
    out = []
    for child in node.children:
        if child.tag == tag:
            out.append(child)
        out.extend(query_by_tag(child, tag))
    return out


def query_by_class(node, class_name):
    """Query by class."""
    out = []
    for child in node.children:
        classes = child.attrs.get("class", "").split()
        if class_name in classes:
            out.append(child)
        out.extend(query_by_class(child, class_name))
    return out


def ep04_rest_app():
    """Ep04 rest app."""
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    items: dict[int, dict[str, object]] = {1: {"id": 1, "name": "book"}}

    @app.get("/api/v1/items")
    def get_items():
        """Get items."""
        return jsonify(list(items.values()))

    @app.post("/api/v1/items")
    def create_item():
        """Create item."""
        data = request.get_json(force=True)
        nid = max(items.keys(), default=0) + 1
        item = {"id": nid, "name": data["name"]}
        items[nid] = item
        return jsonify(item), 201

    @app.put("/api/v1/items/<int:item_id>")
    def update_item(item_id):
        """Update item."""
        data = request.get_json(force=True)
        if item_id not in items:
            return jsonify({"error": "not found"}), 404
        items[item_id]["name"] = data["name"]
        return jsonify(items[item_id])

    @app.delete("/api/v1/items/<int:item_id>")
    def delete_item(item_id):
        """Delete item."""
        if item_id not in items:
            return jsonify({"error": "not found"}), 404
        del items[item_id]
        return "", 204

    return app


def ep05_split_app():
    """Ep05 split app."""
    app = Flask(__name__)

    @app.get("/api/data")
    def data():
        """Data."""
        return jsonify({"message": "hello-from-backend", "version": 1})

    return app


def ep06_auth_app():
    """Ep06 auth app."""
    app = Flask(__name__)
    app.secret_key = "dev-secret"
    users = {"alice": hashlib.sha256(b"pw123").hexdigest()}

    @app.post("/login")
    def login():
        """Login."""
        data = request.get_json(force=True)
        digest = hashlib.sha256(data["password"].encode()).hexdigest()
        if users.get(data["username"]) != digest:
            return jsonify({"error": "invalid"}), 401
        session["user"] = data["username"]
        return jsonify({"ok": True})

    @app.post("/logout")
    def logout():
        """Logout."""
        session.clear()
        return jsonify({"ok": True})

    @app.get("/protected")
    def protected():
        """Protected."""
        if "user" not in session:
            return jsonify({"error": "unauthorized"}), 401
        return jsonify({"user": session["user"]})

    return app


def ep07_db_app(db_path):
    """Ep07 db app."""
    app = Flask(__name__)
    app.config["DB_PATH"] = db_path

    def get_db():
        """Get db."""
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DB_PATH"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(_exc):
        """Close db."""
        db = g.pop("db", None)
        if db is not None:
            db.close()

    with app.app_context():
        db = get_db()
        db.execute(
            "create table if not exists users (id integer primary key autoincrement, name text not null)"
        )
        db.commit()

    @app.post("/users")
    def create_user():
        """Create user."""
        data = request.get_json(force=True)
        db = get_db()
        cur = db.execute("insert into users(name) values (?)", (data["name"],))
        db.commit()
        return jsonify({"id": cur.lastrowid, "name": data["name"]}), 201

    @app.get("/users")
    def list_users():
        """List users."""
        rows = get_db().execute("select id, name from users order by id").fetchall()
        return jsonify([{"id": r["id"], "name": r["name"]} for r in rows])

    return app


def ep08_readiness_app():
    """Ep08 readiness app."""
    app = Flask(__name__)

    @app.get("/health")
    def health():
        """Health."""
        return jsonify({"status": "ok", "port": os.getenv("PORT", "not-set")})

    return app


def readiness_check():
    """Readiness check."""
    return {"port_set": bool(os.getenv("PORT")), "ci": os.getenv("CI") == "true"}


def gunicorn_fixture_text():
    """Gunicorn fixture text."""
    return "bind = '0.0.0.0:8000'\nworkers = 2\n"


def lru_cache(maxsize=8):
    """Lru cache."""
    return functools.lru_cache(maxsize=maxsize)


@lru_cache(maxsize=4)
def slow_square(x):
    """Slow square."""
    time.sleep(0.01)
    return x * x


def ep09_etag_app():
    """Ep09 etag app."""
    app = Flask(__name__)
    payload = {"name": "cache-demo", "version": 1}
    body = json.dumps(payload, sort_keys=True)
    etag = hashlib.md5(body.encode()).hexdigest()

    @app.get("/resource")
    def resource():
        """Resource."""
        if request.headers.get("If-None-Match") == etag:
            resp = make_response("", 304)
            resp.headers["ETag"] = etag
            return resp
        resp = jsonify(payload)
        resp.headers["ETag"] = etag
        return resp

    return app


def ep10_todo_app(db_path):
    """Ep10 todo app."""
    app = Flask(__name__)
    app.secret_key = "todo-secret"
    app.config["DB_PATH"] = db_path

    def db():
        """Db."""
        if "db" not in g:
            g.db = sqlite3.connect(app.config["DB_PATH"])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(_exc):
        """Close db."""
        conn = g.pop("db", None)
        if conn is not None:
            conn.close()

    with app.app_context():
        conn = db()
        conn.execute(
            "create table if not exists todos (id integer primary key autoincrement, title text not null, done integer not null default 0)"
        )
        conn.commit()

    @app.post("/login")
    def login():
        """Login."""
        data = request.get_json(force=True)
        if data.get("username") != "alice" or data.get("password") != "pw123":
            return jsonify({"error": "invalid"}), 401
        session["user"] = "alice"
        return jsonify({"ok": True})

    def auth_required():
        """Auth required."""
        return "user" in session

    @app.get("/api/v1/todos")
    def list_todos():
        """List todos."""
        if not auth_required():
            return jsonify({"error": "unauthorized"}), 401
        rows = db().execute("select id, title, done from todos order by id").fetchall()
        return jsonify(
            [
                {"id": r["id"], "title": r["title"], "done": bool(r["done"])}
                for r in rows
            ]
        )

    @app.post("/api/v1/todos")
    def create_todo():
        """Create todo."""
        if not auth_required():
            return jsonify({"error": "unauthorized"}), 401
        data = request.get_json(force=True)
        cur = db().execute(
            "insert into todos(title, done) values (?, ?)", (data["title"], 0)
        )
        db().commit()
        return jsonify(
            {"id": cur.lastrowid, "title": data["title"], "done": False}
        ), 201

    return app
