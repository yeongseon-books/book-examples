import os
import time

from groq import APIStatusError, Groq


def stream_with_timeout(client: Groq, prompt: str, timeout_sec: float = 10.0) -> str:
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    parts: list[str] = []
    deadline = time.monotonic() + timeout_sec

    try:
        for chunk in stream:
            if time.monotonic() > deadline:
                print("\n[타임아웃: 지금까지 받은 부분 결과를 반환합니다.]")
                break
            delta = chunk.choices[0].delta.content
            if delta:
                parts.append(delta)
                print(delta, end="", flush=True)
    except APIStatusError as exc:
        print(f"\n[APIStatusError {exc.status_code}] {exc.message}")

    return "".join(parts)


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    result = stream_with_timeout(
        client,
        "파이썬 asyncio 이벤트 루프를 설명해 주세요.",
        timeout_sec=8.0,
    )
    print(f"\n\n수집한 글자 수: {len(result)}")


if __name__ == "__main__":
    main()
