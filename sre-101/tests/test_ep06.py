import pytest

from en.ep06_incident_response import next_state, should_page


def test_ep06_state_machine_and_paging():
    assert next_state("Detected", "Triaged") == "Triaged"
    assert should_page("SEV2", 20)
    with pytest.raises(ValueError):
        next_state("Detected", "Resolved")
