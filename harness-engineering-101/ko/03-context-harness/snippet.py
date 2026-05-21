"""Generated from book-content article."""

import re

def mask_secrets(text: str) -> str:
    """Mask API keys and PII."""
    text = re.sub(r"sk-[a-zA-Z0-9]{20,}", "[REDACTED_API_KEY]", text)
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", "[REDACTED_CARD]", text)
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]", text)
    return text

def filter_tools_for_task(all_tools: list[dict], task_tags: set[str]) -> list[dict]:
    """Expose only tools whose tags match the task."""
    return [t for t in all_tools if set(t.get("tags", [])) & task_tags]

def trim_tool_history(history: list[dict], keep_last: int = 3) -> list[dict]:
    """Keep only the most recent N tool outputs."""
    tool_msgs = [i for i, m in enumerate(history) if m.get("role") == "tool"]
    if len(tool_msgs) <= keep_last:
        return history
    keep = set(tool_msgs[-keep_last:])
    return [m for i, m in enumerate(history) if m.get("role") != "tool" or i in keep]
