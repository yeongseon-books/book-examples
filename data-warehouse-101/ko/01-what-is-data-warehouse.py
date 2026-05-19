# 한국어 예제
from common import make_dw


def run_demo() -> dict:
    conn = make_dw(200)
    rows = conn.execute(
        "SELECT d.year,d.month,ROUND(SUM(f.amount),2) FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key GROUP BY d.year,d.month ORDER BY d.year,d.month"
    ).fetchall()
    return {
        "months": len(rows),
        "first_row": rows[0],
        "total_revenue": round(sum(r[2] for r in rows), 2),
    }


if __name__ == "__main__":
    print(run_demo())
