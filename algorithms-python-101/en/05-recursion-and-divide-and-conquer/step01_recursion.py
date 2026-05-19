def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)


if __name__ == "__main__":
    print(power(2, 10))
