"""Generated from book-content article."""

from typing import Optional


def get_weather(location: str) -> dict:
    """Weather lookup (with validation)"""
    try:
        response = requests.get(f"https://api.weather.com/{location}", timeout=5)
        response.raise_for_status()
        data = response.json()

        # Validate and standardize response
        return {
            "success": True,
            "data": {
                "location": data.get("location", location),
                "temperature": data.get("temp", data.get("temperature", None)),
                "condition": data.get("condition", "unknown"),
                "humidity": data.get("humidity", None)
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Usage
result = get_weather("Seoul")
if result["success"]:
    temp = result["data"]["temperature"]  # Safe access
    if temp is not None:
        print(f"Current temperature: {temp}°C")
