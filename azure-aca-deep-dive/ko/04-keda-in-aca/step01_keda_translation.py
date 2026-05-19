from __future__ import annotations

from common import AzPlan, as_json, dry_run_az


def run() -> dict[str, object]:
    plan = AzPlan(
        command=(
            "az containerapp update -n worker -g rg-aca --min-replicas 0 --max-replicas 30 "
            "--scale-rule-name queue-rule --scale-rule-type azure-queue "
            "--scale-rule-metadata queueName=jobs queueLength=5"
        ),
        payload={
            "revision_scope": True,
            "keda_shape": {
                "target": "worker",
                "minReplicas": 0,
                "maxReplicas": 30,
                "trigger": {"type": "azure-queue", "queueLength": 5},
            },
        },
    )
    simulated = dry_run_az(plan.command)
    return {"episode": 4, "plan": plan.payload, "simulated": simulated}


if __name__ == "__main__":
    print(as_json(run()))
