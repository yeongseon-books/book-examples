from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
from common import ImageLayerSimulator

# English note: offline validation example.


def run() -> dict[str, object]:
    simulator = ImageLayerSimulator()
    builder = [
        {"name": "deps", "size_mb": 240},
        {"name": "build-cache", "size_mb": 120},
    ]
    runtime = [{"name": "python-slim", "size_mb": 80}, {"name": "app", "size_mb": 35}]
    result = simulator.compare_multistage(builder, runtime)
    return {"success": result["saved"] > 0, "estimate": result}


if __name__ == "__main__":
    print(run())
