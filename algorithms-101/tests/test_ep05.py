"""Tests for ep05 in Algorithms 101."""

from conftest import load_module

ko = load_module(
    "ko/05-recursion-and-divide-and-conquer/step01_fast_power.py", "ko_ep05"
)


def test_ep05_fast_power() -> None:
    """Test ep05 fast power."""
    assert ko.fast_power(2, 10) == 1024
    assert ko.run()["value"] == 1073741824
