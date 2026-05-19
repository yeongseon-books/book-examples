from __future__ import annotations

from ko import _02_ci_pipeline as ci
from ko import _03_cd_and_deployment as cd
from ko import _07_monitoring_and_alerting as mon
from ko import _09_incident_and_oncall as inc


def run_golden_path(version: str) -> dict[str, object]:
    runner = __import__("common").MockCommandRunner(
        {"lint": (0, "ok", ""), "test": (0, "ok", ""), "build": (0, "ok", "")}
    )
    pipeline = ci.Pipeline(
        [
            ci.Stage("lint", "lint"),
            ci.Stage("test", "test"),
            ci.Stage("build", "build"),
        ],
        runner,
    )
    pipeline_result = pipeline.run()

    deployment = cd.simulate_canary(version)

    metrics = mon.MetricStore(window=3)
    metrics.observe("error_rate", 0.002)
    metrics.observe("error_rate", 0.001)
    metrics.observe("error_rate", 0.002)
    alert = mon.AlertRule("error_rate", threshold=0.01, mode="above")

    oncall = inc.pick_oncall(["alice", "bob", "carol"], vacation={"carol"}, offset=1)

    return {
        "pipeline": pipeline_result["status"],
        "deployed_version": version,
        "deployment_healthy": deployment["zero_downtime"],
        "incident_opened": alert.evaluate(metrics),
        "oncall": oncall,
        "metrics": {"error_rate_window_avg": (0.002 + 0.001 + 0.002) / 3},
    }
