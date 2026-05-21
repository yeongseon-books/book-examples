"""Generated from book-content article."""

def resolve_timeout(action_id: str, requested_at, now, timeout_sec: int = 600) -> dict:
    elapsed = (now - requested_at).total_seconds()
    if elapsed < timeout_sec:
        return {"status": "waiting"}
    return {
        "status": "timed_out",
        "decision": "reject",
        "reason": "No approver responded within the policy window.",
        "next_action": "escalate_or_cancel",
    }
