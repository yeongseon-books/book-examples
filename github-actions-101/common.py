from __future__ import annotations

import itertools
import re
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

VALID_TRIGGERS = {
    "push",
    "pull_request",
    "schedule",
    "workflow_dispatch",
    "workflow_call",
}
VALID_RUNNERS = {
    "ubuntu-latest",
    "ubuntu-22.04",
    "ubuntu-24.04",
    "macos-latest",
    "windows-latest",
}
DEPRECATED_ACTIONS = {"actions/upload-artifact@v3", "actions/download-artifact@v3"}
SECRET_KEY_PATTERN = re.compile(r"(secret|token|password|apikey|api_key)", re.I)
SHA_PIN = re.compile(r"^[0-9a-f]{40}$")


def load_workflow(path: str) -> dict[str, Any]:
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("workflow must be a mapping")
    if True in data and "on" not in data:
        data["on"] = data.pop(True)
    return data


class WorkflowParser:
    def parse(self, workflow: dict[str, Any]) -> dict[str, Any]:
        jobs = workflow.get("jobs", {})
        parsed_jobs = {}
        for job_id, job in jobs.items():
            steps = job.get("steps", [])
            parsed_jobs[job_id] = {
                "needs": self._to_list(job.get("needs", [])),
                "runner": job.get("runs-on"),
                "steps": steps,
                "matrix": (((job.get("strategy") or {}).get("matrix")) or {}),
                "environment": job.get("environment"),
            }
        return {
            "name": workflow.get("name", ""),
            "triggers": self._parse_triggers(workflow.get("on")),
            "jobs": parsed_jobs,
        }

    def _parse_triggers(self, on_section: Any) -> list[str]:
        if isinstance(on_section, str):
            return [on_section]
        if isinstance(on_section, list):
            return [x for x in on_section if isinstance(x, str)]
        if isinstance(on_section, dict):
            return list(on_section.keys())
        return []

    def _to_list(self, value: Any) -> list[str]:
        if isinstance(value, str):
            return [value]
        if isinstance(value, list):
            return [v for v in value if isinstance(v, str)]
        return []


