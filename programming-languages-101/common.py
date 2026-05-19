"""Shared utilities and domain models for Programming Languages 101."""

import ast
from dataclasses import dataclass

_ALLOWED_BINOPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.FloorDiv)
_ALLOWED_UNARY = (ast.UAdd, ast.USub)


def safe_eval_arith(expr: str) -> float:
    """Safe eval arith."""
    node = ast.parse(expr, mode="eval")
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            raise ValueError("calls are not allowed")
        if isinstance(n, ast.Name):
            raise ValueError("names are not allowed")
        if isinstance(n, ast.BinOp) and not isinstance(n.op, _ALLOWED_BINOPS):
            raise ValueError("operator not allowed")
        if isinstance(n, ast.UnaryOp) and not isinstance(n.op, _ALLOWED_UNARY):
            raise ValueError("unary operator not allowed")
        if isinstance(n, ast.Constant) and not isinstance(n.value, int | float):
            raise ValueError("only numbers are allowed")
    return eval(compile(node, "<safe-arith>", "eval"), {"__builtins__": {}}, {})


@dataclass
class FeatureScore:
    """Feature score."""

    orthogonality: int
    readability: int
    safety: int
    tooling: int

    def total(self) -> int:
        """Total."""
        return self.orthogonality + self.readability + self.safety + self.tooling
