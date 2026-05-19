from conftest import run_dict


def test_ep07_synthetic() -> None:
    result = run_dict("ko/07-synthetic-data-generation/step01_self_instruct_mock.py")
    assert result["count"] == 2
    assert "samples" in result
