"""Generated from book-content article."""

from dataclasses import dataclass, field
from enum import Enum


class ConstraintType(Enum):
    CAPABILITY = "capability"
    RESOURCE = "resource"
    BEHAVIORAL = "behavioral"
    SCOPE = "scope"

@dataclass
class Constraint:
    """A single constraint definition."""
    name: str
    type: ConstraintType
    rule: str  # Human-readable rule
    enforcer: str  # Identifier of the enforcement mechanism

@dataclass
class ConstraintPolicy:
    """The set of constraints applied to a task."""
    task_id: str
    constraints: list[Constraint] = field(default_factory=list)

    def by_type(self, t: ConstraintType) -> list[Constraint]:
        return [c for c in self.constraints if c.type == t]

policy = ConstraintPolicy(
    task_id="generate-report",
    constraints=[
        Constraint("read-only", ConstraintType.CAPABILITY, "Read-only DB access", "tool-filter"),
        Constraint("max-cost", ConstraintType.RESOURCE, "Max 0.5 USD", "cost-meter"),
        Constraint("no-pii", ConstraintType.BEHAVIORAL, "No PII in output", "output-validator"),
        Constraint("apac-only", ConstraintType.SCOPE, "APAC region only", "row-filter"),
    ],
)
