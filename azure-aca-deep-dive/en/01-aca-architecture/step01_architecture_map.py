from __future__ import annotations

from common import AzPlan, as_json, dry_run_az


def run() -> dict[str, object]:
    plan = AzPlan(
        command="az containerapp env show --name aca-prod-env --resource-group rg-aca",
        payload={
            "environment": "aca-prod-env",
            "layers": ["environment", "revision", "replica"],
            "components": ["envoy", "keda", "dapr"],
            "control_plane": "managed-by-microsoft",
        },
    )
    simulated = dry_run_az(plan.command)
    return {"episode": 1, "plan": plan.payload, "simulated": simulated}


if __name__ == "__main__":
    print(as_json(run()))
