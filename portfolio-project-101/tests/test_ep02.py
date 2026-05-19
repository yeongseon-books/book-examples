"""Tests for ep02 in Portfolio Project 101."""

from ko.ep02_trait_checklist import validate_project_traits


def test_ep02_trait_validator() -> None:
    """Test ep02 trait validator."""
    ok, missing = validate_project_traits(
        {"solving_real_problem": True, "scoped": True, "deployable": False}
    )
    assert ok is False
    assert missing == ["deployable"]
