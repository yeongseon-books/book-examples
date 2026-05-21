"""Generated from book-content article."""

from typing import Any

from pydantic import BaseModel, Field


class TaskSpec(BaseModel):
    """Specification for an executable task."""
    goal: str = Field(..., description="Goal to achieve (one sentence)")
    inputs: dict[str, Any] = Field(..., description="Input data and resources")
    outputs: dict[str, Any] = Field(..., description="Output format and location")
    completion_criteria: list[str] = Field(
        ...,
        description="Conditions to verify completion (automatable)",
    )

    def is_executable(self) -> bool:
        """Check whether the task is executable."""
        return bool(
            self.goal
            and self.inputs
            and self.outputs
            and self.completion_criteria
        )

# 예시: a clear task
task = TaskSpec(
    goal="Generate a daily summary report from sales data for the past 7 days",
    inputs={
        "data_source": "postgres://reports/sales",
        "date_range": {"start": "2026-04-26", "end": "2026-05-02"},
        "filters": {"region": "APAC"},
    },
    outputs={
        "format": "markdown",
        "destination": "s3://reports/daily/2026-05-03.md",
        "schema": "ReportSchema",
    },
    completion_criteria=[
        "All required sections are present",
        "All numeric figures match the source data",
        "File is uploaded to the destination",
    ],
)

assert task.is_executable()
