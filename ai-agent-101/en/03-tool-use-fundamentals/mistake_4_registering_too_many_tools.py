"""Generated from book-content article."""

def get_relevant_tools(user_query: str, all_tools: list) -> list:
    """Filter to query-relevant tools only."""
    query_lower = user_query.lower()

    # Keyword-based filtering
    if "weather" in query_lower:
        return [t for t in all_tools if "weather" in t["function"]["name"]]
    elif "email" in query_lower:
        return [t for t in all_tools if "email" in t["function"]["name"]]
    else:
        # Base tools only (max 5)
        return all_tools[:5]

# Pass only relevant tools to LLM
relevant_tools = get_relevant_tools(user_query, all_tools)

response = openai.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": user_query}],
    tools=relevant_tools  # 3-5 tools only
)
