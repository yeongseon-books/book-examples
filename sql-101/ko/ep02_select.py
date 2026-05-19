from common import seed_db


def run_demo():
    conn = seed_db()
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT id AS emp_id, name AS employee_name, salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 3
        """
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]
