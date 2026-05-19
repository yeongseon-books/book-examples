from __future__ import annotations

from common import python_functions_with_docstrings, readability_score, todo_count


def combined_quality_report(code_text: str) -> dict[str, float]:
    total, documented = python_functions_with_docstrings(code_text)
    doc_cov = 0.0 if total == 0 else documented / total
    debt = todo_count(code_text)
    debt_penalty = debt["TODO"] * 0.05 + debt["FIXME"] * 0.1
    lines = [line for line in code_text.splitlines() if line.strip()]
    readability = readability_score(lines) / 100
    maintainability = max(0.0, min(1.0, 0.5 * doc_cov + 0.5 * readability - debt_penalty))
    return {
        "testability": round(doc_cov, 2),
        "readability": round(readability, 2),
        "maintainability": round(maintainability, 2),
    }
