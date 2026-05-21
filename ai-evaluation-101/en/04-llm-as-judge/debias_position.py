# eval/debias_position.py
def judge_pairwise_debiased(question: str, ans_a: str, ans_b: str) -> str:
    v1 = judge_pairwise(question, ans_a, ans_b)  # A=ans_a, B=ans_b
    v2 = judge_pairwise(question, ans_b, ans_a)  # A=ans_b, B=ans_a (swapped)

    # In v2, "A" really means ans_b, so flip and compare
    flip = {"A": "B", "B": "A", "Tie": "Tie"}
    v2_normalized = flip[v2]

    if v1 == v2_normalized:
        return v1  # consistent
    return "Tie"  # if order changes the verdict, call it a tie
