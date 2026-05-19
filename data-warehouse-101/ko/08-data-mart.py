# 한국어 예제
from common import make_dw


def run_demo() -> dict:
    conn = make_dw(600)
    conn.execute(
        "CREATE TABLE finance_mart_monthly AS SELECT d.year AS fiscal_year,d.month AS fiscal_month,ROUND(SUM(f.amount),2) AS booked_revenue FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key GROUP BY d.year,d.month"
    )
    mart = conn.execute(
        "SELECT ROUND(SUM(booked_revenue),2) FROM finance_mart_monthly"
    ).fetchone()[0]
    dw = conn.execute("SELECT ROUND(SUM(amount),2) FROM fact_sales").fetchone()[0]
    return {
        "mart_rows": conn.execute(
            "SELECT COUNT(*) FROM finance_mart_monthly"
        ).fetchone()[0],
        "mart_total": mart,
        "dw_total": dw,
    }


if __name__ == "__main__":
    print(run_demo())
