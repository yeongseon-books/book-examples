# agent_eval/dashboard.py
import pandas as pd

results = []
for run in agent_runs:  # 100 runs
    results.append({
        "task_success":    end_to_end_success(run),
        "tool_f1":         step_match_score(run["steps"], expected),
        "step_overhead":   trajectory_metrics(run, 4)["step_overhead"],
        "recovered":       evaluate_recovery(run) in ("RETRIED", "ALTERNATIVE"),
    })

df = pd.DataFrame(results)
print(df.describe())
#                  task_success  tool_f1  step_overhead  recovered
# mean             0.78          0.85     1.6            0.72
# std              0.41          0.18     0.7            0.45
