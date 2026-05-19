"""Sql 101 - Episode 4: Join."""

from common import seed_db


def run_demo():
    """Run demo."""
    conn = seed_db()
    cur = conn.cursor()

    inner_count = cur.execute(
        "SELECT COUNT(*) FROM employees e INNER JOIN departments d ON e.department_id = d.id"
    ).fetchone()[0]

    left_nulls = cur.execute(
        "SELECT COUNT(*) FROM employees e LEFT JOIN departments d ON e.department_id = d.id WHERE d.id IS NULL"
    ).fetchone()[0]

    right_emulated = cur.execute(
        "SELECT COUNT(*) FROM departments d LEFT JOIN employees e ON e.department_id = d.id"
    ).fetchone()[0]

    cross_sample = cur.execute(
        "SELECT COUNT(*) FROM (SELECT e.id, d.id FROM employees e CROSS JOIN departments d LIMIT 5)"
    ).fetchone()[0]

    self_pairs = cur.execute(
        "SELECT COUNT(*) FROM employees e JOIN employees m ON e.manager_id = m.id"
    ).fetchone()[0]

    conn.close()
    return {
        "inner_count": inner_count,
        "left_nulls": left_nulls,
        "right_emulated": right_emulated,
        "cross_sample": cross_sample,
        "self_pairs": self_pairs,
    }
