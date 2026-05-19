REQUIRED_SECTIONS = [
    "functional_requirements",
    "non_functional_requirements",
    "capacity_estimates",
    "api",
    "data_model",
    "components",
]


def generate_spec(prompt: str) -> dict:
    return {
        "prompt": prompt,
        "functional_requirements": ["shorten", "redirect", "analytics"],
        "non_functional_requirements": ["99.99% availability", "low latency"],
        "capacity_estimates": {"read_qps": 1000, "write_qps": 10},
        "api": ["POST /shorten", "GET /{code}"],
        "data_model": ["short_code", "original_url", "created_at"],
        "components": ["lb", "api", "kv_store", "cache", "analytics"],
    }


def is_complete_spec(spec: dict) -> bool:
    return all(key in spec and spec[key] for key in REQUIRED_SECTIONS)
