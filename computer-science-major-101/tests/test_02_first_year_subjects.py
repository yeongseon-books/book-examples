"""Tests for 02 first year subjects in Computer Science Major 101."""

from conftest import load_module


def test_discrete_math_helpers() -> None:
    """Test discrete math helpers."""
    mod = load_module("ko/02-first-year-subjects.py")
    ops = mod.set_operations({1, 2, 3}, {3, 4})
    assert ops["union"] == {1, 2, 3, 4}
    assert ops["intersection"] == {3}
    assert mod.mod_pow(2, 10, 7) == pow(2, 10, 7)
    assert mod.verify_induction_sum(100)
