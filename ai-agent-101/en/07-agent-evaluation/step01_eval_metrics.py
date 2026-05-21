"""Ai Agent 101 - Episode 7: agent evaluation example."""


def evaluate(results: list[dict[str, object]]) -> dict[str, float]:
    """Evaluate."""
    total = len(results)
    success = sum(1 for r in results if r.get("success") is True)
    step_values: list[int] = []
    for result in results:
        value = result.get("steps", 0)
        step_values.append(value if isinstance(value, int) else 0)
    avg_steps = sum(step_values) / total if total else 0.0
    return {"success_rate": success / total if total else 0.0, "avg_steps": avg_steps}


if __name__ == "__main__":
    sample = [{"success": True, "steps": 3}, {"success": False, "steps": 6}]
    print(evaluate(sample))
