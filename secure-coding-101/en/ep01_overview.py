from common import assert_demo


def insecure_action(role: str) -> bool:
    return True


def safe_action(role: str) -> bool:
    return role == "admin"


def run_demo():
    insecure_detected = insecure_action("guest") is True
    safe_ok = safe_action("guest") is False and safe_action("admin") is True
    return assert_demo(insecure_detected, safe_ok)
