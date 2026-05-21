"""Generated from book-content article."""

def is_tree(G):
    edges = sum(len(v) for v in G.values())
    return edges == len(G) - 1
