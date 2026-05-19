from functools import wraps

from common import assert_demo


def insecure_delete(user: dict) -> bool:
    return True


def require_role(role: str):
    def deco(fn):
        @wraps(fn)
        def wrapped(user: dict, *args, **kwargs):
            if user.get("role") != role:
                raise PermissionError("forbidden")
            return fn(user, *args, **kwargs)

        return wrapped

    return deco


@require_role("admin")
def safe_delete(user: dict) -> bool:
    return True


def run_demo():
    insecure_detected = insecure_delete({"role": "viewer"}) is True
    ok = False
    denied = False
    try:
        safe_delete({"role": "viewer"})
    except PermissionError:
        denied = True
    ok = safe_delete({"role": "admin"})
    return assert_demo(insecure_detected, denied and ok)
