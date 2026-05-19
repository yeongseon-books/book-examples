"""Algorithms Python 101 - Episode 1: Dijkstra."""

import heapq


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    """Dijkstra."""
    dist: dict[str, int] = {start: 0}
    heap: list[tuple[int, str]] = [(0, start)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist.get(node, 10**18):
            continue
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist.get(neighbor, 10**18):
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return dist


if __name__ == "__main__":
    graph = {"A": [("B", 4), ("C", 2)], "B": [("D", 3)], "C": [("D", 10)], "D": []}
    print(dijkstra(graph, "A"))
