"""Tests for ep02 in Kubernetes 101."""

from pathlib import Path

from common import ManifestParser, PodValidator


def test_ep02_pod_validation_passes():
    """Test ep02 pod validation passes."""
    pod = ManifestParser().parse(Path("ko/02-pod/pod.yaml").read_text())[0]
    assert PodValidator().validate(pod) == []
