from ko import _01_what_is_a_container as ep


def test_virtual_container_visibility_and_access():
    result = ep.run_isolation_demo()
    assert '/app/main.py' in result['visible']
    assert result['can_read_shadow'] is False
    assert result['can_read_app'] is True
