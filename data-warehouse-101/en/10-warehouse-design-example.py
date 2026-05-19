"""Data Warehouse 101 - Episode 10: Warehouse design example."""

# English example
import sqlite3
from random import Random


def run_demo() -> dict:
    """Run demo."""
    r = Random(99)
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.executescript(
        "CREATE TABLE oltp_orders(order_id INTEGER,order_date TEXT,customer_id TEXT,product_id TEXT,qty INTEGER,amount REAL);CREATE TABLE dim_date(date_key INTEGER PRIMARY KEY,full_date TEXT,year INTEGER,month INTEGER);CREATE TABLE dim_customer(customer_key INTEGER PRIMARY KEY AUTOINCREMENT,customer_id TEXT UNIQUE);CREATE TABLE dim_product(product_key INTEGER PRIMARY KEY AUTOINCREMENT,product_id TEXT UNIQUE,category TEXT);CREATE TABLE fact_sales(order_id INTEGER,date_key INTEGER,customer_key INTEGER,product_key INTEGER,qty INTEGER,amount REAL);"
    )
    for oid in range(1, 301):
        m = (oid % 6) + 1
        d = f"2026-{m:02d}-{(oid % 27) + 1:02d}"
        cid = f"C{(oid % 40) + 1:03d}"
        pid = f"P{(oid % 5) + 1:02d}"
        qty = (oid % 4) + 1
        amount = round(qty * (10 + r.randint(0, 30)), 2)
        c.execute(
            "INSERT INTO oltp_orders VALUES (?,?,?,?,?,?)",
            (oid, d, cid, pid, qty, amount),
        )
    c.execute(
        "INSERT INTO dim_customer(customer_id) SELECT DISTINCT customer_id FROM oltp_orders"
    )
    c.execute(
        "INSERT INTO dim_product(product_id,category) SELECT DISTINCT product_id,CASE WHEN product_id IN ('P01','P02') THEN 'Core' ELSE 'Plus' END FROM oltp_orders"
    )
    c.execute(
        "INSERT INTO dim_date(date_key,full_date,year,month) SELECT DISTINCT CAST(REPLACE(order_date,'-','') AS INTEGER),order_date,CAST(substr(order_date,1,4) AS INTEGER),CAST(substr(order_date,6,2) AS INTEGER) FROM oltp_orders"
    )
    c.execute(
        "INSERT INTO fact_sales SELECT o.order_id,CAST(REPLACE(o.order_date,'-','') AS INTEGER),dc.customer_key,dp.product_key,o.qty,o.amount FROM oltp_orders o JOIN dim_customer dc ON dc.customer_id=o.customer_id JOIN dim_product dp ON dp.product_id=o.product_id"
    )
    c.execute(
        "CREATE TABLE mart_sales AS SELECT d.year,d.month,p.category,ROUND(SUM(f.amount),2) AS revenue,COUNT(*) AS orders FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key JOIN dim_product p ON p.product_key=f.product_key GROUP BY d.year,d.month,p.category"
    )
    top = c.execute(
        "SELECT year,month,revenue FROM mart_sales ORDER BY revenue DESC LIMIT 3"
    ).fetchall()
    share = c.execute(
        "SELECT category,SUM(revenue) FROM mart_sales GROUP BY category"
    ).fetchall()
    rows = c.execute("SELECT COUNT(*) FROM mart_sales").fetchone()[0]
    doc = "# Warehouse Design Doc\n\n- Grain: one order line per row in fact_sales\n- Dimensions: date, customer, product\n- Mart: mart_sales with monthly category revenue\n- BI Queries: top months, category share, mart row count\n"
    return {
        "mart_rows": rows,
        "bi_top_months": top,
        "bi_category_share": share,
        "bi_mart_count": rows,
        "design_doc": doc,
    }


if __name__ == "__main__":
    print(run_demo()["design_doc"])
