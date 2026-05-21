# Bad
def evaluate(agent, task):
    result = agent.run(task)
    return result == expected_answer

# Good
def evaluate(agent, task):
    recorder = TrajectoryRecorder(task["id"])
    result = agent.run(task, recorder=recorder)
    traj = recorder.finalize(result, result == expected_answer)
    eff = evaluate_trajectory_efficiency(traj)
    return {
        "correct": result == expected_answer,
        "efficient": eff["tool_calls"] <= task["max_tool_calls"],
        "no_duplicates": eff["duplicate_tool_calls"] == 0
    }
