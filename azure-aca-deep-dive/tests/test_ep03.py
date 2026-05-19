"""Tests for ep03 in Azure Aca Deep Dive."""

from conftest import load_module

run = load_module(
    "ko/03-revision-and-traffic-split/step01_revision_split.py", "ep03"
).run


def test_ep03_traffic_split_is_weighted_to_100() -> None:
    """Test ep03 traffic split is weighted to 100."""
    result = run()
    assert result["episode"] == 3
    assert result["weight_total"] == 100
    assert result["traffic"][0]["revisionName"] == "orders--blue"
