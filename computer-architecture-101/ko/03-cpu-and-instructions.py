from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, TypedDict

Opcode = Literal["LOAD", "STORE", "ADD", "SUB", "JMP", "HLT"]


class Instruction(TypedDict):
    op: Opcode
    a: str | int | None
    b: str | int | None
    c: str | int | None


@dataclass
class TinyISA:
    memory: list[int]
    program: list[Instruction]
    regs: dict[str, int] = field(default_factory=lambda: {"R0": 0, "R1": 0})
    pc: int = 0
    halted: bool = False

    def step(self) -> None:
        inst = self.program[self.pc]
        op = inst["op"]
        if op == "LOAD":
            reg = str(inst["a"])
            addr_v = inst["b"]
            if not isinstance(addr_v, int):
                raise ValueError("LOAD requires integer address")
            addr = addr_v
            self.regs[reg] = self.memory[addr]
            self.pc += 1
        elif op == "STORE":
            reg = str(inst["a"])
            addr_v = inst["b"]
            if not isinstance(addr_v, int):
                raise ValueError("STORE requires integer address")
            addr = addr_v
            self.memory[addr] = self.regs[reg]
            self.pc += 1
        elif op == "ADD":
            dst = str(inst["a"])
            left = str(inst["b"])
            right = str(inst["c"])
            self.regs[dst] = self.regs[left] + self.regs[right]
            self.pc += 1
        elif op == "SUB":
            dst = str(inst["a"])
            left = str(inst["b"])
            right = str(inst["c"])
            self.regs[dst] = self.regs[left] - self.regs[right]
            self.pc += 1
        elif op == "JMP":
            target_v = inst["a"]
            if not isinstance(target_v, int):
                raise ValueError("JMP requires integer target")
            self.pc = target_v
        elif op == "HLT":
            self.halted = True


def run_sample_program() -> tuple[int, int]:
    program: list[Instruction] = [
        {"op": "LOAD", "a": "R0", "b": 0, "c": None},
        {"op": "LOAD", "a": "R1", "b": 1, "c": None},
        {"op": "ADD", "a": "R0", "b": "R0", "c": "R1"},
        {"op": "STORE", "a": "R0", "b": 2, "c": None},
        {"op": "HLT", "a": None, "b": None, "c": None},
    ]
    memory = [10, 32, 0]
    cpu = TinyISA(memory=memory, program=program)
    while not cpu.halted:
        cpu.step()
    return cpu.memory[2], cpu.regs["R0"]


if __name__ == "__main__":
    print(run_sample_program())
