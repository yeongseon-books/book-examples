from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Machine:
    memory: list[tuple[str, int]]
    data: list[int]
    acc: int = 0
    pc: int = 0
    halted: bool = False

    def step(self) -> None:
        op, arg = self.memory[self.pc]
        if op == "LOAD":
            self.acc = self.data[arg]
            self.pc += 1
        elif op == "ADD":
            self.acc += self.data[arg]
            self.pc += 1
        elif op == "STORE":
            self.data[arg] = self.acc
            self.pc += 1
        elif op == "HALT":
            self.halted = True
        else:
            raise ValueError(op)


def run_program() -> int:
    program = [("LOAD", 0), ("ADD", 1), ("STORE", 2), ("HALT", 0)]
    data = [7, 5, 0]
    m = Machine(memory=program, data=data)
    while not m.halted:
        m.step()
    return m.data[2]


if __name__ == "__main__":
    print(run_program())
