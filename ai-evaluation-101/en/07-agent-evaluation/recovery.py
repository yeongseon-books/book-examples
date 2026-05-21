# agent_eval/recovery.py
def evaluate_recovery(agent_run: dict) -> str:
    steps = agent_run["steps"]
    for i, s in enumerate(steps):
        if s.get("tool_result", {}).get("error"):
            if i + 1 >= len(steps):
                return "GAVE_UP"
            next_step = steps[i + 1]
            if next_step.get("tool") == s["tool"]:
                return "RETRIED"
            if "tool" in next_step:
                return "ALTERNATIVE"
            return "GAVE_UP"
    return "NO_FAILURE"

# 50 runs with injected failures
results = [evaluate_recovery(r) for r in fault_injected_runs]
from collections import Counter
print(Counter(results))
# Counter({'RETRIED': 30, 'ALTERNATIVE': 12, 'GAVE_UP': 8})
# → 16% of cases the agent gave up. Reinforce recovery in the prompt.
