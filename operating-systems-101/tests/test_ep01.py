from common import ep01_os_info


def test_ep01_os_info_has_required_keys():
    data = ep01_os_info()
    assert "platform" in data
    assert "cpu_count" in data
    assert isinstance(data["cpu_count"], int | type(None))
