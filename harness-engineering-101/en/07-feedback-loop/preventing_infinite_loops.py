"""Generated from book-content article."""

from collections import Counter
from dataclasses import dataclass, field


@dataclass
class FeedbackLoop:
    """Manages the retry/reflect loop safely."""
    max_attempts: int = 5
    max_repetitions: int = 2
    attempts: int = 0
    failure_history: list[FailureClassification] = field(default_factory=list)

    def should_continue(self, latest: FailureClassification) -> bool:
        self.attempts += 1
        self.failure_history.append(latest)

        if self.attempts >= self.max_attempts:
            return False

        recent_modes = Counter(f.mode for f in self.failure_history[-3:])
        return not any(count >= self.max_repetitions + 1 for count in recent_modes.values())

    def escalate(self) -> dict:
        return {
            "status": "escalated",
            "attempts": self.attempts,
            "failure_history": [{"mode": f.mode.value, "feedback": f.feedback[:200]} for f in self.failure_history],
            "recommended_action": "human_review",
        }

def run_with_feedback(agent, task, loop: FeedbackLoop) -> dict:
    while True:
        try:
            return agent.run(task)
        except Exception as e:
            classification = classify_failure(e)
            if not loop.should_continue(classification):
                return loop.escalate()

            if classification.mode == FailureMode.TRANSIENT:
                import time
                time.sleep(classification.retry_after)
            elif classification.mode == FailureMode.REASONING:
                task = task.with_feedback(classification.feedback)
            else:
                return loop.escalate()
