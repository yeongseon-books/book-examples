"""Generated from book-content article."""

few_shot_examples = {
    "sql_generation": [
        {"input": "Last month's top 10 sales", "output": "SELECT * FROM sales WHERE month = LAST_MONTH ORDER BY amount DESC LIMIT 10;"},
        {"input": "Number of customers in Seoul", "output": "SELECT COUNT(*) FROM customers WHERE city='Seoul';"}
    ],
    "email_draft": [
        {"input": "Meeting schedule change notification", "output": "Hello. The scheduled meeting has been changed as follows..."},
        {"input": "Product inquiry response", "output": "Thank you for your inquiry. Regarding the product..."}
    ]
}

def inject_examples(task_type: str, base_prompt: str) -> str:
    """Adds examples matching task type to prompt."""
    examples = few_shot_examples.get(task_type, [])
    if not examples:
        return base_prompt

    example_text = "\n\nExamples:\n"
    for i, ex in enumerate(examples, 1):
        example_text += f"Example {i}:\nInput: {ex['input']}\nOutput: {ex['output']}\n\n"

    return base_prompt + example_text
