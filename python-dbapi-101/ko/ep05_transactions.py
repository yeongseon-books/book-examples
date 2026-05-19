"""Python Dbapi 101 - Episode 5: Transactions."""

from common import create_connection, initialize_schema


def run_demo() -> dict[str, object]:
    """Run demo."""
    conn = create_connection(":memory:")
    initialize_schema(conn)

    conn.execute("BEGIN")
    conn.execute(
        "INSERT INTO users(name, email) VALUES (?, ?)", ("TxA", "txa@example.com")
    )
    conn.rollback()

    conn.execute("BEGIN")
    conn.execute(
        "INSERT INTO users(name, email) VALUES (?, ?)", ("TxB", "txb@example.com")
    )
    conn.commit()

    cur = conn.execute("SELECT COUNT(*) FROM users")
    count_after = cur.fetchone()[0]
    isolation = conn.isolation_level
    conn.close()

    return {"count_after": count_after, "isolation_level": isolation}


if __name__ == "__main__":
    print(run_demo())
