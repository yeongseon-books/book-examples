"""Tests for ep04 in Type Hints Python 101."""

from ko.ep04_function_hints import run_op, sum_all


def test_ep04_callable_and_varargs() -> None:
    """Test ep04 callable and varargs."""
    assert run_op(lambda a, b: a * b, 3, 4) == 12
    assert sum_all(1, 2, x=3, y=4, scale=2) == 20
