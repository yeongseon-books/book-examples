"""Generated from book-content article."""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class AgentState:
    """Agent state definition"""
    task_id: str                        # Unique task ID
    goal: str                           # Final goal
    current_step: int                   # Current step number
    completed_steps: list[dict]         # Completed steps
    pending_steps: list[str]            # Remaining steps
    context: dict[str, Any]            # Accumulated information
    status: str                         # pending/running/completed/failed
    created_at: datetime
    updated_at: datetime

    def to_dict(self) -> dict[str, Any]:
        """Serialize state to dictionary"""
        return {
            "task_id": self.task_id,
            "goal": self.goal,
            "current_step": self.current_step,
            "completed_steps": self.completed_steps,
            "pending_steps": self.pending_steps,
            "context": self.context,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
