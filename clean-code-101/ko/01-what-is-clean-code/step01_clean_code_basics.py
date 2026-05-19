"""Clean Code 101 - Episode 1: Clean code basics."""


def total_with_tax(amount: int, tax_rate: float) -> float:
    """Total with tax."""
    return amount * (1 + tax_rate)


def readability_signals(
    function_lines: int, arg_count: int, nesting_depth: int
) -> dict[str, bool]:
    """Readability signals."""
    return {
        "short_function": function_lines <= 20,
        "small_args": arg_count <= 3,
        "shallow_nesting": nesting_depth <= 3,
    }
