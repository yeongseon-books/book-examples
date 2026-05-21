"""Generated from book-content article."""

import random

class CanaryRouter:
    """Route a fraction of traffic to a new version."""

    def __init__(self, canary_percentage: float = 0.05):
        self.canary_percentage = canary_percentage
        self.versions = {"stable": None, "canary": None}

    def register(self, version: str, agent):
        self.versions[version] = agent

    def route(self, request) -> tuple:
        if (self.versions["canary"] and
            random.random() < self.canary_percentage):
            return self.versions["canary"], "canary"
        return self.versions["stable"], "stable"

    def adjust_canary(self, percentage: float):
        self.canary_percentage = max(0.0, min(1.0, percentage))

# Example usage
router = CanaryRouter(canary_percentage=0.05)  # 5% canary
router.register("stable", agent_v1)
router.register("canary", agent_v2)

agent, version = router.route(user_request)
result = agent.run(user_request)
metrics.increment("agent.requests", version=version)
