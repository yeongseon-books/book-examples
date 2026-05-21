"""Generated from book-content article."""

def agent_with_fallback(user_query: str) -> str:
    """Use fallback strategy when tools fail."""

    # First attempt: real-time tool
    weather_result = execute_tool_with_retry("get_weather", {"location": "Seoul"})

    if weather_result["success"]:
        return f"Current weather in Seoul: {weather_result['data']}"

    # Second attempt: cached data
    cached_data = get_cached_weather("Seoul")
    if cached_data:
        return f"Recent weather in Seoul (1 hour ago): {cached_data}"

    # Third attempt: LLM knowledge-based response
    return "Sorry, real-time weather information is currently unavailable. I can provide general weather information."
