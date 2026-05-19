from en.ep09_capacity_planning import forecast_next, headroom_ok


def test_ep09_capacity_forecast_headroom():
    assert round(forecast_next([100, 110, 120]), 5) == 130
    assert headroom_ok(70, 100)
    assert not headroom_ok(90, 100)
