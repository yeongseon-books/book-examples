"""Tests for ep08 in Programming Languages 101."""

from ko.ep08_interpreter_compiler import compile_bytecode, interpret


def test_ep08_interpret_and_compile():
    """Test ep08 interpret and compile."""
    expr = ("add", ("num", 1), ("num", 2))
    assert interpret(expr) == 3
    assert compile_bytecode(expr)[-1] == ("ADD",)
