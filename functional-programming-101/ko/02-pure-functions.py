from __future__ import annotations


def apply_discount(price: int, discount_rate: float) -> int:
    return int(price * (1 - discount_rate))


if __name__ == "__main__":
    print(apply_discount(10000, 0.1))
