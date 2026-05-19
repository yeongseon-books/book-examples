from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Cart:
    items: list[dict[str, int]]

    def total(self) -> int:
        return sum(item["price"] * item["qty"] for item in self.items)


def total_fp(items: list[dict[str, int]]) -> int:
    return sum(item["price"] * item["qty"] for item in items)


def total_hybrid(cart: Cart) -> int:
    return total_fp(cart.items)


if __name__ == "__main__":
    cart = Cart(items=[{"price": 1000, "qty": 2}, {"price": 500, "qty": 3}])
    print(cart.total(), total_hybrid(cart))
