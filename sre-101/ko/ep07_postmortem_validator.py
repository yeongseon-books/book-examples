REQUIRED = ["Summary", "Impact", "Timeline", "Root Cause", "Actions"]
BLAME_WORDS = ["fault", "stupid", "careless", "blame"]


def validate_sections(doc: str) -> list[str]:
    missing = []
    for sec in REQUIRED:
        if f"## {sec}" not in doc:
            missing.append(sec)
    return missing


def blameless_issues(doc: str) -> list[str]:
    lower = doc.lower()
    return [w for w in BLAME_WORDS if w in lower]
