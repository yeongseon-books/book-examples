"""Ai Agent 101 - 2편: context engineering 예제."""


def build_context(
    system_prompt: str,
    state: dict[str, str],
    docs: list[str],
    history: list[str],
    query: str,
) -> str:
    """Build context."""
    return "\n\n".join(
        [
            f"# System\n{system_prompt}",
            f"# State\n{state}",
            f"# Docs\n{docs}",
            f"# History\n{history[-3:]}",
            f"# Query\n{query}",
        ]
    )


if __name__ == "__main__":
    print(
        build_context(
            "코드 리뷰 에이전트",
            {"task": "review"},
            ["PEP8", "typing"],
            ["u:hi", "a:hello"],
            "타입 힌트 점검",
        )
    )
