"""Generated from book-content article."""

def decompose_task_topdown(task: str) -> List[Dict[str, Any]]:
    """Top-Down task decomposition"""
    
    prompt = f"""
    Task: {task}
    
    List major subtasks required to complete this task.
    Each subtask should be independently executable.
    
    Format:
    1. [Subtask 1]
       - Goal: [specific goal]
       - Required tools: [tool list]
    2. [Subtask 2]
       ...
    """
    
    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse response
    subtasks = parse_subtasks(response.choices[0].message.content)
    
    # Recursively decompose each complex subtask
    for subtask in subtasks:
        if is_complex(subtask):
            subtask["children"] = decompose_task_topdown(subtask["description"])
    
    return subtasks
