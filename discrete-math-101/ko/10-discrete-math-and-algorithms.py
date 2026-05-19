"""Discrete Math 101 - Episode 10: Discrete math and algorithms."""

import heapq


def lis_length(nums):
    """Lis length."""
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(tails):
            tails.append(x)
        else:
            tails[lo] = x
    return len(tails)


def edit_distance(a, b):
    """Edit distance."""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c)
    return dp[-1][-1]


def dijkstra(adj, start):
    """Dijkstra."""
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d != dist.get(v):
            continue
        for u, w in adj.get(v, []):
            nd = d + w
            if nd < dist.get(u, float("inf")):
                dist[u] = nd
                heapq.heappush(pq, (nd, u))
    return dist


def count_grid_paths(m, n):
    """Count grid paths."""
    if m <= 0 or n <= 0:
        return 0
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]
