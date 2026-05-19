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


def test_overlay_profile_has_pod_cidr_ko() -> None:
    module = load_module(
        "ko/03-cni-and-azure-cni-overlay/step01_network_mode_model.py", "ep03_ko"
    )
    profile = module.build_network_profile("overlay")
    assert profile["networkPluginMode"] == "overlay"
    assert profile["podCidr"] == "10.244.0.0/16"


def test_network_yaml_has_mode_en() -> None:
    module = load_module(
        "en/03-cni-and-azure-cni-overlay/step01_network_mode_model.py", "ep03_en"
    )
    payload = module.network_profile_yaml("pod-subnet")
    assert "networkPluginMode: transparent" in payload
