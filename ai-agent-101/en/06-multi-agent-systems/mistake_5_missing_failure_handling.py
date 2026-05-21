# Bad example
# Whole system stops if any agent fails
def run_pipeline():
    result1 = agent1.execute(task)  # Failure here halts everything
    result2 = agent2.execute(result1)
    return result2

# Good example
# Add retry, fallback, and graceful-degradation logic
def run_pipeline():
    try:
        result1 = agent1.execute(task)
    except AgentError:
        result1 = fallback_agent.execute(task)  # Alternative agent

    try:
        result2 = agent2.execute(result1)
    except AgentError:
        result2 = result1  # Fall back to previous step's result

    return result2
