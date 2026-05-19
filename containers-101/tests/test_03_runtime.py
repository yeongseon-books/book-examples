from ko import _03_runtime as ep


def test_valid_oci_subset_passes():
    cfg = {
        'process': {'args': ['python', 'app.py']},
        'root': {'path': '/rootfs'},
        'mounts': [{'destination': '/proc', 'type': 'proc', 'source': 'proc'}],
    }
    assert ep.validate_oci_config(cfg) == []


def test_missing_sections_fail():
    errors = ep.validate_oci_config({})
    assert 'process is required' in errors
    assert 'root is required' in errors
