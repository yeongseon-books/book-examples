"""Generated from book-content article."""

from dataclasses import dataclass

@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str


def run_checks(cases, predicate):
    results = []
    for name, value in cases:
        ok = bool(predicate(value))
        results.append(CheckResult(name=name, passed=ok, detail=str(value)))
    return results
