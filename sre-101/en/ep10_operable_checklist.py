CHECKS = ["logs", "metrics", "traces", "runbook", "dashboards", "alerts"]


def checklist_score(state: dict[str, bool]) -> tuple[int, float]:
    passed = sum(1 for k in CHECKS if state.get(k, False))
    return passed, passed / len(CHECKS)
