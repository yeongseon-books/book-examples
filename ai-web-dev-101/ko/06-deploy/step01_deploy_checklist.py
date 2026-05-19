from __future__ import annotations


def deployment_checklist(
    has_requirements: bool, uses_env_var: bool, has_healthcheck: bool
) -> dict[str, object]:
    checks = {
        "dependencies": has_requirements,
        "secrets": uses_env_var,
        "healthcheck": has_healthcheck,
    }
    ready = all(checks.values())
    missing = [name for name, ok in checks.items() if not ok]
    return {"ready": ready, "missing": missing}


def estimate_monthly_cost(
    requests_per_day: int, avg_tokens: int, price_per_1k_tokens: float
) -> float:
    monthly_tokens = requests_per_day * 30 * avg_tokens
    return round((monthly_tokens / 1000) * price_per_1k_tokens, 4)
