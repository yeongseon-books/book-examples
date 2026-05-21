"""Generated from book-content article."""

def build_agent_prompt(role: dict, behaviors: list[str]) -> str:
    """Builds agent prompt separating role and behavior."""
    prompt = f"""
You are a {role['title']}.

Responsibilities:
{chr(10).join(f"- {r}" for r in role['responsibilities'])}

Behavior rules:
{chr(10).join(f"{i+1}. {b}" for i, b in enumerate(behaviors))}
"""
    return prompt

# Usage example
role = {
    "title": "Customer support agent",
    "responsibilities": [
        "Look up order status",
        "Accept refund requests",
        "Guide product information"
    ]
}

behaviors = [
    "First verify the user's order number",
    "Never ask for sensitive information (card number, password)",
    "Escalate unsolvable issues to human agents"
]

prompt = build_agent_prompt(role, behaviors)
