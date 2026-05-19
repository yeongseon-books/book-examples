from __future__ import annotations


def build_hops() -> list[str]:
    return ["client", "dns", "frontend", "worker", "app"]


def diagnose_status(status_code: int, app_log_exists: bool) -> str:
    if status_code == 403:
        return "frontend_policy"
    if status_code == 502 and not app_log_exists:
        return "frontend_to_worker"
    if status_code == 504:
        return "timeout_or_dependency"
    return "app_or_dependency"
