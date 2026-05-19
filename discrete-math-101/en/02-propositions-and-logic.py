# English runnable example
from common import bool_table


def evaluate(p, q):
    return p and (not q)


def tautology(func, variables):
    return all(result for _, result in bool_table(variables, func))


def contradiction(func, variables):
    return all(not result for _, result in bool_table(variables, func))


def equivalent(f, g, variables):
    rows_f = bool_table(variables, f)
    rows_g = bool_table(variables, g)
    return all(a[1] == b[1] for a, b in zip(rows_f, rows_g))


if __name__ == '__main__':
    print(tautology(lambda p: p or (not p), ['p']))
