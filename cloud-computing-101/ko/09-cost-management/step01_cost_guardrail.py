"""Cloud Computing 101 - Episode 1: Cost guardrail."""

from __future__ import annotations


def record(service: str, action: str, **payload: object) -> dict[str, object]:
    """Record."""
    return {"ok": True, "service": service, "action": action, "payload": payload}


def cost_guardrail_plan(monthly_budget_usd: int) -> dict[str, object]:
    """Cost guardrail plan."""
    return record(
        "finops",
        "create_guardrail",
        budget_usd=monthly_budget_usd,
        alert_threshold_percent=80,
        required_tags=["Project", "Env", "Owner"],
    )
