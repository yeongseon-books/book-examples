import pytest
from tests._loader import load_ko


def test_state_machine_reaches_application_data() -> None:
    ep = load_ko("06-tls-basics")
    sm = ep.TLSStateMachine()
    for msg in ep.VALID_SEQUENCE:
        sm.consume(msg)
    assert sm.state == "APPLICATION_DATA"


def test_state_machine_rejects_wrong_sequence() -> None:
    ep = load_ko("06-tls-basics")
    sm = ep.TLSStateMachine()
    with pytest.raises(ValueError):
        sm.consume("ServerHello")
