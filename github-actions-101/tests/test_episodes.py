import importlib.util
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("common", ROOT / "common.py")
assert spec and spec.loader
common = importlib.util.module_from_spec(spec)
sys.modules["common"] = common
spec.loader.exec_module(common)

ActionUsageLinter = common.ActionUsageLinter
ArtifactSimulator = common.ArtifactSimulator
DockerBuildSimulator = common.DockerBuildSimulator
JobGraphAnalyzer = common.JobGraphAnalyzer
MatrixExpander = common.MatrixExpander
PipelineRunner = common.PipelineRunner
SecretsMaskingChecker = common.SecretsMaskingChecker
TriggerMatcher = common.TriggerMatcher
WorkflowParser = common.WorkflowParser
WorkflowValidator = common.WorkflowValidator
load_workflow = common.load_workflow


def wf(ep: str) -> dict[str, Any]:
    return load_workflow(str(ROOT / "ko" / ep / ".github/workflows/workflow.yml"))


def test_ep01_parse_and_validate_passes() -> None:
    data = wf("01-what-is-github-actions")
    parsed = WorkflowParser().parse(data)
    assert parsed["triggers"] == ["push"]
    assert WorkflowValidator().validate(data) == []


def test_ep02_job_graph_and_parallelism() -> None:
    data = wf("02-workflow-and-job")
    graph = JobGraphAnalyzer().analyze(data)
    assert graph["has_cycle"] is False
    assert graph["max_parallel"] >= 2


def test_ep03_trigger_matcher_push_main_src() -> None:
    data = wf("03-triggers")
    ok = TriggerMatcher().matches(
        data, "push", {"ref": "refs/heads/main", "changed_files": ["src/app.py"]}
    )
    assert ok is True


def test_ep04_matrix_expands_to_six() -> None:
    data = wf("04-python-test-automation")
    combos = MatrixExpander().expand(data["jobs"]["test"])
    assert len(combos) == 3


def test_ep05_validator_rejects_bad_runner() -> None:
    data = wf("05-lint-and-typecheck")
    data["jobs"]["lint"]["runs-on"] = "ubuntu-old"
    issues = WorkflowValidator().validate(data)
    assert any("invalid runner" in i for i in issues)


def test_ep06_artifact_upload_download_flow() -> None:
    data = wf("06-build-artifact")
    flow = ArtifactSimulator().flow(data)
    assert "dist" in flow["produced"]["build"]
    assert "dist" in flow["consumed"]["deploy"]


def test_ep07_docker_build_step_validates() -> None:
    data = wf("07-docker-build")
    step = data["jobs"]["docker"]["steps"][1]
    assert DockerBuildSimulator().validate(step) == []


def test_ep08_pipeline_runner_dependency_order() -> None:
    data = wf("08-deploy-automation")
    result = PipelineRunner().run(data)
    assert result.success is True
    assert result.order.index("deploy-staging") < result.order.index(
        "deploy-production"
    )


def test_ep09_secret_checker_catches_plaintext() -> None:
    data = wf("09-secret-management")
    issues = SecretsMaskingChecker().check(data)
    assert any("plaintext" in i for i in issues)


def test_ep10_action_linter_warns_latest_tag() -> None:
    data = wf("10-real-world-cicd-pipeline")
    warnings = ActionUsageLinter().lint(data)
    assert any("@latest" in w for w in warnings)


def test_cycle_detection() -> None:
    cyc = {
        "on": ["push"],
        "jobs": {
            "a": {
                "runs-on": "ubuntu-latest",
                "needs": ["b"],
                "steps": [{"run": "echo a"}],
            },
            "b": {
                "runs-on": "ubuntu-latest",
                "needs": ["a"],
                "steps": [{"run": "echo b"}],
            },
        },
    }
    graph = JobGraphAnalyzer().analyze(cyc)
    assert graph["has_cycle"] is True
