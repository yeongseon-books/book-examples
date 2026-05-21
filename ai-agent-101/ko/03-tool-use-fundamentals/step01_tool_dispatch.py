"""Ai Agent 101 - 3편: tool use fundamentals 예제."""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import safe_calculate, search_knowledge


def dispatch(tool: str, args: dict[str, str]) -> dict[str, object]:
    """Dispatch."""
    if tool == "search":
        return {"success": True, "data": search_knowledge(args["query"])}
    if tool == "calculate":
        return {"success": True, "data": safe_calculate(args["expression"])}
    return {"success": False, "error": f"unknown tool: {tool}"}


if __name__ == "__main__":
    print(dispatch("search", {"query": "FastAPI"}))
    print(dispatch("calculate", {"expression": "3*4"}))
