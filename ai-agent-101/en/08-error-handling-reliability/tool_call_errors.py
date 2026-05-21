"""Generated from book-content article."""

from typing import Any

import requests


class ToolExecutionError(Exception):
    """Tool execution failed."""
    def __init__(self, tool_name: str, reason: str, recoverable: bool = True):
        self.tool_name = tool_name
        self.reason = reason
        self.recoverable = recoverable
        super().__init__(f"{tool_name} failed: {reason}")

def execute_tool_safely(tool_name: str, tool_fn, **kwargs) -> Any:
    """Run a tool safely."""
    try:
        return tool_fn(**kwargs)
    except requests.Timeout:
        raise ToolExecutionError(tool_name, "timeout", recoverable=True)
    except requests.ConnectionError:
        raise ToolExecutionError(tool_name, "network connection failed", recoverable=True)
    except ValueError as e:
        # Bad arguments — same args won't succeed on retry
        raise ToolExecutionError(tool_name, f"bad argument: {e}", recoverable=False)
    except Exception as e:
        raise ToolExecutionError(tool_name, f"unexpected error: {e}", recoverable=False)
