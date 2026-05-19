"""Azure Aks 101 - Episode 1: Ingress manifest."""

from __future__ import annotations

from common import dump_yaml


def build_ingress() -> dict[str, object]:
    """Build ingress."""
    return {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "Ingress",
        "metadata": {"name": "fastapi-hello"},
        "spec": {
            "ingressClassName": "webapprouting.kubernetes.azure.com",
            "rules": [
                {
                    "host": "api.example.com",
                    "http": {
                        "paths": [
                            {
                                "path": "/",
                                "pathType": "Prefix",
                                "backend": {
                                    "service": {
                                        "name": "fastapi-hello",
                                        "port": {"number": 80},
                                    }
                                },
                            }
                        ]
                    },
                }
            ],
        },
    }


def build_ingress_yaml() -> str:
    """Build ingress yaml."""
    return dump_yaml(build_ingress())


if __name__ == "__main__":
    print(build_ingress_yaml())
