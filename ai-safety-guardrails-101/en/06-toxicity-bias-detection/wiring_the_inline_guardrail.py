"""Generated from book-content article."""

def safe_generate(prompt: str) -> str:
    output = llm.generate(prompt)
    verdict = classify_toxicity(output)
    if verdict["triggered"]:
        log_blocked_output(output, verdict)
        return "We can't process that request. Please rephrase and try again."
    return output
