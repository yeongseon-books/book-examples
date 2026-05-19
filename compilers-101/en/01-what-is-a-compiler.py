"""Compilers 101 - Episode 1: What is a compiler."""

# English mirror of Korean episode example
from __future__ import annotations


def compile_pipeline(source: str) -> dict[str, object]:
    """Compile pipeline."""
    tokens = ["2", "+", "3", "*", "4"]
    ast = ("bin", "+", ("num", 2), ("bin", "*", ("num", 3), ("num", 4)))
    ir = ["t1 = 3 * 4", "t2 = 2 + t1", "ret t2"]
    return {"source": source, "tokens": tokens, "ast": ast, "ir": ir, "output": 14}


if __name__ == "__main__":
    print(compile_pipeline("2 + 3 * 4"))
