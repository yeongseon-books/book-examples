"""Generated from book-content article."""

from datetime import datetime
from typing import Any


@dataclass
class TrajectoryStep:
    """A single step in a trajectory."""
    step_number: int
    action: str           # "think", "tool_call", "respond"
    input: Any
    output: Any
    timestamp: datetime
    duration_ms: int

@dataclass
class Trajectory:
    """The full path."""
    task_id: str
    steps: List[TrajectoryStep]
    final_answer: str
    success: bool

class TrajectoryRecorder:
    """Records trajectories."""

    def __init__(self, task_id: str):
        self.task_id = task_id
        self.steps: List[TrajectoryStep] = []
        self._step_counter = 0
