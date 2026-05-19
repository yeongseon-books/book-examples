from pathlib import Path

from common import HelmTemplater


def test_ep09_helm_template_substitution():
    template = Path("ko/09-helm/chart-template.yaml").read_text()
    values = {
        "name": "web",
        "replicaCount": 2,
        "image": {"repository": "myorg/app", "tag": "1.0.0"},
    }
    rendered = HelmTemplater().render(template, values)
    assert "name: web" in rendered
    assert "replicas: 2" in rendered
    assert "image: myorg/app:1.0.0" in rendered
