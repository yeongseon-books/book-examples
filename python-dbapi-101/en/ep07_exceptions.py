import sqlite3

from common import create_connection, initialize_schema


def run_demo() -> dict[str, str]:
    conn = create_connection(":memory:")
    initialize_schema(conn)
    conn.execute("INSERT INTO users(name, email) VALUES (?, ?)", ("A", "a@example.com"))
    conn.commit()

    result = {}

    try:
        conn.execute("INSERT INTO users(name, email) VALUES (?, ?)", ("B", "a@example.com"))
        conn.commit()
    except sqlite3.IntegrityError:
        result["integrity"] = "caught"

    try:
        conn.execute("SELECT * FROM missing_table")
    except sqlite3.OperationalError:
        result["operational"] = "caught"

    try:
        conn.execute("BROKEN SQL")
    except sqlite3.DatabaseError:
        result["database"] = "caught"

    conn.close()
    return result


if __name__ == "__main__":
    print(run_demo())
