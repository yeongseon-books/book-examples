"""Generated from book-content article."""

from typing import Any, Dict


def execute_tool_with_retry(
    tool_name: str,
    params: dict[str, Any],
    max_retries: int = 3
) -> dict[str, Any]:
    """Execute tool with retry logic."""
    for attempt in range(max_retries):
        try:
            result = execute_tool(tool_name, params)
            return {"success": True, "data": result}

        except ConnectionError:
            # Network error: retry
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            return {"success": False, "error": f"Connection failed after {max_retries} attempts"}

        except ValueError as e:
            # Parameter error: no retry needed
            return {"success": False, "error": f"Invalid parameters: {str(e)}"}

        except Exception as e:
            # Unexpected error: log and return
            log_error(tool_name, params, e)
            return {"success": False, "error": f"Unexpected error: {str(e)}"}
