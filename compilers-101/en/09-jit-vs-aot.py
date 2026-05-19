"""Compilers 101 - Episode 9: Jit vs aot."""

# English mirror of Korean episode example
from __future__ import annotations

import time


def compile_expr(expr: str):
    """Compile expr."""
    return compile(expr, "<jit>", "eval")


def aot_eval(expr: str, rounds: int) -> tuple[float, int]:
    """Aot eval."""
    code = compile_expr(expr)
    t0 = time.perf_counter()
    val = 0
    for _ in range(rounds):
        val = eval(code, {"__builtins__": {}}, {})
    return time.perf_counter() - t0, int(val)


def jit_eval(expr: str, rounds: int) -> tuple[float, int]:
    """Jit eval."""
    cache: dict[str, object] = {}
    t0 = time.perf_counter()
    val = 0
    for _ in range(rounds):
        code = cache.get(expr)
        if code is None:
            code = compile_expr(expr)
            cache[expr] = code
        val = eval(code, {"__builtins__": {}}, {})
    return time.perf_counter() - t0, int(val)


if __name__ == "__main__":
    expr = "(1+2+3+4)*5"
    print("aot", aot_eval(expr, 10000))
    print("jit", jit_eval(expr, 10000))
