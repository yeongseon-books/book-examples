"""Compilers 101 - Episode 9: Jit vs aot."""

from __future__ import annotations

import ast
import time


def compile_expr(expr: str):
    """Compile expr."""
    return ast.parse(expr, mode="eval")


def _safe_eval(node: ast.AST) -> int:
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, int | float):
        return int(node.value)
    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.FloorDiv):
            return left // right
        if isinstance(node.op, ast.Div):
            return int(left / right)
        if isinstance(node.op, ast.Mod):
            return left % right
        if isinstance(node.op, ast.Pow):
            return left**right
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd | ast.USub):
        value = _safe_eval(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    raise ValueError("unsupported expression")


def aot_eval(expr: str, rounds: int) -> tuple[float, int]:
    """Aot eval."""
    code = compile_expr(expr)
    t0 = time.perf_counter()
    val = 0
    for _ in range(rounds):
        val = _safe_eval(code)
    return time.perf_counter() - t0, int(val)


def jit_eval(expr: str, rounds: int) -> tuple[float, int]:
    """Jit eval."""
    cache: dict[str, ast.AST] = {}
    t0 = time.perf_counter()
    val = 0
    for _ in range(rounds):
        code = cache.get(expr)
        if code is None:
            code = compile_expr(expr)
            cache[expr] = code
        val = _safe_eval(code)
    return time.perf_counter() - t0, int(val)


if __name__ == "__main__":
    expr = "(1+2+3+4)*5"
    print("aot", aot_eval(expr, 10000))
    print("jit", jit_eval(expr, 10000))
