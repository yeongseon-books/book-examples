"""Generated from book-content article."""

import logging
from datetime import datetime


class ObservableWorkflow:
    """Observable workflow"""

    def __init__(self, workflow_id: str):
        self.workflow_id = workflow_id
        self.logger = logging.getLogger(f"workflow.{workflow_id}")
        self.trace = []

    def execute(self, steps: List[str]) -> Any:
        """Traceable execution"""
        self.logger.info(f"Workflow {self.workflow_id} started")
        start_time = datetime.now()

        for idx, step in enumerate(steps):
            step_start = datetime.now()

            try:
                self.logger.info(f"[Step {idx+1}] Starting: {step}")
                result = execute_step(step)

                duration = (datetime.now() - step_start).total_seconds()

                self.trace.append({
                    "step": idx + 1,
                    "description": step,
                    "status": "success",
                    "duration": duration,
                    "result": result
                })

                self.logger.info(f"[Step {idx+1}] Completed in {duration}s")

            except Exception as e:
                duration = (datetime.now() - step_start).total_seconds()

                self.trace.append({
                    "step": idx + 1,
                    "description": step,
                    "status": "failed",
                    "duration": duration,
                    "error": str(e)
                })

                self.logger.error(f"[Step {idx+1}] Failed: {e}")
                raise

        total_duration = (datetime.now() - start_time).total_seconds()
        self.logger.info(f"Workflow completed in {total_duration}s")

        return self.trace
