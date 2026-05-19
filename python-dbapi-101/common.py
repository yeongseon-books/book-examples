"""Common sqlite3 helpers used by all episodes."""

from __future__ import annotations

import sqlite3
from pathlib import Path

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
"""

SEED_USERS = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
]

SEED_ORDERS = [
    (1, 120.5),
    (2, 80.0),
    (1, 42.75),
]


def create_connection(db_path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)


def seed_data(conn: sqlite3.Connection) -> None:
    conn.executemany("INSERT INTO users(name, email) VALUES (?, ?)", SEED_USERS)
    conn.executemany("INSERT INTO orders(user_id, amount) VALUES (?, ?)", SEED_ORDERS)
    conn.commit()


def setup_demo_db(db_path: str = ":memory:") -> sqlite3.Connection:
    conn = create_connection(db_path)
    initialize_schema(conn)
    seed_data(conn)
    return conn


def file_db_path(tmp_dir: Path, name: str = "demo.db") -> str:
    return str(tmp_dir / name)
