from common import PodValidator, ManifestParser
from pathlib import Path


def test_ep02_pod_validation_passes():
    pod = ManifestParser().parse(Path('ko/02-pod/pod.yaml').read_text())[0]
    assert PodValidator().validate(pod) == []
