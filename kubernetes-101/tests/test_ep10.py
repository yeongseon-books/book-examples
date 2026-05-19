"""Tests for ep10 in Kubernetes 101."""

from pathlib import Path

from common import ClusterStateSimulator, ManifestParser


def test_ep10_cluster_apply_delete_cycle():
    """Test ep10 cluster apply delete cycle."""
    pod = ManifestParser().parse(
        Path("ko/10-kubernetes-in-operation/ops.yaml").read_text()
    )[0]
    cluster = ClusterStateSimulator()
    cluster.apply(pod)
    assert cluster.get("Pod", "web") is not None
    cluster.delete("Pod", "web")
    assert cluster.get("Pod", "web") is None
