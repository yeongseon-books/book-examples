"""Generated from book-content article."""

import sympy as sp

p, q, r = sp.symbols('p q r')
expr1 = sp.Implies(p, sp.And(q, r))
expr2 = sp.And(sp.Implies(p, q), sp.Implies(p, r))
is_equiv = sp.simplify_logic(sp.Equivalent(expr1, expr2))
