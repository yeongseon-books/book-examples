from en.ep09_toggle import toggle


def test_ep09_toggle_module_and_ci_fixture_file_exists():
    from pathlib import Path

    assert toggle(True) is False
    assert toggle(False) is True
    assert Path(".github/workflows/ci.yml.example").exists()
