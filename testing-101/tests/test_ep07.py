"""Tests for ep07 in Testing 101."""

from ko.ep07_coverage import shipping_fee


def test_ep07_branch_coverage_cases():
    """Test ep07 branch coverage cases."""
    assert shipping_fee(70000, False) == 0
    assert shipping_fee(10000, True) == 1500
    assert shipping_fee(10000, False) == 3000
