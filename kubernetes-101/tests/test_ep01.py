from pathlib import Path

from common import ManifestParser


def test_ep01_parse_basic_pod():
    docs = ManifestParser().extract(
        Path("ko/01-what-is-kubernetes/pod.yaml").read_text()
    )
    assert docs[0]["kind"] == "Pod"
