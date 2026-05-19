"""
Step 05 — 토큰 예산 초과 감지
======================================================
실행:
    python step05_token_budget_guard.py

문자 수 기반 rough 추정으로 입력 토큰이 예산을 넘는지
미리 확인하고 필요하면 이력을 잘라내는 유틸 함수입니다.
"""


def rough_token_count(messages: list[dict[str, str]]) -> int:
    total_chars = sum(len(message["content"]) for message in messages)
    overhead = len(messages) * 12
    return (total_chars // 4) + overhead


def enforce_budget(
    messages: list[dict[str, str]],
    max_input_tokens: int = 6000,
) -> list[dict[str, str]]:
    if rough_token_count(messages) <= max_input_tokens:
        return messages

    trimmed = messages[:1] + messages[-8:]
    if rough_token_count(trimmed) <= max_input_tokens:
        print(f"이력을 {len(messages) - len(trimmed)}개 잘라냈습니다.")
        return trimmed

    raise ValueError("대화 이력이 너무 깁니다. 더 강한 요약이 필요합니다.")


def main() -> None:
    system = {"role": "system", "content": "당신은 도우미입니다."}
    short_history = [system] + [
        {
            "role": "user" if index % 2 == 0 else "assistant",
            "content": f"메시지 {index}",
        }
        for index in range(10)
    ]
    long_history = [system] + [
        {"role": "user" if index % 2 == 0 else "assistant", "content": "x" * 200}
        for index in range(200)
    ]

    print(f"short_history rough tokens: {rough_token_count(short_history)}")
    result = enforce_budget(short_history)
    print(f"after enforce: {len(result)} messages\n")

    print(f"long_history rough tokens: {rough_token_count(long_history)}")
    try:
        result = enforce_budget(long_history, max_input_tokens=3000)
        print(f"after enforce: {len(result)} messages")
    except ValueError as exc:
        print(f"예외: {exc}")


if __name__ == "__main__":
    main()
