"""Episode 05: tiny stack-machine VM"""

from typing import TypeAlias

Instruction: TypeAlias = tuple[str, int] | tuple[str]


def run_program(program: list[Instruction], max_steps: int = 10_000) -> list[int]:
    stack: list[int] = []
    pc = 0
    steps = 0
    while 0 <= pc < len(program):
        steps += 1
        if steps > max_steps:
            raise RuntimeError("program did not halt")
        op, *args = program[pc]
        if op == "PUSH":
            stack.append(int(args[0]))
            pc += 1
        elif op == "ADD":
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
            pc += 1
        elif op == "SUB":
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
            pc += 1
        elif op == "JZ":
            target = int(args[0])
            value = stack.pop()
            pc = target if value == 0 else pc + 1
        elif op == "JMP":
            pc = int(args[0])
        elif op == "HALT":
            break
        else:
            raise ValueError(f"unknown opcode: {op}")
    return stack


if __name__ == "__main__":
    demo = [("PUSH", 2), ("PUSH", 3), ("ADD",), ("HALT",)]
    print(run_program(demo))
