from conftest import load_module

mod = load_module("ko/09-jit-vs-aot.py", "ep09")


def test_jit_aot_same_value() -> None:
    _, a = mod.aot_eval("(1+2+3)*4", 20)
    _, b = mod.jit_eval("(1+2+3)*4", 20)
    assert a == b == 24
