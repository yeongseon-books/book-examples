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


def test_hpa_ratio_math_ko() -> None:
    module = load_module(
        "ko/05-hpa-and-cluster-autoscaler-internals/step01_hpa_ca_loops.py", "ep05_ko"
    )
    assert module.desired_replicas(3, 140.0, 70.0) == 6


def test_ca_profile_and_scale_signal_en() -> None:
    module = load_module(
        "en/05-hpa-and-cluster-autoscaler-internals/step01_hpa_ca_loops.py", "ep05_en"
    )
    profile = module.aks_autoscaler_profile()
    assert profile["scan-interval"] == "10s"
    assert module.ca_scale_up_needed(pending_pods=5, free_node_slots=2)
