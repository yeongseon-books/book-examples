# 한국어 예제
import json
from common import make_dw

def ascii_bars(items):
    maxv=max((v for _,v in items),default=1.0)
    return '\n'.join(f"{k:10} | {'#'*int((v/maxv)*20)} {v:.1f}" for k,v in items)

def run_demo(start='2025-01-01',end='2026-12-31',region='KR-Seoul') -> dict:
    conn=make_dw(500)
    total=conn.execute('SELECT ROUND(SUM(f.amount),2) FROM fact_sales f JOIN dim_customer c ON c.customer_key=f.customer_key JOIN dim_date d ON d.date_key=f.date_key WHERE d.full_date BETWEEN ? AND ? AND c.region=?',(start,end,region)).fetchone()[0] or 0.0
    trend=conn.execute('SELECT d.year||"-"||printf("%02d",d.month),ROUND(SUM(f.amount),2) FROM fact_sales f JOIN dim_date d ON d.date_key=f.date_key JOIN dim_customer c ON c.customer_key=f.customer_key WHERE d.full_date BETWEEN ? AND ? AND c.region=? GROUP BY 1 ORDER BY 1',(start,end,region)).fetchall()
    breakdown=conn.execute('SELECT p.category,ROUND(SUM(f.amount),2) FROM fact_sales f JOIN dim_product p ON p.product_key=f.product_key JOIN dim_customer c ON c.customer_key=f.customer_key JOIN dim_date d ON d.date_key=f.date_key WHERE d.full_date BETWEEN ? AND ? AND c.region=? GROUP BY p.category ORDER BY 2 DESC',(start,end,region)).fetchall()
    p={"total":total,"trend":trend,"breakdown":breakdown,"preview":ascii_bars(breakdown)}
    p['json']=json.dumps(p,ensure_ascii=False)
    return p

if __name__=='__main__':
    print(run_demo()['preview'])
