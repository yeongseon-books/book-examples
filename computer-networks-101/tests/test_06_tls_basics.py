"""Tests for 06 tls basics in Computer Networks 101."""

import pytest

from tests._loader import load_ko


def test_state_machine_reaches_application_data() -> None:
    """Test state machine reaches application data."""
    ep = load_ko("06-tls-basics")
    sm = ep.TLSStateMachine()
    for msg in ep.VALID_SEQUENCE:
        sm.consume(msg)
    assert sm.state == "APPLICATION_DATA"


def test_state_machine_rejects_wrong_sequence() -> None:
    """Test state machine rejects wrong sequence."""
    ep = load_ko("06-tls-basics")
    sm = ep.TLSStateMachine()
    with pytest.raises(ValueError):
        sm.consume("ServerHello")
