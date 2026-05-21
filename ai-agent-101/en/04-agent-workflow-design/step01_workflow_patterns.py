"""Ai Agent 101 - Episode 4: agent workflow design example."""


def run_workflow(task: str, confidence: float) -> dict[str, object]:
    """Run workflow."""
    steps: list[str] = ["plan"]
    if confidence < 0.5:
        steps.extend(["search_more", "review"])
    else:
        steps.append("execute")
    steps.append("finalize")
    return {"task": task, "steps": steps, "parallel_group": ["lint", "tests"]}


if __name__ == "__main__":
    print(run_workflow("write report", 0.4))
