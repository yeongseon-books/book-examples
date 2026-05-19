from __future__ import annotations

import random


class DirectMappedCache:
    def __init__(self, lines: int = 8, line_size: int = 4) -> None:
        self.lines: int = lines
        self.line_size: int = line_size
        self.tags: list[int | None] = [None] * lines
        self.hits: int = 0
        self.misses: int = 0

    def access(self, address: int) -> bool:
        block = address // self.line_size
        index = block % self.lines
        tag = block // self.lines
        if self.tags[index] == tag:
            self.hits += 1
            return True
        self.tags[index] = tag
        self.misses += 1
        return False

    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total else 0.0


def compare_locality(seed: int = 7) -> tuple[float, float]:
    seq_cache = DirectMappedCache()
    for i in range(256):
        _ = seq_cache.access(i)

    rnd_cache = DirectMappedCache()
    rng = random.Random(seed)
    for _ in range(256):
        _ = rnd_cache.access(rng.randrange(0, 256))
    return seq_cache.hit_rate(), rnd_cache.hit_rate()


if __name__ == "__main__":
    print(compare_locality())
