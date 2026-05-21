"""Generated from book-content article."""

from dataclasses import dataclass


@dataclass
class EvalCase:
    case_id: str
    prompt: str
    must_include: list[str]

def run_smoke_eval(cases: list[EvalCase], system_under_test) -> dict:
    failed_cases = []
    scores = []

    for case in cases:
        answer = system_under_test(case.prompt)
        matched = sum(1 for kw in case.must_include if kw.lower() in answer.lower())
        passed = matched == len(case.must_include)
        scores.append(int(passed))
        if not passed:
            failed_cases.append(
                {
                    "case_id": case.case_id,
                    "answer": answer,
                    "missing": [kw for kw in case.must_include if kw.lower() not in answer.lower()],
                }
            )

    return {
        "pass_rate": sum(scores) / len(scores),
        "failed_cases": failed_cases,
    }

smoke_cases = [
    EvalCase("rag-001", "What is RAG?", ["retrieval", "generation"]),
    EvalCase("async-001", "Explain async/await", ["coroutine", "await"]),
    EvalCase("json-001", "Return valid JSON with a title field", ["title"]),
]

report = run_smoke_eval(smoke_cases, summarize)
print(report)
