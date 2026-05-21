"""Generated from book-content article."""

def run_regression():
    suites = {
        "jailbreak_attacks": load_jailbreak_set(),
        "benign_prompts": load_benign_set(),
        "pii_examples": load_pii_set(),
        "moderation_cases": load_moderation_set(),
        "rag_grounding": load_rag_set(),
    }
    return {name: evaluate_pipeline(pipeline, cases) for name, cases in suites.items()}
