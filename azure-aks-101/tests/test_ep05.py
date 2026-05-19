from conftest import load_module
from common import load_yaml


def test_ep05_ingress_yaml_shape() -> None:
    ko = load_module(
        "ko/05-networking-and-ingress/step01_ingress_manifest.py", "ep05_ko"
    )
    en = load_module(
        "en/05-networking-and-ingress/step01_ingress_manifest.py", "ep05_en"
    )
    for module in (ko, en):
        ingress = load_yaml(module.build_ingress_yaml())
        assert ingress["kind"] == "Ingress"
        assert (
            ingress["spec"]["ingressClassName"] == "webapprouting.kubernetes.azure.com"
        )
        assert (
            ingress["spec"]["rules"][0]["http"]["paths"][0]["backend"]["service"][
                "name"
            ]
            == "fastapi-hello"
        )
