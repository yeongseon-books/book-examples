from __future__ import annotations

from common import RouterSim


def run_demo() -> tuple[str, str]:
    router = RouterSim(
        routes={
            "/": lambda _: "home",
            "/users/:id": lambda p: f"user:{p['id']}",
            "*": lambda _: "404",
        }
    )
    return router.navigate("/users/42"), router.navigate("/missing")
