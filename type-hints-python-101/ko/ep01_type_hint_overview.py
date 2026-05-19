"""Type Hints Python 101 - Episode 1: Type hint overview."""


def add(a: int, b: int) -> int:
    """Add."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be int")
    return a + b
