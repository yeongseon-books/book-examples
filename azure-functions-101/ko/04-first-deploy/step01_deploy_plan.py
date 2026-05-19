"""Azure Functions 101 - Episode 1: Deploy plan."""

from __future__ import annotations


def deployment_commands(app: str, rg: str, sa: str, loc: str) -> list[str]:
    """Deployment commands."""
    return [
        f"az group create --name {rg} --location {loc}",
        f"az storage account create --name {sa} --resource-group {rg} --location {loc} --sku Standard_LRS",
        f"az functionapp create --name {app} --resource-group {rg} --storage-account {sa} --runtime python --runtime-version 3.11 --functions-version 4 --flexconsumption-location {loc}",
        f"func azure functionapp publish {app}",
    ]


def run() -> dict[str, list[str]]:
    """Run."""
    return {
        "commands": deployment_commands(
            "func-hello-100", "rg-hello", "sthello100", "koreacentral"
        )
    }


if __name__ == "__main__":
    print(run())
