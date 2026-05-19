from en.ep07_window import run_demo


def test_ep07_window_functions():
    rows = run_demo()
    bob_rows = [r for r in rows if r["employee_id"] == 2]
    assert bob_rows[0]["rn"] == 1
    assert bob_rows[1]["prev_amount"] == 300
    assert bob_rows[-1]["running_sum"] == 850
