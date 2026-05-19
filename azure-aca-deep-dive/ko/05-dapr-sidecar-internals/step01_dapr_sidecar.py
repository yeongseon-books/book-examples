from __future__ import annotations

from common import AzPlan, as_json, dry_run_az


def run() -> dict[str, object]:
    plan = AzPlan(
        command=(
            "az containerapp update -n orders -g rg-aca --enable-dapr true "
            "--dapr-app-id orders --dapr-app-port 8080 --dapr-app-protocol http"
        ),
        payload={
            "sidecar": "daprd",
            "ports": {"http": 3500, "grpc": 50001},
            "component_scope": "environment-with-app-id-filter",
        },
    )
    simulated = dry_run_az(plan.command)
    return {"episode": 5, "plan": plan.payload, "simulated": simulated}


if __name__ == "__main__":
    print(as_json(run()))
