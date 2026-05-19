"""Tests for 01 what is developer career in Developer Career 101."""

import importlib.util
from pathlib import Path


def load(name: str):
    """Load."""
    path = Path(__file__).resolve().parents[1] / "ko" / name
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_01_classifier_returns_senior_for_strong_input():
    """Test 01 classifier returns senior for strong input."""
    mod = load("01-what-is-developer-career.py")
    result = mod.classify_stage(years=7, technical_depth=9, ownership=8, influence=7)
    assert result["stage"] == "senior"
