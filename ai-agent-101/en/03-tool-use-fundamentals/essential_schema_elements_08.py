"""Generated from book-content article."""

{
    "name": "get_weather",
    "description": "Retrieves current weather for a specific location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City name (e.g., Seoul, New York)"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Temperature unit"
            }
        },
        "required": ["location"]  # location is required, unit is optional
    }
}
