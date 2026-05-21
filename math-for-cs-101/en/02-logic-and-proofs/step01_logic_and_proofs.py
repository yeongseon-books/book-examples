"""Math For Cs 101 - Episode 2: logic and proofs example."""


def implies(p, q):
    """Implies."""
    return (not p) or q


def and_op(p, q):
    """And op."""
    return p and q


def sum_induction_identity(n):
    """Sum induction identity."""
    return sum(range(1, n + 1)) == n * (n + 1) // 2
