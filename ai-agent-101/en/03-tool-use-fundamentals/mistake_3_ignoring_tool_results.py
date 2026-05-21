"""Generated from book-content article."""

def agent_loop(user_query: str) -> str:
    """Agent loop (result not checked)"""
    decision = llm.decide_next_action(user_query)
    
    if decision["action"] == "use_tool":
        tool_result = execute_tool(decision["tool"], decision["params"])
        # Return final answer without checking result
        return "Task completed"
