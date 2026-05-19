from __future__ import annotations

from collections.abc import Iterator

from common import SideEffectCounter


def lazy_prices(counter: SideEffectCounter) -> Iterator[int]:
    for price in [1200, 3400, 5600, 9000]:
        counter.tick()
        yield int(price * 0.9)


if __name__ == "__main__":
    c = SideEffectCounter()
    stream = lazy_prices(c)
    print(next(stream), c.calls)
