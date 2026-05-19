from common import ApiResponse


def fetch_exchange_rate(http_get, base: str = "USD") -> float:
    resp: ApiResponse = http_get(f"https://example.invalid/rates?base={base}")
    if resp.status_code != 200:
        raise RuntimeError("service unavailable")
    return float(resp.payload["rate"])
