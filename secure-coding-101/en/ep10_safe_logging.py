"""Secure Coding 101 - Episode 10: Safe logging."""

from common import EMAIL_RE, SSN_RE, TOKEN_RE, assert_demo


def insecure_log(message: str) -> str:
    """Insecure log."""
    return message


def sanitize(message: str) -> str:
    """Sanitize."""
    message = EMAIL_RE.sub("[EMAIL]", message)
    message = SSN_RE.sub("[SSN]", message)
    message = TOKEN_RE.sub("token=[REDACTED]", message)
    return message


def audit(event: str, actor: str, message: str) -> dict:
    """Audit."""
    return {"event": event, "actor": actor, "message": sanitize(message)}


def run_demo():
    """Run demo."""
    raw = "email=a@b.com ssn=123-45-6789 token=abc"
    insecure_detected = "123-45-6789" in insecure_log(raw)
    log = audit("login", "user-1", raw)
    safe_ok = (
        "[SSN]" in log["message"]
        and "[EMAIL]" in log["message"]
        and "[REDACTED]" in log["message"]
    )
    return assert_demo(insecure_detected, safe_ok)
