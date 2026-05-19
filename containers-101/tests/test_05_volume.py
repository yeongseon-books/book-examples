import pytest
from ko import _05_volume as ep


def test_detect_mount_overlap():
    spec = [
        {"type": "bind", "source": "/host/a", "target": "/data"},
        {"type": "volume", "source": "cache", "target": "/data/cache"},
    ]
    assert ep.detect_overlap(spec)


def test_duplicate_target_raises():
    spec = [
        {"type": "bind", "source": "/host/a", "target": "/data"},
        {"type": "tmpfs", "source": "tmpfs", "target": "/data"},
    ]
    with pytest.raises(ValueError):
        ep.resolve_mounts(spec)
