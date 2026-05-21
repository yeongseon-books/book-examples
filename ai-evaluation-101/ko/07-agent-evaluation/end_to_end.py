# agent_eval/end_to_end.py
def end_to_end_success(agent_run: dict) -> bool:
    return agent_run["final_state"]["email_sent"] is True
