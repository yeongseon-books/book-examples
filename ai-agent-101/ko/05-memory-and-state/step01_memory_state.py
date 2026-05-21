"""Ai Agent 101 - 5편: memory and state 예제."""


class SlidingMemory:
    """Sliding memory."""

    def __init__(self, max_items: int = 4):
        self.max_items = max_items
        self.items: list[str] = []

    def add(self, message: str) -> None:
        """Add."""
        self.items.append(message)
        self.items = self.items[-self.max_items :]


def checkpoint(state: dict[str, object]) -> dict[str, object]:
    """Checkpoint."""
    return dict(state)


if __name__ == "__main__":
    mem = SlidingMemory(3)
    for x in ["a", "b", "c", "d"]:
        mem.add(x)
    print(mem.items)
    print(checkpoint({"step": 2, "status": "running"}))
