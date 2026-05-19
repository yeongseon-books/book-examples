"""Portfolio Project 101 - Episode 3: Readme linter."""

from __future__ import annotations

from common import extract_markdown_sections

REQUIRED_SECTIONS = {
    "Overview",
    "Install",
    "Usage",
    "Demo",
    "Architecture",
    "Tech Stack",
}


def lint_readme_sections(readme_text: str) -> tuple[bool, list[str]]:
    """Lint readme sections."""
    found = extract_markdown_sections(readme_text)
    missing = sorted(REQUIRED_SECTIONS - found)
    return (len(missing) == 0, missing)
