from common import ContextHarness
from conftest import load_episode


def test_ep03_context_harness_dedup_and_budget():
    m = load_episode('ko', '03-context-harness')
    out = m.context_harness_example()
    assert len(out) == 3
    assert len(out) == len(set(out))
    ch = ContextHarness(max_items=2)
    assert ch.build(['x', 'x', 'y', 'z']) == ['x', 'y']
