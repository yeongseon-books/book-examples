import heapq
import math
import random
from collections import deque


def truth_table(op):
    rows = []
    for p in (False, True):
        for q in (False, True):
            rows.append((p, q, op(p, q)))
    return rows


def is_injective(mapping):
    values = list(mapping.values())
    return len(values) == len(set(values))


def bfs(graph, start):
    visited = set([start])
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return order


def dfs(graph, start):
    visited = set()
    order = []

    def _visit(node):
        visited.add(node)
        order.append(node)
        for nxt in graph.get(node, []):
            if nxt not in visited:
                _visit(nxt)

    _visit(start)
    return order


def monte_carlo_estimate(fn, sampler, n, seed=42):
    rnd = random.Random(seed)
    total = 0.0
    for _ in range(n):
        total += fn(sampler(rnd))
    return total / n


def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def gradient_descent(grad, x0, lr=0.1, steps=100):
    x = float(x0)
    for _ in range(steps):
        x = x - lr * grad(x)
    return x


def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)


def kl_divergence(p, q):
    return sum(
        pi * math.log2(pi / qi)
        for pi, qi in zip(p, q, strict=False)
        if pi > 0 and qi > 0
    )


def gcd(a, b):
    x, y = abs(a), abs(b)
    while y:
        x, y = y, x % y
    return x


def fast_power(base, exp, mod=None):
    if exp < 0:
        raise ValueError("exp must be non-negative")
    result = 1
    b = base if mod is None else base % mod
    e = exp
    while e > 0:
        if e & 1:
            result = result * b if mod is None else (result * b) % mod
        b = b * b if mod is None else (b * b) % mod
        e >>= 1
    return result


def huffman_code_lengths(freqs):
    heap = [(w, {sym: 0}) for sym, w in freqs.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        only = heap[0][1]
        return {k: 1 for k in only}
    while len(heap) > 1:
        w1, c1 = heapq.heappop(heap)
        w2, c2 = heapq.heappop(heap)
        merged = {}
        for k, v in c1.items():
            merged[k] = v + 1
        for k, v in c2.items():
            merged[k] = v + 1
        heapq.heappush(heap, (w1 + w2, merged))
    return heap[0][1]
