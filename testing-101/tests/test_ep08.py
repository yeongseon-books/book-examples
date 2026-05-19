"""Tests for ep08 in Testing 101."""

from ko.ep08_regression_test import apply_discount


def test_ep08_regression_bug_does_not_return_added_value():
    """Test ep08 regression bug does not return added value."""
    assert apply_discount(10000, 2500) == 7500
