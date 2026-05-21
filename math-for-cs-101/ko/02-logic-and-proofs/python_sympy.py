"""Generated from book-content article."""

from sympy import symbols
from sympy.logic.boolalg import Equivalent, Implies
from sympy.logic.inference import satisfiable

p, q = symbols('p q')
claim = Equivalent(Implies(p, q), (~p) | q)
print("is tautology:", not satisfiable(~claim))
