"""Episode 06: supervisor와 worker handoff 예제입니다."""


def supervisor(task: str) -> dict[str, str]:
    worker = (
        "ResearchWorker"
        if "조사" in task or "research" in task.lower()
        else "WriterWorker"
    )
    return {"task": task, "worker": worker, "message": f"handoff to {worker}"}


if __name__ == "__main__":
    print(supervisor("FastAPI 자료 조사"))
