"""Ai Agent 101 - Episode 6: multi agent systems example."""


def supervisor(task: str) -> dict[str, str]:
    """Supervisor."""
    worker = "ResearchWorker" if "research" in task.lower() else "WriterWorker"
    return {"task": task, "worker": worker, "message": f"handoff to {worker}"}


if __name__ == "__main__":
    print(supervisor("Research FastAPI references"))
