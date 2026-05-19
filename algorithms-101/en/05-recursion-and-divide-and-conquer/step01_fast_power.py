from __future__ import annotations


def fast_power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


def run() -> dict[str, int]:
    return {"base": 2, "exp": 30, "value": fast_power(2, 30)}


if __name__ == "__main__":
    print(run())
