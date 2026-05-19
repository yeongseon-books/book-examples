from pathlib import Path

from _loader import load_module

m = load_module("06-visualization.py")


def test_episode_06_charts_are_created(tmp_path) -> None:
    charts = m.create_charts(tmp_path, seed=42)
    assert set(charts.keys()) == {"histogram", "scatter", "bar", "line"}
    for p in charts.values():
        assert Path(p).exists()
