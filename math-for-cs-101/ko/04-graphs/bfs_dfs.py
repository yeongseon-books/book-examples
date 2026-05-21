"""Generated from book-content article."""

from collections import deque

def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    q = deque([start])
    seen = {start}
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph.get(v, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order

def dfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    stack = [start]
    seen = set()
    order = []
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        order.append(v)
        for nxt in reversed(graph.get(v, [])):
            if nxt not in seen:
                stack.append(nxt)
    return order
