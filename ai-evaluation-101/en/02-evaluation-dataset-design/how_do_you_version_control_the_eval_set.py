"""Generated from book-content article."""

import json
from pathlib import Path


def save_eval_set(eval_set: list[EvalExample], path: Path):
    with path.open("w") as f:
        for ex in eval_set:
            f.write(json.dumps({
                "id": ex.id,
                "input": ex.input,
                "expected": ex.expected,
                "category": ex.category,
                "notes": ex.notes,
            }, ensure_ascii=False) + "\n")

def load_eval_set(path: Path) -> list[EvalExample]:
    with path.open() as f:
        return [EvalExample(**json.loads(line)) for line in f]
