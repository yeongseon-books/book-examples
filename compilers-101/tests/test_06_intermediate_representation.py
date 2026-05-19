from conftest import load_module

mod = load_module("ko/06-intermediate-representation.py", "ep06")


def test_ast_to_tac() -> None:
    ast = ("bin", "+", ("num", 1), ("num", 2))
    code, result = mod.ast_to_tac(ast)
    assert code[-1] == "t3 = t1 + t2"
    assert result.startswith("t")
