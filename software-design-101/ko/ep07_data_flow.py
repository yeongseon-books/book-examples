def parse(raw: str) -> dict:
    key, value = raw.split("=")
    return {"key": key.strip(), "value": value.strip()}


def validate(data: dict) -> dict:
    if not data["value"]:
        raise ValueError("value required")
    return data


def transform(data: dict) -> dict:
    return {"key": data["key"].upper(), "value": data["value"].upper()}


def output(data: dict) -> str:
    return f"{data['key']}:{data['value']}"


def run_pipeline(raw: str) -> str:
    return output(transform(validate(parse(raw))))
