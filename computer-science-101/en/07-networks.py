"""Episode 07: in-memory packet switching simulator"""

from collections import deque


class Router:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue: deque[str] = deque()
        self.dropped = 0

    def receive(self, packet: str) -> None:
        if len(self.queue) >= self.capacity:
            self.dropped += 1
        else:
            self.queue.append(packet)

    def forward_one(self) -> str | None:
        if self.queue:
            return self.queue.popleft()
        return None


def simulate_line(packet_count: int, capacity: int, ticks: int) -> tuple[int, int]:
    r1 = Router(capacity)
    r2 = Router(capacity)
    delivered = 0
    for i in range(packet_count):
        r1.receive(f"p{i}")
    for _ in range(ticks):
        moved = r1.forward_one()
        if moved is not None:
            r2.receive(moved)
        out = r2.forward_one()
        if out is not None:
            delivered += 1
    return delivered, r1.dropped + r2.dropped


if __name__ == "__main__":
    delivered, dropped = simulate_line(packet_count=12, capacity=4, ticks=20)
    print("delivered=", delivered, "dropped=", dropped)
