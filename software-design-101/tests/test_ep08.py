"""Tests for ep08 in Software Design 101."""

from ko.ep08_reduce_change_impact import (
    change_points_bad,
    change_points_good,
    good_total,
)


def test_ep08_config_driven_change_impact() -> None:
    """Test ep08 config driven change impact."""
    assert good_total(2, {"price": 200, "fee": 10}) == 410
    assert change_points_good() < change_points_bad()
