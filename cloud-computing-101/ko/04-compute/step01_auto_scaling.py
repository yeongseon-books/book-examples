"""Cloud Computing 101 - Episode 1: Auto scaling."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def compute_scale_plan(baseline_rps: int, peak_rps: int) -> dict[str, object]:
    """Compute scale plan."""
    min_instances = max(2, baseline_rps // 100)
    max_instances = max(min_instances, peak_rps // 80)
    return record(
        "compute",
        "autoscaling_plan",
        min_instances=min_instances,
        max_instances=max_instances,
    )
