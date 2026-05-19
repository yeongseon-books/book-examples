from en.ep02_select import run_demo


def test_ep02_select_order_limit_alias():
    rows = run_demo()
    assert rows[0]["employee_name"] == "Alice"
    assert len(rows) == 3
