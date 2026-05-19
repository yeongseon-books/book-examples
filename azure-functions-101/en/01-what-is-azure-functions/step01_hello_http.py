"""Azure Functions 101 - Episode 1: Hello http."""

from __future__ import annotations


def hello_http(params: dict[str, str]) -> str:
    """Hello http."""
    name = params.get("name", "world")
    return f"Hello, {name}!"


def run() -> dict[str, str]:
    """Run."""
    return {"response": hello_http({"name": "Sisyphus"})}


if __name__ == "__main__":
    print(run())
