"""Cloud Computing 101 - Episode 1: Shared responsibility."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def shared_responsibility(model: str) -> dict[str, object]:
    """Shared responsibility."""
    managed_by_customer = {
        "IaaS": ["app", "runtime", "os"],
        "PaaS": ["app"],
        "SaaS": [],
    }[model]
    return record(
        "governance",
        "responsibility_matrix",
        model=model,
        customer_scope=managed_by_customer,
    )
