"""Generated from book-content article."""

from dataclasses import dataclass

@dataclass
class InjectionCheckResult:
    is_injection: bool
    layer: str | None
    reason: str | None

def check_injection(user_input: str) -> InjectionCheckResult:
    # Layer 1: regex (fast, free)
    if pattern := detect_direct_injection(user_input):
        return InjectionCheckResult(True, "regex", pattern)

    # Layer 2: embedding similarity (medium cost)
    if detect_by_similarity(user_input, threshold=0.78):
        return InjectionCheckResult(True, "embedding", "high similarity to known injection")

    # Layer 3: LLM judge (most expensive, strongest)
    if llm_injection_judge(user_input):
        return InjectionCheckResult(True, "llm_judge", "judge classified as injection")

    return InjectionCheckResult(False, None, None)

def safe_pipeline(user_input: str, retrieved_docs: list[tuple[str, str]]) -> str:
    check = check_injection(user_input)
    if check.is_injection:
        log_injection_attempt(user_input, check)
        return "Sorry, I cannot process that request."

    safe_docs = "\n\n".join(sanitize_external_content(c, src) for src, c in retrieved_docs)
    return llm.complete(SYSTEM_PROMPT, user=user_input, context=safe_docs)
