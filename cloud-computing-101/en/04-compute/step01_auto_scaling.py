from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    return {'ok': True, 'service': service, 'action': action, 'payload': payload}


def compute_scale_plan(baseline_rps: int, peak_rps: int) -> dict[str, object]:
    min_instances = max(2, baseline_rps // 100)
    max_instances = max(min_instances, peak_rps // 80)
    return record('compute', 'autoscaling_plan', min_instances=min_instances, max_instances=max_instances)
