from ko.ep02_parser import parse_arith_to_ast

def test_ep02_parser_returns_ast():
    tree = parse_arith_to_ast("(1+2)*3")
    assert tree.body.op.__class__.__name__ == "Mult"
