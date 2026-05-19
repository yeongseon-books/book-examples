from __future__ import annotations

from .conftest import load_module


mod = load_module("ko/04-data-portfolio.py")


def test_missing_projects_section_is_flagged() -> None:
    markdown = """
## About
소개
## Skills
Python, SQL
## Contact
email@example.com
"""
    result = mod.validate_portfolio_readme(markdown)
    assert "projects" in result["missing_sections"]
    assert result["is_valid"] is False
