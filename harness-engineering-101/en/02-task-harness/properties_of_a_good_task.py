"""Generated from book-content article."""

from collections.abc import Callable

class VerifiableTask(TaskSpec):
    """Task with executable completion criteria."""
    verifier: Callable[[Any], bool] = Field(..., exclude=True)

    def verify(self, output: Any) -> bool:
        """Verify the output."""
        return self.verifier(output)

def verify_report(output: dict) -> bool:
    """Verifier for the daily summary report."""
    required_sections = ["summary", "metrics", "anomalies", "next_actions"]
    return (
        all(section in output for section in required_sections)
        and isinstance(output.get("metrics"), dict)
        and len(output.get("anomalies", [])) >= 0
    )

task = VerifiableTask(
    goal="Generate the daily summary report",
    inputs={"date": "2026-05-03"},
    outputs={"format": "json"},
    completion_criteria=[
        "Required sections are present",
        "metrics is a dict",
        "anomalies field exists",
    ],
    verifier=verify_report,
)

# Verify the agent's output
result = {"summary": "...", "metrics": {}, "anomalies": [], "next_actions": []}
assert task.verify(result)
