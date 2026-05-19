from __future__ import annotations
# pyright: reportMissingTypeArgument=false, reportUnknownParameterType=false, reportUnknownVariableType=false, reportUnusedCallResult=false, reportUnknownArgumentType=false


class SemanticError(Exception):
    pass


def check_program(program: list[tuple]) -> dict[str, str]:
    env: dict[str, str] = {}

    def type_of(node: tuple) -> str:
        kind = node[0]
        if kind == "num":
            return "int"
        if kind == "str":
            return "str"
        if kind == "var":
            name = node[1]
            if name not in env:
                raise SemanticError(f"undefined variable: {name}")
            return env[name]
        if kind == "bin":
            op, left, right = node[1], node[2], node[3]
            lt, rt = type_of(left), type_of(right)
            if lt != rt:
                raise SemanticError(f"type mismatch for {op}: {lt} vs {rt}")
            return lt
        raise SemanticError(f"unknown node: {kind}")

    for stmt in program:
        if stmt[0] == "let":
            _, name, expr = stmt
            env[name] = type_of(expr)
        elif stmt[0] == "expr":
            type_of(stmt[1])
        else:
            raise SemanticError("unknown statement")
    return env


if __name__ == "__main__":
    sample = [
        ("let", "x", ("num", 1)),
        ("expr", ("bin", "+", ("var", "x"), ("num", 2))),
    ]
    print(check_program(sample))