class WorkflowValidator:
    def validate(self, workflow: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        if "on" not in workflow:
            issues.append("missing on trigger")
        else:
            for trigger in WorkflowParser()._parse_triggers(workflow["on"]):
                if trigger not in VALID_TRIGGERS:
                    issues.append(f"invalid trigger: {trigger}")
        jobs = workflow.get("jobs")
        if not isinstance(jobs, dict) or not jobs:
            issues.append("missing jobs")
            return issues
        for job_id, job in jobs.items():
            if "runs-on" not in job:
                issues.append(f"{job_id}: missing runs-on")
            elif job["runs-on"] not in VALID_RUNNERS:
                issues.append(f"{job_id}: invalid runner {job['runs-on']}")
            if not isinstance(job.get("steps", []), list) or not job.get("steps"):
                issues.append(f"{job_id}: missing steps")
        return issues


class TriggerMatcher:
    def matches(
        self, workflow: dict[str, Any], event_name: str, payload: dict[str, Any]
    ) -> bool:
        on_section = workflow.get("on", {})
        if isinstance(on_section, str):
            return on_section == event_name
        if isinstance(on_section, list):
            return event_name in on_section
        if not isinstance(on_section, dict) or event_name not in on_section:
            return False
        cfg = on_section[event_name]
        if not isinstance(cfg, dict):
            return True
        ref = payload.get("ref", "")
        branch = (
            ref.replace("refs/heads/", "")
            if ref.startswith("refs/heads/")
            else payload.get("branch", "")
        )
        changed = payload.get("changed_files", [])
        branches = cfg.get("branches")
        if branches and branch not in branches:
            return False
        paths = cfg.get("paths")
        if paths:
            prefixes = [p[:-3] for p in paths if p.endswith("/**")]
            exact = [p for p in paths if not p.endswith("/**")]
            if not any(
                any(f.startswith(px) for px in prefixes) or f in exact for f in changed
            ):
                return False
        return True


class JobGraphAnalyzer:
    def analyze(self, workflow: dict[str, Any]) -> dict[str, Any]:
        jobs = workflow.get("jobs", {})
        indeg = {k: 0 for k in jobs}
        graph: dict[str, list[str]] = defaultdict(list)
        for job_id, job in jobs.items():
            needs = job.get("needs", [])
            if isinstance(needs, str):
                needs = [needs]
            for dep in needs:
                graph[dep].append(job_id)
                indeg[job_id] += 1
        q = deque([k for k, d in indeg.items() if d == 0])
        order = []
        levels = {k: 0 for k in q}
        while q:
            node = q.popleft()
            order.append(node)
            for nxt in graph[node]:
                levels[nxt] = max(levels.get(nxt, 0), levels.get(node, 0) + 1)
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        has_cycle = len(order) != len(jobs)
        parallelism = defaultdict(int)
        for _, lvl in levels.items():
            parallelism[lvl] += 1
        return {
            "order": order,
            "has_cycle": has_cycle,
            "max_parallel": max(parallelism.values(), default=0),
        }


class MatrixExpander:
    def expand(self, job: dict[str, Any]) -> list[dict[str, Any]]:
        matrix = ((job.get("strategy") or {}).get("matrix")) or {}
        if not matrix:
            return [{}]
        keys = sorted(matrix.keys())
        values = [matrix[k] for k in keys]
        return [
            dict(zip(keys, combo, strict=False)) for combo in itertools.product(*values)
        ]


class ActionUsageLinter:
    def lint(self, workflow: dict[str, Any]) -> list[str]:
        warnings: list[str] = []
        for job in workflow.get("jobs", {}).values():
            for step in job.get("steps", []):
                uses = step.get("uses")
                if not uses:
                    continue
                if uses in DEPRECATED_ACTIONS:
                    warnings.append(f"deprecated action: {uses}")
                if uses.endswith("@latest"):
                    warnings.append(f"unpinned latest tag: {uses}")
                ref = uses.split("@", 1)[1] if "@" in uses else ""
                if ref and not (ref.startswith("v") or SHA_PIN.match(ref)):
                    warnings.append(f"non-version tag: {uses}")
                if "@" not in uses:
                    warnings.append(f"missing action ref: {uses}")
        return warnings


class SecretsMaskingChecker:
    def check(self, workflow: dict[str, Any]) -> list[str]:
        issues: list[str] = []
        for job in workflow.get("jobs", {}).values():
            for step in job.get("steps", []):
                for key, value in (step.get("env") or {}).items():
                    if isinstance(value, str) and SECRET_KEY_PATTERN.search(key):
                        if "${{ secrets." not in value:
                            issues.append(f"plaintext secret env: {key}")
                run = step.get("run", "")
                if isinstance(run, str) and (
                    "password=" in run.lower() or "token=" in run.lower()
                ):
                    issues.append("possible plaintext secret in run command")
        return issues


class ArtifactSimulator:
    def flow(self, workflow: dict[str, Any]) -> dict[str, dict[str, set[str]]]:
        produced: dict[str, set[str]] = defaultdict(set)
        consumed: dict[str, set[str]] = defaultdict(set)
        for job_id, job in workflow.get("jobs", {}).items():
            for step in job.get("steps", []):
                uses = step.get("uses", "")
                with_cfg = step.get("with", {})
                name = with_cfg.get("name")
                if uses.startswith("actions/upload-artifact") and name:
                    produced[job_id].add(name)
                if uses.startswith("actions/download-artifact") and name:
                    consumed[job_id].add(name)
        return {"produced": produced, "consumed": consumed}


class DockerBuildSimulator:
    def validate(self, step: dict[str, Any]) -> list[str]:
        issues = []
        if not str(step.get("uses", "")).startswith("docker/build-push-action@"):
            return ["not docker build step"]
        cfg = step.get("with", {})
        if "context" not in cfg:
            issues.append("missing context")
        if "tags" not in cfg:
            issues.append("missing tags")
        if cfg.get("push") not in (True, "true", "True", False, "false", "False"):
            issues.append("invalid push flag")
        return issues


@dataclass
class PipelineResult:
    order: list[str]
    success: bool
    failed_job: str | None


class PipelineRunner:
    def run(
        self, workflow: dict[str, Any], fail_jobs: set[str] | None = None
    ) -> PipelineResult:
        fail_jobs = fail_jobs or set()
        graph = JobGraphAnalyzer().analyze(workflow)
        if graph["has_cycle"]:
            return PipelineResult([], False, "cycle")
        for job_id in graph["order"]:
            if job_id in fail_jobs:
                return PipelineResult(graph["order"], False, job_id)
        return PipelineResult(graph["order"], True, None)
