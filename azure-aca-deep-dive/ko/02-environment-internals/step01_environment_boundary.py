from __future__ import annotations

from common import AzPlan, as_json, dry_run_az


def run() -> dict[str, object]:
    plan = AzPlan(
        command="az containerapp env show --name aca-prod-env --resource-group rg-aca --query appLogsConfiguration",
        payload={
            "environment": "aca-prod-env",
            "shared_network_boundary": True,
            "shared_log_analytics": True,
            "dapr_component_scope": "environment",
        },
    )
    simulated = dry_run_az(plan.command)
    return {"episode": 2, "plan": plan.payload, "simulated": simulated}


if __name__ == "__main__":
    print(as_json(run()))
