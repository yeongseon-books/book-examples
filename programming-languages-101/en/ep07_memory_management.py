def simulate_ref_count(edges: dict):
    counts = {k: 0 for k in edges}
    for refs in edges.values():
        for r in refs:
            counts[r] += 1
    return counts

def mark_and_sweep(edges: dict, roots: list):
    marked = set()
    stack = list(roots)
    while stack:
        n = stack.pop()
        if n in marked:
            continue
        marked.add(n)
        stack.extend(edges.get(n, []))
    return sorted(set(edges) - marked)
