"""Generated from book-content article."""

def decompose_task_bottomup(task: str, available_tools: List[str]) -> List[str]:
    """Bottom-Up: tool-based task decomposition"""
    
    prompt = f"""
    Task: {task}
    
    Available tools:
    {', '.join(available_tools)}
    
    Design steps to complete the task by combining the above tools.
    Each step should use one tool.
    """
    
    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return parse_steps(response.choices[0].message.content)
