# Bad example
# Orchestrator manages even Worker internals
orchestrator.assign_task(code_agent, "Write a function")
orchestrator.review_code(code_agent.result)  # Should be Reviewer's job
orchestrator.refactor(code_agent.result)     # Removes Worker autonomy

# Good example
# Each agent has clear responsibilities
orchestrator.delegate("write_code", code_agent)  # Orchestrator only says "what" to do
# code_agent decides "how" to do it
review_agent.review(code_agent.result)
refactor_agent.refactor(code_agent.result)
