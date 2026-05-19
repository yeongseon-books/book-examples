from __future__ import annotations


class MemoryHierarchy:
    def __init__(self) -> None:
        self.registers: dict[int, int] = {}
        self.l1: dict[int, int] = {}
        self.main: dict[int, int] = {}
        self.access_counter: dict[str, int] = {"register": 0, "l1": 0, "main": 0}

    def store_main(self, addr: int, value: int) -> None:
        self.main[addr] = value

    def load(self, addr: int) -> int:
        if addr in self.registers:
            self.access_counter["register"] += 1
            return self.registers[addr]
        if addr in self.l1:
            self.access_counter["l1"] += 1
            self.registers[addr] = self.l1[addr]
            return self.l1[addr]
        self.access_counter["main"] += 1
        value = self.main[addr]
        self.l1[addr] = value
        self.registers[addr] = value
        return value


def demo_sequence() -> dict[str, int]:
    mem = MemoryHierarchy()
    mem.store_main(100, 42)
    _ = mem.load(100)
    mem.registers.clear()
    _ = mem.load(100)
    _ = mem.load(100)
    return mem.access_counter


if __name__ == "__main__":
    print(demo_sequence())
