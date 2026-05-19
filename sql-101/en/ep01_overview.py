from common import seed_db


def run_demo():
    conn = seed_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE demo (id INTEGER PRIMARY KEY, label TEXT)")
    cur.execute("INSERT INTO demo(label) VALUES (?)", ("hello",))
    cur.execute("INSERT INTO demo(label) VALUES (?)", ("sql",))
    rows = cur.execute("SELECT id, label FROM demo ORDER BY id").fetchall()
    conn.close()
    return [dict(r) for r in rows]
