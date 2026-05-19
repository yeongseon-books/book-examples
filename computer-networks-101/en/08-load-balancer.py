# English mirror of the corresponding episode demo
from dataclasses import dataclass


@dataclass
class Backend:
    name: str
    weight: int = 1
    active_connections: int = 0


class RoundRobinBalancer:
    def __init__(self, backends: list[Backend]):
        self.backends = backends
        self._cursor = 0

    def pick(self) -> Backend:
        backend = self.backends[self._cursor % len(self.backends)]
        self._cursor += 1
        return backend


class WeightedRoundRobinBalancer:
    def __init__(self, backends: list[Backend]):
        self.sequence: list[Backend] = []
        for backend in backends:
            self.sequence.extend([backend] * backend.weight)
        self._cursor = 0

    def pick(self) -> Backend:
        backend = self.sequence[self._cursor % len(self.sequence)]
        self._cursor += 1
        return backend


class LeastConnectionsBalancer:
    def __init__(self, backends: list[Backend]):
        self.backends = backends

    def pick(self) -> Backend:
        return min(self.backends, key=lambda backend: backend.active_connections)


if __name__ == "__main__":
    rr = RoundRobinBalancer([Backend("a"), Backend("b")])
    print([rr.pick().name for _ in range(4)])
