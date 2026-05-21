"""Generated from book-content article."""

GOLD_CASES = [
    {
        "input": "What kind of framework is FastAPI?",
        "must_contain": ["Python", "web"],
    },
    {
        "input": "What is 100 plus 200?",
        "must_contain": ["300"],
    },
]

def run_eval() -> dict[str, Any]:
    """Run evaluation against the golden dataset."""
    passed = 0
    failures = []
    for case in GOLD_CASES:
        agent = ResearchAgent()
        answer = agent.run(case["input"])
        if all(kw in answer for kw in case["must_contain"]):
            passed += 1
        else:
            failures.append({"input": case["input"], "answer": answer})
    return {
        "total": len(GOLD_CASES),
        "passed": passed,
        "pass_rate": passed / len(GOLD_CASES),
        "failures": failures,
    }

if __name__ == "__main__" and os.getenv("RUN_EVAL"):
    result = run_eval()
    print(json.dumps(result, ensure_ascii=False, indent=2))
