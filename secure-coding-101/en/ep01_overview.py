"""Secure Coding 101 - Episode 1: Overview."""

from common import assert_demo


def insecure_action(role: str) -> bool:
    """Insecure action."""
    return True


def safe_action(role: str) -> bool:
    """Safe action."""
    return role == "admin"


def run_demo():
    """Run demo."""
    insecure_detected = insecure_action("guest") is True
    safe_ok = safe_action("guest") is False and safe_action("admin") is True
    return assert_demo(insecure_detected, safe_ok)
