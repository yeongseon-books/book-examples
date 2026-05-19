"""Tests for 09 jit vs aot in Compilers 101."""

from conftest import load_module

mod = load_module("ko/09-jit-vs-aot.py", "ep09")


def test_jit_aot_same_value() -> None:
    """Test jit aot same value."""
    _, a = mod.aot_eval("(1+2+3)*4", 20)
    _, b = mod.jit_eval("(1+2+3)*4", 20)
    assert a == b == 24
