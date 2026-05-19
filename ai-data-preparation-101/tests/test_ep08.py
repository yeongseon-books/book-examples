"""Tests for ep08 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep08_augmentation() -> None:
    """Test ep08 augmentation."""
    result = run_dict("ko/08-data-augmentation/step01_light_augmentation.py")
    assert str(result["source"]) != ""
    assert str(result["augmented"]) != ""
