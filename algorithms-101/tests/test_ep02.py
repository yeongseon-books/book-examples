"""Tests for ep02 in Algorithms 101."""

from conftest import load_module

ko = load_module(
    "ko/02-time-and-space-complexity/step01_complexity_playground.py", "ko_ep02"
)


def test_ep02_quadratic_is_slower() -> None:
    """Test ep02 quadratic is slower."""
    result = ko.run()
    assert result["linear_ms"] > 0
    assert result["quadratic_ms"] > result["linear_ms"]
