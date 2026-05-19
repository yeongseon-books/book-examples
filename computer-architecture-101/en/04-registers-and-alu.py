from __future__ import annotations


class ALU:
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def bit_and(self, a: int, b: int) -> int:
        return a & b

    def bit_or(self, a: int, b: int) -> int:
        return a | b

    def bit_xor(self, a: int, b: int) -> int:
        return a ^ b

    def shl(self, a: int, n: int) -> int:
        return a << n

    def shr(self, a: int, n: int) -> int:
        return a >> n


class RegisterFile:
    def __init__(self) -> None:
        self.regs: dict[str, int] = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}

    def read(self, name: str) -> int:
        return self.regs[name]

    def write(self, name: str, value: int) -> None:
        self.regs[name] = value


def demo() -> int:
    rf = RegisterFile()
    alu = ALU()
    rf.write("R0", 7)
    rf.write("R1", 5)
    rf.write("R2", alu.add(rf.read("R0"), rf.read("R1")))
    return rf.read("R2")


if __name__ == "__main__":
    print(demo())
