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

    def record(self, action: str, input_data: Any, output_data: Any, duration_ms: int):
        self._step_counter += 1
        self.steps.append(TrajectoryStep(
            step_number=self._step_counter,
            action=action,
            input=input_data,
            output=output_data,
            timestamp=datetime.now(),
            duration_ms=duration_ms
        ))

    def finalize(self, final_answer: str, success: bool) -> Trajectory:
        return Trajectory(
            task_id=self.task_id,
            steps=self.steps,
            final_answer=final_answer,
            success=success
        )
