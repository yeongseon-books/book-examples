from __future__ import annotations


def choose_plan(
    needs_vnet: bool, strict_cold_start: bool, existing_app_service: bool
) -> str:
    if existing_app_service:
        return "Dedicated"
    if strict_cold_start:
        return "Premium"
    if needs_vnet:
        return "Flex Consumption"
    return "Consumption"


def run() -> dict[str, str]:
    return {"plan": choose_plan(True, False, False)}


if __name__ == "__main__":
    print(run())
