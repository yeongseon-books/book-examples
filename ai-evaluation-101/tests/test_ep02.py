"""Tests for ep02 in Ai Evaluation 101."""

from conftest import load_module


def test_ep02_dataset_contains_edge_and_regression() -> None:
    """Test ep02 dataset contains edge and regression."""
    module = load_module(
        "ko/02-evaluation-dataset-design/step01_dataset_mix.py", "ep02"
    )
    result = module.run()
    assert result["edge_case"] >= 1
    assert result["regression"] >= 1
