"""Generated from book-content article."""

import itertools
import math

items = ['A', 'B', 'C', 'D']
perms = list(itertools.permutations(items, 2))
combs = list(itertools.combinations(items, 2))

assert len(perms) == math.perm(4, 2)
assert len(combs) == math.comb(4, 2)
