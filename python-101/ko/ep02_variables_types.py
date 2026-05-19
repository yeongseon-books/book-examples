def calculate_basics(a: int, b: int) -> dict[str, float | int | bool]:
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b,
        "is_a_greater": a > b,
    }


def main() -> None:
    age = 20
    height = 170.5
    name = "민수"
    is_student = True
    print(age, type(age))
    print(height, type(height))
    print(name, type(name))
    print(is_student, type(is_student))
    print(calculate_basics(10, 3))


if __name__ == "__main__":
    main()
