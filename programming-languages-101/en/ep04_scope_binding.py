"""Programming Languages 101 - Episode 4: Scope binding."""


def lexical_scope(x: int):
    """Lexical scope."""

    def inner(y: int) -> int:
        """Inner."""
        return x + y

    return inner


def dynamic_scope(func, env: dict, y: int) -> int:
    """Dynamic scope."""
    return func(env, y)


def dyn_add(env: dict, y: int) -> int:
    """Dyn add."""
    return env["x"] + y
