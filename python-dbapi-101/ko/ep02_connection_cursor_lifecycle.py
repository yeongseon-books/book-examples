from common import create_connection, initialize_schema


def run_demo() -> dict[str, object]:
    with create_connection(":memory:") as conn:
        initialize_schema(conn)
        cur = conn.cursor()
        cur.execute("SELECT 1")
        value = cur.fetchone()[0]
        cur.close()
    return {"selected": value, "conn_closed_after_with": conn is not None}


if __name__ == "__main__":
    print(run_demo())
