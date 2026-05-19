"""Computer Science Major 101 - Episode 1: What cs majors learn."""

from collections import deque


def topological_curriculum_order(prerequisites: dict[str, list[str]]) -> list[str]:
    """Topological curriculum order."""
    indegree: dict[str, int] = {node: 0 for node in prerequisites}
    graph: dict[str, list[str]] = {node: [] for node in prerequisites}
    for course, needs in prerequisites.items():
        for pre in needs:
            if pre not in graph:
                graph[pre] = []
            if pre not in indegree:
                indegree[pre] = 0
            graph[pre].append(course)
            indegree[course] = indegree.get(course, 0) + 1

    queue = deque(sorted(node for node, deg in indegree.items() if deg == 0))
    order: list[str] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, []):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(indegree):
        raise ValueError("Cycle detected in prerequisite graph")
    return order


if __name__ == "__main__":
    curriculum = {
        "math": [],
        "programming": ["math"],
        "systems": ["programming"],
        "data": ["programming"],
        "ai": ["data", "math"],
        "project": ["systems", "data", "ai"],
    }
    print(topological_curriculum_order(curriculum))
