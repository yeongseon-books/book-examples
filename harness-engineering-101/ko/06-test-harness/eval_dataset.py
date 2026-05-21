"""Generated from book-content article."""

@dataclass
class EvalExample:
    """A single eval example."""
    id: str
    input: dict
    expected: dict  # exact match or rubric-evaluated
    category: str  # "happy_path" | "edge" | "adversarial"
    source: str  # "production" | "synthetic" | "manual"

def build_eval_dataset() -> list[EvalExample]:
    """Balance the dataset across categories."""
    examples = []
    examples.extend(sample_from_production_logs(n=50, category="happy_path"))
    examples.extend(generate_synthetic_variations(n=30, category="happy_path"))
    examples.extend(load_manual_edge_cases(n=15, category="edge"))
    examples.extend(load_adversarial_examples(n=5, category="adversarial"))
    return examples
