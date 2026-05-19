"""Tests for 06 operating systems in Computer Science 101."""

import importlib.util
from pathlib import Path


def load(name, rel):
    """Load."""
    spec = importlib.util.spec_from_file_location(
        name, Path(__file__).parent.parent / rel
    )
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def test_sjf_beats_fcfs_on_sample():
    """Test sjf beats fcfs on sample."""
    m = load("ep06", "ko/06-operating-systems.py")
    jobs = [("P1", 0, 8), ("P2", 1, 4), ("P3", 2, 2)]
    assert m.sjf_avg_waiting(jobs) < m.fcfs_avg_waiting(jobs)
