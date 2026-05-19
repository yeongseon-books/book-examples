"""Secure Coding 101 - Episode 4: Authorization."""

from functools import wraps

from common import assert_demo


def insecure_delete(user: dict) -> bool:
    """Insecure delete."""
    return True


def require_role(role: str):
    """Require role."""

    def deco(fn):
        @wraps(fn)
        def wrapped(user: dict, *args, **kwargs):
            """Wrapped."""
            if user.get("role") != role:
                raise PermissionError("forbidden")
            return fn(user, *args, **kwargs)

        return wrapped

    return deco


@require_role("admin")
def safe_delete(user: dict) -> bool:
    """Safe delete."""
    return True


def run_demo():
    """Run demo."""
    insecure_detected = insecure_delete({"role": "viewer"}) is True
    ok = False
    denied = False
    try:
        safe_delete({"role": "viewer"})
    except PermissionError:
        denied = True
    ok = safe_delete({"role": "admin"})
    return assert_demo(insecure_detected, denied and ok)
