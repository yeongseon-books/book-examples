from en.ep10_practical_analysis import run_demo


def test_ep10_practical_analysis_queries():
    out = run_demo()
    assert out["top_customers"][0]["customer_id"] == 101
    assert out["top_customers"][0]["total"] == 670
    assert [m["month"] for m in out["monthly"]] == [
        "2024-01",
        "2024-02",
        "2024-03",
        "2024-04",
    ]
    assert out["cohort"][0]["cohort_month"] == "2024-01"
