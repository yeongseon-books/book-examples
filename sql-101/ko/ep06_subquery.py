from common import seed_db


def run_demo():
    conn = seed_db()
    cur = conn.cursor()

    scalar = cur.execute(
        "SELECT name FROM employees WHERE salary = (SELECT MAX(salary) FROM employees)"
    ).fetchone()[0]

    in_subquery = cur.execute(
        """
        SELECT name FROM employees
        WHERE id IN (SELECT employee_id FROM sales GROUP BY employee_id HAVING SUM(amount) >= 700)
        ORDER BY name
        """
    ).fetchall()

    correlated = cur.execute(
        """
        SELECT e1.name
        FROM employees e1
        WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id)
        ORDER BY e1.name
        """
    ).fetchall()

    exists = cur.execute(
        """
        SELECT name
        FROM employees e
        WHERE EXISTS (SELECT 1 FROM sales s WHERE s.employee_id = e.id AND s.amount >= 500)
        """
    ).fetchall()

    conn.close()
    return {
        "scalar": scalar,
        "in_subquery": [r[0] for r in in_subquery],
        "correlated": [r[0] for r in correlated],
        "exists": [r[0] for r in exists],
    }
