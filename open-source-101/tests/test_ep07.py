from en.ep07_contributing_validator import run_example as run_en
from ko.ep07_contributing_validator import run_example as run_ko


def test_ep07_behavior():
    result = run_ko()
    assert result["has_steps"] is True
    assert result["has_code_of_conduct"] is True
    assert run_en()["has_code_of_conduct"] is True
