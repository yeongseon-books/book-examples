from conftest import load_module

mod = load_module("ko/10-building-a-tiny-interpreter.py", "ep10")


def test_interpreter_assignment_and_eval() -> None:
    assert mod.run("x = 5; x * 2") == 10
