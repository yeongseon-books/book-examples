"""Tests for ep09 in Programming Languages 101."""

from ko.ep09_static_dynamic import dynamic_run, static_check


def test_ep09_static_dynamic_compare():
    """Test ep09 static dynamic compare."""
    expr = ("add", ("num", 1), ("num", 2))
    assert static_check(expr) == "Int"
    assert dynamic_run(expr) == 3
