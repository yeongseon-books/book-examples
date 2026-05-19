from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Protocol, cast

from fastapi import FastAPI
from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str) -> ModuleType:
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Ep01Module(Protocol):
    app: FastAPI

    def az_show_command(self, cluster_name: str, resource_group: str) -> str: ...


def test_control_plane_fastapi_surface_ko() -> None:
    module = cast(
        Ep01Module,
        load_module(
            "ko/01-control-plane-anatomy/step01_control_plane_boundary.py", "ep01_ko"
        ),
    )
    client = TestClient(module.app)
    response = client.get("/control-plane")
    assert response.status_code == 200
    body = response.json()
    assert body["managed_by"] == "microsoft"
    assert "kube-apiserver" in body["model"]["control_plane"]


def test_control_plane_command_preview_en() -> None:
    module = cast(
        Ep01Module,
        load_module(
            "en/01-control-plane-anatomy/step01_control_plane_boundary.py", "ep01_en"
        ),
    )
    cmd = module.az_show_command("my-cluster", "my-rg")
    assert "az aks show" in cmd
    assert "--query" in cmd
