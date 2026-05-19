import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import az


def build_up_command() -> str:
    cmd = az(
        "containerapp",
        "up",
        "--name",
        "hello-aca",
        "--resource-group",
        "rg-demo",
        "--image",
        "mcr.microsoft.com/azuredocs/containerapps-helloworld:latest",
        "--ingress",
        "external",
        "--target-port",
        "80",
    )
    return cmd.render()


def run() -> dict[str, str]:
    return {
        "service": "aca",
        "mental_model": "container-first managed platform",
        "command": build_up_command(),
    }


if __name__ == "__main__":
    print(run())
