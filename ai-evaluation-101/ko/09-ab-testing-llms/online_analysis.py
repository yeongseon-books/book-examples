# ab/online_analysis.py
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_sql("SELECT variant, thumbs_up FROM events WHERE experiment='...'", conn)
a = df[df.variant == "A"]["thumbs_up"]
b = df[df.variant == "B"]["thumbs_up"]
t, p = ttest_ind(a, b, equal_var=False)
print(f"A satisfaction: {a.mean():.3f}, B: {b.mean():.3f}, p={p:.4f}")
