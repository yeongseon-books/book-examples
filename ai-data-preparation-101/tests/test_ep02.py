from conftest import run_dict


def test_ep02_catalog() -> None:
    result = run_dict(
        "ko/02-source-data-collection-cataloging/step01_dataset_catalog.py"
    )
    assert result["version"] == "1.0.0"
    assert len(str(result["sha256"])) == 64
