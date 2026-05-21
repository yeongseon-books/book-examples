# regression/golden_dataset.py
import json

GOLDEN = [
    # Top usage cases
    {"id": "freq-001", "input": "today's weather", "expected_intent": "weather_query"},
    {"id": "freq-002", "input": "change my password", "expected_intent": "account_password"},

    # Past regressions (with commit reference)
    {"id": "reg-001", "input": "where is my order?",
     "expected_contains": ["order", "status"],
     "note": "v1.2 returned 'item' instead of 'order' (PR #234)"},

    # Edge cases
    {"id": "edge-001", "input": "", "expected_behavior": "ask_clarification"},
    {"id": "edge-002", "input": "asdfgh", "expected_behavior": "ask_clarification"},
    {"id": "edge-003", "input": "Hi! I'm John. Actually I'm Mike. No wait, Sarah.",
     "expected_behavior": "ask_clarification"},
]

with open("regression/golden.jsonl", "w") as f:
    for item in GOLDEN:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
