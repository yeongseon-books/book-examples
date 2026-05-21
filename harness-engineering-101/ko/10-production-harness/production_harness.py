"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class HarnessStack:
    task: object          # Ep2 — TaskSpec
    context: object       # Ep3 — ContextBudget
    constraint: object    # Ep4 — ConstraintPolicy
    tools: object         # Ep5 — ToolRegistry
    tests: object         # Ep6 — eval suite
    feedback: object      # Ep7 — FeedbackLoop
    approval: object      # Ep8 — ApprovalWorkflow
    observability: object # Ep9 — Tracer
