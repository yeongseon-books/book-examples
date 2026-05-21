"""Generated from book-content article."""

from typing import Protocol


class WorkflowStep(Protocol):
    """Workflow step interface"""

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute step"""
        ...

    def validate(self, result: Dict[str, Any]) -> bool:
        """Validate result"""
        ...

class DataCollectionStep:
    """Data collection step"""

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Collect data from web"""
        url = context["url"]
        data = scrape_website(url)
        return {"collected_data": data}

    def validate(self, result: Dict[str, Any]) -> bool:
        """Check data is not empty"""
        return "collected_data" in result and len(result["collected_data"]) > 0

class DataAnalysisStep:
    """Data analysis step"""

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze collected data"""
        data = context["collected_data"]
        insights = analyze_data(data)
        return {"insights": insights}

    def validate(self, result: Dict[str, Any]) -> bool:
        """Check insights were generated"""
        return "insights" in result

# Assemble workflow
workflow_steps = [
    DataCollectionStep(),
    DataAnalysisStep()
]

def run_modular_workflow(context: Dict[str, Any]) -> Dict[str, Any]:
    """Execute modular workflow"""
    for step in workflow_steps:
        result = step.execute(context)

        if not step.validate(result):
            raise ValueError(f"Step validation failed: {step.__class__.__name__}")

        context.update(result)

    return context
