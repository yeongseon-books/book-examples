from common import StructuredLogger


def run_demo() -> str:
    log = StructuredLogger(sample_rate=1.0).with_context(service="auth")
    log.log("ERROR", "login_failed", user_id="42", reason="bad_password")
    return log.lines[0]
