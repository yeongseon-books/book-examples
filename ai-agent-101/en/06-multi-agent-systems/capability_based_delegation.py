"""Generated from book-content article."""

from typing import Set

class CapabilityRegistry:
    """Capability registry."""

    def __init__(self):
        self.agent_capabilities: Dict[str, Dict[str, float]] = {}

    def register(self, agent_name: str, capabilities: Dict[str, float]) -> None:
        """Register an agent's capabilities (capability name → proficiency 0.0-1.0)."""
        self.agent_capabilities[agent_name] = capabilities

    def find_best_agent(
        self,
        required_capabilities: Set[str],
        min_proficiency: float = 0.5
    ) -> Optional[str]:
        """Find the agent best matching the required capabilities."""
        best_agent = None
        best_score = 0.0

        for agent, caps in self.agent_capabilities.items():
            # Calculate average proficiency on required capabilities
            scores = [
                caps.get(cap, 0.0) for cap in required_capabilities
                if caps.get(cap, 0.0) >= min_proficiency
            ]
            if len(scores) == len(required_capabilities):
                avg_score = sum(scores) / len(scores)
                if avg_score > best_score:
                    best_score = avg_score
                    best_agent = agent

        return best_agent

# Example usage
registry = CapabilityRegistry()
registry.register("AgentA", {
    "python": 0.9,
    "machine_learning": 0.7,
    "data_analysis": 0.8
})
registry.register("AgentB", {
    "python": 0.95,
    "machine_learning": 0.9,
    "deep_learning": 0.85
})

required = {"python", "machine_learning"}
best = registry.find_best_agent(required)
# Picks AgentB (python: 0.95, machine_learning: 0.9)
