"""Episode 05: sliding window memory and checkpoint example."""


class SlidingMemory:
    def __init__(self, max_items: int = 4):
        self.max_items = max_items
        self.items: list[str] = []

    def add(self, message: str) -> None:
        self.items.append(message)
        self.items = self.items[-self.max_items :]


def checkpoint(state: dict[str, object]) -> dict[str, object]:
    return dict(state)


if __name__ == "__main__":
    mem = SlidingMemory(3)
    for x in ["a", "b", "c", "d"]:
        mem.add(x)
    print(mem.items)
    print(checkpoint({"step": 2, "status": "running"}))
