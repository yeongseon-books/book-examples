"""Generated from book-content article."""

import time


class LoadBalancingDelegator:
    """Load-based delegator."""

    def __init__(self):
        self.agent_loads: Dict[str, int] = {}
        self.agent_max_capacity: Dict[str, int] = {}
        self.lock = threading.Lock()

    def register(self, agent_name: str, max_capacity: int = 10) -> None:
        """Register an agent."""
        with self.lock:
            self.agent_loads[agent_name] = 0
            self.agent_max_capacity[agent_name] = max_capacity

    def assign_task(self, task_id: str) -> Optional[str]:
        """Assign a task to the agent with the lightest load."""
        with self.lock:
            available_agents = [
                (name, load) for name, load in self.agent_loads.items()
                if load < self.agent_max_capacity[name]
            ]
            if not available_agents:
                return None
            # Pick the agent with the lowest load
            selected = min(available_agents, key=lambda x: x[1])[0]
            self.agent_loads[selected] += 1
            return selected

    def complete_task(self, agent_name: str) -> None:
        """Mark a task as completed."""
        with self.lock:
            if agent_name in self.agent_loads and self.agent_loads[agent_name] > 0:
                self.agent_loads[agent_name] -= 1

# Example usage
balancer = LoadBalancingDelegator()
balancer.register("AgentA", max_capacity=5)
balancer.register("AgentB", max_capacity=5)
balancer.register("AgentC", max_capacity=5)

# Process several tasks concurrently
for i in range(10):
    agent = balancer.assign_task(f"task_{i}")
    print(f"Task {i} assigned to {agent}")
    # ... actually run the task ...
    # balancer.complete_task(agent)
