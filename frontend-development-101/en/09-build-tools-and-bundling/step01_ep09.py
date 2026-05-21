"""Frontend Development 101 - Episode 9: build tools and bundling example."""

from __future__ import annotations

from common import BundleSimulator


def run_demo() -> dict[str, int]:
    """Run demo."""
    sim = BundleSimulator()
    bundle = sim.concat(["const a = 1;", "const b = 2;", "console.log(a+b);"])
    mini = sim.minify(bundle)
    return {
        "raw": sim.estimate_size(bundle),
        "min": sim.estimate_size(mini),
    }
