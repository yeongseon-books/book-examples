"""Devops 101 - Episode 6: Containers and build."""

from __future__ import annotations


def lint_dockerfile(text: str) -> dict[str, object]:
    """Lint dockerfile."""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    warnings: list[str] = []

    has_multistage = sum(1 for line in lines if line.startswith("FROM ")) >= 2
    if any(":latest" in line for line in lines if line.startswith("FROM ")):
        warnings.append("Avoid latest tag in base image")
    if not any(
        "--no-cache-dir" in line
        for line in lines
        if line.startswith("RUN ") and "pip install" in line
    ):
        warnings.append("Use --no-cache-dir for pip install")
    if not any(
        line.startswith("USER ") and "root" not in line.lower() for line in lines
    ):
        warnings.append("Run container as non-root user")

    return {
        "warnings": warnings,
        "has_multistage": has_multistage,
        "estimated_size_mb": estimate_image_size(lines),
    }


def estimate_image_size(lines: list[str]) -> int:
    """Estimate image size."""
    score = 50
    for line in lines:
        if line.startswith("FROM "):
            score += 30
        elif line.startswith("RUN "):
            score += 15
        elif line.startswith("COPY ") or line.startswith("ADD "):
            score += 10
    return score
