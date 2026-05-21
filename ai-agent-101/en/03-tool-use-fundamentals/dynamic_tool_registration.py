"""Generated from book-content article."""

class DynamicToolRegistry:
    """Dynamic tool registry."""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
    
    def register(self, tool_schema: Dict[str, Any]):
        """Register a tool."""
        tool_name = tool_schema["function"]["name"]
        self.tools[tool_name] = tool_schema
    
    def unregister(self, tool_name: str):
        """Remove a tool."""
        if tool_name in self.tools:
            del self.tools[tool_name]
    
    def get_tools(self, context: str = None) -> List[Dict[str, Any]]:
        """Return tools matching context."""
        
        if context == "weather":
            # Weather-related tools only
            return [t for name, t in self.tools.items() if "weather" in name]
        
        elif context == "database":
            # Database-related tools only
            return [t for name, t in self.tools.items() if "db" in name or "sql" in name]
        
        else:
            # All tools
            return list(self.tools.values())

# Usage example
registry = DynamicToolRegistry()

# Register base tools
registry.register({
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Weather lookup",
        "parameters": {...}
    }
})

# Add database tools when user requests database operations
if "database" in user_query:
    registry.register({
        "type": "function",
        "function": {
            "name": "execute_sql",
            "description": "Execute SQL query",
            "parameters": {...}
        }
    })

# Pass context-appropriate tools to LLM
tools = registry.get_tools(context="database")
