"""Data Science Career 101 - Episode 4: Data portfolio."""

from __future__ import annotations

import re

REQUIRED_SECTIONS = ["about", "projects", "skills", "contact"]
PROJECT_REQUIRED = ["problem", "data", "method", "result", "code"]


def validate_portfolio_readme(markdown: str) -> dict[str, object]:
    """Validate portfolio readme."""
    lower = markdown.lower()
    missing_sections = [
        section for section in REQUIRED_SECTIONS if f"## {section}" not in lower
    ]
    projects_block = re.search(r"## projects(.*?)(\n## |\Z)", lower, flags=re.S)
    missing_project_parts: list[str] = []
    if projects_block:
        block = projects_block.group(1)
        for part in PROJECT_REQUIRED:
            if part not in block:
                missing_project_parts.append(part)
    else:
        missing_project_parts = PROJECT_REQUIRED[:]
    score = 100 - 20 * len(missing_sections) - 8 * len(missing_project_parts)
    return {
        "score": max(0, score),
        "missing_sections": missing_sections,
        "missing_project_parts": missing_project_parts,
        "is_valid": not missing_sections and not missing_project_parts,
    }
