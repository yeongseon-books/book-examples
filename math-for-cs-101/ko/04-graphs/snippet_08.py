"""Generated from book-content article."""

def problem_type(weighted: bool, negative_edge: bool, reachability_only: bool) -> str:
    if reachability_only:
        return 'BFS/DFS'
    if weighted and negative_edge:
        return 'Bellman-Ford 계열'
    if weighted:
        return 'Dijkstra 계열'
    return 'BFS 최단간선수'
