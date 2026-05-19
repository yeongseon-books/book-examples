import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import az


def deployment_plan() -> list[str]:
    rg = az(
        "group", "create", "--name", "rg-aca-101-demo", "--location", "eastus"
    ).render()
    acr = az(
        "acr",
        "create",
        "--name",
        "aca101demo",
        "--resource-group",
        "rg-aca-101-demo",
        "--location",
        "eastus",
        "--sku",
        "Basic",
    ).render()
    build = az(
        "acr", "build", "--registry", "aca101demo", "--image", "fastapi-hello:v1", "."
    ).render()
    deploy = az(
        "containerapp",
        "create",
        "--name",
        "fastapi-aca-demo",
        "--resource-group",
        "rg-aca-101-demo",
        "--environment",
        "aca-env-101-demo",
        "--image",
        "aca101demo.azurecr.io/fastapi-hello:v1",
        "--ingress",
        "external",
        "--target-port",
        "8000",
    ).render()
    return [rg, acr, build, deploy]


def run() -> dict[str, object]:
    plan = deployment_plan()
    return {"steps": len(plan), "commands": plan}


if __name__ == "__main__":
    print(run())
