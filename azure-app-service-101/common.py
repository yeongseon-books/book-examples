"""Shared utilities and domain models for Azure App Service 101."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AzCommand:
    """Az command."""

    args: list[str]

    def as_string(self) -> str:
        """As string."""
        return " ".join(self.args)


def build_webapp_show_command(resource_group: str, app_name: str) -> AzCommand:
    """Build webapp show command."""
    return AzCommand(
        [
            "az",
            "webapp",
            "show",
            "--resource-group",
            resource_group,
            "--name",
            app_name,
            "--query",
            "{state:state,hostNames:hostNames,httpsOnly:httpsOnly}",
            "--output",
            "json",
        ]
    )
