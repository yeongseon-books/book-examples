"""Discrete Math 101 - Episode 2: Propositions and logic."""

# English runnable example
from common import bool_table


def evaluate(p, q):
    """Evaluate."""
    return p and (not q)


def tautology(func, variables):
    """Tautology."""
    return all(result for _, result in bool_table(variables, func))


def contradiction(func, variables):
    """Contradiction."""
    return all(not result for _, result in bool_table(variables, func))


def equivalent(f, g, variables):
    """Equivalent."""
    rows_f = bool_table(variables, f)
    rows_g = bool_table(variables, g)
    return all(a[1] == b[1] for a, b in zip(rows_f, rows_g, strict=False))


if __name__ == "__main__":
    print(tautology(lambda p: True, ["p"]))
