def parse_key_value(text: str) -> dict[str, str]:
    pairs = [chunk.strip() for chunk in text.split(",") if chunk.strip()]
    result: dict[str, str] = {}
    for pair in pairs:
        if "=" not in pair:
            raise ValueError(f"Invalid pair: {pair}")
        key, value = [item.strip() for item in pair.split("=", 1)]
        result[key] = value
    return result
