import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from common import mock_log_rows


def revision_error_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in mock_log_rows():
        if "ERROR" in row["Log_s"]:
            revision = row["RevisionName_s"]
            counts[revision] = counts.get(revision, 0) + 1
    return counts


def kql_examples(app_name: str) -> list[str]:
    return [
        f'ContainerAppConsoleLogs_CL | where ContainerAppName_s == "{app_name}" | top 100 by TimeGenerated desc',
        f'ContainerAppConsoleLogs_CL | where ContainerAppName_s == "{app_name}" and Log_s contains "ERROR" | summarize ErrorCount=count() by RevisionName_s',
        f'ContainerAppSystemLogs_CL | where ContainerAppName_s == "{app_name}" and Log_s contains "Scal"',
    ]


def run() -> dict[str, object]:
    return {"errors": revision_error_counts(), "kql": kql_examples("fastapi-aca-demo")}


if __name__ == "__main__":
    print(run())
