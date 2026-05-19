def fizzbuzz(n: int) -> list[str]:
    out: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def main() -> None:
    print(fizzbuzz(20))
    x = 0
    while x < 3:
        x += 1
        if x == 2:
            continue
        print("while:", x)


if __name__ == "__main__":
    main()
