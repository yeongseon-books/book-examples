from __future__ import annotations

from collections import defaultdict, deque


ROLE_TOPICS = {
    "analyst": ["sql_basics", "analytics_sql", "dashboard", "ab_test", "storytelling"],
    "scientist": [
        "python_basics",
        "statistics",
        "ml_basics",
        "feature_engineering",
        "model_eval",
    ],
    "engineer": [
        "python_basics",
        "sql_basics",
        "etl",
        "data_modeling",
        "orchestration",
    ],
}

PREREQS = {
    "analytics_sql": ["sql_basics"],
    "dashboard": ["analytics_sql"],
    "ab_test": ["statistics"],
    "ml_basics": ["statistics", "python_basics"],
    "feature_engineering": ["ml_basics"],
    "model_eval": ["ml_basics"],
    "etl": ["python_basics", "sql_basics"],
    "data_modeling": ["sql_basics"],
    "orchestration": ["etl"],
}


def topo_sort(topics: list[str]) -> list[str]:
    indegree = {topic: 0 for topic in topics}
    graph = defaultdict(list)
    for topic in topics:
        for pre in PREREQS.get(topic, []):
            if pre in indegree:
                graph[pre].append(topic)
                indegree[topic] += 1
    queue = deque(sorted([topic for topic, deg in indegree.items() if deg == 0]))
    order: list[str] = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for nxt in graph[current]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order


def generate_12_week_plan(
    target_role: str, weekly_hours: int, current_skills: set[str]
) -> list[dict[str, object]]:
    topics = ROLE_TOPICS[target_role]
    ordered = [topic for topic in topo_sort(topics) if topic not in current_skills]
    if not ordered:
        ordered = topics[:]
    hours_per_topic = max(2, weekly_hours // max(1, len(ordered)))
    plan = []
    for week in range(1, 13):
        topic = ordered[(week - 1) % len(ordered)]
        plan.append({"week": week, "topic": topic, "hours": hours_per_topic})
    return plan
