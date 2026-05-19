"""Python Dbapi 101 - Episode 3: Fetch patterns."""

from common import setup_demo_db


def run_demo() -> dict[str, object]:
    """Run demo."""
    conn = setup_demo_db()
    cur = conn.cursor()

    cur.execute("SELECT name FROM users ORDER BY id")
    first = cur.fetchone()[0]

    cur.execute("SELECT name FROM users ORDER BY id")
    many = [row[0] for row in cur.fetchmany(2)]

    cur.execute("SELECT name FROM users ORDER BY id")
    all_rows = [row[0] for row in cur.fetchall()]

    cur.executemany(
        "INSERT INTO users(name, email) VALUES (?, ?)",
        [("Dora", "dora@example.com"), ("Eve", "eve@example.com")],
    )
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()
    return {"first": first, "many": many, "all": all_rows, "count": count}


if __name__ == "__main__":
    print(run_demo())
