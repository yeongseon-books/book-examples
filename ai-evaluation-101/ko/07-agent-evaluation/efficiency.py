# agent_eval/efficiency.py
def trajectory_metrics(agent_run: dict, expected_steps: int) -> dict:
    actual_steps = len(agent_run["steps"])
    return {
        "step_count":      actual_steps,
        "step_overhead":   actual_steps / expected_steps,  # 1.0 = optimal
        "total_latency_s": sum(s["latency_s"] for s in agent_run["steps"]),
        "total_tokens":    sum(s["tokens"] for s in agent_run["steps"]),
        "tool_calls":      sum(1 for s in agent_run["steps"] if "tool" in s),
    }

overheads = [trajectory_metrics(r, 4)["step_overhead"] for r in runs]
print(f"avg step overhead: {sum(overheads)/len(overheads):.2f}")
# avg step overhead: 1.8  ← agent uses ~2x more steps than needed
