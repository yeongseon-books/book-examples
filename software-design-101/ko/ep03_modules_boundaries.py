from types import ModuleType

__all__ = ["public_api", "get_public_exports", "can_import"]


def _internal_helper() -> str:
    return "internal"


def public_api() -> str:
    return "public:" + _internal_helper()


def get_public_exports(module: ModuleType) -> list[str]:
    return list(getattr(module, "__all__", []))


def can_import(name: str, module: ModuleType) -> bool:
    return name in get_public_exports(module)
