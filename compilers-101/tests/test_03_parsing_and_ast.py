from conftest import load_module

mod = load_module("ko/03-parsing-and-ast.py", "ep03")


def test_parser_precedence() -> None:
    ast = mod.parse_expression("1 + 2 * 3")
    assert ast == ("bin", "+", ("num", 1), ("bin", "*", ("num", 2), ("num", 3)))
