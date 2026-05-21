"""Github Actions 101 - Episode 3: triggers example."""

from common import WorkflowParser, WorkflowValidator, load_workflow


def main() -> None:
    """Main."""
    wf = load_workflow(
        __file__.replace("step01_demo.py", ".github/workflows/workflow.yml")
    )
    parsed = WorkflowParser().parse(wf)
    issues = WorkflowValidator().validate(wf)
    print(parsed["name"], len(parsed["jobs"]), len(issues))


if __name__ == "__main__":
    main()
