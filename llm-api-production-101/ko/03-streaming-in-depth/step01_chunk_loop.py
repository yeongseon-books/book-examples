import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    stream = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "TCP/IP 4계층을 각 층마다 한 줄씩 설명해 주세요."}
        ],
        stream=True,
    )

    parts: list[str] = []
    empty_count = 0

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta is None:
            empty_count += 1
            continue
        parts.append(delta)
        print(delta, end="", flush=True)

    print(f"\n\n총 글자 수={len(''.join(parts))} 빈 청크 수={empty_count}")


if __name__ == "__main__":
    main()
