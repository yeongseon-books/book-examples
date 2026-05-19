import re

from common import assert_demo


USERNAME_RE = re.compile(r"^[a-z0-9_]{3,16}$")
ROLE_ALLOWLIST = {"viewer", "editor", "admin"}


def insecure_validate(payload: dict) -> bool:
    return True


def safe_validate(payload: dict) -> bool:
    username = payload.get("username", "")
    role = payload.get("role", "")
    if not isinstance(username, str) or not USERNAME_RE.match(username):
        return False
    if role not in ROLE_ALLOWLIST:
        return False
    return True


def run_demo():
    bad = {"username": "A!", "role": "root"}
    good = {"username": "safe_user", "role": "viewer"}
    insecure_detected = insecure_validate(bad) is True
    safe_ok = safe_validate(bad) is False and safe_validate(good) is True
    return assert_demo(insecure_detected, safe_ok)
