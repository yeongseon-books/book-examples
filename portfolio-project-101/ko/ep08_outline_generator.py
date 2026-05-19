from __future__ import annotations


def generate_blog_outline(meta: dict[str, str]) -> str:
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
