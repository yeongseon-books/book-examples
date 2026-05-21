"""Generated from book-content article."""

class RoleBasedDelegator:
    """Role-based delegator."""

    def __init__(self):
        self.agents_by_role: Dict[str, List[str]] = defaultdict(list)
        self.agent_capabilities: Dict[str, Dict] = {}

    def register(self, agent_name: str, roles: List[str], capabilities: Dict) -> None:
        """Register an agent."""
        for role in roles:
            self.agents_by_role[role].append(agent_name)
        self.agent_capabilities[agent_name] = capabilities

    def find_agent_for_task(self, task: Dict) -> Optional[str]:
        """Find an appropriate agent for the task."""
        required_role = task.get("required_role")
        if required_role and required_role in self.agents_by_role:
            candidates = self.agents_by_role[required_role]
            # Pick the agent with best capability match
            best_agent = None
            best_score = -1
            for agent in candidates:
                score = self._calculate_match_score(
                    self.agent_capabilities[agent],
                    task.get("requirements", {})
                )
                if score > best_score:
                    best_score = score
                    best_agent = agent
            return best_agent
        return None

    def _calculate_match_score(self, capabilities: Dict, requirements: Dict) -> float:
        """Calculate the capability match score."""
        if not requirements:
            return 1.0
        matches = sum(
            1 for k, v in requirements.items()
            if capabilities.get(k) == v
        )
        return matches / len(requirements)

# Example usage
delegator = RoleBasedDelegator()
delegator.register("DocWriter", ["documentation"], {"language": "ko", "format": "markdown"})
delegator.register("CodeWriter", ["coding"], {"language": "python", "framework": "fastapi"})

task = {
    "required_role": "documentation",
    "requirements": {"language": "ko", "format": "markdown"}
}
selected = delegator.find_agent_for_task(task)
# Identifies "documentation" role → delegates to DocWriter
