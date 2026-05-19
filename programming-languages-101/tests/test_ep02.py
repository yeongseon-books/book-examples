"""Tests for ep02 in Programming Languages 101."""

from ko.ep02_parser import parse_arith_to_ast


def test_ep02_parser_returns_ast():
    """Test ep02 parser returns ast."""
    tree = parse_arith_to_ast("(1+2)*3")
    assert tree.body.op.__class__.__name__ == "Mult"
