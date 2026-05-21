"""Generated from book-content article."""

def mitigation_plan(can_rollback: bool, has_flag: bool, traffic_spike: bool) -> list[str]:
    actions = []
    if can_rollback:
        actions.append("rollback")
    if has_flag:
        actions.append("disable_feature_flag")
    if traffic_spike:
        actions.append("apply_throttle")
    if not actions:
        actions.append("scale_out")
    return actions


def resolution_ready(test_pass: bool, config_reviewed: bool, peer_approved: bool) -> bool:
    return test_pass and config_reviewed and peer_approved
