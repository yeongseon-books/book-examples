"""Generated from book-content article."""

def dynamic_decomposition(task: str, initial_context: Dict) -> str:
    """Dynamic task decomposition: decide next step based on current state"""

    context = initial_context
    completed_steps = []

    while not is_task_complete(context):
        # Decide next step based on current state
        next_step_prompt = f"""
        Final goal: {task}

        Completed steps so far:
        {format_steps(completed_steps)}

        Current state:
        {context}

        What should be done next?
        """

        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": next_step_prompt}]
        )

        next_action = response.choices[0].message.content

        # Execute next step
        result = execute_step(next_action)

        # Update context
        context.update(result)
        completed_steps.append(next_action)

        # Check termination condition
        if should_stop(context, task):
            break

    return generate_final_answer(context, task)
