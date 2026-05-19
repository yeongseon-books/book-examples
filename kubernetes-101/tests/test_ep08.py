"""Tests for ep08 in Kubernetes 101."""

from common import HPAController


def test_ep08_hpa_scales_up_on_high_cpu():
    """Test ep08 hpa scales up on high cpu."""
    desired = HPAController().desired_replicas(
        3, current_cpu=90, target_cpu=60, min_replicas=2, max_replicas=10
    )
    assert desired == 5
