"""Generated from book-content article."""

def resume_agent_workflow(task_id: str, state_manager: StateManager) -> str:
    """Resume interrupted workflow"""

    # Load saved state
    state = state_manager.load_state(task_id)

    print(f"Resuming task: {state.goal}")
    print(f"Progress: {state.current_step}/{len(state.completed_steps) + len(state.pending_steps)}")

    # Execute remaining steps
    for step in state.pending_steps:
        print(f"[Step {state.current_step + 1}] {step}")

        try:
            result = execute_step(step, state.context)

            # Update state
            state.completed_steps.append({
                "step": state.current_step + 1,
                "description": step,
                "result": result,
                "timestamp": datetime.now().isoformat()
            })
            state.current_step += 1
            state.context.update(result)

            # Save intermediate state
            state_manager.save_state(state)

        except Exception as e:
            print(f"Step failed: {e}")
            state.status = "failed"
            state_manager.save_state(state)
            raise

    state.status = "completed"
    state_manager.save_state(state)

    return generate_final_answer(state.context, state.goal)
