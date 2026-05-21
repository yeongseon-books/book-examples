"""Generated from book-content article."""

import json
from typing import Optional


class LLMResponseError(Exception):
    """LLM response error."""
    pass

def parse_llm_json(response_text: str) -> dict:
    """Safely parse JSON returned by an LLM."""
    # 1. Strip markdown code fences
    cleaned = response_text.strip()
    if cleaned.startswith("```"):
        # Remove ```json ... ``` or ``` ... ```
        lines = cleaned.split("\n")
        cleaned = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

    # 2. Try to parse
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        raise LLMResponseError(f"JSON parse failed: {e}\nraw: {response_text[:200]}")
