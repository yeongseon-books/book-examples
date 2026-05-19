import ast

def parse_arith_to_ast(expr: str) -> ast.AST:
    return ast.parse(expr, mode="eval")
