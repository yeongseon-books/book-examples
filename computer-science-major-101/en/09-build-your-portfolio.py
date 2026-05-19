"""Computer Science Major 101 - Episode 9: Build your portfolio."""


def validate_portfolio_readme(content: str) -> tuple[bool, list[str]]:
    """Validate portfolio readme."""
    required = ["about", "projects", "skills", "contact"]
    lower = content.lower()
    missing = [section for section in required if f"## {section}" not in lower]
    return len(missing) == 0, missing


if __name__ == "__main__":
    sample = """# Portfolio\n\n## About\ntext\n\n## Projects\ntext\n\n## Skills\ntext\n\n## Contact\ntext\n"""
    print(validate_portfolio_readme(sample))
