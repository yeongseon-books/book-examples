from common import truth_table


def implies(p, q):
    return (not p) or q


def and_op(p, q):
    return p and q


def sum_induction_identity(n):
    return sum(range(1, n + 1)) == n * (n + 1) // 2
