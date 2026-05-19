from __future__ import annotations

from common import build_webapp_show_command


def classify_plane(endpoint: str) -> str:
    if ".scm.azurewebsites.net" in endpoint:
        return "scm"
    if endpoint.startswith("https://management.azure.com"):
        return "management"
    return "runtime"


def runtime_assumptions() -> dict[str, bool]:
    return {
        "stateless": True,
        "ephemeral_instance": True,
        "external_session_store": True,
    }


if __name__ == "__main__":
    cmd = build_webapp_show_command("rg-demo", "app-demo")
    print(cmd.as_string())
