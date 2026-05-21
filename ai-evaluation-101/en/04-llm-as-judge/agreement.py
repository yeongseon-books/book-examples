# eval/agreement.py
from sklearn.metrics import cohen_kappa_score

# Human grader scores 50 samples on a 1-5 scale
human_scores  = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5, ...]  # len=50
judge_scores  = [5, 4, 4, 5, 2, 3, 5, 3, 4, 4, ...]  # len=50

# Cohen's kappa: -1 to 1 (1=perfect, 0=chance, <0=worse than random)
kappa = cohen_kappa_score(human_scores, judge_scores, weights="quadratic")
print(f"Cohen's kappa: {kappa:.3f}")

# Interpretation (Landis & Koch, 1977):
# 0.0-0.2: slight
# 0.2-0.4: fair
# 0.4-0.6: moderate
# 0.6-0.8: substantial
# 0.8-1.0: almost perfect
