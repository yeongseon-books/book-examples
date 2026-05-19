from __future__ import annotations

import struct


def int_to_binary(value: int, width: int = 8) -> str:
    return format(value & ((1 << width) - 1), f"0{width}b")


def int_to_hex(value: int) -> str:
    return hex(value)


def to_twos_complement(value: int, width: int = 8) -> str:
    return int_to_binary(value, width)


def decompose_float64(value: float) -> tuple[int, int, int]:
    bits = int.from_bytes(struct.pack(">d", value), "big")
    sign = (bits >> 63) & 1
    exponent = (bits >> 52) & 0x7FF
    mantissa = bits & ((1 << 52) - 1)
    return sign, exponent, mantissa


if __name__ == "__main__":
    print(int_to_binary(-5, 8))
    print(int_to_hex(255))
    print(decompose_float64(0.1))
