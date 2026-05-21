"""Generated from book-content article."""

def get_weather(city: str) -> dict:
    # In production this calls a real API. Mock here.
    fake = {"Tokyo": {"temp": 18, "condition": "rain"},
            "Seoul": {"temp": 22, "condition": "clear"}}
    return fake.get(city, {"error": "unknown city"})
