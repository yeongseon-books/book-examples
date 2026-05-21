# eval/judge_single.py
from openai import OpenAI

client = OpenAI()

JUDGE_PROMPT = """You are a strict evaluator. Read the question and answer below and grade on a 1-5 scale.

Question: {question}
Answer: {answer}

Rubric:
- 5: Accurate, complete, clear
- 4: Accurate but missing minor details or slightly ambiguous
- 3: Partially accurate
- 2: Mostly inaccurate
- 1: Completely wrong or off-topic

Write a one-sentence reasoning first, then output only 'Score: N' on the last line.
"""

def judge_single(question: str, answer: str) -> tuple[int, str]:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": JUDGE_PROMPT.format(
            question=question, answer=answer
        )}],
        temperature=0,  # reproducibility
    )
    text = response.choices[0].message.content
    last_line = text.strip().split("\n")[-1]
    score = int(last_line.replace("Score:", "").strip())
    return score, text

if __name__ == "__main__":
    score, reasoning = judge_single(
        "What is the difference between list and tuple in Python?",
        "Lists are mutable and tuples are immutable."
    )
    print(f"Score: {score}\nReasoning: {reasoning}")
