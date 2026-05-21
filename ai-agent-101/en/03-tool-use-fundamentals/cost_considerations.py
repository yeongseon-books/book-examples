"""Generated from book-content article."""

def select_tool_by_cost(
    query: str,
    available_tools: List[str]
) -> str:
    """Select cost-efficient tool."""
    
    # Tool costs (relative)
    tool_costs = {
        "cache_lookup": 0,      # Free
        "simple_api": 1,        # Low cost
        "expensive_api": 10,    # High cost
        "llm_call": 5           # Medium cost
    }
    
    # Analyze query complexity
    if len(query.split()) <= 5:
        # Simple query: prefer low-cost tools
        preferred = ["cache_lookup", "simple_api"]
    else:
        # Complex query: allow high-cost tools
        preferred = available_tools
    
    # Select cheapest available tool
    available_preferred = [t for t in preferred if t in available_tools]
    return min(available_preferred, key=lambda t: tool_costs.get(t, 999))
