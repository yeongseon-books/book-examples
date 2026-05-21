"""Generated from book-content article."""

from enum import Enum


class FailureStrategy(Enum):
    ABORT = "abort"          # Halt immediately
    SKIP = "skip"            # Skip and continue
    RETRY = "retry"          # Retry
    FALLBACK = "fallback"    # Use alternative method

def resilient_workflow(
    steps: List[str],
    failure_strategy: FailureStrategy = FailureStrategy.SKIP
) -> Dict[str, Any]:
    """Workflow with failure strategy"""
    results = {"successful": [], "failed": []}

    for step in steps:
        try:
            result = execute_step(step)
            results["successful"].append(result)

        except Exception as e:
            if failure_strategy == FailureStrategy.ABORT:
                raise

            elif failure_strategy == FailureStrategy.SKIP:
                results["failed"].append({"step": step, "error": str(e)})
                continue

            elif failure_strategy == FailureStrategy.RETRY:
                result = retry_with_backoff(execute_step, step)
                results["successful"].append(result)

            elif failure_strategy == FailureStrategy.FALLBACK:
                result = execute_fallback(step)
                results["successful"].append(result)

    return results
