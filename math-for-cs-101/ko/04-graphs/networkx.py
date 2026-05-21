"""Generated from book-content article."""

import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ('auth', 'user-db'),
    ('api', 'auth'),
    ('api', 'cache'),
    ('worker', 'queue'),
    ('queue', 'api'),
])

is_dag = nx.is_directed_acyclic_graph(G)
