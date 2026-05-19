\
"""
Step 04 — 동기 vs 비동기 패턴
======================================================
실행:
    python step04_sync_vs_async.py

동기(Groq)와 비동기(AsyncGroq) 호출 패턴을 나란히 보여줍니다.
마지막에 asyncio.gather로 세 질문을 병렬 호출하는 예제도 포함합니다.
"""
import asyncio
import os

from groq import AsyncGroq, Groq


def sync_call() -> None:
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "비동기 프로그래밍을 한 문단으로 설명해 주세요.",
            }
        ],
    )
    print("[동기 호출]")
    print(completion.choices[0].message.content)


async def async_call() -> None:
    client = AsyncGroq(api_key=os.environ["GROQ_API_KEY"])
    completion = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "asyncio가 필요한 상황을 두 가지로 설명해 주세요.",
            }
        ],
    )
    print("\n[비동기 호출]")
    print(completion.choices[0].message.content)


async def parallel_calls() -> None:
    client = AsyncGroq(api_key=os.environ["GROQ_API_KEY"])

    async def ask(question: str) -> str:
        completion = await client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": question}],
        )
        return completion.choices[0].message.content or ""

    questions = [
        "리스트와 튜플의 차이를 설명해 주세요.",
        "파이썬 딕셔너리의 핵심 특징을 설명해 주세요.",
        "예외 처리가 필요한 이유를 설명해 주세요.",
    ]
    answers = await asyncio.gather(*(ask(question) for question in questions))

    print("\n[병렬 비동기 호출 — 질문 3개]")
    for idx, answer in enumerate(answers, start=1):
        print(f"[{idx}] {answer}\n")


def main() -> None:
    sync_call()
    asyncio.run(async_call())
    asyncio.run(parallel_calls())


if __name__ == "__main__":
    main()
