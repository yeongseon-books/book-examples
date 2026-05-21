"""Generated from book-content article."""

def execute_with_priority(
    tools: List[str],
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Execute tools in priority order."""
    
    # Priority: 1. Cache lookup 2. Real-time API 3. LLM knowledge
    priority_order = ["check_cache", "api_call", "llm_knowledge"]
    
    for tool_name in priority_order:
        if tool_name not in tools:
            continue
        
        result = execute_tool(tool_name, params)
        
        if result["success"]:
            return result
    
    return {"success": False, "error": "All tools failed"}
