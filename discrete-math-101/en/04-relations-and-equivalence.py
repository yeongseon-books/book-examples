# English runnable example
from common import UnionFind


class Relation:
    def __init__(self, universe, pairs):
        self.universe = set(universe)
        self.pairs = set(pairs)

    def is_reflexive(self):
        return all((x, x) in self.pairs for x in self.universe)

    def is_symmetric(self):
        return all((b, a) in self.pairs for a, b in self.pairs)

    def is_transitive(self):
        return all(
            (a, c) in self.pairs for a, b in self.pairs for x, c in self.pairs if b == x
        )

    def equivalence_classes(self):
        uf = UnionFind(self.universe)
        for a, b in self.pairs:
            uf.union(a, b)
        groups = {}
        for x in self.universe:
            groups.setdefault(uf.find(x), set()).add(x)
        return list(groups.values())
