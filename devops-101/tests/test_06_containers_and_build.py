"""Tests for 06 containers and build in Devops 101."""

from ko import _06_containers_and_build as ep06


def test_linter_flags_latest_and_root_and_detects_multistage() -> None:
    """Test linter flags latest and root and detects multistage."""
    dockerfile = """
FROM python:latest AS builder
RUN pip install -r requirements.txt
FROM python:3.12-slim
COPY . .
USER root
""".strip()
    result = ep06.lint_dockerfile(dockerfile)
    assert result["has_multistage"] is True
    text = " ".join(result["warnings"])
    assert "latest" in text.lower()
    assert "non-root" in text.lower()
