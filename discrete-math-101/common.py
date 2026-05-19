"""Shared utilities and domain models for Discrete Math 101."""

from __future__ import annotations

from collections import deque
from itertools import product


class UnionFind:
    """Union find."""

    def __init__(self, items):
        self.parent = {x: x for x in items}
        self.rank = {x: 0 for x in items}

    def find(self, x):
        """Find."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        """Union."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def bool_table(variables, func):
    """Bool table."""
    rows = []
    for vals in product([False, True], repeat=len(variables)):
        env = dict(zip(variables, vals, strict=False))
        rows.append((env, func(**env)))
    return rows


def is_bipartite(adj):
    """Is bipartite."""
    color = {}
    for s in adj:
        if s in color:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if u not in color:
                    color[u] = 1 - color[v]
                    q.append(u)
                elif color[u] == color[v]:
                    return False
    return True
