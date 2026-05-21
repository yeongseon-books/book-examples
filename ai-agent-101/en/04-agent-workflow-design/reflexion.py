"""Generated from book-content article."""

def reflexion_agent(user_query: str, tools: List[Dict], max_retries: int = 3) -> str:
    """Reflexion pattern: Execute → Evaluate → Reflect → Retry"""
    
    reflections = []
    
    for attempt in range(max_retries):
        print(f"\n=== Attempt {attempt + 1} ===")
        
        # Include previous reflections in context
        context = "\n".join([f"Reflection {i+1}: {r}" for i, r in enumerate(reflections)])
        
        prompt = f"""
        Task: {user_query}
        
        Lessons from previous attempts:
        {context if context else "None (first attempt)"}
        
        Perform the task.
        """
        
        # Execute task
        result = execute_task(prompt, tools)
        
        # Evaluate result
        evaluation = evaluate_result(result, user_query)
        
        if evaluation["success"]:
            return result
        
        # Reflect on failure
        reflection_prompt = f"""
        Task: {user_query}
        Attempted method: {result}
        Failure reason: {evaluation['reason']}
        
        Reflect on what went wrong and how to improve in the next attempt.
        """
        
        reflection_response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": reflection_prompt}]
        )
        
        reflection = reflection_response.choices[0].message.content
        reflections.append(reflection)
        
        print(f"Reflection: {reflection}")
    
    return "Max retries reached without success."
