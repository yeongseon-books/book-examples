from pathlib import Path

from common import DeploymentSimulator, ManifestParser


def test_ep03_rolling_update_min_available():
    dep = ManifestParser().parse(Path("ko/03-deployment/deployment.yaml").read_text())[
        0
    ]
    result = DeploymentSimulator().rollout(dep)
    assert result["min_available"] == 2
    assert result["replicaset"]["pods"] == 4
