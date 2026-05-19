PREREQUISITES = {
    "python-basics": [],
    "http-api": ["python-basics"],
    "database": ["python-basics"],
    "testing": ["python-basics"],
    "deployment": ["http-api", "database"],
}


def topo_order(prereqs: dict[str, list[str]]) -> list[str]:
    order: list[str] = []
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visited:
            return
        for dep in prereqs[node]:
            visit(dep)
        visited.add(node)
        order.append(node)

    for skill in prereqs:
        visit(skill)
    return order


def build_12_week_plan(
    target_role: str, weekly_hours: int, current_skills: set[str]
) -> list[dict]:
    tasks = [s for s in topo_order(PREREQUISITES) if s not in current_skills]
    weeks = []
    i = 0
    for week in range(1, 13):
        block = []
        used = 0
        while i < len(tasks) and used + 3 <= weekly_hours:
            block.append(tasks[i])
            used += 3
            i += 1
        weeks.append({"week": week, "role": target_role, "tasks": block, "hours": used})
    return weeks
