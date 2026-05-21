# agent_eval/step_level.py
expected_trajectory = [
    {"tool": "read_calendar", "args_match": lambda a: "week" in a.get("range", "")},
    {"tool": "read_emails",   "args_match": lambda a: a.get("limit", 0) <= 10},
    {"tool": "summarize",     "args_match": lambda a: True},
    {"tool": "send_email",    "args_match": lambda a: "@" in a.get("to", "")},
]

def step_match_score(actual: list[dict], expected: list[dict]) -> float:
    matches = 0
    for i, exp in enumerate(expected):
        if i >= len(actual):
            break
        a = actual[i]
        if a["tool"] == exp["tool"] and exp["args_match"](a["args"]):
            matches += 1
    return matches / len(expected)
