"""Tests for 07 optimization basics in Compilers 101."""

from conftest import load_module

mod = load_module("ko/07-optimization-basics.py", "ep07")


def test_constant_folding() -> None:
    """Test constant folding."""
    folded = mod.constant_fold(("bin", "+", ("num", 3), ("num", 4)))
    assert folded == ("num", 7)
