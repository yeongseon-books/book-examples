from conftest import load_module

run = load_module("ko/08-postmortem/step01_example.py", "ep08").run


def test_ep08_postmortem_required_sections() -> None:
    text = run()
    for section in [
        "## Summary",
        "## Impact",
        "## Timeline",
        "## Root Cause",
        "## Action Items",
    ]:
        assert section in text
