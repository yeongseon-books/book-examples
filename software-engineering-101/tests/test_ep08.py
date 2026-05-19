"""Tests for ep08 in Software Engineering 101."""

from pathlib import Path

from en.ep08_collab import raci_matrix_validator, standup_notes_parser


def test_ep08_raci_and_standup():
    """Test ep08 raci and standup."""
    raci = Path("fixtures/ep08_raci.csv").read_text(encoding="utf-8")
    notes = Path("fixtures/ep08_standup.txt").read_text(encoding="utf-8")
    assert raci_matrix_validator(raci)["valid"] is True
    parsed = standup_notes_parser(notes)
    assert parsed["blockers"] == "none"
