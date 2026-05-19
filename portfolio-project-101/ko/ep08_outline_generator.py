"""Portfolio Project 101 - Episode 8: Outline generator."""

from __future__ import annotations


def generate_blog_outline(meta: dict[str, str]) -> str:
    """Generate blog outline."""
    return "\n".join(
        [
            f"# {meta.get('project_name', 'Project')} Blog Outline",
            "",
            "## Problem",
            meta.get("problem", ""),
            "",
            "## Approach",
            meta.get("approach", ""),
            "",
            "## Result",
            meta.get("result", ""),
        ]
    )
