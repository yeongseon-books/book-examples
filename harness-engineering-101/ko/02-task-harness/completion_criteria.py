"""Generated from book-content article."""

class TaskCandidate(BaseModel):
    """Candidate task — incomplete spec."""
    description: str
    missing_fields: list[str] = []

    def to_spec(self, **filled) -> TaskSpec | None:
        """Convert to a TaskSpec. Returns None if fields are missing."""
        if self.missing_fields:
            return None
        return TaskSpec(**filled)

def request_to_tasks(request: str) -> list[TaskCandidate]:
    """Convert a vague request into task candidates."""
    # In production this is built with LLM + templates.
    return [
        TaskCandidate(
            description="Send a weekly retrospective summary",
            missing_fields=["recipient", "data_source"],
        ),
        TaskCandidate(
            description="Visualize the meeting load",
            missing_fields=["chart_type", "time_range"],
        ),
    ]

# Workflow
candidates = request_to_tasks("Do something about productivity")
for c in candidates:
    if c.missing_fields:
        print(f"Need clarification: {c.description}")
        print(f"  Missing fields: {c.missing_fields}")
