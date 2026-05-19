from __future__ import annotations

# pyright: reportMissingImports=false, reportUnknownVariableType=false, reportUnknownMemberType=false, reportUnknownArgumentType=false

# English note: offline validation example.


def run() -> dict[str, object]:
    lifecycle = ["created", "running", "stopped", "removed"]
    immutable_image = True
    return {"success": True, "lifecycle": lifecycle, "immutable_image": immutable_image}


if __name__ == "__main__":
    print(run())
