"""Generated from book-content article."""

TOOLS = {
    "search": {
        "function": tool_search,
        "schema": SearchInput,
        "description": "Search for material by keyword.",
    },
    "calculator": {
        "function": tool_calculator,
        "schema": CalculatorInput,
        "description": "Evaluate an arithmetic expression.",
    },
}

def tools_to_openai_format() -> list[dict[str, Any]]:
    """Convert the registry to OpenAI Function Calling format."""
    result = []
    for name, info in TOOLS.items():
        result.append({
            "type": "function",
            "function": {
                "name": name,
                "description": info["description"],
                "parameters": info["schema"].model_json_schema(),
            },
        })
    return result
