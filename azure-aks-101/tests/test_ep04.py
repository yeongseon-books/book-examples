from conftest import load_module
from common import load_yaml


def test_ep04_deployment_yaml_shape() -> None:
    ko = load_module(
        "ko/04-pod-deployment-service/step01_deployment_service_manifest.py", "ep04_ko"
    )
    en = load_module(
        "en/04-pod-deployment-service/step01_deployment_service_manifest.py", "ep04_en"
    )
    for module in (ko, en):
        manifest = load_yaml(module.build_manifest_yaml())
        assert manifest["kind"] == "Deployment"
        assert manifest["spec"]["replicas"] == 2
        assert (
            manifest["spec"]["template"]["spec"]["containers"][0]["ports"][0][
                "containerPort"
            ]
            == 8000
        )
