"""Generated from book-content article."""

def brittle_workflow(steps: List[str]) -> List[Any]:
    """Halt on first failure"""
    results = []
    for step in steps:
        result = execute_step(step)  # Raises Exception on failure
        results.append(result)
    return results
