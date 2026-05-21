"""Generated from book-content article."""

from typing import Any, Dict, List


def select_relevant_tools(
    user_query: str,
    all_tools: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Select tools relevant to query."""

    # Keyword-based filtering
    query_lower = user_query.lower()

    relevant_tools = []
    for tool in all_tools:
        tool_name = tool["function"]["name"]
        tool["function"]["description"]

        # Weather query → weather tools only
        if "weather" in query_lower and "weather" in tool_name or any(kw in query_lower for kw in ["search", "find", "lookup"]) and "search" in tool_name:
            relevant_tools.append(tool)

    # Return all tools if no relevant tools found
    return relevant_tools if relevant_tools else all_tools
