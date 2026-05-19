"""Discrete Math 101 - Episode 9: Trees and graph traversal."""

# English runnable example
from collections import defaultdict, deque


def build_graph(edges, directed=False):
    """Build graph."""
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g


def bfs(g, start):
    """Bfs."""
    q = deque([start])
    seen, out = {start}, []
    while q:
        v = q.popleft()
        out.append(v)
        for u in g[v]:
            if u not in seen:
                seen.add(u)
                q.append(u)
    return out


def dfs_recursive(g, start, seen=None):
    """Dfs recursive."""
    seen = seen or set()
    seen.add(start)
    out = [start]
    for u in g[start]:
        if u not in seen:
            out.extend(dfs_recursive(g, u, seen))
    return out


def dfs_iterative(g, start):
    """Dfs iterative."""
    stack, seen, out = [start], set(), []
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
        stack.extend(reversed(g[v]))
    return out


def topo_sort(g):
    """Topo sort."""
    indeg = {v: 0 for v in g}
    for v in g:
        for u in g[v]:
            indeg[u] = indeg.get(u, 0) + 1
    q = deque([v for v, d in indeg.items() if d == 0])
    out = []
    while q:
        v = q.popleft()
        out.append(v)
        for u in g.get(v, []):
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    if len(out) != len(indeg):
        raise ValueError("cycle detected")
    return out


def connected_components(g):
    """Connected components."""
    seen = set()
    comps = []
    for v in g:
        if v in seen:
            continue
        comp = set(bfs(g, v))
        seen |= comp
        comps.append(comp)
    return comps
