from __future__ import annotations

from common import BundleSimulator


def run_demo() -> dict[str, int]:
    sim = BundleSimulator()
    bundle = sim.concat(["const a = 1;", "const b = 2;", "console.log(a+b);"])
    mini = sim.minify(bundle)
    return {
        "raw": sim.estimate_size(bundle),
        "min": sim.estimate_size(mini),
    }
