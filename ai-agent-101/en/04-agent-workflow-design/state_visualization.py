"""Generated from book-content article."""

def visualize_state(state: AgentState) -> str:
    """Visualize state"""
    total_steps = len(state.completed_steps) + len(state.pending_steps)
    progress = (state.current_step / total_steps) * 100 if total_steps > 0 else 0
    
    # Progress bar
    bar_length = 40
    filled = int(bar_length * progress / 100)
    bar = "=" * filled + "-" * (bar_length - filled)
    
    output = f"""
=== Agent Workflow Status ===
Task ID: {state.task_id}
Goal: {state.goal}
Status: {state.status}
Progress: [{bar}] {progress:.1f}%

Completed Steps ({len(state.completed_steps)}):
{format_steps(state.completed_steps)}

Pending Steps ({len(state.pending_steps)}):
{format_pending(state.pending_steps)}
    """
    
    return output
