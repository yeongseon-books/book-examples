from conftest import load_module

mod = load_module("ko/02-lexical-analysis.py", "ep02")


def test_tokenize_simple_expression() -> None:
    tokens = mod.tokenize("1 + 2")
    assert [(t.kind, t.value) for t in tokens] == [("NUMBER", 1), ("PLUS", "+"), ("NUMBER", 2)]
