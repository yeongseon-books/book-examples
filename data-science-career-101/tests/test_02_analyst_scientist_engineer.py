from __future__ import annotations

from .conftest import load_module


mod = load_module("ko/02-analyst-scientist-engineer.py")


def test_role_classifier_prefers_scientist_for_experiment_text() -> None:
    text = "Run experiment, validate hypothesis, improve model feature pipeline"
    result = mod.classify_job_description(text)
    assert result["predicted_role"] == "scientist"
