from en.ep04_error_budget import burn_rate, mwmb_alert


def test_ep04_mwmb():
    assert round(burn_rate(0.0288, 0.002), 1) == 14.4
    assert mwmb_alert(14.4, 6.0)
