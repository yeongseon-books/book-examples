"""Generated from book-content article."""

def execute_tool(tool_name: str, params: dict) -> dict:
    """Execute tool (with error handling)"""
    try:
        if tool_name == "get_weather":
            response = requests.get(
                f"https://api.weather.com/{params['location']}",
                timeout=5
            )
            response.raise_for_status()
            return {"success": True, "data": response.json()}
    
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "API timeout. Please try again later."
        }
    
    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "error": f"HTTP error {e.response.status_code}: {e.response.text}"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }
