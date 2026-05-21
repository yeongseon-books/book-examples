"""Generated from book-content article."""

def to_adj_list(edges):
    g = {}
    for u, v in edges:
        g.setdefault(u, []).append(v)
        g.setdefault(v, [])
    return g

def to_adj_matrix(nodes, edges):
    idx = {n: i for i, n in enumerate(nodes)}
    n = len(nodes)
    m = [[0] * n for _ in range(n)]
    for u, v in edges:
        m[idx[u]][idx[v]] = 1
    return m
