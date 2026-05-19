import sqlite3

import pytest


@pytest.fixture
def in_memory_db():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
    )
    conn.commit()
    try:
        yield conn
    finally:
        conn.close()
