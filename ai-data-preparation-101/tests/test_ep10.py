"""Tests for ep10 in Ai Data Preparation 101."""

from conftest import run_dict


def test_ep10_pipeline() -> None:
    """Test ep10 pipeline."""
    result = run_dict("ko/10-production-data-pipeline/step01_pipeline_orchestrator.py")
    assert int(result["ingest"]) >= int(result["quality"])
    assert int(result["clean"]) >= int(result["dedup"])
