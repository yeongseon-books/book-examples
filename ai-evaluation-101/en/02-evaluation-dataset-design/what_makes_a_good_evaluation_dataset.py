"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class EvalExample:
    id: str
    input: dict
    expected: dict | None       # only filled when a deterministic answer exists
    category: str               # one of "happy_path", "edge_case", "adversarial"
    notes: str = ""
