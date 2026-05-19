"""Discrete Math 101 - Episode 3: Sets and functions."""

# English runnable example
from itertools import combinations


def power_set(s):
    """Power set."""
    items = list(s)
    return [set(c) for r in range(len(items) + 1) for c in combinations(items, r)]


class Function:
    """Function."""

    def __init__(self, domain, codomain, rule):
        self.domain = set(domain)
        self.codomain = set(codomain)
        self.rule = rule

    def image(self):
        """Image."""
        out = {self.rule(x) for x in self.domain}
        if not out <= self.codomain:
            raise ValueError("range must be subset of codomain")
        return out

    def is_injective(self):
        """Is injective."""
        vals = [self.rule(x) for x in self.domain]
        return len(vals) == len(set(vals))

    def is_surjective(self):
        """Is surjective."""
        return self.image() == self.codomain

    def is_bijective(self):
        """Is bijective."""
        return self.is_injective() and self.is_surjective()
