from ko import _05_infrastructure_as_code as ep05


def test_idempotent_reapply_produces_empty_diff(tmp_path) -> None:
    state = tmp_path / 'state.json'
    desired = [
        {'type': 'Server', 'name': 'api', 'size': 'small'},
        {'type': 'Network', 'name': 'vpc-main', 'cidr': '10.0.0.0/16'},
    ]
    ep05.apply(desired, str(state))
    second = ep05.apply(desired, str(state))
    assert second == {'create': [], 'update': [], 'destroy': []}
