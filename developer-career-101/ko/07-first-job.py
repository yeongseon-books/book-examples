def onboarding_plan(role: str) -> dict:
    return {
        "role": role,
        "30": ["codebase tour", "glossary", "shadow on-call"],
        "60": ["question log", "first small fix", "weekly 1:1"],
        "90": ["ship scoped feature", "retro", "growth goals"],
    }


def validate_onboarding(plan: dict) -> bool:
    return all(k in plan and len(plan[k]) >= 2 for k in ["30", "60", "90"])
