"""Generated from book-content article."""

def require_policy_review(branch: str, teacher_name: str, review_ticket: str | None) -> None:
    if branch != "distillation":
        return
    if not review_ticket:
        raise RuntimeError(
            f"Stop: review output-usage rights for {teacher_name} before creating a distillation dataset."
        )

require_policy_review(
    branch="distillation",
    teacher_name="OpenAI API model",
    review_ticket=None,  # must be populated by legal/policy review
)
