from conftest import run_dict


def test_ep06_filter() -> None:
    result = run_dict("ko/06-quality-filtering/step01_heuristic_filter.py")
    assert result["input"] == 2
    assert result["kept"] == 1
