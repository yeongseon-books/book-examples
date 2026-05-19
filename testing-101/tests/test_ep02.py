"""Tests for ep02 in Testing 101."""

from ko import ep02_unit_test as sut


def test_ep02_unit_isolated_price():
    """Test ep02 unit isolated price."""
    assert sut.calculate_final_price(10000, 0.2) == 8000.0
