# English mirror of Korean episode example
from __future__ import annotations


def ast_to_tac(
    node: tuple, out: list[str] | None = None, counter: list[int] | None = None
) -> tuple[list[str], str]:
    if out is None:
        out = []
    if counter is None:
        counter = [0]

    def fresh() -> str:
        counter[0] += 1
        return f"t{counter[0]}"

    kind = node[0]
    if kind == "num":
        dst = fresh()
        out.append(f"{dst} = {node[1]}")
        return out, dst

    _, op, left, right = node
    out, l = ast_to_tac(left, out, counter)
    out, r = ast_to_tac(right, out, counter)
    dst = fresh()
    out.append(f"{dst} = {l} {op} {r}")
    return out, dst


if __name__ == "__main__":
    ast = ("bin", "+", ("num", 1), ("bin", "*", ("num", 2), ("num", 3)))
    code, result = ast_to_tac(ast)
    print("\n".join(code + [f"ret {result}"]))
