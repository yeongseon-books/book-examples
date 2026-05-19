"""Programming Languages 101 - Episode 2: Parser."""

import ast


def parse_arith_to_ast(expr: str) -> ast.AST:
    """Parse arith to ast."""
    return ast.parse(expr, mode="eval")
