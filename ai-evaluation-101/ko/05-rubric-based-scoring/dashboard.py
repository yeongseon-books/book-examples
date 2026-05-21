# rubric/dashboard.py
import pandas as pd
df = pd.DataFrame(scored_responses)
print(df[["correctness","completeness","clarity","tone"]].describe())
#         올바른 방식: complete  clarity  tone
# mean      4.2      4.5      3.8      4.7
# min       1        2        1        3
