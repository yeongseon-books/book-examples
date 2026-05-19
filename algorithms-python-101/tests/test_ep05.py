"""Tests for ep05 in Algorithms Python 101."""

from tests.conftest import load_module


def test_power_divide_and_conquer() -> None:
    """Test power divide and conquer."""
    mod = load_module(
        "ko/05-recursion-and-divide-and-conquer/step01_recursion.py", "ep05"
    )
    assert mod.power(2, 10) == 1024
    assert mod.power(3, 5) == 243
