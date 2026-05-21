"""Generated from book-content article."""

from collections import deque


def bfs(graph, start):
    seen, q, order = {start}, deque([start]), []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in graph.get(v, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order

def dfs(graph, start):
    seen, stack, order = set(), [start], []
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
