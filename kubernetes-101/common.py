"""Shared utilities and domain models for Kubernetes 101."""

from __future__ import annotations

import base64
import copy
import re
from dataclasses import dataclass
from typing import Any

import yaml


class ManifestParser:
    """Manifest parser."""

    def parse(self, content: str) -> list[dict[str, Any]]:
        """Parse."""
        docs = [d for d in yaml.safe_load_all(content) if d]
        if not isinstance(docs, list):
            return []
        return docs

    def extract(self, content: str) -> list[dict[str, Any]]:
        """Extract."""
        result: list[dict[str, Any]] = []
        for doc in self.parse(content):
            if not isinstance(doc, dict):
                continue
            result.append(
                {
                    "kind": doc.get("kind"),
                    "metadata": doc.get("metadata", {}),
                    "spec": doc.get("spec", {}),
                }
            )
        return result


class PodValidator:
    """Pod validator."""

    def validate(self, pod: dict[str, Any]) -> list[str]:
        """Validate."""
        errors: list[str] = []
        if pod.get("kind") != "Pod":
            errors.append("kind must be Pod")
        meta = pod.get("metadata", {})
        if not meta.get("name"):
            errors.append("metadata.name is required")
        spec = pod.get("spec", {})
        containers = spec.get("containers") or []
        if not containers:
            errors.append("spec.containers is required")
            return errors
        for c in containers:
            img = c.get("image", "")
            if ":" not in img or img.endswith(":latest"):
                errors.append("image must use explicit non-latest tag")
            resources = c.get("resources", {})
            limits = resources.get("limits")
            if not limits:
                errors.append(
                    f"container {c.get('name', 'unknown')} missing resource limits"
                )
            if "readinessProbe" not in c or "livenessProbe" not in c:
                errors.append(f"container {c.get('name', 'unknown')} missing probes")
        return errors


class DeploymentSimulator:
    """Deployment simulator."""

    def rollout(self, deployment: dict[str, Any]) -> dict[str, Any]:
        """Rollout."""
        spec = deployment.get("spec", {})
        replicas = int(spec.get("replicas", 1))
        strategy = spec.get("strategy", {}).get("rollingUpdate", {})
        max_unavailable = int(str(strategy.get("maxUnavailable", 1)).rstrip("%"))
        max_surge = int(str(strategy.get("maxSurge", 1)).rstrip("%"))
        min_available = max(replicas - max_unavailable, 0)
        rs_name = f"{deployment['metadata']['name']}-rs-v2"
        return {
            "replicas": replicas,
            "min_available": min_available,
            "max_surge": max_surge,
            "replicaset": {"name": rs_name, "pods": replicas + max_surge},
        }


class ServiceResolver:
    """Service resolver."""

    def resolve_type(self, service: dict[str, Any]) -> str:
        """Resolve type."""
        return service.get("spec", {}).get("type", "ClusterIP")

    def match_pods(
        self, service: dict[str, Any], pods: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """Match pods."""
        selector = service.get("spec", {}).get("selector", {})
        matched: list[dict[str, Any]] = []
        for pod in pods:
            labels = pod.get("metadata", {}).get("labels", {})
            if all(labels.get(k) == v for k, v in selector.items()):
                matched.append(pod)
        return matched


class IngressRouter:
    """Ingress router."""

    def route(self, ingress: dict[str, Any], host: str, path: str) -> str | None:
        """Route."""
        rules = ingress.get("spec", {}).get("rules", [])
        for rule in rules:
            if rule.get("host") != host:
                continue
            paths = rule.get("http", {}).get("paths", [])
            candidates: list[tuple[int, str]] = []
            for p in paths:
                prefix = p.get("path", "/")
                if path.startswith(prefix):
                    svc = p.get("backend", {}).get("service", {}).get("name")
                    if svc:
                        candidates.append((len(prefix), svc))
            if candidates:
                candidates.sort(reverse=True)
                return candidates[0][1]
        return None


class ConfigMapSecretLoader:
    """Config map secret loader."""

    def load_env(
        self,
        pod: dict[str, Any],
        configmaps: dict[str, dict[str, str]],
        secrets: dict[str, dict[str, str]],
    ) -> dict[str, str]:
        """Load env."""
        env: dict[str, str] = {}
        c = pod.get("spec", {}).get("containers", [{}])[0]
        for item in c.get("envFrom", []):
            cm_ref = item.get("configMapRef", {}).get("name")
            sec_ref = item.get("secretRef", {}).get("name")
            if cm_ref and cm_ref in configmaps:
                env.update(configmaps[cm_ref])
            if sec_ref and sec_ref in secrets:
                env.update(secrets[sec_ref])
        return env

    def decode_secret(self, secret: dict[str, Any]) -> dict[str, str]:
        """Decode secret."""
        decoded: dict[str, str] = {}
        for k, v in secret.get("data", {}).items():
            decoded[k] = base64.b64decode(v).decode("utf-8")
        return decoded


class VolumeBinder:
    """Volume binder."""

    def bind(self, pvs: list[dict[str, Any]], pvc: dict[str, Any]) -> str | None:
        """Bind."""
        req = (
            pvc.get("spec", {})
            .get("resources", {})
            .get("requests", {})
            .get("storage", "0Gi")
        )
        req_size = int(req.replace("Gi", ""))
        req_sc = pvc.get("spec", {}).get("storageClassName")
        req_modes = set(pvc.get("spec", {}).get("accessModes", []))
        for pv in pvs:
            cap = int(
                pv.get("spec", {})
                .get("capacity", {})
                .get("storage", "0Gi")
                .replace("Gi", "")
            )
            sc = pv.get("spec", {}).get("storageClassName")
            modes = set(pv.get("spec", {}).get("accessModes", []))
            if cap >= req_size and sc == req_sc and req_modes.issubset(modes):
                return pv.get("metadata", {}).get("name")
        return None


class HPAController:
    """HPA controller."""

    def desired_replicas(
        self,
        current_replicas: int,
        current_cpu: int,
        target_cpu: int,
        min_replicas: int,
        max_replicas: int,
    ) -> int:
        """Desired replicas."""
        if target_cpu <= 0:
            return current_replicas
        desired = int((current_replicas * current_cpu + target_cpu - 1) / target_cpu)
        return max(min_replicas, min(max_replicas, desired))


class HelmTemplater:
    """Helm templater."""

    pattern = re.compile(r"{{\s*\.Values\.([a-zA-Z0-9_.]+)\s*}}")

    def render(self, template: str, values: dict[str, Any]) -> str:
        """Render."""

        def lookup(key: str) -> str:
            """Lookup."""
            cur: Any = values
            for part in key.split("."):
                if isinstance(cur, dict):
                    cur = cur.get(part)
                else:
                    cur = None
            return "" if cur is None else str(cur)

        return self.pattern.sub(lambda m: lookup(m.group(1)), template)


@dataclass
class ClusterStateSimulator:
    """Cluster state simulator."""

    objects: dict[tuple[str, str], dict[str, Any]]

    def __init__(self) -> None:
        self.objects = {}

    def apply(self, manifest: dict[str, Any]) -> None:
        """Apply."""
        key = (manifest.get("kind", ""), manifest.get("metadata", {}).get("name", ""))
        self.objects[key] = copy.deepcopy(manifest)

    def delete(self, kind: str, name: str) -> None:
        """Delete."""
        self.objects.pop((kind, name), None)

    def get(self, kind: str, name: str) -> dict[str, Any] | None:
        """Get."""
        return self.objects.get((kind, name))
