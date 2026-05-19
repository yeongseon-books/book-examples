"""Azure App Service 101 - Episode 1: Hosting decision."""

from __future__ import annotations


def choose_hosting_model(
    *, needs_windows_dependency: bool, needs_os_control: bool
) -> str:
    """Choose hosting model."""
    if needs_windows_dependency:
        return "windows-code"
    if needs_os_control:
        return "linux-container"
    return "linux-code"


def estimate_plan_strategy(app_count: int, isolation_required: bool) -> str:
    """Estimate plan strategy."""
    if isolation_required:
        return "separate-plans"
    return "shared-plan" if app_count > 1 else "single-plan"
