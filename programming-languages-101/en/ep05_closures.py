"""Programming Languages 101 - Episode 5: Closures."""


def make_counter(start: int = 0):
    """Make counter."""
    value = start

    def inc():
        """Inc."""
        nonlocal value
        value += 1
        return value

    return inc


def partial_add(x: int):
    """Partial add."""
    return lambda y: x + y
