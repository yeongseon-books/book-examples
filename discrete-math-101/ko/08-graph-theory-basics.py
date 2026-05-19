"""Discrete Math 101 - Episode 8: Graph theory basics."""

from collections import defaultdict

from common import is_bipartite


class Graph:
    """Graph."""

    def __init__(self):
        self.adj = defaultdict(set)

    def add_edge(self, u, v):
        """Add edge."""
        self.adj[u].add(v)
        self.adj[v].add(u)

    def degree(self, v):
        """Degree."""
        return len(self.adj[v])

    def has_cycle(self):
        """Has cycle."""
        seen = set()

        def dfs(v, p):
            """Dfs."""
            seen.add(v)
            for u in self.adj[v]:
                if u == p:
                    continue
                if u in seen or dfs(u, v):
                    return True
            return False

        return any(dfs(v, None) for v in list(self.adj) if v not in seen)

    def is_bipartite(self):
        """Is bipartite."""
        return is_bipartite(self.adj)
