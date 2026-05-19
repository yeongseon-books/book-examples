from en.ep05_group_by import run_demo


def test_ep05_group_by_aggregations_having():
    rows = run_demo()
    assert rows[0]["employee_id"] == 2
    assert rows[0]["total_amount"] == 850
    assert rows[1]["employee_id"] == 6
