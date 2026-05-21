"""Generated from book-content article."""

from itertools import product


def expr_a(is_admin, is_member, has_paid):
    return is_admin or (is_member and has_paid)

def expr_b(is_admin, is_member, has_paid):
    return (is_admin or is_member) and (is_admin or has_paid)

rows = []
for a, m, p in product([False, True], repeat=3):
    rows.append((a, m, p, expr_a(a, m, p), expr_b(a, m, p)))

for r in rows:
    print(r, "OK" if r[3] == r[4] else "DIFF")
