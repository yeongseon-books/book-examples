from __future__ import annotations

from typing import TypeAlias

Inst: TypeAlias = tuple[str, str | None, str | int | None, str | int | None]


def constant_fold(node: tuple) -> tuple:
    if node[0] == "num":
        return node
    _, op, left, right = node
    left = constant_fold(left)
    right = constant_fold(right)
    if left[0] == "num" and right[0] == "num":
        a = left[1]
        b = right[1]
        return ("num", {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[op])
    return ("bin", op, left, right)


def dce(instructions: list[Inst]) -> list[Inst]:
    used: set[str] = set()
    result: list[Inst] = []
    for op, dst, a, b in reversed(instructions):
        if op == "RET":
            used.add(a)
            result.append((op, dst, a, b))
        elif dst in used:
            if isinstance(a, str):
                used.add(a)
            if isinstance(b, str):
                used.add(b)
            result.append((op, dst, a, b))
    return list(reversed(result))


if __name__ == "__main__":
    ast = ("bin", "+", ("num", 3), ("num", 4))
    print(constant_fold(ast))
