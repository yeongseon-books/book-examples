from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_scaledobject_manifest_shape_ko() -> None:
    module = load_module(
        "ko/06-keda-internals/step01_keda_scaledobject_flow.py", "ep06_ko"
    )
    doc = module.build_scaledobject("queue-worker", "worker", "orders")
    assert doc["kind"] == "ScaledObject"
    assert doc["spec"]["minReplicaCount"] == 0


def test_scale_to_zero_boundary_en() -> None:
    module = load_module(
        "en/06-keda-internals/step01_keda_scaledobject_flow.py", "ep06_en"
    )
    assert module.scale_to_zero_boundary(3, active=False) == 0
    assert module.scale_to_zero_boundary(0, active=True) == 1
