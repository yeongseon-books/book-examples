# 한국어 예제
import sqlite3

from common import make_dw, time_query


def run_demo() -> dict:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE orders_oltp(order_id INTEGER PRIMARY KEY, customer_id TEXT, amount REAL)"
    )
    conn.executemany(
        "INSERT INTO orders_oltp VALUES (?,?,?)",
        [(i, f"C{i % 100:03d}", float(i % 97 + 1)) for i in range(1, 3001)],
    )
    o_rows, o_t = time_query(
        conn, "SELECT amount FROM orders_oltp WHERE order_id=?", (1500,)
    )
    dw = make_dw(1200)
    a_rows, a_t = time_query(
        dw,
        "SELECT d.year,d.month,c.region,SUM(f.amount) FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key JOIN dim_customer c ON c.customer_key=f.customer_key GROUP BY d.year,d.month,c.region",
    )
    return {
        "oltp_one_row": len(o_rows),
        "olap_groups": len(a_rows),
        "oltp_time": o_t,
        "olap_time": a_t,
    }


if __name__ == "__main__":
    print(run_demo())
