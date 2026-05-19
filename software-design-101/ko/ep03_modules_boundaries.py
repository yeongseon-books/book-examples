"""Software Design 101 - Episode 3: Modules boundaries."""

from types import ModuleType

__all__ = ["public_api", "get_public_exports", "can_import"]


def _internal_helper() -> str:
    """Internal helper."""
    return "internal"


def public_api() -> str:
    """Public api."""
    return "public:" + _internal_helper()


def get_public_exports(module: ModuleType) -> list[str]:
    """Get public exports."""
    return list(getattr(module, "__all__", []))


def can_import(name: str, module: ModuleType) -> bool:
    """Can import."""
    return name in get_public_exports(module)
