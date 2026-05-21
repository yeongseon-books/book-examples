"""Generated from book-content article."""

from dataclasses import dataclass
from collections.abc import Callable
from typing import List

@dataclass
class TestCase:
    """A test case."""
    task_id: str
    user_input: str
    expected_outcome: dict
    success_criteria: Callable[[dict], bool]

@dataclass
class EvaluationResult:
    """An evaluation result."""
    task_id: str
    success: bool
    actual_outcome: dict
    error: str = ""

def evaluate_success_rate(
    agent,
    test_cases: List[TestCase]
) -> dict:
    """Measure task success rate."""
    results: List[EvaluationResult] = []

    for test in test_cases:
        try:
            outcome = agent.run(test.user_input)
            success = test.success_criteria(outcome)
            results.append(EvaluationResult(
                task_id=test.task_id,
                success=success,
                actual_outcome=outcome
            ))
        except Exception as e:
            results.append(EvaluationResult(
                task_id=test.task_id,
                success=False,
                actual_outcome={},
                error=str(e)
            ))

    total = len(results)
    succeeded = sum(1 for r in results if r.success)
    return {
        "success_rate": succeeded / total if total else 0.0,
        "total": total,
        "succeeded": succeeded,
        "failed_cases": [r for r in results if not r.success]
    }
