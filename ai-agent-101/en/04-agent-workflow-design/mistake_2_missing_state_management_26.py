"""Generated from book-content article."""

def resilient_workflow(task_id: str, task: str) -> str:
    """Workflow with state persistence"""
    state = load_or_create_state(task_id, task)

    if state.current_step < 1:
        step1_result = execute_step1(task)
        state.context["step1"] = step1_result
        state.current_step = 1
        save_state(state)

    if state.current_step < 2:
        step2_result = execute_step2(state.context["step1"])
        state.context["step2"] = step2_result
        state.current_step = 2
        save_state(state)

    if state.current_step < 3:
        step3_result = execute_step3(state.context["step2"])
        state.context["step3"] = step3_result
        state.current_step = 3
        save_state(state)

    return state.context["step3"]
