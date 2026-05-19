"""Algorithms Python 101 - Episode 1: Graph traversal."""

from collections import deque


def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """Bfs."""
    visited = {start}
    queue = deque([start])
    order: list[str] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


if __name__ == "__main__":
    sample = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
    print(bfs(sample, "A"))
