"""Secure Coding 101 - Episode 6: Secret management."""

from common import TOKEN_RE, assert_demo


def insecure_load_secret() -> str:
    """Insecure load secret."""
    return "hardcoded-secret"


def parse_env_text(text: str) -> dict:
    """Parse env text."""
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        result[k.strip()] = v.strip()
    return result


def safe_load_secret(env: dict, name: str) -> str:
    """Safe load secret."""
    value = env.get(name)
    if not value:
        raise ValueError("missing secret")
    return value


def sanitize_log(msg: str) -> str:
    """Sanitize log."""
    return TOKEN_RE.sub("token=[REDACTED]", msg)


def run_demo():
    """Run demo."""
    insecure_detected = insecure_load_secret() == "hardcoded-secret"
    env = parse_env_text("API_TOKEN=tok:abc123")
    safe_ok = safe_load_secret(env, "API_TOKEN") == "tok:abc123"
    safe_ok = safe_ok and "[REDACTED]" in sanitize_log("api token=abc")
    return assert_demo(insecure_detected, safe_ok)
