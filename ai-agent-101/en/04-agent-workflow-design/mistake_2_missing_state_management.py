"""Generated from book-content article."""

def fragile_workflow(task: str) -> str:
    """Workflow without state persistence"""
    step1_result = execute_step1(task)
    step2_result = execute_step2(step1_result)  # Failure restarts from step1
    step3_result = execute_step3(step2_result)
    return step3_result
