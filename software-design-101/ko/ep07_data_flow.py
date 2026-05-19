"""Software Design 101 - Episode 7: Data flow."""


def parse(raw: str) -> dict:
    """Parse."""
    key, value = raw.split("=")
    return {"key": key.strip(), "value": value.strip()}


def validate(data: dict) -> dict:
    """Validate."""
    if not data["value"]:
        raise ValueError("value required")
    return data


def transform(data: dict) -> dict:
    """Transform."""
    return {"key": data["key"].upper(), "value": data["value"].upper()}


def output(data: dict) -> str:
    """Output."""
    return f"{data['key']}:{data['value']}"


def run_pipeline(raw: str) -> str:
    """Run pipeline."""
    return output(transform(validate(parse(raw))))
