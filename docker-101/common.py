from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

import yaml


@dataclass
class DockerInstruction:
    keyword: str
    value: str
    raw: str


class DockerfileParser:
    def parse(self, content: str) -> list[DockerInstruction]:
        instructions: list[DockerInstruction] = []
        for raw_line in content.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(maxsplit=1)
            keyword = parts[0].upper()
            value = parts[1] if len(parts) > 1 else ""
            instructions.append(DockerInstruction(keyword=keyword, value=value, raw=line))
        return instructions


class DockerfileLinter:
    def lint(self, content: str) -> list[str]:
        parser = DockerfileParser()
        ins = parser.parse(content)
        issues: list[str] = []
        from_lines = [i for i in ins if i.keyword == "FROM"]
        if not from_lines:
            issues.append("missing FROM")
        for item in from_lines:
            image = item.value.split()[0]
            if image.endswith(":latest"):
                issues.append("avoid latest tag")
        if not any(i.keyword == "USER" for i in ins):
            issues.append("missing USER instruction")
        if any(i.keyword == "ADD" for i in ins):
            issues.append("prefer COPY over ADD unless archive auto-extract is needed")
        return issues


class ComposeValidator:
    def validate(self, content: str) -> list[str]:
        issues: list[str] = []
        data = yaml.safe_load(content) or {}
        services = data.get("services")
        if not isinstance(services, dict) or not services:
            return ["services section is required"]
        for name, svc in services.items():
            if not isinstance(svc, dict):
                issues.append(f"service {name} must be mapping")
                continue
            if "image" not in svc and "build" not in svc:
                issues.append(f"service {name} needs image or build")
            if name in {"web", "api"} and "depends_on" not in svc:
                issues.append(f"service {name} should declare depends_on")
            if name in {"db", "postgres"} and "healthcheck" not in svc:
                issues.append(f"service {name} should define healthcheck")
        return issues


class ImageLayerSimulator:
    def estimate_size_mb(self, layers: list[dict[str, int]]) -> int:
        return sum(layer.get("size_mb", 0) for layer in layers)

    def compare_multistage(self, builder_layers: list[dict[str, int]], runtime_layers: list[dict[str, int]]) -> dict[str, int]:
        full = self.estimate_size_mb(builder_layers + runtime_layers)
        optimized = self.estimate_size_mb(runtime_layers)
        return {
            "full": full,
            "optimized": optimized,
            "saved": max(full - optimized, 0),
        }


class EnvParser:
    def parse_env_file(self, content: str) -> dict[str, str]:
        values: dict[str, str] = {}
        for raw_line in content.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            values[k.strip()] = v.strip()
        return values


class SecurityPolicyChecker:
    def verify_runtime_flags(self, flags: list[str]) -> list[str]:
        required = {"--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges"}
        missing = sorted(required - set(flags))
        return [f"missing runtime flag: {m}" for m in missing]


class HealthcheckVerifier:
    def has_healthcheck(self, dockerfile_content: str) -> bool:
        return bool(re.search(r"^HEALTHCHECK\b", dockerfile_content, flags=re.MULTILINE))


def parse_yaml(content: str) -> dict[str, Any]:
    data = yaml.safe_load(content)
    if isinstance(data, dict):
        return data
    return {}
