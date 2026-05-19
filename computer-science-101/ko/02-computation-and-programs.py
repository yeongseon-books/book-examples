"""에피소드 02: 같은 계산의 세 가지 표현"""


def sum_of_squares_imperative(n: int) -> int:
    """Sum of squares imperative."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def sum_of_squares_recursive(n: int) -> int:
    """Sum of squares recursive."""
    if n < 0:
        raise ValueError("negative input not supported")
    if n == 0:
        return 0
    return n * n + sum_of_squares_recursive(n - 1)


def sum_of_squares_functional(n: int) -> int:
    """Sum of squares functional."""
    return sum(map(lambda x: x * x, range(1, n + 1)))


if __name__ == "__main__":
    n = 10
    print(sum_of_squares_imperative(n))
    print(sum_of_squares_recursive(n))
    print(sum_of_squares_functional(n))
