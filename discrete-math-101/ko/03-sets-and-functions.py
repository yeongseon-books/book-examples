from itertools import combinations


def power_set(s):
    items = list(s)
    return [set(c) for r in range(len(items) + 1) for c in combinations(items, r)]


class Function:
    def __init__(self, domain, codomain, rule):
        self.domain = set(domain)
        self.codomain = set(codomain)
        self.rule = rule

    def image(self):
        out = {self.rule(x) for x in self.domain}
        if not out <= self.codomain:
            raise ValueError("range must be subset of codomain")
        return out

    def is_injective(self):
        vals = [self.rule(x) for x in self.domain]
        return len(vals) == len(set(vals))

    def is_surjective(self):
        return self.image() == self.codomain

    def is_bijective(self):
        return self.is_injective() and self.is_surjective()
