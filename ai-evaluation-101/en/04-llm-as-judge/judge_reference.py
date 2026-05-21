# eval/judge_reference.py
REFERENCE_PROMPT = """Decide whether the answer is semantically equivalent to the reference.

Question: {question}
Reference: {reference}
Answer: {answer}

If the answer covers all the key points of the reference, output 'PASS'. Otherwise 'FAIL'.
Write a one-sentence reasoning, then output only 'Result: PASS' or 'Result: FAIL' on the last line.
"""
