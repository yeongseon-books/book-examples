"""Tests for 07 modeling in Data Science 101."""

from _loader import load_module

m = load_module("07-modeling.py")


def test_episode_07_model_accuracy() -> None:
    """Test episode 07 model accuracy."""
    result = m.train_models(seed=42)
    assert result["logreg_accuracy"] > 0.7
    assert result["rf_accuracy"] > 0.7
    assert result["rf_cv_accuracy"] > 0.7
