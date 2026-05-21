"""Generated from book-content article."""

def proposition_even_sum(a: int, b: int) -> bool:
    if a % 2 == 0 and b % 2 == 0:
        return (a + b) % 2 == 0
    return True
