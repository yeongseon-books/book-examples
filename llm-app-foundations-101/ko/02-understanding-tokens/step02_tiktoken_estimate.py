\
"""
Step 02 — tiktoken으로 토큰 수 사전 추정
======================================================
실행:
    python step02_tiktoken_estimate.py

tiktoken cl100k_base 인코딩으로 문자열과 메시지 목록의
토큰 수를 미리 추정합니다. Groq 청구값의 근사치입니다.
"""
import tiktoken


def count_tokens(text: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(text))


def estimate_messages_tokens(messages: list[dict[str, str]]) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    serialized = "\n".join(f"{m['role']}: {m['content']}" for m in messages)
    return len(encoding.encode(serialized))


def main() -> None:
    samples = [
        "hello world",
        "unbelievable",
        'print(user_profile[0]["email"])',
        "토큰 길이를 미리 재면 긴 프롬프트를 더 안전하게 다룰 수 있습니다.",
    ]

    print("=== 단일 문자열 토큰 수 ===")
    for text in samples:
        tokens = count_tokens(text)
        print(f"{tokens:3d} tokens | {text!r}")

    messages = [
        {"role": "system", "content": "당신은 간결하게 설명하는 파이썬 튜터입니다."},
        {"role": "user", "content": "리스트와 튜플의 차이를 설명해 주세요."},
        {"role": "assistant", "content": "리스트는 변경 가능하고, 튜플은 변경 불가능합니다."},
        {"role": "user", "content": "예제 코드도 짧게 덧붙여 주세요."},
    ]

    estimated = estimate_messages_tokens(messages)
    print("\n=== 메시지 토큰 추정치 ===")
    print(f"estimated_prompt_tokens={estimated}")
    print("Groq 실제 청구값과 약간 다를 수 있습니다.")


if __name__ == "__main__":
    main()
