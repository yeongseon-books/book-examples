from common import ApprovalGate
from conftest import load_episode


def test_ep08_approval_gate_blocks_when_required_not_approved():
    m = load_episode("ko", "08-approval-gate")
    assert m.approval_gate_example() == "approved"
    gate = ApprovalGate("require-approve")
    assert gate.decide(approved=False) == "blocked"
