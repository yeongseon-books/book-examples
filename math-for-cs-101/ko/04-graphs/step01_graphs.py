"""Math For Cs 101 - Episode 1: Graphs."""


def has_cycle_directed(graph):
    """Has cycle directed."""
    color = {node: 0 for node in graph}

    def visit(node):
        """Visit."""
        color[node] = 1
        for nxt in graph.get(node, []):
            if color[nxt] == 1:
                return True
            if color[nxt] == 0 and visit(nxt):
                return True
        color[node] = 2
        return False

    return any(visit(node) for node in graph if color[node] == 0)
