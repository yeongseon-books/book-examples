import pytest
from common import ConstraintHarness
from conftest import load_episode


def test_ep04_constraint_harness_blocks_forbidden_token():
    m = load_episode('ko', '04-constraint-harness')
    assert m.constraint_harness_example() == 'safe output'
    c = ConstraintHarness(forbidden_tokens=['SECRET'], max_length=50)
    with pytest.raises(ValueError):
        c.validate_output('contains SECRET text')
