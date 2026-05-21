"""Generated from book-content article."""

def get_weather(location: str) -> dict:
    """Weather lookup (no validation)"""
    response = requests.get(f"https://api.weather.com/{location}")
    return response.json()  # Assume response format

# Usage
weather = get_weather("Seoul")
temperature = weather["temp"]  # May raise KeyError
