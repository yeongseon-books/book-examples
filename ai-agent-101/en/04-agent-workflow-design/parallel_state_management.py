"""Generated from book-content article."""

import asyncio
from typing import List

class ParallelStateManager:
    """Parallel task state management"""
    
    def __init__(self):
        self.subtask_states: Dict[str, AgentState] = {}
    
    async def execute_parallel_tasks(
        self,
        tasks: List[str],
        parent_task_id: str
    ) -> Dict[str, Any]:
        """Execute parallel tasks and track states"""
        
        # Create state for each subtask
        for idx, task in enumerate(tasks):
            subtask_id = f"{parent_task_id}_sub_{idx}"
            self.subtask_states[subtask_id] = AgentState(
                task_id=subtask_id,
                goal=task,
                current_step=0,
                completed_steps=[],
                pending_steps=[task],
                context={},
                status="pending",
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
        
        # Execute in parallel
        results = await asyncio.gather(*[
            self.execute_subtask(subtask_id)
            for subtask_id in self.subtask_states.keys()
        ])
        
        # Aggregate results
        return {
            subtask_id: result
            for subtask_id, result in zip(self.subtask_states.keys(), results)
        }
    
    async def execute_subtask(self, subtask_id: str) -> Any:
        """Execute subtask"""
        state = self.subtask_states[subtask_id]
        state.status = "running"
        
        try:
            result = await async_execute_step(state.goal)
            state.status = "completed"
            return result
        except Exception as e:
            state.status = "failed"
            raise
