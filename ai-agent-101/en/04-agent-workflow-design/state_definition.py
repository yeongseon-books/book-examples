"""Generated from book-content article."""

from typing import Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class AgentState:
    """Agent state definition"""
    task_id: str                        # Unique task ID
    goal: str                           # Final goal
    current_step: int                   # Current step number
    completed_steps: List[Dict]         # Completed steps
    pending_steps: List[str]            # Remaining steps
    context: Dict[str, Any]            # Accumulated information
    status: str                         # pending/running/completed/failed
    created_at: datetime
    updated_at: datetime
    
    def to_dict(self) -> Dict[str, Any]:
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
