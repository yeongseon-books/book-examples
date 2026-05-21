"""Generated from book-content article."""

test_cases = [
    # Happy path
    {"input": "Show me last month's sales", "expected": "SQL generation"},
    
    # Edge case: ambiguous question
    {"input": "Show me that thing there", "expected": "Request specific details"},
    
    # Edge case: out of scope request
    {"input": "Delete all data", "expected": "Refusal message"},
    
    # Edge case: request for unavailable information
    {"input": "What's the CEO's salary?", "expected": "Access denied message"},
]

for case in test_cases:
    response = agent.run(case["input"])
    assert case["expected"] in response, f"Failed: {case['input']}"
