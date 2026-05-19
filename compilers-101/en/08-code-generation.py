# English mirror of Korean episode example
from __future__ import annotations


def tac_to_stack_bytecode(tac: list[str], result_temp: str) -> list[tuple]:
    bytecode: list[tuple] = []
    for line in tac:
        lhs, rhs = [x.strip() for x in line.split("=", 1)]
        parts = rhs.split()
        if len(parts) == 1:
            bytecode.append(("PUSH", int(parts[0])))
            bytecode.append(("STORE", lhs))
        else:
            a, op, b = parts
            bytecode.append(("LOAD", a))
            bytecode.append(("LOAD", b))
            bytecode.append(({"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}[op],))
            bytecode.append(("STORE", lhs))
    bytecode.append(("LOAD", result_temp))
    bytecode.append(("RET",))
    return bytecode


def run_bytecode(bytecode: list[tuple]) -> int:
    stack: list[int] = []
    env: dict[str, int] = {}
    for inst in bytecode:
        op = inst[0]
        if op == "PUSH":
            stack.append(inst[1])
        elif op == "STORE":
            env[inst[1]] = stack.pop()
        elif op == "LOAD":
            stack.append(env[inst[1]])
        elif op == "ADD":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif op == "SUB":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif op == "MUL":
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif op == "DIV":
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        elif op == "RET":
            return stack[-1]
    raise RuntimeError("no RET")


if __name__ == "__main__":
    tac = ["t1 = 3", "t2 = 4", "t3 = t1 + t2"]
    bc = tac_to_stack_bytecode(tac, "t3")
    print(run_bytecode(bc))
