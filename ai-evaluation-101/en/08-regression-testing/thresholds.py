# regression/thresholds.py
THRESHOLDS = {
    "exact_match":  0.80,   # Ep3
    "bleu":         0.40,
    "judge_score":  4.0,    # Ep4 on 1-5 scale
    "faithfulness": 0.85,   # Ep6 RAG
    "task_success": 0.90,   # Ep7 agent
}

FAIL_POLICY = "any"  # "any" | "majority" | "weighted"
