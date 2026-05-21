"""Generated from book-content article."""

from typing import Dict, Set

import networkx as nx


def decompose_with_dependencies(
    tasks: List[str],
    dependencies: dict[str, List[str]]
) -> List[str]:
    """Dependency-based task ordering"""

    # Create DAG (Directed Acyclic Graph)
    graph = nx.DiGraph()
    graph.add_nodes_from(tasks)

    for task, deps in dependencies.items():
        for dep in deps:
            graph.add_edge(dep, task)  # dep → task

    # Topological sort for execution order
    execution_order = list(nx.topological_sort(graph))

    return execution_order

# Example
tasks = ["Collect data", "Clean data", "Analyze", "Visualize", "Write report"]

dependencies = {
    "Clean data": ["Collect data"],
    "Analyze": ["Clean data"],
    "Visualize": ["Analyze"],
    "Write report": ["Visualize", "Analyze"]
}

order = decompose_with_dependencies(tasks, dependencies)
# Result: ['Collect data', 'Clean data', 'Analyze', 'Visualize', 'Write report']
