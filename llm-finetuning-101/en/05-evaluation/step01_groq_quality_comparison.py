"""Compare response quality before and after fine-tuning with Groq"""

from __future__ import annotations

import os
import textwrap
from typing import Any

try:
    from groq import Groq
except ImportError:
    Groq = None

MODEL = os.getenv('GROQ_MODEL', 'llama-3.1-8b-instant')


def complete(client: Any, system_prompt: str, user_prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def judge(client: Any, prompt: str, first: str, second: str) -> str:
    judge_prompt = textwrap.dedent(
        f"""
        Pick the better answer and explain why in up to three lines.

        Question:
        {prompt}

        Answer A:
        {first}

        Answer B:
        {second}
        """
    ).strip()
    return complete(client, 'You are an evaluator. Check accuracy, specificity, and tone.', judge_prompt)


def main() -> None:
    if Groq is None:
        print('Skipping comparison because the groq package is unavailable.')
        return

    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        print('Skipping comparison because GROQ_API_KEY is missing.')
        return

    client = Groq(api_key=api_key)
    prompt = 'Answer the following customer question: "How long are audit logs retained on the new pricing plan?"'
    base_answer = complete(client, 'You are a generic assistant. Provide a reasonable general answer.', prompt)
    tuned_answer = complete(client, 'You are a customer-support model trained on PulseBoard documentation. Mention retention period, plan limits, and the escalation path.', prompt)
    verdict = judge(client, prompt, base_answer, tuned_answer)

    print('Answer A')
    print('-' * 80)
    print(base_answer)
    print()
    print('Answer B')
    print('-' * 80)
    print(tuned_answer)
    print()
    print('Evaluation verdict')
    print('-' * 80)
    print(verdict)


if __name__ == '__main__':
    main()
