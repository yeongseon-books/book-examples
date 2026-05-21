# eval/judge_pairwise.py
PAIRWISE_PROMPT = """Pick the better answer to the question.

Question: {question}
Answer A: {answer_a}
Answer B: {answer_b}

Respond with one of: 'A', 'B', 'Tie'.
Write a one-sentence reasoning first, then output only 'Verdict: X' on the last line.
"""

def judge_pairwise(question: str, answer_a: str, answer_b: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": PAIRWISE_PROMPT.format(
            question=question, answer_a=answer_a, answer_b=answer_b
        )}],
        temperature=0,
    )
    text = response.choices[0].message.content
    last_line = text.strip().split("\n")[-1]
    return last_line.replace("Verdict:", "").strip()
