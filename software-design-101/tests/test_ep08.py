from ko.ep08_reduce_change_impact import (
    change_points_bad,
    change_points_good,
    good_total,
)


def test_ep08_config_driven_change_impact() -> None:
    assert good_total(2, {"price": 200, "fee": 10}) == 410
    assert change_points_good() < change_points_bad()
