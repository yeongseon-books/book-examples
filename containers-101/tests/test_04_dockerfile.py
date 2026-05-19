"""Tests for 04 dockerfile in Containers 101."""

from ko import _04_dockerfile as ep


def test_parser_builds_ast():
    """Test parser builds ast."""
    ast = ep.parse_dockerfile("FROM python:3.12-slim\nRUN echo hi")
    assert ast[0].opcode == "FROM"
    assert ast[1].opcode == "RUN"


def test_linter_flags_cache_and_latest_and_root():
    """Test linter flags cache and latest and root."""
    src = "\n".join(["FROM python:latest", "RUN pip install flask", "USER root"])
    warnings = ep.lint_dockerfile(src)
    assert any("no-cache-dir" in w for w in warnings)
    assert any("latest" in w.lower() for w in warnings)
    assert any("root" in w.lower() for w in warnings)
