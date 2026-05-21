"""Generated from book-content article."""

def agent_loop(user_query: str) -> str:
    """Agent loop (result checked)"""
    decision = llm.decide_next_action(user_query)
    
    if decision["action"] == "use_tool":
        tool_result = execute_tool(decision["tool"], decision["params"])
        
        # Check result
        if tool_result["success"]:
            # Success: pass result to LLM for final answer
            return llm.generate_answer(user_query, tool_result["data"])
        else:
            # Failure: inform LLM of error and request alternative strategy
            error_context = f"Tool execution failed: {tool_result['error']}"
            return llm.decide_next_action(user_query, context=error_context)
