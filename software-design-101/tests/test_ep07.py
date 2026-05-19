from ko.ep07_data_flow import run_pipeline


def test_ep07_pipeline() -> None:
    assert run_pipeline("lang=python") == "LANG:PYTHON"
