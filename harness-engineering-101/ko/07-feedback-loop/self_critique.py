"""Generated from book-content article."""

def self_critique(agent, draft: str, criteria: list[str]) -> tuple[bool, str]:
    """Have the agent review its own draft."""
    critique_prompt = f"""Review the following draft against these criteria.

Criteria:
{chr(10).join(f'- {c}' for c in criteria)}

Draft:
{draft}

Respond in JSON:
{{
  "passes_all": true/false,
  "violations": ["criterion that failed: reason"],
  "suggested_fix": "concrete change to make"
}}"""
    response = agent.complete(critique_prompt)
    parsed = parse_json(response)
    return parsed["passes_all"], parsed.get("suggested_fix", "")

def generate_with_critique(agent, prompt: str, criteria: list[str], max_rounds: int = 3) -> str:
    draft = agent.complete(prompt)
    for _ in range(max_rounds):
        passes, fix = self_critique(agent, draft, criteria)
        if passes:
            return draft
        draft = agent.complete(f"{prompt}\n\nPrevious draft:\n{draft}\n\nApply this fix: {fix}")
    return draft
