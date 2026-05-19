"""
Step 03 — temperature 비교
======================================================
실행:
    python step03_temperature.py

같은 프롬프트를 temperature=0.0과 0.9로 각각 호출해
일관성과 다양성의 차이를 출력합니다.
"""

import os

from groq import Groq


def main() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    prompt = "FastAPI를 처음 배우는 개발자에게 세 문장으로 소개해 주세요."

    for temperature in (0.0, 0.9):
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "당신은 한국어 기술 블로그 편집자입니다. 간결하게 답하세요.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=temperature,
        )
        print(f"[temperature={temperature}]")
        print(completion.choices[0].message.content)
        print()


if __name__ == "__main__":
    main()
