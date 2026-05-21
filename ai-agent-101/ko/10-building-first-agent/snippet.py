"""Generated from book-content article."""

from typing import Any
from pydantic import BaseModel, Field
import json

class SearchInput(BaseModel):
    """Input schema for the search tool."""
    query: str = Field(..., description="Search query")
    top_k: int = Field(3, description="Number of results to return")

class CalculatorInput(BaseModel):
    """Input schema for the calculator tool."""
    expression: str = Field(..., description="Python arithmetic expression")

def tool_search(query: str, top_k: int = 3) -> list[dict[str, str]]:
    """Fake search tool. In production this would call an external API."""
    fake_db = [
        {"title": "FastAPI Official Docs", "snippet": "FastAPI is a modern, fast Python web framework."},
        {"title": "FastAPI Performance Benchmarks", "snippet": "FastAPI delivers performance comparable to Node.js and Go."},
        {"title": "FastAPI vs Flask", "snippet": "FastAPI beats Flask in async support and automatic documentation."},
    ]
    return fake_db[:top_k]

def tool_calculator(expression: str) -> float:
    """Safe arithmetic. Plain eval is dangerous, so we use a restricted environment."""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError(f"Disallowed characters in expression: {expression}")
    return eval(expression, {"__builtins__": {}}, {})
