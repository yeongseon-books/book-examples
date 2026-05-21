"""Generated from book-content article."""

def task_to_system_prompt(task: TaskSpec) -> str:
    """Generate a system prompt from a TaskSpec."""
    criteria = "\n".join(f"- {c}" for c in task.completion_criteria)
    return f"""You are an AI agent.

Goal: {task.goal}

Completion criteria (all required):
{criteria}

Output format: {task.outputs.get('format')}
Output destination: {task.outputs.get('destination')}

Available inputs:
{task.inputs}

Verify each criterion before reporting completion.
"""

def task_to_eval_dataset(task: TaskSpec, n: int = 10) -> list[dict]:
    """Generate eval cases from a TaskSpec."""
    # Vary inputs to create test cases
    return [
        {"task": task.model_dump(), "variation": i, "expected_pass": True}
        for i in range(n)
    ]
