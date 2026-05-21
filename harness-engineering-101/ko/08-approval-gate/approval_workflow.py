"""Generated from book-content article."""

import uuid
from datetime import datetime, timezone


class ApprovalWorkflow:
    def __init__(self, store, notifier):
        self.store = store
        self.notifier = notifier

    def request(self, action_type: str, summary: str, payload: dict, risk: str) -> str:
        action_id = str(uuid.uuid4())
        req = ApprovalRequest(
            action_id=action_id,
            action_type=action_type,
            summary=summary,
            risk_level=risk,
            payload=payload,
        )
        self.store.save_request(req, created_at=datetime.now(timezone.utc))
        self.notifier.notify(req)
        return action_id

    def wait(self, action_id: str, timeout_sec: int = 600) -> ApprovalDecision | None:
        return self.store.wait_for_decision(action_id, timeout_sec)

    def execute_if_approved(self, action_id: str, executor):
        decision = self.store.get_decision(action_id)
        if decision is None:
            return {"status": "pending"}
        if decision.decision == "reject":
            return {"status": "rejected", "reason": decision.reason}
        result = executor()
        self.store.mark_executed(action_id, result)
        return {"status": "executed", "result": result}
