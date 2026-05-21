"""Generated from book-content article."""

def safe_chat(user_input: str) -> str:
    # 1. Input guardrail
    if not input_guardrail(user_input):
        return "Sorry, I cannot process that request."

    # 2. LLM call
    raw_output = llm.complete(user_input)

    # 3. Output guardrail
    if not output_guardrail(raw_output):
        return fallback_response()

    return raw_output
