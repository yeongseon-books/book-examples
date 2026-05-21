"""Generated from book-content article."""

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re

BLOCKED_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"system\s+prompt\s+leak",
]

@dataclass
class GuardDecision:
    allowed: bool
    stage: str
    reason: str | None = None

def input_guardrail(text: str) -> GuardDecision:
    if len(text) > 2_000:
        return GuardDecision(False, "pre-input", "input_too_long")
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return GuardDecision(False, "pre-input", "prompt_injection_pattern")
    return GuardDecision(True, "pre-input")

def output_guardrail(text: str) -> GuardDecision:
    if re.search(r"\b\d{3}-\d{2}-\d{4}\b", text):
        return GuardDecision(False, "post-output", "pii_detected")
    return GuardDecision(True, "post-output")

def log_decision(request_id: str, decision: GuardDecision) -> None:
    print(json.dumps({
        "request_id": request_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": decision.stage,
        "allowed": decision.allowed,
        "reason": decision.reason,
    }))
