"""Generated from book-content article."""

from enum import Enum


class WorkflowState(Enum):
    """Workflow states"""
    IDLE = "idle"
    PLANNING = "planning"
    EXECUTING = "executing"
    EVALUATING = "evaluating"
    COMPLETED = "completed"
    FAILED = "failed"

class StateMachine:
    """State machine"""

    TRANSITIONS = {
        WorkflowState.IDLE: [WorkflowState.PLANNING],
        WorkflowState.PLANNING: [WorkflowState.EXECUTING, WorkflowState.FAILED],
        WorkflowState.EXECUTING: [WorkflowState.EVALUATING, WorkflowState.FAILED],
        WorkflowState.EVALUATING: [WorkflowState.COMPLETED, WorkflowState.PLANNING, WorkflowState.FAILED],
        WorkflowState.COMPLETED: [],
        WorkflowState.FAILED: []
    }

    def __init__(self, initial_state: WorkflowState = WorkflowState.IDLE):
        self.current_state = initial_state
        self.state_history = [initial_state]

    def transition(self, next_state: WorkflowState) -> bool:
        """Transition state"""
        if next_state not in self.TRANSITIONS[self.current_state]:
            print(f"Invalid transition: {self.current_state} → {next_state}")
            return False

        print(f"State transition: {self.current_state.value} → {next_state.value}")
        self.current_state = next_state
        self.state_history.append(next_state)
        return True

    def can_transition(self, next_state: WorkflowState) -> bool:
        """Check if transition is possible"""
        return next_state in self.TRANSITIONS[self.current_state]

# Usage example
state_machine = StateMachine()

state_machine.transition(WorkflowState.PLANNING)     # IDLE → PLANNING (OK)
state_machine.transition(WorkflowState.EXECUTING)    # PLANNING → EXECUTING (OK)
state_machine.transition(WorkflowState.EVALUATING)   # EXECUTING → EVALUATING (OK)
state_machine.transition(WorkflowState.PLANNING)     # EVALUATING → PLANNING (replan, OK)
