"""Generated from book-content article."""

def handle_tool_error(
    tool_name: str,
    params: Dict[str, Any],
    error: Exception
) -> str:
    """Convert error to LLM-understandable message."""
    
    if isinstance(error, ConnectionError):
        return f"Tool '{tool_name}' failed: Network connection error. Try again later or use an alternative method."
    
    elif isinstance(error, ValueError):
        return f"Tool '{tool_name}' failed: Invalid parameters '{params}'. Please correct the parameters and retry."
    
    elif isinstance(error, PermissionError):
        return f"Tool '{tool_name}' failed: Permission denied. This operation cannot be performed."
    
    else:
        return f"Tool '{tool_name}' failed: {str(error)}. Try a different approach."
