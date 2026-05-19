"""Azure Aks 101 - Episode 1: Deployment service manifest."""

from __future__ import annotations

from common import dump_yaml


def build_manifest() -> dict[str, object]:
    """Build manifest."""
    return {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "fastapi-hello"},
        "spec": {
            "replicas": 2,
            "selector": {"matchLabels": {"app": "fastapi-hello"}},
            "template": {
                "metadata": {"labels": {"app": "fastapi-hello"}},
                "spec": {
                    "containers": [
                        {
                            "name": "app",
                            "image": "example.azurecr.io/fastapi-hello:latest",
                            "ports": [{"containerPort": 8000}],
                        }
                    ]
                },
            },
        },
    }


def build_manifest_yaml() -> str:
    """Build manifest yaml."""
    return dump_yaml(build_manifest())


if __name__ == "__main__":
    print(build_manifest_yaml())
