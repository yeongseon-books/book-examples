"""Azure Aks Deep Dive - Episode 1: Scheduler decision."""

from __future__ import annotations

from typing import TypedDict


class Node(TypedDict):
    """Node."""

    name: str
    free_cpu: int
    pod_count: int
    tainted: bool


def filter_nodes(nodes: list[Node], cpu_request: int) -> list[Node]:
    """Filter nodes."""
    return [
        n for n in nodes if n["free_cpu"] >= cpu_request and not n.get("tainted", False)
    ]


def score_nodes(nodes: list[Node]) -> list[Node]:
    """Score nodes."""
    return sorted(
        nodes, key=lambda n: n["free_cpu"] - n["pod_count"] * 10, reverse=True
    )


def choose_node(nodes: list[Node], cpu_request: int) -> str | None:
    """Choose node."""
    feasible = filter_nodes(nodes, cpu_request)
    if not feasible:
        return None
    return score_nodes(feasible)[0]["name"]
