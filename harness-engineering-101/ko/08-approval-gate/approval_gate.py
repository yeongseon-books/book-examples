"""Generated from book-content article."""

from dataclasses import dataclass
from typing import Literal


@dataclass
class ApprovalRequest:
    action_id: str
    action_type: str
    summary: str
    risk_level: Literal["low", "medium", "high"]
    payload: dict

@dataclass
class ApprovalDecision:
    action_id: str
    decision: Literal["approve", "reject"]
    approver: str
    reason: str
