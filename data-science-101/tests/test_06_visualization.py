"""Tests for 06 visualization in Data Science 101."""

from pathlib import Path

from _loader import load_module

m = load_module("06-visualization.py")


def test_episode_06_charts_are_created(tmp_path) -> None:
    """Test episode 06 charts are created."""
    charts = m.create_charts(tmp_path, seed=42)
    assert set(charts.keys()) == {"histogram", "scatter", "bar", "line"}
    for p in charts.values():
        assert Path(p).exists()
