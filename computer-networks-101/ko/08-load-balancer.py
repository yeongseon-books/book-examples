"""Computer Networks 101 - Episode 8: Load balancer."""

from dataclasses import dataclass


@dataclass
class Backend:
    """Backend."""

    name: str
    weight: int = 1
    active_connections: int = 0


class RoundRobinBalancer:
    """Round robin balancer."""

    def __init__(self, backends: list[Backend]):
        self.backends = backends
        self._cursor = 0

    def pick(self) -> Backend:
        """Pick."""
        backend = self.backends[self._cursor % len(self.backends)]
        self._cursor += 1
        return backend


class WeightedRoundRobinBalancer:
    """Weighted round robin balancer."""

    def __init__(self, backends: list[Backend]):
        self.sequence: list[Backend] = []
        for backend in backends:
            self.sequence.extend([backend] * backend.weight)
        self._cursor = 0

    def pick(self) -> Backend:
        """Pick."""
        backend = self.sequence[self._cursor % len(self.sequence)]
        self._cursor += 1
        return backend


class LeastConnectionsBalancer:
    """Least connections balancer."""

    def __init__(self, backends: list[Backend]):
        self.backends = backends

    def pick(self) -> Backend:
        """Pick."""
        return min(self.backends, key=lambda backend: backend.active_connections)


if __name__ == "__main__":
    rr = RoundRobinBalancer([Backend("a"), Backend("b")])
    print([rr.pick().name for _ in range(4)])
