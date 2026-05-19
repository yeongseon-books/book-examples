from __future__ import annotations

import sqlite3
import time
from contextlib import contextmanager

from common import create_connection, initialize_schema


def execute_with_retry(conn: sqlite3.Connection, sql: str, params=(), retries: int = 3):
    last_error = None
    for attempt in range(retries):
        try:
            return conn.execute(sql, params)
        except sqlite3.OperationalError as error:
            last_error = error
            if attempt == retries - 1:
                raise
            time.sleep(0.01)
    raise last_error  # pragma: no cover


@contextmanager
def transaction(conn: sqlite3.Connection):
    try:
        conn.execute("BEGIN")
        yield
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def run_demo() -> dict[str, int]:
    conn = create_connection(":memory:")
    initialize_schema(conn)

    with transaction(conn):
        conn.executemany(
            "INSERT INTO users(name, email) VALUES (?, ?)",
            [("R1", "r1@example.com"), ("R2", "r2@example.com"), ("R3", "r3@example.com")],
        )

    execute_with_retry(conn, "SELECT 1")
    count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    conn.close()
    return {"count": count}


if __name__ == "__main__":
    print(run_demo())
