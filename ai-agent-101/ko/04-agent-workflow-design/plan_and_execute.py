"""Generated from book-content article."""

def plan_and_execute_agent(user_query: str, tools: List[Dict]) -> str:
    """Plan-and-Execute pattern: Plan → Execute"""

        # 1단계: Create plan
    plan_prompt = f"""
    Task: {user_query}

    Create a step-by-step plan to complete this task.
    Each step should have a clear goal and required tools.

    Format:
    1. [step description] - Tool: [tool name]
    2. [step description] - Tool: [tool name]
    ...
    """

    response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": plan_prompt}]
    )

    plan = response.choices[0].message.content
    print(f"Plan:\n{plan}\n")

        # 2단계: Execute plan
    steps = parse_plan(plan)  # "1. step - Tool: name" → structured

    results = []
    for idx, step in enumerate(steps):
        print(f"[Step {idx + 1}] {step['description']}")

        # 도구 실행
        tool_result = execute_tool(step["tool"], step["params"])
        results.append({
            "step": idx + 1,
            "description": step["description"],
            "result": tool_result
        })

        print(f"Result: {tool_result}\n")

        # 3단계: Generate final answer
    summary_prompt = f"""
    Task: {user_query}

    Executed steps and results:
    {format_results(results)}

    Answer the user's question based on the above results.
    """

    final_response = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": summary_prompt}]
    )

    return final_response.choices[0].message.content
