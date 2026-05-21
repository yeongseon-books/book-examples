"""Generated from book-content article."""

def safe_call(user_input: str, retrieved_docs: list[str]) -> str:
    user_detected = detect_pii(user_input)
    masked_input = mask_text(user_input, user_detected)

    masked_docs = [mask_text(d, detect_pii(d)) for d in retrieved_docs]

    response = llm.complete(SYSTEM_PROMPT, user=masked_input, context="\n".join(masked_docs))

    output_detected = detect_pii(response)
    if output_detected:
        log_pii_leak(output_detected, response)
        # Option 1: block
        # return "Response blocked due to detected personal information."
        # Option 2: mask and pass through
        response = mask_text(response, output_detected)

    return response
