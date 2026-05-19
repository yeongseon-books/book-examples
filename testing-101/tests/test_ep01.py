"""Tests for ep01 in Testing 101."""

from ko import ep01_testing_overview as sut


def test_ep01_add():
    """Test ep01 add."""
    assert sut.add(2, 3) == 5


def test_ep01_regression_guard_for_multiply():
    """Test ep01 regression guard for multiply."""
    assert sut.multiply(4, 5) == 20
