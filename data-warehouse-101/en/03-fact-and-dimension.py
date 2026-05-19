# English example
import sqlite3


def run_demo() -> dict:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE raw_orders(order_id INTEGER,order_date TEXT,customer_id TEXT,product_id TEXT,qty INTEGER,amount REAL)"
    )
    c.executemany(
        "INSERT INTO raw_orders VALUES (?,?,?,?,?,?)",
        [
            (1, "2026-01-01", "C1", "P1", 2, 20.0),
            (1, "2026-01-01", "C1", "P2", 1, 15.0),
            (2, "2026-01-02", "C2", "P2", 3, 45.0),
        ],
    )
    c.executescript(
        "CREATE TABLE dim_customer(customer_key INTEGER PRIMARY KEY AUTOINCREMENT,customer_id TEXT UNIQUE);CREATE TABLE dim_product(product_key INTEGER PRIMARY KEY AUTOINCREMENT,product_id TEXT UNIQUE);CREATE TABLE dim_date(date_key INTEGER PRIMARY KEY,full_date TEXT UNIQUE);CREATE TABLE fact_order_line(order_line_key INTEGER PRIMARY KEY AUTOINCREMENT,order_id INTEGER,date_key INTEGER,customer_key INTEGER,product_key INTEGER,qty INTEGER,amount REAL);"
    )
    c.execute(
        "INSERT INTO dim_customer(customer_id) SELECT DISTINCT customer_id FROM raw_orders"
    )
    c.execute(
        "INSERT INTO dim_product(product_id) SELECT DISTINCT product_id FROM raw_orders"
    )
    c.execute(
        "INSERT INTO dim_date(date_key,full_date) SELECT DISTINCT CAST(REPLACE(order_date,'-','') AS INTEGER),order_date FROM raw_orders"
    )
    c.execute(
        "INSERT INTO fact_order_line(order_id,date_key,customer_key,product_key,qty,amount) SELECT r.order_id,CAST(REPLACE(r.order_date,'-','') AS INTEGER),dc.customer_key,dp.product_key,r.qty,r.amount FROM raw_orders r JOIN dim_customer dc ON dc.customer_id=r.customer_id JOIN dim_product dp ON dp.product_id=r.product_id"
    )
    fr = c.execute("SELECT COUNT(*) FROM fact_order_line").fetchone()[0]
    od = c.execute("SELECT COUNT(DISTINCT order_id) FROM fact_order_line").fetchone()[0]
    return {"fact_grain": "order_line", "fact_rows": fr, "orders": od}


if __name__ == "__main__":
    print(run_demo())
