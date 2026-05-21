"""Generated from book-content article."""

def execute_tool(tool_name: str, params: dict) -> dict:
    """Execute tool (no error handling)"""
    if tool_name == "get_weather":
        # Throws Exception if API call fails
        return requests.get(f"https://api.weather.com/{params['location']}").json()
