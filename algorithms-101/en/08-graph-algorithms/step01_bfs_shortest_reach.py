"""Algorithms 101 - Episode 1: Bfs shortest reach."""

from __future__ import annotations

from collections import defaultdict, deque


def bfs_dist(n: int, edges: list[tuple[int, int]], start: int) -> dict[int, int]:
    """Bfs dist."""
    adj: dict[int, list[int]] = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    dist: dict[int, int] = {start: 0}
    q: deque[int] = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def run() -> dict[str, object]:
    """Run."""
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    return {"dist": bfs_dist(5, edges, 0)}


if __name__ == "__main__":
    print(run())
