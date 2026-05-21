"""Generated from book-content article."""

import json


def execute_tool(tool_name: str, arguments: str) -> str:
    """Execute the requested tool and return results."""
    params = json.loads(arguments)

    if tool_name == "get_weather":
        # Call actual weather API
        weather_data = get_weather_api(params["location"])
        return json.dumps(weather_data)

    return json.dumps({"error": "Unknown tool"})

# Execute tool
tool_call = response.choices[0].message.tool_calls[0]
result = execute_tool(tool_call.function.name, tool_call.function.arguments)
