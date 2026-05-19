"""Software Engineering 101 - Episode 7: Docs."""

from __future__ import annotations

from common import python_functions_with_docstrings


def docstring_coverage(code: str) -> dict[str, float]:
    """Docstring coverage."""
    total, documented = python_functions_with_docstrings(code)
    coverage = 0.0 if total == 0 else round(documented / total, 2)
    return {"total_functions": total, "documented": documented, "coverage": coverage}


def readme_quality_score(readme_text: str) -> int:
    """Readme quality score."""
    required = ["# ", "## Installation", "## Usage", "## Contributing"]
    return sum(1 for item in required if item in readme_text)
