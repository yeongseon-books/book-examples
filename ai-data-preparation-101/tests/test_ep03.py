from conftest import run_dict


def test_ep03_dedup() -> None:
    result = run_dict("ko/03-cleaning-deduplication/step01_clean_dedup.py")
    assert int(result["raw"]) >= int(result["exact"]) >= int(result["near"])
