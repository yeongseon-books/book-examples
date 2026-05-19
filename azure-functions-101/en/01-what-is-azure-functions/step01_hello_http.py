from __future__ import annotations


def hello_http(params: dict[str, str]) -> str:
    name = params.get("name", "world")
    return f"Hello, {name}!"


def run() -> dict[str, str]:
    return {"response": hello_http({"name": "Sisyphus"})}


if __name__ == "__main__":
    print(run())
