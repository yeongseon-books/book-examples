"""Generated from book-content article."""

import json
import redis

class StateManager:
    """State manager"""
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    def save_state(self, state: AgentState) -> None:
        """Save state"""
        key = f"agent_state:{state.task_id}"
        value = json.dumps(state.to_dict())
        
        # Save to Redis (1 hour TTL)
        self.redis.setex(key, 3600, value)
    
    def load_state(self, task_id: str) -> AgentState:
        """Load state"""
        key = f"agent_state:{task_id}"
        value = self.redis.get(key)
        
        if not value:
            raise ValueError(f"State not found for task {task_id}")
        
        data = json.loads(value)
        return AgentState(
            task_id=data["task_id"],
            goal=data["goal"],
            current_step=data["current_step"],
            completed_steps=data["completed_steps"],
            pending_steps=data["pending_steps"],
            context=data["context"],
            status=data["status"],
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"])
        )
    
    def update_state(self, task_id: str, updates: Dict[str, Any]) -> None:
        """Update state"""
        state = self.load_state(task_id)
        
        for key, value in updates.items():
            setattr(state, key, value)
        
        state.updated_at = datetime.now()
        self.save_state(state)
