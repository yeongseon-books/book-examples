"""Data Science Career 101 - Episode 5: Sql and analytics interview."""

from __future__ import annotations

import sqlite3
from typing import Any


def build_connection() -> sqlite3.Connection:
    """Build connection."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, country TEXT, signup_date TEXT);
        CREATE TABLE products (id INTEGER PRIMARY KEY, category TEXT, price INTEGER);
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            product_id INTEGER,
            amount INTEGER,
            order_date TEXT
        );
        CREATE TABLE funnel (user_id INTEGER, step TEXT);
        """
    )
    cur.executemany(
        "INSERT INTO users VALUES (?, ?, ?)",
        [
            (1, "KR", "2026-01-01"),
            (2, "KR", "2026-01-02"),
            (3, "US", "2026-01-03"),
        ],
    )
    cur.executemany(
        "INSERT INTO products VALUES (?, ?, ?)",
        [(1, "book", 10), (2, "course", 30), (3, "tool", 20)],
    )
    cur.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
        [
            (1, 1, 1, 10, "2026-02-01"),
            (2, 1, 2, 30, "2026-02-03"),
            (3, 2, 3, 20, "2026-02-04"),
            (4, 3, 2, 30, "2026-02-05"),
        ],
    )
    cur.executemany(
        "INSERT INTO funnel VALUES (?, ?)",
        [
            (1, "visit"),
            (1, "signup"),
            (1, "purchase"),
            (2, "visit"),
            (2, "signup"),
            (3, "visit"),
        ],
    )
    conn.commit()
    return conn


def sql_questions() -> dict[str, str]:
    """Sql questions."""
    return {
        "top_country_by_revenue": """
            SELECT u.country, SUM(o.amount) AS revenue
            FROM orders o JOIN users u ON u.id = o.user_id
            GROUP BY u.country
            ORDER BY revenue DESC, u.country ASC
            LIMIT 1
        """,
        "orders_per_user": "SELECT user_id, COUNT(*) FROM orders GROUP BY user_id ORDER BY user_id",
        "running_revenue": """
            SELECT order_date, SUM(amount) OVER (ORDER BY order_date) AS running_sum
            FROM orders ORDER BY order_date
        """,
        "funnel_counts": """
            WITH steps AS (
              SELECT user_id,
                MAX(CASE WHEN step='visit' THEN 1 ELSE 0 END) AS s1,
                MAX(CASE WHEN step='signup' THEN 1 ELSE 0 END) AS s2,
                MAX(CASE WHEN step='purchase' THEN 1 ELSE 0 END) AS s3
              FROM funnel GROUP BY user_id
            )
            SELECT SUM(s1), SUM(s2), SUM(s3) FROM steps
        """,
        "retention_d1_proxy": """
            SELECT COUNT(DISTINCT o.user_id)
            FROM orders o JOIN users u ON o.user_id = u.id
            WHERE julianday(o.order_date) - julianday(u.signup_date) <= 35
        """,
    }


def run_query(conn: sqlite3.Connection, query: str) -> list[tuple[Any, ...]]:
    """Run query."""
    return conn.execute(query).fetchall()
