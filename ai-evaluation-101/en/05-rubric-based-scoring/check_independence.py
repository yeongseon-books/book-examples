# rubric/check_independence.py
import pandas as pd

df = pd.DataFrame({
    "correctness": [5, 4, 3, 5, 2, ...],
    "clarity":     [4, 3, 4, 5, 3, ...],
    "tone":        [5, 5, 3, 4, 4, ...],
})
print(df.corr())
# Correlation > 0.9 means the two dimensions are effectively the same
# → merge or drop one
