from en.ep02_n_nines import availability_from_nines, downtime_budget_minutes


def test_ep02_n_nines_budget():
    assert round(availability_from_nines(3), 3) == 0.999
    assert round(downtime_budget_minutes(3, 30 * 24 * 60), 1) == 43.2
