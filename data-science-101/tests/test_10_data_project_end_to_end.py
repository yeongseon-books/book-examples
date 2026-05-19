"""Tests for 10 data project end to end in Data Science 101."""

from pathlib import Path

from _loader import load_module

m = load_module("10-data-project-end-to-end.py")


def test_episode_10_pipeline_saves_and_loads_model(tmp_path) -> None:
    """Test episode 10 pipeline saves and loads model."""
    result = m.run_pipeline(tmp_path, seed=42)
    assert result["accuracy"] > 0.7
    assert result["same_predictions"] is True
    assert Path(result["model_path"]).exists()
