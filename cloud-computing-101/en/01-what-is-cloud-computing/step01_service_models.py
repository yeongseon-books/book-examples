"""Cloud Computing 101 - Episode 1: Service models."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def classify_service_model(
    workload: str, manages_os: bool, manages_runtime: bool
) -> dict[str, object]:
    """Classify service model."""
    if manages_os and manages_runtime:
        model = "IaaS"
    elif not manages_os and manages_runtime:
        model = "PaaS"
    else:
        model = "SaaS"
    return record("catalog", "classify_model", workload=workload, model=model)
