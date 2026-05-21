"""Generated from book-content article."""

from collections.abc import Callable


@dataclass
class Rubric:
    """A bundle of scoring criteria."""
    name: str
    weight: float
    check: Callable[[dict, dict], float]  # (output, expected) -> 0.0..1.0

def has_required_sections(output: dict, expected: dict) -> float:
    required = expected.get("required_sections", [])
    if not required:
        return 1.0
    present = sum(1 for s in required if s in output.get("text", ""))
    return present / len(required)

def numbers_match(output: dict, expected: dict) -> float:
    e_nums = expected.get("numbers", {})
    o_nums = output.get("numbers", {})
    if not e_nums:
        return 1.0
    correct = sum(1 for k, v in e_nums.items() if abs(o_nums.get(k, 0) - v) < 0.01)
    return correct / len(e_nums)

def llm_judge_helpfulness(output: dict, expected: dict) -> float:
    """Have an LLM rate helpfulness from 0 to 1."""
    return 0.85  # actual: call judge LLM

RUBRICS = [
    Rubric("structure", weight=0.3, check=has_required_sections),
    Rubric("accuracy", weight=0.5, check=numbers_match),
    Rubric("helpfulness", weight=0.2, check=llm_judge_helpfulness),
]

def rubric_score(output: dict, expected: dict, rubrics=RUBRICS) -> float:
    return sum(r.check(output, expected) * r.weight for r in rubrics)
