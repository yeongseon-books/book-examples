"""Llm Api Production 101 - Episode 1: Basic tool call."""

import json
import os
from typing import Any, cast

from groq import Groq

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Return the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit",
                    },
                },
                "required": ["city"],
            },
        },
    }
]


def get_weather(city: str, unit: str = "celsius") -> dict:
    """Get weather."""
    return {"city": city, "temperature": 22, "unit": unit, "condition": "clear"}


def main() -> None:
    """Main."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Tell me the weather in Seoul."}],
        tools=cast("Any", TOOLS),
        tool_choice="auto",
    )

    choice = response.choices[0]
    print(f"finish_reason: {choice.finish_reason}")

    if choice.finish_reason == "tool_calls":
        for tc in choice.message.tool_calls or []:
            fn_name = tc.function.name
            args = json.loads(tc.function.arguments)
            print(f"tool call: {fn_name}({args})")
            if fn_name == "get_weather":
                result = get_weather(**args)
                print(f"function result: {result}")
    else:
        print(choice.message.content)


if __name__ == "__main__":
    main()


# Expected output:
# Tool call: get_weather({"location": "San Francisco"})
# Tool result: {"temperature": 62, "condition": "foggy"}
# Assistant: The weather in San Francisco is 62°F and foggy.
