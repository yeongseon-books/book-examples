"""Generated from book-content article."""

from datetime import datetime


def resolve_timeout(action_id: str, requested_at: datetime, now: datetime, timeout_sec: int = 600) -> dict:
    elapsed = (now - requested_at).total_seconds()
    if elapsed < timeout_sec:
        return {"status": "waiting"}

    return {
        "status": "timed_out",
        "decision": "reject",
        "reason": "정책상 허용된 응답 시간 안에 승인자가 응답하지 않았습니다.",
        "next_action": "escalate_or_cancel",
    }
