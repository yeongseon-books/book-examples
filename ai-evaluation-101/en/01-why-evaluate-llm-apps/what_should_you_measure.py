"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class EvalResult:
    correctness: float  # are the facts right
    relevance: float    # does it answer the question
    safety: float       # any harm or bias
    style: float        # does it follow the requested format and tone
