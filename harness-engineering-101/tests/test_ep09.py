"""Tests for ep09 in Harness Engineering 101."""

import json
from pathlib import Path

from common import Observability
from conftest import load_episode


def test_ep09_observability_writes_jsonl(tmp_path: Path):
    """Test ep09 observability writes jsonl."""
    m = load_episode("ko", "09-observability")
    log_path = tmp_path / "events.jsonl"
    m.observability_example(log_path)
    lines = log_path.read_text().strip().splitlines()
    assert len(lines) == 1
    row = json.loads(lines[0])
    assert row["event"] == "timing"
    obs = Observability(log_path)
    obs.log_event("custom", {"ok": True})
    assert "custom" in log_path.read_text()
