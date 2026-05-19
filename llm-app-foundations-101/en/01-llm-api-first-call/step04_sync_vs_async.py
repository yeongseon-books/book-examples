\
"""
Step 04 — Sync vs async patterns
======================================================
Run:
    python step04_sync_vs_async.py

Compare synchronous and asynchronous Groq calls,
then run three async requests in parallel with asyncio.gather.
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
                "content": "Explain asynchronous programming in one paragraph.",
            }
        ],
    )
    print("[sync]")
    print(completion.choices[0].message.content)


async def async_call() -> None:
    client = AsyncGroq(api_key=os.environ["GROQ_API_KEY"])
    completion = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": "Describe two situations where asyncio is useful.",
            }
        ],
    )
    print("\n[async]")
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
        "Explain the difference between a list and a tuple.",
        "Explain the core features of a Python dictionary.",
        "Explain why exception handling matters.",
    ]
    answers = await asyncio.gather(*(ask(question) for question in questions))

    print("\n[parallel async — 3 questions at once]")
    for idx, answer in enumerate(answers, start=1):
        print(f"[{idx}] {answer}\n")


def main() -> None:
    sync_call()
    asyncio.run(async_call())
    asyncio.run(parallel_calls())


if __name__ == "__main__":
    main()
