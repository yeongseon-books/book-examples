# English example
from common import make_dw


def run_demo() -> dict:
    conn = make_dw(400)
    rows = conn.execute(
        "SELECT d.year,d.month,p.category,c.region,ROUND(SUM(f.amount),2) FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key JOIN dim_product p ON p.product_key=f.product_key JOIN dim_customer c ON c.customer_key=f.customer_key GROUP BY d.year,d.month,p.category,c.region"
    ).fetchall()
    total = conn.execute("SELECT ROUND(SUM(amount),2) FROM fact_sales").fetchone()[0]
    return {
        "groups": len(rows),
        "fact_total": total,
        "grouped_total": round(sum(r[4] for r in rows), 2),
    }


if __name__ == "__main__":
    print(run_demo())
