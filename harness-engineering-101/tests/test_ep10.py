"""Tests for ep10 in Harness Engineering 101."""

from pathlib import Path

from conftest import load_episode


def test_ep10_production_harness_pipeline(tmp_path: Path):
    """Test ep10 production harness pipeline."""
    m = load_episode("ko", "10-production-harness")
    result = m.production_harness_example(tmp_path / "prod.jsonl")
    assert result["status"] == "ok"
    assert result["tool"]["value"].startswith("resolved:")
    assert len(result["context"]) <= 3
