from conftest import load_module


def test_portfolio_readme_validator_detects_missing_sections() -> None:
    mod = load_module("ko/09-build-your-portfolio.py")
    valid = """# Portfolio\n## About\n## Projects\n## Skills\n## Contact\n"""
    ok, missing = mod.validate_portfolio_readme(valid)
    assert ok
    assert missing == []

    incomplete = """# Portfolio\n## About\n## Projects\n"""
    ok2, missing2 = mod.validate_portfolio_readme(incomplete)
    assert not ok2
    assert set(missing2) == {"skills", "contact"}
