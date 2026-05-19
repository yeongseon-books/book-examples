"""Python Dbapi 101 - Episode 4: Parameter binding injection."""

from common import setup_demo_db


def unsafe_lookup(conn, email_input: str):
    """Unsafe lookup."""
    query = f"SELECT id, name FROM users WHERE email = '{email_input}'"
    cur = conn.execute(query)
    return cur.fetchall()


def safe_lookup(conn, email_input: str):
    """Safe lookup."""
    cur = conn.execute("SELECT id, name FROM users WHERE email = ?", (email_input,))
    return cur.fetchall()


def run_demo() -> dict[str, object]:
    """Run demo."""
    conn = setup_demo_db()
    payload = "' OR 1=1 --"
    unsafe_rows = unsafe_lookup(conn, payload)
    safe_rows = safe_lookup(conn, payload)
    conn.close()
    return {"unsafe_count": len(unsafe_rows), "safe_count": len(safe_rows)}


if __name__ == "__main__":
    print(run_demo())
