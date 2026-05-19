from ko.ep08_type_checker_demo import run_mypy_if_available


def test_ep08_mypy_demo_runs_or_skips() -> None:
    out = run_mypy_if_available()
    assert out["status"] in {"ran", "skipped"}
    if out["status"] == "ran":
        assert isinstance(out["returncode"], int)
