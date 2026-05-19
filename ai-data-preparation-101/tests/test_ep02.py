"""Tests for ep02 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep02_catalog() -> None:
    """Test ep02 catalog."""
    result = run_dict(
        "ko/02-source-data-collection-cataloging/step01_dataset_catalog.py"
    )
    assert result["version"] == "1.0.0"
    assert len(str(result["sha256"])) == 64
