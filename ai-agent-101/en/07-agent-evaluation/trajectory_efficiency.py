"""Generated from book-content article."""

def evaluate_trajectory_efficiency(traj: Trajectory) -> dict:
    """Analyze trajectory efficiency."""
    tool_calls = [s for s in traj.steps if s.action == "tool_call"]
    thinks = [s for s in traj.steps if s.action == "think"]

    # Detect duplicate tool calls
    tool_signatures = [
        (s.input.get("tool"), str(s.input.get("args")))
        for s in tool_calls
    ]
    duplicate_calls = len(tool_signatures) - len(set(tool_signatures))

    return {
        "total_steps": len(traj.steps),
        "tool_calls": len(tool_calls),
        "thinking_steps": len(thinks),
        "duplicate_tool_calls": duplicate_calls,
        "total_duration_ms": sum(s.duration_ms for s in traj.steps),
        "avg_step_ms": sum(s.duration_ms for s in traj.steps) / len(traj.steps)
            if traj.steps else 0
    }

# Compare efficiency
traj_a = recorder_a.finalize("answer A", True)
traj_b = recorder_b.finalize("answer B", True)

eff_a = evaluate_trajectory_efficiency(traj_a)
eff_b = evaluate_trajectory_efficiency(traj_b)
# Same answer; fewer steps means more efficient
