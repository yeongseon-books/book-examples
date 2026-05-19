"""Episode 03: bits, encoding, floating point"""

import math


def int_to_binary(n: int) -> str:
    return format(n, "b")


def utf8_bytes(text: str) -> list[int]:
    return list(text.encode("utf-8"))


def float_sum_issue() -> tuple[float, bool]:
    value = 0.1 + 0.2
    return value, math.isclose(value, 0.3)


if __name__ == "__main__":
    print("42 ->", int_to_binary(42))
    print("A utf8 ->", utf8_bytes("A"))
    print("가 utf8 ->", utf8_bytes("가"))
    print("0.1+0.2 ->", float_sum_issue())
