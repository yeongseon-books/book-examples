"""Episode 04: linear/branching/parallel 워크플로 예제입니다."""


def run_workflow(task: str, confidence: float) -> dict[str, object]:
    steps: list[str] = ["plan"]
    if confidence < 0.5:
        steps.extend(["search_more", "review"])
    else:
        steps.append("execute")
    steps.append("finalize")
    return {"task": task, "steps": steps, "parallel_group": ["lint", "tests"]}


if __name__ == "__main__":
    print(run_workflow("보고서 작성", 0.4))
