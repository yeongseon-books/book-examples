from __future__ import annotations


def build_invoice(payload: dict[str, int]) -> dict[str, int]:
    return {"id": payload["order_id"], "amount": payload["total"]}


def process_order(payload: dict[str, int]) -> dict[str, int]:
    return build_invoice(payload)


def run() -> dict[str, int]:
    return process_order({"order_id": 101, "total": 35000})


if __name__ == "__main__":
    print(run())
