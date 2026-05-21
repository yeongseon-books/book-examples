# rubric/agreement_per_dim.py
from sklearn.metrics import cohen_kappa_score

dimensions = ["correctness", "completeness", "clarity", "tone"]
for dim in dimensions:
    h = [s[dim] for s in human_scores]
    j = [s[dim] for s in judge_scores]
    k = cohen_kappa_score(h, j, weights="quadratic")
    print(f"{dim}: kappa={k:.3f}")
# correctness: kappa=0.78  ← trustworthy
# completeness: kappa=0.65 ← trustworthy
# clarity:     kappa=0.42  ← fair, prompt needs work
# tone:        kappa=0.31  ← weak, rewrite anchors
