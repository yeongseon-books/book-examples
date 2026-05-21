"""Generated from book-content article."""

class FeatureFlags:
    """Feature flags."""

    def __init__(self):
        self._flags = {}

    def set(self, name: str, enabled: bool):
        self._flags[name] = enabled

    def is_enabled(self, name: str, user_id: Optional[str] = None) -> bool:
        return self._flags.get(name, False)

# Example usage
flags = FeatureFlags()
flags.set("use_new_planning", False)

def plan_task(task):
    if flags.is_enabled("use_new_planning"):
        return new_planner(task)
    return legacy_planner(task)
